from __future__ import absolute_import, unicode_literals
import random
from celery import shared_task
from django.core.mail import send_mail

# @shared_task
# def add(x, y):
#     return x + y


@shared_task
def send_joinemail(to_email):
    send_mail('Welcome to Fitness Centre', 'Thank you for joining!', 'jayawd02@myunitec.ac.nz', [to_email],
              fail_silently=False)
