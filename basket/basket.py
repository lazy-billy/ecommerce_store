


class Basket():
    """
    A class providing some default behaviour that can be inherited or overrited.
    """

    def __init__(self, request):
        
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {'number':65768}
        self.basket = basket