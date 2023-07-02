from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AbstractSocialProvider(ABC):
    def __init__(self, token: str):
        self.token = token

    @abstractmethod
    def send_direct_message(self, account_id: str, message: str):
        ...  # The logic of sending a message


class FacebookProvider(AbstractSocialProvider):
    def send_direct_message(self, account_id: str, message: str):
        logger.info(
            f'Sent message via Facebook to {account_id}. Message: {message}'
        )


class InstagramProvider(AbstractSocialProvider):
    def send_direct_message(self, account_id: str, message: str):
        logger.info(
            f'Sent message via Instagram to {account_id}. Message: {message}'
        )


class SocialMediaMailingService:
    def __init__(self, social_provider: AbstractSocialProvider):
        self.social_provider = social_provider

    def send_direct_message_to_user(self, account_id: str, message: str):
        self.social_provider.send_direct_message(account_id, message)


if __name__ == '__main__':
    USER_TOKEN = '__TOKEN__'
    social_provider_instance = FacebookProvider(token=USER_TOKEN)
    mailing_service = SocialMediaMailingService(social_provider_instance)
    mailing_service.send_direct_message_to_user('user1234', 'Hi! How are you?')
