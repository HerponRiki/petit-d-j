############################################################################################################################################################
# Things for you to do:
#
# Write dialogue for each choice, and the expressions that would go along with it.
# Change the mood variables for each choice to fit your needs.
##########################################################################################################################################################

# The game starts here.

define j = Character("June")
define m = Character("Mark")

label start:
    
    # variable used to track which ending you get.
    $ mood = 0

    # variables to track which drink and food you chose.
    $ drink = 0
    $ food = 0
    $ sides = 0

    ##############################################################################
    # story starts here.
    ##############################################################################

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

########################################################################################################
# The start of drink choices
########################################################################################################

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

########################################################################################################
# all choices converge back here to make the choice for food.
########################################################################################################

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

########################################################################################################
# remember to change the mood numbers for this part! Idk which choice is good or bad!
########################################################################################################

label bne:

    j "Eggs and bacon, oh yeah!"

    j "fun fact: that is the lyrics to the shortest Phineas and Ferb song, sung by Candace."

    $ mood += 1
    $ food = 1

    jump cont2


label oml:

    j "this is where we make alex mald using cherry tomatoes and a pink floyd shirt."

    $ mood -= 1
    $ food = 2

    jump cont2


label parf:

    j "parfait is french for perfect. Parfaits suck though."

    $ mood += 1
    $ food = 3

    jump cont2


##############################################################################
# Start of Side Choices
##############################################################################

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

##################################################################################################################################
# remember to change the mood numbers for this part! Idk which choice is good or bad!
##################################################################################################################################

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

    $ mood -= 1
    $ sides = 4

    jump serve


########################################################################################################
# Here is where the petit dej is served. 
# mood will be used right at the end to change mark's reaction.
# use drink, food, and side to give the player dialogue.
# Example given below.
########################################################################################################

label serve:

    if drink == 1:
        jump keepbuying

    if drink == 2:
        jump alcoholism

    if drink == 3:
        jump sour

    if drink == 4:
        jump caffiene



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


label sour:

    "test"
    # insert dialogue and expressions here

    jump foodcont


label caffiene:

    "test"
    # insert dialogue and expressions here

    jump foodcont


##############################################################################################################################################################
# Time for food conversations!!!
# same process as before lads!
##################################################################################################################################

label foodcont:

    if food == 1:
        jump baconegg

    if food == 2:
        jump poser

    if food == 3:
        jump perfect



label baconegg:

    j "barbecue bacon burger"

    m "a hot side of apple pie"

    j "2 number 45s, and a large soda"

    jump sidecont


label poser:

    j "I AM NOT A POSER JUST CUZ IM WEARIN DIS SHIRT"

    m "haha fake fan Ummagumma better album"

    j "fok u m8 im fucking minging"

    jump sidecont


label perfect:

    "test"
    # insert dialogue and expressions here

    jump sidecont





##############################################################################################################################################################
# Time for side conversations!!!
# same process as before lads!
##################################################################################################################################

label sidecont:

    if sides == 1:
        jump toasty

    if sides == 2:
        jump omeal

    if sides == 3:
        jump foot

    if sides == 4:
        jump nothin

label toasty:

    j "People underestimate the power of toast. Like, twice cooked bread with some butter? sounds boring but tis the best thing ever made."

    m "Couldn't agree more june, youre so based."

    j "thanks mark, youre also based. mwah."

    jump ending


label omeal:

    j "oatmeal is like a peasant dish."

    m "do not disrespect oatmeal in this house."

    j "disrespect these nuts fucker."

    jump ending


label foot:
    
    "test"
    # insert dialogue and expressions here

    jump ending


label nothin:

    "test"
    # insert dialogue and expressions here

    jump ending


##############################################################################################################################################################
# OH BOY, its the ending! aren't you glad you made it all this way? 
# The process is quite simple here too, im sure you can figure it out by now.
# If you can't, here is what you must do.
# change the mood variables to your liking,
# add dialogue and expressions.
########################################################################################################################################################

label ending:

    if mood <= -1:
        jump silent

    if mood == 0:
        jump eh

    if mood >= 1:
        jump yay


label silent:

    m "..."

    j "sad"

    return


label eh:

    m "ty for bfast"

    j "ok"

    return
    
label yay:

    m "Thanks for breakfast June. We should do this again tomorrow."

    j "happi"

    return


##############################################################################################################################################################
# YOU MADE IT TO THE END, HOORAY!!!!!
# Calvin is proud of you!
########################################################################################################################################################

    
