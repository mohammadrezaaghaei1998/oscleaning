from django.shortcuts import render,redirect
from .models import Contact

from django.contrib import messages

# def index(request):
#     if request.method == "POST":
#         name = request.POST.get("name", "").strip()
#         email = request.POST.get("email", "").strip()
#         subject = request.POST.get("subject", "").strip()
#         message = request.POST.get("message", "").strip()

#         if not name or not email or not subject or not message:
#             messages.error(request, "Bitte füllen Sie alle Felder aus.")
#             return render(request, "index.html")

#         try:
#             Contact.objects.create(
#                 name=name,
#                 email=email,
#                 subject=subject,
#                 message=message
#             )
#             messages.success(request, "Nachricht wurde erfolgreich gesendet!")
#             return redirect("index")

#         except Exception as e:
#             messages.error(request, "Fehler beim Senden der Nachricht. Bitte versuchen Sie es später erneut.")

#     return render(request, "index.html")





from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, Appointment


def index(request):

    # =========================
    # CONTACT FORM (UNCHANGED)
    # =========================
    if request.method == "POST" and request.POST.get("form_type") == "contact":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not email or not subject or not message:
            messages.error(request, "Bitte füllen Sie alle Felder aus.")
            return redirect("index")

        try:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, "Nachricht wurde erfolgreich gesendet!")
            return redirect("index")

        except Exception:
            messages.error(request, "Fehler beim Senden der Nachricht.")
            return redirect("index")

    # =========================
    # APPOINTMENT FORM (NEW)
    # =========================
    if request.method == "POST" and request.POST.get("form_type") == "appointment":
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()
        cleaners = request.POST.get("cleanersCount", "").strip()
        service = request.POST.get("services", "").strip()

        # Validation
        if not name or not phone or not cleaners or not service:
            messages.error(request, "Bitte füllen Sie alle Termin-Felder aus.")
            return redirect("index")

        if len(phone) < 6:
            messages.error(request, "Bitte geben Sie eine gültige Telefonnummer ein.")
            return redirect("index")

        try:
            Appointment.objects.create(
                name=name,
                phone=phone,
                cleaners_count=cleaners,
                service=service
            )

            messages.success(request, "Termin wurde erfolgreich gebucht!")
            return redirect("index")

        except Exception:
            messages.error(request, "Fehler beim Buchen des Termins.")
            return redirect("index")

    return render(request, "index.html")




def about_us(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not email or not subject or not message:
            messages.error(request, "Bitte füllen Sie alle Felder aus.")
            return render(request, "about.html")

        try:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, "Nachricht wurde erfolgreich gesendet!")
            return redirect("about-us")

        except Exception as e:
            messages.error(request, "Fehler beim Senden der Nachricht. Bitte versuchen Sie es später erneut.")
            
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def portfolio(request):
    return render(request, "portfolio.html")

def contact(request):

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not email or not subject or not message:
            messages.error(request, "Bitte füllen Sie alle Felder aus.")
            return render(request, "contact.html")

        try:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, "Nachricht wurde erfolgreich gesendet!")
            return redirect("contact")

        except Exception as e:
            messages.error(request, "Fehler beim Senden der Nachricht. Bitte versuchen Sie es später erneut.")
    return render(request, "contact.html")

    