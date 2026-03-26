from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Pet, AdoptionRequest, Donation, ContactMessage


def get_mode(request):
    """Get current mode from session, default to 'cat'."""
    return request.session.get('mode', 'cat')


def home(request):
    mode = get_mode(request)
    pets = Pet.objects.filter(species=mode, is_available=True)[:3]
    return render(request, 'core/home.html', {'mode': mode, 'featured_pets': pets})


@csrf_exempt
def set_mode(request):
    """AJAX endpoint to toggle mode."""
    if request.method == 'POST':
        mode = request.POST.get('mode', 'cat')
        if mode in ('cat', 'dog'):
            request.session['mode'] = mode
            return JsonResponse({'status': 'ok', 'mode': mode})
    return JsonResponse({'status': 'error'}, status=400)


def adoption(request):
    mode = get_mode(request)
    pets = Pet.objects.filter(species=mode, is_available=True)
    return render(request, 'core/adoption.html', {'mode': mode, 'pets': pets})


def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    mode = get_mode(request)

    if request.method == 'POST':
        AdoptionRequest.objects.create(
            pet=pet,
            applicant_name=request.POST.get('name', ''),
            email=request.POST.get('email', ''),
            phone=request.POST.get('phone', ''),
            message=request.POST.get('message', ''),
        )
        messages.success(request, f'Your adoption request for {pet.name} has been submitted!')
        return redirect('pet_detail', pk=pk)

    return render(request, 'core/pet_detail.html', {'mode': mode, 'pet': pet})


def awareness(request):
    mode = get_mode(request)
    return render(request, 'core/awareness.html', {'mode': mode})


def gallery(request):
    mode = get_mode(request)
    pets = Pet.objects.filter(species=mode)
    return render(request, 'core/gallery.html', {'mode': mode, 'pets': pets})


def donation(request):
    mode = get_mode(request)

    if request.method == 'POST':
        Donation.objects.create(
            donor_name=request.POST.get('name', ''),
            email=request.POST.get('email', ''),
            amount=request.POST.get('amount', 0),
            message=request.POST.get('message', ''),
        )
        messages.success(request, 'Thank you for your generous donation!')
        return redirect('donation')

    return render(request, 'core/donation.html', {'mode': mode})


def about(request):
    mode = get_mode(request)
    return render(request, 'core/about.html', {'mode': mode})


def contact(request):
    mode = get_mode(request)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message_text = request.POST.get('message', '')

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message_text,
        )

        # Send email notification
        try:
            from django.core.mail import send_mail
            from django.conf import settings
            send_mail(
                subject=f'[PawsOfHope Contact] {subject}',
                message=f'Name: {name}\nEmail: {email}\n\n{message_text}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=True,
            )
        except Exception:
            pass  # Email sending is best-effort

        messages.success(request, 'Your message has been sent! We\'ll get back to you soon.')
        return redirect('contact')

    return render(request, 'core/contact.html', {'mode': mode})
