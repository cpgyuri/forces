image noface1:
    topleft
    xtile 10 ytile 10
    block:
        block:
            choice:
                "images/sayori/noface1.png"
            choice:
                "images/sayori/noface1b.png"
        block:
            choice:
                0.075
            choice:
                0.3
            choice:
                0.4
            choice:
                0.5
            choice:
                0.6
        repeat
    
image noface2:
    "images/sayori/noface2.png"
    xalign 0.95 yalign 0.47

# How long the player has to make a choice in timeout seconds.
default timeout = 15.0

# The height position of the gauge. If the gauge is clipping through the choice box,
# you can set it lower than 400
define gauge_ypos = 400

# The label the player is sent to if they fail to make a choice in the time
# allotted. If None, the timeout is disabled.
default timeout_label = None

image timer_gauge:
    "mod_assets/gauge-legacy.png"
    truecenter
    ypos gauge_ypos

image timer_gauge_green:
    "mod_assets/gauge-green.png"
    truecenter
    ypos gauge_ypos
    gauge_timeout

image timer_gauge_red:
    "mod_assets/gauge-red.png"
    truecenter
    ypos gauge_ypos
    gauge_timeout_red

transform gauge_timeout:
    alpha 1.0
    xzoom 1.0
    parallel:
        linear timeout xzoom 0.0
    parallel:
        linear (timeout * 0.9) alpha 0.0

transform gauge_timeout_red:
    xzoom 1.0
    linear timeout xzoom 0.0

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    if timeout_label is not None:
        
        add "timer_gauge_red"
        add "timer_gauge_green"
        add "timer_gauge"

        timer timeout action Jump(timeout_label)

label chapter5start:
    scene bg tcMirageSaloon
    with dissolve_scene_full
    stop music
    pause 2.0
    $ quick_menu = False
    scene white
    show noface1
    "You must know already what you have to do! Do it!"
    play music drowning
    $ timeout_label = "sayori_ignore"
    menu:
        "What will you do?"
        "Help her":
            stop music
            jump sayori_help
        "Ignore":
            stop music
            jump sayori_ignore
    return

label sayori_help:
    $ timeout_label = None
    if renpy.loadable("../characters/sayori.chr"):
        $ persistent.sayori_helped = True
        mc "There is a bright light ocurring!\nI can sense something with my Wispon!"
        "The white light shines stronger...!"
        show mirageSaloon_glitch3
        "You reached out to the bright light and it seems to be a person there. You can't remember that person, to be honest."
        "... Suddendly, within the depths of the white void, you see that someone more clearly. She is wet and surrounded by rainclouds!"
        " And her Soul is starting to resonate with your soul and your Wispon, and to the rythm of a song!"
        "Suddendly, a poem appears in front of you...!"
        call showpoem(poem_s5)
        "Now everything is clear! You remember fully the person in front of you!"
        mc "It's Sayori!!!"
        play music yuriLastStand
        $ s_name = "Sayori"
        s "Is somebody there?"
        s "This raincloud is too strong!"
        mc "Sayori, I'm going!!!"
        "..."
        show mirageSaloon_glitch5
        mc "I'm here, Sayori!!! I'm happy to see you!"
        s "Rookie! Is that you?"
        s "My soul... my memories... my own being..."
        s "Are trapped inside Metal me."
        s "But, somehow, you reached to my own soul, thank you."
        s "Despite what Metal me says, don't believe her. The rainclouds are stronger."
        s "I'm worried about MC, about Monika and Natsuki, about Yuri... about you and your team."
        s "But seeing you here... it conforts my soul."
        s "I will help you in advance. First, there is this song, it's one of my favourites. Let me concentrate..."
        show honey djHoney at l31 zorder 5
        dj "Hey! I can reach Sayori's soul too! If I'm here, it's because Sayori is trying to share the song's name with you!"
        dj "... Hmmm..."
        dj "Gotcha! Sayori's soul is resonating with the rythm of {i}Markus Gardeweg feat. Michael Feiner - Fairplay (Let There Be Love) (Radio Edit){/i}!"
        s "Please, Honey, keep this secret!"
        dj "Your secret is secure, my darling! Rookie will help you, I swear!"
        show honey at lhide zorder 1
        hide honey
        s "For some reason I can't reach my beloved MC's soul. Is everything alright with him?"
        mc "MC got spaced out after you revealed yourself as a Metal robot, but now he is better!"
        mc "We let him on our Headquarter and he is recovering. Amy is checking on him, and when he feels better, those two will be back in action!"
        mc "He is very worried of you, I can swear! I think that his recovering will be faster if he knows about this."
        s "Yes! Please tell MC that I love him! He is the only one I allow, besides Honey, to know that I'm still here!"
        s "By the way, Yuri is trying to screw you up a lot this time, using that Phantom Ruby, but I know I can help! It's my desire!"
        s "I will try my best to stop most of Yuri's screwed stuff, keep being strong, [player]!"
        s "I will wait patiently that all of you rescue me, ok? Please support Monika and Natsuki. And give Tails a hug from me."
        s "Time to go back!"
        "Another bright light...!"
        $ s_name = "Metal-Sayori"
        jump chapter5
    else:
        $ timeout_label = None
        $ persistent.sayori_helped = False
        g "What? You decided to not help Sayori? Shame on you, piece of shit, shame on you!"
        jump chapter5

label sayori_ignore:
    stop music
    $ timeout_label = None
    $ persistent.sayori_helped = False
    g "What? You decided to not help Sayori? Shame on you, piece of shit, shame on you!"
    jump chapter5

