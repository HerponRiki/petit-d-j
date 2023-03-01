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

    play music bgm volume 0.3

    j "Ugh...{w=1}I should really stop staying up so late..."

    "You begin to brush your teeth while scrolling through emails on your phone."

    show june downmad squintforward tiredsquint sad

    j "Nope...{w=1}Denied...{w=1}That one still hasn't gotten back to me..."

    show june downmad forward tiredopen yell

    j "UGH.{w=1} I'll never find another job at this rate."

    show june downmad side tiredopen sad

    j "Why the hell did I decide to become a graphic designer..."

    show june forward

    j "*spits*"

    j "Whatever."


    scene closet
    with fade

    show june downsad tiredopen sad at right 
    with easeinright

    j "*Sigh*{w=1} I forgot to do the laundry again last night."

    j "Guess I'm not changing out of this shirt."

    show june downmad tiredopen sad side

    j "Ugh, and Mark left his fucking documents all over the dresser."

    j "I'd complain about this if I wasn't guilty of not cleaning myself."

    j "Time for breakfast I guess."


    ## She is supposed to get dressed here but I cannot for the life of me draw a fucking bra.

    scene livingroom
    with fade

    show june normal sad at left
    show mark at right
    with dissolve

    j "Mornin' Mark."

    m "Hey June."

    j "What's up?"

    m "..."

    "Mark is on the couch with a cup of coffee and his laptop."

    "He seems to be too lost in his inbox to respond."

    show june side downmad sad at left

    j "...{w=1}I'll get started on breakfast."


    scene kitchen
    with fade

    show june normal sad 
    with dissolve

    j "Nothing like a distant spouse to start the day..."

    j "Guess I'll start with a drink."

    j "What to choose..."

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

    "It's only in the fridge for Mark's sake, but you pour 2 glasses of it anyways."

    "You refuse to buy 2 seperate milks, especially with the prices of groceries nowadays."

    "Oh, what you do for love."

    # Unlocks "Do we really need to keep buying this?"
    # Mood is positive because you both happily realize that you no longer need to keep buying Lactaid,
    # after a discovery by Mark at work once.

    $ mood += 1
    $ drink = 1

    jump cont


label oj:

    "You pour orange juice into two glasses."
    
    "You then reach for the liquor cabinet, but stop yourself when you realize that he might catch you."

    "But even if he saw you, would he even care? It's not like he is any less of an alcoholic than you are."

    "You free pour Grand Marnier into your glass. God knows he'd do the same."

    "Nothing like hard liquor at 7am in the morning."

    # Unlocks "Add another bottle to the shopping list."

    $ mood += 0
    $ drink = 2

    jump cont


label water:

    "You use the water dispenser on the fridge to get two glasses of water."

    "You're quite thirsty, so you immediately take a sip."

    show june oneup sad

    "...what the fuck?{w=1} Its...sour?"

    show june downmad

    "We need to buy new filters..."

    # Unlocks "We need new filters"

    $ mood -= 1
    $ drink = 3

    jump cont


label cof:

    "The fuel of productivity worldwide. That's probably why you haven't had any in months."

    "Mark already has a cup, but perhaps he needs another judging by the way he greeted you this morning."

    "You pour two cups of straight black coffee."

    # Unlocks "Another cup?"

    $ mood += 1
    $ drink = 4

    jump cont

########################################################################################################
# all choices converge back here to make the choice for food.
########################################################################################################

label cont:

    show june forward normal sad

    j "Next up is the food."

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

    "Can't go wrong with just bacon and eggs."

    $ mood += 1
    $ food = 1

    jump cont2


label oml:

    "The omlette,{w=0.5} a classic but slightly higher effort breakfast food."

    j "Alright,{w=1} just gotta chop these fillings,{w=0.5} cook the eggs,{w=0.5} throw them in,{w=0.5} and we're good."

    "You get the all the ingredients ready and get to work."

    play audio cut volume 1.5

    $ renpy.pause(3.5,hard = True)  # add chopping noises.

    show june downsad yell
    
    j "Ow-!"

    "Despite your caution,{w=0.5} you cut yourself while chopping cherry tomatoes."

    "It seems that somehow you've managed to cut the shirt you're wearing as well."

    show june downsad sad

    show mark at right
    with moveinright

    m "You alright over there?"

    j "Yeah,{w=0.5} I just cut my finger and your shirt. Sorry."

    m "It's fine.{w=0.5} That shirt's for posers anyways."

    hide mark
    with easeoutright

    'He walks back to his couch, grumbling about how "Ummagumma is a better album anyways..."' 

    show june oneup sad

    "You didn't understand what he meant by that, but his snarky tone was not appreciated."

    show june downmad sad

    "Regardless, you continue your cooking."

    "You finish the omlettes, now with a sliced shirt and a bandaged finger."

    # Unlocks music snob dialogue

    $ mood -= 1
    $ food = 2

    jump cont2


