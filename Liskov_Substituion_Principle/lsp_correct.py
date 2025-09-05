from abc import ABC, abstractmethod

class Bird(ABC):
    pass

class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass

class NonFlyingBird(Bird):
    @abstractmethod
    def run(self):
        pass

class Duck(FlyingBird):
    def fly(self):
        return "Duck flying"

class Ostrich(NonFlyingBird):
    def run(self):
        return "Ostrich running fast!"

def make_flying_bird_fly(bird: FlyingBird):
    return bird.fly()

def make_bird_move(bird: Bird):
    if isinstance(bird, FlyingBird):
        return bird.fly()
    elif isinstance(bird, NonFlyingBird):
        return bird.run()

# Теперь все подтипы могут использоваться корректно