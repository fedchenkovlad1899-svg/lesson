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

'''
3.Создайте класс User с ролью. Реализуйте policy-класс, определяющий доступ к методам. 
Создайте декоратор, который проверяет право пользователя на выполнение метода. 
Продемонстрируйте разрешённый и запрещённый доступ без if внутри метода.
'''
class User():
    def __init__(self, name: str, access_policy: str):
        self.name = name
        self.access_policy = access_policy


class Policy():
    def admin(user: User):
        return user.access_policy == "admin"

    def default_user(user: User):
        return user.access_policy in ["default_user", "admin"]


def chek_policy(policy_f):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            while not policy_f(user):
                raise PermissionError(f"у {user.name} нет доступа ")
            return func(user, *args, **kwargs)

        return wrapper

    return decorator


@chek_policy(Policy.admin)
def delete_inf(user: User):
    print(f'Информация удалена {user.name}')


@chek_policy(Policy.default_user)
def read(user: User):
    print(f'читайте:) {user.name}')


user = User('Vova', "default_user")
admin = User('Administrator', "admin")

delete_inf(admin)
read(admin)
read(user)
try:
    delete_inf(user)
except PermissionError as e:
    print(e)

'''
4.	Создай класс BankAccount, который имеет закрытый баланс __balance. Позволяет пополнять deposit
и снимать withdraw деньгию. Не позволяет снимать больше, чем есть на счету. Вводит суточный лимит снятия
 (например, 5000). Сделайте ограничение по транзакциям, не более 3 – х
'''
class BankAccount:
    def __init__(self, balance: float = 0):
        self.__balance = balance
        self.daily_limit = 5000
        self.withdrawals_today = 0
        self.max_withdrawals = 3
        self.withdrawals_count = 0

    def deposit(self, amount: float):
        if amount < 0:
            print('Пополнение должно быть положительным')
            return
        self.__balance += amount
        print(f'Cчет пополнен на {amount}.Баланс: {self.__balance}')

    def withdraw(self, amount: float):
        if amount > self.__balance:
            print('Недостаточно средств')
            return
        if self.withdrawals_today + amount >= self.daily_limit:
            print(f'превышен лимит снятия.Доступно {self.daily_limit - self.withdrawals_today} ')
            return
        if self.withdrawals_count >= self.max_withdrawals:
            print('превышен лимит операций')
            return
        self.__balance -= amount
        self.withdrawals_today += amount
        self.withdrawals_count += 1
        print(f'Снято: {amount}.Баланс: {self.__balance}')

    def get_balance(self):
        print(f"Баланс: {self.__balance}")
        return self.__balance


bank = BankAccount()
bank.deposit(10000)
bank.withdraw(4000)
bank.withdraw(100)
bank.withdraw(1000)
bank.deposit(1000)
bank.withdraw(100)
bank.withdraw(170)
bank.withdraw(100)
bank.withdraw(100)
bank.withdraw(100)
bank.get_balance()