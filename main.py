# For information on the Enigma Machine see the accompanying text file.
# Note: This code was not designed to be written in the most efficient way.
#       Rather, it was designed to mimic the way the Enigma Machine actually works.
import MachineSetup
from Slots import slots
from RotorSet import Rotors


def machine_setup():
    MachineSetup.select_slot(1)
    MachineSetup.select_slot(2)
    MachineSetup.select_slot(3)
    MachineSetup.select_steckerboard()


def show_settings():
    rotor_selection = f"{slots[1].rotor.name}{slots[2].rotor.name}{slots[3].rotor.name}"
    rings = []
    for i in range(1, 4):
        ring = slots[i].rotor.ring
        if ring < 9:
            rings.append(" 0" + str(ring + 1) + " ")
        else:
            rings.append(" " + str(ring + 1) + " ")
    ring_selection = rings[0] + rings[1] + rings[2]
    steckerboard_selection = " "
    for letter in slots[4].pairs:
        steckerboard_selection += letter
        if slots[4].pairs.index(letter) % 2 != 0:
            steckerboard_selection += " "
    print(f"""
    Your selected settings are:
    
    |  Walzenlage  | Ringstellung |      Steckerverbindungen      |
    |              |              |                               |
    |{rotor_selection}| {ring_selection} |{steckerboard_selection}|
    """)


# Since the message key is changed for each message, it is not included in the general show_settings function.
def show_message_key():
    print(f"""Your selected rotor positions are:
                        |{slots[1].letter}|    |{slots[2].letter}|    |{slots[3].letter}|
    """)


def operate_enigma():
    keyboard = {}
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        keyboard[letter] = [slots[4].interface[ord(letter) - 65]]
    test_val = True
    text_in = input("Enter the text you wish to encipher/decipher: ")
    while test_val:
        text_in = text_in.replace(" ", "")  # Spaces are never included in the enciphering/deciphering system.
        if not text_in.isalpha():
            print("The enigma machine only encipher/decipher alphabet characters. ")
            text_in = input("Enter the text you wish to encipher/decipher: ")
        else:
            test_val = False
    text_in = text_in.upper()
    text_out = ""
    i = 1
    for letter in text_in:
        slots[3].advance()  # The rotors are advanced BEFORE the letter goes through the cipher.
        keyboard[letter][0][0][0][0][0][0][0][0][0][0][0][0][0][0] = True
        keyboard[letter] = [[[[[[[[[[[[[[False]]]]]]]]]]]]]]
        # I chose to replace the keyboard[letter] value instead of skipping the letter in the loop,because this mimics
        # the actual workings of the machine (i.e. it shorts the circuit between the bulb and the rotor).
        for key, val in keyboard.items():
            # Each iteration of [0] brings us one step closer to the reflector. The first references the steckerboard
            # interface. The second, references slot1 interface. Then rotor1 interface, rotor1 outerface, slot 2
            # interface. The same is repeated for slots 2 and 3. Then reflector slot interface, reflector interface, and
            # finally the reflector pairs, which contain the True/False values.
            if val[0][0][0][0][0][0][0][0][0][0][0][0][0][0]:
                text_out += key
                # The following 2 ifs are to make the output into telegram format to make them easier to read.
                if i % 5 == 0:
                    text_out += " "
                if i % 100 == 0:
                    text_out += "\n"
        keyboard[letter] = [slots[4].interface[ord(letter) - 65]]
        keyboard[letter][0][0][0][0][0][0][0][0][0][0][0][0][0][0] = False
        i += 1
    print()
    print(text_out)
    print()
    ans = input("Would you like to continue to use the Enigma (Y/N)? ")
    if ans != "" and ans[0] in ["y", "Y"]:
        show_settings()
        ans = input("Would like to keep the existing settings (Y/N)? ")
        if ans != "" and ans[0] in ["y", "Y"]:
            show_message_key()
            ans = input("Would you like to keep the existing Message Key (Y/N)? ")
            if ans != "" and ans[0] in ["y", "Y"]:
                operate_enigma()
            else:
                MachineSetup.select_message_key()
                show_message_key()
                operate_enigma()
        else:
            # I don't give the option to change reflector, because that is specific to each machine and isn't changed.
            machine_setup()
            show_settings()
            MachineSetup.select_message_key()
            show_message_key()
            operate_enigma()
    else:
        pass


def reset_slots():
    slots[1].remove()
    slots[2].remove()
    slots[3].remove()
    slots[4].reset()


def reset_rotors(rotors):
    for rotor in rotors:
        rotor.ring = "A"


print(
    """
    Welcome to the Enigma Machine Simulator.
    
    To begin, select your desired settings.
    """
)
# Since the reflector is set for the machine and never changed, the select_reflector is only run once.
MachineSetup.select_reflector()
machine_setup()
show_settings()
# Since the message key is changed for each message, it is not included in the general machine_setup function.
MachineSetup.select_message_key()
show_message_key()
operate_enigma()
reset_slots()
reset_rotors(Rotors.values())
print("""
    Good bye!
    """)
