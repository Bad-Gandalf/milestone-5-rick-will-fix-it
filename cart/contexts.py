from django.shortcuts import get_object_or_404
from features.models import Feature


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """
    
    cart= request.session.get('cart', {})
    
    cart_items = []
    total = 0
    
    for id, contribution in cart.items():
        feature = get_object_or_404(Feature, pk=id)
        total += contribution
        
        cart_items.append({'id': id, 'contribution': contribution, 'feature': feature})

    return { 'cart_items': cart_items, 'total': total} 