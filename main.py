from planet import planets
from animate import animated_print


def query_planets():
    while True:
        animated_print("Welcome to the Solar System", delay=0.05)

        query = input(
            "\nAsk a question about the planets (or type 'exit' to quit): "
        ).lower()

        if query == "exit":
            print("Goodbye!")
            break

        # Check if a specific planet is in the query
        planet_name = None
        for planet in planets:
            if planet.name.lower() in query:
                planet_name = planet
                break

        # Handle the queries based on detected planet name
        if planet_name:
            if "everything" in query or "tell me" in query:
                animated_print(planet_name.get_info())
            elif "massive" in query or "mass" in query:
                animated_print(planet_name.get_mass())
            elif "moons" in query:
                animated_print(planet_name.number_of_moons())
            elif "distance" in query:
                animated_print(planet_name.get_distance_from_sun(), delay=0.01)
            # if question is not clear enough
            else:
                print("Sorry, I don't understand the question.")
        elif "pluto" in query:
            print("Pluto is not considered a planet in the current list.")
        else:
            print("Sorry, the planet is not in the list.")


if __name__ == "__main__":
    query_planets()
