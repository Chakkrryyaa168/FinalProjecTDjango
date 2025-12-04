from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Views currently used in your urls.py (kept as-is for now)
def home(request):
    # This might eventually render index.html or indexTour.html depending on your main page
    return HttpResponse('Home_page') 

def products(request):
    return HttpResponse('Products_page')

def customer(request):
    return HttpResponse('Customer_page')

# Existing views that render templates
def index(request):     
    return render(request, 'Tour/index.html')

def indexTour(request):
    return render(request, 'Tour/index.html')

# --- New Views to match the navigation menu and your template files ---

def about(request):
    return render(request, 'Tour/about.html')

def destinations(request):
    return render(request, 'Tour/destinations.html')

def tours(request):
    return render(request, 'Tour/tours.html')

def gallery(request):
    return render(request, 'Tour/gallery.html')

def blog(request):
    return render(request, 'Tour/blog.html')

def contact(request):
    return render(request, 'Tour/contact.html')

# Views for the 'More Pages' dropdown
def destination_details(request):
    return render(request, 'Tour/destination-details.html')

def tour_details(request):
    return render(request, 'Tour/tour-details.html')

def booking(request):
    return render(request, 'Tour/booking.html')

def testimonials(request):
    return render(request, 'Tour/testimonials.html')

def faq(request):
    return render(request, 'Tour/faq.html')

def blog_details(request):
    return render(request, 'Tour/blog-details.html')

def terms(request):
    return render(request, 'Tour/terms.html')

def privacy(request):
    return render(request, 'Tour/privacy.html')

def error_404(request):
    # Use your custom 404 template
    return render(request, 'Tour/404.html', status=404)

