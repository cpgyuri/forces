image mask_child:
    "images/cg/monika/child_2.png"
    xtile 2

image mask_mask:
    "images/cg/monika/mask.png"
    xtile 3

image mask_mask_flip:
    "images/cg/monika/mask.png"
    xtile 3 xzoom -1


image maskb:
    "images/cg/monika/maskb.png"
    xtile 3

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image monika_room = "images/cg/monika/monika_room.png"
image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png"
    function monika_alpha

image room_glitch = "images/cg/monika/monika_bg_glitch.png"

image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")

image bg beach = "mod_assets/beach/beach01.png"
image bg beach2 = "mod_assets/beach/beach02.png"

image bg stardustBF = "mod_assets/stardustSpeedway_BF.png"

image monika toyChica = im.FactorScale("mod_assets/just_toychica_dark.png",0.625)
image yuri end_sprite = im.FactorScale("mod_assets/spooky_yuri.png",0.625)
image yuri_scare = "mod_assets/yandere_speedwayBF_creepy.png"

label MonikaSong:
    stop music fadeout 2.0
    scene bg studiopolis2
    with dissolve_scene_full
    play music monikaSong
    "Tee Lopes feat. Monika - Monika's Weather Machine\nSonic Mania's Eggman Boss 2 vs Your Reality."
    show monika 5a at t43 zorder 5
    show natsuki 5x at l42 zorder 4
    show yuri 3y3 at l44 zorder 2
    show sayori 4j at l41 zorder 3
    m 5b "IT'S SHOWTIME!"
    show monika 4b at t43 zorder 5
    show natsuki 1a at t42 zorder 4
    show yuri 1a at t44 zorder 2
    show sayori 1a at t41 zorder 3
    m "Okay, everyone! Let's listen to the new track I did for the Boss fight song."
    show natsuki at lhide zorder 1
    show yuri at lhide zorder 1
    show sayori at lhide zorder 1
    hide sayori
    hide yuri
    hide natsuki
    show monika 1a at t11 zorder 2
    m 1a "Every day, I imagine a future where I can be with you..."
    m 1b "In my hand is a pen that will write a poem of me and you..."
    m 2q "The ink flows down into a dark puddle..."
    m 3k "Just move your hand - write the way into his heart!"
    m 2q "But in this world of infinite choices..."
    m 1n "What will it take just to find that special day?"
    m 2a "What will it take... just to find... that special day?"
    show monika 5a at h11 zorder 2
    m "C'mon guys and girls, dance to this funky tune!"
    show monika 4b at h41 zorder 2
    m "Have I found everybody a fun assignment to do today?"
    show monika 4j at h44 zorder 2
    m "When you're here, everything that we do is fun for them anyway..."
    show monika 2p at h43 zorder 2
    m "When I can't even read my own feelings..."
    show monika 1m at h42 zorder 2
    m "What good are words when a smile says it all?"
    show monika 2r at h11 zorder 2
    m "And if this world won't write me an ending"
    show monika 5a at h11 zorder 2
    m "What will it take just for me to have it all?"
    show monika 4b at t11 zorder 2
    m "Now Natsuki, the flute part!"
    show monika 1j at t22 zorder 3
    show natsuki 4y at l21 zorder 2
    "{i}Natsuki plays her flute solo.{/i}"
    show monika 1j at t33 zorder 4
    show sonic sonic14 at l32 zorder 3
    show natsuki 4y at t31 zorder 2
    sth "Hey girls! This arrangement of my song is amazing! C'mon, step it up!"
    sth sonic02 "OH YEAH THIS IS HAPPENING!"
    show monika 1j at t22 zorder 2
    show natsuki at lhide zorder 1
    show sonic at lhide zorder 1
    hide natsuki
    hide sonic
    m 5a "Now the last part!"
    show monika 2q at t43 zorder 2
    show natsuki 1d at l42 zorder 3
    show yuri 1d at l44 zorder 4
    show sayori 4s at l41 zorder 5
    m "The ink flows down into a dark puddle..."
    m 2n "How can I write love into reality?"
    m 1q "If I can't hear the sound of your heartbeat..."
    m 1r "What do you call love in your reality?"
    m 2o "And in your reality, if I don't know how to love you..."
    show monika 2p at f43 zorder 2
    show natsuki 4n at t42 zorder 3
    show yuri 2s at t44 zorder 4
    show sayori 1y at t41 zorder 5
    m "I'll leave you be..."
    show monika 2q at h43 zorder 2
    show natsuki 1d at h42 zorder 3
    show yuri 3d at h44 zorder 4
    show sayori 4s at h41 zorder 5
    m 1k "GOOD JOB EVERYONE! I LOVE YOU GIRLS!"
    n 2y "THAT WAS THE MOST PRO THING EVER!"
    s 4p "NOW LET'S EAT NATSUKI'S CUPCAKES, I'M HUNGRY!"
    show monika 1l at h43 zorder 2
    show natsuki 5v at h42 zorder 3
    n "SAYORI LEAVE MY CUPCAKES ALONE!!!!!"
    mc "OK girls, and... ending recording!"

    return

