label chapter3_mid:
    scene bg studiopolis2
    with dissolve_scene_half
    if persistent.packagedMusic == True:
        play music studioPCKG1
    else:
        play music studioP2
    "And so, Sonic, Amy, Monika, Sayori, Natsuki, Ghost, MC and I continued our journey through Studiopolis."
    "Now we are inside the big EGGTV studio in which Eggman produces his empire propaganda."
    "But we couldn't explore all of it, because... guess who's here."
    show monika 4g at l43 zorder 2
    show natsuki 1g at t42 zorder 3
    show mc2 1g at t44 zorder 5
    show sayori 1g at t41 zorder 4
    m "Yuri!"
    show monika at lhide zorder 1
    show mc2 at lhide zorder 1
    show sayori at lhide zorder 1
    hide monika
    hide sayori
    hide mc2
    show natsuki 1d at t41 zorder 3
    show yuri cuts1 at l43 zorder 4
    y "I can't believe this! It's like you're following me!"
    n 4e "Stop right there, Yuri!"
    show sonic sonic07 at l44 zorder 5
    sth "You better start explaining what you're doing in Eggman's TV studio. And why you do you want to build your Empire on his?"
    y cuts5 "NO! The right question is: Why don't you just fight my trashy robot????"
    y cuts7 "Metal Monika, show yourself!"
    show boss2 metalMonika at h42 zorder 3
    m "METAL. MONIKA. IN ORDER. OPERATING SYSTEM ACTIVE AND FUNCTIONING CORRECTLY!"
    m "AND. I'M. STILL. STUPID! LIKE ORIGINAL MONIKA!"
    n 4o "STOP WITH THIS SHIT, YURI! I WOULD BE SO GLAD TO SMASH YOUR BOOBS ON THE FLOOR RIGHT NOW..."
    mc "NATSUKI! LANGUAGE!"
    n 4v "BUT-BUT-BUT-BUT!!! AAAAAAAAAAAAA!"
    y cuts2 "Hey, brat! I even choose a song especially for this battle between cuties!"
    stop music fadeout 2.0
    if persistent.packagedMusic == True:
        y cuts5 "AND THIS TIME, YOU STUPID DJ, PLAY EXACTLY WHAT I WROTE ON THE SHEET OF PAPER I GAVE TO YOU!"
        play music metalDokisPCKG
        show honey djHoney at l31 zorder 5
        dj "Now playing: {i}Alvaro & Jetfire - Guestlist{/i}. You can do it! Beat that faker!"
        show honey at lhide zorder 1
        hide honey
    else:
        play music metalDokis
    show natsuki 4p at h41 zorder 3
    n "YUUUURIIIIIIIII!!!!"
    show sonic sonic09 at h44 zorder 5
    sth "Take it easy, buddy... take it easy... take it..."
    sth sonic05 "Here we go... we lost her."
    show sonic at lhide zorder 1
    hide sonic
    show yuri cuts2 at t33 zorder 4
    show natsuki 4v at h31 zorder 5
    show boss2 metalMonika at h32 zorder 4
    n "YURIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII...!"
    show yuri at thide zorder 1
    hide yuri
    n 4o "I WILL BEAT THE SHIT OUT OF YOU AND YOUR FUCKING PIECE OF SHIT ROBOT!"
    show natsuki 4o at h31 zorder 5
    show boss2 metalMonika at h32 zorder 4
    show sonic sonic07 at h33 zorder 5
    m "Natsuki! Remember that Rookie is the one that chooses who should fight them!"
    n "Yeah, right... Rookie! Which one of us do you choose?"
    mc "Well! We don't have time to make poems! So I will use the same decision that I made on the EGGTV minigame!"
    if ch4_scene == "yuri":
        $ ch4_scene = "natsuki"
    if ch4_scene == "natsuki":
        mc "Natsuki, I already selected you in the minigame, so it's best that you fight her!"
        n "WITH FUCKING PLEASURE!"
        "And so, the battle between Natsuki and Metal Monika has begun!"
    elif ch4_scene == "monika":
        mc "Well, I already selected Monika in the minigame. And this robot is based on her, so it's best that she has the chance to fight it."
        show natsuki at lhide zorder 1
        hide natsuki
        show monika 2h at l31 zorder 5
        m "First of all, I wanna say something."
        mtp "MONIKA, STOP! WHAT YOU THINK ARE YOU DOING?{nw}"
        mtp "OH MY GOD, MONIKA YOU PROMISED!{nw}"
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        stop music fadeout 2.0
        pause 6.0
        hide screen tear
        show sonic at thide zorder 1
        hide sonic
        show boss2 at thide zorder 1
        hide boss2
        show darkred zorder 98:
            alpha 0.0
            easein 4.0 alpha 1.0
        show noise zorder 99:
            alpha 0.0
            linear 3.0 alpha 0.25
        show ghostMenuFull zorder 3
        show monika dragon at face(y=600) with dissolve
        m "I'M SO FUCKING DONE WITH ALL YOUR JOKES."
        m "WHAT DID I DO TO DESERVE ALL OF THIS?"
        m "I'M TRYING TO {i}HELP{/i} EVERYONE."
        m "I CARE ABOUT MY FRIENDS."
        m "I CARE ABOUT EVERYONE IN THIS WORLD."
        m "I'M NOT EVIL! I WILL NOT DELETE MY FRIENDS! I WILL NOT BETRAY YOU FOR YOUR LOVE AT THE LAST SECOND!"
        m "SO, PLEASE, WITH ALL MY LOVE..."
        m "STOP BASHING ME WITH MY PAST MISTAKES. OK? THANK YOU."
        mtp "MONIKA BRING THE GAME BACK NOW!!!!!!"
        m "Okay Tails."
        m "And you, player, look at this marvelous background for some time to think about {i}what I'm still capable of in this game.{/i}"
        $ quick_menu = False
        hide monika
        pause 0.75
        hide ghostMenuFull
        scene white
        show image "gui/menu_art_m_ghost.png":
            xpos -100 ypos -100 zoom 3.5
        show darkred zorder 98:
            alpha 0.0
            easein 4.0 alpha 1.0
        show noise zorder 99:
            alpha 0.0
            linear 3.0 alpha 0.25
        pause 5.0
        hide noise
        hide darkred
        $ quick_menu = True
        show monika 2h at l31 zorder 5
        show boss2 metalMonika at h32 zorder 4
        show sonic sonic07 at h33 zorder 5
        if persistent.packagedMusic == True:
            play music metalDokisPCKG
        else:
            play music metalDokis
        m "Metal Trashy."
        show sonic sonic10 at h33 zorder 5
        sth "Woah! What happened to Studiopolis' background?{nw}"
        m "Your existance will end in a cacophonic epiphany, trashy robot!"
        show sonic sonic08 at h33 zorder 5
        sth "Seriously these girls are scary, 'specially Monika. Better to not give my opinion on this.{nw}"
        m 5b "AND ONLY ONE MONIKA WILL PREVAIL, AND THAT MONIKA WILL BE {i}ME{/i}."
        show sonic at thide zorder 1
        hide sonic
        show boss2 at thide zorder 1
        hide boss2
        show monika dragon at face(y=600) with dissolve
        m "AND NO, I WILL NOT BOTHER TO RESTORE THE BACKGROUND AGAIN."
        m "I HOPE WE BOTH UNDERSTAND EACH OTHER NOW."
        mtp "MOONIIIKAAA!!!!!!!\nENOUGH!!!!!!!"
        "Leeeeeeeeeeeeet's get to the battle, ok?"
    elif ch4_scene == "sayori":
        mc "Well, I already selected Sayori in the minigame. But I'm concerned about her getting hurt... or worse..."
        show natsuki at lhide zorder 1
        hide natsuki
        show sayori 2j at l31 zorder 5
        s "No need to be concerned, Rookie! Sayori the Robot Destroyer is ready to fight!"
        mc2 "I will help my cinnamon bun too, Rookie! My awesome videogame skills will be useful at last!"
        s 4j "IT'S TIME TO GET YOU OUT OF MY HEAD, METAL TRASHY!"
        "And so, the battle between Sayori and MC against Metal Monika has begun!"
    else:
        mc "Well, I already selected Ghost in the minigame. It's time to prove yourself, Ghost!"
        show natsuki at lhide zorder 1
        hide natsuki
        show ghostnatsuki gNatsu1 at l31 zorder 5
        g "..."
        play sound "sfx/crack.ogg"
        g gNatsu2 "THERE IS NOTHING MORE CATHARTIC THAN DESTROYING PIECES OF SHIT LIKE YOU, ROBOT."
        $ style.say_dialogue = style.edited
        g "IT'S TIME FOR YOU TO PLAY WITH MEEEEEEEEEEEEEEEEEE!!!"
        $ style.say_dialogue = style.normal
        "And so, the battle between Ghost and Metal Monika has begun!"
    pause 2.0

    scene bg studiopolis2
    with dissolve_scene_half
    stop music fadeout 2.0
    "As always, because this is a demo, we don't have the script for boss fights yet, so..."
    "The girls, Sonic and I fought hard, and we defeated the Monika robot!"
    show monika 4b at t31 zorder 4
    m "And this is goodbye for my pathetic imitation."
    show yuri cuts5 at h32 zorder 4
    y "THIS WILL NOT BE THE END! I WILL REBUILD HER, AND CREATE ANOTHER ROBOT TOO! YOU WILL NOT STOP MY DREAM, THE YURI EMPIRE!"
    m 2h "STOP THIS STUPID SHIT, YURI! YOU EVEN WEREN'T EVEN THE PRESIDENT OF A CLUB, AND YOU WANT TO BE THE QUEEN OF AN EMPIRE? C'MON!"
    y "It's menester to say that I didn't ask for your opinion, President of the Failure Club!"
    m 5b "Okay, everyone! I will slap this son of a bitch in the face!"
    inf "How cute! A girly fight! I just asked the world for a REAL challenge, and it answered me with two stupid teenagers fighting for petty reasons."
    inf "This is really unfair."
    m 2i "Infinite!"
    y 2y5 "At last this asshole decided to show himself!"
    if persistent.packagedMusic == False:
        play music infiniteMusic
    else:
        play music infiniteJoke
        inf "NO. I WILL NOT WASTE TIME COMPLAINING ABOUT THE MUSIC. IF YOU WANT IT THAT WAY, I WILL BE PROFESSIONAL."
    show infinite infinite3 at l33 zorder 4
    inf "Well, well, well- The President of the Literature Club, the so-called Queen of the Yuri Empire, and you."
    inf infinite2 "I hope you are feeling fear, [player], we both know that you remember me."
    inf infinite3 "Are you feeling the same fear that you felt when I killed your pathethic friends from the Resistance?"
    show monika 5b at h31 zorder 4
    show yuri cuts5 at h32 zorder 4
    inf "Oh well, it seems you didn't learn your lesson, Rookie. And now the pain will hit you harder."
    m "YOU ARE A MURDERER AND A PSYCHO! ROOKIE WILL NEVER BE AFRAID OF YOU!"
    y "YOU ARE A MURDERER! I WILL NEVER WORK WITH YOU ON MY GOALS!"
    inf "DID I ASK FOR YOUR OPINIONS, TEENAGERS? YOU TWO SMELL LIKE FEAR ENCARNATE!"
    inf "AND IF YOU WERE SERIOUSLY DESPERATE FOR A BOYFRIEND TO MAKE OU..."
    show monika 1p at h31 zorder 4
    show yuri 2p at h32 zorder 4
    show sonic sonic15 at l41 zorder 5
    sth "Actually, that odor is mine! I ran here all the way from the Chemical Plant!"
    sth sonic02 "And why don't we just talk a little, Infinite? We could chat about your favourite color, your favourite cupcake flavour, the secret source of your power..."
    inf infinite2 "THIS DOESN'T INVOLVE YOU, STUPID WIMPY HEDGEHOG! I ALREADY DEFEATED YOU, YOU PATHETIC SEWER RAT!"
    inf "AND MY POWER SOURCE IS TOP SECRET!!!!"
    sth sonic04 "Jeez! If you seriously wanna confess to one of the girls, you could have just said it already!"
    sth "And you can't just tell a lady that they need to do that kind of stuff! Aren't you a gentleman, Infinite?"
    show sonic at lhide zorder 1
    hide sonic
    inf "OK, I DON'T WANNA WASTE MORE TIME WITH THESE LOSERS! IF YOU WANNA FIGHT, SHOW YOURSELVES ON FLYING BATTERY! I WILL BE WAITING THERE!"
    show monika 2h at t31 zorder 4
    show yuri cuts5 at t32 zorder 4
    show infinite at thide zorder 1
    hide infinite
    m "Yeah! Go away, coward!!! And also, Infinite, both Yuri and I are busy, because we have a special person already!"
    show yuri 4d at h22 zorder 4
    show monika 2h at t21 zorder 4
    stop music
    play sound djstop
    y "Monika what are you saying??????"
    y 4c "I don't have a special person..."
    m 3b "Yes you do! You left a piece of scrap paper inside your book in the last club meeting."
    m "It looked like you were working on a poem called \"Simple Confession for my Lovely Cupcake\", and it was dedicated to Natsuki."
    m "You even started to imitate her style, because your poem was full of simple words and ideas to express your feelings to her!"
    show monika 2j at t21 zorder 4
    show yuri 1y2 at h22 zorder 4
    y "MONIKA GODDAMMIT DON'T SAY IT OUT LOUD!!!"
    y 4c "URRRGH! THANKS, PRESIDENT."
    "Sorry, Natsuki obviously noticed..."
    show natsuki 4p at l31 zorder 5
    n "WHAT. THE. FUCKING. FUCK??????"
    n 4o "YURI! TELL ME THIS IS A JOKE, RIGHT?"
    play music t10
    y "No, Natsuki, it's not a joke."
    n 4m "Eh?"
    show natsuki 1n at t31 zorder 5
    y 1w "Since the first day we meet on the Literature Club, I've been in love with you."
    y 1v "I love your attitude to confront your life and all the problems you have everyday."
    y "I love all the cute things you do for all of us, especially your cupcakes. They go so well with my tea."
    y 1u "And even though I told MC that I disliked your poetry style and your advice was biased, it was a lie to trying to forget my feelings and redirect them to MC."
    show monika 1o at t21 zorder 4
    y 1t "But that was in vain. I never loved MC, even when Monika hacked us, I tried to fight those feelings."
    show monika 1j at t21 zorder 4
    show natsuki 1u at t31 zorder 5
    y "The one that I love is you, Natsuki. You are my special person. I want to make you happy everyday."
    y "You can even stay in my house if you want, if we recover our world. Or you can be with me in my Empire."
    y 1s "Natsuki, do you accept my confession?"
    show monika at lhide zorder 1
    hide monika
    show natsuki 1u at t21 zorder 4
    n "URGGGGH YURI, PLEASE DON'T SAY ANYMORE THOSE CUTE THINGS ABOUT ME!"
    n 1v "I TOLD YOU ALREADY I'M NOT CUTE, AND, AND, AND..."
    n 1r "..."
    n 1u "..."
    n 12f "I love you too, Yuri. I always loved you, too."
    n "I accept your confession."
    n 12h "But let's not make this more awkward, OK? My friends and my hero are still here."
    y 2j "You still need to fight that asshole on the Flying Battery, right?"
    y "I know you can. I have other things to do for a while."
    y 4c "You don't know how much I want to kiss you right now! But I will not do it in front of everyone, I agree with you on that."
    y 4e "I will wait for you in that Zone called Press Garden, don't fail me! And please don't come before fighting Infinite first..."
    show yuri at lhide zorder 1
    hide yuri
    show natsuki 12h at t11 zorder 2
    "Yuri ran away very fast, with a purple imitation of Eggman's Extreme Gear."
    mc "Well... I don't know what to say or do at this moment..."
    m "Me neither..."
    show natsuki 12h at t21 zorder 2
    show sonic sonic13 at t22 zorder 2
    sth "The right thing to do is put our Extreme Gears in flying mode, and go to Eggman's Flying Battery to kick Infinite's ass!"
    n "Sorry Sonic, but I need all of you supporting me when I go to Press Garden..."
    m "Well, it's Rookie's decision!"
    menu:
        "Flying Battery.":
            $ chapter3decision = "FB"
            mc "Sonic is right! We need to go to Flying Battery first and fulfill the mission!"
            show sonic sonic14 at t22 zorder 2
            mc "Remember that {i}Yuri{/i} told us that we must continue the mission before checking on her."
            sth "I feel this is the perfect opportunity for Tails and myself to know what's up with Infinite. We need to go there first!"
            sth "I promise that we will defeat Infinite the Sonic way: faster! And then we will go see Yuri."
            mc "So, Flying Battery, here we go!"

            pause 1.0
            stop music fadeout 1.0
            scene black
            with wipeleft_scene
            "You got 250 rings for ending Chapter 3!"
            "You got 500 rings for getting a Chaos Emerald!"
            "Yuri gifted you 1000 rings for her confession!"
            "Sonic gifted you 1000 rings for your choice!"
            play sound Ring
            $ persistent.ringCount += 2750
            if persistent.sonicMania == True:
                "The mod author gives you 2000 rings as a gift for playing Sonic Mania with Doki Doki Studiopolis Club mod!"
                $ persistent.ringCount += 2000
            "You now have [persistent.ringCount] Rings!\n{i}Click to continue...{/i}"
            call screen confirm("You have unlocked a special poem.\nWould you like to read it?", Return(True), Return(False))
            if _return:
                call expression "poem_special_" + "5" from _call_expression_48
                scene black with Dissolve(1.0)
            else:
                pass
            return
        "Press Garden.":
            $ chapter3decision = "PG"
            mc "Sorry, Sonic. I'm with Natsuki on this one."
            show natsuki 12f at t21 zorder 2
            mc "While you and Amy went ahead, we were worried and we talked a lot about Yuri."
            m "Also, Yuri was acting like herself while she confessed, so it's the right time to try to help her and see whats wrong!"
            m "And we are sure Natsuki is eager to see her!"
            mc "So, then, Press Garden, here we come!"

            pause 1.0
            stop music fadeout 1.0
            scene black
            with wipeleft_scene
            "You got 250 rings for ending Chapter 3!"
            "You got 500 rings for getting a Chaos Emerald!"
            "Yuri gifted you 1000 rings for her confession!"
            "Natsuki gifted you 1000 rings for your choice!"
            play sound Ring
            $ persistent.ringCount += 2750
            if persistent.sonicMania == True:
                "The mod author gives you 2000 rings as a gift for playing Sonic Mania with Doki Doki Studiopolis Club mod!"
                $ persistent.ringCount += 2000
            "You now have [persistent.ringCount] Rings!\n{i}Click to continue...{/i}"
            call screen confirm("You have unlocked a special poem.\nWould you like to read it?", Return(True), Return(False))
            if _return:
                call expression "poem_special_" + "5" from _call_expression_47
                scene black with Dissolve(1.0)
            else:
                pass
            return


