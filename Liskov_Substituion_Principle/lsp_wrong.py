class Bird:
    def fly(self):
        return "Flying"

class Duck(Bird):
    def fly(self):
        return "Duck flying"

class Ostrich(Bird):  # Страус не может летать!
    def fly(self):
        raise Exception("Ostriches can't fly!")
    # Нарушение LSP: нельзя использовать Ostrich вместо Bird

def make_bird_fly(bird: Bird):
    try:
        return bird.fly()
    except Exception as e:
        return f"Error: {e}"

# Проблема: код, ожидающий Bird, не работает с Ostrich