label YuriSong:
    stop music fadeout 2.0
    scene bg club_day2_2
    show sayori 2f at t41 zorder 2
    show natsuki 4f at t42 zorder 2
    show monika 3g at t44 zorder 2
    with dissolve_scene_full
    m "Here we are in the clubroom... again."
    s "Are you sure that Yuri is here, Rookie?"
    n "Rookie! Why those shitty things that Tails build always fail in the most important moments?"
    mtp "MY WORK IS NOT SHITTY, THANK YOU."
    mc "According to MILESELECTRIC, Yuri IS here!"
    show yuri 1s at l43 zorder 2
    y "Hi, Rookie!"
    y "Thank you for coming back!"
    y 1y3 "And you arrived with guests! How lovely!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound NegaRing
    pause 0.3
    hide screen tear
    show yuri 1y3 at face(y=600) with dissolve
    show sayori 4w at t41 zorder 2
    show natsuki 1p at t42 zorder 2
    show monika 5b at t44 zorder 2
    y "IT'S TIME FOR SHOW YOU ALL MY NEW POEM!"
    play sound djstop
    y 1y7 "WAIT! What's up with that poster on the background? Are you joking with me again???"
    y "Room magic! Change scene!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    pause 0.3
    hide screen tear
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_room
    show monika_room_highlight
    show sayori 4w at t41 zorder 2
    show natsuki 1f at t42 zorder 2
    show monika 5b at t44 zorder 2
    show yuri 1y3 at t43 zorder 3
    m "Wait a minute, this is my secret room! You cheater!"
    show yuri 1b at t43 zorder 3
    $ style.say_dialogue = style.edited
    y "It's time for the Literature Club to stop giving me feedback..."
    y "...stay silent, and let me rewrite this world in my own way."
    $ style.say_dialogue = style.normal
    show sayori at thide zorder 1
    show natsuki at thide zorder 1
    show monika at thide zorder 1
    show yuri at thide zorder 1
    hide yuri
    hide sayori
    hide natsuki
    hide monika
    show sonic sonic09 at t43 zorder 2
    show tails tails04 at t41 zorder 2
    show amy amy06 at t44 zorder 2
    show shadow shadow05 at t42 zorder 2
    sth "Oh no! We arrived too late!"
    mtp "Sonic, look! Our friends!"
    sha "Stop using your pink magic and come here for a fair fight, Yuri!"
    show yuri 1b at t11 zorder 3
    $ style.say_dialogue = style.edited
    y "All of you will be an awesome audience, stay still, and listen to my new poem, right?"
    $ style.say_dialogue = style.normal
    mc "Welcome to Doki Doki Forces..."
    y 4a "AND JOIN MY YURI EMPIRE, PLEASE..."
    show sonic at thide zorder 1
    show tails at thide zorder 1
    show amy at thide zorder 1
    show shadow at thide zorder 1
    hide sonic
    hide tails
    hide amy
    hide shadow
    show yuri 1r at t11 zorder 2
    play music finalBoss
    show neometal djNeo at l31 zorder 2
    $ dj_name = "DJ-NeoMetal"
    dj "Now Playing:\n{i}6thirtyAM - The Marionette (Instrumental){/i}."
    dj "Check 6thirtyAM's amazing songs at:\nhttps://soundcloud.com/6thirtyam/"
    show neometal at lhide zorder 1
    hide neometal
    $ dj_name = "DJ-Honey"
    y 2r "{i}Love me. Breathe me. Kiss me. TOUCH ME.{/i}"
    y 3y5 "{i}FEEL MY KNIFE IN YOUR THROAT.{/i}"
    y 1c "{i}I will cut your skin open and crawl inside you.{/i}"
    y 1s "{i}Please accept my confession.{/i}"
    y 1l "Yuri’s here, and I'm singing what I wanted to feel."
    y 1m "Turning angles into endless pits;"
    y 1h "Gearboxes falling from these holy stakes;"
    y 2a "Endless portals to another worlds;"
    show yuri at thide zorder 1
    hide yuri
    show sonic sonic07 at t43 zorder 6
    show tails tails07 at t41 zorder 6
    show amy amy02 at t44 zorder 6
    show shadow shadow03 at t42 zorder 6
    y "Strange heroes fighting against me;"
    show sonic at thide zorder 1
    show tails at thide zorder 1
    show amy at thide zorder 1
    show shadow at thide zorder 1
    hide sonic
    hide tails
    hide amy
    hide shadow
    show sayori 1g at t41 zorder 2
    show natsuki 12d at t43 zorder 2
    show monika 1o at t44 zorder 2
    show mc2 1f at t42 zorder 2
    y "My friends are tied to these thickened ropes;"
    show sayori at thide zorder 1
    show natsuki at thide zorder 1
    show monika at thide zorder 1
    show mc2 at thide zorder 1
    hide sayori
    hide natsuki
    hide monika
    hide mc2
    show yuri 4d at t11 zorder 2
    y "I'm controlled by the Ruby’s wrath…"
    y 4e "I'm her Marionette..."
    y cuts2 "My mind is getting filled with these"
    show black zorder 3
    show bg eyes_move zorder 4
    y "HAPPY THOUGHTS HAPPY THOUGHTS\nHAPPY HAPPY HAPPY THOUGHTS"
    hide bg eyes_move
    hide black
    y cuts2 "I wanted to embrace all of these"
    y cuts1 "HAPPY THOUGHTS HAPPY THOUGHTS\nHAPPY HAPPY HAPPY THOUGHTS"
    y dragon "Third Eye is tempting me with these"
    show mik_exe_scene zorder 3
    y "HAPPY THOUGHTS HAPPY THOUGHTS\nHAPPY HAPPY HAPPY THOUGHTS"
    hide mik_exe_scene
    show y_kill_forces zorder 3
    y "Get inside my head and give me"
    hide y_kill_forces
    y 4e "HAPPY THOUGHTS HAPPY THOUGHTS\nHAPPY HAPPY HAPPY THOUGHTS"
    show sayori 2s at l41 zorder 2
    s "Yay! Happy thoughts!"
    y natsuAngry "SHUT UP SAYORI, THIS IS MY POEM!"
    show sayori at lhide zorder 1
    hide sayori
    y 1k "Forty gears, spinning wheels and a ticking clock;"
    y 2k "Bloody prayers written in these harness torns;"
    y 3y3 "The Dark Cloud drinks my breathing blood;"
    y yuriIllusion "Have you ever heard of a warmer ghost?"
    show yuri at thide zorder 1
    hide yuri
    show monika g1 at i11 zorder 2
    y "Monika failed to reprogram the script;"
    show monika at thide zorder 1
    hide monika
    show yuri 3y3 at t11 zorder 2
    y "My mind is giving up to the glitched code;"
    y cuts2 "Touch my body with your stolen pen!"
    show darkred zorder 5:
        alpha 0.0
        easein 4.0 alpha 1.0
    $ style.say_dialogue = style.edited
    y cuts4 "Have you considered killing yourself???"
    show room_glitch
    show yuri cuts6 at face(y=600) with dissolve
    y "The flickering light no longer shines!!!"
    y "Raccoon is hungry for my slice of blood!!!"
    y "The breeze is not gentle and the sand is dry!!!"
    y "Drive the knife into my flesh, make me a mess!!!"
    y "Breathing human eyes, skies and gods!!!"
    y "Diabolist sticks, curial pentagraphs!!!"
    y "HEY NATSUKI..."
    hide darkred
    show black zorder 3
    show y_glitch_head zorder 4:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    y "Who cares about you, obnoxious brat???"
    $ style.say_dialogue = style.normal
    hide black
    hide y_glitch_head
    hide room_glitch
    show monika_room
    show monika_room_highlight
    show yuri cuts2 at t11 zorder 7
    y "My mind is getting filled with these"
    show menu_bg_ghost zorder 5
    show menu_bg_ghost2 zorder 5
    y cuts1 "HAPPY THOUGHTS HAPPY THOUGHTS\nHAPPY HAPPY HAPPY THOUGHTS"
    y cuts3 "I wanted to embrace all of these"
    y cuts1 "HAPPY THOUGHTS HAPPY THOUGHTS\nHAPPY HAPPY HAPPY THOUGHTS"
    y cuts5 "Third Eye is tempting me with these"
    y cuts1 "HAPPY THOUGHTS HAPPY THOUGHTS\nHAPPY HAPPY HAPPY THOUGHTS"
    y cuts2 "Get inside my head and give me"
    y glitch "HAPPY THOUGHTS HAPPY THOUGHTS\nHAPPY HAPPY HAPPY THOUGHTS"
    hide menu_bg_ghost
    hide menu_bg_ghost2
    show yuri at thide zorder 1
    hide yuri
    $ style.say_dialogue = style.normal
    show natsuki 42f at t32 zorder 4
    show sonic sonic07 at t33 zorder 3
    show eggman eggman07 at f31 zorder 3
    egg "EGG FORCES! RED ALERT! THE EMPIRE IS IN DANGER!!!"
    show natsuki 42f at t32 zorder 4
    show sonic sonic07 at f33 zorder 3
    show eggman eggman07 at t31 zorder 3
    sth "WE WILL STOP YURI, FOR THE RESISTANCE AND OUR WORLD!"
    show natsuki 42f at f32 zorder 4
    show sonic sonic07 at t33 zorder 3
    show eggman eggman07 at t31 zorder 3
    n "Rookie, please SAVE YURI, she's not like this!!!"
    show eggman at thide zorder 1
    show sonic at thide zorder 1
    show natsuki at thide zorder 1
    hide natsuki
    hide sonic
    hide eggman
    show gfm rexe10 at face(y=600) with dissolve
    $ style.say_dialogue = style.edited_mik
    mik2 "Look at these morons, and how they are destroying themselves!"
    mik2 rexe11 "My work here will be WAY easier, ehehe~!"
    show gfm at thide zorder 1
    hide gfm
    $ style.say_dialogue = style.normal
    show tsun 8yu at t11 zorder 2
    krazy "I'm here making a cameo!!! Do you want Kraft Dinner?"
    show tsun at thide zorder 1
    hide tsun
    show yuri glitch at t11 zorder 2
    $ style.say_dialogue = style.edited
    y "Your minds will soon obey to my"
    y cuts6 "HAPPY THOUGHTS HAPPY THOUGHTS\nHAPPY HAPPY HAPPY THOUGHTS"
    y "You will be forced to embrace all my"
    show bg eyes_move zorder 4
    y "HAPPY THOUGHTS HAPPY THOUGHTS\nHAPPY HAPPY HAPPY THOUGHTS"
    hide bg eyes_move
    y "LISTEN TO YOUR THIRD EYE AND DREAM WITH"
    y "HAPPY THOUGHTS HAPPY THOUGHTS\nHAPPY HAPPY HAPPY THOUGHTS"
    $ style.say_dialogue = style.normal
    show sayori 2f at l41 zorder 2
    show natsuki 1f at l42 zorder 2
    show monika 1i at l44 zorder 2
    show yuri stab_1 at t43 zorder 3
    y "KNIVES ARE STABING ME, I WANT THESE"
    show sayori 4w at t41 zorder 2
    show natsuki scream at t42 zorder 2
    show monika 5b at t44 zorder 2
    y stab_8 "HAPPY THOUGHTS HAPPY THOUGHTS\nHAPPY HAPPY HAPPY THOUGHTS"
    y stab_7 "HAPPY THOUGHTS HAPPY THOUGHTS!!"
    y stab_8 "HAPPY HAPPY HAPPY THOUGHTS!!!"
    y stab_7 "HAPPY THOUGHTS HAPPY THOUGHTS!!"
    y stab_8 "HAPPY HAPPY HAPPY THOUGHTS!!!"
    y oh_crap "HAPPY THOUGHTS HAPPY THOUGHTS!!"
    y what_the "HAPPY HAPPY HAPPY THOUGHTS!!!"
    show yuri at thide zorder 1
    hide yuri
    show room_glitch
    show layer master at heartbeat
    show noise zorder 99:
        alpha 0.0
        linear 3.0 alpha 0.25
    show yuri eyes zorder 6
    $ style.say_dialogue = style.edited
    y "HAPPY THOUGHTS HAPPY THOUGHTS!!"
    y "HAPPY HAPPY HAPPY THOUGHTS!!!"
    stop music
    $ style.say_dialogue = style.normal 

    return

