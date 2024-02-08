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

    def pays(self, bill, flatmate2):
        weight = self.days_in_house /(self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay



class PdfReport:

    '''
    Creates a PDF file which documents flatmate name, due amount and period of stay
    '''

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(amount= 120, period= 'March 2021')
john = Flatmate(name= 'John', days_in_house= 20)
mary = Flatmate(name= 'Mary', days_in_house= 25)
print(john.pays(bill= the_bill, flatmate2= mary))
