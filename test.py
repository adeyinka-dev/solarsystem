import unittest
from planet import Planet


class TestPlanet(unittest.TestCase):
    def setUp(self):
        """
        This method runs before each test and creates the planet objects for testing.
        """
        self.mercury = Planet(
            "Mercury",
            0.055,
            57.9,
            0,
            "Mercury is the closest planet to the Sun and the smallest in the solar system.",
        )

    def test_get_mass(self):
        """
        Test if the get_mass method returns the correct mass of the planet.
        """
        self.assertEqual(self.mercury.get_mass(), 0.055)

    def test_get_distance(self):
        """
        Test if the get_distance_from_sun method returns the correct distance from the Sun.
        """
        self.assertEqual(
            self.mercury.get_distance_from_sun(),
            57.9,
        )

    def test_number_of_moons(self):
        """
        Test if the number_of_moons method returns the correct number of moons.
        """
        self.assertEqual(self.mercury.number_of_moons(), 0)


if __name__ == "__main__":
    unittest.main()
