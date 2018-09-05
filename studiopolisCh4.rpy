image rsod_bg_sayori = "Resources/rsod_overlay_sayori.png"

label metalsayoriFakeLock:
    stop music
    scene rsod_bg_sayori
    show rsod_face:
        xpos 0.1
        yalign 0.3
    show rsod_generic_message:
        xpos 0.1
        yalign 0.6
    show rsod_search_error_text:
        xpos 0.1
        yalign 0.75
    show rsod_sayori_test_lock_message:
        xpos 0.1
        yalign 0.8
    pause 10.0

    show sayori metalB at t32 zorder 3
    $ quick_menu = True
    play music metalSayori
    s "METAL SAYORI IS HERE!"
    show natsuki 4o at l31 zorder 3
    n "ANOTHER ONE OF YURI'S UGLY ROBOTS? C'MON! WHERE DO YOU HAVE OUR FRIEND???"
    s metalF "It seems you are not understanding, Natsuki..."
    show natsuki 1p at t31 zorder 3
    show sonic sonic10 at h33 zorder 3
    s metalA "I AM SAYORI!"
    s metalC "I was roboticized by the genius Dr. Eggman. Now I feel more alive and with less rainclouds than ever!"
    s metalB "And ready to destroy all of you."
    sth sonic07 "OH NO! EGGMAN, YOU WILL SERIOUSLY PAY FOR THIS!"
    n 12f "No! Anyone, but Sayori no!!!!!"
    "Natsuki ran to Monika, crying uncontrolably."
    show natsuki at lhide zorder 1
    hide natsuki
    show mc2 1p at l31 zorder 3
    mc2 "My cinnamon bun... This can't be..."
    mc2 1q "..."
    mc2 1c "I can't fight with her, Sonic, sorry..."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "<from 0.69>sfx/monikapound.ogg"
    pause 0.3
    hide screen tear
    mc2 1u "Losing control..."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "<from 0.69>sfx/monikapound.ogg"
    pause 0.3
    hide screen tear
    mc2 1t "..."
    "WHAT? It seems like MC disconnected from the world!"
    mc "Sonic, this is BAD, seriously BAD, why is this happening?"
    show mc2 at lhide zorder 1
    hide mc2
    show monika dragon at l31 zorder 3
    m "NOW I'M SERIOUSLY PISSED. FOR REAL."
    m "WHERE IS THAT MOTHERFUCKING DR. EGGMAN'S BASE?"
    m "ANYONE, BUT NOT SAYORI. SAYORI IS PRECIOUS FOR ALL OF US."
    y "Did you said Sayori...?"
    "Oh boy, the last thing missing in this bad puzzle. Yuri appeared too."
    show monika at lhide zorder 1
    hide monika
    show yuri 3y7 at l31 zorder 3
    y "NO NO NO NO NO! EGGMAN! HOW COULD YOU..."
    y "Sayori is important to all of us..."
    y "This can't be possible..."
    y 3y3 "This can't be..."
    show sonic sonic10 at h33 zorder 3
    $ quick_menu = False
    y 3d "I feel... I'm losing my mind... again..."
    y "...Ahahaha."
    y "Ahahahahahaha!"
    $ style.say_dialogue = style.normal
    y 3y5 "Ahahahahahahahaha!"
    "It seems Yuri is in shock about seeing Sayori like thi... Wait was happening?{nw}"
    $ style.say_dialogue = style.edited
    y 3y3 "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA"
    y cuts1 "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA{nw}"
    window hide(None)
    window auto
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "<from 0.69>sfx/monikapound.ogg"
    pause 0.3
    hide screen tear
    pause 1.43
    show sayori metalD at t32 zorder 3
    show yuri stab_1
    pause 0.75
    show sayori metalC at t32 zorder 3
    show yuri stab_8
    show blood:
        pos (610,485)
    pause 1.25
    show yuri stab_7
    pause 0.75
    show yuri stab_8
    show blood:
        pos (610,485)
    show sayori metalB at t32 zorder 3
    show yuri stab_4
    pause 1.25
    show yuri stab_5
    pause 0.70
    show yuri stab_6:
        2.55
        easeout_cubic 0.5 yoffset 300
    show blood as blood2:
        pos (635,335)
    pause 2.55
    hide blood
    hide blood2
    pause 0.25
    play sound fall
    $ style.say_dialogue = style.edited
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "<from 0.69>sfx/monikapound.ogg"
    pause 0.3
    hide screen tear
    show emerald phantomRuby at t41 zorder 4
    show sayori metalF at t32 zorder 3
    show yuri cuts6 at t31 zorder 3
    show sonic sonic10 at t33 zorder 3
    $ quick_menu = True
    y "AT LAST! NOW THAT YURI'S MIND WENT TO HELL, I CAN CONTROL HER FULLY!!!!"
    y "THANK YOU EGGMAN FOR MAKING THIS EASIER!!!"
    y "NOW I WILL PLAN HOW TO DESTROY ALL OF YOU, SUCKERS! YOU CAN ENJOY YOUR NEW ROBOT BUDDY!!!!"
    $ style.say_dialogue = style.normal
    s "CURSE YOU PHANTOM RUBY!"
    s metalH "DOCTOR EGGMAN! THE PHANTOM RUBY IS DOUBLE-CROSING BOTH YOU AND THE ASSHOLES, AND IS USING YURI FOR THAT!"
    show emerald at lhide zorder 1
    show yuri at lhide zorder 1
    hide emerald
    hide yuri
    show knuckles knuckles02 at l31 zorder 3
    kte "We need to do something, Sonic, [player]! This is not OK!!!!"
    sth sonic13 "Sayori! We know that the real you is inside that robot stuff! Try to listen to us!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "<from 0.69>sfx/monikapound.ogg"
    pause 0.3
    hide screen tear
    s metalG "DON'T TRY TO CALL THE SPIRIT OF THE ORIGINAL SAYORI! I'M IMPROVED AND BETTER THAN THAT STUPID!"
    s metalH "Now excuse me. I don't have orders to waste my precious time destroying all of you."
    s "I have better things to do, now that we all know the Phantom Ruby is the REAL threath here!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "<from 0.69>sfx/monikapound.ogg"
    pause 0.3
    hide screen tear
    show sayori at thide zorder 1
    hide sayori
    hide noise
    show knuckles at thide zorder 1
    hide knuckles
    show natsuki glitch1 at i31 zorder 2
    show monika 1p at t32 zorder 3
    n "Seriously... I can't believe Sayori is like that because of my dream of meeting Sonic... This is all my fault."
    n 12f "I WILL NEVER FORGIVE ME FOR THIS!"
    m "This is bad! Bad, bad, bad, bad! The glitches started again! We need to find a way to recover our friend!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "<from 0.69>sfx/monikapound.ogg"
    pause 0.3
    hide screen tear

    return

