import random
from Teclado import Teclado

def main():
    # Generar el número secreto
    numero_secreto = random.randint(1, 100)
    # Declara las variables de intentos
    intentos = 0
    print("Bienvenido al juego: Adivina el Número!")

    # Ejecutar hasta que se acierte
    while True:
        # Se solicita un número entero entre 1 y 100.
        intento = Teclado.read_integer("Adivina el número (entre 1 y 100):", min_value=1, max_value=100)
        # Aumenta los intentos después de ingresar un número valido.
        intentos += 1
        # Verificación
        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
if __name__ == "__main__":
    main()
