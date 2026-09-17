def menu():
    while True:
        print("\n==========================")
        print("        CryptoLabX")
        print("==========================")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Attack")
        print("4. Analyze")
        print("5. Exit")
        print("==========================")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Encryption module: Coming Soon")

        elif choice == "2":
            print("Decryption module: Coming Soon")

        elif choice == "3":
            print("Attack module: Coming Soon")

        elif choice == "4":
            print("Analysis module")

        elif choice == "5":
            print("Exiting CryptoLabX...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()