class Planet:
    def __init__(self, name, mass, distance, moons, summary):
        self.name = name
        self.mass = mass
        self.distance = distance
        self.moons = moons
        self.summary = summary

    def get_name(self):
        return self.name

    def get_mass(self):
        return self.mass

    def get_distance_from_sun(self):
        return self.distance

    def number_of_moons(self):
        return self.moons

    def get_description(self):
        return self.summary

    def get_info(self):
        return (
            f"Planet {self.name}\n"
            f"Mass: {self.mass}\n Earths"
            f"Distance From the sun: {self.distance}\n"
            f"Moons: {self.moons}\n"
            f"Summary: {self.summary}\n"
        )


# DATA from WIKIPEDIA


mercury = Planet(
    "Mercury",
    0.055,
    57.9,
    0,
    "Mercury is the closest planet to the Sun and the smallest in the solar system. It has a very thin atmosphere, leading to extreme temperature fluctuations between day and night.",
)

venus = Planet(
    "Venus",
    0.815,
    108.2,
    0,
    "Venus is similar in size to Earth but has a thick, toxic atmosphere composed mainly of carbon dioxide, with clouds of sulfuric acid. It experiences a runaway greenhouse effect, making its surface extremely hot.",
)

earth = Planet(
    "Earth",
    1.0,
    149.6,
    1,
    "Earth is the only planet known to support life, thanks to its liquid water, protective atmosphere, and moderate temperatures. The Moon is Earth's only natural satellite.",
)

mars = Planet(
    "Mars",
    0.107,
    227.9,
    2,
    "Mars is known as the Red Planet and has a thin atmosphere composed mostly of carbon dioxide. Phobos and Deimos are its two small, irregular moons.",
)

jupiter = Planet(
    "Jupiter",
    317.8,
    778.5,
    79,
    "Jupiter is the largest planet in the solar system. It has a thick atmosphere and is known for its Great Red Spot, a giant storm. It has dozens of moons, including Io, Europa, Ganymede, and Callisto.",
)

saturn = Planet(
    "Saturn",
    95.2,
    1_429.0,
    83,
    "Saturn is known for its stunning ring system, composed of ice and rock. Its largest moon, Titan, has a thick atmosphere, and Enceladus has icy geysers suggesting a subsurface ocean.",
)

uranus = Planet(
    "Uranus",
    14.5,
    2_870.0,
    27,
    "Uranus is an ice giant with a unique sideways rotation. Its atmosphere contains water, ammonia, and methane ice crystals, giving it a blue-green color. Its moons include Titania, Oberon, and Miranda.",
)

neptune = Planet(
    "Neptune",
    17.1,
    4_498.0,
    14,
    "Neptune is the farthest known planet from the Sun and is known for its deep blue color caused by methane in its atmosphere. It has the strongest winds in the solar system. Triton is its largest moon.",
)

# Store planets in a list for easy access

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
