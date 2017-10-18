from config import twitter
import base64


class Credentials(object):
    """Container for processing credentials needed for application-only authentication in Twitter API,
    namely Consumer Key and Consumer Secret, which need to be Base64 encoded for BASIC authentication.
        https://developer.twitter.com/en/docs/basics/authentication/overview/application-only
    """

    consumer_key = twitter.consumer_key
    consumer_secret = twitter.consumer_secret


def get_bearer_token_credentials(self):
    """Concatenate the encoded consumer key, a colon character ':', and the encoded consumer secret into a single
    string.
    """
    return self.consumer_key + ':' + self.consumer_secret


def get_base64_bearer_token_credentials(bearer_token):
    """Base64 encode the string obtained from #get_bearer_token_credentials() method, needed for BASIC authentication
    in Twitter API
    """
    return base64.b64encode(bearer_token.encode('utf-8')).decode('utf-8')
