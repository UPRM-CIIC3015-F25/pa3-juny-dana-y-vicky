class PlanetCard:
    def __init__(self, name, description, price=6, chips=0, mult=0, image=None, isActive=False):
        self.name = name
        self.description = description
        self.price = price
        self.chips = chips
        self.mult = mult
        self.image = image
        self.isActive = isActive

    def __str__(self):
        return f"{self.name}: {self.description}"

    def sellPrice(self):
        return int(self.price * 0.6)

# TODO (TASK 6.1): Implement the Planet Card system for Balatro.
#   Create a dictionary called PLANETS that stores all available PlanetCard objects.
#   Each entry should use the planet's name as the key and a PlanetCard instance as the value.
#   Each PlanetCard must include:
#       - name: the planet's name (e.g., "Mars")
#       - description: the hand it levels up or affects
#       - price: how much it costs to purchase
#       - chips: the chip bonus it provides
#       - mult: the multiplier it applies
#   Example structure:
#       "Gusty Garden": PlanetCard("Gusty Garden", "levels up galaxy", 6, 15, 7)
#   Include all planets up to "Sun" to complete the set.
#   These cards will be used in the shop and gameplay systems to upgrade specific poker hands.

PLANETS = {
    "Mercury": PlanetCard(
        "Mercury",
        "Levels up High Card",
        4,
        10,
        1
    ),
    "Venus": PlanetCard(
        "Venus",
        "Levels up Pair",
        4,
        12,
        1
    ),
    "Earth": PlanetCard(
        "Earth",
        "Levels up Two Pair",
        5,
        14,
        2
    ),
    "Mars": PlanetCard(
        "Mars",
        "Levels up Three of a Kind",
        5,
        15,
        2
    ),
    "Jupiter": PlanetCard(
        "Jupiter",
        "Levels up Straight",
        6,
        18,
        3
    ),
    "Saturn": PlanetCard(
        "Saturn",
        "Levels up Flush",
        6,
        18,
        3
    ),
    "Uranus": PlanetCard(
        "Uranus",
        "Levels up Full House",
        7,
        20,
        4
    ),
    "Neptune": PlanetCard(
        "Neptune",
        "Levels up Four of a Kind",
        8,
        25,
        5
    ),
    "Pluto": PlanetCard(
        "Pluto",
        "Levels up Straight Flush",
        10,
        35,
        6
    )
}
