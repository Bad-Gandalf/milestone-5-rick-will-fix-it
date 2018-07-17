from django.shortcuts import render, redirect, reverse

def view_cart(request):
    """ A view that renders the cart contents page """
    return render(request, "cart.html")
    
def add_to_cart(request, id):
    """Add a donation of the specified products to the cart"""
    contribution=int(request.POST.get('contribution'))
    
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, contribution)
    
    request.session['cart'] = cart
    return redirect(reverse('index'))

def adjust_cart(request):
    """Adjust the donation of the specified product to the specified amount"""
    contribution = int(request.POST.get('contribution'))
    cart = request.session.get('cart', {})
    
    if contribution > 0:
        cart[id] = contribution
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))