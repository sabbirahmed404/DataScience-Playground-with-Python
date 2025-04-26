import random

def generate_population(pop_size, n):
    return [random.sample(range(n), n) for _ in range(pop_size)]

def fitness(chromosome):
    n = len(chromosome)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(chromosome[i] - chromosome[j]) == j - i:
                conflicts += 1
    return conflicts

def selection(population, elite_size=2):
    """Selects the best individuals from the population based on fitness."""
    population.sort(key=lambda x: fitness(x))
    return population[:elite_size]

def order_crossover(parent1, parent2):
    """Performs Order Crossover (OX1) to create a child permutation."""
    n = len(parent1)
    child = [-1] * n  # Initialize child with placeholders

    start, end = sorted(random.sample(range(n), 2))

    child[start:end+1] = parent1[start:end+1]

    parent2_idx = (end + 1) % n
    child_idx = (end + 1) % n
    elements_in_child = set(child[start:end+1])

    while -1 in child: # While there are still empty slots in the child
        element = parent2[parent2_idx]
        if element not in elements_in_child:
            child[child_idx] = element
            child_idx = (child_idx + 1) % n # Move to the next child slot

        parent2_idx = (parent2_idx + 1) % n

    return child

def swap_mutation(child, mutation_rate=0.1):
    """Performs Swap Mutation on a child chromosome."""
    n = len(child)
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(n), 2)
        child[idx1], child[idx2] = child[idx2], child[idx1]
    return child # Return the child whether mutated or not

def genetic_algorithm(n, pop_size=100, max_generations=1000, elite_size=2, mutation_rate=0.1):
    """Solves the N-Queens problem using a Genetic Algorithm."""
    population = generate_population(pop_size, n)
    generation = 0

    while generation < max_generations:
        population.sort(key=lambda x: fitness(x))

        if fitness(population[0]) == 0:
            return population[0], generation

        next_generation = []

        elites = population[:elite_size]
        next_generation.extend(elites)

        while len(next_generation) < pop_size:
            parent1 = random.choice(elites) # Simple selection from the best
            parent2 = random.choice(elites) # Allow self-pairing for simplicity

            child = order_crossover(parent1, parent2)

            child = swap_mutation(child, mutation_rate)

            next_generation.append(child)

        population = next_generation
        generation += 1

    population.sort(key=lambda x: fitness(x))
    return population[0], generation 

n = 8 
pop_size = 150
max_generations = 500
mutation_rate = 0.15 

best_solution, generations = genetic_algorithm(n, pop_size, max_generations, mutation_rate=mutation_rate)

if best_solution:
    final_fitness = fitness(best_solution)
    if final_fitness == 0:
        print(f"Solution found in {generations} generations:")
        print(best_solution)
        for row in range(n):
            line = ""
            for col in range(n):
                if best_solution[col] == row:
                    line += " Q"
                else:
                    line += " ."
            print(line)
    else:
        print(f"No perfect solution found after {generations} generations.")
        print(f"Best solution found had {final_fitness} conflicts:")
        print(best_solution)
else:
    print("Genetic algorithm failed to run.")
