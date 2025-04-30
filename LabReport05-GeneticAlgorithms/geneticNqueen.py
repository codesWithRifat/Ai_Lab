import random


class Individual:
    def __init__(self, N):
        self.fitness = 0
        self.genes = []
        self.geneLength = N
        for _ in range(N):
            self.genes.append(random.randint(0, N - 1))

    def calcFitness(self):
        conflicts = 0
        n = self.geneLength
        for i in range(n):
            for j in range(i + 1, n):
                if self.genes[i] == self.genes[j] or abs(i - j) == abs(self.genes[i] - self.genes[j]):
                    conflicts += 1
        total_pairs = (n * (n - 1)) // 2
        self.fitness = total_pairs - conflicts


class Population:
    def __init__(self, size, N):
        self.popSize = size
        self.individuals = [Individual(N) for _ in range(size)]
        self.fittest = 0

    def getFittest(self):
        max_fit = -1
        max_index = 0
        for i in range(self.popSize):
            if self.individuals[i].fitness > max_fit:
                max_fit = self.individuals[i].fitness
                max_index = i
        self.fittest = max_fit
        return self.individuals[max_index]

    def getSecondFittest(self):
        max1 = 0
        max2 = 0
        for i in range(self.popSize):
            if self.individuals[i].fitness > self.individuals[max1].fitness:
                max2 = max1
                max1 = i
            elif self.individuals[i].fitness > self.individuals[max2].fitness:
                max2 = i
        return self.individuals[max2]

    def getLeastFittestIndex(self):
        min_fit = float('inf')
        min_index = 0
        for i in range(self.popSize):
            if self.individuals[i].fitness < min_fit:
                min_fit = self.individuals[i].fitness
                min_index = i
        return min_index

    def calculateFitness(self):
        for ind in self.individuals:
            ind.calcFitness()
        self.getFittest()


class SimpleDemoGA:
    def __init__(self, N, population_size=10):
        self.population = Population(population_size, N)
        self.fittest = None
        self.secondFittest = None
        self.generationCount = 0
        self.N = N

    def selection(self):
        self.fittest = self.population.getFittest()
        self.secondFittest = self.population.getSecondFittest()

    def crossover(self):
        crossover_point = random.randint(0, self.N - 1)
        # Swap genes up to crossover point
        for i in range(crossover_point):
            temp = self.fittest.genes[i]
            self.fittest.genes[i] = self.secondFittest.genes[i]
            self.secondFittest.genes[i] = temp

    def mutation(self):
        mutation_point = random.randint(0, self.N - 1)
        self.fittest.genes[mutation_point] = random.randint(0, self.N - 1)
        mutation_point = random.randint(0, self.N - 1)
        self.secondFittest.genes[mutation_point] = random.randint(0, self.N - 1)

    def getFittestOffspring(self):
        return self.fittest if self.fittest.fitness > self.secondFittest.fitness else self.secondFittest

    def addFittestOffspring(self):
        self.fittest.calcFitness()
        self.secondFittest.calcFitness()
        least_index = self.population.getLeastFittestIndex()
        self.population.individuals[least_index] = self.getFittestOffspring()


def main():
    N = int(input("Enter number of queens (N): "))
    population_size = 50
    max_fitness = (N * (N - 1)) // 2

    demo = SimpleDemoGA(N, population_size)
    demo.population.calculateFitness()

    print(f"Generation {demo.generationCount}: Fittest = {demo.population.fittest}")

    while demo.population.fittest < max_fitness:
        demo.generationCount += 1
        demo.selection()
        demo.crossover()

        if random.random() < 0.7:
            demo.mutation()

        demo.addFittestOffspring()
        demo.population.calculateFitness()
        print(f"Generation {demo.generationCount}: Fittest = {demo.population.fittest}")

    solution = demo.population.getFittest()
    print(f"\nSolution found in generation {demo.generationCount}")
    print(f"Fitness: {solution.fitness}")

    print("\nResult:")
    for row in range(N):
        line = ['Q' if col == solution.genes[row] else '.' for col in range(N)]
        print(' '.join(line))


if __name__ == "__main__":
    main()