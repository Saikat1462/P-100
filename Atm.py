class Details(object):
    def __init__(self,cardNumber,balanceInquiry,pinNumber,cashWithdrawl):
        self.cardNumber=cardNumber
        self.balaneInquiry=balanceInquiry
        self.pinNumber=pinNumber
        self.cashWithdrawl=cashWithdrawl

    def start(self):
        print(self.cardNumber + " has started")
    def stop(self):
        print(self.cardNumber + " has stoped")
Saikat=Details("123456789","1000","XXXX","500")
print(Saikat.start())
print(Saikat.stop())
print(Saikat.balaneInquiry)