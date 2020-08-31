from .base import BaseEmailProvider
from fes.config import FROM_EMAIL, EMAIL_PROVIDERS


class SendGridEmailService(BaseEmailProvider):
    config = EMAIL_PROVIDERS['SEND_GRID']

    def send_email(self, to_address, subject, body):
        self._send(to_address, subject, body)

    def _send(self, to_address, subject, body):
        data = {
            "personalizations": [
                {
                    "to": [],
                    "subject": ""
                }
            ],
            "from": {
                "email": ""
            },
            "content": [

            ]
        }
        to_addreses = [dict(email=addr)  for addr in to_address]
        content = {"type": "text/html",
                   "value": body
                   }
        data['from']['email'] = FROM_EMAIL
        data['personalizations']['to'] = to_address
        data['personalizations']['subject'] = to_address
        data['content'].append(content)
        url = self.config['base_url'] + '/send'
        headers = {
            'authorization': "Bearer {api_key}".format(
                api_key=self.config['apy_key']),
            'Content-Type': 'application/json'
        }
        self._post(url=url,
                   data=data,
                   auth=None,
                   headers=headers)