label chapter5:
    $ quick_menu = True
    scene bg mirageSaloonbg
    with dissolve_scene_full
    if persistent.packagedMusic == True:
        play music mirageSaloonPCKG
    else:
        play music mirageSaloon
    "..."
    "We felt a weird sensation..."
    if persistent.sayori_helped == True:
        "But I feel the presence of our friend Sayori also! Thanks to her, we will do this!"
    "Now, we are flying through Mirage Saloon!"
    "Mirage Saloon, an unexplored area of Sonic's home island, had everything needed to make a cowboy movie!"
    "It has an extended desert, mountains, rock formations, cactus, sand, totems made by ancient indigenous populations and more sand."
    "The girls and I are flying over the area on Sonic's plane, the Tornado Mk.1."
    "The Tornado is piloted by Tails since the day he repaired the engine and added pieces of professional engineering, such as a turbine to increase the flight time."
    "Monika, Natsuki and me are on the Tornado, while Ghost fly around us, because... well, she is a ghost."
    show monika 4b at t21 zorder 3
    show natsuki 5g at t22 zorder 3
    m "How awesome is that you have a plane, mr. Tails!"
    mtp "Oh yeah! Since Sonic and I have been friends for so long, he lets me use his plane."
    mtp "I'm a technology enthusiast, so I have built many advances for the Tornado, as a thank you for Sonic's help."
    mtp "And it's cool to have you testing it! The fresh wind on the face is an spectacular sensation."
    n 5h "But let's not forget why we are here! We need to rescue my girlfriend, and Sayori!"
    n 5n "I wish things were a bit different for my friends, so everyone would be at the same side."
    mc "Don't worry Natsuki! We will rescue Sayori and Yuri, we promised it!"
    kte "And also, I'm preparing an awesome plan to invade Eggman's headquarters! It will be called Operation BigWave!"
    m 1k "It's good to see that everyone is having awesome ideas for helping my friends!"
    m 2f "I wish to be more helpful for everyone. My leadership skills are still lacking."
    m "If I was more careful with Sayori and confronted Eggman for real, this would hadn't happened."
    if persistent.sayori_helped == False:
        show mirageSaloon_glitch1 zorder 99
        $ style.say_dialogue = style.edited
        play music saloonGlitched
        m "But that doesn't matter. Sayori is annoying."
        m "She was my most direct competition for my love to the player."
        m "So I had to ramp up her depression A LOT, and the magic did it's job!"
        m "I can't believe she did everything I told her in her mind!"
        m "I didn't cried at the death of that stupid crybaby bitc..."
        hide mirageSaloon_glitch1
        if persistent.packagedMusic == True:
            play music mirageSaloonPCKG
        else:
            play music mirageSaloon
        $ style.say_dialogue = style.normal
        m 12s "WHAT? I DIDN'T SAID THAT!!!! THAT IS NOT WHAT I THINK OF SAYORI!!!!"
        m "Rookie, what is happening????"
        show mirageSaloon_glitch2 zorder 99
        $ style.say_dialogue = style.edited
        play music saloonGlitched
        mc "I don't fucking care!"
        mc "All of you are a nuisance for my mission!"
        mc "I'm sick of everyone calling me Rookie, I have a name!"
        mc "My name is [player], the King, the Pro of the Team, the Number One!"
        mc "And I will prove it when i beat the motherfucking ass of that asshole Soni..."
        hide mirageSaloon_glitch2
        if persistent.packagedMusic == True:
            play music mirageSaloonPCKG
        else:
            play music mirageSaloon
        $ style.say_dialogue = style.normal
        mc "The fuck? This is not what I think of all of you, girls! I'm sorry!!!"
        n 4f "WHAT IS HAPPENING WITH ALL OF YOU???"
        mtp "Guys at the Resistance Headquarters, we are having a problem with glitches and stuff here!"
        n "I can't believe this!"
        n "The only thing that you must remember is..."
        show black zorder 5
        show n_glitch_head zorder 6:
            xpos 630 ypos -50 zoom 2.0
        $ style.say_dialogue = style.edited
        $ currentpos = get_pos()
        play music "<from " + str(currentpos) + " loop 0>mod_assets/specialMenu.ogg"
        n "I'm an useless piece of shit."
        n "My Papa beat the shit out of me everyday at my home, just for breathing and exist."
        n "I read that stupid manga just for hiding my own problems."
        n "I'm an insecure, annoying and anorexic brat."
        n "I'm so weak that I even let my Papa assaulted me a LOT of times."
        n "That's why I had to find his special gun and stoping this by killing hi..."
        $ style.say_dialogue = style.normal
        hide black
        hide n_glitch_head
        if persistent.packagedMusic == True:
            play music mirageSaloonPCKG
        else:
            play music mirageSaloon
        $ style.say_dialogue = style.normal
        show monika 12s at t31 zorder 3
        show sonic sonic07 at t32 zorder 4
        show natsuki 42f at t33 zorder 3
        n "No way..."
        n "It wasn't supposed for any of you to know... my shit... this way."
        sth "Tails, let's hurry up! This is getting out of control and I don't like it."
        mtp "Sure Sonic, I'm worried about this glitches damaging the self steem of Rookie and the girls."
    else:
        show mirageSaloon_glitch1 zorder 99
        $ style.say_dialogue = style.edited
        play music saloonGlitched
        m "But that doesn't matter. Sayori is annoying. I can't believe she is so stupi..."
        play music yuriLastStand
        s "YURI, STOP THIS!!!"
        mc "Sayori!!!"
        y "NO FUCKING WAY!!! SAYORI??? YOU ARE SUPPOSED TO BE DEAD!!!"
        y "NO... WAIT!!! STOP SCREWING WITH MY ILLUSIONS!!!"
        hide mirageSaloon_glitch1
        show mirageSaloon_glitch5 zorder 99
        $ style.say_dialogue = style.normal
        s "Rookie!"
        s "I'm using the communication system of the metal version of me to reach your Miles Electric!"
        s "Thank you for reaching my soul!!!"
        s "As I promised, I'm able to stop some of Yuri's deranged stuff!"
        s "Please continue your mission and save the world and my friends!!!"
        s "The rainclouds will go out soon if you keep doing your good deeds!"
        mc "Sayori! I promise to free you from your robotic prison! Thank you!"
        hide mirageSaloon_glitch5
        show monika 12s at t31 zorder 3
        show sonic sonic11 at t32 zorder 4
        show natsuki 42f at t33 zorder 3
        "YES! MIRAGE SALOON FEELS NORMAL NOW! THANK YOU SO MUCH, SAYORI!"
        mc "Hey! Suddendly I feel comforted and warm!"
        m "Yeah, Rookie! And emotional too! Did all of you felt something special?"
        n "Yeah... like... if Sayori was here, comforting and cheering us... I can't stop crying for her! I want her back!"
        sth "I felt that sensation too, Rookie! Tails, we need to hurry up!"
        mtp "Sure thing, Sonic! I have a good feeling too, like if I had received a hug from someone! Let's keep going!"
    "Suddendly..."
    stop music fadeout 2.0
    if persistent.packagedMusic == True:
        play music heavyMagicianPCKG
    else:
        play music heavyMagician
    "A group of robotic turtles was approaching quickly to our position!"
    show sonic at thide zorder 1
    hide sonic
    show boss4 heavyMagician at h32 zorder 4
    play sound magicianHat
    "Among the group of turtles, a yellow robot, dressed like an elegant magician, greeted us in a friendly way using her hat."
    "This robot was Heavy Magician, one of the transformed EggRobos by the Phantom Ruby, specialized in using magic and creating illusions."
    "And sure thing, she had a trick under her sleeve... or in this case, her hat."
    "She... entered her hat, and then, with a sound, made appear... Monika?"
    show boss4 at thide zorder 1
    hide boss4
    play sound magicianTrick 
    show glitch illusionMonika at h32 zorder 4
    m 2q "My godness, everything bad in this game is represented by me. This is amazing."
    n 2p "WATCH OUT, EVERYONE! THAT MONIKA IS SHOOTING SOMETHING..."
    "Too late! The missile of that Monika did hit the Tornado, and catapulted our plane to the ground!"
    scene bg magicianRoom
    "The plane is destroyed in an explosion after reaching the ground, and we land in a kind of improvised stage."
    "The scenery has a big curtain, with a box in the middle of it, that had drawings of Heavy Magician."
    show boss4 heavyMagician at h32 zorder 4
    show monika 12h at t31 zorder 3
    show natsuki 4o at t33 zorder 3
    "The robot opens the box from the inside, greeting us by taking off her hat, and then she closes the box."
    mc "Watch out girls! Get ready. Anything can come out from that box, be ready to attack if needed!"
    show boss4 at thide zorder 1
    hide boss4
    if persistent.packagedMusic == True:
        show honey djHoney at l31 zorder 5
        if persistent.sayori_helped == True:
            dj "SORRY! I was feeling so warm after Sayori's help, that I almost forgot to announce the song!"
            dj "Now playing: {i}Alesso - Anthem{/i}, the song of the Hard Boiled Heavies!"
        else:
            dj "SORRY! The game glitched up a lot, I couldn't make myself appear to announce the song!"
            dj "Before another creepy stuff happen, now playing: {i}Alesso - Anthem{/i}, the song of the Hard Boiled Heavies!"
        show honey at lhide zorder 1
        hide honey
    play sound magicianBox
    "The box started to contort itself and making sounds!"
    "And then something appeared!"
    play sound magicianTransform
    show glitch illusionMonika at t11 zorder 4
    show monika at thide zorder 1
    hide monika
    show natsuki at thide zorder 1
    hide natsuki
    "It's the Glitched Shadow Monika!"
    "Shadow Monika carried a laser gun, and she was shooting laser bullets while jumping from one side of the stage to the other."
    "The girls didn't wanted to move or attack, so Tails took the initiative."
    show glitch illusionMonika at t22 zorder 4
    show tails tails07 at l21 zorder 4
    mtp "I'm not scared of you! Twin-tails spin attack!"
    "Tails suspected and decided to jump towards her with her trademark spinning tails attack!"
    "He hitted the illusion of Monika and the robot appeared again, getting a hit!"
    show glitch at lhide zorder 1
    hide glitch
    show tails at lhide zorder 1
    hide tails
    "Heavy Magician went again to her box."
    m "Oh, that cheating robot is using illusions to attack us! Natsuki, we must be more careful next time!"
    play sound magicianBox
    "The box started to contort itself and making sounds a second time!"
    play sound magicianTransform
    if persistent.sayori_helped == False:
        show black zorder 5
        show s_glitch_head zorder 6:
            xpos 630 ypos -50 zoom 2.0
        s "WHY ALL OF YOU LET ME DIE IN STARDUST SPEEDWAY???"
        s "I WILL DESTROY ALL OF YOU!!!"
        s "DID YOU LISTEN TO ME???"
        s "ALL"
        s "OF"
        s "YOU!"
        s "Starting with that motherfucker Monik...{nw}"
        hide black
        hide s_glitch_head
    else:
        s "I WILL NEVER SAY THE THINGS YOU ARE FORCING METAL SAYORI TO SAY, YURI!"
        "Sayori is helping again! Probably that was another mean illusion from Yuri!"
    show glitch sayoriGhost at t11 zorder 4
    g "HEHEHE! HAHAHAHA! HAHAHAHAHAHA!"
    "It's a Ghost Sayori, with a very angry expression!"
    show glitch sayoriGhost at t22 zorder 4
    show natsuki 4o at l21 zorder 4
    "The Ghost Sayori started to launch raincloud bombs everywhere, creating chains of explosions!"
    mtp "Be careful, she's throwing something!"
    "Natsuki decided to attack her."
    n "You are not Sayori! Eat my Wispon!"
    "Natsuki launched a fire missile using the Fire Wispon. The missile impacted the Ghost Sayori!"
    show glitch at lhide zorder 1
    hide glitch
    show natsuki at lhide zorder 1
    hide natsuki
    "The robot received another hit and went to her box again!"
    play sound magicianBox
    "The box started to contort itself and making sounds a third time!"
    play sound magicianTransform
    show glitch sayoriRed at t11 zorder 4
    "It's another Sayori illusion! This time is bloody red and with a sad expression!"
    g "Rainclouds, happy thoughts, rainclouds, happy thoughts, rainclouds, happy thoughts..."
    show glitch sayoriRed at t22 zorder 4
    show sonic sonic07 at l21 zorder 4
    sth "Your rainclouds are as fake as you! Attack!"
    "The Sayori illusion started to pound the ground. Her rainclouds started to fall from the ceiling, trying to impact us!"
    "Sonic ran to Sayori and launched at her with a strong homing attack!"
    show glitch at lhide zorder 1
    hide glitch
    show sonic at lhide zorder 1
    hide sonic
    "The homing attack impacted her and launched the robot to her box. The robot detransformed while the box was closing."
    play sound magicianBox
    "The box started to contort itself and making sounds a fourth time!"
    show darkred zorder 99:
        alpha 0.0
        easein 4.0 alpha 1.0
    stop music fadeout 2.0
    "Uh? The stage darkens in a red tone and the music stops, then changes to a cheery tune that goes creepy in a record time."
    n "Oh no, don't tell me is THAT illusion..."
    play sound magicianTransform
    $ renpy.music.play("<loop 4.444>bgm/5_ghost.ogg")
    $ style.say_dialogue = style.edited
    show natsuki 1g at t11 zorder 3
    n "Sonic..."
    n "Why didn't you come to play with me today?"
    n 1m "I was waiting for you. I was waiting for a long time."
    n "It was the only thing I had to look forward to today."
    n "Why did you ruin it?"
    n "Do you like Yuri more?"
    n ghost1 "I think everyone're better off {i}associating{/i} with her."
    show n_rects_ghost1 zorder 4
    show n_rects_ghost2 zorder 4
    show n_rects_ghost3 zorder 4
    show natsuki_ghost_blood zorder 5
    n "Are you listening to me, Sonic?"
    n "Yuri will be your Queen now."
    n "That should be obvious by now. Let she win this battle already!"
    n "While she is doing her job, just play with me instead. Okay?"
    n "You don't hate me, Sonic, do you?"
    n "Do you hate me?"
    n "Do you want to make me go home crying?"
    n "Don't ruin my happiness, please."
    n "Just play with me instead."
    n "Play with me."
    n "Play with me and surrender."
    n "Play with me AND SURRENDER."
    stop music
    hide n_rects_ghost3
    n ghost2 "SURRENDER!!!"
    n "SURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDERSURRENDER"
    $ style.say_dialogue = style.normal
    show sonic sonic11 at l31 zorder 5
    sth "Sorry Natsuki. I don't know what are you talking about."
    sth "But let's make it clear I promised everyone to save this world and the girls own world."
    sth "So I will never surrender, ok?"
    mtp "Sonic! That Natsuki is an illusion! Watch out!"
    $ style.say_dialogue = style.edited
    n "OMG, CAN THE TWO OF YOU SHUT YOUR FUCKING MOUTHS AND SURRENDER ALREADY????"
    show sonic at lhide zorder 1
    hide sonic
    $ quick_menu = False
    pause 1
    play sound "sfx/crack.ogg"
    hide natsuki_ghost_blood
    hide n_rects_ghost1
    hide n_rects_ghost2
    show natsuki ghost3
    show n_rects_ghost4 onlayer front zorder 4
    show n_rects_ghost5 onlayer front zorder 4
    pause 0.5
    hide natsuki
    play sound "sfx/run.ogg"
    show natsuki ghost4 at i11 onlayer front
    pause 0.25
    window hide(None)
    hide natsuki onlayer front
    hide n_rects_ghost4 onlayer front
    hide n_rects_ghost5 onlayer front
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.3
    hide screen tear
    hide darkred
    show black zorder 5
    show n_glitch_head zorder 6:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    play music specialMenu
    n "Join the Yuri Empire, [player]. This is your last warning."
    n "And fucking tell your friend Sonic to surrender."
    n "He will never save you."
    n "He will never save anybody, [player]."
    n "He will never save his world"
    n "He will never save the Literature Club."
    n "HE WILL NEVER SAVE MEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE{nw}"
    $ style.say_dialogue = style.normal
    hide black
    hide n_glitch_head
    if persistent.packagedMusic == True:
        play music heavyMagicianPCKG
    else:
        play music heavyMagician
    $ quick_menu = True
    show boss4 heavyMagician at h11 zorder 4
    "Holy shit! We're still sweating from the scare that had just happened!"
    "The Heavy Magician appeared and showed us a sign that says:"
    "SORRY! THIS WAS NOT AN ILLUSION MADE BY ME!"
    "I THINK IS BETTER TO GO OUT! SO LONG, FOLKS!"
    show boss4 at thide zorder 1
    hide boss4
    play sound magicianBox
    "The Heavy Magician dissapeared, scared shitless."
    "AND SUDDENDLY THE MAGICIAN'S BOX STARTING TO CONTORT BY ITSELF!!!"
    play sound magicianTransform
    "Something is coming from the box..."
    show dark zorder 100
    with wipeleft
    play music hb
    show layer master at heartbeat
    show yuri yuriIllusion at h11 zorder 4
    "Oh no."
    kte "Hey, that's my line!"
    y "Hey!"
    y "It seems I didn't made myself clear."
    show yuri yuriIllusion at face(y=600) with dissolve
    y "I SAID THAT EVERYONE SHOULD SURRENDER!"
    m "Watch out guys and girls, that Yuri is making something!"
    "Raising her left arm, a gigantic plasma sphere began to form."
    "Tails tried to run to ram Yuri, still frightened by the previous illusion, but she blocked the way with pink crystal walls."
    "The size of the plasma sphere continued to increase."
    $ style.say_dialogue = style.edited
    y "DIE."
    $ style.say_dialogue = style.normal
    "We closed our eyes for the inevitable doom..."
    stop music fadeout 2.0
    scene bg magicianRoom
    with wipeleft_scene
    "CRASH!!! KABOOM!!! {i}falling noises{/i}"
    mc "What?"
    play music shadowAppears
    show shadow shadow03 at h11 zorder 3
    sha "Next time... try to make this a challenge, Yuri!"
    "OMG IT'S THE LEGENDARY LORD OF EDGYNESS HIMSELF, OW THE EDGE!!!{nw}"
    "OMG IT'S THE LEGENDARY SHADOW THE HEDGEHOG FROM THE G.U.N. FORCES!!! WHAT IS HE DOING HERE?"
    show shadow shadow03 at t21 zorder 3
    show yuri 3y2 at h22 zorder 3
    y "OMG IS THE LORD OF THE EDGYNESS HIMSELF, MY FAVOURITE ONE!!!"
    y 3y3 "SHADOW, LET'S MAKE SOME CUTTING EDGE JOKES AT THE EXPENSE OF THOSE MORONS!!!"
    y "{i}Where are my pens when I need them for touching myself at this awesome moment, goddamit???{/i}"
    sha shadow04 "Give yourself a break, Yuri. Do you think making some cuts in your arms makes you a edgy person too? Don't make me laugh."
    sha shadow03 "YOU ARE NOT EVEN CLOSE TO THE LEVEL OF EDGYNESS, SUFFERING AND SERIOUSNESS THAT I POSSESS!"
    show yuri 3y7 at t22 zorder 3
    sha "Do you think you are the EDGY BITCH of Doki Doki Literature Club? HAHAHAHA."
    sha "Everyone knows the real edgy person of DDLC is Monika!!! She is my favourite one!"
    sha "I'm Shadow the Hedgehog, Monika is my favourite Doki... and this is who I am."
    show shadow shadow03 at t32 zorder 4
    show yuri 3y7 at t33 zorder 3
    show sonic sonic12 at l31 zorder 3
    stop music
    play sound djstop
    sth "That DOES MEAN that YOU PLAYED DOKI DOKI LITERATURE CLUB, Shadow. You are not so edgy and dark after all!"
    show sonic at lhide zorder 1
    hide sonic
    show monika 2h at l31 zorder 3
    play music shadowAppears
    sha shadow02 "Always interrupting with stupid remarks, Sonic the FAKEhog. Shut your fucking mouth!"
    sha shadow04 "You don't know how I suffered on the part when Sayori killed herself. That was a pain in my black heart."
    sha "I couldn't save her, like I couldn't save and protect my beloved Maria."
    sha shadow03 "But I have to recognize the evil plan of Monika was amazing since the start of the game."
    sha "It was obvious that morons like Sonic, Tails and Knuckles couldn't recognize the obvious foreshadowing of Monika's lines of dialog."
    sha "You kind of left her hanging this morning, you know?"
    sha "WHAT DO YOU THINK MONIKA WAS TALKING? A HANGOUT? A PARTY?"
    sha "Only a hedgehog like ME can recognize the hidden talent of Monika and her selfish but loable desire!!!"
    m 2n "And I just want to be knocked out with an atomic bomb at this time..."
    m 2o "Even Ow the Edge thinks I'm the evilest person in the whole world."
    sha shadow00 "Anyways, that is not the reason why I'm here!"
    sha shadow04 "First, I have to say Monika's legs are more exquisite than what the game shows you."
    mc "Yeah, right??? I believed I was the only one thinking about that!"
    sha shadow03 "So the Rookie and me have the same way of thinking. Cool job, Rookie! I will be your ally then."
    m 5b "AND I'M JUST RIGHT HERE. STOP LOOKING AT MY LEGS! THANKS!"
    sha shadow04 "Second, and most important: Rouge, Omega and a whole squad of G.U.N. soldiers dissapeared thanks to THIS STUPID PURPLE HAIRED GIRL RIGHT HERE!"
    sha "I recognized you from that mountain far away, and then I used Chaos Control to teleport here and confront you!"
    sha "But while I was travelling with the Chaos Energy, some weird girl with pink hair and with blood in her eyes appeared in front of me, at the same speed!"
    sha "She approached me with her neck broken, and told me it would have been much better if I had stayed on G.U.N. headquarters, and that we would not save the Literature Club."
    sha shadow01 "SO, YURI, I DEMAND TO KNOW WHERE DO YOU HAVE MY FRIENDS, AND THAT YOU STOP YOUR STUPID FREAK SHOW FIESTA OF ILLUSIONS!!!!"
    y 1y3 "I WILL NEVER TELL YOU, STUPID CHINESE IMITATION OF SONIC THE MORON!!!"
    y 1y5 "IF YOU WANT THEM AGAIN, YOU WILL HAVE TO RECOGNIZE THAT I'M THE QUEEN OF THE EDGINESS!!!"
    m 4r "Oh c'mon, it's official, Yuri has a mental disease, this is ridiculous at this point."
    y 1y7 "BUT HE WAS THE ONE WHO KNOCKED OUT MY SPECTACULAR ILLUSION ACROSS THE SCENERY AND DESTROYING THE MAGIC BOX!!!"
    y "AND ALSO I CAN'T FORGIVE HIM! SHE LIKES MONIKA TOO? WHAT DO THEY LIKE OF THE RECYCLE BIN WITH LEGS????"
    m 5a "They said it already: my legs! Legs win against boobs, Yuri! {i}Wink{/i}."
    y 3y2 "UWAAAAAAAAAAAAAAAAA!"
    y 4c "Useless piece of presidential shit, stop joking about my cup size!!!"
    y "This is... this is..."
    y natsuUWA "THIS IS NOT FUCKING FAIR!!!!"
    m 2g "Uh... Yuri..."
    sha shadow00 "What now?"
    stop music
    play sound djstop
    y natsuTalk "I'M SO ANGRY ABOUT ALL OF THIS! I CAN'T BELIEVE SHADOW PREFERS MONIKA!!!"
    play music t7
    y natsuAngry "I memorized a lot of Shadow's stuff seeing the games of my lovely cupcake!!!"
    "Even being our enemy at this point, I see Yuri and this... passion that is showing now is incredible!"
    "She started to almost recite a lot of Shadow's facts and info!!!"
    y natsuAnnoyed "If the world chooses to become my enemy... I will fight like I always have!"
    y "That one is my favourite Shadow phrase."
    y "Shadow is a brooding loner, to put it bluntly. He usually acts with a cool and business like indifference, only occasionally showing his vulnerable side."
    y "Like recently when he commented about Recycle Bin with legs and saying that he will help Rookie."
    y "Shadow's infamous ruthlessness and aggression leads to fear and a nervousness from his unshakable intent or sheer power in combat."
    y "He is considered an anti-hero by the most part due to his morality."
    y "He will do whatever is necessary to get what he wants or feels is right."
    y "Shadow was created as \"The Ultimate Lifeform\", an immortal being that could be used for the benefit of military and stuff."
    y "He has blood of the Black Arms in his veins - which ended up being the key to perfect the ultimate lifeform -, but Black Doom asked in exchange the seven Chaos Emeralds for his own interest."
    y "BUT SHADOW DEFEATED THE BLACK ARMS AND DESTROYED THEIR EVIL STAR!"
    y "Shadow's belief that Maria's final wish was revenge against humanity stemmed from Gerald Robotnik modifying Shadow's memories between Maria's death and Shadow's encapsulation."
    y "Shadow also believed that Sonic was trying to copy him and that the blue obnoxious rodent was his faker."
    y "He befriended Rouge and Omega and formed Team Dark, and then they joined the G.U.N. organization."
    y "Shadow had been labeled as the enemy of mankind in one possible future, due to his perceived role in the disaster of the Iblis..."
    y "and their fear of his power. Mephiles asked Shadow to join in his evil cause, but Shadow refused to join him!"
    y natsuTalk "The Phantom Ruby helped me with that info, because those events are erased from the memories of the inhabitants of this world..."
    y natsuAnnoyed "Shorty before our arrive to this world, Shadow was on his way to Eggman's Facility to raid and destroy the base."
    y "Along the way, he annihilated the Jackal Squad defense unit and defeated their captain, whom Shadow told to never show his face to him again"
    y "That asshole of a captain is that imbecile autocalled Infinite. So weakly minion."
    y "And his default Extreme Gear is called the Black Shot."
    y natsuPro "As everyone can see, I'm a fucking pro on giving and memorizing facts. Baka."
    show monika at thide zorder 1
    hide monika
    show natsuki 12a at l31 zorder 3
    show shadow shadow04 at h32 zorder 4
    sha "I'm... totally speechless with this abstract of my life..."
    sha shadow03 "Maybe you are not so bad after all."
    n "Yuri..."
    n "Do you get that you are doing the same expressions as me, right?"
    n 1t "And that makes you look attractive and desirable for me."
    n 1x "WHICH IS A THING I WAS TRYING TO EVADE RIGHT NOW, THANKS FOR AWAKENING MY HORMONES AGAIN, YOU IDIOT!"
    y 3y2 "UWAAAAAAAAAAAAAAAAA! NATSUKI!!!!"
    y 4c "This is... this is... AAAAAAAAAAAAAAAAAAAAAAAAH!!!"
    y 4d "Please excuse me, my hormones are treasoning me too..."
    show yuri at lhide zorder 1
    hide yuri
    y "You are not seeing the last of me, Shadow! I will be back!!! YOU WILL BE SORRY FOR REJECTING ME!!!"
    y "WHAT A SHAME I ACTED LIKE AN IDIOT IN FRONT OF NATSUKI AGAIN!!!!!"
    show natsuki at thide zorder 1
    hide natsuki
    show shadow shadow01 at t32 zorder 4
    show monika 4r at t33 zorder 3
    show ghostnatsuki gNatsu1 at t31 zorder 3
    if persistent.packagedMusic == True:
        play music heavyMagicianPCKG
    else:
        play music mirageSaloon
    g "Well, what are we waiting for? Where we should be going?"
    g "We are wasting a precious time for rescuing all the people we care!"
    sha shadow04 "You look the same as the girl of that freak illusion."
    g "Well, I'm on the side of the heroes, so... no, she wasn't me."
    g "So let's move peopl... WTF DON'T TELL ME EVERYONE IS STILL SCARED!"
    show ghostnatsuki at thide zorder 1
    hide ghostnatsuki
    show monika at thide zorder 1
    hide monika
    show shadow shadow02 at t32 zorder 4
    show tails tails06 at t31 zorder 3
    show natsuki 42f at t33 zorder 3 
    "Tails pointed to the construction near the far away mountains: an oil refinery of Doctor Eggman."
    "Then he gived Shadow a copy of the MilesElectric device and a pair of headphones with microphone."
    "Tails and Natsuki were still terrified and approached Sonic. He was near them, as a sign of protection."
    show tails at thide zorder 1
    hide tails
    show natsuki at thide zorder 1
    hide natsuki
    show sonic sonic09 at t31 zorder 3
    show monika 12s at t33 zorder 3
    "Sonic was scared, but he is the hero, so everyone was counting on him anyways." 
    "Monika was scared too, but she was trying to hide it for the sake of Natsuki. I'm scared too about what will come next."
    show shadow shadow04 at t32 zorder 4
    "Shadow understood and then he placed the communicator in his ears."
    show sonic at thide zorder 1
    hide sonic
    show monika at thide zorder 1
    hide monika
    sha shadow05 "Whoever is behind this communicator, my name is Shadow the Hedgehog, Commander of Team Dark and a soldier of G.U.N."
    sha shadow04 "That miser... Wait I hate her less now, she is a fan of me after all..."
    sha shadow05 "That {i}little{/i} purple girl and her shitty pink gem kidnapped Rouge, Omega and my squad, and I want to recover them!"
    sha "We recently had a terrifying experience here on Mirage Saloon and Tails and the little girls can't talk because of it."
    sha "Sonic and Tails are here with me, so the Resistance's mission is still going!"
    sha "I want you to find out where that YURI is hiding, and Eggman's closest base of operation, and I want it now!"
    kte "THEN LET'S START OPERATION BIG WAVE, GUYS! SONIC, TAILS, SHADOW, MOVE WITH ROOKIE AND THE GIRLS TO OIL OCEAN ZONE, NOW!"
    kte "IT'S TIME FOR THE RESISTANCE'S RETALIATION!!!"
    show shadow shadow03 at t22 zorder 4
    show monika 2o at t21 zorder 3
    sha "By the way, Rookie..."
    sha "We will be allies, so I will share this with you and your team."
    show emerald turquoise at t22 zorder 4
    mc "A Chaos Emerald! Sweet! Thanks Shadow!"
    sha "Just lend me the {i}DAMN{/i} fourth Chaos Emerald, I prefer the green colour."
    sth "Do what he says, Rookie. Shadow is our friend too. The Emerald enhances his skills."
    mc "Ok, we exchange the green one with this one. But please keep the Emerald safe."
    sha "I will protect it with my life!"
    $ persistent.emeraldCount = 5
    play sound Emerald_word
    "{i}You won a Chaos Emerald!\n(Click to continue...){/i}"
    "Now we have [persistent.emeraldCount] Chaos Emerald!"
    show emerald at thide zorder 1
    hide emerald
    sha "Before we going, I want to show something for Monika, too."
    call showpoem(poem_m5, track="mod_assets/shadowAppears.ogg", revert_music=True)
    sha "I want to know what do you think about my po...{nw}"
    show shadow shadow06 at h22 zorder 4
    show monika 1o at h21 zorder 3
    kte "Wait what's happen...{nw}"
    m "What is happening, Rookie???{nw}"
    sha "WHAT THE HE...{nw}"
    show black zorder 5
    show n_glitch_head zorder 6:
        xpos 430 ypos -450 zoom 4.5
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 0>mod_assets/specialMenu.ogg"
    n "OH MY FUCKING DAMMIT!!!"
    n "WHO FUCKING CARES ABOUT THAT OBNOXIOUS KNUCKLEHEAD?"
    n "WHY IS SO DIFFICULT TO MAKE EVERYONE OF YOU UNDERSTAND THE TRUTH?"
    n "JOIN MY PRECIOUS YURI EMPIRE, GOD FUCKING DAMMIT!!!"
    n "AND TELL KNUCKLEBALLS THAT HE CAN STOP CHUCKLING!!!{nw}"
    $ style.say_dialogue = style.normal
    hide black
    hide n_glitch_head
    stop music
    scene white
    show introSegaGhost with Dissolve(0.5, alpha=True):
        xzoom -1
    play sound segaGhost
    pause 3.0
    hide introSegaGhost with Dissolve(0.5, alpha=True)
    play music yuriLastStand
    show splash-glitch with Dissolve(0.5, alpha=True):
        xzoom -1
    pause 2.0
    hide splash-glitch with Dissolve(0.5, alpha=True)
    show splash_warning "WELCOME TO YOUR SPECIAL HELL\n -Yuri." with Dissolve(0.5, alpha=True)
    pause 2.0
    play sound "sfx/giggle.ogg"
    show yuriMessedUp with Dissolve(0.5, alpha=True)
    pause 5.0
    show tcOilOcean with Dissolve(0.5, alpha=True)
    pause 3.0
    $ skip_transition = True

    scene bg oilocean1
    with wipeleft_scene
    if persistent.sayori_helped == True:
        s "I will try to help you in everything I can, Rookie!"
        s "But I have to warn you that Metal Sayori is preparing to battle all of you. Be safe and take care of my friends!"
    if persistent.packagedMusic == True:
        play music oilOcean1PCKG
        show honey djHoney at l31 zorder 5 
        dj "Now playing: {i}Sunnery James & Ryan Marciano - Lethal Industry{/i}."
        mc "I can't stop thinking that the name of the song is very fitting..."
        show honey at lhide zorder 1
        hide honey
    else:
        play music oilOcean1
    "..."
    mc "Well, we are here on Eggman's Base of Operations!"
    mc "Sonic said that this is called Oil Ocean Zone, and I can see why."
    mc "They are extracting a lot of oil. It looks like an ocean!"
    "Rivers of oil are flooding from all parts of the base, and polluted air expelled to the atmosphere."
    "And since we are still on desert, the temperature is abrasive."
    "The girls are in a safeplace inside this construction, resting of the fight against the Heavy Magician and the scares."
    "Knuckles, our captain, and Shadow, are ready to explore the base. Knuckles called the start of Operation BigWave."
    show knuckles knuckles01 at t21 zorder 3
    show shadow shadow07 at t22 zorder 3
    kte "Well guys! This is it! We found the Operational base of Dr. Eggman!"
    kte "I shall declare that Operation BigWave is starting now!"
    kte "Soon, all our elite troops and allies will come here to help us in the invasion of Oil Ocean zone."
    kte "We will stop the energy flux that keeps the machines of Eggman in operation, and hopefully the source of that pesky Ruby."
    sha "And I will have my revenge here for the kidnapping of Rouge, Omega and our squad."
    sha "Also, we will recover the location of the robotizer machine, and that should help the friend of Rookie that is now a robot."
    kte knuckles00 "Rookie, when Monika, Natsuki and Ghost recover their energies, you will command them to fight with us too!"
    kte "Amy and tails are taking good care of them, including the boy, which is eager to help Sayori."
    kte "Sonic told me that there is a giant submarine not so far away from here. We should go to investigate."
    sha shadow00 "If something happen, use the communicators. I will be there in a blast with Chaos Control."
    
    scene bg oilocean1
    with wipeleft_scene
    "After some time, we found the submarine."
    "Before Knuckles and I enter it, I called Monika to know how they are and receiving moral support."
    m "Don't worry Rookie! We are good and energetic now!"
    m "Amy took good care of everyone! I love that girl! We will be friends in no time."
    m "Tails did some reparations to Metal Monika, she is coming to your position now! She is eager to help you two!"
    n "AND PLEASE ROOKIE, IF YOU FIND SOMETHING, KICK IT'S ASS, OK?"
    n "WHEN YOU GO OUT OF THE SUBMARINE, WE WILL BE READY TO FOLLOW YOU!"
    n "It's not that I care or anything... ok? I'm eager to fight, that's all."
    g "Also, she prepared cupcakes for the future celebration, and she learned to do chilidogs too!"
    g "Take care and good luck you two. I don't think that there is a trap on that submarine, but giving best wishes is always a good thing."
    show boss2 metalMonika at h11 zorder 2
    m "I'M HERE! METAL MONIKA ONLINE! OPERATING SYSTEM FUNCTIONING CORRECTLY!"
    m "NOW I'M RUNNING IN MILES ELECTRIC OS! LESS PRONE TO GET BLUE SCREENS OF DEATH."
    m "SHALL WE MOVE, MISTER KNUCKLES?"
    kte "Absolutely! I have a good feeling about this!"

    scene bg oiloceanSub
    with wipeleft_scene
    show knuckles knuckles06 at t21 zorder 2
    show boss2 metalMonika at t22 zorder 2
    mc "So this is the infamous submarine. Curious. It seems like there is nothing here, except for rings and some powerups."
    kte "Of course this shit wouldn't be so easy. It's Eggman. He could still put a trap here."
    kte "We shall be concious of our surroundings and explore this thing."
    m "Hey! I'm Tails, talking using the communication system of Trashy!"
    m "There is a wireless online connection. I'm receiving and hacking data of Eggman."
    m "It seems the power source of the Ruby is in your island, in Lava Reef zone, the volcano."
    m "But Dr. Eggman make a subacuatic transport system of the oil and the electricity that this base is generating."
    m "If we can destroy it, Eggman will have a severe diminishing of resources for the Ruby and himself."
    m "And will have to activate his secondary resources, wasting precious time that we can use!"
    m "AS YOU CAN SEE, I'M USEFUL FOR THE BATTLE NOW! METAL TRASHY IS HAPPY."
    m "SHALL INVESTIGATE NOW?"
    kte "Absolutely! Let's move, team!"
    mc "Hey Captain, I see something over there!"
    mc "Wait... there are living beings and robots coming, what's up?"
    "Curious! Suddendly, from the far away part of the submarine, some animals and badnik robots of Eggman started to run in the direction of the entrance."
    "They are trying to escape using the entrance we used to let ourselves in, instead of the exit!"
    "Also, both the robots and the animals were doing signals to us of not going to the exit."
    "That opened more than ever our curiosity."

    scene bg oiloceanSub2
    with wipeleft_scene
    show knuckles knuckles06 at t21 zorder 2
    show boss2 metalMonika at t22 zorder 2
    "Curious."
    "At the exit of the submarine, there is a white shiny door."
    "The door seems to be locked."
    kte knuckles05 "This stupid door will not stop us, Rookie."
    kte "If it's locked, it means Eggman is hiding something important there."
    m "I. DON'T THINK THAT ENTER HERE IS A GOOD IDEA. PROBABILITY OF RISK: 95%%."
    kte knuckles04 "I was born and raised in the risk!!! Now get back, I will open this stupid door!!!"
    kte "RAAAAAAAAWWWWRRRRRRRRRRRRRRR!!!"
    mc "OH NO!!!! WHAT DID YOU DO, CAPTAIN???? THE DOOR IS ATTRACTING US!!!"
    m "EMERGENCY, EMERGENCY!!! CALLING THE RESISTANCE!!! I WILL GO FOR HELP!!!"
    "We are doomed, this door was a trap and is sucking us in!"
    stop music fadeout 2.0

    #Yuri illusion starts here
    scene bg class_day
    with dissolve_scene_full
    show yuri eyes_base
    pause 5
    play music "<loop 0>mod_assets/pumpedUpMettatonsFast.ogg"
    show yuri at thide zorder 1
    hide yuri
    show noise at noise_alpha zorder 100
    show vignette at vignetteflicker(-2.030) zorder 100
    show layer master at rewind
    y "{cps=*3}Thaaank yoouuu... Rookie...{/cps}{nw}"
    "{cps=*3}15 {i}pleasant minutes{/i} passed...{/cps}{nw}"
    y "{cps=*3}ROOOOOKIIIIIIEEEEEEEEEE...{/cps}{nw}"
    y "{cps=*3}YEEEEEEEESSSSSSSSSSSSS!!! YEEEEEEEEEEESSSSSSSSSSSSSSSSS!!!{/cps}{nw}"
    mc "{cps=*3}YEEEEES! YURI! I'M HERE TO BE WITH YOU! GIVE ME THOSE PENS AND BE MINEEEEEEE...!!!{/cps}{nw}"
    scene bg corridor
    show noise at noise_alpha zorder 100
    show vignette at vignetteflicker(-2.030) zorder 100
    show layer master at rewind
    "{cps=*3}SORRY KNUCKLES BUT I DON'T WANT YOU BOTHERING ME! I SHUT THE DOOR IN HIS FACE AND HE FALLS TO THE GROUND UNCONCIOUS!{/cps}{nw}"
    "{cps=*3}I FOUND THE CLASSROOM WHERE SHE IS!!! AND SHE IS READY FOR ME!!!{/cps}{nw}"
    "{cps=*3}I feel a {i}very comfortable scream{/i}, like if {i}someone is horny and excited, and calling to me{/i}. She is near.{/cps}{nw}"
    y "{cps=*3}AAAAAAAAAAHHHH--{/cps}{nw}"
    "{cps=*3}YURI IS CALLING ME. I CAN'T FOCUS. I WANT THIS. I SHOOT MY WISPON AND KNOCKED KNUCKLES AWAY.{/cps}{nw}"
    kte "{cps=*3}This is a trap, don't go, Rookie...! STOP, I DON'T WANT TO FIGHT WITH YOU TO MAKE YOU STOP!!!{/cps}{nw}"
    kte "{cps=*3}What's that noise? No... wait... Rookie!!!{/cps}{nw}"
    y "{cps=*3}....Haah....Come here, Rookie....haah....{/cps}{nw}"
    y "{cps=*3}Haah.....I need you....haah....Make me yours....{/cps}{nw}"
    "{cps=*3}I started heading down the hallway. Knuckles still follows me. Stop following me, sucker.{/cps}{nw}"
    "{cps=*3}We arrived in the corridor that Yuri said in her poem.{/cps}{nw}"
    mc "{cps=*3}I want to be with Yuri... I want to be with Yuri... I want to be with Yuri...{/cps}{nw}"
    window hide(None)
    window auto
    scene bg club_day2
    show noise at noise_alpha zorder 100
    show vignette at vignetteflicker(-2.030) zorder 100
    show layer master at rewind
    "{cps=*3}Of course, my boring boss, Knuckles, is convinced that this is a trap, and ran after me.{/cps}{nw}"
    "{cps=*3}I'm bored of not having any action in this stupid war, so I decide to go look for her, as she wants.{/cps}{nw}"
    "{cps=*3}Yuri wrote a poem for me, it says that she {i}wants that I make her my woman{/i}!{/cps}{nw}"
    "{cps=*3}Yuri said that she has a surprise for me and only me...{/cps}{nw}"
    "{cps=*3}I can't stop thinking about Yuri.{/cps}{nw}"
    "{cps=*3}The mod author is not responsible if you read the History log because your curiosity killed you and find this too hot. Be warned.{/cps}{nw}"
    scene bg club_day2
    hide noise
    hide vignette
    show layer master
    stop music
    "What...?"
    "We are back in the clubroom!!! But how??? It was destroyed at the start of this adventure!!!"
    "Huh? Why I'm smiling? Why I have a {i}very wet{/i} pen in my hand? It says SAVE IT. So I will save it on my secret compartiment of my Wispon."
    "I feel... so relaxed."
    "The classroom has a poster of Sayori hanged up in the back."
    "It's like nobody notices that, except Knuckles and me."
    "Knuckles is here with me, and Metal Monika called for help before we were sucked into that white door. I'm glad of not being alone here."
    "But Knuckles is angry with me. And suddendly, Yuri enters the classroom."
    play music pumpedUpMettatons
    show yuri 1a at t22 zorder 2
    show knuckles knuckles06 at t21 zorder 2
    y "I'm back. Thanks for waiting patiently."
    kte "{i}ROOKIE. I will seriously talk with you when we go back to our world. I will take notice in your life paper about how you closed the door in my face!{/i}"
    mc "{i}WHAT!!! So, then, THAT was true??? What... but... oh no.{/i}"
    kte "{i}OF COURSE WHAT YOU DID WAS TRUE!!! Your STUPID RELAXED EXPRESSION screams it! And also that wet pen you have in your hand.{/i}"
    "{i}Then I WILL save this pen, forever. Period.{/i}"
    y 1f "Oh, [player], I didn't know you came with a friend to our club meeting."
    y 1s "Pleased to meet you, Rookie's friend. I'm Yuri, the Vice President."
    "Wasn't Sayori the Vice President?"
    y 1a "Anyways, do both of you like oolong tea?"
    kte "{i}It's just me or Yuri just believe that we are classmates of her?{/i}"
    mc "{i}I don't have any idea what's going on, Captain. It's like my mind it's still compelling me to answer to her using some predefined dialog.{/i}"
    kte "{i}Me too. And even if this scene must be between she and you only, the game is adapting it for the three of us.{/i}"
    kte "{i}I think this is a kind of trap or a Ruby illusion, let's play it safe and keep the charade, soldier.{/i}"
    show knuckles knuckles01 at t21 zorder 2
    mc "Ah, yeah, Yuri. My friend is called Knuckles, sorry for not telling you that I would bring him to the Club."
    mc "And also, any kind of tea is fine for me."
    kte "Yeah, I'm open to any kind of flavours, don't worry too much about it."
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 0>mod_assets/pumpedUpMettatonsReverse.ogg"
    $ style.say_dialogue = style.edited
    mc "Specially if it comes from you."
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 0>mod_assets/pumpedUpMettatons.ogg"
    "Wait, what?"
    y "Very well."
    "Yuri sets the temperature on the kettle to 200 degrees."
    y 1f "Now it's time to get the teapot."
    mc "You really do this properly, don't you?"
    y 1u "Of course... I shouldn't do any less when I'm making tea for others."
    mc "Even if we are not experts on tea or anything...?"
    y 2m "Huhu."
    y 2a "In that case, you'll only be even more impressed."
    mc "Ah...perhaps we will!"
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 0>mod_assets/pumpedUpMettatonsReverse.ogg"
    y 2y3 "Specially with this oolong tea with a touch of Monika's unholy blood!"
    $ style.say_dialogue = style.normal
    show yuri at thide zorder 1
    hide yuri
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 0>mod_assets/pumpedUpMettatons.ogg"
    "Yuri fetches the teapot and begins measuring the tea leaves. She even starts humming a little to herself."
    "But Knuckles and I still feel uneasy about this."
    show yuri 1c at t22 zorder 2
    kte knuckles00 "You must be in a good mood now, lady..."
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 0>mod_assets/pumpedUpMettatonsReverse.ogg"
    $ style.say_dialogue = style.edited
    y 1y3 "YES! I had A HOT ACTION OUT THERE! I'M EXTREMELY HAPPY!!!"
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 0>mod_assets/pumpedUpMettatons.ogg"
    y 1a "Is that so? I was letting it show..."
    y "And you noticed."
    y 2u "I was doing a bit of thinking..."
    y "And I decided that I would try expressing myself a little bit more."
    y "It turns out it's not very hard for me to do..."
    y 1c "When it's Rookie who's around, anyway. And I feel comfortable with you too, Knuckles."
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 0>mod_assets/pumpedUpMettatonsReverse.ogg"
    y 1y3 "So come here and touch me AGAIN!!!"
    $ style.say_dialogue = style.normal
    kte "{i}Weird, the purple hair girl has a crush on Rookie in this shitty illusion.{/i}"
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 0>mod_assets/pumpedUpMettatons.ogg"
    show yuri 1a
    mc "Ah...That's great, Yuri! Just don't push yourself too much, ok?"
    y 3u "You're always worrying about me, [player]... It's very endearing."
    "Yuri wasn't kidding... I don't even know if I can keep up with this thing that is happening...!"
    "I watch Yuri pour a cup of tea for each of us. Knuckles also signals me to keep going."
    y 1a "[player], Knuckles, I have another request."
    y "Do you mind if we sit on the floor today?"
    mc "Eh? Why's that?"
    y 1h "It's a little bit easier on my back... I can read with my back against the wall rather than bending over at my desk."
    mc "Ah, sorry, I didn't realize."
    y 1a "No worries."
    y "I just have back pain fairly regularly, so I do my best to manage it."
    mc "Is that so? I wonder why that is..."
    y 1f "It's most likely because my--"
    y 1n "Ah--"
    y 1o "M-My..."
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 0>mod_assets/pumpedUpMettatonsReverse.ogg"
    y 1y3 "TIME TO SHOW MY POWER! ROOKIIEE... LOOK. AT. MY. BOOBS. NOW."
    $ style.say_dialogue = style.normal
    "Why I'm staring like an idiot to her boobs?"
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 0>mod_assets/pumpedUpMettatons.ogg"
    kte "It's your posture, right, lady? Always hunched over like that while reading..."
    y 2p "Yes!"
    y 2q "I have terrible reading posture! So that's why we should sit on the floor."
    kte "Fair enough. Rookie, be a gentleman and get the book from the teacher's desk."
    show yuri at thide zorder 1
    hide yuri
    kte knuckles06 "{i}Rookie, you were about to tell her about her mammals size and also stared at them, you moron!{/i}"
    mc "{i}Sorry, boss!!! It's the same thing that happens to me with Monika's legs!{/i}"
    kte "{i}And also, your name is really [player]? Interesting... We believed you didn't have a name.{/i}"
    "I retrieve a book that appeared misteriously in the teacher's desk. Also, a bag of small chocolate candies that appeared there too."
    "Knuckles told me that Amy said one time that chocolate go well with tea."
    "Yuri, Knuckles and I then sit against the wall, teacups at our sides, and one of us at each side of Yuri."
    show knuckles at thide zorder 1
    hide knuckles
    show yuri 2h at t11 zorder 2
    y "I can't see too well..."
    mc "--!"
    show yuri 2e at d11
    "Yuri slides closer until our shoulders are touching. Knuckles was free to move. That's good if something weird happen."
    "But that means that I need to worry about making sure I don't accidentally touch her chest...! Glad that Yuri hasn't noticed a single thing."
    "She wears her intense reading expression, like if the world around her has faded away."
    "Knuckles signals me to keep going! So, I use all of my willpower to focus on reading."
    "..."
    "After a few minutes, we finally manage to relax a little. I put the teacup between my legs and fumble with the chocolate wrapper. Knuckles has his own bag of chocolates."
    mc "Ah, sorry..."
    "I briefly let go of the book to finish opening the wrapper."
    mc "You can have as much as you want."
    y 2s "Ah, that's..."
    y "That's okay, I won't take any..."
    mc "Eh? Are you sure?"
    y 2v "Well..."
    y "If I touch it, then it might get smudges on the pages..."
    mc "Ah, you're right... I didn't even think about that, my bad, sorry."
    y 2a "No need to apologize. I'll hold the book, okay?"
    mc "Are you sure...?"
    y "Of course."
    scene y_cg2_bg
    show y_cg2_base
    show y_cg2_details
    show y_cg2_nochoc
    show y_cg2_dust1
    show y_cg2_dust2
    show y_cg2_dust3
    show y_cg2_dust4
    with dissolve_cg
    "Yuri opens the book with both hands."
    "She holds it so that I don't have any harder of a time reading from it. But as a result, her left arm is practically resting on top of my leg."
    "Knuckles has good visual to see the book and the surroundings. Because Yuri is focused on the book, she didn't notice anything."
    "Then, for some reason, I'm forced to take a chocolate..."
    "And I hold it up to Yuri."
    "She doesn't even look away from the book. She simply parts her lips, as if this situation was completely natural."
    "But that means I can't stop here!"
    hide y_cg2_nochoc
    "I apprehensively place the chocolate in her mouth. Yuri closes her lips over it."
    y "Eh...?"
    show y_cg2_exp2
    "Yuri's expression suddenly breaks."
    y "Did I just..."
    "Yuri looks at me like she needs to confirm what just happened."
    show y_cg2_exp3
    show y_cg2_nochoc:
        alpha 0
        linear 0.5 alpha 1
    hide y_cg2_exp2
    y "U-Um... [player]..."
    kte "{i}Attention, Rookie! You triggered something!!!{/i}"
    mc "I guess I shouldn't have done that... sorry Yuri, I wasn't thinking..." 
    "Yuri starts to breathe heavily."
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 0>mod_assets/pumpedUpMettatonsFast.ogg"
    hide y_cg2_exp3
    show y_cg2_expforces
    y "Rookie."
    y "Did you believed I didn't noticed?"
    y "You are extremely horny for being an anthropomorphic animal in a vital mission to save your world, eh?"
    y "If you are not staring to Moronika's legs, you stare at my boobs."
    y "Every. single. time. I appear, you stare."
    y "Very clever, Rookie. Very clever."
    y "I really left you two big reasons in your brain as a good impresion of me."
    y "But don't worry, [player]. I'm super horny and turned on right now, too."
    "And even the music got horny it seems..."
    y "So, that means there is only one thing to do!"
    "Suddenly, Yuri forcefully grabs my arm and jerks me to my feet."
    "My teacup gets knocked over. Knuckles stands up inmediatly!"
    scene bg closet_creepy
    show yuri 2t at t11 zorder 2
    with wipeleft
    y "[player]..."
    play sound closet_close
    kte "WOAH! ALL THE DOORS OF THIS CLASSROOM CLOSED BY THEMSELVES!!! WE ARE TRAPPED!!!"
    "And we are frozen in place!!! I can't move my body!"
    mc "Yuri what's wrong with you??? And..."
    "What the heck happened to the closet?"
    y 2y3 "SHUT UP YOU MORON AND LISTEN!"
    y "My heart won't stop pounding, [player]... Look how you left me."
    y "I can't calm down. I can't focus on my book, I can't focus on my plan, and I can't focus on my lovely cupcake."
    y "What the fuck did you put in this chocolate???"
    y "Anyways, [player], there's no need for you to keep going with your mission."
    y 1y5 "Just stay here with me instead."
    y 3y5 "The whole eternity, with just the two of us..."
    y "Doesn't that sound wonderful?"
    mc "In reality, no. It doesn't sound fun at all..."
    "I'm sweating."
    y 3y1 "Ahahaha!"
    y 1y3 "I don't care about your answer!!!"
    y "I've never felt this good my whole life."
    y 1y4 "Just being with you is a far greater pleasure than anything I could imagine."
    y "I'm addicted to you."
    y 3y4 "It feels like I'm going to die if I'm not breathing the same air as you."
    y 4a "Doesn't it feel nice to have someone care about you so much?"
    y "To have someone who wants to revolve their entire life around you?"
    mc "Yeeeeeaaaaaah... Specially if that person is a creepy one..."
    kte "{i}I have a VERY BAD feeling about this...{/i}"
    y 2y6 "But if it feels so good..."
    y 2y4 "Then why does it feel more and more like something horrible is going to happen?"
    y 3y1 "It doesn't matter! I don't care about that anymore, [player]!"
    y "And also I don't care if Knuckles is here listening like an idiot and all your friends are seeing this in EGGTV!"
    "WHAT??? ALL MY FRIENDS??? SEEING THIS???"
    y 3y4 "I'm...I'm madly in love with you! Every inch of my body...every drop of blood in me...is screaming your name."
    y 3w "Please, [player], just know how much I love you."
    $ style.say_dialogue = style.edited
    y 3m "I love you so much that I even touch myself with pens. Every single day. It's addictive."
    y 3y4 "I just want to pull your skin open and crawl inside of you."
    y 3y6 "I want you all to myself. And I will be only yours. Doesn't that sound perfect for you?"
    y 3s "Tell me, [player]!!! Do you accept my confession???"
    $ style.say_dialogue = style.normal

    menu:
        kte "ROOKIE! DON'T ANSWER THAT QUESTION, IT MUST BE ANOTHER WAY!"
        "Yes! Free boobs!!!":
            show yuri cuts1 at i11
            kte "Rookie goddamit!!!"
        "No way!!!":
            show yuri cuts6 at i11
            kte "Well said, Rookie!"
            y "OK. Say goodbye to this girl."
            mc "Wait what...?{nw}"
        "Do as Knuckles says!":
            mc "Sorry Yuri, but there must be another way to solve this!"
            kte "Now, girl, let us move again and stop this madness! What is that stupid thing about loving Rookie?"
            show yuri cuts1 at face(y=600) with dissolve
            y "WHY? WHY? WHY? EVERYTIME I DO SOMETHING COOL FOR YOU, YOU ARE TRYING TO STOP IT!"
            y "I AM THE PHANTOM RUBY! I AM THE ONE CONTROLLING THIS SCRIPT! SO SHUT THE FUCKING UP AND EVERYONE WATCH THIS STUPID GIRL GET KILLED!"
            show yuri cuts1 at i11
        
    stop music
    show yuri cuts1 at i11
    mc "Yuri what the hell is happening?{nw}"
    kte "OH COME ON WHAT THE FUCK WITH THIS GIRL??? WHAT NOW???{nw}"
    $ style.say_dialogue = style.edited
    y 3y5 "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA{nw}"
    window hide(None)
    window auto
    $ style.say_dialogue = style.normal

    play music "mod_assets/pumpedUpMettatonsYuriPls.ogg"
    pause 1.43
    show yuri stab_1
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    pause 1.25
    show yuri stab_3
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
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
    #play sound ruby
    pause 0.25
    scene black
    pause 3.0

    scene black
    show y_kill_forces
    show y_kill_forces_exp2
    with dissolve_cg
    window show(None)
    play music "<loop 0>mod_assets/pumpedUpMettatonsSlow.ogg"
    mc "WHAT THE FUCK? WHAT THE FUCK WHAT THE FUCK WHAT THE FUCK WHAT THE FUCK NO NO NO NO NONONONONONONONONO"
    kte "FOR FUCKS SAKE!!! SERIOUSLY??? THIS STUPID COMMITED SUICIDE HERSELF???"
    kte "WHY THE FUCK WE HAVE TO LOOK AT THIS SHIT???"
    mc "KNUCKLES, PLEASE, SHUT THE FUCKING UP, GODDAMIT!!!! YOU DON'T UNDERSTAND!!!"
    mc "EVERY SINGLE TIME YOU SPEAK IS FOR DOING A BRAVADO, A WORTHLESS WAR STRATEGY, OR TALK ABOUT THE MASTER EMERALD!!!"
    mc "PLEASE!!! SHUT UP!!! FOR ONCE!!!"
    "Knuckles got surprised and stopped yelling. He bowed his head down and looked at the girl."
    "I get closer to Yuri. Her eyes had little life force in them."
    mc "I... I lost friends too in this war, you know! And you, me and everyone knows that Yuri is not as a villain as it seems!"
    mc "At least let me give her peace in her final moments, illusion or not, in exchange of my friends!"
    y "Ro-Rookie..."
    hide y_kill_forces_exp2
    show y_kill_forces_exp3
    with dissolve_cg
    "I cleaned the blood from her beautiful face."
    mc "I'm... I'm really sorry I couldn't help you..."
    "Why I'm crying all of a sudden...?"
    y "Rookie... it-it's fine..."
    y "The... last time this happened... MC couldn't do nothing... he was frozen in place..."
    y "Please... tell my friends that they are the best..."
    y "And tell my little cupcake that... I... l-l-l..."
    hide y_kill_forces_exp3
    hide y_kill_forces
    stop music fadeout 2.0
    show y_kill_forces_gameOver
    with dissolve_cg
    "I can't believe what is happening... The communicator is ringing..."
    mc "Tails. Sonic. Monika. Natsuki..."
    mc "ANYBODY CAN FUCKING HEAR ME!!!???"
    mtp "Rookie! Thanks to the Master Emerald! We weren't unable to call you until... well..."
    n "So that was what happened in the club room that day... Yuri... why???"
    m "Rookie... I'm sorry... I'm so sorry!!! You all didn't deserve to see that!!! This was my fault too..."
    mc "WHAT THE FUCK WE DID TO DESERVE ALL OF THIS??? THIS NON-SENSE WAR HAS TO BE STOPPED!!!"
    mc "YURI DIDN'T DESERVE THIS!!!"
    "We all cried for some minutes, except for Sonic and Shadow. They got silent in respect."
    amyR "We will try to get you out. Stay calm."
    kte "The white door appeared behind us, [player]. I will go in. I will give you some alone time, ok?"
    "Knuckles gived me some pats in my head. I waited for my tears to stop and dry before going to the door of the clubroom."
    "This is the first time an illusion affected me so much since my squad and friends got killed at the hands of Infinite."
    "I will do whatever is neccesary to prevent that the Phantom Ruby force Yuri to do this thing."
    play sound ruby

    scene bg oilocean2
    with dissolve_scene_full
    if persistent.packagedMusic == True:
        play music oilOcean2PCKG
        show honey djHoney at l31 zorder 5 
        dj "Now playing: {i}Global Deejays - Lonely{/i}."
        dj "LONELYLONELYLONELYLONELYLONELY\nLONELYLONELYLONELYLONELYLONELY\nLONELYLONELYLONELYLONELYLONELY"
        show honey at lhide zorder 1
        hide honey
    else:
        play music oilOcean2
    "We are outside the submarine, but..."
    "It seems the base is damaged already."
    "Hey! I still have the pen on my Wispon..."
    "Now I'm really worried about Yuri."
    y "Why are you worried, Rookie? I'm here again!"
    show monika 2i at t41 zorder 4
    show natsuki 4i at t42 zorder 5
    show yuri 1y3 at t43 zorder 5
    show knuckles knuckles02 at t44 zorder 6
    kte "YOU!"
    show knuckles at thide zorder 1
    hide knuckles
    show mc2 1h at t44 zorder 6
    n "Yuri! What you did with Rookie... I believed you were in love with me..."
    mc2 "Yuri, this is not the Yuri I remember from the club. You are still on time to stop this."
    m "That was enough, Yuri. I'm still your President. You will throw away that Phantom Ruby at this instant."
    y 3y7 "NO! I'm done of you giving me orders!"
    y "I'm done of you taking away Natsuki from me!"
    y "I'M DONE OF YOU TRYING TO BE THE HERO THAT YOU AREN'T, SINNER."
    y "YOU KILLED SAYORI. YOU IGNORED EVERYTHING ABOUT NATSUKI. YOU MADE ME GO CRAZY. AND YOU STILL FEEL THAT YOU ARE THE MOST IMPORTANT OF US."
    y cuts6 "But no more."
    show monika at thide zorder 1
    show natsuki at thide zorder 1
    show mc2 at thide zorder 1
    hide mc2
    hide monika
    hide natsuki
    show yuri cuts8 at t11 zorder 2
    y "It's time for me to play by MY rules now!"
    play sound ruby
    scene bg octiBoss
    "Yuri summoned a robot! It's a giant Octi!"
    "But not only that, she also summoned illusions to the stage!"
    "Oil Ocean is surrounded by bigger as fuck illusions of Yuri, red Yuris and Natsukis without a face."
    "Yuri was piloting the OctiBoss."
    show yuri cuts8 at t11 zorder 2
    y "I hope you like the new {i}decorations{/i} I'm giving to this base!"
    kte "SCREW YOU! The illusions are messing with everything!"
    kte "We are receiving calls from all the Resistance soldier and the G.U.N. troops!"
    kte "The illusions that Yuri created are attacking our forces and are invincible, and also screwing with the gravity!"
    kte "Operation BigWave is ruined!!! We can't engage with all of this!"
    show yuri at thide zorder 1
    hide yuri
    show amy amy10 at t41 zorder 4
    show tails tails03 at t42 zorder 5
    show sonic sonic07 at t43 zorder 5
    show shadow shadow05 at t44 zorder 6
    mc "What shall we do now? We need to think on something! Yuri only wants to defeat her classmates and friends at all costs!"
    mc "I can't stand that Monika and Natsuki keep suffering about this! And there are too much illusions to fight!"
    mtp "Sonic, friends! The OctiBoss is invincible, according to my lectures. Even if we want, our attacks will do nothing against it!"
    amyR "We can't surrender, guys! The stakes are high and the future of the world is at our hands!"
    sha "We can't surrender against the desires and cries of a little girl! That's the most embarrasing thing ever!"
    kte "There are Resistance soldiers that I am dispatching. They let us their Wispons and powerups!"
    sth "Rookie, give the Wispons to the girls. It's time for Monika, Natsuki, Ghost and MC to fight!"
    sth sonic13 "We are the Resistance! We will save our world! We will save Natsuki's world! And we will kick the Ruby's ass!"
    sth "WE ARE SONIC HEROES!"
    mc "And nothing can destroy the power of friendship!"
    y "How cute, the power of friendship!"
    y "What's wrong with everyone, aren't you having fun? HAHAHAHAHAHAHA!"
    y "Come to play, Sonic! Let's see if you are the fastest thing alive for dying!"
    sth "Nobody challenges me to a race and laugh at my face, Yuri. Guys! The fight for our world starts now!"
    "And so, we separated and started to fight against the illusions! As requested, I team up with my friends of the Literature Club!"
    show amy at thide zorder 1
    show tails at thide zorder 1
    show sonic at t43 zorder 1
    show shadow at t44 zorder 1
    hide sonic
    hide tails
    hide amy
    hide shadow
    show monika 2h at t41 zorder 4
    show natsuki 4o at t42 zorder 5
    show mc2 1h at t44 zorder 6
    show ghostnatsuki gNatsu1 at t43 zorder 5
    if persistent.packagedMusic == True:
        play music vsoctibossPCKG
        show honey djHoney at l31 zorder 5 
        dj "Now playing: {i}Knife Party - 404{/i}!"
        dj "EVERYONE WILL DIE HERE. THERE IS NO HOPE. THE SOUND OF THE SILENCE SHALL BURY YOU IN A WAVE OF AGONY SCREAMS!"
        dj "SO DO ME A FAVOR AND PLEASE D-D-D-D-DIE!"
        mc "COME ON, YURI! EVEN THE DJ IS AGAINST US NOW! NOT FAIR!"
        show honey at lhide zorder 1
        hide honey
    else:
        play music vsoctiboss
    mc "This is it, everyone! It's time to defend our worlds! If Sonic has his Sonic Heroes, we will be the DOKI-DOKI HEROES!"
    m "For the justice, the literature, our lovely club, and my love for the player!"
    n "For all the cupcakes in the world, my love for Sonic, manga, and for rescuing Yuri!"
    g "For the new opportunity I was given to have friends, and for the piece of shit out there, we will fight!"
    mc2 "For my world, for the friendships I made in the club, and specially I will fight for my true love, my cinnamon bun!"
    "WE ARE DOKI-DOKI HEROES!!!"
    kte "REMEMBER: DON'T ENGAGE IN COMBAT WITH THE ROBOT! THE GOAL IS TO GET IN ONE PIECE TO THE VOLCANO! THE ROBOTICIZER AND THE TRUE SOURCE OF EGGMAN'S BASES ARE THERE!"
    kte "FOR ALL THE SOLDIERS: THE ONLY REAL GIRLS AND DUDE WITH UNIFORM ARE THE ONES WHO ARE WITH [player]!"
    kte "EVERY OTHER GIRL IS AN ILLUSION OF YURI, AND YOU CAN DESTROY THEM WITHOUT SECOND DOUBTS!!!"
    n 4v "The OctiBoss is near us!!! It's time to run!!!"
    scene bg oilocean2Creepy
    "The battle with the illusions started."
    show sonic sonic07 at t21 zorder 3
    show monika help at t22 zorder 3
    $ style.say_dialogue = style.edited
    g "THERE IS NOWHERE TO RUN."
    g "STOP FIGHTING. GIVE UP."
    g "MONIKA IS USELESS."
    $ style.say_dialogue = style.normal
    sth "Monika is not useless! Dissapear!"
    "A homing attack ended with the glitched Monika."
    show sonic at thide zorder 1
    show monika at thide zorder 1
    hide sonic
    hide monika
    show sonic sonicEXE at t21 zorder 3
    show monika wispon at t22 zorder 3
    $ style.say_dialogue = style.edited
    sth "HELLO. DO YOU WANT TO PLAY A GAME OF HIDE AND SEEK?"
    sth "SONIC WILL NOT SAVE YOU AT ALL."
    sth "BUT YOU CAN JOIN ME. WE CAN RULE THIS WORLD WITH YURI."
    sth "AND WE WILL HAVE SO MANY SOULS TO PLAY AND TORTURE..."
    $ style.say_dialogue = style.normal
    m "And I will have {i}LOTS OF FUN{/i} with you."
    m "Do you want to play a game? Let's play EAT THE BULLETS!"
    "Monika used her Wispon and shoots at the Sonic illusion."
    show sonic at thide zorder 1
    show monika at thide zorder 1
    hide sonic
    hide monika
    sth "Stupid girl! Sonic.Exe doesn't die! Just dissapear until another convenient moment!"
    sth "HAHAHAHAHAHAAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA!!!"
    show mc2 wispon at t21 zorder 3
    show glitch sayoriRed at t22 zorder 3
    $ style.say_dialogue = style.edited
    g "SAYORI DOESN'T LOVE YOU. SHE IS USELESS."
    g "STOP THE FIGHT. GIVE UP AND I CAN REUNITE YOU WITH HER AGAIN."
    g "SAYORI IS WEAK. YOU DESERVE BETTER."
    $ style.say_dialogue = style.normal
    mc2 "My cinnamon bun is not weak. She is strong, lovely, cheerful and a good friend and girlfriend."
    mc2 "And her rainclouds can go away. Everyone are supporting her, and she is taking a therapy."
    mc2 "But in contrast, you are a mere ghost of her nightmares. You can't damage her."
    "MC used the drill and sended the illusion underground."
    show mc2 at thide zorder 1
    show glitch at thide zorder 1
    hide glitch
    hide mc2
    show natsuki wispon at t31 zorder 3
    show monika broken2 at t32 zorder 3
    show yuri yuriIllusion at t33 zorder 3
    $ style.say_dialogue = style.edited
    g "HEEEEEEEY! LOOK HOW SHE IS. THE WEAKER, NEGLECTED AND OBNOXIOUS ONE."
    g "LET'S DO TO HER THE SAME YOUR DADDY DID TO YOU."
    y "CUPCAKE. BE WITH ME. EMBRACE MY EMPIRE. FOLLOW ME."
    $ style.say_dialogue = style.normal
    n "YOU ARE NOT YURI."
    "Good shot, Natsuki, the illusions were gone."
    show y_glitch_head zorder 6:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    y "Still believing you can win?"
    y "Think again, [player]."
    hide y_glitch_head
    show natsuki at thide zorder 1
    show monika at thide zorder 1
    show yuri at thide zorder 1
    hide natsuki
    hide monika
    hide yuri
    show ghostnatsuki wispon at t21 zorder 3
    show tails tailsGlitch at t22 zorder 3
    $ style.say_dialogue = style.edited
    mtp "THERE IS NOWHERE TO RUN."
    mtp "STOP FIGHTING. GIVE UP."
    mtp "USELESS PIECE OF SHIT!"
    $ style.say_dialogue = style.normal
    g "There is only one piece of shit, and it's not me."
    g "Also you don't have a gun, and I can use it without hands. Goodbye!"
    "Goodbye glitched Tails!"
    show ghostnatsuki at thide zorder 1
    show tails at thide zorder 1
    hide ghostnatsuki
    hide tails
    show n_glitch_head zorder 6:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    y "Surrender, idiot!!!"
    y "Sonic's world will be MINE!!!"
    hide n_glitch_head
    show t_glitch_head zorder 6:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    y "You will never save this world."
    y "The Yuri Empire will rise!"
    hide t_glitch_head
    show m_glitch_head zorder 6:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    y "I'm the Presidential Shit."
    y "Deliver your surrender letter to me. I will deliver it to Yuri."
    hide m_glitch_head
    show glitch illusionMonika at t31 zorder 3
    show natsuki broken at t33 zorder 3
    show amy amy02 at t32 zorder 3
    $ style.say_dialogue = style.edited
    g "EAT THE SWEET CUPCAKE OF THE DEFEAT, AMY."
    g "SONIC WILL NEVER LOVE YOU."
    $ style.say_dialogue = style.normal
    amyR amy05 "Oh, how cute those two look."
    amyR "I want to give both of you a fashion emergency. Let's start with new clothes."
    amyR amy10 "You can dress with these shiny new clothes. They are called PIKO PIKO HAMMER!!!"
    "Amy sent the illusions to fly with his powerful hammer."
    amyR amy04 "And don't come back!!!"
    show amy at thide zorder 1
    hide amy
    show natsuki at thide zorder 1
    hide natsuki
    show glitch at thide zorder 1
    hide glitch
    show tails tails07 at t21 zorder 2
    show boss2 metalMonika at t22 zorder 2
    mtp "Hey guys, I found the way to Lava Reef!"
    m "Let's hurry, boys and girls!!! The robot is still behind us!!!"
    mc "Girls! MC! To that cave out there!!! Fast!!!"

    scene black
    with wipeleft_scene
    show yuriMessedUp
    y "HAHAHAHA! Were you waiting for a title card???"
    y "YOU WILL NEVER ESCAPE, PLAYER!!!"
    y "This is your last warning to join me. Use it wisely!"
    window hide
    pause 3.0
    scene bg lavaReefVS
    with dissolve_scene_full
    show yuri cuts8 at t22 zorder 2
    show monika wispon at t21 zorder 2
    "We ran very fast to Lava Reef zone!"
    "We tried to have a bigger distance from the OctiBoss, but it keeps chasing us."
    "At that moment, Monika stopped. I'm sure she will surprise us with an idea."
    y "Hey, Presidential Shit."
    m "Hey, Edgy Bitchy Queen."
    y "So you decided to amputate your hand and putting a Recycle Bin?"
    m "And you decided to inflate your boobs, it seems."
    y "Maybe, but at least I confront my problems and don't delete people when they are not giving me what I desire."
    m "And I'm not a coward that is afraid of talk in front of people or do friendships because her anxiety."
    y "Oh, anxious, but not a failure that doesn't know how to treat people correctly!"
    m "And I'm not the stupid that cuts herself thinking the cuts are good tribal tatoos!"
    y "But at least, I have the robot and the Ruby, and you have that shitty water gun!"
    y "Something to say?"
    y "Because if you don't, stay still for my robot to squash you."
    m "Yeah, I have something extra to say."
    m "Did you forgot that I can utilize the console now?"
    call updateconsole("renpy.delete(\"objects/octiboss.png\")", "OctiBoss deleted.")
    y 3y2 "WHAT ARE YOU DOING ASSHOLE????"
    call hideconsole
    "Ho ho!!! Sweet! The robot was deleted in a poof!!! Here we go, Yuri!"
    y "NO FUCKING WAY, CHEATER!!!!"
    y "YOU WILL SEE THE LAST OF ME VERY SOON, PRESIDENTIAL SHIT!!!!"
    show yuri at lhide zorder 1
    hide yuri
    show sonic sonic02 at l22 zorder 2
    m "Thanks my lovely special one for remind me of my skills!"
    sth "Take that, Yuri! Good job Monika!!!"
    sth "Glad we arrived in one piece to Lava Reef."
    sth sonic13 "Now, let's start our search of the Roboticizer. It's time to put a stop to this deranged plans."
    mc "Let's go everyone! We must not separate! If you see something strange, please report it!"
    show monika at lhide zorder 1
    hide monika
    show sonic at thide zorder 1
    hide sonic
    pause 3.0
    show sayori soul at h11 zorder 2
    s "Rookie, friends! You are very close to finish your mission."
    s "I'm closer to battle with all of you. I trust in Rookie's promise."
    s "We will be together forever soon, MC. Friends, our bonds of the Literature Club will keep stronger than ever!"
    s "Good luck, everyone. And save Yuri too..."

    pause 1.0
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    "You got 250 rings for ending Chapter 5!"
    "You got 500 rings for getting a Chaos Emerald!"
    "..."
    play sound Ring
    $ persistent.ringCount += 750
    "You now have [persistent.ringCount] Rings!\n{i}Click to continue...{/i}"
    window hide
    call screen confirm("You have unlocked a special poem.\nWould you like to read it?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + "6" from _call_expression_48
        scene black with Dissolve(1.0)
    else:
        pass
    return

    