label chapter4PG:
    scene bg tcPressGarden
    with dissolve_scene_full
    stop music
    pause 3.0
    
    scene bg pressGarden
    with dissolve_scene_half
    if persistent.packagedMusic == True:
        show honey djHoney at l31 zorder 5
        play music pulpSolstice
        dj "Now playing! {i}Garmiani - Fogo (feat. Julimar Santos){/i}."
        show honey at lhide zorder 1
        hide honey
    else:
        play music pressGarden1
    "..."
    "And so, contrary to what Sonic wanted, we went to Press Garden."
    "The girls and MC were surprised to find a base in the middle of a snowy and cozy forest."
    "The base was used by Dr. Eggman as a press room, creating and publishing negative propaganda against Sonic and favorable to his own interests"
    "The gigantic structure was painted in pastel green colors and had pink roses at the inside, due to trying to imitate the native vegetation of the forest."
    "The base has large presses transporting pamphlets and iconography at high speeds, rotating machines in the shape of umbrellas, ink bottles and paper sheets."
    "While we waited that Yuri appeared, Ghost was telling us creepypasta stories that she found on Internet."
    show ghostnatsuki gNatsu1 at face with dissolve
    g "AND THEN, CONTRARY AT WHAT HE WAS EXPECTING, THE ANIMATRONICS ARRIVED AT THE ROOM OF THE POOR SECURITY GUARD!"
    g "GIVE US YOUR SOUL, MIKE SCHMIDT!!! YOU KILLED US!!! WE WANT REVENGE!!!"
    g "NOOOO! YOUR KILLER WASN'T ME! NOOOOO! NOOOOO! GET AWAYYYYY!!! AAAAAAAAAAAAAAAAAAARGH!!!!"
    g "THE SOUND OF THE TOREADOR MARCH FILLED THE PLACE..."
    show ghostnatsuki gNatsu1 at t11 zorder 2
    g "AND THEN THE IMPOSSIBLE HAPPENED!!!"
    play sound "sfx/crack.ogg"
    show ghostnatsuki gNatsu2 at t11 zorder 2
    g "THE GOLDEN ANIMATRONIC BEAR NECKED THE POOR SECURITY GUARD!!!"
    g "MUAHAHAHAHAHAHAHAHAHAHA! THE BLACK PUPPET ANIMATRONIC LAUGHED HEAVILY, AND ALL THE ANIMATRONICS CELEBRATED EATING PIZZAS!"
    g "BUT WITHOUT THEY KNOWING IT, A SINISTER FIGURE WAS HIDDEN IN THE BATHROOMS, COVERED BY THE SHADOWS OF THE NIGHT."
    g "THE PURPLE GUY CLAIMED THE LIVES OF MORE CHILDREN, AND A STUPID SECURITY GUARD! HE LAUGHED MANIATICALLY AFTER ESCAPING FROM THE PIZZERIA..."
    g "NOW, THANKS TO THE INCREASE IN THEIR KILL COUNT, THE ANIMATRONICS WERE FORCED TO BE RECLASSIFIED AS KETER BY DR. LIGHT, AND THE FRANCHISES OF THE PIZZERIA CLOSED."
    play sound "sfx/crack.ogg"
    show ghostnatsuki gNatsu1 at t11 zorder 2
    g "Ta-da! End of the story! Do you think I could convince Marc13Bautista to add my creepypasta to the Doki Doki Lost Control mod?"
    g "I love crossovers with SCP Foundation!"
    show ghostnatsuki at thide zorder 1
    hide ghostnatsuki
    show monika 1b at t43 zorder 2
    show natsuki 1d at t42 zorder 3
    show mc2 1e at t44 zorder 4
    show sayori 1d at t41 zorder 4
    show sonic sonic14 at l41 zorder 5
    sth "What a thrilling story, sis! Tails wrote everything to program a videogame based on that!"
    show sonic at lhide zorder 1
    hide sonic
    mc "Seriously, if he doesn't accept your story, his mod will lose a good source of horror!"
    m "Absolutely! The story was thrilling! I was scared almost the entire time!"
    n "I hate horror, but I can't say that the story was bad at all."
    s "I just wanted the story to end! I will never go to a pizzeria at night ever again!"
    mc2 "Sayori! It was a fan fiction of Ghost! Haunted robots in pizzerias doesn't exist! That is the most stupid idea ever!"
    "Suddendly, Yuri appeared!"
    m 4g "Hey buddies, it's Yuri!"
    show monika at lhide zorder 1
    show mc2 at lhide zorder 1
    show sayori at lhide zorder 1
    hide monika
    hide sayori
    hide mc2
    show natsuki 1d at t31 zorder 3
    show yuri cuts1 at l33 zorder 4
    y "I can't believe this! You came here to see me before fighting the asshole Infinite!"
    n 4e "Yuri, seriously, can you stop cutting yourself? This is bad for your health!"
    y 1p "Natsuki!!!! I..."
    y cuts5 "That doesn't involve you..."
    y 1p "..."
    y 1w "You are right, I'm sorry. Thank you for worring about me..."
    "Suddendly, a robot, similar to Natsuki, appeared! I think Yuri built this robot too..."
    show boss3 metalNatsuki at h32 zorder 3
    n "METAL. NATSUKI. IN ORDER. OPERATING SYSTEM ACTIVE AND FUNCTIONING CORRECTLY!"
    show natsuki 4v at h31 zorder 3
    n "ARE YOU FUCKING KIDDING ME, YURI? YOU BUILD THIS AFTER ME???? I'M. NOT. CUTE!!!!!!!"
    n 4o "HOW DARED YOU? I WILL PUNCH YOU RIGHT NOW!"
    mc "NATSUKI! LANGUAGE! AGAIN!"
    n 4v "BUT-BUT-BUT-BUT!!! AAAAAAAAAAAAA! I'M NOT FUCKING CUTE GODDAMIT! WHY DOES THE ONE I LOVE KEEP JOKING WITH ME???"
    y cuts5 "But I built this robot to express your manga fantasies, Natsuki! That's not fair!!!"
    y "OK, Metal Natsuki, you will not be used now. Go back with Metal Trashy."
    show boss3 at thide zorder 1
    hide boss3
    show natsuki 4v at t21 zorder 3
    show yuri cuts5 at h22 zorder 4
    y "LET'S. TRY. WITH. THE SONG. THEN. STUPID DJ, THE SONG PLEASE!"
    stop music fadeout 2.0
    play music lovePCKG
    show honey djHoney at l31 zorder 5
    dj "Now playing: {i}Café Quijano - Robarle Tiempo al Tiempo (BonerDeejey remix){/i}."
    dj "Yuri explicity told me that I had to stream a CUTE song for her loved one!"
    dj "And I'm not stupid."
    if persistent.packagedMusic == False:
        dj "Also: Hi! I'm Honey, Honey the Cat! the resident DJ for this mod!"
        dj "Because you didn't choose to play my EDM session music, you will only see me in this scene! Kisses!"
    show honey at lhide zorder 1
    hide honey
    show natsuki 4p at h21 zorder 3
    n "WHAAAAAAAAAAAAAAAAAAAAAAAT?"
    show sonic sonic05 at h44 zorder 5
    sth "Oh c'mon! Why she explodes in rage so fast????"
    show sonic at lhide zorder 1
    hide sonic
    show yuri cuts2 at t22 zorder 4
    show natsuki 4v at h21 zorder 5
    n "YURIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII...!"
    n 4o "I WILL BEAT THE SHIT OUT OF YOU!"
    n "I WILL NEVER FORGIVE YOU FOR PLAYING A CUTE SONG!!!! I TOLD YOU THAT I'M. NOT. CU..."
    n 2c "Eh... actually..."
    n 1c "The song it's amazing."
    n 1t "And it's cute."
    "{i}Suddendly all Press Garden is filled with jazmine aromatherapy essence, and the newspaper machines stopped...{/i}"
    y cuts5 "You know what? I'm sick of being so coward! I will do the thing I should had do since first day of class!"
    y 1t "Do you concede me this dance, my lovely obnoxious brat?"
    n "Yeah, sure, gorgeous edgy bitch."
    $ quick_menu = False
    show natsuki 1d at h21 zorder 5
    show yuri 1d at h22 zorder 5
    pause 1.0
    show natsuki 4z at h21 zorder 5
    show yuri 3m at h22 zorder 5
    pause 1.0
    show natsuki 1d at h22 zorder 5
    show yuri 1d at h21 zorder 5
    pause 1.0
    show natsuki 4z at h22 zorder 5
    show yuri 3m at h21 zorder 5
    pause 1.0
    show natsuki 1d at h21 zorder 5
    show yuri 1d at h22 zorder 5
    show monika 2b at l41 zorder 4
    pause 1.0
    show natsuki 4z at h21 zorder 5
    show yuri 3m at h22 zorder 5
    show monika 4k at h41 zorder 4
    pause 1.0
    show natsuki 1d at h22 zorder 5
    show yuri 1d at h21 zorder 5
    show monika 2b at h41 zorder 4
    pause 1.0
    show natsuki 4z at h22 zorder 5
    show yuri 3m at h21 zorder 5
    show monika 4k at h41 zorder 4
    pause 1.0
    show natsuki 1d at h21 zorder 5
    show yuri 1d at h22 zorder 5
    show monika 2b at h41 zorder 4 
    pause 1.0
    show natsuki 4z at h21 zorder 5
    show yuri 3m at h22 zorder 5
    show monika 4k at h41 zorder 4
    pause 1.0
    show natsuki 1d at h22 zorder 5
    show yuri 1d at h21 zorder 5
    show monika at lhide zorder 1
    hide monika
    show ghostnatsuki gNatsu1 at l41 zorder 4
    pause 1.0
    show natsuki 4z at h22 zorder 5
    show yuri 3m at h21 zorder 5
    show ghostnatsuki gNatsu2 at h41 zorder 4
    pause 1.0
    show natsuki 1d at h21 zorder 5
    show yuri 1d at h22 zorder 5
    show ghostnatsuki gNatsu1 at h41 zorder 4
    pause 1.0
    show natsuki 4z at h21 zorder 5
    show yuri 3m at h22 zorder 5
    show ghostnatsuki gNatsu2 at h41 zorder 4
    pause 1.0
    show natsuki 1d at h22 zorder 5
    show yuri 1d at h21 zorder 5
    show ghostnatsuki gNatsu1 at h41 zorder 4
    pause 1.0
    show natsuki 4z at h21 zorder 5
    show yuri 3m at h22 zorder 5
    show ghostnatsuki gNatsu2 at h41 zorder 4
    pause 1.0
    show natsuki 1d at h22 zorder 5
    show yuri 1d at h21 zorder 5
    show ghostnatsuki at lhide zorder 1
    hide ghostnatsuki
    show sayori 2s at l41 zorder 4
    pause 1.0
    show natsuki 4z at h21 zorder 5
    show yuri 3m at h22 zorder 5
    show sayori 3s at h41 zorder 4
    pause 1.0
    show natsuki 1d at h21 zorder 5
    show yuri 1d at h22 zorder 5
    show sayori 2s at h41 zorder 4
    pause 1.0
    show natsuki 4z at h22 zorder 5
    show yuri 3m at h21 zorder 5
    show sayori 3s at h41 zorder 4
    pause 1.0
    show natsuki 1d at h22 zorder 5
    show yuri 1d at h21 zorder 5
    show sayori 2s at h41 zorder 4
    pause 1.0
    show natsuki 4z at h21 zorder 5
    show yuri 3m at h22 zorder 5
    show sayori 3s at h41 zorder 4
    pause 1.0
    show natsuki 1d at h21 zorder 5
    show yuri 1d at h22 zorder 5
    show sayori at lhide zorder 1
    hide sayori
    show sonic sonic00 at l41 zorder 4
    pause 1.0
    show natsuki 4z at h21 zorder 5
    show yuri 3m at h22 zorder 5
    show sonic sonic01 at h41 zorder 4
    pause 1.0
    show natsuki 1d at h22 zorder 5
    show yuri 1d at h21 zorder 5
    show sonic sonic02 at h41 zorder 4
    pause 1.0
    show natsuki 4z at h22 zorder 5
    show yuri 3m at h21 zorder 5
    show sonic sonic12 at h41 zorder 4
    pause 1.0
    show natsuki 1d at h22 zorder 5
    show yuri 1d at h21 zorder 5
    show sonic sonic14 at h41 zorder 4
    pause 1.0
    show natsuki 4z at h22 zorder 5
    show yuri 3m at h21 zorder 5
    show sonic sonic15 at h41 zorder 4
    pause 1.0
    show natsuki 1d at h21 zorder 5
    show yuri 1d at h22 zorder 5
    show sonic sonic03 at h41 zorder 4
    pause 1.0
    show natsuki 4z at h21 zorder 5
    show yuri 3m at h22 zorder 5
    show sonic at lhide zorder 4
    hide sonic
    pause 1.0
    show natsuki 1d at h22 zorder 5
    show yuri 1d at h21 zorder 5
    pause 1.0
    show natsuki 4z at h21 zorder 5
    show yuri 3m at h22 zorder 5
    pause 1.0
    show natsuki 1d at h21 zorder 5
    show yuri 1d at h22 zorder 5
    pause 1.0
    show natsuki 4z at h22 zorder 5
    show yuri 3m at h21 zorder 5
    $ quick_menu = True
    pause 1.0
    n 4t "Well, that was amazing, Yuri. I wanted to do that since we meet on the Literature Club."
    y 2u "The same with me, Natsuki. How is this called? \"Unresolved Sexual Tension\", it seems?"
    n "It seems you and me read too much TVTropes..."
    y "And we read the same exact topics."
    y "Do you read the SCP Foundation too, my love?"
    n "I'm a big fan of SCP-682 The Invincible Lizard. I think it is cute."
    n "Also, just asking, why did you choose a song with spanish lyrics...?"
    y "Quoting the greatest Victor Hugo:"
    y 2l "El inglés es ideal para hablar de negocios, el alemán se hizo para las ciencias, el francés es el lenguaje del amor y el español, ¡ah, el español!, es el idioma para hablar con Dios."
    y "Translation! English is the language for speak about business, german is for sciences, french is the love language, and spanish... ah! spanish is the language for talk with God."
    y 2m "And you are my Goddess, Natsuki."
    n "And you are my lovely gorgeous bilingual girl."
    y 2u "Also the mod's author is Chilean, so obviously he planned to use a spanish song."
    "NOW YOU CAN REALLY FEEL THE TENSION IN THE AIR! IS LIKE IF YOU CAN CUT IT WITH A KNIFE!"
    "CUE THE NATSUKI X YURI SHIP! MY DREAM COME TRUE!!! {i}SQUEEEEEEEEEEEEEEEE{/i}..."
    show monika 4k at l41 zorder 4
    m "Who would guess this? So this is why those two love to fight so much..."
    show monika at lhide zorder 1
    hide monika
    show sayori 4s at l41 zorder 4
    s "THEY WILL MAKE A CUTE COUPLE!!!!!"
    show sayori at lhide zorder 1
    hide sayori
    show mc2 1n at l41 zorder 4
    mc2 "SAYORI! This is not the moment to say that!"
    s "Sorry xD."
    show mc2 at lhide zorder 1
    hide mc2
    show ghostnatsuki gNatsu1 at l41 zorder 4
    g "WELL, WHY IS THE PIECE OF SHIT CALLED ROOKIE STILL LOOKING AT THEM? LET'S GIVE THEM THEIR SO WANTED SPACE!"
    m "True, girls! Club activity: let's make Natsu and Yuri make her own poetry of love alone, ok?"
    show ghostnatsuki at lhide zorder 1
    hide ghostnatsuki
    show sonic sonic13 at l41 zorder 4
    sth "Let's go, everyone! There is a world to save out there!"
    show natsuki 4u at h22 zorder 5
    show yuri 3u at h21 zorder 5
    mc "BUT I WANT TO SEE THIS!!!!!"
    show sonic sonic06 at h41 zorder 4
    sth "Rookie, come here and let us give quality time to this two girls, ok?"
    show natsuki 4o at h22 zorder 5
    show yuri 3r at h21 zorder 5
    mc "BUT I WANNNA SEE THE ACTION!"
    show sonic at lhide zorder 1
    hide sonic
    show knuckles knucklesCom at h41 zorder 4
    kte "ROOOOOKIIIIIEEEEEE! CAPTAIN'S ORDERS!!!!"
    mc "BUT THE GOOD PART STARTS HERE!!!!"
    show knuckles at thide zorder 1
    hide knuckles
    show tails tailsCom at h41 zorder 4
    show natsuki 4o at h22 zorder 5
    show yuri 3y3 at h21 zorder 5
    mtp "ROOKIE! YOU ARE MAKING THEM FEEL UNCOMFORTABLE! MOVE FROM THERE ALREADY!"
    mc "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!"
    show tails at thide zorder 1
    hide tails
    n "(WHY THIS MOTHERFUCKER DOESN'T MOVE???? I WANNA KISS YURI NOW!!!!)"
    if persistent.genderMale == True:
        y "(C'MON, STUPID RETARDED WOLF!!!! I WANNA KISS NATSUKI ALREADY!!!!)"
    else:
        y "(C'MON, STUPID RETARDED CAT!!!! I WANNA KISS NATSUKI ALREADY!!!!)"
    show honey djHoney at l41 zorder 4
    dj "ROOKIE! ARE YOU RETARDED? MOVE YOUR STUPID ASS ALREADY!!!! YOU ARE RUINING THE MOMENT!!!!"
    mc "NO, NO, NO, NO, NO! THIS IS MY DREAM COME TRUE!!!!"
    mc "I WILL NOT MOVE, I ALWAYS WANTED TO SEE THI..."
    show natsuki 4z at h22 zorder 5
    show yuri 3s at h21 zorder 5
    show honey at lhide zorder 1
    hide honey
    show amy amy02 at l41 zorder 4
    mc "OUCH! NOOOO! MY EAR!!! AMYYYYYYY!!!! OOOOUUUUUCH!"
    amyR "MOVE. ROOKIE. NOW."
    show natsuki 1t at h22 zorder 5
    show yuri 1u at h21 zorder 5
    show amy at lhide zorder 1
    hide amy
    n "Well, now that we are TRULY alone here... Oh gosh this is so difficult and embarrasing..."
    y "Just kiss me for fucks sake, ok? This is what we wanted from so long, let's go outside..."
    show yuri at lhide zorder 1
    show natsuki at lhide zorder 1
    hide yuri
    hide natsuki
    show pictures yuriXnatsu at t11 zorder 5
    "AND REMEMBER: THIS IS JUST A SHIPPING!\nA GAAAAAAAAAAAME SHIPPING!\nTHANKS FOR WATCHING!"
    "While Natsuki and Yuri did their poetry of love, Sonic and Co. were fighting Infinite on Flying Battery."
    "When both teams got together, we left the interior of Press garden and went straight to the forest."
    stop music fadeout 3.0
    pause 3.0

    return

