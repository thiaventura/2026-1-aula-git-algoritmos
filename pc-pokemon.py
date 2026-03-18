pc = []  #This is the list where you fill with something

#This is how we begin the loop
while True:

#This is the interface
    print("\n=== Beep Boop Boop Beep ===")
    print("1 - Deposit")
    print("2 - List")
    print("3 - Search")
    print("4 - Delete")
    print("5 - Leave")

    opcao = input("Choose: ")

#This is where the fun begins
    if opcao not in ["1", "2", "3", "4", "5"]:
        print("❌ Opção inválida")
        continue

#This is used to add something
    if opcao == "1":
        nome = input("Choose a Pokémon to store: ")

        if nome.strip():
            pc.append(nome)
            print("Deposited successfully!")
        else:
            print("MissingNo.")

#This is used to check if you added something
    elif opcao == "2":
        if not pc:
            print("You have no Pokémon 😭")
        else:
            print("\n📦 Your Pokémon: ")
            for i, pokemon in enumerate(pc, 1):
                print(f"{i}. {pokemon}")

#This is used to search something you add
    elif opcao == "3":
        poke = input("Search: ")

        found = [p for p in pc if poke.lower() in p.lower()]

        if not found:
            print("MissingNo.")
        else:
            for p in found:
                print(p)

    elif opcao == "4":
        if not pc:
            print("Nothing happens.")
        else:
            print("\nYour Pokémon: ")
            for i, pokemon in enumerate(pc, 1):
                print(f"{i}.{pokemon}")

            try:
                index = int(input("Type the Pokémon you want to delete. (Type the number) "))

                if 1 <= index <= len(pc):
                    removida = pc.pop(index - 1)
                    print(f"... '{removida}' Is gone.")
                else:
                    print("MissingNo.")

            except ValueError:
                print("Please. Type a valid number!")

    elif opcao == "5":
        print("See ya!")
        break