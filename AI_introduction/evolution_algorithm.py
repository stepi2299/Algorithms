import numpy as np
import random
from cec2017.functions import f4, f5
import time


class EvolutionAlg:
    dimensions = 10
    bound = 100

    def __init__(
        self,
        ob_func,
        population_size,
        mutate_probability=0.1,
        crossing_probability=0.7,
        iteration_max=500,
        sigma=0.5,
        best_safe=1,
    ):
        random.seed(time.perf_counter())
        self.objective_function = ob_func
        self.population_size = population_size
        self.best_safe = best_safe
        self.mutate_probability = mutate_probability
        self.crossing_probability = crossing_probability
        self.iteration_max = iteration_max
        self.population = self._create_population(
            EvolutionAlg.bound, EvolutionAlg.dimensions
        )
        self.sigma = sigma

    def _create_population(self, bound, dims):
        pop = []
        for i in range(self.population_size):
            pop.append(np.random.uniform(-bound, bound, size=dims))
        return pop

    def look_for_optimum(self):
        t = 0
        quality = []
        for pop in self.population:
            quality.append(self.objective_function(pop))
        idx = np.argmin(quality)
        best_individual, min_val = self.population[idx], quality[idx]
        while t < self.iteration_max:
            print(f"iteration: {t}, pos: {best_individual}, val: {min_val}")
            reproduction = self.reproduction(self.population, quality)
            # crossing

            mutation = self.mutate(
                reproduction, self.mutate_probability, sig=self.sigma
            )
            new_quality = [
                self.objective_function(individual) for individual in mutation
            ]
            idx = np.argmin(new_quality)
            new_best_individual, new_min_val = mutation[idx], new_quality[idx]
            if new_min_val <= min_val:
                min_val = new_min_val
                best_individual = new_best_individual
            self.population, quality = self.succession(
                self.population,
                mutation,
                quality,
                new_quality,
                best_safe=self.best_safe,
            )
            t += 1
        return best_individual, min_val

    def crossing(self):
        pass

    def reproduction(self, population, population_values) -> list:
        pop_size = len(population)
        idxes = np.argsort(population_values)
        new_population = [population[idx] for idx in idxes]
        new_population_values = [population_values[idx] for idx in idxes]
        reproducted_population = []
        for i in range(pop_size):
            idx1 = random.randint(0, pop_size - 1)
            idx2 = random.randint(0, pop_size - 1)
            reproducted_population.append(
                self._fight(
                    new_population[idx1],
                    new_population_values[idx1],
                    new_population[idx2],
                    new_population_values[idx2],
                )
            )
        return reproducted_population

    @staticmethod
    def _fight(obj1, val1, obj2, val2):
        if val1 < val2:
            return obj1
        else:
            return obj2

    @staticmethod
    def succession(
        base_population, mutate_population, quality, mutate_quality, best_safe=1
    ):
        for i in range(best_safe):
            best_idx = np.argmin(quality)
            worst_idx = np.argmax(mutate_quality)
            mutate_population[worst_idx] = base_population[best_idx]
            mutate_quality[worst_idx] = quality[best_idx]
            del base_population[best_idx]
            del quality[best_idx]
        return mutate_population, mutate_quality

    def mutate(self, population, probability, sig):
        new_population = []
        i = 0
        for pop in population:
            changed_pop = pop.copy()
            rand = random.randint(0, 9)
            if rand <= 10 * probability:
                new_population.append(self._mutate(changed_pop, sig))
            i += 1
        return new_population

    @staticmethod
    def _mutate(individual, sig) -> list:
        for i, ind in enumerate(individual):
            gauss = random.gauss(0, 1)
            new = ind + sig * gauss
            if new > EvolutionAlg.bound or new < -EvolutionAlg.bound:
                ind = np.random.uniform(-EvolutionAlg.bound, EvolutionAlg.bound, size=1)
            else:
                ind = new
            individual[i] = ind
        return individual


alg = EvolutionAlg(
    f5, 40, sigma=2, mutate_probability=1, iteration_max=250, best_safe=0
)
best, val = alg.look_for_optimum()
print("BEST:")
print(best)
print(val)
