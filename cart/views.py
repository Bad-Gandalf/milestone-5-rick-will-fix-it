from django.shortcuts import render, redirect, reverse

def view_cart(request):
    """ A view that renders the cart contents page """
    return render(request, "cart.html")
    
def add_to_cart(request, id):
    """Add a donation of the specified products to the cart"""
    donation=int(request.POST.get('donation'))
    
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, donation)
    
    request.session['cart'] = cart
    return redirect(reverse('index'))

def adjust_cart(request):
    """Adjust the donation of the specified product to the specified amount"""
    donation = int(request.POST.get('donation'))
    cart = request.session.get('cart', {})
    
    if donation > 0:
        cart[id] = donation
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))