import random

# Diccionario de categorías
categories = {
    "programacion":[ "python", "programa", "variable", "funcion", "bucle", "cadena", "entero", "lista"],
    "bandas": ["beatles", "oasis", "queen", "sumo", "babasonicos", "virus"],
    "animales": ["perro", "gato", "tigre", "elefante", "leon"],
    "colores": ["rojo", "azul", "amarillo", "violeta", "rosa", "verde"]
}


print("¡Bienvenido al Ahorcado!")
print()

# Bucle principal para jugar varias rondas
while True:
    
    # Mostrar categorías
    print("Categorías:")
    for category in categories.keys():
        print(f"{category}", end=" | ")

    print()

    # Elegir categoría
    while True:
        choice = input("Elegí una categoría: ").lower()
        if choice in categories:
            break
        else:
            print("Categoría inválida. Intentá de nuevo.")

    # Usamos random.sample para obtener una lista de palabras desordenadas aleatoriamente
    words_to_play = random.sample(categories[choice], len(categories[choice]))

    #Recorrer la lista palabra por palabra garantizando que no se repitan en las siguientes rondas
    for word in words_to_play:
       
        guessed = [] 
        attempts = 6 
        score = 0
         
        print()
        print("-" * 40)
        print(f"Categoría elegida: {choice}")
        print("-" * 40)

        while attempts > 0: 
            
            # Mostrar progreso: letras adivinadas y guiones para las que faltan
            progress = ""
            for letter in word:
                if letter in guessed:
                    progress += letter + " "
                else:
                    progress += "_ "
            print(progress)
            
            # Verificar si el jugador ya adivinó la palabra completa
            if "_" not in progress:
                score += 6
                print("¡Ganaste!")
                break
        
            print(f"Intentos restantes: {attempts}")
            print(f"Letras usadas: {', '.join(guessed)}")
            
            letter = input("Ingresá una letra: ")
        
            # Si no es de longitud 1 o no es letra, continuar el juego en la siguiente iteración
            if len(letter) != 1 or not letter.isalpha():
                print("Entrada no válida")
                continue

            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                score -= 1
                print("Esa letra no está en la palabra.")
            
            print()
        
        else:
            score = 0
            print(f"¡Perdiste! La palabra era: {word}")

        print("FIN DE LA RONDA".center(30,"*"))
        print(f"Tu puntaje final en esta ronda es: {score}")

        #Cuando finaliza la ronda preguntamos si se quiere seguir jugando
        play_again = input("¿Querés seguir jugando?(si/no): ").lower()
        
        #Salir del for para dejar de sacar palabras de la categoria actual
        if play_again != "si":
            break
    
    else:
        print("Se terminaron las palabras de esta categoría...")
        play_again = input("Queres elegir otra categoria y seguir jugando?(si/no): ").lower()
    
    #Si el usuario no quiere jugar más, finaliza el juego
    if play_again != "si":
        print("FIN DEL JUEGO".center(30, "-"))
        break

    

    