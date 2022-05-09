import time

from celery import shared_task


# Keep in mind celery doesen't naturally work with windows
@shared_task
def send_successful_registration_email(user):
    time.sleep(3)
    print(f'Email sent to {user}')
