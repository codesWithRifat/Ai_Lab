import random

class Individual:
    def __init__(self, k):
        self.fitness = 0
        self.gene_length = k
        self.genes = [random.randint(1, 9) for _ in range(self.gene_length)]

    def calc_fitness(self, T):
        total = sum(self.genes)
        self.fitness = T - abs(total - T)


class Population:
    def __init__(self, size, k):
        self.pop_size = size
        self.individuals = [Individual(k) for _ in range(size)]
        self.fittest = 0

    def get_fittest(self):
        max_fit = -1
        max_fit_index = 0
        for i, individual in enumerate(self.individuals):
            if individual.fitness >= max_fit:
                max_fit = individual.fitness
                max_fit_index = i
        self.fittest = self.individuals[max_fit_index].fitness
        return self.individuals[max_fit_index]

    def get_second_fittest(self):
        max_fit1 = 0
        max_fit2 = 0
        for i in range(len(self.individuals)):
            if self.individuals[i].fitness > self.individuals[max_fit1].fitness:
                max_fit2 = max_fit1
                max_fit1 = i
            elif self.individuals[i].fitness > self.individuals[max_fit2].fitness:
                max_fit2 = i
        return self.individuals[max_fit2]

    def get_least_fittest_index(self):
        min_fit_val = float('inf')
        min_fit_index = 0
        for i, individual in enumerate(self.individuals):
            if individual.fitness <= min_fit_val:
                min_fit_val = individual.fitness
                min_fit_index = i
        return min_fit_index

    def calculate_fitness(self, T):
        for individual in self.individuals:
            individual.calc_fitness(T)
        self.get_fittest()


class SimpleDemoGA:
    def __init__(self, T, k, size=10):
        self.T = T
        self.k = k
        self.population = Population(size, k)
        self.fittest = None
        self.second_fittest = None
        self.generation_count = 0

    def selection(self):
        self.fittest = self.population.get_fittest()
        self.second_fittest = self.population.get_second_fittest()

    def crossover(self):
        crossover_point = random.randint(0, self.fittest.gene_length - 1)
        for i in range(crossover_point):
            self.fittest.genes[i], self.second_fittest.genes[i] = self.second_fittest.genes[i], self.fittest.genes[i]

    def mutation(self):
        mutation_point = random.randint(0, self.fittest.gene_length - 1)
        self.fittest.genes[mutation_point] = random.randint(0, 9)
        mutation_point = random.randint(0, self.second_fittest.gene_length - 1)
        self.second_fittest.genes[mutation_point] = random.randint(0, 9)

    def get_fittest_offspring(self):
        if self.fittest.fitness > self.second_fittest.fitness:
            return self.fittest
        return self.second_fittest

    def add_fittest_offspring(self):
        self.fittest.calc_fitness(self.T)
        self.second_fittest.calc_fitness(self.T)
        least_fittest_index = self.population.get_least_fittest_index()
        self.population.individuals[least_fittest_index] = self.get_fittest_offspring()


def main(T, k):
    demo = SimpleDemoGA(T, k)
    demo.population.calculate_fitness(demo.T)
    print(f"Generation: {demo.generation_count} Fittest: {demo.population.fittest}")

    while demo.population.fittest < demo.T:
        demo.generation_count += 1
        demo.selection()
        demo.crossover()
        if random.randint(0, 6) < 5:
            demo.mutation()
        demo.add_fittest_offspring()
        demo.population.calculate_fitness(demo.T)
        print(f"Generation: {demo.generation_count} Fittest: {demo.population.fittest}")

    print(f"\nSolution found in generation {demo.generation_count}")
    print(f"Fitness: {demo.population.get_fittest().fitness}")
    print("Genes: " + ' '.join(map(str, demo.population.get_fittest().genes)))


if __name__ == "__main__":

    T = int(input())
    k = int(input())
    main(T, k)