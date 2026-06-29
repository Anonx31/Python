balance = 0.0
kyc_documents = {}


def check_balance():
    print(f"Your current balance is ₹{balance:.2f}")
    print("********************************")


def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"Amount ₹{amount:.2f} deposited successfully.")
    else:
        print("You can't deposit a negative or zero amount.")
    print("********************************")


def withdraw(amount):
    global balance
    if amount <= 0:
        print("You can't withdraw a negative or zero amount.")
    elif amount > balance:
        print("Cannot withdraw. Insufficient balance.")
    else:
        balance -= amount
        print(f"Amount ₹{amount:.2f} withdrawn successfully.")
    print("********************************")


def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)


def check_kyc():
    if len(kyc_documents) == 0:
        print("KYC not done.")
    else:
        print("KYC Documents:")
        for doc in kyc_documents:
            print(f"{doc}: {kyc_documents[doc]}")
    print("********************************")


if __name__ == "__main__":
    print("********************************")
    print("Welcome to ABC Bank")
    print("********************************")

    while True:
        print("\n1. Check your balance")
        print("2. Deposit an amount")
        print("3. Withdraw an amount")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")
        print("********************************")

        if choice == '1':
            check_balance()

        elif choice == '2':
            amt = float(input("Enter the amount to deposit: "))
            deposit(amt)

        elif choice == '3':
            amt = float(input("Enter the amount to withdraw: "))
            withdraw(amt)

        elif choice == '4':
            check_kyc()

        elif choice == '5':
            kyc_docs = {}
            n_documents = int(input("Enter the number of documents you want to add: "))

            for i in range(n_documents):
                key = input("Enter the document type: ")
                value = input("Enter the document number: ")
                kyc_docs[key] = value

            update_kyc(kyc_docs)
            print("KYC updated successfully!")
            print("********************************")

        elif choice == '6':
            print("Quitting. Have a nice day!")
            break

        else:
            print("Invalid choice! Please try again.")
            print("********************************")

    print("Thank you for banking with us.")4