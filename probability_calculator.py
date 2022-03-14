import copy
import random
# Consider using the modules imported above.

class Hat():
    
    def __init__(self, **kwargs) : 
        self.kwargs = kwargs
        self.contents = []
        for key, value in self.kwargs.items(): 
            for k in range(value) : 
               key = self.kwargs.get('key', key)
               self.contents.append(key)
        
    def draw(self, num_balls) :
        self.num_balls = num_balls
        if self.num_balls >= len(self.contents) : 
            return self.contents
        else : 
            original = self.contents 
            pulled = random.sample(self.contents, num_balls)
            self.contents = [x for x in original if x not in pulled]
            return pulled
            

def experiment(hat, expected_balls, num_balls_drawn, num_experiments) :
    m = 0 
    for x in range(num_experiments) :
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        balls_req = 0
        for key, value in expected_balls.items() :
            if balls_drawn.count(key) >= value : 
                balls_req += 1
        if balls_req == len(expected_balls) : 
            m += 1
        else : 
            m += 0
    
    return m / num_experiments 



#random.seed(95)
hat = Hat(blue=4, red=2, green=6)
print(hat.draw(4))
print(hat.contents)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)

