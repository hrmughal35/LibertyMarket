from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User
from .forms import Query
from django.core.mail import send_mail
import logging
# Create your views here.


def home(request):
    return render(request, 'Market/home.html')

def explore(request):
    return render(request, 'Market/explore.html')

# def details(request):
#     return render(request, 'Market/details.html')

def about(request):
    return render(request, 'Market/about.html')


logger = logging.getLogger(__name__)
def contact(request):
    if request.method=="POST":
        fm=Query(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pn=fm.cleaned_data['phone']
            cm=fm.cleaned_data['comments']
            reg=User(name=nm, email=em, phone=pn, comments=cm)
            reg.save()
            fm=Query()
            
            try:
                # Attempt to send the email
                send_mail(
                    'Liberty Market',
                    'Thank you for contacting us. We will get back to you soon.',
                    'Liberty Market',
                    ['bannuccillc@gmail.com'],
                    fail_silently=False
                )
                logger.info("Email sent successfully to: %s" % em)
            except Exception as e:
                # Log any exceptions raised during sending email
                logger.error("Error sending email: %s" % str(e))
                # Print the exception if you're running Django in development mode
                print("Error sending email:", e)
            
    else:
        fm =Query()
    return render(request, "Market/contact.html", {"forms": fm}) 

