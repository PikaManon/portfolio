from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from portfolio.forms import ContactForm
from django.shortcuts import redirect


# Create your views here.
def home(request):
    #return HttpResponse("This is my homepage (/)")


    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send an email
            send_mail(
                f'From {email}, Subject: {subject}',
                f'Message: {message}',
                email,  # From email
                [settings.ADMIN_EMAIL],  # To email
                fail_silently=False,
            )
            return redirect('home')
    else:
        form = ContactForm()

        #message = request.POST.get('message')
        #print(message)
        #email = request.POST.get('email')
        #print(email)
        #name = request.POST.get('name')
        #print(name)
        #send_mail('Contact Form'+str(name), message, email, ['manonsamson2001@gmail.com'], fail_silently=False)

    return render(request, 'home/home.html', {'form': form})


