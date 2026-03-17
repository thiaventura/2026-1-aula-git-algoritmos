# Armazenar tarefas (por enquanto em memória)
tarefas = []

#Loop infinito até o usuário escolher sair
while True:
    #Exibir menu
    print("\n=== TASK MANAGER V1.0 ===")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Buscar por palavra-chave")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ")

    # Validar entrada
    if opcao not in ["1", "2", "3", "4"]:
        print("❌ Opção inválida! Digite 1, 2, 3 ou 4")
        continue

    # Processar opção
    if opcao == "1":
        #Subfunção: criar tarefa
        nome =input("Nome da tarefa: ")
        if nome.strip():  # Validar que não está vazio
            tarefas.append(nome)
            print(f"✔️ Tarefa '{nome}' criada com sucesso!")
        else:
            print("❌ Nome da tarefa não pode ser vazio!")

    elif opcao == "2":
        # Subfunção: listar tarefas
        if len(tarefas) == 0:
            print("📫 Nenhuma tarefa registrada ainda")
        else:
            print("\n📔 Suas tarefas: ")
            for i, tarefa in enumerate(tarefas, 1):
                print(f" {i}. {tarefa}")

    elif opcao == "3":
        palavra = input("Buscar por: ")
        encontradas = [t for t in tarefas if palavra.lower() in t.lower()]
        if len(encontradas) == 0:
            print("❌ Nenhuma tarefa encontrada")
        else:
            print("\n🔎 Resultados: ")
        for i, tarefa in enumerate(encontradas, 1):
            print(f"{i}. {tarefa}")

    elif opcao == "4":
        # Subfunção: sair
        print("👋 Até logo!")
        break