from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


# Абстракции (DIP)
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass


class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message: str) -> bool:
        pass


# Конкретные реализации
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing credit card payment: ${amount}")
        return True


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing PayPal payment: ${amount}")
        return True


class EmailNotification(NotificationService):
    def send_notification(self, message: str) -> bool:
        print(f"Sending email: {message}")
        return True


class SMSNotification(NotificationService):
    def send_notification(self, message: str) -> bool:
        print(f"Sending SMS: {message}")
        return True


# Модель данных (SRP)
@dataclass
class OrderItem:
    product_id: str
    quantity: int
    price: float


@dataclass
class Order:
    order_id: str
    items: List[OrderItem]
    total_amount: float

    def calculate_total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)


# Сервис заказов (OCP, LSP, ISP)
class OrderService:
    def __init__(self,
                 payment_processor: PaymentProcessor,
                 notification_service: NotificationService):
        self.payment_processor = payment_processor
        self.notification_service = notification_service

    def process_order(self, order: Order) -> bool:
        try:
            # Обработка платежа
            payment_success = self.payment_processor.process_payment(order.total_amount)

            if payment_success:
                # Отправка уведомления
                message = f"Order {order.order_id} processed successfully"
                self.notification_service.send_notification(message)
                return True

            return False

        except Exception as e:
            print(f"Order processing failed: {e}")
            return False


# Использование
def main():
    # Создаем заказ
    items = [
        OrderItem("prod1", 2, 25.0),
        OrderItem("prod2", 1, 50.0)
    ]
    order = Order("order123", items, 100.0)

    # Настраиваем зависимости (DIP)
    payment_processor = PayPalProcessor()
    notification_service = SMSNotification()

    # Создаем сервис
    order_service = OrderService(payment_processor, notification_service)

    # Обрабатываем заказ
    success = order_service.process_order(order)
    print(f"Order processing {'succeeded' if success else 'failed'}")


if __name__ == "__main__":
    main()