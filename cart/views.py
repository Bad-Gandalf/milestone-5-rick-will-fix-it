from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ContributionForm
from features.models import Feature
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def view_cart(request):
    """ A view that renders the cart contents page """
    return render(request, "cart/cart.html")


@login_required    
def contribution_amount(request, id):
    """As users choose the amount they wish to contribute, I have created a 
    contribution form to validate the amount, ie. it needs to be at least €10."""
    feature = get_object_or_404(Feature, pk=id)
    contribution_form = ContributionForm(request.POST)
    context = {"contribution_form": contribution_form, "feature": feature}
    return render(request, "cart/contribution_amount.html", context)
    
@login_required    
def add_to_cart(request, id):
    """Add a donation of the specified products to the cart"""
    
    contribution=int(request.POST.get('contribution'))
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, contribution)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
    
@login_required
def adjust_cart(request, id):
    """Adjust the donation of the specified product to the specified amount.
    It will also check again to see if the amount meets the threshold """
    
    contribution = int(request.POST.get('contribution'))
    if contribution < 10:
        messages.error(request, 'Contributions must be at least €10')
        return redirect(reverse('view_cart'))
    cart = request.session.get('cart', {})
    
    if contribution > 0:
        cart[id] = contribution
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

@login_required    
def empty_cart(request, id):
    """Get the cart and delete it."""
    request.session['cart'] = request.session.get('cart', {})
    del request.session['cart']
    messages.error(request, "You have successfully emptied your cart!")
    return redirect(reverse('view_cart'))
    