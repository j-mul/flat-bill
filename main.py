class Bill:

    '''
    Object that contains data about a bill, such as total amount and billing period.
    '''

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:

    '''
    Create flatmate object that pays a share of the bill.
    '''

    def __init__(self, name, days_in_house):

        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        pass


class PdfReport:

    '''
    Creates a PDF file which documents flatmate name, due amount and period of stay
    '''

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass
