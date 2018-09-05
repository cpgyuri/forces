# This script contains the entirety of Yuri's Route to her Yuri Empire.

label yuriRoute1:
    scene bg tcGreenHill
    with dissolve_scene_full
    pause 3.0
    scene bg greenHill1
    with dissolve_scene_half
    play sound NegaRing
    $ persistent.yuriKnife = True
    y "As I promised, an important question first!"
    menu:
        y "Do you wanna play my glorious route with the EDM Session music?\n A demo song will play {i}AFTER{/i} you choose an option!"
        "Yes, my Queen!":
            $ persistent.packagedMusic = True
            $ dj_name = "DJ-NeoMetal"
            show neometal djNeo at l31 zorder 5
            dj "Surprise! It's me, Neo Metal Sonic!"
            dj "Reprogrammed to serve our glorious leader, Yuri. All hail Yuri!"
            dj "Unfortunately, instead of crushing biological life forms, I have to serve as resident DJ of electronical dance audio waveforms."
            play music greenHillPCKG
            dj "Now playing: {i}RIO - After the Love{/i}."
            dj "Routine MK-25A: Say a musical phrase - ACTIVATED. Crush your opposition with the rythm of the night."
            show neometal at lhide zorder 1
            hide neometal
            y "Thanks, DJ. And without further ado, let's start my route!"
        "No, my Lady":
            $ persistent.packagedMusic = False
            play music greenHillZ1
            y "Ok then, without further ado, let's start my route!"
    y "..."
    play sound NegaRing
    $ persistent.ringCount = -500000
    y "Oh yeah! You now will have NegaRings. Your ring count is now [persistent.ringCount] negarings!"
    y "..."
    y "From certain distance, I see those losers discussing about the mission to rescue Sonic."
    show knuckles knucklesCom at t33 zorder 2
    show monika 2c at t32 zorder 3
    show natsuki 1d at t31 zorder 4
    y "Rookie is preparing their Wispon after a conversation with Knuckles."
    y "Probably they will waste time making a poem. That must have been another of Monika's patented and stupid ideas."
    y "Knuckles is my favourite one from this universe: he is strong, very capable, he doesn't chuckle, and he is not coward."
    y "All the things I would have loved to be before meeting the Literature Club."
    y "And probably when he knows that he is my favourite, he will feel betrayed, like my friends."
    y "But now that's not a problem, because I WILL BE STRONGER."
    y "Don't feel sad, player, my friends will understand soon the sacrifices I have to do to following my dream."
    y "It's time to act!"
    y "And yes, this is MY route, I will be the one that narrates it! What did you expected, my love?"
    kte "So, did you selected the girl who will go to the mission?"
    m 2b "Oh yeah! Based on the results, and because she is so eager to go and meet him, we choosed Natsuki as our representant!"
    n 5y "I'm pro on this! I have expert knowledge of Sonic's world, this will be a blast!"
    mc "And with that, Captain, I think we are ready to go. I have my partner, they have the Extreme Gears, and Monika will command from here."
    kte "Excellent, then! Operation: Rescue is officially starting!"
    stop music
    y "How cute everyone looks, including that obnoxious brat!"
    show knuckles knucklesCom at h33 zorder 2
    show monika 1i at h32 zorder 3
    show natsuki 5f at h31 zorder 4
    y "Sad that I will have to ruin the fun now, it's... dissapointing, to say the least."
    kte "OH NO! Please don't tell me that is she..."
    show knuckles at thide zorder 1
    show monika at thide zorder 1
    show natsuki at thide zorder 1
    hide knuckles
    hide monika
    hide natsuki
    if persistent.packagedMusic == True:
        play music yuriRoutePCKG
        show neometal djNeo at l31 zorder 5
        dj "Now playing the glorious Prime Leader Yuri's song.'"
        dj "{i}Scary Noise - Deadspace{/i}. JUST YURI, the perfect biological life form!"
        y "YEEEEEEEEESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS..."
        show neometal at lhide zorder 1
        hide neometal
    else:
        play music yuriRoute
    show yuri 1y3 at t11 zorder 2
    y "SURPRISE! IT'S ME! THE FAVOURITE EDGY ONE! YOUR PREFERED YANDERE! THE ONE WHO IS THE MOST KNOWLEDGED OF THE CLUB! MISS GOOD LITERARY ADVICE."
    y 2y3"THE ONE WITH THE BIGGEST BOOB..."
    y 2y2 "..."
    y 4c "WAIT, NOT THAT, GODDAMIT SCRIPT!"
    $ style.say_dialogue = style.edited
    y 2y7 "FUCKING MONIKAMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"
    $ style.say_dialogue = style.normal
    show yuri 1y3 at t22 zorder 3
    show monika 5b at l21 zorder 2
    m "FOR THE LAST TIME, STOP STEALING MY CATCHPHRASES AND HACKED QUOTES!!!!"
    show yuri 1y3 at h22 zorder 3
    show monika 5b at t21 zorder 2
    y 1r "GO AWAY, YOU MOTHERFUCKING RECYCLE BIN WITH LEGS!"
    y 2y1 "NOBODY CARES ABOUT YOUR OPINION, GODDAMIT! YOU CAN'T EVEN STOP A FIGHT WITHOUT RESORTING TO HACKING EVERYONE AND EVERYTHING!"
    y "And no, the player doesn't love you, nobody does."
    y 2y3 "Follow FOR REAL the suggestion YOU forced me to say: {i}CONSIDER KILLING YOURSELF.{/i}"
    show yuri 1y3 at t22 zorder 3
    show monika 1p at h21 zorder 2
    m "Hey... that was mean..."
    show monika 1o at t21 zorder 2
    m "..."
    show monika at lhide zorder 1
    hide monika
    show yuri 3a at h11 zorder 2
    y "See? That's how you put Moronika in her place! Useless piece of presidential shit."
    y 3y7 "Ehem..."
    y 1y3 "What? Did I ruined your stupids plans and fun?"
    y "And don't worry about Delete-onika's feelings, she deserved it."
    show sayori 2j at t21 zorder 3
    show yuri 1y7 at t22 zorder 2
    s "Yuri! What is happening to you? You seem possessed!"
    s "AND NOBODY TREATS THE PRESIDENT OF THE CLUB BADLY!"
    y 2y7 "What is happening?"
    y 2y1 "I FEEL MORE ALIVE THAN EVER, LOSER-YORI"
    s 4j "OK YURI! WE ARE FRIENDS BUT YOU ARE ACTING WEIRD, AND NOW YOU WON A WELL DESERVED PUNCH IN YOUR FACE!"
    s "SAYOOOOOOORIIIIIIIIII PUNCH!"
    show sayori 4j at t31 zorder 4
    show ruby rubyProto at t32 zorder 3
    show yuri 1y3 at t33 zorder 2
    mc "NO WAY, YOU HAD THE PROTOTYPE RUBY PIECE ALL THIS TIME, YURI!"
    y "GO HANG YOURSELF WITH YOUR STUPID GIRLY PUNCHES! SAYO-NARA!"
    play sound ruby
    show sayori 4j at h31 zorder 4
    s 4p "NO WAY, WHAT IS HAPPENING???"
    show sayori at lhide zorder 1
    hide sayori
    s "AAAAAAAAAAAAAAAAAAAAAAAAAAAH!"
    show ruby rubyProto at t21 zorder 3
    show yuri 2y3 at t22 zorder 2
    y "If some other MORON wanna try something, think it twice."
    show ruby at thide zorder 3
    show yuri at thide zorder 2
    hide ruby
    hide yuri
    y "HOW CUTE, ROOKIE'S ASSHOLE FRIENDS DECIDED TO TELEPORT HERE BECAUSE I SHOWED MYSELF!"
    y "I COULDN'T EVEN CREATE SO PERFECT POETRY."
    show amy amy10 at t44 zorder 5
    show knuckles knuckles03 at t43 zorder 4
    show natsuki 5o at t42 zorder 3
    show tails tails07 at t41 zorder 2
    kte "I HAD ENOUGH WITH YOU, PURPLE SCHOLAR GIRL! YOUR MEDDLING WITH THE RESISTANCE ENDS HERE!"
    amyR "YOU WILL TEST THE POWER OF MY PIKO-PIKO HAMMER, RIGHT HERE AND RIGHT NOW!"
    mtp "You are a nuissance Yuri, I feel sorry for your friends, but you have to give us the Ruby prototype back!"
    n "YURI I DON'T KNOW WHAT THE HELL IS HAPPENING WITH YOU, I WILL SAVE YOU RIGHT NOW!"
    n "GIVE ME THAT SHINY ROCK, YOU WANNABE EDGY BITCH!"
    y "OK, COME HERE TO STEAL IT!"
    y "OH WAIT, YOU CAN'T, THE GRAVITY SCRIPT IS FAILING."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.3
    hide screen tear
    show rubypink zorder 6:
        alpha 0.0
        easein 4.0 alpha 0.5
    show amy amy08 at h44 zorder 5
    show knuckles knuckles02 at h43 zorder 4
    show natsuki 1m at h42 zorder 3
    show tails tails03 at h41 zorder 2
    mtp "Oh no, don't tell me..."
    amyR "Rookie, do something!"
    mc "MY WISPON IS JAMMED RIGHT NOW! I CAN'T DO ANYTHING!"
    kte "STUPID CHEAPER RUBY! FIGHT LIKE A MAN, STUPID SCHOOL TEENAGER!"
    n 1v "YURI WHY YOU ALWAYS USE CHEATS FOR EVERYTHING?"
    y "WHY ARE YOU ANGRY? I WILL SEND YOU ALL TO SAVE YOUR STUPID {i}RODENT{/i} FRIEND!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.3
    hide screen tear
    play sound ruby
    hide rubypink
    show amy at thide zorder 1
    show knuckles at thide zorder 1
    show natsuki at thide zorder 1
    show tails at thide zorder 1
    hide amy
    hide knuckles
    hide tails
    hide natsuki
    show yuri 2y3 at t11 zorder 2
    y "YES!"
    y 3y3 "Finally, they are gone!"
    y 3d "THEY WERE TOO SLOW!"
    y 1q "OMG my pun was horrible, let's focus Yuri..."
    y 3k "I sent them to Chemical Plant, since they were so eager to rescue that infamous Sonic."
    y 3y3 "AND I REALLY WANT TO FIGHT AND STAB HIM AND INFINITE AT THE SAME TIME!"
    y 1j "Now that I will not have distractions for a while..."
    y 1c "It's time to start with my master plan!"
    y 2b "You must be asking yourself what is that plan..."
    y 2c "Well, thanks for asking me, my love!"
    y "As I said, I will create the Yurism cult, and for that, we need to submit this planet to the Yuri Empire."
    y "My own special place where EVERYBODY WILL HAVE TO LOVE ME OR THEY WILL BE GUTTED!"
    y 2j "I started to investigate a little about this stupid planet."
    y 2l "It seems there is another person that has the same goal as me, and now he is succeding on it."
    show yuri 2r at t21 zorder 2
    show eggman eggman00 at h22 zorder 3
    y "That idiot is called Dr. Eggman!"
    y "He is constructing his glorius {i}Eggman Empire{/i} on this universe, and he seems to be the mortal enemy of Sonic and the idiots."
    y 1s "It seems that I learned something or two from Natsuki's stupid videogames."
    show eggman at thide zorder 1
    hide eggman
    show yuri 4e at t11 zorder 2
    y "Well, my love and fellow Yurist. I think you understand where I'm going now."
    y 2y5 "YES! We will going to Chemical Plant to pay a visit to the good doctor!"
    y 2y1 "I DON'T LIKE OTHER COMPETITORS ON MY WAY..."
    y "AND MAYBE I WILL ENCOUNTER SONIC AND SHOW HIM WHO I REALLY AM."
    y 3y3 "It's time to start purging this earth from the clutches of the Doctor's machinery!"
    y "And build my Yurism cult from the ruins of them!!!!"
    y "It's time for Sonic and friends to open their third eye..."
    y "AHAHAHAHAHAHAHAHAHAHAHA!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.3
    hide screen tear
    play sound ruby

    scene bg tcChemicalPlant
    with dissolve_scene_full
    pause 3.0
    scene bg chemicalPlant
    with dissolve_scene_full
    if persistent.packagedMusic == True:
        play music eggmanPCKG
        show neometal djNeo at l31 zorder 5
        dj "Now playing {i}Downfall{/i}, from the mobile game Crash Fever."
        y "I hope this time I can got Turing from the special FES ticket gacha! I wasted a lot of money buying polygons and only got 5 copies of Baldr in each pull..."
        y "AND NOW THEY ARE RELEASING THE HATSUNE MIKU CROSSOVER AGAIN???? YES, NOW I CAN GET MEGURINE LUKA AT LAST!!! AHAHAHAHA!"
        y "Wait! I'm rambling again!"
        show neometal at lhide zorder 1
        hide neometal
    else:
        play music eggmanMusic
    show eggman eggman01 at t22 zorder 3
    show infinite infinite3 at t21 zorder 2
    egg "NO WAY! I CAN'T BELIEVE THIS!"
    inf "So, it seems that you felt the same sensation as me, Doctor."
    egg eggman03 "That stupid Resistance found my secret special prison!"
    egg "We can't let them release Sonic. That would be a nuissance for my plans!"
    egg "I told you that you had to destroy Sonic at the best opportunity, Infinite!"
    inf "Sonic was weak. It's not my concern toying with weaklings."
    egg "YOUR CONCERN IS TO OBEY MY ORDERS, NOW WE HAVE TO DEAL WITH THOSE PESKY SONIC FRIENDS..."
    egg "AND WHO KNOW WHAT OTHER PROBLEMS..."
    y "May I interrupt this stupid conversation?"
    show eggman eggman04 at h22 zorder 3
    show infinite infinite2 at h21 zorder 2
    egg "WHO SAID THAT?"
    show yuri 3y3 at l31 zorder 2
    show eggman eggman07 at h33 zorder 3
    show infinite infinite3 at h32 zorder 4
    y "I WANTED TO KNOW YOU SINCE THE DESTRUCTION OF MY WORLD, DR. EGGMAN..."
    egg "Who the heck are you? How did you know about my secret base on my Chemical Plant?"
    inf "Doctor, I'm sensing the missing Ruby Prototype! She has it!"
    y 4d "Hey you two! That's not the correct way to treat a lady."
    y 1y1 "The correct way is to surrender yourselves to the Yuri Empire."
    egg eggman02 "YURI EMPIRE? It's official, the people of that Cuisine Club is crazy. HOOOOOOO HO HO HO!"
    y 2y7 "{i}LITERATURE{/i} club, ignorant piece of rotten egg."
    show eggman eggman06 at h33 zorder 3
    inf infinite2 "I'm afraid you can't insult my master, girl. What do you want?"
    inf "ANSWER OR PREPARE YOURSELF TO SUFFER INFINITE PAIN..."
    y 1y3 "What a good pun, how much time did you worked to think on that?"
    inf "ARE YOU FUCKING KIDDING ME?"
    y 1y1 "YES I'M FUCKING KIDDING YOU."
    y 1y5 "Now I want all the information about where your secret bases, stations, supply centers and Headquarters are positioned on this planet, Doctor."
    y 1d "I can't build a Yuri Empire with blood and passion and thrilling if I have to do all the hard man work."
    y 2y3 "I PREFER TO TAKE OVER ALL THE THINGS YOU BUILT."
    y "That is definitively more poetic and fascinating. And the correct way of treating a lady like me."
    egg eggman05 "HOW DARE YOU TO INSULT MY DREAMS OF EGGMANLAND AND MY EMPIRE, ELEMENTARY SCHOOL GIRL?"
    egg eggman03 "If you want to build your own bloody reign over this planet..."
    egg eggman02 "YOU WILL HAVE TO DEFEAT ME AND THAT PESKY BLUE RODENT FIRST! HOHOHOHOHOHOHOO..."
    show eggman at lhide zorder 1
    hide eggman
    show yuri 3y3 at t21 zorder 2
    show infinite infinite3 at t22 zorder 4
    egg "Infinite! Strategic retreat! We need to study this girl first!"
    inf "Your turn will come, Yuri. As the turn of Sonic and company and all the Resistance TO DIE."
    inf infinite2 "AND WHEN THAT TIME COMES, I WILL MAKE SURE TO KILL YOU QUICKLY, ARROGANT SCHOOLGIRL."
    show infinite at thide zorder 1
    hide infinite
    show yuri 1j at t11 zorder 2
    y "Yeah yeah, whatever. Bunch of cowards."
    y "I will investigate the info I need from the computers of this disorganized place that Eggman abandoned here."
    y 2m "And damn it, I couldn't have fun with my rivals."
    y 3y3 "It's time to search for Sonic and have fun with those obnoxious morons then!"

    scene bg chemicalPlant2
    with wipeleft_scene
    stop music fadeout 2.0
    y "And so, after I discovered where the prison cells were, I travelled to the location."
    y "I managed to find some files that indicated information about projects of robots, Infinite's data, and a new base of operations that Eggman will build on a planet that orbits this planet from time to time."
    y "According to the files, that is the legendary Little Planet, the place where you can control the flow of time using speed."
    y "That could be useful for me. Let's save these important info."
    y "The exit door and Sonic's special prison cell where on a long road parked on a platform, which floated on a giant river of blue chemicals."
    y "Suddendly, when I reached the plataform, the alarms of the place go hairwire!"
    "Attention! Intruder Alert! Intruder Alert! All Security Systes Online!"
    egg "YOU WILL NOT RELEASE ANYONE, GIRL WITH PURPLE HAIR!"
    egg "IF YOU WANT MY EMPIRE SO BADLY, START SHOWING YOUR EVILNESS FIRST!"
    play music bossQueen
    show boss1 queenBomber at t11 zorder 2
    y "Indeed, from the river of chemical compounds emerged a robot of considerable size, autonomous, capable of creating a force field of liquid."
    y "It was the Queen Buzz Bomber!"
    y "And, as always, the team of assholes come to this place too..."
    show boss1 at thide zorder 1
    hide boss1
    show monika 5b at t31 zorder 2
    m "I can't seem to hack you, but Rookie and I will sure beat you, ugly bee!"
    show natsuki 5o at t32 zorder 2
    n "THIS IS FOR SONIC, YOU UGLY BITCH! PREPARE TO BE SMACKED DOWN!"
    show sayori 4p at t33 zorder 2
    s 4j "Hey you, ugly bee! Do you want to share happy thoughts with me????"
    m 2h "Wait girls and Rookie! We are not alone here!"
    m "What are you doing here, ex-friend?"
    show monika 2h at t21 zorder 2
    show yuri 3y7 at l22 zorder 2
    show sayori at thide zorder 1
    show natsuki at thide zorder 1
    hide sayori
    hide natsuki
    y "GO AWAY ALL OF YOU!"
    y "I made a barrier force appear in front of Rookie and the girls, so that way they not disturb my plans."
    y 3y3 "I WILL SHOW TO EVERYONE AND THIS STUPID ROBOT THE POWER OF THE YURI EMPIRE!"
    y 2y7 "TRY TO INTERVENE AND I WILL STAB YOUR PRECIOUS SONIC WITH MY KNIFE!"
    m 2p "What are you saying Yuri? We are your friends! We must work together to..."
    y "I SAID GO AWAY, RECYCLE BIN WITH LEGS!"
    m 2q "Jeez! Fine, fine! But don't you dare to do something to Sonic."
    m 2h "If this is what you want, fine, Yuri. I will not intervene."
    m "But let's make it clear that I didn't hack your personality. This is your own fucking psycho idea."
    m "And I hope that it fails, for the sake of our world and this world."
    show boss1 queenBomber at t21 zorder 3
    show monika at thide zorder 1
    hide monika
    y 1y3 "And so, MY battle has begun!"
    y cuts1 "But don't worry! I will not do the hard work!"
    y cuts2 "True leaders always make other people to get their hands dirty instead."
    y "So, let's not make this boss and the annoying Resistance wait! I present to you..."
    show yuri at thide zorder 1
    hide yuri
    show boss2 metalMonika at t22 zorder 3
    stop music fadeout 2.0
    y "MY NEWEST CREATION: METAL PRESIDENT TRASHBAG!"
    m "M-M-M-M-MODEL. MK2-032A. METAL. MONIKA."
    m "WE. bzzzk. PROPERTY. OF THE. GLORIOUS. YURI EMPIRE. JUST YURI AND NO ONE ELSE."
    show boss1 at thide zorder 1
    hide boss1
    show boss2 metalMonika at t32 zorder 3
    show yuri cuts2 at t33 zorder 4
    show monika 1f at t31 zorder 5
    m "{i}Okay, seriously, this is the WORST form of flattery ever.{/i}"
    m "I can't believe this trash copy of me says that {i}you{/i} built it..."
    y "WHAT? DID YOU DON'T LOVED IT? IT'S AS TRASHY AS YOU!!!!"
    y "You can just call her \"Metal Trashy\", or something like that."
    y 3m "I learned to build her using some plans and data that Eggman left scrapped here!"
    y 3y7 "AND I MADE HER TO BE SO ANNOYING AS YOU, TRASHONIKA!"
    y cuts5 "But wait, where is the music for my precious Trashonika robot????"
    show neometal djNeo at l31 zorder 5
    play music jokePCKG
    y "WHAT THE FUCKING FUCK, FUCKING PIECE OF DJ! For fucks sake! Not that fucking piece of shit song IN MY GLORIOUS ROUTE!!!!"
    dj "Now playing: {i}Despacito.{/i} That's what the script says. Do your complaints to the mod's author."
    show neometal at lhide zorder 1
    hide neometal
    m 4k "Hahahahaha! Even your fucking servants doesn't obey you fully!"
    m "..."
    m 1f "OK, yeah. You win on this, Yuri. I don't understand why are people that {i}like{/i} this shit."
    y "AND THIS SHIT WON GRAMMYS TOO! GRAMMYS! WHAT THE FUCK!"
    y "URRRRRRGH! Ok, Metal Monika, destroy the boss. And let's imagine we are listening silence!"
    show yuri at thide zorder 1
    hide yuri
    show monika at thide zorder 1
    hide monika
    show boss1 queenBomber at t21 zorder 3
    show boss2 metalMonika at t22 zorder 5
    y "And so, my robot will trash this stupid barrier that Eggman left here. First this bee, then Sonic."
    y "But because this is the demo, assume that, as always, we won."
    show boss1 at thide zorder 1
    hide boss1
    show yuri cuts7 at l21 zorder 5
    y "GOOD JOB, MY PRECIOUS TRASHY ROBOT!"
    y 2m "Now let's go to search for that pesky rodent before those assholes do it."
    y "And made the barrier force dissapear only when we are far, far away from them."

    scene bg chemicalPlant2
    with wipeleft_scene
    stop music fadeout 2.0
    show sonic sonic07 at l33 zorder 4
    sth "Man, something doesn't feel alright."
    sth "The doors were open without any kind of input, but nobody was there for rescuing me, or sending me to listen another of Eggman's stupid monologues..."
    sth "It's better that I keep running and get the hell out of here!"
    show boss2 metalMonika at l32 zorder 5
    show yuri cuts7 at l31 zorder 5
    if persistent.packagedMusic == True:
        play music yuriRoutePCKG
    else:
        play music yuriRoute
    m "WE. FOUND THE. PESKY RODENT."
    m "YOU WILL NOT. GET AWAY FROM. US. SONIC THE HEDGEHOG!"
    y "Where do you think you are going, Sonic?"
    y 3y5 "You have to meet ME and my Metal Robot too, first!"
    sth sonic10 "NO WAY! SHE IS YURI, THE GIRL FROM THE VISUAL NOVEL WE PLAYED BEFORE!"
    sth sonic11 "And you built a Metal Monika, like that trash copy of me called Metal Sonic?"
    sth sonic07 "WAIT A SECOND, IF YOU BUILT A ROBOT AND YOU ARE HERE TO STOP ME, THAT MEANS YOU ARE MY ENEMY!"
    sth "LIKE IN THE VISUAL NOVEL! ALL YANDERES ARE EQUAL!"
    sth "STAY AWAY FROM MY PATH, YURI. YOU HAVE A REALLY NASTY AURA, AND I DON'T WANT TO FIGHT YOU... FOR NOW."
    y cuts5 "HOW DARE YOU, SONIC THE HEDGEHOG!"
    y "NASTY HEROES, ALWAYS BELIEVING THEY ARE NOBLE AND THE GOOD SIDE OF THE FORCE!"
    y "SO, YOUR SOUR ATTITUDE MEANS THAT YOU WILL NOT JOIN MY GLORIOUS YURI EMPIRE THEN..."
    sth "I will never join anything that threatens my world and my friends. Now stay away from me!"
    show rubypink zorder 5:
        alpha 0.0
        easein 4.0 alpha 0.5
    sth sonic09 "Oh no, not that pink light again! Do you have control of the Phantom Ruby too?"
    y cuts7 "I don't have to give you any explanation, blue blur."
    y "So this is our Good bye for now, Sonic the Hedgehog!"
    y "And don't worry, I will send your friends to the place I will send you, so you don't feel lonely!"
    y cuts1 "I grant you your claim in its entirety: you are released from this prison and free of all charges. I say it, CASE CLOSED! {i}(smash the jury's hammer in the table){/i}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.3
    hide screen tear
    play sound ruby

    scene bg tcStudiopolis
    with dissolve_scene_full
    pause 3.0
    scene bg studiopolis
    with dissolve_scene_half
    if persistent.packagedMusic == True:
        play music studioPCKG1
        show neometal djNeo at l31 zorder 5
        dj "Now playing: {i}Planet Funk - Lemonade{/i}, Benny Benassi's remix. We are more closer to our objective!"
        y "And our objective will be completed, the Resistance crushed and Eggman sabotaged."
        show neometal at lhide zorder 1
        hide neometal
    else:
        play music studioP1
    play sound NegaRing
    $ style.say_dialogue = style.edited
    "There is no turning back now."
    "I WILL MAKE SURE the Yuri Empire start..."
    "{i}...Thanks for your help. Continue doing that.{/i}"
    $ style.say_dialogue = style.normal
    show yuri 3s at t21 zorder 2
    y "Awwww. This place brings me memories!"
    y "We where here in Studiopolis already."
    y 3i "But is not the time to remember that, since after I build my Empire, I will visit this place every single day."
    y 3y3 "I SENSE THAT INFINITE IS HERE. TIME TO SHOW HIM WHO IS THE BOSS!"

    call DEMO from _call_DEMO


    

    
    #Call exclusive scene
    $ nextscene = poemwinner[1] + "_exclusive_" + str(eval(poemwinner[1][0] + "_appeal"))
    call expression nextscene from _call_expression_26

    #After exclusive scene, we go back to poem responses

    return


