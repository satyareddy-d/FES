from fes.utils.providers.mail_gun import MailGunEmailService
from fes.utils.providers.send_grid import SendGridEmailService
from fes.exceptions import EmailServiceUnAvailable

# Email provides
MAIL_GUN = 'mailgun'
SEND_GRID = 'sendgrid'

EMAIL_PROVIDERS = [MAIL_GUN, SEND_GRID]


def email_service_factory(provider_name):
    if provider_name == MAIL_GUN:
        return MailGunEmailService()
    elif provider_name == SEND_GRID:
        return SendGridEmailService()
    else:
        raise ValueError("Invalid provider name")


def send_email(to_addresses, subject, body):
    if not to_addresses or not isinstance(to_addresses, list):
        raise ValueError("To addresses should be list")
    if not subject:
        raise ValueError("Subject is required")
    if not body:
        raise ValueError("Email body is required")

    for provider_name in EMAIL_PROVIDERS:
        email_service = email_service_factory(provider_name)
        try:
            email_service.send_email(to_address=to_addresses,
                                     subject=subject,
                                     body=body)
            break  # no Exception means email sent successfully
        except EmailServiceUnAvailable as error:
            # log the error and pass request to another email provider
            continue
    else:
        # this will execute if all email services are down
        raise EmailServiceUnAvailable("All email services are down"
                                      "Please try after some time")
