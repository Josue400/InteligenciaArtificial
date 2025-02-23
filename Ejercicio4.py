import random

def recomendar_pelicula(genero):
    """Sistema de recomendación de películas basado en el género favorito del usuario."""
    peliculas = {
        "accion": ["Mad Max: Fury Road", "John Wick", "Gladiador"],
        "comedia": ["Superbad", "The Hangover", "Step Brothers"],
        "drama": ["Forrest Gump", "The Shawshank Redemption", "The Godfather"],
        "ciencia ficcion": ["Interstellar", "Blade Runner 2049", "The Matrix"],
        "terror": ["The Conjuring", "IT", "A Nightmare on Elm Street"]
    }
    
    genero = genero.lower().strip()
    if genero in peliculas:
        return random.choice(peliculas[genero])
    else:
        return "Género no encontrado. Intente con acción, comedia, drama, ciencia ficción o terror."

if __name__ == "__main__":
    print("Bienvenido al sistema de recomendación de películas.")
    try:
        genero_favorito = input("Ingrese su género favorito: ")
        pelicula_recomendada = recomendar_pelicula(genero_favorito)
        print(f"Película recomendada: {pelicula_recomendada}")
    except Exception as e:
        print(f"Error al procesar la entrada: {e}")
