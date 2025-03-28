# Tabla_de_Multiplicar.py

from Teclado import Teclado

def tabla_unica():
    # Solicita al usuario un número entero y muestra su tabla de multiplicar del 1 al 10.
    num = Teclado.read_integer("Ingrese un número entero para ver su tabla de multiplicar:")
    print(f"\nTabla de multiplicar del {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

def tablas_todas():
    # Muestra las tablas de multiplicar del 1 al 10.
    print("Tablas de multiplicar del 1 al 10:")
    for n in range(1, 11):
        print(f"\nTabla del {n}:")
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")

def main():
    # Se le pregunta al usuario si desea ver la tabla de un número específico o todas.
    opcion = Teclado.read_text("¿Deseas ver la tabla de un número específico o todas las tablas del 1 al 10? (Escribe '1' para una tabla o '2' para todas):", min_length=1, max_length=1)
    if opcion == '1':
        tabla_unica()
    elif opcion == '2':
        tablas_todas()
    else:
        print("Opción no válida. Saliendo del programa.")

if __name__ == "__main__":
    main()
