
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
            print("Invalid withdrawal amount. Amount must be between 0 and amount of current balance; cannot withdraw.")

    def credit_amount(self, deposit_amount:float) -> None:
        if deposit_amount > 0:
            self.balance += deposit_amount
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")


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

    @phone.setter
    def phone(self, set_phone:str) -> None:
        self._phone = set_phone

    def display_info(self) -> None:
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
    customer1 = Customer(customerId=100001, name="Crishel B. Ponce", address="Palawan", phone="09123456789")
    customer2 = Customer(customerId=100002, name="Fernando P. Pineda Jr.", address="Puerto Princesa", phone="09345678912")

    savings1 = SavingsAccount(accountNumber=125456, balance=4500, dateofOpening="Jan 3, 2015", minBalance=100)
    savings2 = SavingsAccount(accountNumber=125457, balance=5500, dateofOpening="Aug 3, 2015", minBalance=100)
    savings1.add_customer(customer1)
    savings2.add_customer(customer2)

    current1 = CurrentAccount(accountNumber=125456, balance=4500, dateofOpening="Jan 3, 2015", interestRate=0.02)
    current2 = CurrentAccount(accountNumber=125457, balance=5500, dateofOpening="Sep 15, 2015", interestRate=0.05)
    current1.add_customer(customer1)
    current2.add_customer(customer2)

    # TESTER

    # print(len(SavingsAccount.all_savings_accounts))
    # savings2.add_customer(customer2)
    # savings2.remove_customer()
    # savings2.remove_customer()
    # print(savings2.customer)

    # savings1.debit_amount(5000)
    # print(savings1.balance)
    # savings1.credit_amount(-50)
    # print(savings1.balance)

    # current1.interestRate = -5

    # MAIN
    withdraw_savings1 = 200
    withdraw_savings2 = 300
    withdraw_currrent1 = 100
    withdraw_current2 = 200

    deposit_savings1 = 500
    deposit_savings2 = 600
    deposit_current1 = 1000
    deposit_current2 = 1100

    print("Savings Accounts Withdraw and Deposit History")
    print(f"Savings Account 1 Initial Balance: {savings1.balance}")
    savings1.debit_amount(withdraw_amount=withdraw_savings1)
    print(f"Balance after cash withdrawal 200: {savings1.balance}")
    savings1.credit_amount(deposit_amount=deposit_savings1)
    print(f"Balance after cash deposit {deposit_savings1}:    {savings1.balance}\n")

    print(f"Savings Account 2 Initial Balance: {savings2.balance}")
    savings2.debit_amount(withdraw_amount=withdraw_savings2)
    print(f"Balance after cash withdrawal {withdraw_savings2}: {savings2.balance}")
    savings2.credit_amount(deposit_amount=deposit_savings2)
    print(f"Balance after cash deposit {deposit_savings2}:    {savings2.balance}\n")

    print("Current Accounts Withdraw and Deposit History")
    print(f"Current Account 1 Initial Balance: {current1.balance}")
    current1.debit_amount(withdraw_amount=withdraw_currrent1)
    print(f"Balance after cash withdrawal {withdraw_currrent1}: {current1.balance}")
    current1.credit_amount(deposit_amount=deposit_current1)
    print(f"Balance after cash deposit {deposit_current1}: {current1.balance}\n")
    
    print(f"Current Account 2 Initial Balance: {current2.balance}")
    current2.debit_amount(withdraw_amount=withdraw_current2)
    print(f"Balance after cash withdrawal {withdraw_current2}: {current2.balance}")
    current2.credit_amount(deposit_amount=deposit_current2)
    print(f"Balance after cash deposit {deposit_current2}: {current2.balance}\n")


    print("----------Account Logs----------")
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
