from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import Review
from django.utils import timezone

@receiver(post_save, sender=Review)
def send_email_on_save(sender, instance, **kwargs):
    subject = instance.user_name.Name+' Review Details'
    message = (
                f'Name: {instance.user_name.Name}\n'
                f'Moral Character: {instance.Moral_character}\n'
                f'Punctuality: {instance.punctuality}\n'
                f'Health: {instance.health}\n'
                f'Behaviour: {instance.behaviour}\n'
                f'Attitude: {instance.attitude}\n'
                f'Career Goals: {instance.Career_goals}\n'
                f'Understanding Level: {instance.understanding_level}\n'
                f'Positive Attitude and mind: {instance.possitive_attitude_and_mind}\n'
                f'Executive: {instance.executive}\n'
                f'Responsibility: {instance.responsibility}\n'
                f'Response Ability: {instance.response_ability}\n'
                f'Team Handling: {instance.team_handling}\n'
                f'Planning: {instance.planing}\n'
                f'Communication Ability: {instance.communicate_ability}\n'
                f'Passion: {instance.passion}\n'
                f'Confidence: {instance.confidence}\n'
                f'Professional Background: {instance.profissional_background}\n'
                f'Work Experience: {instance.work_experience}\n'
                f'Knowledge Level: {instance.knowledge_level}\n'
                f'English Skills: {instance.english_skils}\n'
                f'Other Languages: {instance.other_languages}\n'
                f'Consider to Client: {instance.consider_to_client}\n'
                f'Internal Hiring: {instance.Internal_hiring}\n'
                f'Reject: {instance.reject}\n'
                f'Created At: {str(instance.created_at)[:18]}\n'
                f'Remarks: {instance.remarks}\n'
                f'Reviewedby: {instance.ReviewedBy}\n')


    from_email = "athirupan.kk@gmail.com"
    recipient_list = ["harikrishnad76@gmail.com"]
    #businesshr@meridatechminds.com
    
    # send_mail(subject, message, from_email, recipient_list)


from django.contrib.auth.models import User
# from django.contrib.auth.signals import user_logged_in
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from django.conf import settings

# @receiver(user_logged_in)
# def send_login_notification(sender, request, user, **kwargs):
#     # Check if the logged-in user is a superuser, staff user, or staff user using superuser credentials

#     superusers = User.objects.filter(is_superuser=True)
#     if superusers.exists():
#         superuser_username = superusers.first().username
#     else:
#         # No superuser found
#         return
    
#     if user.is_superuser:
#         subject = 'Superuser Logged in Notification'
#         message = f'The superuser {superuser_username} logged in.'
#     elif user.is_staff and user.username == superuser_username:
#         subject = f'{user.username} Logged in Using Superuser Credentials'
#         message = f'A staff user{user.username} logged in using the superuser credentials.'
#     elif user.is_staff:
#         subject = 'Staff User Logged in Notification'
#         message = f'A staff user {user.username} logged in'
#     else:
#         return  # Do nothing if the user is neither superuser nor staff user

#     send_mail(
#         subject,
#         message,
#         settings.DEFAULT_FROM_EMAIL,
#         ["businesshr@meridatechminds.com"],  # Sending email to the logged-in user
#         fail_silently=True,
#     )




