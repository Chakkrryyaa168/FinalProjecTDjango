from django.contrib import admin
from .models import Customer, Destination, Hotel, Room, Booking

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "date_created")
    search_fields = ("name", "email")
    list_filter = ("date_created",)


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    search_fields = ("name", "country")


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "destination", "stars")
    list_filter = ("destination", "stars")
    search_fields = ("name",)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("hotel", "room_type", "price_per_night", "capacity", "is_available")
    list_filter = ("hotel", "room_type", "is_available")
    search_fields = ("hotel__name", "room_type")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("customer", "room", "check_in", "check_out", "status", "created_at")
    list_filter = ("status", "created_at", "check_in")
    search_fields = ("customer__name",)
