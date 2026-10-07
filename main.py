def Howell_Exp():

    user_Income = 0
    amount_used = 0
    used_for = ""
    balance = 0
    total_expenses = 0
    item_price = {}

    print("**Welcome to Howell Exp**", end="\n\n")

    # Income validation
    while True:

        user_Income = input("Input your income: ")

        try:
            user_Income = int(user_Income)

            if user_Income < 0:
                print("Income cannot be negative.")
                continue

            break

        except ValueError:
            print("Income must be a number.")

    Exit = True

    while Exit:

        choice = input(
            "\n1. continue\n"
            "2. exit\n"
            "..."
        ).lower()

        if choice == "continue" or choice == "1":

            amount_used = input("Input amount spent: ")
            used_for = input("What was the money used for: ")

            try:
                amount_used = int(amount_used)

                if amount_used < 0:
                    print("Expense cannot be negative.")
                    continue

                total_expenses += amount_used
                balance = user_Income - total_expenses

                item_price[used_for] = amount_used

            except ValueError:
                print("Amount spent must be a number.")
                continue

            Receipt = input(
                "Would you like to print receipt? yes/no: "
            ).lower()

            if Receipt == "yes":

                print("\n     ****RECEIPT****")
                print(f"{'Item':<12} {'Price':>10}")
                print(f"{'Income':<12} ₦ {user_Income:>8}")
                print("-" * 25)

                for key, value in item_price.items():
                    print(f"{key:<12} -₦ {value:>8}")

                print("-" * 25)
                print(f"{'Balance':<12} ₦ {balance:>8}")

        elif choice == "exit" or choice == "2":

            print("Goodbye!!!")
            Exit = False

        else:
            print("Invalid option. Please choose 1 or 2.")


def main():
    Howell_Exp()



if __name__ == "__main__":
    main()