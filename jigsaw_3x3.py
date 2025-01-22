from queue import PriorityQueue

def manhattan_distance(start, goal):
    distance = 0
    for i in range(1, 9):
        start_x, start_y = divmod(start.index(i), 3)
        goal_x, goal_y = divmod(goal.index(i), 3)
        distance += abs(start_x - goal_x) + abs(start_y - goal_y)
    return distance

def move(state):
    moves = []
    zero_index = state.index(0)
    zero_x, zero_y = divmod(zero_index, 3)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for direction in directions:
        new_x, new_y = zero_x + direction[0], zero_y + direction[1]
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            moves.append(new_state)
    
    return moves

def puzzle(start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {tuple(start): 0}
    f_score = {tuple(start): manhattan_distance(start, goal)}
    
    while not open_set.empty():
        _, current = open_set.get()
        
        if current == goal:
            path = []
            while tuple(current) in came_from:
                current = came_from[tuple(current)]
                path.append(current)
            return path[::-1]
        
        for neighbor in move(current):
            tentative_g_score = g_score[tuple(current)] + 1
            
            if tuple(neighbor) not in g_score or tentative_g_score < g_score[tuple(neighbor)]:
                came_from[tuple(neighbor)] = current
                g_score[tuple(neighbor)] = tentative_g_score
                f_score[tuple(neighbor)] = tentative_g_score + manhattan_distance(neighbor, goal)
                open_set.put((f_score[tuple(neighbor)], neighbor))
    
    return None

def print_puzzle(state):
    for i in range(3):
        print(state[i*3:(i+1)*3])
    print()

try:
    print("Digite a primeira linha (3 dígitos separados por espaço):")
    linha1 = list(map(int, input().split()))
    if len(linha1) != 3:
        raise ValueError("A linha deve conter exatamente 3 dígitos.")
    print(f"Primeira linha: {linha1}")
    
    print("Digite a segunda linha (3 dígitos separados por espaço):")
    linha2 = list(map(int, input().split()))
    if len(linha2) != 3:
        raise ValueError("A linha deve conter exatamente 3 dígitos.")
    print(f"Segunda linha: {linha2}")
    
    print("Digite a terceira linha (3 dígitos separados por espaço):")
    linha3 = list(map(int, input().split()))
    if len(linha3) != 3:
        raise ValueError("A linha deve conter exatamente 3 dígitos.")
    print(f"Terceira linha: {linha3}")
    
    inicio = linha1 + linha2 + linha3
    print(f"Estado inicial: {inicio}")
    
    if len(inicio) != 9 or sorted(inicio) != list(range(9)):
        raise ValueError("O estado inicial deve conter os números de 0 a 8 exatamente uma vez.")
    
    confirmacao = input(f"Você confirma esta sequência? {inicio} (s/n): ")
    if confirmacao.lower() != 's':
        raise ValueError("Sequência não confirmada pelo usuário.")
    
    solucao = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    calc = puzzle(inicio, solucao)

    if calc:
        print(f"Número de movimentos necessários: {len(calc)}")
        passos = 0
        for step in calc:
            passos += 1
            print(f"Passo {passos}:")
            print_puzzle(step)
    else:
        print("Não foi possível encontrar uma solução para o puzzle.")
except ValueError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

input("Pressione Enter para sair...")
