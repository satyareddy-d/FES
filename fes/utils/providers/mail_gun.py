from fes.utils.providers.base import BaseEmailProvider
from fes.config import FROM_EMAIL, EMAIL_PROVIDERS


class MailGunEmailService(BaseEmailProvider):
    config = EMAIL_PROVIDERS['MAIL_GUN']

    def send_email(self, to_address, subject, body):
        self._send(to_address, subject, body)

    def _send(self, to_address, subject, body):
        data = {
            "from": FROM_EMAIL,
            "to": to_address,
            "subject": subject,
            "text": body
        }
        url = self.config['base_url'] + '/messages'
        auth = ('api', self.config['api_key'])
        self._post(url=url,
                   data=data,
                   auth=auth)

if __name__ == '__main__':
    MailGunEmailService().send_email(
        to_address=['badranarayana@gmail.com'],
        subject="From new script",
        body="this content from new script"
    )
