from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass


class Fax(ABC):
    @abstractmethod
    def fax_document(self):
        pass


class BasicPrinter(Printer):
    def print_document(self):
        return "Basic printing"


class AllInOnePrinter(Printer, Scanner, Fax):
    def print_document(self):
        return "High quality printing"

    def scan_document(self):
        return "Scanning document"

    def fax_document(self):
        return "Sending fax"

# Каждый класс реализует только нужные интерфейсы