from django.core.context_processors import csrf

from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response
from forms import ContactForm

from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd.get('email', 'noreply@example.com')+"   says:\n"+cd['message'],
                'magicblogemail@gmail.com',
                ['tylovemx@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    c = {'form': form}
    c.update(csrf(request))
    return render_to_response('contact_form.html', c)
