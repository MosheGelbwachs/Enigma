from RotorSet import Rotors
from RotorSet import Reflectors
from RotorClass import Rotor
from RotorClass import Reflector


# For all slot types, sub_slot refers to the slot which the current slot leads into.


# Steckerboard is German, which (loosely) translates to plugboard in English.
class Steckerboard:
    def __init__(self, sub_slot):
        self.sub_slot = sub_slot
        self.interface = []
        for i in range(26):
            self.interface.append([self.sub_slot.interface[i]])  # This is default setting ("A" -> "A") with no plugs.
        self.pairs = ""

    def set(self, pairs: str):
        self.reset()
        self.pairs = pairs
        for letter in self.pairs:
            if self.pairs.index(letter) % 2 == 0:
                first = letter
            else:
                second = letter
                self.interface[ord(first) - 65][0] = self.sub_slot.interface[ord(second) - 65]
                self.interface[ord(second) - 65][0] = self.sub_slot.interface[ord(first) - 65]
                # This effectively swaps each 2 letter pair (1st letter -> 2nd letter; 2nd letter -> 1st letter).

    def reset(self):
        for i in range(26):
            self.interface[i][0] = self.sub_slot.interface[i]  # This is default setting ("A" -> "A") with no plugs.
        self.pairs = ""


# Defines classic slot which accepts regular rotors.
class Slot:
    def __init__(self, name: str, sub_slot):
        self.name = name
        self.sub_slot = sub_slot
        self.rotor = None  # Stores the rotor inserted into the slot
        self.interface = []
        self.letter = None  # Stores the letter which is displayed by rotor.
        self.num = None  # Stores the number corresponding to the display letter.
        for _ in range(26):
            self.interface.append([None])

    def insert(self, rotor: Rotor, ring: str, letter: str = "A"):
        if self.rotor != None:
            self.remove()
        if rotor not in Rotors.keys():
            print(f"Rotor {rotor} is not available. Please select another rotor. ")
        else:
            self.rotor = Rotors.pop(rotor)
            self.rotor.ring = ord(ring) - 65
            self.letter = letter
            self.num = ord(self.letter) - 65
            self.set_num(self.letter)

    def set_num(self, letter):
        self.letter = letter
        self.num = ord(letter) - 65
        for i in range(26):
            # By assigning to interface[num][0], we are only altering the list elements and leaving the list itself.
            # Assign each slot interface to the new rotor interface position based on the new letter and prior ring num.
            self.interface[(i - (self.num - 1)) % 26][0] = self.rotor.interface[(i + self.rotor.ring) % 26]
            # Assign each rotor interface to the new sub_slot interface position based on the new letter and prior ring num.
            self.rotor.outerface[(i + self.rotor.ring) % 26][0] = self.sub_slot.interface[(i - (self.num - 1)) % 26]

    def remove(self):
        for i in range(26):
            # By assigning to interface[num][0], we are only altering the list elements and leaving the list itself.
            self.interface[i][0] = None
            self.rotor.outerface[i][0] = None
        Rotors[self.rotor.name.replace(" ", "")] = self.rotor
        self.rotor = None
        self.letter = None
        self.num = None

    def advance(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.letter = letters[((ord(self.letter)) - 65 + 1) % 26]
        self.num = ord(self.letter) - 65
        self.set_num(self.letter)
        if self.num in self.rotor.notch:
            self.sub_slot.advance()


class ReflectorSlot:
    def __init__(self):
        self.reflector = None
        self.interface = []
        for _ in range(26):
            self.interface.append([None])

    def insert(self, reflector: Reflector):
        if reflector not in Reflectors.keys():
            print(f"Reflector {reflector} is not available. Please select another reflector. ")
        else:
            self.reflector = Reflectors.pop(reflector)
            for i in range(26):
                # By assigning to interface[num][0], we are only altering the list elements and leaving the list itself.
                self.interface[i][0] = self.reflector.interface[i]

    def remove(self):
        for i in range(26):
            # By assigning to interface[num][0], we are only altering the list elements and leaving the list itself.
            self.interface[i][0] = None
        Reflectors[self.reflector.name.replace(" ", "")] = self.reflector
        self.reflector = None

    def advance(self):
        pass  # Reflectors never rotate


reflector_slot = ReflectorSlot()
slot1 = Slot("Slot 1", reflector_slot)
slot2 = Slot("Slot 2", slot1)
slot3 = Slot("Slot 3", slot2)
steckerboard = Steckerboard(slot3)
slots = [reflector_slot, slot1, slot2, slot3, steckerboard]
