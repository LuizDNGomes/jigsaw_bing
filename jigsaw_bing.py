from queue import PriorityQueue

# Função para calcular a distância de Manhattan
def manhattan_distance(start, goal):
    distance = 0
    for i in range(1, 9):
        start_x, start_y = divmod(start.index(i), 3)
        goal_x, goal_y = divmod(goal.index(i), 3)
        distance += abs(start_x - goal_x) + abs(start_y - goal_y)
    return distance

# Função para gerar os movimentos possíveis
def generate_moves(state):
    moves = []
    zero_index = state.index(0)
    zero_x, zero_y = divmod(zero_index, 3)
    
    # Definir movimentos possíveis (cima, baixo, esquerda, direita)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for direction in directions:
        new_x, new_y = zero_x + direction[0], zero_y + direction[1]
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            moves.append(new_state)
    
    return moves

# Algoritmo A* para resolver o puzzle
def solve_puzzle(start, goal):
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
        
        for neighbor in generate_moves(current):
            tentative_g_score = g_score[tuple(current)] + 1
            
            if tuple(neighbor) not in g_score or tentative_g_score < g_score[tuple(neighbor)]:
                came_from[tuple(neighbor)] = current
                g_score[tuple(neighbor)] = tentative_g_score
                f_score[tuple(neighbor)] = tentative_g_score + manhattan_distance(neighbor, goal)
                open_set.put((f_score[tuple(neighbor)], neighbor))
    
    return None

# Função para imprimir o estado do puzzle
def print_puzzle(state):
    for i in range(3):
        print(state[i*3:(i+1)*3])
    print()

# Obter o estado inicial do usuário com verificações e depuração
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
    
    start_state = linha1 + linha2 + linha3
    print(f"Estado inicial: {start_state}")
    
    if len(start_state) != 9 or sorted(start_state) != list(range(9)):
        raise ValueError("O estado inicial deve conter os números de 0 a 8 exatamente uma vez.")
    
    # Confirmar a sequência completa com o usuário
    confirmacao = input(f"Você confirma esta sequência? {start_state} (s/n): ")
    if confirmacao.lower() != 's':
        raise ValueError("Sequência não confirmada pelo usuário.")
    
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    # Resolver o puzzle
    solution_path = solve_puzzle(start_state, goal_state)

    if solution_path:
        print(f"Solução encontrada! Número de movimentos necessários: {len(solution_path)}")
        step_count = 0
        for step in solution_path:
            step_count += 1
            print(f"Passo {step_count}:")
            print_puzzle(step)
    else:
        print("Não foi possível encontrar uma solução para o puzzle.")
except ValueError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

input("Pressione Enter para sair...")
