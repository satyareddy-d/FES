import requests
from fes.exceptions import (
    EmailServiceUnAvailable,
    BadRequest, UnAuthorized,
    SizeExceeds
)
class BaseEmailProvider(object):

    def send_email(self, to_address, subject, body):
        raise NotImplemented(
            "all concrete class should implement it")

    def _post(self, url, data, auth, headers=None):
        res = requests.post(url=url,
                            data=data,
                            auth=auth,
                            headers=headers)
        if res.status_code != 200:
            raise_http_error(res)
        return res


def raise_http_error(res):
    if res.status_code == 500:
        raise EmailServiceUnAvailable("Service not available")
    elif res.status_code == 400:
        raise BadRequest("missing required parameters")
    elif res.status_code == 401:
        raise UnAuthorized("Invalid credentials")
    elif res.status_code == 413:
        raise SizeExceeds("Attachment size is too big")


