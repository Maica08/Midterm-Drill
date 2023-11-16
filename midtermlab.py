
class Account:
    def __init__(self, accountNumber:int, balance:float, dateofOpening:str):
        self._accountNumber = accountNumber
        self._balance = balance
        self._dateofOpening = dateofOpening

    @property
    def accountNumber(self) -> int:
        return self._accountNumber

    @accountNumber.setter
    def accountNumber(self, new_accNumber:int) -> None:
        self._accountNumber = new_accNumber

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, set_balance:float) -> None:
        self._balance = set_balance

    @property
    def dateofOpening(self) -> str:
        return self._dateofOpening

    @dateofOpening.setter
    def dateofOpening(self, set_date:str) -> None:
        self._dateofOpening = set_date

    def debit_amount(self, withdraw_amount:float) -> None:
        if withdraw_amount > 0 and withdraw_amount < self.balance:
            self.balance -= withdraw_amount
        else:
            print("Invalid withdrawal amount. Cannot withdraw.")

    def credit_amount(self, deposit_amount:float) -> None:
        if deposit_amount > 0:
            self.balance += deposit_amount
        else:
            print("Invalid deposit amount.")


class Customer:
    def __init__(self, customerId:int, name:str, address:str, phone:str):
        self._customerId = customerId
        self._name = name
        self._address = address
        self._phone = phone
    
    @property
    def customerId(self) -> str:
        return self._customerId

    @customerId.setter
    def customerId(self, set_customerId:str) -> None:
        self._customerId = set_customerId

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, set_name:str) -> None:
        self._name = set_name

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, set_address:str) -> None:
        self._address = set_address

    @property
    def phone(self) -> str:
        return self._phone

    @address.setter
    def phone(self, set_phone:str) -> None:
        self._phone = set_phone

    def display_info(self):
        print("CUSTOMER INFORMATION")
        print(f"Name: {self.name}")
        print(f"Customer ID: {self.customerId}")
        print(f"Address: {self.address}")
        print(f"Phone: {self.phone}")



class SavingsAccount(Account):
    all_savings_accounts = []

    def __init__(self, accountNumber:int, balance:float, dateofOpening:str, minBalance:float):
        super().__init__(accountNumber, balance, dateofOpening)
        self._minBalance = minBalance
        self.customer = None

        SavingsAccount.all_savings_accounts.append(self)

    @property
    def minBalance(self) -> float:
        return self._minBalance

    @minBalance.setter
    def minBalance(self, set_minBalance:float) -> None:
        self._minBalance = set_minBalance

    def add_customer(self, customer:Customer):
        if self.customer == None:
            self.customer = customer
        else:
            print("Customer already assigned.")

    def remove_customer(self) -> None:
        if self.customer != None:
            self.customer = None
        else:
            print("Nothing to remove.")
        
    
class CurrentAccount(Account):
    all_current_accounts = []

    def __init__(self, accountNumber: int, balance: float, dateofOpening: str, interestRate:float):
        super().__init__(accountNumber, balance, dateofOpening)
        self._interestRate = interestRate
        self.customer = None

        CurrentAccount.all_current_accounts.append(self)

    @property
    def interestRate(self) -> float:
        return self._interestRate

    @interestRate.setter
    def interestRate(self, set_interestRate:float) -> None:
        if set_interestRate <= 1 and set_interestRate >= 0:
            self._interestRate = set_interestRate
        else:
            print("Invalid value of interest rate; value must be between 1 and 0.")

    def add_customer(self, customer:Customer) -> None:
        if self.customer == None:
            self.customer = customer
        else:
            print("Customer already assigned.")

    def remove_customer(self) -> None:
        if self.customer != None:
            self.customer = None
        else:
            print("Nothing to remove.")


def main():
    customer1 = Customer(customerId=100001, name="George Cruz", address="Palawan", phone="09123456789")
    customer2 = Customer(customerId=100002, name="Maya Magno", address="Puerto Princesa", phone="09345678912")

    savings1 = SavingsAccount(accountNumber = 125456, balance = 4500, dateofOpening = "Jan 3, 2015", minBalance = 100)
    savings2 = SavingsAccount(accountNumber = 125457, balance = 5500, dateofOpening = "Aug 3, 2015", minBalance = 100)
    savings1.add_customer(customer1)
    savings2.add_customer(customer2)

    current1 = CurrentAccount(accountNumber=125456, balance=4500, dateofOpening="Jan 3, 2015", interestRate=0.02)
    current2 = CurrentAccount(accountNumber=125457, balance=5500, dateofOpening="Sep 15, 2015", interestRate=0.05)
    current1.add_customer(customer1)
    current2.add_customer(customer2)

    print("----------Customer Info----------")
    for account in SavingsAccount.all_savings_accounts:
        account.customer.display_info()
        print("Account Type: Savings")
        print(f"Account Number: {account.accountNumber}")
        print(f"Balance: {account.balance}")
        print(f"Date of Opening: {account.dateofOpening}")
        print(f"Minimum Balance: {account.minBalance}")
        print()

    for account in CurrentAccount.all_current_accounts:
        account.customer.display_info()
        print("Account Type: Current")
        print(f"Account Number: {account.accountNumber}")
        print(f"Balance: {account.balance}")
        print(f"Date of Opening: {account.dateofOpening}")
        print(f"Interest Rate: {account.interestRate}")
        print()


if __name__ == "__main__":
    main()
