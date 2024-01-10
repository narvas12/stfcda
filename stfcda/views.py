# views.py in your journalapp

from core import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from stfcda.form import JournalfilesForm, NominationForm

from stfcda.form import NominationForm

  #, CreateView, UpdateView, DeleteView
from .models import Contact, Journal, Journalfiles, Members, Nomination, Todos
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





def nominate_member(request):
    if request.method == 'POST':
        form = NominationForm(request.POST)
        if form.is_valid():
            nomination = form.save()

            # Check if the person has already made a nomination
            nominated_member = nomination.member
           
          
            # Update is_nominated to True in the Members model
            nominated_member.is_nominated = True
            nominated_member.save()

            # Send email notification
            subject = 'New Nomination'
            message = f'New nomination for {nominated_member.full_name}.\nReason: {nomination.n_reason}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['your@email.com']  

            send_mail(subject, message, from_email, recipient_list)

            # Display success message
            messages.success(request, f'Your nomination for {nominated_member.full_name} was submitted successfully! \n Please Do not make another nomination Thank You')

            # Reset the form for a new nomination
            form = NominationForm()

    else:
        form = NominationForm()

    return render(request, 'nominate.html', {'form': form})



def upload_journal(request):
    if request.method == 'POST':
        form = JournalfilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'upload success')
            return redirect('upload_journal')
    else:
        form = JournalfilesForm()
    return render(request, 'upload_journal.html', {'form': form})


def delete_journal(request, pk):
    file_to_delete = get_object_or_404(Journalfiles, pk=pk)
    
    if request.method == 'POST':
        file_to_delete.delete()
        messages.success(request, 'File deleted successfully')
        return redirect('file_list')
    
    return render(request, 'delete_journal.html', {'file': file_to_delete})


def edit_journal(request, pk):
    file_to_edit = get_object_or_404(Journalfiles, pk=pk)
    
    if request.method == 'POST':
        form = JournalfilesForm(request.POST, request.FILES, instance=file_to_edit)
        if form.is_valid():
            form.save()
            messages.success(request, 'File updated successfully')
            return redirect('file_list')
    else:
        form = JournalfilesForm(instance=file_to_edit)
    
    return render(request, 'edit_journal.html', {'form': form, 'file': file_to_edit})






def file_list(request):
    files = Journalfiles.objects.all()
    return render(request, 'files.html', {'files': files})

def volunteer(request):
    return render(request, volunteer.html)