"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 3.5.1 - The song "Puff the Magic Dragon":
 In the attached file, there is a program that prints the words of the song
 Puff the Magic Dragon. The program code contains unnecessary repetitions,
 however. Patch the code by implementing the function print_chorus,
 which prints a the chorus of the song. The program's print out does not
 change in any way, only its implementation is divided to two functions (
 main and print_chorus)

Learning Goals:
 Learning to implement a repeating structure where the user does not know
 the number of repetitions in advance (while).
"""

def print_chorus():
    """
    Prints the chorus of "Puff, the Magic Dragon"

    Parameters:
        None

    Returns:
        None
    """
    print("Puff, the magic dragon lived by the sea")
    print("And frolicked in the autumn mist in a land called Honah Lee,")
    print("Puff, the magic dragon lived by the sea")
    print("And frolicked in the autumn mist in a land called Honah Lee.")
    print()

def main():
    print("Puff, the magic dragon lived by the sea")
    print("And frolicked in the autumn mist in a land called Honah Lee,")
    print("Little Jackie paper loved that rascal puff, ")
    print("And brought him strings and sealing wax and other fancy stuff. oh!")
    print()

    print_chorus()

    print("Together they would travel on a boat with billowed sail")
    print("Jackie kept a lookout perched on puffs gigantic tail,")
    print("Noble kings and princes would bow whene'r they came,")
    print("Pirate ships would lower their flag when puff roared out his "
           "name. oh!")
    print()

    print_chorus()

    print("Dragons live forever but not so little boys")
    print("Painted wings and giant strings make way for other toys.")
    print("One sad night it happened, Jackie Paper came no more")
    print("And Puff that mighty dragon, he ceased his fearless roar.")
    print()

    print("His head was bent in sorrow, green scales fell like rain,")
    print("Puff no longer went to play along the cherry lane.")
    print("Without his life-long friend, puff could not be brave,")
    print("So puff that mighty dragon sadly slipped into his cave. oh!")
    print()

    print_chorus()

if __name__ == "__main__":
    main()