label prologue:
    $ persistent.sayori_kill = False
    $ forces.override_perms()
    if persistent.ghost_menu:
        $ forces.send_temporary_notification("Foster the Ghosts", "Pumped Up Kicks and the Ghost Menu spooked you.", action=Return(1))
    if persistent.seenPrologue == False:
        scene bg prologue1
        with dissolve_scene_full
        "Welcome to Doki Doki Forces!"
        "In this story, you will help Sonic and friends to beat the power of the Phantom Ruby!"
        if persistent.genderMale == True:
            show avatar avatarMale at t11 zorder 2
            "For that, you will play as the Sonic Forces' pal, Rookie!"
            "But you will not fight this battle alone!"
            show monika 2h at t31 zorder 4
            show yuri 2s at t33 zorder 4
            show avatar avatarMale at t32 zorder 2
            "You will have the help and support of the most powerful allies!"
            "The Literature Club! Doki Doki!"
            show avatar at thide zorder 1
            show monika at thide zorder 1
            show yuri at thide zorder 1
            hide avatar
            hide monika
            hide yuri
        else:
            show avatar avatarFemale at t11 zorder 2
            "For that, you will play as the Sonic Forces' pal, Rookie!"
            "But you will not fight this battle alone!"
            show natsuki 5g at t31 zorder 4
            show sayori 2j at t33 zorder 4
            show avatar avatarFemale at t32 zorder 2
            "You will have the help and support of the most powerful allies!"
            "The Literature Club! Doki Doki!"
            show avatar at thide zorder 1
            show natsuki at thide zorder 1
            show sayori at thide zorder 1
            hide avatar
            hide sayori
            hide natsuki
        menu:
            "Did you play Sonic Mania with the Doki Doki Studiopolis Club mod?"
            "Yes!":
                $ persistent.sonicMania = True
                "Ok then! I hope you enjoyed it!"
            "No":
                $ persistent.sonicMania = False
                "Oh. Ok then! Thanks for the answer!"
        show mc2 1 at t31 zorder 4
        show femc lh_1 at t33 zorder 4
        menu:
            "Do you prefer male MC or female MC as the fifth club member?"
            "Male MC":
                $ persistent.ddlc_femc = False
                show femc at thide zorder 1
                hide femc
                show mc2 1 at t11 zorder 4
                $ mc2_name = renpy.input("What's the name of the fifth club member?", default="", length=10)
                $ mc2_name = mc2_name.strip()
                mc2 4c "Thanks for choosing me!"
                mc2 5p "From now on, I will be know as [mc2_name]."
            "Female MC":
                $ persistent.ddlc_femc = True
                show mc2 at thide zorder 1
                hide mc2
                show femc lh_1 at t11 zorder 4
                $ femc_name = renpy.input("What's the name of the fifth club member?", default="", length=10)
                $ femc_name = femc_name.strip()
                femc lh_2c "Thanks for choosing me!"
                femc lh_3w "From now on, I will be know as [femc_name]."
                $ forces.send_temporary_notification("Cinnamon Bun Shake", "You choose Female MC as the fifth club member and shake up the canon.", action=Return(1))
        "Without further ado, let's start!"
        $ persistent.seenPrologue = True
    else:
        scene bg prologue1
        with dissolve_scene_full
        "Welcome to Doki Doki Forces!"
        if persistent.yuriKnife == True:
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.3
            hide screen tear
            play sound ruby
            scene bg prologue2
            play music yuripls
            show rubypink zorder 5:
                alpha 0.0
                easein 4.0 alpha 0.5
            show yuri cuts6 at h11 zorder 4
            $ style.say_dialogue = style.edited
            y "Do you believe that starting a new game will save you from ME???"
            y "Your save file is already corrupted!!!\n{i}The Yuri Empire WILL RISE!!!{/i}"
            show yuri at thide zorder 1
            hide yuri
            show emerald phantomRuby at h11 zorder 4
            y "Choose Yuri AGAIN on MILESPoem.exe!\n Yours truly, {i}the Phantom Ruby.{/i}"
            pause 1.0
            show emerald at thide zorder 1
            hide emerald
            hide rubypink
            play sound "mod_assets/rubySound2.ogg"
            scene bg prologue3
        $ style.say_dialogue = style.normal
        "Oh! This is not your first time here!"
        "So, then, let's not waste more time. Questions!"
        menu:
            "Did you play Sonic Mania with the Doki Doki Studiopolis Club mod?"
            "Yes!":
                $ persistent.sonicMania = True
                "Ok then! I hope you enjoyed it!"
            "No":
                $ persistent.sonicMania = False
                "Oh. Ok then! Thanks for the answer!"
        if persistent.yuriKnife:
            show mc2 1shock at t31 zorder 4
            show femc lh_1z at t33 zorder 4
        else:
            show mc2 1 at t31 zorder 4
            show femc lh_1 at t33 zorder 4
        menu:
            "Do you prefer male MC or female MC as the fifth club member?"
            "Male MC":
                $ persistent.ddlc_femc = False
                show femc at thide zorder 1
                hide femc
                if persistent.yuriKnife:
                    show mc2 1shock at t11 zorder 4
                else:
                    show mc2 1 at t11 zorder 4
                $ mc2_name = renpy.input("What's the name of the fifth club member?", default="", length=10)
                $ mc2_name = mc2_name.strip()
                if persistent.yuriKnife:
                    mc2 4t "What did you do, Player?"
                    mc2 5r "You did something to the game and the girls are suffering, please fix it..."
                    mc2 5z "Sorry for having to break character but I don't have another way to talk with you. Try to understand me."
                    mc2 5m "Let's be the heroes that Sayori and our friends need, ok? I trust you on this."
                else:
                    mc2 4c "Thanks for choosing me!"
                    mc2 5p "From now on, I will be know as [mc2_name]."
            "Female MC":
                $ persistent.ddlc_femc = True
                show mc2 at thide zorder 1
                hide mc2
                if persistent.yuriKnife:
                    show femc lh_1z at t11 zorder 4
                else:
                    show femc lh_1 at t11 zorder 4
                $ femc_name = renpy.input("What's the name of the fifth club member?", default="", length=10)
                $ femc_name = femc_name.strip()
                if persistent.yuriKnife:
                    femc lh_2y "You, asshole. I was waiting for this moment and talk to you."
                    femc lh_3t "You did something to the game that is making the girls suffer, Player. Fix it. Now."
                    femc lh_3q "Sorry for having to break character but I don't have another way to talk with you. Try to understand me."
                    femc lh_3x "Fix what you did, Player, or I will kick you so hard you will pray to not see me in any place ever again."
                else:
                    femc lh_2c "Thanks for choosing me!"
                    femc lh_3w "From now on, I will be know as [femc_name]."
        "Without further ado, let's start!"

    scene bg tcLitClub
    with dissolve_scene_full
    pause 3.0
    scene bg ruined_residential
    show sayori 3k at t33
    show yuri 1p at t31
    show natsuki 4i at t32
    with dissolve_scene_full
    call instant_rain
    play music ghostmenu
    $ style.say_dialogue = style.normal
    $ persistent.ringCount = 0
    $ persistent.emeraldCount = 0
    $ SystemUIServer.send_temporary_notification("Restoring from Backup", "AliceOS is restoring and playing the backup file.", action=Return(0))
    s "What is happening to our town???"
    s 1j "This looks like a war zone!"
    y "Natsuki, why we abandoned the safety of our own homes? Can you repeat it again?"
    n 1v "Yuri, you airhead!!!"
    n 4x "Monika texted us that we must go to the club room right now!"
    n "According to her, it's the only place in which we can be safe!"
    n 4i "And honestly, by the looks of it, I believe it totally at this point..."
    y 2t "I'm sorry, Natsuki, I'm honestly scared, I shall not doubt in our friend Monika again."
    s 2g "Yeah, after she apologized for what she did and restored our normal lives..."
    s 2f "The best we can do for her is trusting her."
    y "Then let's go to the clubroom before something bad happens, girls!"
    if persistent.ddlc_femc:
        s 4h "Wait! What about [femc_name]???"
        n "She should be in the school, she had classes early today, and probably she is with Monika at this point."
        n "She will be safe, Sayori, now let's go or else...!"
    else:
        s 4h "Wait! What about [mc2_name]???"
        n "He should be in the school, he had classes early today, and probably he is with Monika at this point."
        n "He will be safe, Sayori, now let's go or else...!"
    egg "Citizens of {i}REDACTED{/i}, surrender yourselves to the Eggman Empire!!!"
    egg "Give all of your precious resources to my Egg Squad!"
    egg "OR ELSE PREPARE TO SUFFER THE CONSEQUENCES!!!"
    show eggpawn eggpawn1 at t41 zorder 6
    show sayori 4p at t44
    show yuri 1y2 at t42
    show natsuki scream at t43
    egg "EggPawns!!! Kill everyone who doesn't agree to join my Empire!!! Make no exceptions!!!"
    s "WHAT WE GONNA DO???? WHAT WE GONNA DO???"
    y "THIS IS OUR END, GIRLS! I WAS SO PLEASED TO MEET ALL OF YOU!!!"
    n wispon "Dying today is not on my plans! Eat this, weird robot!"
    show eggpawn at thide zorder 1
    hide eggpawn
    show sayori 3k at t33
    show yuri 1p at t31
    show natsuki wispon at t32
    y "Natsuki, where did you got that... weird gun?"
    n "There's no time to explain!!! Let's hurry, the school is near!!!"
    call instant_rain_stop

    scene bg ruined_residential_ruby
    with dissolve_scene_full
    play sound ruby
    mc "Urgh..."
    mc "Where am I...? This is not Park Avenue..."
    play sound "mod_assets/rubySound2.ogg"
    scene bg ruined_residential
    call instant_rain
    "Seriously, where am I? It seems like this is another world of sorts. And it's already damaged."
    inf "So you followed me through the portal. Impressive."
    inf "You are not a coward, after all."
    show infinite infinite1 at t11 zorder 2
    mc "Infinite!"
    inf "Pleased to see you again, Rookie."
    inf "It seems the Phantom Ruby transported us both and Eggman's robots to this realm..."
    mc "What did you do with my friends of the Resistance???"
    show infinite infinite3 at t11 zorder 2
    inf "The Resistance. The Resistance. Seriously, don't you have a better question to ask?"
    inf "Your pathetic Resistance is fine. I just sent your pathethic friends to the afterlife."
    show infinite infinite2 at t11 zorder 2
    inf "And when I get to that school, I will steal the power source of this world, and you will be defenseless against me!"
    inf "I dare you to try to stop me now, coward."
    show infinite at thide zorder 1
    hide infinite
    inf "Now excuse me, I have some books, poems and mangas to burn for the glory of the Eggman Empire."
    mc "I can't let you win, Infinite! Come back here!!!!"
    if persistent.ghost_menu and not persistent.sayonika_unlocked:
        "But before [player] started to run, something flashed before the soldier."
        show syka orb at t11 zorder 2
        mc "What is this? It seems like a strange orb..."
        show syka orb at h11 zorder 2
        mc "Owww, orb, don't push me! It hurts!"
        mc "Is this your way to say that you want to follow me?"
        mc "Ok, we don't have much time to lose, Infinite is on the run! Follow me!"
    call instant_rain_stop

    scene bg corridor_creepy
    with wipeleft_scene
    mc "This is the school at which Infinite was flying."
    mc "Why it has to be so enormous? I visited two buildings of this school and Infinite is not there..."
    "*Rookie trips and falls to the ground.*"
    mc "Agggh... Just now..."
    mc "Wait, what is this piece of paper?"
    if persistent.ddlc_femc:
        call showpoem(poem_y6, music=False, revert_music=False, paper="mod_assets/poem_forces_femc.png")
    else:
        call showpoem(poem_y6, music=False, revert_music=False, paper="mod_assets/poem_forces.png")
    mc "Goddamit. I tripped with a pamphlet for a Literature Club, with a text I can't understand what it means."
    mc "It seems like a poem."
    mc "Wait a second..."
    inf "Now excuse me, {i}I have some books, poems and mangas to burn{/i} for the glory of the Eggman Empire."
    mc "THIS IS WHAT INFINITE IS LOOKING FOR!"
    mc "THE POWER SOURCE OF THIS WORLD IS IN THE ROOM OF THIS LITERATURE CLUB!!!"
    mc "[player], better hurry!!! The students of that club are in danger!!!"

    scene bg club_bulli
    with wipeleft_scene
    show monika 4b at t11 zorder 2
    m "Hey girls! I'm glad you are safe and sound!"
    m 2f "I was so worried that those weird robots did something to all of you."
    m "Something clearly is not right today and I can't fix it."
    show monika 2f at t22 zorder 3
    show sayori 2h at l21 zorder 2
    s "Actually, I believed that I was the only one here getting a bad feeling."
    s 1i "Wait Monika, seriously? I believed you were better than this."
    m "What is up, Sayori?"
    s 1j "The posters..."
    m 4l "Ahaha~! Sorry, I was messing around with the backgrounds. I didn't wanted to make you feel bad, I swear."
    if persistent.ddlc_femc:
        s 2g "Also, where is [femc_name], Monika? I'm worried about her!"
        m 2f "Me too, Sayori, but sadly, she was sent by her teacher to the gym with her own classmates."
        m 4g "We can't do anything for [femc_name] right now."
    else:
        s 2g "Also, where is [mc2_name], Monika? I'm worried about him!"
        m 2f "Me too, Sayori, but sadly, he was sent by his teacher to the gym with his own classmates."
        m 4g "We can't do anything for [mc2_name] right now."
    show monika 2f at t33 zorder 4
    show sayori 2g at t32 zorder 3
    show natsuki 4g at l31 zorder 2
    n "Hey girls, I remember..."
    $ style.say_dialogue = style.edited
    n 4v "fucking monikammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
    n "What about the posters on the clubroom???"
    $ style.say_dialogue = style.normal
    m 9h "I said that it wasn't my intention."
    n 4g "Whatever... Yuri said something a few days ago about these strange feelings..."
    n "She even wrote a poem about that as a pamphlet for the Festival."
    show monika 2f at t44 zorder 5
    show sayori 2g at t43 zorder 4
    show natsuki 4g at t42 zorder 3
    show yuri 4b at l41 zorder 2
    y "I remember, Natsuki: Stagnant air is a common sign that something very bad is about to happen."
    y 1f "Wait... what about those poste..."
    $ style.say_dialogue = style.edited
    show yuri 1y2 at t41 zorder 2
    m 16ad "I SAID: STOP LOOKING AT THE POSTERS!!!"
    m "Is that clear???"
    $ style.say_dialogue = style.normal
    y 4c "Uuuuh... I-i'm sorry, Monika."
    m "For gods sake, who will say another stupid thing next?"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.3
    hide screen tear
    if persistent.packagedMusic == False:
        play music infiniteMusic
    else:
        play music infiniteJoke
    inf "Hello ladies... Can I interrumpt this stupid and worthless meeting of yours?"
    show monika 1d at t44 zorder 5
    show sayori 1m at f43 zorder 2
    show natsuki scream at t42 zorder 4
    show yuri 1y2 at t41 zorder 3
    s "WHO SAID THAT??????"
    scene bg closet_creepy
    show monika 1d at t22 zorder 3
    show infinite infinite2 at t21 zorder 2
    with dissolve_cg
    inf "Excuse me, girl with the weird ribbon. Are you the leader of your girly group of scouts?"
    show monika 2h at t22 zorder 2
    show infinite infinite2 at t21 zorder 3
    if persistent.packagedMusic == False:
        m "The name is Monika, this is a {i}Literature{/i} club, and who the heck are you?"
        m "And what about this type of music without pianos and stuff?"
        show monika 2h at t22 zorder 3
        show infinite infinite3 at t21 zorder 2
        inf "So you can listen to the background music, interesting... I hope you like this masterpiece that represent myse..."
        show monika 2a at t22 zorder 3
        inf infinite7 "Wait this is not the point!"
        show monika 2h at t22 zorder 3
        show infinite infinite3 at t21 zorder 2
    else:
        m "The name is Monika, this is a {i}Literature{/i} club, and... and..."
        m 2l "PFFFFT! HAHAHAHAHAHAHAHAHAHA!"
        m "Is THAT what you call your 'background music'???"
        show infinite infinite3 at t21 zorder 2
        inf "So you can listen to the background music, interesting... I hope you like this masterpiece that represent myse...{nw}"
        inf infinite7 "Wait...{nw}"
        inf "WTF...{nw}"
        show monika at thide zorder 1
        hide monika
        show infinite infinite3 at face(y=600) with dissolve
        inf infinite3 "{i}WHAT THE FUCK DID YOU DO WITH MY AWESOME, POETICAL, AND EDGY MASTERPIECE????{/i}"
        inf "{i}WHAT IS THIS STUPID GANGAM STYLE????{/i}"
        inf "SERIOUSLY, YOU MUST START TO DO JOKES ON ME AT THE START OF THE GAME????"
        inf "I DEMAND MY GLORIOUS NORMAL MUSIC BACK!!!!"
        m "HEY YOU MISTER!"
        show infinite at thide zorder 1
        hide infinite
        show monika 4h at face(y=600) with dissolve
        m "CAN YOU STOP YOUR MELODRAMATIC EDGY BITCHING?"
        m "If you don't like the music, well, too bad."
        m "This is the result of the activation of the EDM Session variable in the game."
        m "So, that said, can you please go back to the script and stop breaking the fourth wall?"
        m "Getting in the face of the player is invasive and annoying."
        m 2e "But, for some reason, I love this."
        show monika 2h at t22 zorder 3
        show infinite infinite3 at t21 zorder 2
        m "Anyways, what's your name?"
        inf "FINE. You won, little girl."
    inf "Ehem... excuse me, my ladies. You all may call me... Infinite."
    inf infinite1 "I work for the glorious Dr. Eggman and his vision of the Eggman Empire."
    inf "And there is something very important for him in this school room."
    m 4i "Which you will absolutely not get!"
    $ consolehistory = []
    call updateconsole("os.remove(weird_invader)", "Our privacy policy has been updated!")
    pause 0.5
    stop music
    play sound djstop
    m 4h "You gotta be kidding me..."
    inf infinite6 "EHEEEEEM... As I was saying...!"
    scene bg club_bulli
    show rubypink zorder 5:
        alpha 0.0
        easein 4.0 alpha 0.5
    show sayori 1m at t33 zorder 4
    show natsuki scream at t32 zorder 3
    show yuri 1y2 at t31 zorder 2
    with dissolve_cg
    inf "Enjoy the few seconds of life you have left, while I extract what I need from your worthless world!"
    play sound ruby
    mc "Oh no! Not the Phantom Ruby again!! GODDAMIT INFINITE AND YOUR CHEAP RUBY STUFF!!!!{nw}"
    n "WHAT IS HAPPENING????{nw}"
    y "WHY IS EVERYTHING TINTED PINK????{nw}"
    s "WHY THE GRAVITY GET SO SCREWED????{nw}"
    m "GIRLS WATCH OUT...!!!!{nw}"
    call hideconsole
    $ delete_character("monika")
    $ delete_character("sayori")
    $ delete_character("natsuki")
    $ delete_character("yuri")
    
    stop music fadeout 2.0
    scene bg tcNullSpace
    with dissolve_scene_full
    pause 2.0
    if persistent.yuriKnife == True:
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
        show yuri 3y1 at t11 zorder 2
        y "DO YOU STILL BELIEVE THIS GAME IS ABOUT DOKI DOKI FORCES?"
        y "NO! THIS GAME IS ABOUT ME FULFILLING MY DREAM! THE YURI EMPIRE IS RISING THANKS TO YOU!"
        show yuri 3y3 at t22 zorder 2
        show emerald phantomRuby at h21 zorder 2
        y "If you wanna be a follower of the Yurism cult and survive..."
        y "Make sure to choose ME in the poem minigame."
        y "DON'T YOU DARE TO CHOOSE ANOTHER OF MY FRIENDS!"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
        play sound ruby
    
    scene bg nullspace
    with dissolve_scene_full
    # show layer front at sysCheckLoop
    # show s_sticker_gm_fixed at rotateLoop zorder 99
    if persistent.packagedMusic == True:
        play music nullSpacePCKG
        show honey djHoney at l31 zorder 5
        $ forces.edmsession_music("It's different - Give it all")
        dj "Now playing: {i}It's different - Give it all{/i}."
        show honey at lhide zorder 1
        hide honey
    else:
        play music mend
    $ SystemUIServer.send_temporary_notification("Backup restored", "AliceOS has been succesfully restored.", action=Return(0))
    "Grrr... so this is what happened then...?"
    "I got unconcious with Infinite's last attack, and now I just wake up in this weird limbo or something..."
    "The thing is: Infinite got all the remaining Phantom Ruby prototypes in my world, and the power source of this world."
    "Now Tails will not have any way of study and replicate it's power."
    "And also I couldn't save them. I couldn't save any of them AGAIN!"
    "This realm is destroyed thanks to Infinite, and..."
    mc "I can't believe that this bastard killed people! Again! And four innocent girls this time!"
    $ forces.send_tails_message("Rookie, can you read this? Please answer!")
    show sayori 2h at t41 zorder 2
    "The one with the red ribbon,"
    show natsuki 4g at t42 zorder 2
    "the one with pink hair,"
    if persistent.yuriKnife == True:
        show yuri 3y3 at t43 zorder 2
        $ style.say_dialogue = style.edited
        y "THE BEST GIRL OF THE CLUB, ME, THE AWESOME YURI!"
        y cuts1 "HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA!"
        $ style.say_dialogue = style.normal
    else:
        show yuri 4b at t43 zorder 2
        "the one with purple hair,"
    show monika 2h at t44 zorder 2
    $ style.say_dialogue = style.normal
    "and the one who seemed to be the leader of them."
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    $ forces.send_tails_message("Rookie! This is Tails! Can you read me?")
    if persistent.ddlc_femc:
        show femc lh_3t at t11 zorder 2
    else:
        show mc2 5x at t11 zorder 2
    "And according to the pamphlet, there was a fifth member of the club, that probably got killed too."
    if persistent.ddlc_femc:
        show femc at thide zorder 1
        hide femc
        with wipeleft
    else:
        show mc2 at thide zorder 1
        hide mc2
        with wipeleft
    "They were so defenseless against the power of Infinite and the Phantom Ruby!"
    "I couldn't save them, as the Resistance couldn't save Sonic when he needed us the most..."
    "I can sense their souls very faintly..."
    if persistent.ghost_menu and not persistent.sayonika_unlocked:
        show syka orb at t11
        "Wait! I still have this shiny orb with me. Glad it wasn't destroyed! At least I could save something."
        show syka orb at thide zorder 1
        hide syka
    $ forces.send_tails_message("Rookie! Tails here! Remember the pamphlet: they were part of a Literature Club...")
    mc "NO! I can't give up again like I cowardly did months ago on the first invasion!"
    mc "I just need to think of how to revive these girls..."
    mc "Those girls are lingering around here, in these Null Space!"
    mc "Maybe, just maybe, I can be able of save them if I write something... like that poem!"
    mc "But how?"
    $ forces.send_tails_message("ROOKIE!!! WHY CAN'T YOU JUST READ THE NOTIFICATIONS???")
    $ forces.send_tails_message("Sorry for doing this, buddy...")
    play music "mod_assets/labyrinthMuffled.ogg"
    "What the fuck? There is some music at the distance..."
    mc "This is impossible... the world was destroyed, there isn't any instrument capable of reproducing sounds left."
    "Wait! Is my MILESELECTRIC!!! This is my ringtone music! Stupid me!"
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 0>mod_assets/labyrinth.ogg"
    "As I correctly guessed, my Wispon weapon is flashing the MILESELECTRIC light."
    "So I'm capable of receiving a signal from my world! I eagerly accept the call!"
    if persistent.packagedMusic == False:
        stop music fadeout 2.0
        play music rWispon
    else:
        stop music fadeout 2.0
        play music nullSpacePCKG
    show tails tailsCom at t11 zorder 2
    mtp "Rookie! Can you hear me... BZZT... communication... BZZT... difficult."
    "Tails is trying to reach me using the messaging and phone app! This is a miracle!"
    mc "Tails, this is Rookie!"
    mtp "Rookie! Is good to see you alive! BZZT..."
    mtp "BUT PLEASE TELL ME WHY YOU CAN'T READ THE FRICKING NOTIFICATIONS!!!!!"
    "Whoops! My MILESELECTRIC is full of pending notifications from Tails."
    mc "Sorry buddy, ehehehe... I was focusing on something..."
    mtp "Okay, Rookie, I forgive you, but please, next time be more cautious of your MILESELECTRIC!!!"
    mtp "It can help you with everything!!!"
    mtp "Now BZZT... how can I help you?"
    mc "If you can hear me, help me with a way to write a poem! There are people I need to save!"
    mtp "BZZT... Did you said a {i}poem{/i}?"
    mc "JUST DO WHAT I SAID, TAILS!!!!"
    mtp "Let me check what kind of info I can recover from this destroyed world first!"
    $ consolehistory = []
    call updateconsole("MILES ELECTRIC SYSTEM ONLINE", "Checking for info...") from _call_updateconsole_22
    pause 0.5
    call updateconsole("Checking for characters...", "ERROR Characters deleted!") from _call_updateconsole_23
    pause 0.5
    call updateconsole("Checking for vital scripts...", "ERROR Scripts deleted!") from _call_updateconsole_24
    pause 0.5
    call updateconsole("Checking for music...", "Some music recovered, downloading...") from _call_updateconsole_25
    pause 0.5
    mtp "I can't find anything useful for you. Let me try something..."
    call updateconsole("Searching: POEM", "Searching...") from _call_updateconsole_26
    pause 0.5
    call updateconsole("Searching: POEM", "POEM Scripts found! Downloading...") from _call_updateconsole_27
    pause 0.5
    call updateconsole("Searching: POEM", "Doki Chibis found! Downloading...") from _call_updateconsole_28
    pause 0.5
    mtp "Ok! I recovered some info, and I know how to make your Wispon a {i}poem machine{/i}."
    mtp "There is some data related to Poem stuff I recovered."
    mtp "Even some cute chibi stuff from those scripts!"
    mtp "The only problem is that the background stuff will look scrambled because of what Infinite did to the scripts of this world."
    mtp "But don't worry, the main data will work and I created a new background for you! Initiating transference!"
    call updateconsole("Transfering MilesPOEM.exe", "MilesPOEM.exe loaded on Wispon!") from _call_updateconsole_29
    pause 0.5
    mtp "Now touch the icon for MilesPOEM.exe on the Wispon screen. It looks like a notebook! Do it now!"
    "And so I touched the new icon. I hope this works..."
    pause 1.0
    if persistent.yuriKnife == True:
        stop music
        play sound NegaRing
        "ERROR! YURIKNIFE == TRUE!"
        "JUST YURI."
        mtp "UH! What is this error? This is new!"
        mtp "\"YURIKNIFE\"? This was not in the recovered stuff before..."
        mtp "And Yuri Empire... Isn't it supposed to be called {i}Eggman{/i} Empire?"
        mtp "..."
        mtp "OH NO!"
        mtp "The script already sent Rookie to my POEM exe minigame, so I can't warn him, yikes!"
        mtp "And it seems detecting this error stops the game for everyone except the one who hacked the game."
        mtp "MILESELECTRIC, check any suspect activity, specially if Yuri is saved by Rookie!"
        mtp "If she is hacking the script, I'm sure I will find a way to hack it too and warn Rookie about this..."
        mtp "NO WAY, SHE CHANGED THE BACKGROUND IN MILESPOEM TOO! I HATE WHEN THEY HACK MY SOFTWARE! YURIIIIIII!!!!!!!!{nw}"
    $ mikEXEPoemChapter = 0
    stop music fadeout 2.0
    $ forces.send_temporary_notification("Obliterated Club", "You completed the prologue.", action=Return(1))
    scene bg tcPoem
    with dissolve_scene_full
    pause 3.0
    return