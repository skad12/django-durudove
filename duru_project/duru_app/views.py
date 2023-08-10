from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail


def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        Dtype = request.POST['Dtype']
        message = request.POST['message']

        # send a mail

        # send_mail(
        #     'Durudove Tour Schedule from ' + name,  # subject
        #     message,  # contactform  message
        #     email,  # from email
        #     ['stephenkunle26@gmail.com', 'dammykunle79@gmail.com']  # to email

        # )

        return render(request, 'home.html', {'name': name, 'email': email, 'Dtype': Dtype, 'mobile': mobile, 'message': message})

    else:
        return render(request, 'home.html')