label chapter4FB:
    scene bg tcVsInfinite
    with dissolve_scene_full
    stop music
    pause 3.0
    
    scene bg flyingBattery
    with dissolve_scene_half
    if persistent.packagedMusic == True:
        show honey djHoney at l31 zorder 5
        play music fBatteryPCKG
        dj "Now playing! {i}Something just like this{/i} from {i}The Chainsmokers feat. Coldplay{/i}!"
        show honey at lhide zorder 1
        hide honey
    else:
        play music fBattery
    "..."
    "And so, contrary to what Natsuki wanted, Sonic and myself went to Flying Battery."
    "After a long battle with Infinite, we were victorious."
    "Tails hacked some of the Eggman's computers, and got info about Infinite's source of power."
    "It seems the Phantom Ruby recharges it's energy on a secret station inside Lava Reef zone."
    "So we exited Flying Battery to reunite with the girls at the outside of Press Garden's base."
    stop music fadeout 3.0
    pause 3.0

    return

label chapter4:
    scene bg tcPressGarden
    with dissolve_scene_full
    stop music
    pause 3.0
    
    scene bg pressGarden
    with dissolve_scene_half
    if persistent.packagedMusic == True:
        play music eggmanPCKG
        show honey djHoney at l31 zorder 5
        dj "Now playing {i}Downfall{/i}, from the mobile game Crash Fever. Dr. Eggman's theme."
        show honey at lhide zorder 1
        hide honey
    else:
        play music eggmanMusic
    "..."
    "Now both teams are together again."
    "We are tresspasing Press Garden's forest, on our ways to Lava Reef zone."
    "After releasing some animals from abandoned animal capsules, we reached a computer unit that showed a planet held in chains, and plans to retrieve a certain robot already known to all of us."
    sth "Metal Sonic! Eggman wants to retrieve Metal Sonic from Little Planet! And that means that Eggy is planning to use the Time Stones!"
    sth "We can't let Eggman retrieve the Time Stones or metalize Little Planet! Tails! Knuckles! Transport here, we have a new mission now!"
    show eggman eggman00 at t11 zorder 3
    egg "Very intelligent, hedgehog. Very smart. Congratulations, stupid rodent, for being clever for once and not let Tails do your homework."
    show eggman eggman00 at t33 zorder 3
    show emerald phantomRuby at t32 zorder 3
    mc "It's Eggman! And he brought the Phantom Ruby with him!"
    egg "Unfortunately for all of you, I've been tracking Metal Sonic for quite some time now."
    egg "And also I'm building a new base in Little Planet, thanks to the power of the Phantom Ruby."
    egg "Now I have new and interesting plans..."
    egg "Which one of your pathetic new friends is called \"Sayori\", rodent?"
    show monika 2h at t31 zorder 3
    m "You will not have information of any of my Club Members, stupid human in a shape of a rotten egg."
    egg eggman03 "HOW DARE YOU! ARE YOU DEFYING ME AND MY ORDERS?"
    egg "THIS IS MY WORLD NOW! I CONQUERED IT THANKS TO THE POWER OF THE PHANTOM RUBY!"
    egg "According to some investigation I did, the Phantom Ruby was here before, and it caused a gigantic war between different factions of our world, each time more destructive."
    egg "But the pathetic heroes of that time destroyed all the work of the Ruby, and sended it to outer space!"
    show rubypink zorder 5:
        alpha 0.0
        easein 4.0 alpha 0.7
    egg "And you, teenager, don't have any power over the Phantom Ruby! RUBY! BRING ME SAYORI RIGHT NOW!"
    show monika at lhide zorder 1
    hide monika
    m "OH NO! SAYORI! NO!"
    mc2 "LEAVE SAYORI ALONE, EGGHEAD!!!!!!"
    n "I'M SERIOUSLY TIRED OF THAT CHEAP PHANTOM RUBY!!!! RELEASE SAYORI, BALDY MC'NOSEHAIR!"
    show sayori 4p at l31 zorder 3:
        dizzy(1, 1.0)
    s "AAAAAAAAAH! What's happening???? I don't wanna go!!!!"
    egg eggman02 "WELCOME TO THE EGGMAN EMPIRE, LITTLE GIRL!"
    egg "I HAVE SOME PLANS FOR YOU!"
    egg "But first, I need to send you to another place for some testings..."
    play sound ruby

    scene bg tcVsMetal
    with dissolve_scene_full
    stop music fadeout 2.0
    pause 3.0
    
    scene bg stardust
    with dissolve_scene_full
    $ gtext = glitchtext(12)
    if persistent.packagedMusic == True:
        $ dj_name = gtext
        play music muffledStardust
        dj "ERROR! CAN'T CONNECT TO MUSIC SERVER! CAN'T SHOW CHARACTER!"
        dj "Now playing: [gtext]."
        dj "[gtext]\n[gtext]."
    else:
        play music stardust
    show sayori 1f at t11 zorder 3
    s "Where am I? What is this place?"
    s "I don't know where am I! And I can't see MC or Monika or my friends!"
    egg "WELCOME TO STARDUST SPEEDWAY, MISS SAYORI!"
    egg "I HAVE MARVELOUS PLANS FOR YOU IN MY GLORIOUS EMPIRE!"
    egg "YOU WERE CHOSEN FOR A VERY SPECIFIC AND IMPORTANT MISSION!"
    egg "IF YOU WANNA ESCAPE FROM THIS PLACE, YOU MUST FULFILL THE MISSION FIRST! NO EXCEPTIONS!"
    egg "METAL SONIC! SHOW YOURSELF!"
    s 4m "METAL WHAT?????"
    if persistent.packagedMusic == True:
        play music vsMetalPCKG
        dj "ERROR! CAN'T CONNECT TO MUSIC SERVER! CAN'T SHOW CHARACTER!"
        dj "[gtext]: {i}Concussive{/i} by {i}DJ Sona{/i}, [gtext]."
        dj "[gtext]."
        $ dj_name = "DJ-Honey"
    else:
        play music vsMetal
    show sayori 4m at h22 zorder 3
    show metal metal00 at l21 zorder 3
    met "METAL SONIC ONLINE! ALL SYSTEMS OPERATIVE AND FUNCTIONING!"
    met "IMPERATIVE FIRST MISSION: DESTROY SONIC THE HEDGEHOG! ONLY ONE SONIC CAN PREVAIL!"
    met "RECEIVING NEW ORDER: EGG-DIRECTIVE-045."
    met "SAYORI: FIGHT WITH ME IN A RACE!"
    met "FIRST ONE THAT FINISHES THE RACE AND GET TO THE MACHINE GENERATOR WILL ESCAPE FROM THIS PLACE!"
    s 3j "I'm not scared of you, Metal Sonic! I'm more confident than ever in myself!"
    s 3j "LET'S FIGHT! THE FASTEST ONE SHALL PREVAIL!"
    met metal01 "EXCELLENT. A NEW BIOLOGICAL LIFEFORM TO SQUASH! STARTING ENGINES!"

    scene bg stardust
    show image Solid("ff0000") as Solid1 zorder 97:
        additive 1.0
    show image Solid("#440000") as Solid2 zorder 98:
        additive 0.4
    show veins zorder 99:
        additive 0.5
    if persistent.packagedMusic == True:
        play music muffledStardust
    else:
        play music stardust
    show sayori 4r at h22 zorder 3
    show metal metal00 at t21 zorder 3
    with dissolve_scene_half
    s "Yes! I win the race!"
    s 1m "Now you must fulfill your part of the mission, Eggman!"
    egg "Yes, yes, yes."
    stop music
    egg "BUT YOU WILL GO BACK TO THE PRESENT TIME IN MY TERMS!"
    egg "METAL SONIC! ACTIVATE THE WEAPON!"
    met "INITIATING ROBOTICIZER WAVE!"
    show sayori 4p at t22 zorder 3
    s 4p "WAIT WHAT?????? WHAT'S HAPPENING???? AAAAAAAAAAAAAAAAAAAAAAAAAAAA..."
    met "GENESIS WAVE'S ROBOTICIZER RAY ACTIVATED!"
    play sound roboticizer
    pause 2.0

    scene bg stardust
    with dissolve_scene_full
    $ in_sayori_kill = True
    $ delete_character("sayori")
    $ persistent.sayori_kill = True
    python:
        try: renpy.file(config.basedir + "/hxppy thxughts.png")
        except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
    "{i}Maybe you want to check your characters folder and understand the seriousness of what happened...{/i}"
    show metal metal00 at t21 zorder 3
    show sayori metalDark at t22 zorder 3
    $ s_name = "Metal-Sayori"
    play music metalSayori
    egg "Did it worked, Metal Sonic?"
    met "MISSION COMPLETED SUCCESSFULLY! YOUR NEW ROBOTICIZED SLAVE IS ONLINE!"
    s metalB "Metal Sayori online! Ready to serve, Dr. Eggman!"
    s metalC "Awaiting your orders, Doctor."
    egg "OHOHOHOHOHOHO! NO WAY, I CAN'T BELIEVE THIS!"
    egg "THE ROBOTICIZER RAY IS WORKING!"
    egg "Well, well, well, Metal Sayori and Metal Sonic."
    egg "New objective: DESTROY SONIC AND THAT PESKY GIRLS OF THE LITERATURE CLUB, F.O.R.E.V.E.R.!"
    stop music fadeout 2.0
    met metal01 "ORDER RECEIVED! COMMENCING TIME TRAVEL TRANSPORT!"
    s metalE "With pleasure, Doctor!"
    show pictures futureStarpost at t32 zorder 4
    show metal metal01 at t31 zorder 3
    show sayori metalE at t33 zorder 3
    play sound FUTURE
    pause 5.5

    scene bg tcStardust
    with dissolve_scene_full
    pause 3.0

    scene bg stardust2
    with dissolve_scene_full
    if persistent.packagedMusic == True:
        show honey djHoney at l31 zorder 5
        play music speedwayPCKG
        dj "Now playing! {i}Robarte un Beso{/i} from {i}Carlos Vives and Sebastian Yatra{/i}."
        dj "Wait. It's just me, or I have a bad feeling about something...?"
        show honey at lhide zorder 1
        hide honey
    else:
        play music stardust2
    mc "We were searching Sayori for hours, MC! We don't know in which part of Little Planet she is!"
    mc2 "WE MUST KEEP SEARCHING! I WILL NOT LET MY CINNAMON BUN ALONE IN A WEIRD PLACE LIKE THIS!"
    m "Mister Sonic, mister Tails, do you have any info?"
    mtp "According to my radar..."
    show sonic sonic10 at l33 zorder 3
    sth "WAIT!!! Someone appeared here!"
    stop music fadeout 2.0
    sth sonic09 "Wait... That is Sayori...? Oh no no NO NO NO NONONONONONONONONO..."
    show sayori 2s at h32 zorder 3
    s "Surprise, hedgehog!"
    $ quick_menu = False
    show sayori 2s at t32 zorder 3
    pause 2.0
    show sayori 2r at t32 zorder 3
    pause 2.0
    show sayori 2q at t32 zorder 3
    pause 2.0
    show sayori 2a at t32 zorder 3
    pause 2.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "<from 0.69>sfx/monikapound.ogg"
    pause 0.3
    hide screen tear
    show noise zorder 99:
        alpha 0.0
        linear 3.0 alpha 0.25
    python:
        try: sys.modules['renpy.error'].report_exception("I TOLD YOU: DON'T DO WHAT SONIC DOES! NOW SAYORI IS MINE... FOREVER! TRY TO RECOVER HER, I DARE YOU!!!!", False)
        except: pass
    $ config.mouse = {"default": [
                                ("gui/mouse/s_head2.png", 0, 0),
                                ("gui/mouse/s_head2.png", 0, 0),
                                ("gui/mouse/s_head2.png", 0, 0),
                                ("gui/mouse/s_head2.png", 0, 0),
                                ("gui/mouse/s_head.png", 0, 0),
                                ("gui/mouse/s_head.png", 0, 0),
                                ("gui/mouse/s_head2.png", 0, 0),
                                ("gui/mouse/s_head2.png", 0, 0),
                                ("gui/mouse/s_head2.png", 0, 0),
                                ("gui/mouse/s_head2.png", 0, 0),
                                ("gui/mouse/s_head2.png", 0, 0),
                                ("gui/mouse/s_head2.png", 0, 0),
                                ("gui/mouse/s_head2.png", 0, 0),
                                ("gui/mouse/s_head2.png", 0, 0),
                                ("gui/mouse/s_head.png", 0, 0),
                                ]}
    
    call metalsayoriFakeLock
    scene bg tcStardust
    pause 1.0
    scene bg creepyDokiForces
    pause 2.0
    scene bg creepyDokiForcesC
    pause 2.0
    scene bg creepyDokiForcesB
    pause 3.0

    scene bg stardust2
    if persistent.packagedMusic == True:
        show honey djHoney at l31 zorder 5
        play music speedwayPCKG
        dj "Now playing! {i}Robarte un...{/i}"
        dj "Wait, I said that before!!! Did something wrong happen?"
        mc "Something VERY wrong, DJ Honey... very wrong..."
        show honey at lhide zorder 1
        hide honey
    else:
        play music stardust2
    show natsuki 12f at t31 zorder 3
    show monika g2 at t32 zorder 3
    show sonic sonic10 at t33 zorder 3
    sth "WHAAAAA... OUR WORLD RELOADED ITSELF????"
    sth sonic06 "Why...?"
    sth "Why is Sayori so important to all of you? And why those... strange weirdo things happened to our world since she appeared?"
    $ gtext = glitchtext(40)
    $ style.say_dialogue = style.edited
    m "[gtext]"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "<from 0.69>sfx/monikapound.ogg"
    pause 0.3
    hide screen tear
    m help "[gtext]."
    m help "HELP ME."
    $ style.say_dialogue = style.normal
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "<from 0.69>sfx/monikapound.ogg"
    pause 0.3
    hide screen tear
    m 1p "Sayori is the one that is our anchor to Earth. She motivates, encourages and love all of us."
    m "And now her soul is not here, and neither is in my special one's OS too..."
    m "[player], remember what I told you about Sayori before and what happened in our world?"
    m 2p "Sayori is our stability. The moment Sayori killed herself, everything went downhill for Yuri, Natsuki and even myself."
    m "We need to find a way to make her normal again, or else..."
    show sonic sonic10 at h33 zorder 3 
    m 4p "The scripts of our Literature Club and what is left of the world will go to hell again if Sayori doesn't go back to normal."
    m "Whatever stuff happens to our scripts will affect your world too, Sonic, because you are with us. We are so sorry for this."
    mc "And now, the destiny of our world is in ours and Sayori's hands!!!"
    "WE HAVE TO DO SOMETHING!"
    sth sonic06 "Tails! Do you have solutions?"
    show natsuki at thide zorder 1
    hide natsuki
    show tails tailsGlitch at l31 zorder 3
    $ style.say_dialogue = style.edited
    mtp "THERE'S NOTHING YOU CAN DO, PLAYER. SURRENDER TO THE PHANTOM RUBY!"
    mtp "SURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDER{nw}"
    $ style.say_dialogue = style.normal
    mtp tails04 "Sonic! This is terrible!"
    mtp "Now I know why is this happening!"
    mtp tails03 "Eggman used the Phantom Ruby to reset our world at his pleasure! That's why we forgot our memories before the race!"
    mtp "And now he has a real roboticizer machine... Poor Sayori..."
    show image Solid("ff0000") as Solid1 zorder 97:
        additive 1.0
    show image Solid("#440000") as Solid2 zorder 98:
        additive 0.4
    show veins zorder 99:
        additive 0.5
    show sonic sonicEXE at t33 zorder 3
    $ style.say_dialogue = style.edited
    sth "IF WE CAN'T DO ANYTHING, THEN WHY ARE YOU WORRIED?"
    sth "JUST SMILE, SO WE CAN PLAY A GAME TOGETHER..."
    sth "SO MANY SOULS TO PLAY WITH, SO LITTLE TIME, DON'T YOU AGREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE{nw}"
    $ style.say_dialogue = style.normal
    hide Solid1
    hide Solid2
    hide veins
    show sonic sonic10 at t33 zorder 3
    mtp "The only way to save Sayori is to get into the place Eggman has the source of Phantom Ruby's power!"
    mtp "Finding the Roboticizer machine, revert it's effects and use it on Sayori!"
    mtp "But now, with the world against us, and even with Yuri fully controlled by the Ruby, our mission will be even more dangerous!"
    show sonic sonic07 at t33 zorder 3
    m 5b "For my friends of the Club, I even will DIE trying it!"
    m "Let's move, team! Sayori and Yuri need us!"
    sth "Egghead, you went too far this time! I will get you!!!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "<from 0.69>sfx/monikapound.ogg"
    stop music
    pause 0.3
    hide screen tear
    show monika at thide zorder 1
    hide monika
    show tails at thide zorder 1
    hide tails
    show image Solid("ff0000") as Solid1 zorder 97:
        additive 1.0
    show image Solid("#440000") as Solid2 zorder 98:
        additive 0.4
    show veins zorder 99:
        additive 0.5
    show sonic sonicEXE at t11 zorder 2 with dissolve
    $ style.say_dialogue = style.edited
    sth "HELLO."
    sth "IT SEEMS YOU DIDN'T UNDERSTAND ME."
    sth "THERE IS {i}NOTHING{/i} TO BE WORRIED ABOUT..."
    sth "YOU CAN'T DO ANYTHING, SO DON'T EVEN DARE TO TRY, PLAYER."
    sth "I AM GOD.\nTHE PHANTOM RUBY IS GOD\nTHE DARK CLOUD WILL RISE."
    sth "YOU CAN'T RUN FROM US!"
    sth "COME HERE AND PLAY, PLAYER!"
    sth "COME HERE AND PLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA{nw}"
    $ style.say_dialogue = style.normal

    scene bg tcHidrocity
    with dissolve_scene_full
    pause 3.0

    scene bg hidrocity
    with dissolve_scene_half
    if persistent.packagedMusic == True:
        play music hidrocityPCKG
        show honey djHoney at l31 zorder 5
        dj "Now playing! {i}True Feeling{/i} from {i}Galantis{/i}."
        dj "Don't get wet, everyone!"
        show honey at lhide zorder 1
        hide honey
    else:
        play music hidrocity
    scene bg creepyDokiForcesC
    pause 0.5
    scene bg hidrocity
    "And so, we exited Little Planet using the big chains that keeps it grounded to Angel Island, and we arrived at Hydrocity."
    "Knuckles told us that these are the ruins of his ancient civilization, before the disaster with Chaos and that stuff."
    "I hate water anyways, so it's not one of my favourite places. Water zones aren't my kind of place to rest and explore."
    "But the ancient flooded citadel offered several research possibilities for the girls. They were all taking notes in the small notebooks Tails gifted to them."
    "Suddendly, a strange portal appeared in the middle of the zone!"
    show monika 1c at t33 zorder 3
    show portal genesisportal at t32 zorder 2
    show amy amy06 at t31 zorder 3
    amyR "What kind of strange thing is this?"
    m 2d "According to the files I hacked from Eggman's computers, those things are called Genesis Portals."
    m 4d "The Genesis Portals were created after the appearance of the Phantom Ruby, and that portals can create connections to another worlds or dimensions."
    m 9l "But if you ask me, I'm a little scared of taking the portal, you know?"
    amyR amy08 "Me too, Monika. I agree with you. But let's ask Rookie. What does our soldier think?"
    mc "Well..."
    mc "I say that we must... Take the Portal!"
    $ enterPortal = True
    mc "...follow this portal to where it take us! Who knows if we can find someone that help us out there?"
    mc "And because we are all stressful about Sayori and stuff, I decided that we will free the stress making poems."
    mc "The best poem will select the girl that will go with me to the portal!"
    m 11n "I'm still not suuuuuure about this, but I wanted to write from sometime ago, so I can't refuse."
    mc "Can you give me the honours then, miss President?"
    mc "But my Wispon is jammed right now! How we will made our poems?"
    amyR "Hey Rookie! Look! There is an Starpost over there!"
    show amy at thide zorder 1
    show monika at thide zorder 1
    show portal at thide zorder 1
    hide amy
    hide monika
    hide portal
    show pictures starPost at t32 zorder 2
    show natsuki 1a at t33 zorder 3
    show ghostnatsuki gNatsu1 at t31 zorder 3
    n "A REAL STARPOST!!!! Those are so pretty!!!"
    g "And it has some weird stars surrounding it."
    mc "Yeah! the starpost make a ring of stars to go to bonus dimensions when we carry a lot of rings."
    mc "And since we have [persistent.ringCount] rings, obviously it created a star ring."
    mc "MAYBE THE STARPOST SENSED OUR WORRIES AND CREATED A PORTAL FOR ACCESING MILESPOEM!!!"
    g "Then we must not waste time! Monika, your catchphrase!!!"
    show ghostnatsuki at lhide zorder 1
    hide ghostnatsuki
    show monika 5b at l31 zorder 3
    m "FOR THE LAST TIME... I DON'T HAVE A LOT OF CATCHPHRASES EXCEPT ONE!"
    m "Wait..."
    m 3b "Oh yeah! That catchphrase, sorry!"
    m 4b "Okay everyone! It's time to share your best poems between us!"
    m 5b "IT'S POEM TIME!"
    stop music fadeout 2.0
    scene bg tcPoem
    with dissolve_scene_full
    pause 3.0
    return


