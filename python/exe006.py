# A gente começa com um dicionário vazio para guardar nossos times.
teams = {} 
# Essa variável vai nos dizer quando o programa deve parar.
done = False

# Função para listar os times de um jeito bonito.
def print_teams():
    print("\n--- Times Listados ---")
    if not teams:
        print("Nenhum time cadastrado ainda.")
        return
        
    # Usamos uma lista temporária para garantir que a ordem dos números seja sempre a mesma.
    team_names = list(teams.keys())
    for i, team_name in enumerate(team_names):
        # Acessamos o time pelo seu nome (a chave do dicionário)
        team_data = teams[team_name]
        # Mostramos o índice (i+1), o nome e a quantidade de jogadores.
        print(f"{i+1}. {team_data['name']} ({len(team_data['players'])} jogadores)")
    print("----------------------\n")

# Função para listar os jogadores de um time específico.
def print_team_players(team):
    print(f"\n--- Jogadores do Time: {team['name']} ---")
    if not team['players']:
        print("Este time não tem jogadores ainda.")
    else:
        for i, player in enumerate(team['players']):
            print(f"{i+1}. {player}")
    print("----------------------------------\n")

# O loop principal que mantém nosso programa rodando!
while not done:
    # Mostra o menu de opções a cada rodada.
    print("O que você deseja fazer?")
    print("1. Adicionar um time")
    print("2. Remover um time")
    print("3. Listar times")
    print("4. Adicionar jogador em um time")
    print("5. Remover jogador de um time")
    print("6. Listar jogadores de um time")
    print("7. Sair")
    
    # Pede para o usuário escolher uma opção.
    choice = input("> ")

    # Agora, o programa decide o que fazer com base na escolha.
    
    # 1. Adiciona um time
    if choice == "1":
        team_name = input("Digite o nome do time: ")
        if team_name in teams:
            print("Erro: Já existe um time com esse nome!")
        else:
            teams[team_name] = {'name': team_name, 'players': []}
            print(f"Time '{team_name}' adicionado com sucesso!")
    
    # 2. Remove um time
    elif choice == "2":
        if not teams:
            print("Não há times para remover.")
        else:
            print_teams()
            try:
                team_num = int(input("Informe o número do time para remover: "))
                team_names = list(teams.keys())
                if 1 <= team_num <= len(team_names):
                    team_to_remove = team_names[team_num-1]
                    del teams[team_to_remove]
                    print(f"Time '{team_to_remove}' removido.")
                else:
                    print("Número de time inválido.")
            except ValueError:
                print("Erro: Por favor, digite um número.")

    # 3. Lista times
    elif choice == "3":
        print_teams()
    
    # 4. Adicionar jogador em um time
    elif choice == "4":
        if not teams:
            print("Não há times para adicionar jogadores.")
        else:
            print_teams()
            try:
                team_num = int(input("Informe o número do time: "))
                team_names = list(teams.keys())
                if 1 <= team_num <= len(team_names):
                    team_name = team_names[team_num-1]
                    player_name = input(f"Informe o nome do jogador para adicionar ao '{team_name}': ")
                    teams[team_name]['players'].append(player_name)
                    print(f"Jogador '{player_name}' adicionado ao time '{team_name}'.")
                else:
                    print("Número do time inválido")
            except ValueError:
                print("Erro: Por favor, digite um número.")


    # 5. Remove jogador de um time
    elif choice == "5":
        if not teams:
            print("Não há times para remover jogadores.")
        else:
            print_teams()
            try:
                team_num = int(input("Informe o número do time: "))
                team_names = list(teams.keys())
                if 1 <= team_num <= len(team_names):
                    team_name = team_names[team_num-1]
                    team_data = teams[team_name]
                    
                    if not team_data['players']:
                        print("Este time não tem jogadores para remover.")
                    else:
                        print_team_players(team_data)
                        player_num = int(input("Informe o número do jogador para remover: "))
                        if 1 <= player_num <= len(team_data['players']):
                            player_removed = team_data['players'].pop(player_num-1)
                            print(f"Jogador '{player_removed}' removido do time '{team_name}'.")
                        else:
                            print("Número do jogador inválido.")
                else:
                    print("Número do time inválido.")
            except ValueError:
                print("Erro: Por favor, digite um número.")


    # 6. Lista jogadores de um time
    elif choice == "6":
        if not teams:
            print("Não há times para listar jogadores.")
        else:
            print_teams()
            try:
                team_num = int(input("Informe o número do time: "))
                team_names = list(teams.keys())
                if 1 <= team_num <= len(team_names):
                    team_name = team_names[team_num-1]
                    print_team_players(teams[team_name])
                else:
                    print("Número do time inválido.")
            except ValueError:
                print("Erro: Por favor, digite um número.")

    # 7. Sair
    elif choice == "7":
        print("Até mais! Obrigado por usar o Gerenciador de Times.")
        done = True

    # Opção inválida
    else:
        print("Opção inválida. Por favor, escolha um número de 1 a 7.")