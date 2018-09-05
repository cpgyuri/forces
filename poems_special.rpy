#This is a copy of poem_special.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#This script defines the special poems that might be shown to the player
#Only three of these are ever shown to the player, selected at random
#image poem_special1 = "poem_special/poem_special1.png" #Happy Thoughts
#image poem_special2 = "poem_special/poem_special2.png" #Can you hear me?
#image poem_special3 = "poem_special/poem_special3.png" #Nothing is real
#image poem_special4 = "poem_special/poem_special4.png" #Cutting memento
#Stare at the dot, after 10 seconds show "I love you"
#image poem_special5:
    #"poem_special/poem_special5a.png"
    #10.0
    #"poem_special/poem_special5b.png"
#image poem_special6 = "poem_special/poem_special6.png" #A Joke
#Glitchy monika
#image poem_special7a = "poem_special/poem_special7a.png"
#image poem_special7b = "poem_special/poem_special7b.png"
#image poem_special8 = "poem_special/poem_special8.png" #A Dream
#image poem_special9 = "poem_special/poem_special9.png" #Things I like about Papa
#image poem_special10 = "poem_special/poem_special10.png" #Go to therapy
#image poem_special11 = "poem_special/poem_special11.png" #A Dream

image poem_special1 = "mod_assets/poem_special1.png" #JUST YURI drawing
image poem_special2 = "mod_assets/poem_special2.png" #Sonic's Poem
image poem_special3 = "mod_assets/poem_special3.png" #Tails explain Backstory
#YouCantSeeMii's Doki Doki Matches!
image poem_special4a = "mod_assets/poem_special4.png"
image poem_special4b = "mod_assets/poem_special4b.png"
image poem_special5 = "mod_assets/poem_special5.png" #Natsuki's Poem to Sonic
image poem_special6 = "mod_assets/poem_special6.png" #Metallic Madness 1 and 2 raps
image poem_special7 = "mod_assets/poem_special7.png" #Intrusive Yuris
image poem_specialS = "mod_assets/poem_specialS.png" #Cool as heck Metal Sayori lineart
image poem_specialT = "mod_assets/poem_specialT.png" #Cool as heck Metal Trashy lineart


#This is the ending poem, either Monika's goodbye or Dan's thank you
image poem_end = ConditionSwitch(
    "persistent.clearall == True", "poem_special/poem_end_clearall.png",
    "True", "poem_special/poem_end.png")