label ch2_end:
    stop music fadeout 1.0
    scene bg club_day
    show monika 4b at t32 zorder 2
    with wipeleft_scene
    play music t3
    m "Okay, everyone!"
    m "We're all done reading each other's poems, right?"
    m "I have something extra planned today, so if everyone could come sit at the front of the room..."
    show natsuki 3c at f31 zorder 3
    n "Is this about the festival?"
    show natsuki at t31 zorder 2
    show monika 1j at f32 zorder 3
    m "Well, sort of~"
    show monika 1a at t32 zorder 2
    show natsuki 1m at f31 zorder 3
    n "Ugh. Do we really have to do something for the festival?"
    n "It's not like we can put together anything good in just a few days."
    n "We'll just end up embarrassing ourselves instead of getting any new members."
    show yuri 2g at f33 zorder 3
    show natsuki at t31 zorder 2
    y "That's a concern of mine as well."
    y "I don't really do well with last-minute preparations..."
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 1b "Don't worry so much!"
    m "We're going to keep it simple, okay?"
    m 1a "We won't need much more than a few decorations."
    m "Sayori has been working on posters, and I've designed some pamphlets we can give out during the event."
    show monika at t32 zorder 2
    show natsuki 3c at f31 zorder 3
    n "Okay, that's great and all..."
    n "But that doesn't tell us what we're actually going to be doing for the event."
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 1d "Ah, sorry! I thought you heard about it already."
    m 1b "We're going to be performing!"
    show monika at t32 zorder 2
    show natsuki at f31 zorder 3
    n 3h "Performing?"
    show natsuki at t31 zorder 2
    show yuri at f33 zorder 3
    y 3n "P..."
    y 3o "Um, Monika..."
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 1k "Yeah! We're going to be having a poetry performance."
    m 1b "Each of us are going to choose a poem to recite during the event."
    m "But the cool part is, we're also going to let anyone else come up and recite poems too!"
    m 1a "Sayori's putting it on all the posters in case anyone wants to prepare ahead of time."
    show yuri at t44 zorder 2
    show monika at t43 zorder 2
    show natsuki at t42 zorder 2
    show sayori 4q at l41
    s "Ehehe~"
    "Sayori, who's been coloring a poster, holds it up for us to see."
    show natsuki 4w at f42 zorder 3
    n "Are you kidding me, Monika?"
    n "You didn't...you didn't already start putting those posters up, did you?"
    show natsuki at t42 zorder 2
    show monika at f43 zorder 3
    m 1d "Eh? Well, I did..."
    m "Do you really think it's that bad of an idea...?"
    show monika at t43 zorder 2
    show natsuki 1s at f42 zorder 3
    n "Well, no."
    n "It's not a bad idea."
    n 1w "But I didn't sign up for this, you know!"
    n 1x "There is {i}no{/i} way I'm going to be performing in front of a group of people like that!"
    show natsuki at t42 zorder 2
    show yuri at f44 zorder 3
    y 3r "I...I agree with Natsuki!"
    y 3w "I could never...in my life...do something like that..."
    "Imagining it, Yuri shakes her head in fear."
    show yuri at t44 zorder 2
    show sayori 1g at f41 zorder 3
    s "Guys..."
    show sayori at t41 zorder 2
    show monika at f43 zorder 3
    m 1g "No, Sayori..."
    m "I understand where they're coming from."
    m "Remember that Natsuki and Yuri have never shared their poems with anyone until just a couple days ago..."
    m "It's a lot to ask for them to recite their poems out loud to a whole room full of people."
    m 1r "I guess I kind of overlooked that."
    m "So, I'm sorry."
    show monika at t43 zorder 2
    show natsuki 5g at f42 zorder 3
    n "..."
    show natsuki at t42 zorder 2
    show monika at f43 zorder 3
    m 1i "...But!"
    m "I still think we should give it our best!"
    m 1d "We're the only ones responsible for the fate of this club."
    m "If we start the event and each put on a good performance..."
    m 3a "Then it will inspire others to do the same!"
    m "And the more people who perform, the better we'll be able to show everyone what literature is all about!"
    show monika at t43 zorder 2
    show sayori 1r at f41 zorder 3
    s "Yeah!"
    s 1x "It's about expressing your feelings..."
    s "Being intimate with yourself..."
    s "Finding new horizons..."
    s "And having fun!"
    show sayori at t41 zorder 2
    show monika at f43 zorder 3
    m 4b "That's right!"
    m "And it's those reasons that we're all in this club today."
    m 4e "Don't you want to share that with others?"
    m "To inspire them to find the same feelings that brought you here in the first place?"
    m 1e "I know you do."
    m "I know we all do."
    m 1b "And if all it takes is standing in front of the room for two minutes and reciting a poem..."
    m "...Then I know you can do it!"
    show monika 1a at t43 zorder 2
    show natsuki 5s at f42 zorder 3
    n "..."
    show natsuki at t42 zorder 2
    show yuri 4b at f44 zorder 3
    y "..."
    show yuri at t44 zorder 2
    show sayori 1g
    "Natsuki and Yuri remain silent."
    "Sayori looks worried."
    "I guess that leaves me no choice..."
    mc "I agree..."
    mc "I don't think it's too much to ask."
    mc "I think that Sayori and Monika have been trying really hard to get new members."
    mc "The least we can do is help them out a little bit."
    show natsuki at f42 zorder 3
    n 5h "Well...maybe, but..."
    n "..."
    "It looks like Natsuki doesn't have any arguments left."
    n "Uu..."
    n 1q "...Okay, fine!"
    n "I guess I'll just have to get it over with."
    show natsuki at t42 zorder 2
    show sayori at f41 zorder 3
    s 4r "Alright~!"
    show sayori 4a at t41 zorder 2
    show monika at f43 zorder 3
    m 1e "Phew..."
    m "Thanks, Natsuki."
    m "What about you, Yuri...?"
    show monika at t43 zorder 2
    show yuri at f44 zorder 3
    y "..."
    "Yuri dejectedly glances around at everyone else's expectant faces."
    y "Sigh..."
    y "I-I guess I don't really have a choice..."
    show yuri at t44 zorder 2
    show sayori at f41 zorder 3
    s 4r "Ahaha! That's everyone!"
    s "You're the best, Yuri~"
    show sayori 4a at t41 zorder 2
    show yuri at f44 zorder 3
    y "This club is seriously going to be the death of me..."
    show yuri at t44 zorder 2
    show monika at f43 zorder 3
    m 1l "Oh gosh..."
    m 1n "You'll be fine, Yuri."
    m "But anyway..."
    m 1b "Let's move onto the main event!"
    m "I want each of you to choose a poem of yours."
    m "We're going to practice reciting them in front of each other."
    show monika 1a at t43 zorder 2
    show natsuki at f42 zorder 3
    n 1p "N-N-No way!!"
    show natsuki at t42 zorder 2
    show yuri 3n at f44 zorder 3
    y "Monika...!"
    y "This is too sudden...!"
    show yuri at t44 zorder 2
    show monika at f43 zorder 3
    m 2a "Well, if you can't recite your poem in front of the club, how do you expect to do it in front of strangers?"
    show monika at t43 zorder 2
    show yuri 4c at f44 zorder 3
    show natsuki 1o
    y "Oh no..."
    show yuri at t44 zorder 2
    show monika at f43 zorder 3
    m 2a "Don't worry."
    m "I'll start off to help everyone feel a little more comfortable."
    show monika at t43 zorder 2
    show sayori 1r at f41 zorder 3
    s "Can I go next??"
    show sayori at t41 zorder 2
    show monika at f43 zorder 3
    m "Ahaha. Of course."
    m 2d "Now, let's see..."
    "Monika flips through her notebook to the specific poem she has in mind for herself."
    "She then stands behind the podium."
    show monika at t11 zorder 2
    show sayori at thide zorder 1
    show natsuki at thide zorder 1
    show yuri at thide zorder 1
    hide sayori
    hide natsuki
    hide yuri
    m 1a "The title of this poem is {i}The Way They Fly{/i}."
    m 1r "Ahem..."
    show monika 1a
    "Monika begins reciting her poem."
    "Her clear, confident voice fills the room."
    "More than that, her inflection is pristine."
    "She knows exactly how to apply emotion behind each line she recites, bringing the words to life."
    "Is this something she's done before, or is she simply a natural?"
    "I glance around me."
    "Everyone has their eyes on Monika."
    "Sayori looks amazed."
    "Yuri has an intense expression on her face that I don't understand."
    show monika 1j
    "Finally, Monika finishes the recitation."
    "The four of us applaud."
    "Monika takes a breath and smiles."
    show monika 1a
    show sayori 4m at f33 zorder 3
    s "That...that was so good, Monika!"
    show sayori at t33 zorder 2
    show monika at f32 zorder 3
    m 1j "Ahaha, thank you very much."
    m 1a "I was just hoping to set a good example."
    m "Are you ready to go next, Sayori?"
    show monika at t32 zorder 2
    show yuri 2r at l31
    y "I...I'll go next!!"
    show sayori at h33
    s 1n "Uwah! Yuri's fired up all of a sudden!"
    "Yuri clutches a sheet of paper between her hands and stands up."
    "Keeping her head down, she walks quickly over to the podium."
    show monika at thide zorder 1
    show sayori at thide zorder 1
    show yuri at t11 zorder 2
    hide monika
    hide sayori
    y 2v "This poem is called--!"
    "Yuri anxiously glances at each of us."
    s "You can do it, Yuri..."
    y "It...It's called...{i}Afterimage of a Crimson Eye{/i}."
    "Yuri's voice shakes as she starts reading the poem."
    "Just a moment ago, she practically refused to do this."
    "Why is she suddenly putting in so much effort?"
    show yuri 2l
    "As Yuri gets past the first couple of lines, her voice changes."
    "It's almost like what happens when Yuri gets absorbed into her books."
    "Her quivering words transform into the sharp syllables of a fierce and confident woman."
    "The poem is full of twists and turns in its structure that she enunciates with perfect timing."
    "This must be a rare glimpse into the whirling fire Yuri keeps concealed inside her head...!"
    show yuri 2t
    "Suddenly, she's finished."
    "Everyone is stunned."
    "Yuri snaps back into reality and glances around her, as if she bewildered even herself."
    y 3o "I..."
    "...It's up to me to save this situation."
    "I'm the first to start applauding."
    "Everyone joins me afterward, and we give Yuri the recognition she deserves."
    "It's not that we didn't want to applaud for her."
    "But we were caught so off-guard that we must have forgotten."
    "As we applaud, Yuri holds the poem to her chest and rushes back into her seat."
    show yuri at lhide
    hide yuri
    show monika 1a at t11 zorder 2
    m "Yuri, that was really good."
    m "Thank you for sharing."
    y "..."
    "Looks like Yuri is down for the count..."
    show sayori 1q at t31 zorder 2
    s "Okaay~"
    s "I guess I'm next, then!"
    "Sayori hops out of her chair and cheerfully walks to the podium."
    show sayori at t11 zorder 2
    show monika at thide zorder 1
    hide monika
    s 1x "This one's called...{i}My Meadow{/i}."
    s "Ah..."
    s 1s "...Ahaha!"
    s 4s "Sorry, I giggled..."
    s 4q "Ehehe..."
    mc "Sayori..."
    s 1l "It's a lot harder than I thought!"
    s "How did you guys do it so easily?"
    show monika 3a at t31 zorder 2
    show sayori 1b
    m "Ah..."
    m "Try not to think of it like you're reciting to other people."
    m "Imagine you're reciting it to yourself, like in front of a mirror, or in your own head."
    m "It's your poem, so it'll come out the best that way."
    show sayori 1i
    s "I see, I see..."
    s "Okay, then..."
    show monika at thide zorder 1
    hide monika
    show sayori 1c
    "Sayori begins her poem."
    "Somehow, it feels like her soft voice was made as a perfect match."
    "The poem isn't aimlessly cheery like Sayori is."
    "It's serene and bittersweet."
    "If I were to read this on paper, I probably wouldn't think much of it..."
    "But hearing it come from Sayori's voice almost gives it a whole new meaning."
    "Maybe this is what Sayori meant when she said she likes my poems."
    "It's like I get to reach more deeply into someone I thought I knew through and through."
    "Sayori finishes, and we applaud."
    s 3q "I did it~!"
    mc "Good job, Sayori."
    s "Ehehe, even [player] liked it."
    s "I guess that's a good sign~"
    mc "What does that even mean...?"
    show monika 2b at f31 zorder 3
    m "It came out nicely, Sayori."
    m "The atmosphere of the poem fits you really nicely."
    m "But it might be that other poems wouldn't work quite as well with that kind of delivery..."
    show monika at t31 zorder 2
    show sayori at f32 zorder 3
    s 1g "Eh? I don't really understand..."
    show sayori at t32 zorder 2
    show monika at f31 zorder 3
    m 1a "In other words, I've seen poems of yours where that sort of gentle delivery wouldn't work as well."
    m "They might need a little more force behind them, depending on what you're reading..."
    show monika at t31 zorder 2
    show sayori at f32 zorder 3
    s 1x "Oh, I know what you mean!"
    s "That's...well, I've been practicing that kind of thing..."
    s 5 "It's just embarrassing to do in front of everyone..."
    s "Ehehe..."
    show sayori at t32 zorder 2
    show monika at f31 zorder 3
    m 4a "Then next time, I'm going to make you pick a poem that challenges you a little more."
    m "We don't have much time before the festival, you know?"
    show monika at t31 zorder 2
    show sayori at f32 zorder 3
    s 1q "Okaaaaay."
    show sayori at t32 zorder 2
    show monika at f31 zorder 3
    m 1a "Now, who's next...?"
    m "Natsuki?"
    show natsuki 5s at f33 zorder 3
    show monika at t31 zorder 2
    n "Hmph."
    n "Don't make me go before [player]."
    n "It's not like I can compare to you guys, anyway..."
    n "Might as well let [player] lower everyone's standards a little before I have to do it."
    show natsuki at t33 zorder 2
    show sayori at f32 zorder 3
    s 1g "Natsuki..."
    show sayori at t32 zorder 2
    mc "It's fine, it's fine."
    mc "I might as well get it over with."
    mc "But it's not like I have much of a selection of what to read..."
    mc "I'll just have to go with what I wrote for today."
    "I stand up and step in front of the podium."
    show natsuki 2c at t44 zorder 2
    show sayori 1a at t43 zorder 2
    show monika 1a at t42 zorder 2
    show yuri 1e at t41 zorder 2
    "Everyone has their eyes on me, making me feel terribly awkward."
    "I recite my poem."
    "Since I'm not exactly confident in my own writing, it's hard to put energy into it."
    "Despite that, once I finish, I receive applause anyway."
    mc "Sorry I'm not really as good as everyone else..."
    show monika at f42 zorder 3
    m 1a "Don't worry about it so much."
    m "I think it's less about your abilities, and more about your lack of confidence in your writing."
    m "That's something that'll improve over time, though."
    show monika at t42 zorder 2
    mc "Yeah... Maybe."
    show monika at f42 zorder 3
    m 1j "Alright, then!"
    m 1a "That just leaves you, Natsuki."
    show monika at t42 zorder 2
    show natsuki at f44 zorder 3
    n 2g "Yeah, yeah."
    n "I'm going."
    "Natsuki begrudgingly gets out of her seat and makes her way to the podium."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    show yuri at thide zorder 1
    show natsuki at t11 zorder 2
    hide sayori
    hide monika
    hide yuri
    n 2c "The poem is called..."
    n 2q "It's called..."
    n 1x "W-Why are you all looking at me?!"
    m "Because you're presenting..."
    n 2x "Hmph..."
    n 2h "Anyway...the poem is called {i}Jump{/i}."
    "Natsuki takes a breath."
    show natsuki 2c
    "Once she starts reciting the poem, her sour attitude disappears a little."
    "While she's still a little unenthused, her poem has a rhythm and rhyme to it."
    "It's Natsuki's trademark style, and it works surprisingly well when spoken aloud."
    "The words feel like they bounce up and down, as if giving life to the poem."
    show natsuki 2s
    "Natsuki finishes, and everyone applauds."
    "She huffs back to her seat."
    show monika 2a at f31 zorder 3
    m "That wasn't so bad, was it?"
    show monika at t31 zorder 2
    show natsuki 5w at f32 zorder 3
    n "Easy for you to say..."
    n "You'd better not make me do that again."
    show natsuki at t32 zorder 2
    show monika 1d at f31 zorder 3
    m "Ah, well..."
    m "Do you at least feel prepared enough to recite a poem in front of other people?"
    show monika at t31 zorder 2
    show natsuki 2c at f32 zorder 3
    n "I mean, doing it in front of other people will be way easier!"
    n "I can put on whatever face I want for other people."
    n 2q "But when it's just my friends..."
    n "It's just...embarrassing."
    show natsuki at t32 zorder 2
    show sayori 1b at f33 zorder 3
    s "That's a surprise, Natsuki..."
    s "I think it would be the other way around for me."
    show sayori at t33 zorder 2
    show natsuki at f32 zorder 3
    n "Well, that's just how it is, so..."
    show natsuki at t32 zorder 2
    show monika at f31 zorder 3
    m 1a "Well, I guess in that case..."
    m "You won't have much to worry about for the festival."
    m 2b "That said, I want to thank everyone for coming through."
    m "It might be hard, but I hope that you all have an idea of what it's like now."
    m 4b "Make sure you pick a poem and get enough practice before the festival, okay?"
    m "I'll be making pamphlets, so let me know ahead of time what you'll be reciting."
    show monika at t31 zorder 2
    mc "Jeez..."
    mc "I should probably find some other poem to recite instead."
    show monika at f31 zorder 3
    m 1j "That's fine, too!"
    m 1a "It doesn't have to be your own."
    m "I'm already pleasantly surprised that you're putting in all this effort for the club."
    m 5 "It makes me really happy."
    show monika at t31 zorder 2
    mc "Ah... Yeah, no problem..."
    play music t8 fadeout 1.0
    show monika at t11 zorder 2
    show sayori at thide zorder 1
    show natsuki at thide zorder 1
    hide sayori
    hide natsuki
    m 4b "Okay, everyone!"
    m "I think that's about it for today."
    m "I know the festival is coming up, but let's try to write poems for tomorrow, as well."
    m "It's been working out really nicely so far, so I'd like to continue that."
    m "As for the festival, we'll finish planning tomorrow, and then we'll have the weekend to prepare."
    m "Monday's the big day!"
    show sayori 4r at t31 zorder 2
    s "I can't wait~!"
    show yuri 4b at t33 zorder 2
    y "I can do this... I can do this..."
    mc "Alright--"
    hide sayori
    hide monika
    hide yuri
    with wipeleft
    "I stand up."
    "There's no way I'll be able to find the same enthusiasm as Sayori and Monika, but I'll do my best to get through it."
    "If it's for the sake of the club..."
    "And impressing Monika..."
    "Then I'll have to do my best."
    show sayori 1a at t32 zorder 2
    mc "Ready to go, Sayori?"
    show sayori at h32
    s 1x "Yep!"
    show natsuki 2d at f33 zorder 3
    n "Look at you two, always going home together like that."
    show monika 5 at f31 zorder 3
    show natsuki at t33 zorder 2
    m "It's kind of adorable, isn't it?"
    show monika at t31 zorder 2
    show sayori at f32 zorder 3
    s 1q "Ehehe~"
    show sayori at t32 zorder 2
    mc "Jeez, guys..."
    mc "Don't make such a big deal out of it."
    show natsuki at t44 zorder 2
    show sayori at t43 zorder 2
    show monika at t42 zorder 2
    show yuri 1u at f41 zorder 3
    y "It must be a little nice, though..."
    show yuri at t41 zorder 2
    mc "Well..."
    mc "Ah..."
    "How am I supposed to respond to that?"
    show sayori at f43 zorder 3
    s 1d "It's okay, [player], you don't have to say it."
    show sayori at t43 zorder 2
    mc "...Whatever. Let's go already."
    scene bg residential_day
    with wipeleft_scene
    $ ch2_winner = poemwinner[1].capitalize()
    if ch2_winner == "Sayori":
        $ ch2_winner = "Yuri"
    "I walk home with Sayori once more."
    "Even though it's only been a few days, a lot of things have already changed."
    "But today, Sayori is being a little quieter than usual on the way home."
    mc "Hey, Sayori..."
    show sayori 1k at t11
    s "..."
    s 1n "...Sorry! I was spacing out!"
    mc "Ah, no wonder..."
    s 1d "Um..."
    s "I was...thinking about something from earlier."
    s "I like how we get to..."
    s 1y "I-I mean..."
    "Sayori fumbles with her words."
    s 1a "So...let's just say that one day, [ch2_winner] asked to walk home with you..."
    mc "Huh?!"
    s "What would you do?"
    mc "What kind of question is that...?"
    mc "You're kind of putting me on the spot here..."
    s 1y "Ehehe..."
    menu:
        "Well..."
        "I would walk home with [ch2_winner].":
            if ch2_winner == "Natsuki":
                call ch2_end_natsuki from _call_ch2_end_natsuki_1
            else:
                call ch2_end_yuri from _call_ch2_end_yuri_1
        "I would still walk home with Sayori.":
            call ch2_end_sayori from _call_ch2_end_sayori_1

    "Then again, the festival is only a few days away..."
    "Who knows what will happen in that time?"
    return
