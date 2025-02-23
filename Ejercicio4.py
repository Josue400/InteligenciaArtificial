import random

def recomendar_pelicula(genero):
    """Devuelve una recomendación de película según el género indicado."""
    peliculas = {
        "accion": ["Mad Max: Fury Road", "John Wick", "Gladiador"],
        "comedia": ["Superbad", "The Hangover", "Dumb and Dumber"],
        "drama": ["Forrest Gump", "The Shawshank Redemption", "The Godfather"],
        "ciencia ficcion": ["Inception", "Interstellar", "Blade Runner 2049"],
        "terror": ["The Conjuring", "It", "A Nightmare on Elm Street"]
    }
    
    genero = genero.lower()
    if genero in peliculas:
        return random.choice(peliculas[genero])
    else:
        return "Género no reconocido. Por favor, elija entre acción, comedia, drama, ciencia ficción o terror."

if __name__ == "__main__":
    genero_predefinido = "accion"  # Simulación de entrada en entornos sin input
    print(f"Género elegido: {genero_predefinido}")
    recomendacion = recomendar_pelicula(genero_predefinido)
    print(f"Película recomendada: {recomendacion}")
