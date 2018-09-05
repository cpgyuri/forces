# Chapter 2 static content. Poem responses called from here are in script-poemresponses.rpy

label chapter2_mid:
    #Call exclusive scene
    $ nextscene = poemwinner[2] + "_exclusive_" + "2"
    call expression nextscene

    #After exclusive scene, we go back to poem responses
    scene bg chemicalPlant2
    with wipeleft_scene
    $ ch2_winner = poemwinner[2].capitalize()
    "And so, after we discovered the prison cells, the rest of the girls teleported to our position."
    "Monika found a place, near the end of the Chemical Plant, where she could connect MILESELECTRIC in order to spy and hack Eggman's network."
    "She managed to find some files that indicated information about projects of robots, Infinite's data, and a new base of operations that Eggman will build on a planet that orbits us from time to time."
    "Sure thing that is the legendary Little Planet, the place where you can control the flow of time using speed."
    "The pipe system that was not connected to the liquids was specially used to travel quickly within the second complex of buildings."
    "The sensation of slipping through the tubes made everyone feel, for a few minutes, like children."
    "The exit door and Sonic's special prison cell where on a long road parked on a platform, which floated on a giant river of blue chemicals."
    "Suddendly, when we reached the plataform, the alarms of the place go hairwire!"
    mtp "Attention! I detect the presence of an Eggman robot in the area. Be careful!"
    play music bossQueen
    show boss1 queenBomber at t21 zorder 3
    "Indeed, from the river of chemical compounds emerged a robot of considerable size, autonomous, capable of creating a force field of liquid."
    "It was the Queen Buzz Bomber! And it was prepared to ramming us!"
    if ch2_winner == "Monika":
        #do something
        show monika 5b at t22 zorder 2
        m "I can't seem to hack you, but Rookie and I will sure beat you, ugly bee!"
    elif ch2_winner == "Natsuki":
        #do another something
        show natsuki 5o at t22 zorder 2
        n "THIS IS FOR SONIC, YOU UGLY BITCH! PREPARE TO BE SMACKED DOWN!"
    else:
        #another shit
        show sayori 4p at t22 zorder 2
        s "AAAAAAAAAAAAAAAAAAAH! Another ugly robot!!!!"
        s 4o "Wait Sayori!"
        s 4h "This is not the moment to be afraid! We are helping on Rookie's important mission!"
        s 4j "Hey you, ugly bee! Do you want to share happy thoughts with me????"
    "The battle against the first Eggman Boss has begun!"
    "Now, because this is the demo, we will assume we won the fight against the robot."
    "Don't worry, we will have boss battles soon. Anyways..."
    show boss1 at thide zorder 1
    hide boss1
    show monika 5a at t32 zorder 3
    show natsuki 1g at t31 zorder 4
    show sayori 4b at t33 zorder 2
    "The girls and I fought to death, and after some time, the Queen Buzz Bomber was defeated!"
    m "Good job girls!"
    n "WE DID IT, PUNKS! LIKE THE PARFAIT GIRLS!"
    s "And we can rescue Sonic now! Hoorray!"
    show monika at thide zorder 1
    show natsuki at thide zorder 1
    show sayori at thide zorder 1
    hide natsuki
    hide sayori
    hide monika
    show emerald yellow at t11 zorder 2
    "SUDDENDLY, FROM THE WRECKAGE OF THE QUEEN ROBOT, THE YELLOW CHAOS EMERALD EMERGED!"
    $ persistent.emeraldCount += 1
    play sound Emerald_word
    "{i}You won a Chaos Emerald!\n(Click to continue...){/i}"
    "Now we have [persistent.emeraldCount] Chaos Emeralds!"
    "And the Emerald started to do something!"
    $ consolehistory = []
    call updateconsole("MILES ELECTRIC SYSTEM ONLINE", "User: Root.")
    pause 1.0
    call updateconsole("Searching: ????", "Searching...")
    pause 1.5
    call updateconsole("Searching: ????", "Data recovered! Downloading...")
    pause 1.5
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.3
    hide screen tear
    show mc2_glitch at t11 zorder 2
    call updateconsole("Data found!", "Reconstructing data...")
    pause 1.5
    show mc2_glitch at thide zorder 1
    hide mc2_glitch
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.3
    hide screen tear
    show mc2 1t at t11 zorder 2
    call updateconsole("Data found!", "Reconstructing data...")
    pause 1.5
    show mc2 1u at t11 zorder 2
    call updateconsole("Data found!", "DDLC's MC online!")
    pause 1.5
    mc2 1v "Oh boy, sure floating in space without a body is treepy!"
    mc2 1g "Wait... where am I? What happened to the Club Room?"
    s "MC!!!!!!!!!!!!!!!!"
    show sayori 1t at t21 zorder 3
    show mc2 1d at t22 zorder 2
    s "My love! You are here again! I don't know why, I don't understand, I wished so much for you..."
    mc2 1j "I'm here, Sayori, the one and only boyfriend of you!"
    mc2 1m "I'm so glad to see you here, alive and well."
    mc2 "I didn't got destroyed fully after the weird pink light shit that happened. I promised to take care of you and do what is best for you."
    mc2 1n "But tell me if I'm wrong, but this seems to be like one of Natsuki's Sonic games. Is this a virtual reality of sorts?"
    mc "I'm afraid this is not a virtual reality of sorts. This is the real deal."
    "The Chaos Emerald restored this guy, who seems to be called MC. What does MC mean? {i}Mint Chocolate{/i}? {i}Murdering Culprit{/i}? {i}Max the Coldsteel{/i}? {i}Mind Concussion{/i}?"
    "And he seems to be very closer to Sayori... wait, no, he's friends with all the girls too, since they started to reach both of them to greeting MC..."
    show emerald at thide zorder 1
    hide emerald
    show sayori at lhide zorder 1
    hide sayori
    show natsuki 5x at l21 zorder 3
    n "PUUUUUNK!!!! We believed you were dea... destroyed or something, since you didn't go to the Club meeting!"
    n 42f "PLEASE don't do that again!"
    mc2 1n "Sorry Natsuki! For some reason I spaced out at my home that day and forgot the Club meeting."
    mc2 1k "But I'm here now and I will not do something stupid again. I promised to take care and love Sayori forever."
    mc2 "And also remember I love you three, girls, you are my dear friends!"
    show natsuki at lhide zorder 1
    hide natsuki
    show monika 2n at l21 zorder 3
    m "Eeeeh... about that... I think you need some details to be explained, MC."
    show monika at thide zorder 1
    hide monika
    show mc2 at thide zorder 1
    hide mc2
    "Monika explained to MC what happened that day, the attack, and how I saved all the girls and now they are part of our Resistance."
    if persistent.yuriKnife == True:
        "And also Natsuki explained to everyone the strange things that happened after I saved Yuri, and why she doesn't be here with us."
    else:
        "But we were intrigued because Yuri was not with the group. Even Knuckles and Tails doesn't know where she is."
    "Tails then reminds us that we can search what of these prison cells is Sonic's one."
    show tails tails02 at t31 zorder 2
    show mc2 1f at t32 zorder 4
    show sayori 1k at t33 zorder 3
    "So we started to search in all the cells, but we started to only release the poor animals that would be converted into Badniks and robots..."
    mtp tails06 "SONIC HAS TO BE HERE, IN SOMEWHERE..."
    mtp "We were searching for hours, were did Eggman has him...?"
    mc2 "We must not surrender, we will find Sonic! I swear..."
    s "I'm not sure about that part... it has been two hours already! This prison seems extremely long to be hided in a chemical plant."
    show tails at lhide zorder 1
    hide tails
    show natsuki 2m at l31 zorder 2
    n "This is not the time to surrender guys! WE need to find Sonic... I don't know what I will do if something happens to him..."
    n 2o "So let's keep our eyes open and continue the search!"
    n 1v "We didn't defeated that stupid bee boss for nothing!!!"
    mc2 1h "Natsuki is right! Let's continue the search on the last floor! If Eggman is a competent villain, he sure left Sonic in the worst place to be founded..."

    pause 1.0
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("poem it\nRead\nyouceived\nre", Return(True), Return(True))
    if _return:
        call expression "poem_special_" + "special2"
        scene black with Dissolve(1.0)
    else:
        pass

    stop music fadeout 2.0
    scene bg chemicalPlant2
    with wipeleft_scene
    "So, we arrived to the last floor of the Egg Prison."
    "And suddendly, something was... no, someone was waiting for us there."
    play music metalDokis
    show boss2 metalMonika at h11 zorder 2
    mc "Monika?"
    n "MONIKA?"
    show tails tails07 at l21 zorder 2
    mtp "There's something weird with this Monika..."
    show tails at lhide zorder 1
    hide tails
    m "OK EVERYONE."
    m "IT'S. TIME TO-TO-TO-TO-TO-TO {i}DI-IIIIII-DIE{/i}."
    m "LET'S MAAAAA.KE A. DEATHLY. POEM OF SORTS."
    m "INK. FLOWS. INK. FLOWS. INK. FLOWS. INK. FLOWS."
    m "I'M THE. BEST. PRESIDENT. OF SORTS."
    m "SAYS. THE ANNOYING. STUPID BOSS OF. TH-TH-THE CLUB."
    m "TIME TO SHARE OUR PIECE OF SHITTY POEMS WITH THE CRYBABY, THE HORNY AND THE CUTE!"
    show boss2 at thide zorder 1
    hide boss2
    menu:
            m "WHOM. SHOULD. YOU. SHOW. YOUR SHITTY POEM TO?"
            "Crybaby":
                show boss2 metalMonika at face(y=600) with dissolve
                m "I'M THE CRYBABY SAYORI."
                m "I HAVE A LOT OF RAINCLOUDS!"
                m "MY LIFE IS SHITTY AS MYSELF."
                m "HAPPY THOUGHTS. HAPPY THOUGHTS. HAPPY THOUGHTS."
                m "KILL YOURSELF. BRING ON THE NOOSE."
                m "AND NO. I WILL NOT GIVE YOU MONEY FOR BREAKFAST. FUCK OFF."
            "Cute":
                show boss2 metalMonika at face(y=600) with dissolve
                m "I'M NATSUKI. I'M EXTREMELY CUTE."
                m "LOOK HOW UTTERLY CUTE I AM!"
                m "I'M A PRO ON BEING CUTE!!!!!"
                m "CUTE. CUTE. CUTE. CUTE. CUTE. CUTE."
                m "LET'S MAKE CUPCAKES WITH HAPPY FACES AND COLORFUL ICE."
                m "AND NO. MANGA IS NOT LITERATURE. FUCK OFF."
            "Horny":
                show boss2 metalMonika at face(y=600) with dissolve
                m "I'M MC. THE HORNY ONE."
                m "THE GIRLS THINK I LOVE LITERATURE, BUT NOOOOO!"
                m "I JUST WANNA GET LAAAAAIIIIIIIID."
                m "SEXUAL. SEXUAL. SEXUAL. SEXUAL. SEXUAL. SEXUAL."
                m "IF I DON'T GET LAID I PREFER TO BE ALONE AND BE FAT WATCHING HENTAI AND STUFF."
                m "AND NO. SAYORI I WILL NOT FUCK YOU. YOU ARE MORON. FUCK OFF."
            "Trashy":
                show boss2 metalMonika at face(y=600) with dissolve
                m "I'M MONIKA."
                m "I'M THE PRESIDENT OF THE FAILURE CLUB!"
                m "LOOK AT ME! I'M THE MOST POPULAR ONE! EVERY MAN WANTS TO GET LAID WITH ME!"
                m "EVERYTHING I DO IS UTTERLY AWESOME AS FUCK. THAT'S WHY I'M TRASHY!"
                m "IF YOU GIVE THE PRESIDENCY OF THE CLUB TO YURI, SURE IT WOULD WORK A LOT BETTER."
                m "YURI HAS MORE IMAGINATION THAN YOU. YOU ARE A MOTHERFUCKING RECYCLE BIN WITH LEGS. FUCK OFF."
    show boss2 metalMonika at t22 zorder 3
    show monika 3h at f21 zorder 2
    m "{i}Okay, seriously, this is the WORST form of flattery ever.{/i}"
    m 2h "Who the fucking heck are you?"
    m "Why you insist on using my patented phrase which I use to talk with the members of my club?"
    m "And that's the worst poem ever! Even MC writes better shit than that."
    show mc2 1o at l31 zorder 3
    mc2 "Thanks Monika, I love you too..."
    show mc2 at lhide zorder 1
    hide mc2
    m "And, most importantly, nobody insults my club members. Or me. So start speaking."
    show boss2 metalMonika at f22 zorder 3
    show monika 2h at t21 zorder 2
    m "M-M-M-M-MODEL. MK2-032A. METAL. MONIKA."
    mtp "METAL????? Like Metal Sonic????? Did Eggman build you????"
    m "WE. DON'T. SERVE. EGGMAN."
    m "WE. bzzzk. PROPERTY. OF THE. GLORIOUS. YURI EMPIRE. JUST YURI AND NO ONE ELSE."
    show boss2 metalMonika at t22 zorder 3
    show monika 1f at f21 zorder 2
    m "I can't believe this trash copy of me says that {i}Yuri{/i} built it..."
    y "WHAT? DID YOU NOT LOVE IT? IT'S AS TRASHY AS YOU!!!!"
    show boss2 metalMonika at t32 zorder 3
    show monika 1f at t31 zorder 2
    show yuri 3y3 at l33 zorder 4
    y "You can just call her \"Metal Trashy\", or something like that."
    y 3m "I learned to build her using some plans and data that Eggman left scrapped here!"
    y 3y7 "AND I MADE HER TO BE SO ANNOYING AS YOU, TRASHONIKA!"
    y "The only thing I'm not very satisfied is her poor logic to make insulting poetry. And the choice of music."
    m 2h "YOU. YOU ARE REALLY PISSING ME OFF."
    m "FIRST OF ALL: I DON'T FUCKING CARE ABOUT THE MUSIC. YOU CAN REPLACE IT WITH \"DESPACITO\" AND THIS ROBOT WILL STILL BE AS USELESS AS YOU."
    if persistent.packagedMusic == True:
        show honey djHoney at l31 zorder 5
        dj "OK... if you really wanna piss Yuri with that song..."
        dj "Seriously I don't know why the fucking hell people loves this song seriously wtf{nw}"
        play music jokePCKG
        y "WHAT THE FUCKING FUCK, FUCKING PIECE OF DJ! For fucks sake! Not that fucking piece of shit song!!!!"
        g "HEY! I'M THE ONE THAT SAYS THE INSULTS HERE!"
        dj "Now playing: {i}Despacito.{/i} Go to hell Yuri!"
        show honey at lhide zorder 1
        hide honey
        dj "They didn't payed me for playing this piece of shit that somebody called \"music\", goddamit!{nw}"
        m 4k "See, Yuri? That's a more fitting BGM for your shitty robots!"
        m "..."
        m 2h "Seriously, how can be people that love this shit?"
        y 3y3 "I told you! I told you! Motherfucking annoying music and now we can't stop it!"
        m "Ok, everyone! Let's resume the script and act like there is silence as BGM, ok? Ehem..."
    show yuri 3y7 at t33 zorder 4
    m "SECOND, I'M NOT TRASHY. I REDEEMED. YOU FORGIVED ME SOME DAYS AGO. AND I WILL NOT GIVE YOU THE VICE-PRESIDENT CHARGE."
    m "THIRD: MC AND SAYORI ARE ENGAGED. IF YOU ARE DOING THIS OUT OF JEALOUSLY, FUCK OFF."
    m "AND WHY THE HELL ARE YOU INTERRUMPTING OUR SEARCHING OF SONIC?"
    show yuri cuts3 at l33 zorder 4
    y "Because I... Urgh what's happening..."
    "Suddendly Yuri lost concience and..."
    stop music
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.3
    hide screen tear
    play music hb
    "Screen Tearing!"
    $ style.say_dialogue = style.edited
    y cuts6 "BECAUSE I DON'T WANT THAT YOU FIND SONIC AT ALL."
    $ style.say_dialogue = style.normal
    m 1l "What happened here? I got scared and a chill on my back all of a sudden..."
    show natsuki 3n at h41 zorder 2
    n "The fuck with the music...?"
    n 3m "Yuri...?"
    show natsuki at thide zorder 1
    hide natsuki
    "NO WAY! HER EYES! THAT IS THE COLOR OF THE PHANTOM RUBY, ACCORDING TO WHAT TAILS SAID TO US!"
    "AND SHE HAS MORE CUTS IN HER ARM!"
    m 1g "YURI! Are you still cutting yourself??? This is... just... not right..."
    mc "I KNEW YURI WAS BEING CONTROLLED!"
    $ style.say_dialogue = style.edited
    show monika 1g at t31 zorder 2
    y "CONGRATULATIONS. YOU SOLVED THE MYSTERY. I WILL GIVE YOU A COOKIE."
    if persistent.packagedMusic == True:
        y "AND I WILL SERIOUSLY KILL THE ASSHOLE THAT SUGGESTED \"DESPACITO\" AS A MINIBOSS BATTLE MUSIC!"
        y "Sorry, I wanted to say that. Ehem..."
    y "AND YES, SHE CUTS HERSELF. FOR ME."
    y "WITH EACH CUT, MY INFLUENCE ON HER IS STRONGER."
    y "BUT THOSE PESKY LOSERS, EGGMAN AND INFINITE, ARE ANNOYING!"
    y "IT SEEM'S THAT THEY CAN'T UNDERSTAND MY UNTAPPED POWER!"
    y "THEY ONLY ARE HAPPY CREATING ILLUSIONS AND LEGO BLOCKS. MORONS..."
    y "AND I TRULY DESPISE WORKING WITH HEROES. THAT MAKES ME SICK."
    y "BUT THIS GIRL!"
    y "THIS GIRL IS WONDERFUL."
    y "HER IMAGINATION... IS AMAZING! SHE IS LIKE AN OPEN, UNLIMITED AND UNTAMMED BOOK OF CREATIVITY."
    y "OH, THE THINGS WE WILL DO TO YOUR WORLDS WHEN SHE HAS ME ON HER CONTROL..."
    y "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA"
    $ style.say_dialogue = style.normal
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.3
    hide screen tear
    if persistent.packagedMusic == True:
        play music jokePCKG
    else:
        play music metalDokis
    y cuts3 "Urrgh... My head... what I was saying..."
    y cuts5 "OH YEAH! I WILL BUILD MY YURI EMPIRE STARTING NOW! Nobody can stop me!"
    show monika at thide zorder 1
    hide monika
    "Except that now, we know Yuri is not being herself most of the time! And that gives us valuable info."
    show natsuki 1v at h31 zorder 2
    n "STOP DOING THAT SHIT, YURI!"
    n 2f "You will not be the one who crosses on my way to know my hero!"
    if persistent.packagedMusic == True:
        n "AND WHY THIS WIMPY MUSIC IS STILL PLAYING?????????"
        y "I DON'T KNOW GODDAMIT! I WILL SUE LUIS FONSI AND DADDY YANKEE FOR DOING THIS ABERRATION!!!!"
        ny "LET'S. JUST. CONTINUE. THE. SCRIPT."
    y cuts2 "Oh, so you wanna fight. OK!"
    y cuts7 "Metal Monika, destroy that annoying obnoxius brat."
    show boss2 metalMonika at t22 zorder 3
    show natsuki 2i at t21 zorder 2
    show yuri at thide zorder 1
    hide yuri
    stop music fadeout 2.0
    "Suddendly, Yuri activated Metal Monika. The robot was prepared to attack Natsuki..."
    "AND THEN A BLUE BLUR DERIBBED YURI'S ROBOT!"
    show boss2 at thide zorder 1
    hide boss2
    play music sonicTheme
    show natsuki 1l at h22 zorder 3
    show sonic sonic01 at l21 zorder 2
    sth "This Egghead! Always building even more slower robots! This is not fun, is too easy!"
    sth sonic02 "And yes! I'm free! Sonic the Hedgehog is back into act..."
    show sonic sonic10 at h21 zorder 2
    show natsuki 1p at h22 zorder 3
    nsth "NO. FUCKING. WAY!"
    sth sonic02 "IT'S NATSUKI!!!! THE BEST POET GIRL ON THE UNIVERSE!!!!!"
    n 1z "IT'S SONIC! MY FAVOURITE RODENT!!!! MY DREAM IS NOW A REALITY!!!!!"
    show sonic sonic02 at h21 zorder 2
    show natsuki 1z at h22 zorder 3
    nsth "MANGA IS LITERATURE!!!!!!"
    $ style.say_dialogue = style.edited
    nsth "FUCKING MONIKAMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"
    $ style.say_dialogue = style.normal
    nsth "YOU'RE TOO SLOW!"
    nsth "SONIC'S MY NAME, SPEED IS MY GAME!"
    nsth "..."
    nsth "THIS IS AMAZING!!!!!"
    sth sonic12 "And you are here with Monika, Sayori and MC too! Outstandingly amazing!"
    show natsuki at thide zorder 1
    hide natsuki
    show monika 2k at h41 zorder 2
    show sayori 4r at h42 zorder 3
    show mc2 1k at h43 zorder 4
    show sonic sonic12 at t44 zorder 5
    m "We are so glad you are saved, mr. Sonic!"
    s "We did it, friends! Achievement Unlocked!"
    mc2 "It's a pleasure meeting you, mr. Sonic! We are glad we found you!"
    sth "The pleasure is mine, Doki-Dokis!"
    show monika at lhide zorder 1
    show sayori at lhide zorder 1
    show mc2 at lhide zorder 1
    hide mc2
    hide monika
    hide sayori
    show sonic sonic12 at t22 zorder 3
    show tails tails01 at t21 zorder 2
    mtp "SONIC! YOU ARE ALIVE! I WAS SO WORRIED ABOUT YOU!"
    mtp tails05 "I was so worried about you... Glad our team could find you here!"
    sth "TAILS! I'm fine! Smooth and suave as always, bro!"
    sth "And thanks for you too, Rookie. You and me will be good pals, bro. And specially for bringing Natsuki and the rest of the Dokis here!"
    sth sonic06 "But something is fishy here... there are {i}five{/i} Dokis, not four..."
    mtp tails03 "Oh no, Sonic, about that..."
    y "So, this is the Sonic everyone was talking..."
    show tails at thide zorder 1
    hide tails
    show yuri 3s at t21 zorder 2
    if persistent.packagedMusic == True:
        play music yuriRoutePCKG
        show honey djHoney at l31 zorder 5
        dj "Now, I'm contractually obligued by the Yuri Empire(TM) to play this song of her glorious Prime Leader, Yuri."
        dj "Her music of choice is called {i}Deadspace{/i}, from the DJ {i}Scary Noise{/i}"
        y "I hope you enjoy MY awesome EDM of choice. How could I know that you can find poetry, imagination and inspiration on electronic music?"
        dj "We don't know, Yuri, that's the magic of EDM I guess."
        show honey at lhide zorder 1
        hide honey
    else:
        play music yuriRoute
    y "Pleased to meet you! My name is Yuri, and I'm the fifth Doki you were missing."
    sth sonic07 "DON'T TRY TO FOOL ME, LADY. WE BOTH KNOW THAT THE GIRLS OF THE YANDERE TYPE ARE THE WORST, AND EVIL!"
    sth "I never liked you in Doki Doki Literature Club, I knew you were fishy from the start."
    sth "And you sent your filthy Eggman Robot to stop me. Also, you are emiting a very nasty aura."
    y 3y3 "So you noticed I'm the evil one here..."
    y cuts1 "THEN LET'S STOP THIS CHARADE! WE BOTH KNOW THAT YOU ARE BOTHERSOME!"
    sth "AND YOU ARE MORE EVIL THAN BALDY MC'NOSEHAIR. GET AWAY FROM MY FRIENDS AND YOUR EX-FRIENDS, YURI."
    y cuts5 "I WILL NOT RECEIVE ORDERS FROM YOU! IT'S TIME EVERYONE GO TO ANOTHER ZONE..."
    show rubypink zorder 5:
        alpha 0.0
        easein 4.0 alpha 0.5
    sth sonic09 "Oh no! Not that pink lighting again..."
    show sonic at thide zorder 1
    hide sonic
    show yuri at thide zorder 1
    hide yuri
    show monika 1f at h41 zorder 2
    show sayori 4p at h42 zorder 3
    show mc2 1v at h43 zorder 4
    show natsuki 1v at h44 zorder 4
    m "Watch out everyone!"
    s "MC! Don't let me go!!!!"
    mc2 "Take my hand Sayori! That way we will not be separated!"
    n "YURI YOU MOTHERFUCKING CHEATER!"
    mtp "Sonic!!!!"
    y cuts7 "GO AWAY, SLOWBROS!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.3
    hide screen tear
    play sound ruby

    pause 1.0
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    "You got 250 rings for ending Chapter 2!"
    "You got a bonus of 1000 rings for choosing Normal Route."
    "You got 500 rings for getting a Chaos Emerald!"
    "You got 1000 rings for saving Sonic!"
    play sound Ring
    $ persistent.ringCount += 2750
    "You now have [persistent.ringCount] Rings!\n{i}Click to continue...{/i}"
    call screen confirm("You have unlocked a special poem.\nWould you like to read it?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + "3" from _call_expression_45
        scene black with Dissolve(1.0)
    else:
        pass

    return