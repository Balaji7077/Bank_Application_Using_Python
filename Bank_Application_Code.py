class Bank:
    Bankname  = 'Canara Bank'
    Ifsc_code = 'CNB8038'
    Branch    = 'Marathali'
    Roi       = 3.8
    def __init__(self, Name, AccNo, MobileNo, Balance, Pin):
        self.Name     = Name
        self.AccNo    = AccNo
        self.MobileNo = MobileNo
        self.Balance  = Balance
        self.Pin      = Pin
    def Check_Balance(self):
        if self.Pin == self.validation():
            return f'{self.Name} has account balance of {self.Balance}'
        else:
            return 'Incorrect Pin'
    def withdraw(self):
        amount= int(input('Enter The Amount To Withdraw'))
        if self.Balance >= amount:
            self.Balance-= amount
            return f' The Amount After Withdraw is {self.Balance}'
        else:
            return 'Insufficient Balance'
    def Deposite(self):
        amount=int(input('Enter the amount for deposit:'))
        self.Balance+= amount
        return f' The Balance After Deposite Is {self.Balance}'
    def Change_Pin(self):
        old_pin = int(input('Enter The Old Pin'))
        new_pin1 = int(input('ENter The New Pin'))
        new_pin2 = int(input('Reenter The New Pin'))
        if new_pin1 != new_pin2:
            return 'Try It Again'
        else:
            return 'Pin Has Been Changed Succsessfully'
    @staticmethod
    def validation():
        return int(input('Enter The 4 Digit Pin: '))
C1 = Bank('Balaji', '803876563', 7789993833,12000, 2323)
C2 = Bank('Sabat', '7893784657', 8763505511, 15000, 4545)
print(C1.Check_Balance())
print(C1.withdraw())
print(C1.Deposite())
print(C1.Change_Pin())
