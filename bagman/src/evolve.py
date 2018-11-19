

class Evolve:
    def __init__(self, generation, delta_stop):
        self.generation = generation.create_generation()
        self.delta_stop = delta_stop

    def __str__(self):
        return 'Evolve: [generation: {}]'.format(self.generation)

    def get_scores(self):
        return sorted([x.score for x in self.generation.units])

    def get_best_score(self):
        return sorted(self.generation.units, key=lambda x: x.score)[0]

    def run(self):
        last_score = 0
        last_score_idx = 0
        infinite_idx = 0
        while infinite_idx >= 0:
            infinite_idx += 1
            multiplication = self.generation.create_multiplication()
            self.generation = self.generation.elimination(self.generation, multiplication)

            if (infinite_idx % 100) == 0:
                print('Iteration: {}, Scores: {}'.format(infinite_idx, self.get_scores()[0]))

            if last_score != self.get_scores()[0]:
                last_score = self.get_scores()[0]
                last_score_idx = infinite_idx

            if infinite_idx - last_score_idx > self.delta_stop:
                break
