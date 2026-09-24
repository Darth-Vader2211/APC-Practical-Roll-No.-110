class Printer:
    def print_document(self):
        print("Printing document...")


class Scanner:
    def scan_document(self):
        print("Scanning document...")


class MultifunctionDevice(Printer, Scanner):
    pass


device = MultifunctionDevice()
device.print_document()
device.scan_document()