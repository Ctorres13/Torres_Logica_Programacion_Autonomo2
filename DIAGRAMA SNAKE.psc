
	Algoritmo JuegoSnake
		Definir cabezaX, cabezaY, comidaX, comidaY Como Entero
		cabezaX <- 0
		cabezaY <- 0
		comidaX <- 100
		comidaY <- 100
		
		Mientras Verdadero Hacer
			// Lógica de movimiento simplificada
			Escribir "Moviendo serpiente..."
			
			// Condicional de colisión
			Si cabezaX = comidaX Y cabezaY = comidaY Entonces
				Escribir "¡Comiste!"
				comidaX <- Aleatorio(-280, 280)
				comidaY <- Aleatorio(-280, 280)
			SiNo
				Escribir "Creciendo..."
			FinSi
			
			Esperar 100 Milisegundos
		FinMientras
FinAlgoritmo