label parf:

    "The lowest effort option of them all, a parfait."

    "Despite parfait meaning perfect in French, you make two extremely subpar parfaits."

    "The making of the parfaits brings you back to simpler times in your relationship, the times where you two would go on cute dates without a care in the world."

    "Oh, how the time has passed."

    $ mood += 1
    $ food = 3

    jump cont2


##############################################################################
# Start of Side Choices
##############################################################################

label cont2:

    show june forward normal sad

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

    $ mood += 0
    $ sides = 2

    jump serve


label fwut:

    j "fwuit gummi"

    $ mood -= 1
    $ sides = 3

    jump serve


label nan:

    j "I think we have enough food already. No need for a side."

    # This unlocks nothing. It's just for speedrunning.

    $ mood -= 0
    $ sides = 4

    jump serve


########################################################################################################
# Here is where the petit dej is served. 
# mood will be used right at the end to change mark's reaction.
# use drink, food, and side to give the player dialogue.
# Example given below.
########################################################################################################

label serve:

    scene diningroom
    with fade

    show june sad at left
    with easeinleft

    "You place all the food and drink on the table and wait for Mark."

    show mark at right 
    with easeinright

    "He shuffles over with his laptop and almost empty coffee in hand."


    if drink == 1:
        jump keepbuying

    if drink == 2:
        jump alcoholism

    if drink == 3:
        jump sour

    if drink == 4:
        jump caffiene



label keepbuying:

    show june downmad sad at left

    j "Ugh, I still can't get over the taste of Lactaid. It's so chemical-y."

    m "We might not even have to keep buying it actually."

    show june bothup sad at left

    j "Really? But I thought you were lactose intolerant?"

    m "I thought so too until about a week ago."

    m "At a work outing, I unknowingly ate a dish with a lot of milk in it."

    m "I was so tired that I forgot to order the vegan macaroni and cheese."

    m "By the time I realized, I had already scarfed down the entire bowl."

    m "Hours passed, and somehow no symptoms came up. I think I've somehow gained a lactose tolerance."

    show june normal happy at left

    j "That's great! I can finally buy real, whole milk!"

    m "I'm excited to have normal milk for the first time in forever. I was starting to get sick of the taste of Lactaid..."

    show june normal happy blush at left

    j "I couldn't agree more."


    jump foodcont


label alcoholism:

    j "mmm i love alcohol in my oj"

    m "you put alcohol in this?"

    j "yea fuck u m9 we getting plastered."

    jump foodcont


label sour:

    j "We need new filters for the water filter."

    m "Why? Didn't we buy some recently?"

    show june downmad sad at left

    j "Yeah, if your definition of recently is 3 months ago."

    show june downmad yell at left

    j "Take a one sip of the fucking water and you tell me."

    show june downmad sad at left

    m "*Sips*"

    m "Why the fuck is it sour?"

    show june downmad yell at left

    j "Probably because someone hasn't bought new filters for it?"

    j "We've established before that {i}you're{/i} in charge of replacing the water filter.{w} You know I don't know how to replace the fridge filter."

    j "Maybe if you weren't such an alcoholic you'd drink more water then you would've noticed already."

    m "That's some big talk coming from someone who pours hard liquor into their OJ all the time."

    show june side downmad sad at left

    "*Silence*"

    j "Just put some new water filters on the shopping list please."

    j "At least I'm trying to get better by not choosing OJ today."

    jump foodcont