#Each of these define a label for showing a poem
label poem_special_1:
    $ quick_menu = False
    play sound page_turn
    scene bg angelIsland_jungle
    show portal genesisportal at t22
    show ghostnatsuki gNatsu5 at t21
    with dissolve
    if persistent.packagedMusic == True:
        play music aizPCKG
    else:
        play music aiz
    g "Okay! Here we are!"
    g gNatsu10 "Next time I will refuse to do these transdimensional travels!"
    g "I almost vomited all the way in..."
    g gNatsu5 "Yes! I have an stomach too! And I CAN see, despite the opposite!"
    g gNatsu12 "All those stupid robots that were attacking MY world arrived from these stupid pink portals!"
    g "I will go to the bottom of this and stop this bullshit invasion."
    scene bg angelIsland_beach
    show ghostnatsuki gNatsu1 at t11
    with dissolve
    g "Here we are! A beach!"
    g "Nothing of my interest here, no robots in sight, or something out of the ordinary..."
    g "The breeze is nice, in any case."
    g gNatsu4 "But I think I should have go to the right side, the left side has nothing of my concern."
    stop music fadeout 2.0
    "{i}The same digging noises as the prologue...{/i}"
    g gNatsu14 "Uh??? The music stopped!"
    g "Normally that's a very bad stuff. Maybe this beach has something hidden, after all..."
    g "The sound comes from the right side, so, to the right!"
    scene bg angelIsland_jungle
    with dissolve
    if persistent.ddlc_femc:
        show boss4 heavyMagician at t31 zorder 2
        show boss6 heavyKing at t33 zorder 3
        show femc orb at t32 zorder 4
        "The Heavy Magician and the Heavy King were talking."
        "Magician said that she found the orb in Null Space and brings it to her chief."
        "The Heavy King used the power of the Phantom Ruby to awake the orb."
        show boss4 at thide zorder 1
        hide boss4
        show emerald phantomRuby at h31 zorder 2
        play music rubyMusic
        play sound ruby
        pause 3.0
        show femc lh_1g2 at t32 zorder 4
        show emerald at thide zorder 1
        hide emerald
        show ghostnatsuki gNatsu1 at t31 zorder 2
        g "Oh boy! What was that pink diamond???"
        g "...Phantom Ruby?"
        g "SO YOU WERE THE PIECE OF SHIT THAT DESTROYED MY WORLD, ROBOT!!!"
        g "Sorry, freaky robot, but I can't let you have the MC!"
        g "[femc_name]!!! Wake up!!!"
        femc lh_1f "Eh?"
        femc lh_1z "Wha... who the heck are you???"
        show rubypink zorder 5:
            alpha 0.0
            easein 4.0 alpha 0.5
        g gNatsu7 "Wait what the fuck are you doing??? What's up with the gravity?!"
        g "THIS IS REALLY UNFAIR! I CAN'T MOVE! WHAT IN TARNATION ARE YOU, STUPID SHINY ROCK???"
        femc lh_1x "Let me go, stupid robot!!!"
        femc "Shutdown your stupid pink light and fight like a woman!!!"
        stop music
        hide rubypink
        play sound ruby
        scene bg angelIsland_beach
        show black zorder 2
        show ghostnatsuki gNatsu9 at h22 zorder 3
        show femc lh_1x at h21 zorder 3
        with dissolve
        g "What happened...?"
        g "Why is everything black and shit? I can't see anything."
        femc "Who the heck are you, weird copy of Natsuki?"
        g "I'm Ghost! But that is not important right now!"
        g gNatsu7 "AS YOU CAN SEE, WE ARE TRAPPED INSIDE SOMETHING!!!"
        femc lh_3t "Like if the day can't get more worse than this..."
        g gNatsu14 "Whats's this? Somebody abandoned a tablet of sorts her..."
        g gNatsu7 "WHAT THE FUCKING FUCK??? ANTHROPOMORPHIC SKELETONS!!!"
        femc lh_1z "OH NO THAT'S TRUE!!! IT'S A REAL SKELETON!!!"
        g "THIS DUDE WAS TRAPPED HERE FOR A LONG TIME AND THEN DIED WAITING FOR HELP!!!"
        g gNatsu11 "Oh no no no nono. I will not be left here trapped in this shitty prison. I came to help my world."
        femc lh_3x "Ok, Ghost, let's focus. We will make this shitty tablet work, and then send a distress call with it."
        femc "And then we will find that stupid robot and destroy it!!!"
        femc "They will know [femc_name]'s fury!!! Nobody messes with me!!!"
        femc "And pray that whatever deity they have here show mercy to them if they did something nasty to Sayori, because I will not have mercy!!!"
    else:
        show boss4 heavyMagician at t31 zorder 2
        show boss6 heavyKing at t33 zorder 3
        show mc2 orb at t32 zorder 4
        "The Heavy Magician and the Heavy King were talking."
        "Magician said that she found the orb in Null Space and brings it to her chief."
        "The Heavy King used the power of the Phantom Ruby to awake the orb."
        show boss4 at thide zorder 1
        hide boss4
        show emerald phantomRuby at h31 zorder 2
        play music rubyMusic
        play sound ruby
        pause 3.0
        show mc2 1error at t32 zorder 4
        show emerald at thide zorder 1
        hide emerald
        show ghostnatsuki gNatsu1 at t31 zorder 2
        g "Oh boy! What was that pink diamond???"
        g "...Phantom Ruby?"
        g "SO YOU WERE THE PIECE OF SHIT THAT DESTROYED MY WORLD, ROBOT!!!"
        g "Sorry, freaky robot, but I can't let you have the MC!"
        g "[mc2_name]!!! Wake up!!!"
        mc2 1h "Eh?"
        mc2 5shock "Wha... who the heck are you???"
        show rubypink zorder 5:
            alpha 0.0
            easein 4.0 alpha 0.5
        g gNatsu7 "Wait what the fuck are you doing??? What's up with the gravity?!"
        g "THIS IS REALLY UNFAIR! I CAN'T MOVE! WHAT IN TARNATION ARE YOU, STUPID SHINY ROCK???"
        mc2 5w "Let me go, stupid robot!!!"
        mc2 "Shutdown your stupid pink light and fight like a man!!!"
        stop music
        hide rubypink
        play sound ruby
        scene bg angelIsland_beach
        show black zorder 2
        show ghostnatsuki gNatsu9 at h22 zorder 3
        show mc2 5w at h21 zorder 3
        with dissolve
        g "What happened...?"
        g "Why is everything black and shit? I can't see anything."
        mc2 "Who the heck are you, weird copy of Natsuki?"
        g "I'm Ghost! But that is not important right now!"
        g gNatsu7 "AS YOU CAN SEE, WE ARE TRAPPED INSIDE SOMETHING!!!"
        mc2 4s "Like if the day can't get more worse than this..."
        g gNatsu14 "Whats's this? Somebody abandoned a tablet of sorts her..."
        g gNatsu7 "WHAT THE FUCKING FUCK??? ANTHROPOMORPHIC SKELETONS!!!"
        mc2 1shock "OH NO THAT'S TRUE!!! IT'S A REAL SKELETON!!!"
        g "THIS DUDE WAS TRAPPED HERE FOR A LONG TIME AND THEN DIED WAITING FOR HELP!!!"
        g gNatsu11 "Oh no no no nono. I will not be left here trapped in this shitty prison. I came to help my world."
        mc2 1w "Ok, Ghost, let's focus. We will make this tablet work, and then send a distress call with it."
        mc2 1t "I need to find Sayori, she is alone out there, in this strange world..."
        mc2 2t "I will never forgive myself if something happen to her..."
        mc2 "I promised to care about her and do what is best for her! Let's hurry, Ghost!"
    $ quick_menu = True
    return

