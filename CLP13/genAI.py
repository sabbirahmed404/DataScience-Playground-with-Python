import random
import numpy as np

def genetic_algorithm_sum(target, list_length, population_size=100, generations=100):
    population = [
        [random.randint(0, 9) for _ in range(list_length)]
        for _ in range(population_size)
    ]
    
    for generation in range(generations):
        fitness_scores = [calculate_fitness(individual, target) for individual in population]
        
        best_individual = get_best_individual(population, target)
        best_fitness = calculate_fitness(best_individual, target)
        
        if best_fitness == 1000:  
            return best_individual
        
        new_population = [best_individual]
        
        while len(new_population) < population_size:
            parent1 = tournament_selection(population, fitness_scores)
            parent2 = tournament_selection(population, fitness_scores)
            
            child = crossover(parent1, parent2)
            
            if random.random() < 0.2:  
                mutate(child)
                
            new_population.append(child)
        
        population = new_population
    
    best_individual = get_best_individual(population, target)
    return best_individual

def calculate_fitness(individual, target):
    total = sum(individual)
    return 1000 if total == target else 100 / (1 + abs(total - target))

def get_best_individual(population, target):
    best_individual = population[0]
    best_fitness = calculate_fitness(best_individual, target)
    
    for individual in population[1:]:
        fitness = calculate_fitness(individual, target)
        if fitness > best_fitness:
            best_individual = individual
            best_fitness = fitness
            
    return best_individual

def tournament_selection(population, fitness_scores):
    selected = random.sample(range(len(population)), 3)
    best_fitness = fitness_scores[selected[0]]
    best_idx = selected[0]
    
    for idx in selected[1:]:
        if fitness_scores[idx] > best_fitness:
            best_fitness = fitness_scores[idx]
            best_idx = idx
    
    return population[best_idx]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    return parent1[:crossover_point] + parent2[crossover_point:]

def mutate(individual):
    individual[random.randint(0, len(individual) - 1)] = random.randint(0, 9)

def solve_case(target, list_length):
    return genetic_algorithm_sum(target, list_length)

print("Case 1:", solve_case(7, 2))  
print("Case 2:", solve_case(10, 3))