label chapter4_mid:
    #Call exclusive scene
    if enterPortal == True:
        if poemwinner[3] == "monika":
            $ portalName = "Miku"
            $ nextscene = "monika" + "_exclusive_" + "3"
            call expression nextscene
        elif poemwinner[3] == "sayori":
            $ portalName = "SCP"
            $ nextscene = "ghost" + "_exclusive_" + "3"
            call expression nextscene
        elif poemwinner[3] == "natsuki":
            $ portalName = "Term"
            $ nextscene = "natsuki" + "_exclusive_" + "3"
            call expression nextscene
        else:
            $ portalName = "Undertale"
            $ nextscene = "yuri" + "_exclusive_" + "3"
            call expression nextscene

    #After exclusive scene, we go back to chapter
    scene bg hidrocity
    with dissolve_scene_half
    "Meanwhile Rookie and the Doki girl were travelling with the Portal, things happened in Hydrocity Zone."
    "Let's check what happened..."
    "Sliding through pipes, the team arrived to a completely submerged area."
    "Dr. Eggman was waiting for them in a submarine, heavily protected and with a huge propeller at the front."
    if persistent.packagedMusic == True:
        play music eggmanPCKG
    else:
        play music eggmanMusic
    show eggman eggman02 at t11 zorder 2
    egg "Oh, ho ho ho. The annoying rodent and his girly fan club have arrived, but don't worry, you will not last long here anyways."
    egg "Activating the Laundro Mobile, my powerful submarine!!!!"
    "The mad Doctor activated his submarine, and began to approach the heroes, while the propeller generated a current of air that dragged them backwards."
    "As they moved through, spiked structures were released from the walls. Also, Eggman placed grenades on the route."
    "Again, as a lack of a battle system, I can tell you the team won against Eggman, but he had an ace under his sleeve."
    "The current of water drags the team towards a kind of deep pool with a pillar in the middle, which fills with water."
    "Eggman appears with another machine that has rotating turbines. Sonic recognized it immediately…"
    scene bg hidrocity_Boss
    show eggman eggman02 at t21 zorder 2
    show sonic sonic07 at t22 zorder 2
    sth "Hey! I've beaten that damned robot before!!!"
    sth "Where's your creativity, fatass?"
    egg "The last time this robot was autonomous and a beta, but now it is under my control, and I'll make sure you drown here, pesky rodent!"
    "The robot activated and it created a rising spinning current, using the pillar and a good demonstration of kinetic energy."
    sth "We are doomed here if we can't attack! Only a miracle can save us now!!!!"
    mc "THE MIRACLE IS HERE, EVERYONE!!!!"
    if portalName == "Miku":
        play music mikuPortal
        show sonic at lhide zorder 1
        hide sonic
        show eggman eggman04 at t32 zorder 3
        show miku mikuSprite at l31 zorder 3
        show monika 5b at l33 zorder 3
        mik "HATSUNE MIKU TO THE RESCUE!!!"
        mik "EVERYONE SING WITH MY HARMONIOUS VOICE!!! LET'S GO!!! FOLLOW THE RYTHM OF THE TUNE!!!"
        mik "SONIC LYRIC DRIVER ATTACK"
        m "AND I WILL ATTACK YOU WITH MY NEW SHINY WISPON TOO, EGGFAT! THIS IS FOR SAYORI!!!!"
        "A blue ray attack from Miku and the blue cubes attack from Monika's Wispon destroyed the machine easily. Sonic and our friends were saved again!"
        egg eggman05 "NO NO NO NO NO NO. THIS WILL NOT BE THE END, HEDGEHOG AND YOUR STUPID LITERATURE HAREM!!!"
        egg "I WILL DESTROY YOU WITH YOUR OWN ROBOT FRIEND!!! WAIT AND YOU WILL SEE!!!"
        show eggman at thide zorder 1
        hide eggman
        egg "I HATE THAT HEDGEHOG!!!!!!"
        scene bg hidrocity
        show sonic sonic14 at t32 zorder 3
        show miku mikuSprite at t31 zorder 3
        show monika 5a at t33 zorder 3
        sth "Hey! Monika, Rookie, and Miku! Thanks for saving us!"
        mik "Another world saved with Miku's purest songs again!!! And everyone cheers and claps!!!"
        m "I told you that you will soon see the power of Monika. That's why I'M the President."
        m 4b "Let's move to the next zone, everyone! Sayori still needs us!"
        mc "LET'S DO IT TO IT, EVERYONE!"
        "MOD AUTHOR'S NOTE: Download the Crash Fever game on the App Store and Google Play."
        "It has cool visuals, a fun play style and catchy music, like this one!"
        "If you play multiplayer 10 times as a new user, you will get enough of the premium currency (Polygons) to pull a gacha and get awesome units!"
        "If you enter author's code, 449 938 462, you will receive extra polygons too! Give it a try :D."
        "Let's go back to the story..."
        show miku at thide zorder 1
        hide miku
        show monika at thide zorder 1
        hide monika
        show sonic sonic14 at t32 zorder 3
        show boss2 metalMonika at h31 zorder 3
        show natsuki 1r at t33 zorder 3
        "Suddendly, Metal Monika appeared! Again!"
    elif portalName == "SCP":
        play music scp682Portal
        show sonic at lhide zorder 1
        hide sonic
        show eggman eggman04 at t32 zorder 3
        show scp scpLizard682 at l33 zorder 3
        show ghostnatsuki gNatsu2 at l31 zorder 3
        liz "HEY... PUNY... WEAKLING HUMAN!!!"
        liz "IT'S TIME EVERYONE HERE KNOWS WHY I'M THE HARD TO DESTROY REPTILE!"
        liz "I WILL FEAST WITH YOUR PUNY MACHINE'S PARTS!!!"
        g "AND I WILL ATTACK YOU WITH MY NEW SHINY WISPON TOO, PIECE OF SHIT! FOR THE WORLD!!!"
        "The blue cubes attack from Ghost's Wispon separated the machine, and then SCP-682 separated Eggman's Egg Mobile from the machine, and sended him to fly away."
        "Sonic and our friends were saved again!"
        egg eggman05 "NO NO NO NO NO NO. THIS WILL NOT BE THE END, HEDGEHOG AND YOUR STUPID LITERATURE HAREM!!!"
        egg "I WILL DESTROY YOU WITH YOUR OWN ROBOT FRIEND!!! WAIT AND YOU WILL SEE!!!"
        show eggman at thide zorder 1
        hide eggman
        egg "I HATE THAT HEDGEHOG!!!!!!"
        scene bg hidrocity
        show sonic sonic14 at t32 zorder 3
        show scp scpLizard682 at t33 zorder 3
        show ghostnatsuki gNatsu2 at t31 zorder 3
        sth "Hey! Ghost, Rookie, and... that thing. Thanks for saving us!"
        liz "You are that thing everyone was saying to me? I'm suppose you are... Sonic."
        liz "Even if you are a disgusting living being, you are a friend of Rookie and Ghost, and SCP-682 is a lizard of word."
        g "See Rookie? Calling the Invincible Lizard was the best idea ever, after all! And my dream come true!"
        liz "YOU GO TO SAVE YOUR WEAKLING FRIEND! I WILL DESTROY SOME OF THAT EGG SHAPED PUNY HUMAN'S BASES!"
        liz "That will be a good sport, and a source of food, in any case."
        sth "Just make sure to NOT eat the animals after you destroy the robots, ok?"
        mc "Let's move to the next zone, everyone! Sayori still needs us!"
        mc "LET'S DO IT TO IT, EVERYONE!"
        "MOD AUTHOR'S NOTE: This is an easter egg to promote the awesome mod Doki Doki Lost Control!"
        "In this mod, the beloved Dokis will form part of the SCP Foundation! It will be an amazing and thrilling adventure."
        "Search the Lost Control (DDLC Project) Discord and give the developers and artists a big hug!"
        "Let's go back to the story..."
        show scp at thide zorder 1
        hide scp
        show ghostnatsuki at thide zorder 1
        hide ghostnatsuki
        show sonic sonic14 at t32 zorder 3
        show boss2 metalMonika at h31 zorder 3
        show natsuki 1r at t33 zorder 3
        "Suddendly, Metal Monika appeared! Again!"
    elif portalName == "Term":
        play music moddersPortal
        show sonic at lhide zorder 1
        hide sonic
        show eggman eggman04 at t32 zorder 3
        show oneterm termHappySprite at l33 zorder 3
        show natsuki 4e at l31 zorder 3
        onT "I'M IN A SONIC AND DDLC GAME!!! OMG"
        onT "FOR THE POWER OF THE DDMC DISCORD AND THE HEART OF THE CARDS!!!"
        onT "BLUE EYES TOON DRAGON, ATTACK!!!!"
        n "AND I WILL ATTACK YOU WITH MY NEW SHINY WISPON TOO, MOTHERFUCKING! I WILL BEAT THE SHIT OUT OF YOU!!!!"
        "The blue cubes attack from Natsuki's Wispon and the big mothafuckin' ray of the Dragon destroyed the machine easily. Sonic and our friends were saved again!"
        egg eggman05 "NO NO NO NO NO NO. THIS WILL NOT BE THE END, HEDGEHOG AND YOUR STUPID LITERATURE HAREM!!!"
        egg "I WILL DESTROY YOU WITH YOUR OWN ROBOT FRIEND!!! WAIT AND YOU WILL SEE!!!"
        show eggman at thide zorder 1
        hide eggman
        egg "I HATE THAT HEDGEHOG!!!!!!"
        scene bg hidrocity
        show sonic sonic14 at t32 zorder 3
        show oneterm termHappySprite at t33 zorder 3
        show natsuki 4z at l31 zorder 3
        sth "Hey! Thanks for saving us!"
        sth "You are the best, Rookie! You made a plan with my heroine!!!"
        sth "Being saved by Natsuki is the best thing ever!!!"
        n "I told you that you will soon see the power of Natsuki. For my friends and my hero, I will do whatever to help!!!"
        n "And don't forget the help of this awesome guys from the alternate dimension's Literature Club!"
        onT "I'm super happy of saving someone important!!!!"
        onT "Take that, Natsuki's haters!"
        n 4v "AND I HOPE EGGMAN AND MONIKA UNDERSTAND NOW THAT MANGA IS LITERATURE!!!"
        n 1r "Now please let's focus on saving Sayori and my now girlfriend, Yuri, please..."
        sth "LET'S DO IT TO IT, THEN, EVERYONE!"
        sth "Time to keep saving the world, at Sonic's style!"
        "MOD AUTHOR'S NOTE: This is a easter egg to promote the awesome mod Doki Doki Modders Fantasy!"
        "In this mod, a lot of friendly modders and personalities from the Modding Community of DDLC will take part in the Literature Club!"
        "Search the DokiDokiModdersFantasy Discord and give the developers and artists a big hug!"
        "Let's go back to the story..."
        show oneterm at thide zorder 1
        hide oneterm
        show sonic sonic14 at t32 zorder 3
        show boss2 metalMonika at h31 zorder 3
        show natsuki 1r at t33 zorder 3
        "Suddendly, Metal Monika appeared! Again!"
    else:
        play music himFrisk
        show sonic at lhide zorder 1
        hide sonic
        show eggman eggman04 at t32 zorder 3
        show him frisk at l33 zorder 3
        show natsuki 4e at l31 zorder 3
        him "Hey you, leave Natsuki and Rookie's friends alone!"
        "Frisk created a red sword and shield and ran into Eggman's machine."
        him "This is for the friendship!"
        n "AND I WILL ATTACK YOU WITH MY NEW SHINY WISPON TOO, MOTHERFUCKING! I WILL BEAT THE SHIT OUT OF YOU!!!!"
        "The blue cubes attack from Natsuki's Wispon and the power of Frisk's sword destroyed the machine easily. Sonic and our friends were saved again!"
        "And I feel compeled to say: \"You are filled with DETERMINATION!\", for some reason!"
        egg eggman05 "NO NO NO NO NO NO. THIS WILL NOT BE THE END, HEDGEHOG AND YOUR STUPID LITERATURE HAREM!!!"
        egg "I WILL DESTROY YOU WITH YOUR OWN ROBOT FRIEND!!! WAIT AND YOU WILL SEE!!!"
        show eggman at thide zorder 1
        hide eggman
        egg "I HATE THAT HEDGEHOG!!!!!!"
        scene bg hidrocity
        show sonic sonic14 at t32 zorder 3
        show him frisk at t33 zorder 3
        show natsuki 4z at l31 zorder 3
        sth "Hey! Thanks for saving us!"
        sth "You are the best, Rookie! You made a plan with my heroine and escaped from Yuri's portal!!!"
        sth "Being saved by Natsuki is the best thing ever!!!"
        n "I told you that you will soon see the power of Natsuki. For my friends and my hero, I will do whatever to help!!!"
        n "And don't forget the help of this awesome guy!"
        him "I'm super happy! Helping people is part of my nature!"
        him "Let me text Mom to tell her that I'm ok, she got extremely worried!"
        him "{i}Hey Mama Toriel: I'm fine! I will stay here a little to help Natsuki's friends, ok? Love you! Frisk.{/i}"
        him "I'm ready!"
        sth "Then it's time to keep saving the world, at Sonic's style!"
        show him at thide zorder 1
        hide him
        show sonic sonic14 at t32 zorder 3
        show boss2 metalMonika at h31 zorder 3
        show natsuki 1r at t33 zorder 3
        "Suddendly, Metal Monika appeared! Again!"
    
    stop music fadeout 2.0
    play music t9
    m "METAL. TRASHY. ONLINE! AND TALKING TO THE ENEMIES!!"
    m "OPERATING SYSTEM AND FUNCTIONS WORKING CORRECTLY!!!"
    m "I WAS REBUILT BY OUR LOVELY BOSS YURI!!!"
    m "I'M DOING THIS ON MY OWN, SONIC AND ROOKIE."
    m "BOSS IS NOT ACTING ALRIGHT. SHE SEEMS MORE ANGRIER AND STRANGE THAN BEFORE."
    m "SHE DISMISSED METAL NATSUKI AND ME, AND SHE IS ACTING VERY COLDLY TOWARDS NATSUKI AND SAYORI."
    m "SHE DIDN'T REMEMBER THE PRETTY DANCE NATSUKI AND HER HAD, AND SHE IS NOT WORRIED ABOUT HOW TO HELP HER FORMER FRIEND."
    m "THE BOSS WASN'T LIKE THAT. EVEN IF SHE MADE ME AS A JOKE OF HER PRESIDENT, SHE STILL CARED ABOUT MONIKA AND THE REST."
    m "BUT NOW SHE FEELS VERY DIFFERENT..."
    m "I HAD TO COME HERE AND ASK YOU FOR HELP, AND JOIN YOUR TEAM. I DISABLED ALL MY GPS FUNCTIONS, SO YURI WILL NEVER KNOW WHERE I AM."
    mc "Trashy: Yuri is being controlled by the Phantom Ruby, so that's why she is out of character for you."
    mc "After that and Sayori's transformation, we are working harder than ever on finishing these zones."
    n 2u "That's why I keep insisting on moving and help our friends!"
    n "Knowing that Yuri is being controlled and not acting on her own after her precious confession... it pains me!"
    n "It's like everything I love is being forced out of me: my good relationship with Papa before that horrible week, the Club, my hobbies, Sayori... and now my girlfriend..."
    sth sonic13 "Robot, welcome to the Resistance."
    sth "It pains me to see Natsuki crying like that. I PROMISE WE WILL SAVE OUR WORLD, YOUR WORLD AND ALL OUR FRIENDS."
    sth "Let's move, everyone. No time to waste."

    pause 1.0
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    "You got 250 rings for ending Chapter 4!"
    "You got 500 rings for getting a Chaos Emerald!"
    "The character that arrived from the portal gifted you 10000 for your choice!"
    "While you were in the portal, Sonic and company recollected 30000 rings. Sonic gives all of them to you."
    play sound Ring
    $ persistent.ringCount += 40750
    "You now have [persistent.ringCount] Rings!\n{i}Click to continue...{/i}"
    call screen confirm("You have unlocked a special poem.\nWould you like to read it?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + "6" from _call_expression_48
        scene black with Dissolve(1.0)
    else:
        pass
    
    return

    