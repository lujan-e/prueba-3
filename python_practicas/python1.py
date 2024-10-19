def ingresar_puntuacion():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            if 1 <= point <= 5:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                print('Puntuación y comentario guardados.')
                break
            else:
                print('Indíquelo en una escala de 1 a 5')
        else:
            print('Por favor, introduzca la puntuación en números')

def comprobar_resultados():
    print('Resultados hasta la fecha:')
    try:
        with open("data.txt", "r") as read_file:
            results = read_file.read()
            if results:
                print(results)
            else:
                print("No hay resultados disponibles.")
    except FileNotFoundError:
        print("No se encontraron resultados. Asegúrese de haber ingresado puntuaciones primero.")

def mostrar_menu():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
        num = input()
        
        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion()
            elif num == 2:
                comprobar_resultados()
            elif num == 3:
                print('Finalizando')
                break
            else:
                print('Introduzca un número del 1 al 3')
        else:
            print('Introduzca un número del 1 al 3')

if __name__ == "__main__":
    mostrar_menu()
