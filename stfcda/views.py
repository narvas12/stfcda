# views.py in your journalapp


from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponseServerError
from core import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from stfcda.form import JournalfilesForm, NominationForm
from stfcda.form import NominationForm
from .models import Contact, Journal, Journalfiles, Members, Todos, VolunteerApplication
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings

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
    return render(request, 'vol.html')


def thank_you_page(request):
    return render(request, 'thank_you.html')



def volunteer_application(request):
    if request.method == 'POST':
        # Extracting data from the submitted form
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name', '')
        surname = request.POST.get('surname')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        skills = request.POST.get('skills')
        position = request.POST.get('position')
        why_volunteer = request.POST.get('why_volunteer')
        fit_for_position = request.POST.get('fit_for_position')
        resume = request.FILES.get('resume')

        # Save the data to the VolunteerApplication model
        application = VolunteerApplication(
            first_name=first_name,
            middle_name=middle_name,
            surname=surname,
            phone_number=phone_number,
            email=email,
            skills=skills,
            position=position,
            why_volunteer=why_volunteer,
            fit_for_position=fit_for_position,
            resume=resume
        )
        application.save()

        # Send email with application details
        send_application_email(application)

        # Redirect to a success page or any other desired page after successful submission
        return HttpResponseRedirect('thank-you')  # Update the URL as needed

    # If the request method is GET, render the form template
    position_choices = VolunteerApplication.POSITION_CHOICES
    return render(request, 'apply.html', {'position_choices': position_choices})



def send_application_email(application):
    subject = 'New Volunteer Application'

    # Prepare the message content
    message = render_to_string('application_email.txt', {'application': application})

    # Attach the resume file
    resume_content = application.resume.read()
    resume_name = application.resume.name
    email = EmailMessage(subject, message, to=['volunteer@stfcda.org'], from_email='volunteer@stfcda.org')
    email.attach(resume_name, resume_content, 'application/pdf')  # Adjust the content type based on your file type
    email.send()
    
    
# def send_application_email(application):
#     subject = 'New Volunteer Application'
#     message = f'A new volunteer application has been submitted.\n\nDetails:\n\n' \
#               f'First Name: {application.first_name}\n' \
#               f'Middle Name: {application.middle_name}\n' \
#               f'Surname: {application.surname}\n' \
#               f'Phone Number: {application.phone_number}\n' \
#               f'Email: {application.email}\n' \
#               f'Skills: {application.skills}\n' \
#               f'Position: {application.get_position_display()}\n' \
#               f'Why Volunteer: {application.why_volunteer}\n' \
#               f'Fit for Position: {application.fit_for_position}\n' \
#               f'Home Address: {application.home_address}\n'

#     from_email = settings.DEFAULT_FROM_EMAIL  # Update with your email
#     recipient_list = ['volunteer@stfcda.org']  # Update with your admin email or a list of recipients

#     send_mail(subject, message, from_email, recipient_list)
