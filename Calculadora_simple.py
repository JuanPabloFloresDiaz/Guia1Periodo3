from Teclado import Teclado

""" Inicia el programa utilizando clase main """
def main():
    # Se solicitan dos números decimales.
    num1 = Teclado.read_double("Ingrese el primer número:") #pide el número 1
    num2 = Teclado.read_double("Ingrese el segundo número:") #pide el número 2

    # Se solicita la operación a realizar.
    operacion = Teclado.read_text("Ingrese la operación (+, -, *, /):", min_length=1, max_length=1)

    # Verifica la operación que se va a ejecutar.
    resultado = None
    # Caso de que quieras sumar.
    if operacion == '+':
        resultado = num1 + num2
    # Caso de que quieras restar.
    elif operacion == '-':
        resultado = num1 - num2
    # Caso de que quieras multiplicar.
    elif operacion == '*':
        resultado = num1 * num2
    # Caso de que quieras dividir.
    elif operacion == '/':
        # Evitar que muera la aplicación si se divide entre cero.
        try:
            resultado = num1 / num2
        except ZeroDivisionError:
            print("Error: División por cero no es permitida.")
            return
    # Caso de que la operación no sea valida
    else:
        print("Operación no válida.")
        return
    # Imprime el resultado
    print(f"Resultado: {resultado}")

""" Ejecuta el programa """
if __name__ == "__main__":
    main()
