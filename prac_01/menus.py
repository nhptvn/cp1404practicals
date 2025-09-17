name = input("Enter name: ")
choice = input("(H)ello\n(G)oodbye\n(Q)uit\n>>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid Choice")
    choice = input("(H)ello\n(G)oodbye\n(Q)uit\n>>> ").upper()
print("Finished.")
