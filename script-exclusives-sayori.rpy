image exception_bg = "#dadada"
image fake_exception = Text("MILESELECTRIC SOFTWARE: EXCEPTION CAUGHT!", size=40, style="_default")
image fake_exception2 = Text("Script \"sayori_exclusive_2.rpy\", Doki Doki Forces program, line 666\nSee traceback.txt for details on player's OS.\nReporting error to root user Tails.\n\n\n\nYou can't do anything, so don't even try.\nGet some help.\nDon't do what Sonic does.\nSONIC, DEAD OR ALIVE... IS M-M-M-MINE!", size=20, style="_default")

label sayori_exclusive_1:
    scene bg nullspace
    with wipeleft_scene
    if not renpy.music.get_playing(channel='music') == audio.mend:
        if persistent.packagedMusic == True:
            play music nullSpacePCKG
        else:
            play music mend
    if persistent.yuriKnife == True:
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
        show yuri 3y2 at t11 zorder 2
        y "NO! WHAT ARE YOU DOING???"
        y "You were supposed to choose ME!"
        y 3y7 "You were a follower of the Yurism cult... OK, that's it!!"
        y 3y3 "ENJOY YOUR PRECIOUS SAYORI WHILE YOU CAN..."
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
        show yuri at thide zorder 1
        hide yuri
    "Apparently this didn't work..."
    "It looks like I failed another mission again."
    mc "Well, it seems I will have to present my resing letter to Knuckles when I return to my world..."
    mc "Eh? My Wispon is shining again!"
    stop music fadeout 2.0
    show sayori orb at t11 zorder 2
    "A strange orb appeared. It's reacting with my Wispon..."
    "What...?"
    "The orb materialized in front of me!"
    "Is one of the girls, and she's the girl with the red ribbon! Unbelievable! I saved her!!!"
    play music tsayori 
    show sayori 1h at t11 zorder 2
    s "Ugh, my head... The last thing I remember, I was in the Literature Club room with my friends..."
    show sayori 4m at t11 zorder 2
    s "MY FRIENDS!!!! Oh no! We were ambushed by a weird creature..."
    s 1f "I can't remember, I'm hungry..."
    mc "If you want, you can eat this sandwich I have."
    "I pulled a sandwich from a secret compartment of the Wispon."
    s 1m "Who are you???? Are you friend with that weird creature called Infinite?"
    s 4s "And thanks for this sandwich! I eated a lot of Natsuki's cupcakes but I'm still hungry!"
    mc "Glad you liked this sandwich!"
    mc "And no! Infinite is our enemy! My name is [player], and I'm a member of the Resistance."
    s 4s "Yay! So you arrived here to rescue us!"
    mc "Well... about that..."
    if persistent.yuriKnife == True:
        stop music
        $ style.say_dialogue = style.edited
        s illusion2 "But before you speak..."
        s illusion4 "WHY DID YOU SAVED ME???"
        mc "Huh? I don't understand the ques..."
        s "SILENCE!!!"
        s illusion3 "I'm the most miserable human being that exists!"
        s "I don't know why people think so high about me."
        s "Rookie, I'm useless, I have depression, most of the time I don't want to get up from bed..."
        if persistent.ddlc_femc:
            s "I even doubt that [femc_name] loves me at all. In reality, I'm a burden to her."
        else:
            s "I even doubt that [mc2_name] loves me at all. In reality, I'm a burden to him."
        s "SO YOU WILL HAVE TO KILL ME!!!"
        s "I JUST WANT THESE ANNOYING RAINCLOUDS TO GET OUT OF MY HEAD!!!"
        s illusion4 "SHOOT ME WITH YOUR WISPON!!!!"
        s "SHOOT ME!!!"
        s "SHOOT ME!!!"
        mc "NO!"
        s illusion1 "SHOOT ME!!!"
        s "SHOOT ME!!!"
        s "SHOOT ME!!!"
        s "SHOOT ME!!!"
        mc "NO!!!"
        s 1u "SHOOT ME!!!"
        mc "ABSOLUTELY NO!!!"
        s "SHOOT ME!!!"
        s "SHOOT ME!!!"
        s "SHOOT ME!!"
        s "SHOOT ME!"
        s "SHOOT ME"
        s "Shoot me please."
        s "Shoot me..."
        s 1v "Rookie, why don't you shoot your weapon at me...?"
        s "These rainclouds are so strong!!! Help me! I don't want to die!"
        s 1w "GET OUT OF MY HEAD, RAINCLOUDS!!!"
        mc "Hey girl! Just listen to me ok!!!"
        $ style.say_dialogue = style.normal
        "I pulled her into a hug and let her cry for as much as she wanted."
        "After that, I started to explain..."
        $ skip_transition = True

    scene bg nullspace
    with wipeleft_scene
    stop music fadeout 2.0
    play music t9
    show sayori 1w at t11 zorder 2
    "I explained to this girl what happened when Infinite attacked her classroom."
    "She told me that her name is Sayori, and her expression changed when I mentioned she was the only one I could revive."
    s "There must be a way to save my friends! It's my duty as Vice President of the club to worry about them."
    s "The only thing I care in this world more than myself, are my friends!"
    s 1y "Monika, Yuri, Natsuki... each one has a quality that makes them special."
    s "If you meet them, you will understand what I'm saying..."
    show sayori 1w at t11 zorder 2
    mc "Please don't cry, Sayori..."
    mc "Maybe... if you write some poem about your friends, and if I load it on my Wispon..."
    mc "Then we could save them all."
    mc "That's how I saved you."
    show sayori 1i at t11 zorder 2
    "Sayori wrote a poem on my communicator. She was very determined to do this."
    call showpoem(poem_s4)
    "Her poem is kinda bittersweet, but is understandable because the situation."
    "I'm intrigued, to be honest. Who is this friend of her? It doesn't seem to be one of the other girls... Maybe is a crush?"
    "I loaded the poem on the Wispon and prepared to fire..."
    mc "Wish me good luck, Sayori!"
    s 4t "I forgot to say thanks for the sandwich."
    mc "It's ok! Now let me concentrate."
    "The Wispon fired a beam again..."
    "After I fired the Wispon, three coloured orbs appeared..."
    show monika orb at t44 zorder 5
    show sayori 1m at t43 zorder 4
    show natsuki orb at t42 zorder 3
    show yuri orb1 at t41 zorder 2
    "Then the other three girls materialized!"
    mc "Unbelievable! I need to report this to Tails when I come back to our Headquarter!"

    "You got 400 rings for saving Sayori!"
    play sound Ring
    $ persistent.ringCount += 400
    "You now have [persistent.ringCount] Rings!\n{i}Click to continue...{/i}"
    return

