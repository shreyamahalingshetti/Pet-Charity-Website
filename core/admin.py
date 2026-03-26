from django.contrib import admin
from .models import Pet, AdoptionRequest, Donation, ContactMessage


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'age', 'gender', 'is_available', 'created_at')
    list_filter = ('species', 'gender', 'is_available')
    search_fields = ('name', 'breed', 'description')
    list_editable = ('is_available',)


@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = ('applicant_name', 'pet', 'email', 'phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('applicant_name', 'email')


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'email', 'amount', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('donor_name', 'email')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject')
