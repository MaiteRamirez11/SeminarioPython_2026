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


# Mostrar categorías
print("Categorías:")
for category in categories.keys():
    print(f"{category}", end=" | ")


# Elegir categoría
while True:
    choice = input("Elegí una categoría: ").lower()
    if choice in categories:
        break
    else:
        print("Categoría inválida. Intentá de nuevo.")


# Se guarda la lista de palabras que corresponde a la categoría elegida
words = categories[choice]

# Se elige una palabra al azar de la lista
word = random.choice(words)

guessed = [] 
attempts = 6 
score = 0

print(f"Categoría elegida: {choice}")
print("*" * 40)

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

print(f"Tu puntaje final es: {score}")