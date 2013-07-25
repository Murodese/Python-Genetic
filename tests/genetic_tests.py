from nose.tools import *
import genetic
import random
import string

def setup():
    pass

def test_shakespeare():
    def gen_func(dna):
        """Used to initialise DNA. Should return a single gene - in this case,
        a letter"""
        return random.choice(string.letters + ' ,.?')

    def eval_func(dna):
        """Used to evaluate fitness of DNA. Should return a fitness value, 0-1
        where higher is better."""
        score = 0
        for index, gene in enumerate(dna.genes):
            if gene == target[index]:
                score += 1
        fitness = score / float(len(target))
        return fitness

    def mut_func(dna):
        """Used to mutate a gene. Should return a single gene."""
        return random.choice(string.letters + ' ,.')

    target = "Is Kevin a giant faglord? Yes."

    population = genetic.Population(200)
    population.setup(gen_func, eval_func, mut_func, gene_length = len(target))

    (generation, dna) = population.run(1.0)
    print('Finished!')
    print('Generation: ' + str(generation))
    print('DNA: ' + ''.join(dna.genes))

def teardown():
    pass

