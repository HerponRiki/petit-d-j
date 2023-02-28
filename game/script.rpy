# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("June")
define m = Character("Mark")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bathroom
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show june downmad tiredopen sad

    j "Ugh...I should really stop staying up so late..."

    "*She begins to brush her teeth while scrolling through emails on her phone."

    show june downmad squintforward tiredsquint sad

    j "Nope...Denied...That one still hasn't gotten back to me..."

    show june downmad forward tiredopen yell

    j "UGH. I'll never find another job at this rate."

    show june downmad tiredopen sad

    j "*spits*"

    j "Whatever."


    scene closet
    with fade

    show june downsad tiredopen sad at right 

    j "*Sigh* I still have yet to fold those clothes..."

    j "And Mark left his fucking documents all over the dresser."

    j "Oh well."

    ## She is supposed to have a sprite where she is only in a bra, but thats not done yet.
    "*She grabs whatever shirt is at the top of the clean pile and heads to the kitchen.*"  

    scene kitchen
    with fade

    show june downsad sad at left

    j "I'm gonna Umma the gumma outta you."

    show mark at right
    with dissolve

    m "hello everybody my name is markipler."

    # This ends the game.

    return
