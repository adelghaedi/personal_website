from django.shortcuts import render
from project_app.models import Project
from contactus_app.models import Contact, Message
from skill_app.models import Skill


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        body = request.POST.get("body")

        Message.objects.create(name=name, email=email, subject=subject, body=body)

    projects = Project.objects.all()
    contact = Contact.objects.all().last()
    socials = contact.socials.all()
    skills = Skill.objects.all()
    return render(
        request,
        "home.html",
        context={"projects": projects, "contact": contact, "socials": socials,"skills": skills },
    )
