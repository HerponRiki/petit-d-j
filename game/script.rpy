# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("June")
define m = Character("Mark")


# The game starts here.

label start:
    
    # variable used to track which ending you get.
    $ mood = 0

    # variables to track which drink and food you chose
    $ drink = 0
    $ food = 0
    $ sides = 0





    scene bathroom
    with fade

    show june downmad tiredopen sad
    with dissolve # with rizz lol


    j "Ugh...I should really stop staying up so late..."

    "*You begin to brush your teeth while scrolling through emails on your phone."

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
    with dissolve

    j "*Sigh* I still have yet to fold those clothes..."

    show june downmad tiredopen sad side at right 

    j "And Mark left his fucking documents all over the dresser."

    j "Oh well."

    ## She is supposed to get dressed here but I cannot for the life of me draw a fucking bra.

    scene livingroom
    with fade

    show june normal sad at left

    j "Unexpected item in bagging area?"

    show mark at right
    with dissolve

    m "Unexpected item in bagging area."


    scene kitchen
    with fade

    show june normal sad 

    j "I'm fucking starving mate, lets make some breakfast eh?"

    j "What to drink..."


menu:

    "Lactaid":
        jump aids

    "Orange Juice":
        jump oj

    "Water":
        jump water

    "Coffee":
        jump cof


label aids:

    "Something always tastes off about it. You can never seem to get used to it."

    "You pour two glasses of it anyways, since you refuse to buy 2 seperate milks."

    "Oh, what you do for love."

    # Unlocks "Do we really need to keep buying this?"

    $ mood += 1
    $ drink = 1

    jump cont


label oj:

    "You pour orange juice into two glasses."
    
    "You then reach for the liquor cabinet, but stop yourself when you realize that he might catch you."

    "But even if he saw you, would he even care?"

    "You free pour Grand Marnier into your glass. God knows he'd do the same."

    # Unlocks "Add another bottle to the shopping list."

    $ mood += 0
    $ drink = 2

    jump cont


label water:

    "You pour water into two glasses."

    "You're quite thirsty, so you immediately take a sip."

    "...what the fuck? Its...sour?"

    # Unlocks "We need new filters"

    $ mood -= 1
    $ drink = 3

    jump cont


label coff:

    "The fuel of productivity worldwide. That's probably why you haven't had any in months."

    "You pour two cups of straight black coffee."

    # Unlocks "Another cup?"

    $ mood += 0
    $ drink = 4

    jump cont


# all choices converge back here to make the choice for food.

label cont:

    j "Alright, now its time to COOK, Jesse."

    j "First off, I need to pick a protein."


menu:

    "Bacon & Eggs":
        jump bne

    "Omlette":
        jump oml

    "Parfait":
        jump parf

# remember to change the mood numbers for this part! Idk which choice is good or bad!

label bne:

    j "Eggs and bacon, oh yeah!"

    j "fun fact: that is the lyrics to the shortest Phineas and Ferb song, sung by Candace."

    $ mood += 1
    $ food = 1

    jump cont2


label oml:

    j "this is where we make alex mald using cherry tomatoes and a pink floyd shirt."

    $ mood += 1
    $ food = 2

    jump cont2


label parf:

    j "parfait is french for perfect. Parfaits suck though."

    $ mood += 1
    $ food = 3

    jump cont2


# End of Protein Choices.

label cont2:

    j "Last but not least, a side."

    j "Can't have just protein right? We're not body builders."


menu:

    "Toast":
        jump toes

    "Oatmeal":
        jump oat

    "Fruits":
        jump fwut

    "Nothing":
        jump nan


# remember to change the mood numbers for this part! Idk which choice is good or bad!

label toes:

    j "lick my toes you bum."

    $ mood += 1
    $ sides = 1

    jump serve


label oat:

    j "Can't go wrong with a classic I guess."

    $ mood += 1
    $ sides = 2

    jump serve


label fwut:

    j "fwuit gummi"

    $ mood += 1
    $ sides = 3

    jump serve


label nan:

    j "wow really? nothing? I JUST TOLD YOU WE CAN'T HAVE JUST PROTEIN DUMBASS."

    $ mood += 1
    $ sides = 4

    jump serve


# Here is where the petit dej is served. 
# mood will be used right at the end to change mark's reaction.
# use drink, food, and side to give the player dialogue.
# Example given below.


label serve:

    if drink == 1:
        jump keepbuying

    if drink == 2:
        jump alcoholism



label keepbuying:

    j "bro are we even lactose intolerant"

    m "prolly not lmao"

    j "aw fuck yea, no more of this liquid shit anymore."

    jump foodcont


label alcoholism:

    j "mmm i love alcohol in my oj"

    m "you put alcohol in this?"

    j "yea fuck u m9 we getting plastered."

    jump foodcont












    return
