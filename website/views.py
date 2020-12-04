from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):

    context = {

    }

    return render(request, 'website/index.html', context)


def contact(request):

    if request.method == 'POST':
        # Do stuff
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # Send an email
        send_mail(

            f'{message_name} Appointment', # Subject
            message, # Message
            message_email, # From Email
            ['jpinedude63@gmail.com', 'jpine4@hotmail.com'], # To Email

        )

        context = {
            'name' : message_name,
        }

        return render(request, 'website/contact.html', context)
        
    else:

        context = {

        }

        return render(request, 'website/contact.html', context)


def about(request):

    context = {

    }

    return render(request, 'website/about.html', context)


def pricing(request):

    context = {

    }

    return render(request, 'website/pricing.html', context)


def service(request):

    context = {

    }

    return render(request, 'website/service.html', context)


def appointment(request):

    if request.method == 'POST':
        # Get the data from the form
        name = request.POST['your-name']
        phone = request.POST['your-phone']
        email = request.POST['your-email']
        address = request.POST['your-address']
        date = request.POST['your-date']
        time = request.POST['your-time']
        message = request.POST['your-message']

        appointment_message = f'{name} {phone} {email} has requested an appointment for {date} {time}. With the message of {message}. Their address is {address}'

        context = {
            'name' : name,
            'phone' : phone,
            'email' : email,
            'address' : address,
            'date' : date,
            'time' : time,
            'message' : message,
        }

        send_mail(

            f'{name} Appointment Request', # Subject
            appointment_message, # Message
            email, # From Email
            ['jpinedude63@gmail.com', 'jpine4@hotmail.com'], # To Email

        )

        return render(request, 'website/appointment.html', context)
        
    else:

        context = {

        }

        return render(request, 'website/home.html', context)
