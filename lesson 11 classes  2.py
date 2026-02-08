'''
1.Создайте абстрактный класс PaymentMethod. Объявить абстрактный метод pay(amount).
Реализовать минимум 3 класса-наследника с разной логикой оплаты. Обеспечить возможность работать
с объектами через общий интерфейс.  Проверить полиморфное поведение при вызове pay
'''
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class ByCard(PaymentMethod):
    def pay(self, amount):
        print(f'оплата картой {amount} BYN')
class Cash(PaymentMethod):
    def pay(self, amount):
        print(f'оплата наличными {amount} BYN')
class QrCode(PaymentMethod):
    def pay(self, amount):
        print(f'оплата QR-кодом {amount} BYN')
class Payer:
    def pay_by_method(self, method: PaymentMethod, amount:int):
        method.pay(amount)
payer_1 = Payer()
payer_1.pay_by_method(Cash(),100)
payer_1.pay_by_method(QrCode(),100)
payer_1.pay_by_method(ByCard(),100)

'''
2.Создайте абстрактный класс Notification. Объявите абстрактный метод send(message).
Реализуйте минимум 3 класса-наследника, каждый из которых отправляет сообщение по-разному.
'''
from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass
class BySMS (Notification):
    def __init__(self, phone_number:str):
        self.phone_number = phone_number
    def send(self, message):
        print(f' СМС на номер {self.phone_number}: {message}')
class ByTelegram(Notification):
    def __init__(self, id:str):
        self.id = id
    def send(self, message):
        print(f'уведомление в Telegram @{self.id}: {message}')
class ByEmail(Notification):
    def __init__(self, email_address:str):
        self.email_address = email_address
    def send(self, message):
        print(f'уведомление на почту {self.email_address}: {message}')
class Sender:
    def send_by_method(self, notification: Notification, message:str):
        notification.send(message)
sender_1 = Sender()
sender_1.send_by_method(BySMS('9379992'),'"You have new message!"')
sender_1.send_by_method(ByTelegram('ddanil'),'"You have new message!"')
sender_1.send_by_method(ByEmail('danilkolbasenko@mail.ru'),'"You have new message!"')