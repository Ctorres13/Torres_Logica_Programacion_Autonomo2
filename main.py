"""
UNIVERSIDAD INTERNACIONAL DEL ECUADOR (UIDE)
Asignatura: Lógica de Programación - Proyecto Integrador
Autor: Torres Alberca Christian Daniel
Sistema: Juego de la Serpiente (Snake Game) - Arquitectura Modular MVC
"""

import turtle
import time
import random

# ==========================================
# 1. MODELO (Capa de Datos y Estados)
# ==========================================
class SnakeModel:
    def __init__(self):
        self.body = [[0, 0]]
        self.direction = "stop"
        self.food = [100, 100]
        self.score = 0

# ==========================================
# 2. VISTA (Interfaz de Usuario Gráfica)
# ==========================================
class SnakeView:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(600, 600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game - Arquitectura MVC (UIDE)")
        self.screen.tracer(0) 
        
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        
        self.score_pen = turtle.Turtle()
        self.score_pen.hideturtle()
        self.score_pen.color("white")

    def draw(self, model):
        self.pen.clear()
        
        # ESTRUCTURA REPETITIVA (For): Renderiza cada segmento del cuerpo
        for segment in model.body:
            self.pen.penup()
            self.pen.goto(segment[0], segment[1])
            self.pen.dot(20, "green")
            
        # Renderizado de la Comida
        self.pen.penup()
        self.pen.goto(model.food[0], model.food[1])
        self.pen.dot(20, "red")
        
        # Renderizado de Puntuación
        self.score_pen.clear()
        self.score_pen.goto(0, 260)
        self.score_pen.write(f"Puntuación: {model.score}", align="center", font=("Courier", 24, "normal"))
        self.screen.update()

# ==========================================
# 3. CONTROLADOR (Lógica de Juego)
# ==========================================
class SnakeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.screen.listen()
        
        self.view.screen.onkey(lambda: setattr(self.model, 'direction', 'up') if self.model.direction != 'down' else None, "Up")
        self.view.screen.onkey(lambda: setattr(self.model, 'direction', 'down') if self.model.direction != 'up' else None, "Down")
        self.view.screen.onkey(lambda: setattr(self.model, 'direction', 'left') if self.model.direction != 'right' else None, "Left")
        self.view.screen.onkey(lambda: setattr(self.model, 'direction', 'right') if self.model.direction != 'left' else None, "Right")

    def run(self):
        # ESTRUCTURA REPETITIVA (While): Motor del juego (Game Loop)
        while True:
            head = self.model.body[0][:]
            
            # ESTRUCTURAS CONDICIONALES (If-Elif): Control de dirección
            if self.model.direction == "up": head[1] += 20
            elif self.model.direction == "down": head[1] -= 20
            elif self.model.direction == "left": head[0] -= 20
            elif self.model.direction == "right": head[0] += 20
            
            if self.model.direction != "stop":
                # CONDICIONALES DE COLISIÓN
                if head[0] > 280 or head[0] < -280 or head[1] > 280 or head[1] < -280 or head in self.model.body:
                    self.reiniciar_juego()
                else:
                    self.model.body.insert(0, head)
                    # Verificación de consumo de alimento
                    if abs(head[0] - self.model.food[0]) < 20 and abs(head[1] - self.model.food[1]) < 20:
                        self.model.food = [random.randint(-14, 14)*20, random.randint(-14, 14)*20]
                        self.model.score += 10
                    else:
                        self.model.body.pop()
            
            self.view.draw(self.model)
            time.sleep(0.1)

    def reiniciar_juego(self):
        print(f"¡Game Over! Puntuación final: {self.model.score}")
        time.sleep(1) # Pausa para que el usuario visualice el fin del juego
        self.model.body = [[0, 0]]
        self.model.score = 0
        self.model.direction = "stop"

if __name__ == "__main__":
    controller = SnakeController(SnakeModel(), SnakeView())
    controller.run()
