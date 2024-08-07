# class Bank_Account:
#     customer_name = "Default"
#     balance = 10.0
#     account_number = 0

# my_account = Bank_Account()
# my_account.customer_name = "Ushmala"
# my_account.balance = 0
# my_account.account_number = 123

# print(my_account.customer_name, my_account.balance , my_account.account_number)


class Bank_Account:
    def __init__(self, customer_name, balance, account_number):
        self.customer_name = customer_name
        self.balance = balance
        self.account_number = account_number
    
    def __str__(self):
        return self.customer_name

my_account = Bank_Account("ushmala", 0 , 82965)

print(my_account.customer_name, my_account.balance , my_account.account_number)
print(my_account)