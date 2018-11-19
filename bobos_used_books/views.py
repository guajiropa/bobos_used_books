"""
AUTHOR      :   Robert James Patterson
DATE        :   11/10/2018
SYNOPSIS    :   Work-thru file for 'Mastering Django: Core'
"""
from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from bobos_used_books.forms import ContactForm


def hello(request):
    return HttpResponse("Hello Django World!")


def index(request):
    return HttpResponse("This is where your homepage belongs!")


def current_datetime(request):
    now = datetime.now()
    return render(request, 'current_datetime.html', {'current_datetime': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
   
    dt = datetime.now() + timedelta(hours=offset)
    
    return render(request, 'hours_ahead.html', 
            {'hours_offset': offset, 'next_time': dt})


def display_meta(request):
    values = request.META.items()
    #values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
    

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'nereply@bobosusedbooks.org'),
                ['siteowner@bobosusedbooks.org'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'We just love this site!'})
    
    return render(request, 'contact_form.html', {'form': form})
