from Slots import slots
from RotorSet import Rotors
from RotorSet import Reflectors


def select_reflector():
    available_reflectors = ""
    for key in Reflectors.keys():
        available_reflectors += (key + ", ")
    available_reflectors = available_reflectors.removesuffix(", ")
    msg = f"\nPlease select a reflector ({available_reflectors}): "
    test_val = True
    reflector = input(msg)
    while test_val:
        for character in reflector:
            if character == " " or character.isalpha():
                reflector = reflector.upper()
                if reflector in Reflectors.keys():
                    test_val = False
                else:
                    print("That is an invalid Reflector.")
                    reflector = input(msg)
            else:
                print("That is an invalid Reflector.")
                reflector = input(msg)
    slots[0].insert(reflector)


def select_slot(num):
    available_rotors = ""
    for key in Rotors.keys():
        available_rotors += (key + ", ")
    available_rotors = available_rotors.removesuffix(", ")
    msg = f"\nPlease select a rotor ({available_rotors}) for Slot {num}: "
    test_val = True
    rotor = input(msg)
    while test_val:
        for character in rotor:
            if character == " " or character.isalpha():
                rotor = rotor.upper()
                if rotor in Rotors.keys():
                    test_val = False
                else:
                    print("That is an invalid Rotor.")
                    rotor = input(msg)
            else:
                print("That is an invalid Rotor.")
                rotor = input(msg)
    msg = f"Please select a ring setting as a single letter for Rotor {rotor}: "
    test_val = True
    ring = input(msg)
    while test_val:
        if len(ring) == 1 and ring.isalpha():
            test_val = False
            ring = ring.upper()
        else:
            print("That is an invalid ring setting.")
            ring = input(msg)
    slots[num].insert(rotor, ring)


def select_steckerboard():
    msg = f"Please enter up to 10 steckerboard connections (e.g.: AB CD EF GH IJ KL MN OP QR ST): "
    test_val = True
    pairs = input(msg)
    while test_val:
        pairs = pairs.replace(" ", "")
        if pairs != "" and not pairs.isalpha():
            print("The Steckerboard can only accept letters.")
            pairs = input(msg)
        elif len(pairs) >= 20:
            print("The steckerboard can on accept 10 pairs of letters.")
            pairs = input(msg)
        elif len(pairs) % 2 == 1:
            print("The steckerboard needs an even amount of letter to make pairs.")
        else:
            pairs = pairs.upper()
            test_val = False
            for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if pairs.count(letter) >= 2:
                    test_val = True
                    print("No letter may appear in the steckerboard connections list more than once. ")
                    pairs = input(msg)
    slots[4].set(pairs)


def select_message_key():
    msg = f"Please select a message key as a group of 3 letters (e.g.: ABA): "
    test_val = True
    settings = input(msg)
    settings = settings.replace(" ", "")
    while test_val:
        if len(settings) == 3 and settings.isalpha():
            settings = settings.upper()
            test_val = False
        else:
            print("That is an invalid message key setting. ")
    for i in range(3):
        slots[i + 1].set_num(settings[i])
