from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ContributionForm
from features.models import Feature
from django.contrib import messages

def view_cart(request):
    """ A view that renders the cart contents page """
    try:
        return render(request, "cart/cart.html")
    
    except Exception as e:
        print(e)
        return render(request, 'error.html')
    
def contribution_amount(request, id):
    try:
        feature = get_object_or_404(Feature, pk=id)
        contribution_form = ContributionForm(request.POST)
        context = {"contribution_form": contribution_form, "feature": feature}
        return render(request, "cart/contribution_amount.html", context)
    
    except Exception as e:
        print(e)
        return render(request, 'error.html')
    
    
    
def add_to_cart(request, id):
    """Add a donation of the specified products to the cart"""
    try:
        contribution=int(request.POST.get('contribution'))
        cart = request.session.get('cart', {})
        cart[id] = cart.get(id, contribution)
        
        request.session['cart'] = cart
        return redirect(reverse('view_cart'))
    
    except Exception as e:
        print(e)
        return render(request, 'error.html')

def adjust_cart(request, id):
    """Adjust the donation of the specified product to the specified amount"""
    try:
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
    
    except Exception as e:
        print(e)
        return render(request, 'error.html')