# Importar funciones del módulo calculadora
from calculadora import suma, resta, multiplicacion, division

# Función para mostrar el menú de opciones
def menu():
    print("Calculadora Simple")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

# Función principal
def main():
    while True:
        # Mostrar el menú
        menu()

        # Solicitar al usuario que elija una opción
        opcion = input("Ingrese el número de la operación que desea realizar: ")

        # Salir del bucle si el usuario elige la opción 5
        if opcion == '5':
            print("¡Hasta luego!")
            break

        # Solicitar los números para realizar la operación
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        # Realizar la operación según la opción elegida
        if opcion == '1':
            print("El resultado de la suma es:", suma(num1, num2))
        elif opcion == '2':
            print("El resultado de la resta es:", resta(num1, num2))
        elif opcion == '3':
            print("El resultado de la multiplicación es:", multiplicacion(num1, num2))
        elif opcion == '4':
            print("El resultado de la división es:", division(num1, num2))
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

# Ejecutar la función principal si este script es el programa principal
if __name__ == "__main__":
    main()








