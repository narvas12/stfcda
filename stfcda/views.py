# views.py in your journalapp

from core import settings
from django.shortcuts import redirect, render
from django.views.generic import ListView  #, CreateView, UpdateView, DeleteView
from .models import Contact, Journal, Members, Todos
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail


def home(request):
    events  =  Todos.objects.all()
    
    return render(request, 'index.html', {'events': events})


def about(request):
    return render(request, 'about.html')


def active_members(request):
    # Retrieve all active members (is_member=True and is_active=True) excluding trustees (is_trustee=True)
    members = Members.objects.filter(is_member=True, is_active=True)

    context = {
        'members': members
    }

    return render(request, 'members.html', context)



def contact(request):
    if request.method == 'POST':
        try:
            full_name = request.POST['name']
            email = request.POST['email']
            company_name = request.POST['company-name']
            message = request.POST['message']

            # Validate form data (you can add more validation logic as needed)

            # Create Contact instance and save to the database
            user_contact = Contact(full_name=full_name, email=email, company_name=company_name, message=message)
            user_contact.save()

            # Send email
            send_mail(
                'New Contact Form Submission',
                f'Name: {full_name}\nEmail: {email}\nCompany Name: {company_name}\nMessage: {message}',
                settings.EMAIL_HOST_USER,  
                ['ebukaemmanuel71@gmail.com'],  
                fail_silently=False,
            )

            # Add success message
            messages.success(request, 'Your message has been sent successfully!')
            
            return redirect('contact_us')  # Redirect to the contact page or another page

        except KeyError:
            # Handle missing form field errors
            messages.error(request, 'Please fill out all the required fields.')

        except Exception as e:
            # Handle other errors
            messages.error(request, f'An error occurred: {str(e)}')

    return render(request, 'contact.html')  # Render the contact page with error messages




def projects(request):
    return render(request, 'projects.html')


class JournalListView(ListView):
    model = Journal
    template_name = 'journals.html'
    context_object_name = 'journals'


def trustees_list(request):
    trustees = Members.objects.filter(is_active=True, is_trustee=True).order_by('-id')
    context = {'trustees': trustees}
    return render(request, 'trustees_list.html', context)

def view_trustee(request, slug):
    trustee = Members.objects.get(slug=slug)
    return render(request, 'trustee.html', {'trustee': trustee})

