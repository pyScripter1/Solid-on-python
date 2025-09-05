from abc import ABC, abstractmethod


class MultiFunctionDevice(ABC):
    @abstractmethod
    def print_document(self):
        pass

    @abstractmethod
    def scan_document(self):
        pass

    @abstractmethod
    def fax_document(self):
        pass


class BasicPrinter(MultiFunctionDevice):
    def print_document(self):
        return "Printing document"

    def scan_document(self):
        raise NotImplementedError("This printer cannot scan!")

    def fax_document(self):
        raise NotImplementedError("This printer cannot fax!")
    # Нарушение ISP: принуждаем реализовывать ненужные методы