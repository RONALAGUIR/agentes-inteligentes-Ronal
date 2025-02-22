import random

def recomendar_pelicula():
    peliculas = {
        "acción": ["Mad Max: Fury Road", "John Wick", "Gladiador", "Die Hard", "The Dark Knight"],
        "comedia": ["Superbad", "The Hangover", "Step Brothers", "Anchorman", "Deadpool"],
        "drama": ["Forrest Gump", "The Shawshank Redemption", "La La Land", "The Godfather", "Fight Club"],
        "ciencia ficción": ["Interstellar", "Inception", "Blade Runner 2049", "The Matrix", "Arrival"],
        "terror": ["A Quiet Place", "The Conjuring", "It", "Hereditary", "Get Out"],
        "aventura": ["Pirates of the Caribbean", "Jumanji", "The Revenant", "Jurassic Park", "Indiana Jones"],
    }

    print("Bienvenido al Agente de Recomendación de Películas")
    print("Géneros disponibles: ", ', '.join(peliculas.keys()))
    genero = input("¿Cuál es tu género favorito? (escribe en minúsculas): ").strip().lower()

    if genero in peliculas:
        pelicula_recomendada = random.choice(peliculas[genero])
        print(f"\nTe recomiendo ver: '{pelicula_recomendada}' ({genero.capitalize()})")
    else:
        print("Lo siento, ese género no está disponible. Por favor, intenta con otro género.")

# Ejecutar el agente
if __name__ == "__main__":
    recomendar_pelicula()
