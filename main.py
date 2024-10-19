from planet import planets
from animate import animated_print


def query_planets():
    while True:
        animated_print("Welcome to the Solar System")

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
                animated_print(f"{planet_name.get_info()}\n\n")
            elif "massive" in query or "mass" in query:
                print(f"{planet_name.get_mass()} Earth masses \n\n")
            elif "moons" in query:
                print(
                    f"{planet_name.name} has {planet_name.number_of_moons()} moons\n\n"
                )
            elif "distance" in query:
                print(planet_name.get_distance_from_sun())
            # if question is not clear enough
            else:
                print("Sorry, I don't understand the question.\n\n")
        elif "pluto" in query:
            print("Pluto is not considered a planet in the current list.\n\n")
        else:
            print("Sorry, the planet is not in the list.\n\n")


if __name__ == "__main__":
    query_planets()
