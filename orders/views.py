import stripe
# needed for secondary pass back tokenize CC bakc to stripe to charge
from django.conf import settings # new for stripe variable pass page 276 dj pro book
from django.contrib.auth.models import Permission # update permissions after purchase to give access

from django.views.generic.base import TemplateView
from django.shortcuts import render # for stripe final steps to charge 

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context



def charge(request):  #for stripe charge 
    #get permissions
    permission = Permission.objects.get(codename='special_status')



    # GetUse

    u = request.user

    #add to user's permissions to access books

    u.user_permissions.add(permission)


    if request.method == 'POST':
        charge = stripe.Charge.create(
                amount=3900,
                currency='usd',
                description='Purchase all books',
                source=request.POST['stripeToken']
            )
    return render(request, 'orders/charge.html')
# Create your views here.
