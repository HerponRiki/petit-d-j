# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("June")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bathroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show june

    # These display lines of dialogue.

    j "Heyo!"

    show june downmad sad

    j "This game is literally cock and balls."

    show june downmad yell

    j "I'm gonna Umma the gumma outta you."

    # This ends the game.

    return