label testingMonikaRoom:
    stop music fadeout 2.0
    $ _window_subtitle = " THE YURI EMPIRE HAS RISEN"
    scene bg stardustBF
    show yuri end_sprite at i11 zorder 2
    with dissolve_scene_full
    play music endingBadYuri
    $ dj_name = "DJ Sona"
    show honey djHoney at l31 zorder 5
    dj "Now Playing: Phonetic Hero - Sonic CD 'Your's Truly, Satan' (Boss!! US) OC ReMix - http://ocremix.org/remix/OCR02784"
    dj "The world is destroyed. Go and make Yuri yours. Congratulations... not."
    show honey at lhide zorder 1
    hide honey
    $ style.say_dialogue = style.default_monika
    y "Hey, [player]!"
    y "This is it. I did it!"
    y "My most wonderful and exciting desire, now as a fulfilled reality."
    y "The Yuri Empire has risen!"
    y "From the ruins of these crumbled speedways, the stardust will be bathed with the blood of the impures..."
    y "No more rainclouds, obnoxious brats or deranged presidents to stand in my way."
    $ style.say_dialogue = style.normal
    "The console here will show the girls deleted."
    $ style.say_dialogue = style.default_monika
    y "No more heroes trying to save the day. No more villains trying to usurping my power!"
    y "Just me. Just Yuri. Forever and ever. Just Yuri and only Yuri."
    y "Just me. Just Yuri and onl{nw}"
    show yuri_scare zorder 99
    play sound "mod_assets/fnaf6scream.ogg"
    window hide
    pause 3.0
    $ style.say_dialogue = style.normal
    $ sth_name = "Sonic.exe"
    sth "Oh oh! How unfortunate."
    sth "Oh oh! How unfortunate."
    sth "I'm gonna do a sneaky thing."
    sth "Behind the psycho I point to the hanged girl."
    sth "HAHAHAHAHAHAHAHAHAHAHAHAHA!!!"
    $ style.say_dialogue = style.default_monika
    y "Just me, pulling your skin open and crawling inside you..."
    y "Just me, satisfying all my secret desires..."
    y "Just me, loving you, and making you mine, by force..."
    y "Now, you will be a gentleman and sit here, inmobile..."
    y "While we enjoy our bodies in this sweet, sweaty and bloody embrace..."
    $ style.say_dialogue = style.normal
    sth "See you later moron! Playing with you soon!{nw}"
    hide yuri_scare
    scene bg stardustBF
    show yuri end_sprite at i11 zorder 2
    with dissolve_scene_full
    $ style.say_dialogue = style.default_monika
    y "And now, the jazmine oil fills the ambience."
    y "My lust... my emotion... my mind... I can't control them anymore."
    y "Let's enjoy the show, shall we?"
    y "We have ALL THE TIME IN THE WORLD..."
    $ style.say_dialogue = style.normal
    "..."
    "The ending credits will be here, and then, the game will be stuck here forever."
    "The same song playing, and Yuri looking at you. Forever. With lust and passion."
    "Congratulations, now you are the official lust slave of Yuri."
    "The Yuri Empire has risen. Just Yuri."
    "Comment in the server if you got this awesome ending :D."

    return

label sayorisoulEDMAvicii:
    scene white
    show mirageSaloon_glitch5
    s "I will help you in advance. First, there is this song, it's one of my favourites. Let me concentrate..."
    "Suddendly one of Sayori's memories passes through your eyes..."
    show white as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0
    scene bg avicii01
    with dissolve_cg
    play music nullSpacePCKG
    show honey djHoney at l31 zorder 5
    dj "Now playing, a special song:\n{i}Avicii - Without You feat. Sandro Cavazza{/i}."
    show honey at lhide zorder 1
    hide honey
    

    return