from babel.numbers import format_currency

balance = int(input("Enter your balance: "))

currency = format_currency(balance, "USD", locale = "en_US")

print ("Your updated balance: ", currency.strip(".00"))