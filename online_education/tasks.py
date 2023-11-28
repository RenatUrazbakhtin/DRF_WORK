from datetime import datetime, timedelta

from celery import shared_task
from django.core.mail import send_mail

from config import settings
from online_education.models import Subscription, Course
from users.models import User


@shared_task
def send_newsletter(course_pk):

    subscribers = Subscription.objects.filter(course=course_pk)
    emails = []
    course_name = Course.objects.get(pk=course_pk).title

    for subscription in subscribers:
        emails.append(subscription.subscriber.email)
    if subscribers:
        send_mail(
            subject='Subscription to the course',
            message=f'There are updates in course {course_name}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[mail for mail in emails]
        )

@shared_task
def last_user_login_check():
    date = datetime.now() - timedelta(days=30)
    users = User.objects.filter(is_active=True, last_login__lt=date)

    for user in users:
        user.is_active = False
        user.save()