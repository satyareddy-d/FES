from fes.celery import app
from fes.utils.providers import send_email as _send_email
from fes.exceptions import EmailServiceUnAvailable

@app.task(nam="send_email", bind=True,
          autoretry_for=(EmailServiceUnAvailable,),
          exponential_backoff=2,
          retry_kwargs={'max_retries': 10},
          retry_jitter=True)
def send_email(self, to_addresses, subject, body):
    _send_email(to_addresses=to_addresses,
                subject=subject,
                body=body)