label caffiene:

    j "Another cup of coffee?"

    m "Oh, thanks."

    show june oneup sad

    j "What's on your mind? You seemed distracted when I greeted you this morning."

    m "I got too lazy to sort my emails, and now I'm digging through them to find evidence for a case I'm working on."

    show june normal sad

    j "Ah, I see."

    pause(1)

    show june downsad

    j "I'm sorry that I haven't been able to get a job recently."

    show june side

    j "The last two jobs I applied to rejected me, and one other hasn't even responded."

    show june forward

    j "I promise I'm trying hard to find a new one."

    m "June.{w=0.5} We've been over this, it's okay."

    m "We've managed these past few months just fine, no reason we can't hold on for another few."

    m "I know you'll find one eventually."

    m "Thanks for checking in with me by the way. It means a lot."

    show june downsad happy

    j "You're welcome.{w=0.5} Thanks for supporting me."

    jump foodcont


##############################################################################################################################################################
# Time for food conversations!!!
# same process as before lads!
##################################################################################################################################

label foodcont:

    show june none forward normal sad at left

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

    show june oneup sad 

    j "What did you mean back then?"

    m "Huh?"

    show june normal sad

    j "When I cut your shirt and you said it was for posers."

    m "Most people wear that shirt, never having listened to a single Pink Floyd song. They are fake fans."

    j "Yeah, but the design is cool. Can you really be this judgmental to a person who just likes how the shirt looks?"

    show june downmad yell

    j "Does it matter that they don't know the source material? It's not like not knowing who Pink Floyd is harmful."

    show june downmad sad

    m "..."

    m "It's not harmful to just take a listen to the band either."

    show june side downmad cheek

    j "Just reduce your snobbery alright? Your snarky remarks aren't welcomed."

    jump sidecont


label perfect:

    j "Remember when we first started dating, and you took me to that frozen yogurt place?"

    show june happy

    j "These parfaits kinda remind me of that."

    m "Oh yeah. I remember we chose eachother's toppings and mixed weird flavours together."

    m "It was so chaotic, but also so much fun."

    m "My favourite topping was the popping boba, I loved the texture and mouth-feel it created."

    show june happy normal

    j "My favourite topping was the crushed oreos."

    j "A simple but versatile topping, it worked with almost every flavour I tried."

    m "We should go back there sometime, relive some old memories."

    show june blush

    j "I would love that."

    jump sidecont





##############################################################################################################################################################
# Time for side conversations!!!
# same process as before lads!
##################################################################################################################################

label sidecont:
    
    show june none forward normal sad at left

    if sides == 1:
        jump toasty

    if sides == 2:
        jump omeal

    if sides == 3:
        jump foot

    if sides == 4:
        jump ending

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
    
    j "fresh fruit."

    m "yease"
    # insert dialogue and expressions here

    jump ending


label nothin:

    # placeholder

    jump ending


##############################################################################################################################################################
# OH BOY, its the ending! aren't you glad you made it all this way? 
# The process is quite simple here too, im sure you can figure it out by now.
# If you can't, here is what you must do.
# change the mood variables to your liking,
# add dialogue and expressions.
########################################################################################################################################################

label ending:

    show june none forward normal sad at left

    if mood <= -1:
        jump silent

    if mood == 0:
        jump eh

    if mood >= 1:
        jump yay


label silent:

    m "..."

    hide mark
    with easeoutright

    "Mark leaves the table in silence."

    "Somehow the room feels even colder than before."

    "This relationship can't possibly last."

    j "{i}*Sigh*{/i}"

    stop music fadeout 1.0
    scene black
    with fade

    return


label eh:

    m "Thanks for breakfast."

    hide mark
    with easeoutright

    "His tone is as cold and distant as ever."

    "He leaves without another word."

    "Seems as though nothing has changed."

    j "You're welcome."

    stop music fadeout 1.0
    scene black
    with fade

    return
    
label yay:

    m "Thanks for breakfast June. We should do this again tomorrow."

    show june bothup blush sad

    "His warm and genuine tone takes you aback. It's unusual for him to be this nice."

    "He stays at the table and continues his work."

    "Perhaps this breakfast has pulled both you and Mark closer together."

    show june normal blush happy

    j "You're welcome, Mark."

    stop music fadeout 1.0
    scene black
    with fade

    return


##############################################################################################################################################################
# YOU MADE IT TO THE END, HOORAY!!!!!
# Calvin is proud of you!
########################################################################################################################################################

    