label sayori_exclusive_2:
    scene bg greenHill1
    with dissolve_scene_half
    if persistent.packagedMusic == True:
        play music greenHillPCKG
    else:
        play music greenHillZ1
    "So, I made another poem of sorts. At this rate I will become a poetry writer more than a soldier xD."
    show knuckles knucklesCom at t22 zorder 2
    show monika 2c at t21 zorder 3
    kte "So, did you selected the girl who will go to the mission?"
    m 2b "Oh yeah! I have the poem of Rookie here!"
    m 4b "Based on the results, the chosen one of us that will represent the Literature Club in this mission is..."
    m 1b "Sayori!"
    show knuckles knucklesCom at t33 zorder 2
    show monika 1b at t32 zorder 3
    show sayori 5a at l31 zorder 4
    "Sayori looks surprised. In fact she got so surprised that she almost dropped the onion rings sandwich..."
    stop music fadeout 2.0  
    s "EH??? But-but-but... Why me?"
    s 5b "I'm not special or anything. Monika is the President, Natsuki was eager to go and..."
    show monika 2p at h32 zorder 3
    s 1u "I will be a nuisance for this mission!"
    s "Our world was destroyed by that ugly creature!"
    s 4w "Everyone are no more! My childhood friend isn't here with me to help me!"
    s "He just confessed to me the day before!"
    s "And my stupid rainclouds are giving me problems again! Why they don't go away????"
    s "Tails will be so dissapointed in me, and Monika too! I don't deserve to be Vice President!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.3
    hide screen tear
    show sayori at thide zorder 1
    hide sayori
    s "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    "Uh-oh. Sayori reacted badly... This reminds me of my own start in the Resistance, depressed and scared about Infinite."
    mc "Wait what's happening?"
    m "Oh no, please not this..."
    menu:
        "MOD AUTHOR'S NOTICE: CONTENT WARNING!!!\nDo you really want to see this scene?"
        "I'm brave! Proceed":
            "OK then."
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.3
            hide screen tear
            show knuckles at thide zorder 1
            show sayori at thide zorder 1
            hide knuckles
            hide sayori
            scene bg tcError
            show s_kill
            pause 3.0
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.3
            hide screen tear
            hide s_kill
            show noise zorder 99:
                alpha 0.0
                linear 3.0 alpha 0.25
            show vignette zorder 99:
                alpha 0.0
                linear 3.0 alpha 0.75
            play music td
            show s_kill_bg as s_kill_bg at s_kill_bg_start
            show s_kill as s_kill at s_kill_start
            pause 3.75
            show s_kill as s_kill zorder 3:
                truecenter
                dizzy(1, 1.0)
            show white zorder 2
            show splash_glitch zorder 2
            pause 2.0
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.3
            stop sound
            hide screen tear
            pause 5.0
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.3
            stop sound
            hide screen tear
            hide splash_glitch
            show splash_glitch2 zorder 2
            show splash_glitch_m zorder 2
            show splash_glitch_n zorder 2
            show splash_glitch_y zorder 2
            pause 1.25
            hide white
            hide splash_glitch2
            hide splash_glitch_m
            hide splash_glitch_n
            hide splash_glitch_y
            show exception_bg zorder 2
            show fake_exception zorder 2:
                xpos 0.1 ypos 0.05
            show fake_exception2 zorder 2:
                xpos 0.1 ypos 0.15
            python:
                try: sys.modules['renpy.error'].report_exception("I DO NOT DESERVE TO BE LOVED! GET OUT OF MY HEAD FRICKIN HAPPY THOUGHTS! HELP ME HELP ME HELP ME HELP ME HELP ME...", False)
                except: pass
            pause 5.0
            "Surprise motherfrickin'."
            g "I'M BRAVE THEY SAID. THIS WILL BE FUN THEY SAID. NOTHING WRONG WILL HAPPEN THEY SAID. THIS MOD DOESN'T HAVE SAYO-NARA THEY SAID."
            g "Stupid piece of shi...{nw}"
            show monika 2p at t33 zorder 2:
                dizzy(1, 1.0)
            mc "WOAH!!!! NO WAY!!! SAYORI??? MONIKA???"
            mc "WHAT THE HELL IS HAPPENING AGAIN? IS THIS YURI'S FAULT?"
            m 2f "Rookie, can you help me with this?"
            mc "MONIKA, DID THIS REALLY HAPPENED IN YOUR WORLD???"
            m "Sadly, yes, [player]."
            m 2q "Sayori has depression since some years ago."
            m "I think that she is reacting just now to everything that happened..."
            m 2p "And this thing that is showing up now was my fault!"
            m "There are some things I REALLY don't want to happen again..."
            m "Like this one, for example."
            m 1q "I'm really sorry for this, Rookie. I will understand if my friends or you can't forgive me for this..."
            mc "Monika, you are showing that you are truly sorry, I believe you, and I forgive you."
            mc "And I'm sure your friends will forgive you too. In fact, I think they did it, or else neither of you would be alive."
            mc "And about this, I think there's someone who can help, I reached to him with my Wispon!"
            mc "He is teleporting there as we speak!"
            show tails tails04 at l31 zorder 2:
                dizzy(1, 1.0)
            mtp "THESE SCRIPT INTERRUPTIONS ARE NASTY AND BAD!"
            mtp "I can't believe Sayori did this in another timeline..."
            mtp "It's time to prevent this to happen again. MILESELECTRIC, purge this script and GET US OUT OF HERE!"
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.3
            hide screen tear
            hide s_kill_bg
            hide s_kill
            hide noise
            hide vignette
            scene bg greenHill1
            show monika 2p at t33 zorder 4
            show sayori 4w at t32 zorder 3
            show tails tails04 at l31 zorder 2
            play music t9
            mtp "Sayori! Stop crying, please!"
            show sayori 4v at t32 zorder 3
            mtp "I know what you are feeling right now, Sayori."
            mtp tails06 "When I was younger, I was bullied in my hometown, thanks to my two tails and my curiosity for inventions and science."
            mtp "I almost decided to end all of this, so I got away from my town, to the forest near Hill Top zone."
            mtp "I was searching for a place with the most altitude to do it."
            mtp tails05 "Then Sonic looked at me from a distance and ran towards me."
            mtp "He asked what's wrong, and I vented to him, almost crying."
            mtp "Sonic felt so dissapointed in my family and friends. He decided that I would be his brother from now on."
            mtp tails00 "So he took me to Green Hill and showed me his plane, the Tornado!"
            mtp "I started to do modifications and fixes to it. As a thank you, Sonic teached me how to keep up with his speed using my tails as an acceleration method."
            mtp "I can't say my depression got away easily. Sometimes I still have nightmares about my childhood."
            mtp "But Sonic is always here for helping me to cope with it and have another adventure."
            show sayori 3t at s32 zorder 3
            mtp "That's why: 1) I'm specially worried in rescuing my friend, and 2) I think you are the most capable to this mission, Sayori."
            m 4b "And I will give you directions from here! I will never abandon my Vice President, Sayori!"
            mc "And with that, Captain, I think we are ready to go. I have my partner, they have the Extreme Gears, and Monika will command from here."
            s "Thanks Rookie and Tails for trusting in me. This is why you are my favourite, cute little fox."
            s "And I would never know you have the same problem as me..."
            mtp tails02 "It feels great to be the favourite of someone! You can do it, Sayori!"
            mtp tails00 "I will go with you two to make sure this mission succeds and give emotional support to Sayori. Is this ok with you, Knuckles?"
            kte "Excellent, then! Operation: Rescue is officially starting!"

            "You got 700 rings for your poem for Sayori, and also for being brave and seeing THAT scene again!"
            play sound Ring
            $ persistent.ringCount += 700
            "You now have [persistent.ringCount] Rings!\n{i}Click to continue...{/i}"

        "I prefer not seeing it":
            show knuckles at thide zorder 1
            hide knuckles
            show monika 2p at t33 zorder 4
            show sayori 4w at t32 zorder 3
            show tails tails05 at l31 zorder 2
            play music t9
            mtp "I decided to stop this corruption of the script from happening. It was too much for us."
            mtp tails04 "Sayori! Stop crying, please!"
            show sayori 4v at t32 zorder 3
            mtp "I know what you are feeling right now, Sayori."
            mtp tails06 "When I was younger, I was bullied in my hometown, thanks to my two tails and my curiosity for inventions and science."
            mtp "I almost decided to end all of this, so I got away from my town, to the forest near Hill Top zone."
            mtp "I was searching for a place with the most altitude to do it."
            mtp tails05 "Then Sonic looked at me from a distance and ran towards me."
            mtp "He asked what's wrong, and I vented to him, almost crying."
            mtp "Sonic felt so dissapointed in my family and friends. He decided that I would be his brother from now on."
            mtp tails00 "So he took me to Green Hill and showed me his plane, the Tornado!"
            mtp "I started to do modifications and fixes to it. As a thank you, Sonic teached me how to keep up with his speed using my tails as an acceleration method."
            mtp "I can't say my depression got away easily. Sometimes I still have nightmares about my childhood."
            mtp "But Sonic is always here for helping me to cope with it and have another adventure."
            show sayori 3t at s32 zorder 3
            mtp "That's why: 1) I'm specially worried in rescuing my friend, and 2) I think you are the most capable to this mission, Sayori."
            m 4b "And I will give you directions from here! I will never abandon my Vice President, Sayori!"
            mc "And with that, Captain, I think we are ready to go. I have my partner, they have the Extreme Gears, and Monika will command from here."
            s "Thanks Rookie and Tails for trusting in me. This is why you are my favourite, cute little fox."
            s "And I would never know you have the same problem as me..."
            mtp tails02 "It feels great to be the favourite of someone! You can do it, Sayori!"
            mtp tails00 "I will go with you two to make sure this mission succeds and give emotional support to Sayori. Is this ok with you, Knuckles?"
            kte "Excellent, then! Operation: Rescue is officially starting!"

            "You got 400 rings for your poem for Sayori!"
            play sound Ring
            $ persistent.ringCount += 400
            "You now have [persistent.ringCount] Rings!\n{i}Click to continue...{/i}"

    scene bg tcChemicalPlant
    with dissolve_scene_full
    pause 3.0
    scene bg chemicalPlant
    with dissolve_scene_full
    if persistent.packagedMusic == True:
        play music chemPlantPCKG
        show honey djHoney at l31 zorder 5
        dj "Now playing: {i}Global Deejays - Happy Station{/i}, a happy tune for your tasty chemical beverages and rescue missions!"
        show honey at lhide zorder 1
        hide honey
    else:
        play music chemPlant1
    "And so, this is it! Operation: Rescue is ongoing!"
    show sayori 1a at l22 zorder 2
    show tails tails02 at l21 zorder 3
    "Sayori, Tails and I are on Chemical Plant now."
    "I can see that Sayori is excited and surprised. She and Tails opened themselves a lot, and with me too."
    "So we had a very interesting conversation while we travelled to Chemical Plant."
    show sayori 4n at t22 zorder 2
    "Now Sayori is looking with surprise the flow of the blue chemical fluids..."
    "And those cute circular chemical serpents that jumps from tube to tube."
    "Monika is talking to us using Tails' communicator."
    m "This is it, [player], Sayori and you will rescue Sonic!"
    s 3d "Sorry for worring you all before, friends."
    s 3j "Now I feel more confident than ever. We will rescue Sonic and kick Eggman's ass"
    mc "Woah Sayori! You really are more confident now! I'm glad!"
    show sayori 3q at t22 zorder 2
    mc "This is it, everyone. We are searching for a secret passage to Eggman's Prison."
    mc "Enjoy the landscape and be focused. If we won, Sayori will have more onion rings sandwiches, and possibly Sonic will share chillidogs with her too!"
    mtp tails07 "Hey guys! Look! The secret entrance to the prison! Let's follow those robots!"

    scene bg chemicalPlant2
    with dissolve_scene_half
    if persistent.packagedMusic == False:
        play music chemPlant2
    "And so, we found the secret entrance to the prison."
    "It was hidden in the second part of the Chemical Plant, in the Liquid Process Section."
    show eggpawn eggpawn1 at t11 zorder 2
    "And as soon as we appeared, a small troop of EggPawns started to ambush us!"
    show eggpawn at thide zorder 1
    hide eggpawn
    show sayori 4h at l22 zorder 2
    show tails tails07 at l21 zorder 3
    mc "EGG PAWNS! What we can do???"
    mtp "Quick! Let's do an attack formation! Prepare your Wispon main weapon, i will distract them and..."
    mtp tails04 "SAYORI WHAT ARE YOU DOING?????"
    m "SAYORI STOP WHAT I THINK YOU ARE GONNA DO!!!!! PRESIDENTIAL ORDER!!!!!!!"
    s 4j "UGLY ROBOTS! SURRENDER TO THE POWER OF THE LITERATURE CLUB!"
    s "SAYOOOOOOORIIIIIIIIII PUNCH!"
    "Sayori is running to tackle the robots..."
    show tails at thide zorder 1
    hide tails
    show sayori 4j at t21 zorder 2
    show eggpawn eggpawn1 at t22 zorder 3
    play sound destroy
    show eggpawn at lhide zorder 1
    hide eggpawn
    s 4r "I did it! I destroyed a pair of robots! We are winning this wa..."
    show eggpawn eggpawn1 at t22 zorder 3
    "Suddendly an entire group of Egg Pawns surrounded Sayori!"
    s 4p "ARE YOU FUCKING KIDDING ME!!!!!!"
    show sayori 4p at s21 zorder 2
    s "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!!!!!! HELP ME!!!!!!!"
    play sound destroy
    show eggpawn eggpawn1 at t22 zorder 2
    show sayori 4p at h21 zorder 3
    play sound destroy
    pause 1.0
    show sayori 4p at h22 zorder 3
    play sound destroy
    pause 1.0
    show sayori 4p at h21 zorder 3
    play sound destroy
    pause 1.0
    show sayori 4p at h22 zorder 3
    play sound destroy
    pause 1.0
    show sayori 4p at h21 zorder 3
    play sound destroy
    pause 1.0
    show sayori 4p at h22 zorder 3
    play sound destroy
    pause 1.0
    show sayori 4p at h21 zorder 3
    play sound destroy
    pause 1.0
    show sayori 4p at h22 zorder 3
    play sound destroy
    pause 1.0
    show sayori 4p at h21 zorder 3
    play sound destroy
    pause 1.0
    show eggpawn at lhide zorder 3
    hide eggpawn
    "She destroyed the robots by making them try to follow her while she was running in circles!"
    "I can't believe that Eggman's robot troops are so stupid."
    play sound Ring
    "Animals and rings dropped of the robots, so I made sure to collect all the rings."
    show sayori 5a at t22 zorder 2
    show tails tails05 at t21 zorder 3
    mtp "Well, this was an unorthodox way of cleaning this area, Sayori. Congrats?"
    s "Sorry guys, again xD."
    "So, anyways, the way to Sonic's prison cell is clear!"
    return
