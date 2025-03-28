from Teclado import Teclado

def main():
    # Se solicitan dos números decimales.
    num1 = Teclado.read_double("Ingrese el primer número:")
    num2 = Teclado.read_double("Ingrese el segundo número:")

    # Se solicita la operación a realizar.
    operacion = Teclado.read_text("Ingrese la operación (+, -, *, /):", min_length=1, max_length=1)

    # Verifica la operación que se va a ejecutar
    resultado = None
    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        # Evitar que muera la aplicación si se divide entre cero.
        try:
            resultado = num1 / num2
        except ZeroDivisionError:
            print("Error: División por cero no es permitida.")
            return
    else:
        print("Operación no válida.")
        return

    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
