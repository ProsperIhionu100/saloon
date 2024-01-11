from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Employee, Service, why_us, About
from django.core.paginator import Paginator
# Create your views here.

def HomePage(request):
    employees = Employee.objects.all()
    img2 = why_us.objects.get(img1="stylist-1_dopPnFb.png")
    page = 1
    results = 3
    paginator = Paginator(employees, results)
    
    employees = paginator.page(page)
    
    
    context = {'employees':employees, 'img2':img2}
    return render(request, 'base/index.html', context)

def AboutPage(request):
    employees = Employee.objects.all()
    about1 = About.objects.get(image="about-us-image_eTLieSW.jpg")
    context = {'employees':employees, 'about1':about1}
    return render(request, 'base/about.html', context)

def Service2Page(request):
    services = Service.objects.all()
    context = {'services':services}
    return render(request, 'base/service-2-col.html', context)

def Service3Page(request):
    services = Service.objects.all()
    
    page = 1
    page2 = 2
    results = 3
    paginator = Paginator(services, results)
    paginator1 = Paginator(services, results)
    
    services = paginator.page(page)
    services2 = paginator1.page(page2)
    
    context = {'services':services, 'services2':services2}
    return render(request, 'base/service-3-col.html', context)

def SingleService(request):
    service = Service.objects.get(Title="Shaves and Hot Towels")
    service1 = service.employee_set.get(name="Carkson")
    service2 = service.price_set.get(price_service="Hair Cut")
    context = {'service':service, 'service1':service1, 'service2':service2}
    return render(request, 'base/single-service.html', context)

def BookingPage(request):
    employees = Employee.objects.all()
    context = {'employees':employees}
    return render(request, 'base/booking.html', context)

def contactPage(request):
    
    if request.POST == 'POST':
        email = request.POST['email']
        
        
        subject = 'Welcome to our Newsletter'
        message = 'Thank you for subscribing to our newsletter!'
        from_email = 'prosperbiz720@gmail.com'
        to_email = [email]
        send_mail(subject, message, from_email, to_email, fail_silently=False)
        
        return redirect('contact') 
    
    return render(request, 'base/contact-1.html')