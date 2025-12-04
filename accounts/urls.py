from django.urls import path
from . import views

urlpatterns = [
    # Existing Paths (Now with 'name' arguments)
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/', views.customer, name='customer'),
    path('hiaub/', views.index, name='index'),
    path('indexTour/', views.indexTour, name='indexTour'), 

    # Paths for Main Navigation Links
    path('about/', views.about, name='about'),
    path('destinations/', views.destinations, name='destinations'),
    path('tours/', views.tours, name='tours'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),

    # Paths for 'More Pages' Dropdown
    path('destination-details/', views.destination_details, name='destination_details'),
    path('tour-details/', views.tour_details, name='tour_details'),
    path('booking/', views.booking, name='booking'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('faq/', views.faq, name='faq'),
    path('blog-details/', views.blog_details, name='blog_details'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('404/', views.error_404, name='error_404'),
]