from django.conf import settings
from store.models import Articulos
from store.views import get_prices
from decimal import Decimal
from time import sleep

class Cart(object):
    def __init__(self,request):
        """
            Inicializacion de carrito
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            #Guarda el carrito vacio en la sesion
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session.modified = True

    def add(self,product,quantity=1,change_quantity=False):
        """
            Anade un producto al carrito
        """
        product_id = str(product.IdArticulo)
        price = get_prices(pIdListaPrecio=3,pIdArticulo=product.IdArticulo)[0]['PrecioArticulo']
        if product_id not in self.cart:
            self.cart[product_id] = {'cantidad': 0,
                                     'precio': str(price)}
        if change_quantity:
            self.cart[product_id]['cantidad'] = quantity
        else:
            self.cart[product_id]['cantidad'] += quantity

        self.save()

    def remove(self,product):
        product_id = str(product.IdArticulo)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):

        """
            Iterar sobre los articulos en el carrito y
            obtenerlos de la base de datos
        """

        ids_products = self.cart.keys()
        products = Articulos.objects.filter(IdArticulo__in=ids_products)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.IdArticulo)]['producto'] = product
        for item in cart.values():
            item['precio'] = Decimal(item['precio'])
            item['precio_total'] = item['precio'] * item['cantidad']
            yield item

    def __len__(self):
        """
            Conteo de productos en el carrito
        """
        return sum(item['cantidad'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['precio']) * item['cantidad']
                    for item in self.cart.values())

    def clean_cart(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
