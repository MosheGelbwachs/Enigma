# ord(letter) - 65 returns 0 for letter="A", 1 for letter="B" ...


class Rotor:
    def __init__(self, cipher: list, notch: list[str], name: str, ring=1):
        self.notch = [ord(letter) - 65 for letter in notch]
        self.name = name
        self.ring = ring - 1  # The settings list the ring setting from 1 to 26, but our code calculates uses 0 to 25.
        self.interface = []
        self.outerface = []
        for _ in range(26):
            self.outerface.append([None])
            # By making each element a list which is mutable, I can change the contents of the list to change any
            # variable which references it.
        for i in range(26):
            self.interface.append([self.outerface[cipher[i]]])
            # Uppon review I realize that it is unnecessary to make the interface a list of lists containing elements of
            # the outerface, since for any given rotor the cipher never changes. However, it's not worth fixing.

    def set_ring(self, ring: int):
        self.ring = ring - 1  # The settings list the ring setting from 1 to 26, but our code calculates uses 0 to 25.


class Reflector:
    def __init__(self, cipher: list, name: str):
        self.name = name
        self.interface = []
        self.pairs = []
        # While rotor interface mapped to 26 outerface, a reflector only has 13 wires, each linking 2 interfaces.
        for _ in range(13):
            self.pairs.append([False])
            # False is the default, which means there is no current in the wire.
            # Since the True False value is contained in a mutable list, I can change the contents of the list which
            # will immediately update the value of both interfaces simultaneously.
        for _ in range(26):
            self.interface.append([None])
        for i in range(13):
            self.interface[cipher[2 * i]][0] = self.pairs[i]
            self.interface[cipher[(2 * i) + 1]][0] = self.pairs[i]
