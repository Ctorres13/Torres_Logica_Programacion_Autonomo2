import turtle
import time
import random

#Datos y Estado del juego 
class SnakeModel:
    def __init__(self):
        self.body = [[0, 0]]  
        self.direction = "stop"
        self.food = [100, 100]

#Renderizado
class SnakeView:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(600, 600)
        self.screen.bgcolor("black")
        self.screen.tracer(0) 
        self.pen = turtle.Turtle()
        self.pen.hideturtle()

    def draw(self, model):
        self.pen.clear()
        # Dibujar serpiente
        for segment in model.body:
            self.pen.penup()
            self.pen.goto(segment[0], segment[1])
            self.pen.dot(20, "green")
        # Dibujar comida
        self.pen.penup()
        self.pen.goto(model.food[0], model.food[1])
        self.pen.dot(20, "red")
        self.screen.update()

# Lógica 
class SnakeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # Controlador
        self.view.screen.listen()
        self.view.screen.onkey(lambda: self.set_dir("up"), "Up")
        self.view.screen.onkey(lambda: self.set_dir("down"), "Down")
        self.view.screen.onkey(lambda: self.set_dir("left"), "Left")
        self.view.screen.onkey(lambda: self.set_dir("right"), "Right")

    def set_dir(self, direction):
        self.model.direction = direction

    def run(self):
        while True:
            # movimiento
            head = self.model.body[0][:]
            if self.model.direction == "up": head[1] += 20
            elif self.model.direction == "down": head[1] -= 20
            elif self.model.direction == "left": head[0] -= 20
            elif self.model.direction == "right": head[0] += 20
            
            if self.model.direction != "stop":
                self.model.body.insert(0, head)
                
                # colisión con comida
                if abs(head[0] - self.model.food[0]) < 20 and abs(head[1] - self.model.food[1]) < 20:
                    self.model.food = [random.randint(-280, 280), random.randint(-280, 280)]
                else:
                    self.model.body.pop() # Eliminar cola si no comió
            
            self.view.draw(self.model)
            time.sleep(0.1)

if __name__ == "__main__":
    model = SnakeModel()
    view = SnakeView()
    controller = SnakeController(model, view)
    controller.run()
    