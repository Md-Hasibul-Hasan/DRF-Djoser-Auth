# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth import get_user_model
# from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

# User = get_user_model()

# @receiver(post_save, sender=User)
# def blacklist_tokens_on_password_change(sender, instance, **kwargs):
#     if instance.pk:
#         tokens = OutstandingToken.objects.filter(user=instance)

#         for token in tokens:
#             try:
#                 BlacklistedToken.objects.get_or_create(token=token)
#             except:
#                 pass