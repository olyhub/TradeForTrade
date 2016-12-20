from django.shortcuts import redirect
from accounts.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def email(request):
   if request.method == 'GET':
       form = ContactForm()
   else:
       form = ContactForm(request.POST)
       if form.is_valid():
           subject = form.cleaned_data['subject']
           from_email = form.cleaned_data['from_email']
           message = form.cleaned_data['message']
           try:
               send_mail(subject, message, from_email, ['testing@example.com'])
           except BadHeaderError:
               return HttpResponse('Invalid header found.')
           return redirect('thanks')
   return render(request, "contact.html", {'form': form})

def thanks(request):
   return render(request, 'thanks.html')