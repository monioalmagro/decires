from django.core.mail import send_mail
from apps.psychology.models import ContactMe


password = "qryk iyiy aghr fesj"


SUBJECT_NEW_PROFESSIONAL = "Nuevo registro de un Profesional"
MESSAGE_NEW_PROFESSIONAL = "Nuevo registro de un Profesional"
EMAIL_FROM = "decirespsicologia@gmail.com"
RECIPIENT_LIST = ["emazzurque@gmail.com"]

SUBJECT_CONTACT_ME = "Derivación"

EMAIL_FROM = "decirespsicologia@gmail.com"
RECIPIENT_LIST = ["emazzurque@gmail.com"]


async def prepare_data_contact_me(contact_me_instance: ContactMe):
    email_proff = contact_me_instance.user.email
    full_name = contact_me_instance.full_name
    email = contact_me_instance.email
    phone = contact_me_instance.phone
    user_message = contact_me_instance.message
    subject = SUBJECT_CONTACT_ME
    MESSAGE_CONTACT_ME = f"El usuario {full_name}, solicito una derivacióncon el profesional {email_proff}, con el siguiente mensaje: {user_message}. Datos del usuario: email: {email},  telefono: {phone}"
    email_from = EMAIL_FROM
    recipient_list = RECIPIENT_LIST
    await prepare_and_send_email(
        subject, MESSAGE_CONTACT_ME, email_from, recipient_list
    )
    await prepare_and_send_email(
        subject, MESSAGE_CONTACT_ME, email_from, [str(email_proff)]
    )


async def prepare_and_send_email(
    subject: str, message: str, email_from: str, recipient_list: list
):
    send_mail(subject, message, email_from, recipient_list)


async def prepare_data_new_professional(new_professional):
    subject = SUBJECT_NEW_PROFESSIONAL
    message = MESSAGE_NEW_PROFESSIONAL
    email_from = EMAIL_FROM
    recipient_list = RECIPIENT_LIST
    await prepare_and_send_email(subject, message, email_from, recipient_list)
