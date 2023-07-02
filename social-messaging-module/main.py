"""
Использованные принципы дизайна:
1. Полиморфизм
2. Single Responsibility Principle - SRP
3. Open/Closed Principle - OCP
4. Liskov Substitution Principle - LSP
5. Interface Segregation Principle - ISP
6. Dependency Inversion) - DI

AbstractSocialProvider - Определяет абстрактный метод send_direct_message, который должен быть
реализован в производных классах FacebookProvider и InstagramProvider. Использование
абстрактного базового класса помогает задать общий интерфейс для всех провайдеров социальных
сетей и гарантирует, что все провайдеры будут иметь метод send_direct_message.

Классы FacebookProvider и InstagramProvider отвечают за отправку сообщений через Facebook и
Instagram. Класс SocialMediaMailingService отвечает за отправку сообщений пользователю, используя
конкретный провайдер социальных сетей. Каждый класс имеет свою отдельную ответственность и
может быть изменен независимо от других классов.

Класс SocialMediaMailingService использует абстрактный класс AbstractSocialProvider в своем
конструкторе. Это позволяет подставить любой класс, наследующий AbstractSocialProvider, в качестве
провайдера социальных сетей, без изменения кода SocialMediaMailingService. Таким образом, класс
SocialMediaMailingService открыт для расширения новыми провайдерами социальных сетей, но закрыт
для изменений в своей основной логике.

Классы FacebookProvider и InstagramProvider являются подтипами AbstractSocialProvider.
Это означает, что они могут использоваться везде, где ожидается AbstractSocialProvider

AbstractSocialProvider определяет общий интерфейс для всех социальных провайдеров, который включает
только метод send_direct_message. Это позволяет клиентам использовать только те методы, которые им
действительно нужны, не навязывая лишний функционал.

Класс SocialMediaMailingService принимает в своем конструкторе абстрактный тип
AbstractSocialProvider. Это позволяет инвертировать зависимость между SocialMediaMailingService
и конкретными провайдерами социальных сетей. Вместо того, чтобы SocialMediaMailingService зависел
от конкретных реализаций провайдеров, он зависит от абстрактного типа
"""

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
