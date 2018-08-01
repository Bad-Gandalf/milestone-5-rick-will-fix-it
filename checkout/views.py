from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm, ContributionForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from features.models import Feature
import stripe

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method =="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        contribution_form = ContributionForm(request.POST)
    
        
        if order_form.is_valid() and payment_form.is_valid() and contribution_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            
            contribution = request.POST.get('contribution')
            
            feature = get_object_or_404(Feature, pk=request.feature.id)
            total = contribution
            user = request.user
            order_line_item = OrderLineItem(user = user,
                                            order = order,
                                            feature = feature, 
                                            contribution = total,
                                            )
            order_line_item.save()
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                    )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
                
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        
    return render(request, "checkout/checkout.html", {"order_form": order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})