label ch2_end_sayori:
    mc "Sayori..."
    mc "You really think I would ditch you for [ch2_winner]?"
    s 1e "Eh?!"
    s "B-But..."
    if ch2_winner == "Natsuki":
        s "She's so cute and fun to be around..."
    else:
        s "She's so beautiful and smart..."
    mc "Jeez..."
    mc "I already see her in the club every day."
    mc "Besides, you always seem to really like going home together..."
    mc "I wouldn't just ruin that for you."
    s 1y "You're so silly, [player]..."
    s "You think about me too much sometimes."
    s "[ch2_winner] would deserve it if she wanted it, so..."
    mc "Sayori, I've already made up my mind."
    mc "I really can't figure you out sometimes..."
    s "Sorry..."
    mc "Besides, what's the point in speculating something that's never going to happen?"
    s 1k "Hm..."
    show sayori at thide
    hide sayori
    "The conversation trails off."
    "It's kind of a weird thing for Sayori to care so much about..."
    "But I want to respect her and keep her happy, too."
    return

label ch2_end_natsuki:
    mc "Walking home with Natsuki, huh..."
    "Why does the thought of that make my heart pound...?"
    mc "I mean..."
    mc "I think I would be afraid of what she'd do to me if I turned her down..."
    s 1x "Isn't she so cute and fun to be around?"
    jump ch2_end_shared

label ch2_end_yuri:
    mc "Walking home with Yuri, huh..."
    "Why does the thought of that make my heart pound...?"
    mc "I mean..."
    mc "Given how hard it is for her to socialize, I would feel awful turning her down, so..."
    s 1x "Isn't she so beautiful and smart?"
    jump ch2_end_shared

label ch2_end_shared:
    mc "That has nothing to do with what I just said!"
    s 4s "Ahaha! You admitted it!"
    mc "Jeez..."
    mc "There's not even any point in speculating something that's never going to happen."
    s 1d "Well, maybe..."
    s "But I just like to think about it."
    s 1y "It's not long before you won't need me anymore, you know?"
    mc "Need you...?"
    mc "Sayori..."
    mc "I can't figure out how you're seeing things in your head right now."
    s "Sorry..."
    mc "Everyone is different..."
    mc "Nobody in the club is a replacement for you."
    s 1k "Hmm..."
    s "If you say so..."
    show sayori at thide
    hide sayori
    "The conversation trails off, and I'm left feeling awkward."
    "But it was kind of her fault for trapping me with such a weird question..."
    "I can't just lie to her."
    "But if there's something that makes her happy, I would hate to take that away from her."
    "That's why I said there's no point in speculating."
    return