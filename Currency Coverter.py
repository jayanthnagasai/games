USD = 1
USD = 1.13798
GBP = 0.857679
RUB = 74.9470


def currencyConverter():
    chosenCurrency = input("Do you wish to convert your euros into \n1)USD \n2)RUB \n3)GBP\n\n")
    print(("-" * 36) + "\n")
    print(chosenCurrency, "\n\n" + ("-" * 36))

    # USD
    if (chosenCurrency) == "1":
        eurAmount = round(float(input("How many euros do you wish to convert into USD?\n\n")))
        print(("-" * 36) + "\n")
        print(eurAmount, "euros is", round((eurAmount) * 1.13798, 2), "US dollars.\n\n" + ("-" * 36),
              "\nThank you for using my program!")

    # RUB
    elif (chosenCurrency) == "2":
        eurAmount = round(float(input("How many euros do you wish to convert into RUB?\n\n")))
        print(("-" * 36) + "\n")
        print(eurAmount, "euros is", round((eurAmount) * 74.9470, 2), "rubles.\n\n" + ("-" * 36),
              "\nThank you for using my program!")

    # GBP
    elif (chosenCurrency) == "3":
        eurAmount = round(float(input("How many euros do you wish to convert into GBP?\n\n")))
        print(("-" * 36) + "\n")
        print(eurAmount, "euros is", round((eurAmount) * 0.857679, 2), "pounds.\n\n" + ("-" * 36),
              "\n\nThank you for using my program!")

    # Fail
    else:
        print("Error, please try again. \nEnter 1 for USD, 2 for RUB or 3 for GBP.")


currencyConverter()