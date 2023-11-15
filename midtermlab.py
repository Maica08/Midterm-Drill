
class Account:
    def __init__(self, accountNumber:int, balance:float, dateofOpening:str):
        self._accountNumber = accountNumber
        self._balance = balance
        self._dateofOpening = dateofOpening


    @property
    def accountNumber(self) -> int:
        account_number = self._accountNumber
        return account_number

    @accountNumber.setter
    def accountNumber(self, new_accNumber:int) -> None:
        self._accountNumber = new_accNumber

    @property
    def balance(self) -> float:
        balance = self._balance
        return balance

    @balance.setter
    def balance(self, set_balance:float) -> None:
        self._balance = set_balance

    @property
    def dateofOpening(self) -> str:
        date = self._dateofOpening
        return date

    @dateofOpening.setter
    def dateofOpening(self, set_date:str) -> None:
        self._dateofOpening = set_date


    def debit_amount(self, withdraw_amount:float) -> None:
        if withdraw_amount > self.balance:
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
        customerId = self._customerId
        return customerId

    @customerId.setter
    def customerId(self, set_customerId:str) -> None:
        self._customerId = set_customerId

    @property
    def name(self) -> str:
        name = self._name
        return name

    @name.setter
    def name(self, set_name:str) -> None:
        self._name = set_name

    @property
    def address(self) -> str:
        address = self._address
        return address

    @address.setter
    def address(self, set_address:str) -> None:
        self._address = set_address

    @property
    def phone(self) -> str:
        phone = self._phone
        return phone

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

    @property
    def minBalance(self) -> float:
        minBalance = self._minBalance
        return minBalance

    @minBalance.setter
    def minBalance(self, set_minBalance:float) -> None:
        self._minBalance = set_minBalance

    def add_customer(self, customer:Customer):
        for account in self.all_savings_accounts:
            if account["customer"] == customer:
                print("Cannot add account; account already exists.")
            
        self.customer = customer
        account = {"customer": self.customer, "account number": self.accountNumber, "balance": self.balance, "date of opening": self.dateofOpening, "minimum balance": self.minBalance}
        self.all_savings_accounts.append(account)

    def remove_customer(self) -> None:
        self.customer = None

    
class CurrentAccount(Account):
    all_current_accounts = []

    def __init__(self, accountNumber: int, balance: float, dateofOpening: str, interestRate:float):
        super().__init__(accountNumber, balance, dateofOpening)
        self._interestRate = interestRate

    @property
    def interestRate(self) -> float:
        interestRate = self._interestRate
        return interestRate

    @interestRate.setter
    def interestRate(self, set_interestRate:float) -> None:
        self._interestRate = set_interestRate

    def add_customer(self, customer):
        # if len(self.all_current_accounts) != 0:
        for account in self.all_current_accounts:
            if account["customer"] == customer:
                print("Cannot add account; account already exists.")
                return
            
        self.customer = customer
        account = {"customer": self.customer, "account number": self.accountNumber, "balance": self.balance, "date of opening": self.dateofOpening, "interest rate": self.interestRate}
        self.all_current_accounts.append(account)


    def remove_customer(self) -> None:
        self.customer = None


def main():
    customer1 = Customer(customerId=100001, name="George Cruz", address="Palawan", phone="09123456789")
    customer2 = Customer(customerId=100002, name="Maya Magno", address="Puerto Princesa", phone="09345678912")


    savings = SavingsAccount(accountNumber = 125456, balance = 4500, dateofOpening = "Jan 3, 2015", minBalance = 100)
    savings.add_customer(customer1)

    savings.remove_customer()
    savings.accountNumber = 125457
    savings.balance = 5500
    savings.dateofOpening = "Aug 3, 2015"
    savings.minBalance = 100
    savings.add_customer(customer2)


    # savings2 = SavingsAccount(accountNumber="125457", balance="5500", dateofOpening="Aug 3, 2015", minBalance=100)
    # savings2.add_customer(customer2)

    current = CurrentAccount(accountNumber=125456, balance="4500", dateofOpening="Jan 3, 2015", interestRate=0.02)
    current.add_customer(customer1)

    current.remove_customer()
    current.accountNumber = 125457 
    current.balance = 5500 
    current.dateofOpening = "Jan 3, 2015"
    current.interestRate = 0.03
    current.add_customer(customer2)


    customer1.display_info()
    print()
    customer2.display_info()
    print()

    # print(savings.all_savings_accounts)

    for account in savings.all_savings_accounts:
        print(account)
    print()

    for account in current.all_current_accounts:
        print(account)

    # print(savings.customer.display_info())


if __name__ == "__main__":
    main()
