import json
from celery import shared_task
from django.utils.html import strip_tags
from time import sleep
from django.template.loader import render_to_string 
from django.contrib.auth import get_user_model
from django.core.mail import send_mail, send_mass_mail, EmailMessage, EmailMultiAlternatives
from django.template.loader import get_template
from pyparsing import html_comment

from user.models import ProjectUser

from email.mime.text import MIMEText
@shared_task
def send_email_task(item, data):
    mail = EmailMultiAlternatives(
        subject='Hello',
        to=[item],
        from_email="bodya11dii@gmail.com",
        
    )
    
    
    mail.content_subtype = "html"
    # mail.attach(file, data)
    mail.attach_alternative( data, "text/html")
    mail.send()
    
    return None