"""
UNIVERSIDAD INTERNACIONAL DEL ECUADOR (UIDE)
Asignatura: Lógica de Programación - Autónomo 2
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
        # Estructura de lista compleja para almacenar los segmentos corporales
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
        self.screen.tracer(0) # Desactiva actualizaciones automáticas para optimizar memoria
        
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        
        self.score_pen = turtle.Turtle()
        self.score_pen.hideturtle()
        self.score_pen.color("white")

    def draw(self, model):
        self.pen.clear()
        
        """
        ESTRUCTURA REPETITIVA (Bucle For)
        Itera dinámicamente a través de los segmentos del cuerpo de la serpiente
        para renderizar cada posición en la interfaz gráfica.
        """
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
# 3. CONTROLADOR (Lógica de Juego y Reglas)
# ==========================================
class SnakeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.screen.listen()
        
        # Captura de eventos del teclado (Interacción del Usuario)
        self.view.screen.onkey(lambda: setattr(self.model, 'direction', 'up') if self.model.direction != 'down' else None, "Up")
        self.view.screen.onkey(lambda: setattr(self.model, 'direction', 'down') if self.model.direction != 'up' else None, "Down")
        self.view.screen.onkey(lambda: setattr(self.model, 'direction', 'left') if self.model.direction != 'right' else None, "Left")
        self.view.screen.onkey(lambda: setattr(self.model, 'direction', 'right') if self.model.direction != 'left' else None, "Right")

    def run(self):
        """
        ESTRUCTURA REPETITIVA PRINCIPAL (Bucle While Infinito)
        Actúa como el motor de ciclo de juego continuo (Game Loop)
        manteniendo la aplicación activa hasta que el proceso sea interrumpido.
        """
        while True:
            # Copia la cabeza de la serpiente para calcular el siguiente movimiento
            head = self.model.body[0][:]
            
            """
            ESTRUCTURAS LÓGICAS CONDICIONALES MÚLTIPLES (If-Elif)
            Evalúa la dirección actual asignada por el controlador para
            transformar las coordenadas de la cabeza sobre el plano cartesiano.
            """
            if self.model.direction == "up": 
                head[1] += 20
            elif self.model.direction == "down": 
                head[1] -= 20
            elif self.model.direction == "left": 
                head[0] -= 20
            elif self.model.direction == "right": 
                head[0] += 20
            
            """
            ESTRUCTURA CONDICIONAL ANIDADA
            Verifica si el juego ha iniciado oficialmente. Evita ejecuciones en estado 'stop'.
            """
            if self.model.direction != "stop":
                
                # CONDICIONAL: Validación Crítica de Colisiones contra las Paredes (Límites del Mapa)
                if head[0] > 280 or head[0] < -280 or head[1] > 280 or head[1] < -280:
                    self.reiniciar_juego()
                    
                # CONDICIONAL: Validación Crítica de Auto-colisión (Chocar contra su propio cuerpo)
                elif head in self.model.body:
                    self.reiniciar_juego()
                    
                else:
                    # Avanza insertando la nueva posición de la cabeza
                    self.model.body.insert(0, head)
                    
                    # CONDICIONAL: Verificación de Proximidad y Consumo de Alimento
                    if abs(head[0] - self.model.food[0]) < 20 and abs(head[1] - self.model.food[1]) < 20:
                        # Reposiciona la comida usando cálculos pseudoaleatorios controlados
                        self.model.food = [random.randint(-14, 14)*20, random.randint(-14, 14)*20]
                        self.model.score += 10
                    else:
                        # Si no come, remueve el último segmento para simular desplazamiento continuo
                        self.model.body.pop()
            
            # Actualiza la pantalla mediante la Capa de Vista
            self.view.draw(self.model)
            time.sleep(0.1)

    def reiniciar_juego(self):
        """Restablece los estados lógicos del Modelo al ocurrir un Game Over."""
        self.model.body = [[0, 0]]
        self.model.score = 0
        self.model.direction = "stop"

if __name__ == "__main__":
    # Inicialización del ecosistema bajo el patrón arquitectónico modular
    controller = SnakeController(SnakeModel(), SnakeView())
    controller.run()
