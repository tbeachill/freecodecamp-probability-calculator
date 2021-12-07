import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []

        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self, num):
        # accepts number of balls to draw and randomly draws that amount
        # if the number to draw exceeds the number of balls, draw all
        balls = []
        if num < len(self.contents):
            for _ in range(num):
                balls.append(self.contents.pop(random.randrange(len(self.contents))))
        else:
            balls = self.contents

        return balls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # determine probability of drawing a given number of each ball

    expected_no_of_balls = []
    for value in expected_balls.values():
        expected_no_of_balls.append(value)
    
    success = 0
    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls = new_hat.draw(num_balls_drawn)

        no_of_balls = []
        for key in expected_balls:
            no_of_balls.append(balls.count(key))

        if no_of_balls >= expected_no_of_balls:
            success += 1

    probability = success / num_experiments

    return probability