#All the rest are the same
label poem_special_2:
    $ quick_menu = False
    play sound page_turn
    show poem_special2 with Dissolve(1.0)
    $ pause()
    #play sound "sfx/giggle.ogg"
    $ quick_menu = True
    return
label poem_special_3:
    $ quick_menu = False
    play sound page_turn
    show poem_special3 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_4:
    $ quick_menu = False
    play sound page_turn
    show poem_special4a with Dissolve(1.0)
    pause 5.0
    show poem_special4b
    $ pause()
    play sound "sfx/giggle.ogg"
    $ quick_menu = True
    return
label poem_special_5:
    $ quick_menu = False
    play sound page_turn
    show poem_special5 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_6:
    $ quick_menu = False
    play sound page_turn
    show poem_special6 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_7:
    $ quick_menu = False
    play sound page_turn
    show poem_special7a as ps with Dissolve(1.0)
    $ pause()
    show poem_special7b as ps
    pause 0.01
    $ quick_menu = True
    return
label poem_special_8:
    $ quick_menu = False
    play sound page_turn
    show poem_special8 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_9:
    $ quick_menu = False
    play sound page_turn
    show poem_special9 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_10:
    $ quick_menu = False
    play sound page_turn
    show poem_special10 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_11:
    $ quick_menu = False
    play sound page_turn
    show poem_special11 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_special:
    $ quick_menu = False
    play sound page_turn
    play music vsSayori
    show poem_specialS with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_special2:
    $ quick_menu = False
    play sound page_turn
    play music metalDokis
    show poem_specialT with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
