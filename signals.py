from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db.models import Q
from myFirstApp.models import AccountUser

@receiver(post_save, sender=AccountUser, dispatch_uid="nim")
def check_nim(sender, instance, created, **kwargs):
    if not created:
        get_student_number = AccountUser.objects.filter(Q(account_user_student_number=instance.nim))
        get_email = User.objects.filter(Q(username=instance.nim))

        if get_student_number.exists() or get_email.exists():
            return HttpResponse('Data Exist')

        user = User.objects.create(username=instance.email)
        AccountUser.objects.create(
            account_user_related_user=user,
            account_user_fullname=instance.fullname,
            account_user_student_number=instance.nim
        )

    else:
        return redirect('myfirstapp:create-data-student')