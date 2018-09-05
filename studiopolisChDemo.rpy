# Chapter 2 static content. Poem responses called from here are in script-poemresponses.rpy

label DEMO:
    scene bg tcStardustYuri
    with dissolve_scene_full
    pause 3.0
    stop music fadeout 2.0
    scene bg stardustYuri
    with dissolve_scene_full
    show yuri 1b at t11 zorder 2
    window show(None)
    y "Hey! You finished Beta 5! Congratulations!"
    y "I hope you loved the new title card!"
    y 3d "What you see here, it's one little spoiler for my revamped route!"
    y 3y3 "The glorious route of me, Yuri!"
    y 1j "The route where I fulfill my dream of creating my Yuri Empire."
    y 2u "I wish my little cupcake can join me in my vision for the purple, perfect world."
    y 1y6 "What, I'm missing something?"
    y 3y2 "OH NO! I forgot the music!!!"
    y 4d "Sorry, I was thinking on my little cupcake and in the world order I was trying to submit here, and how everyone will share my vision and..."
    y 3y2 "OH NO!"
    y 4c "SORRY! I'm rambling again!" 
    y "Why this always happens to me?"
    y "I'm not accustomed to narrate a lot, specially if it's my own story..."
    y 1w "I need to focus, Yuri..."
    $ dj_name = "DJ-NeoMetal"
    y 1s "Let's check the mod variables!"
    if persistent.packagedMusic == True:
        play music yuriStardustKP
        show neometal djNeo at l31 zorder 5
        y 1d "You have the EDM Session active, my fellow Yurist! What do you have for me, DJ Neo?"
        dj "Now we are playing: {i}Knife Party - Boss Mode{/i}, the song for Secretive Speedway."
        y "What a good noise! I'm starting to love the tunes of these Knife Part..."
        y 1e "..."
        y 1y7 "DID YOU SAID KNIFE PARTY? ARE YOU JOKING ABOUT MY GUILTY PLEASURE OF KNIVES???"
        y 1y3 "Very. Very. Very, very funny, player. Very."
        y 2y3 "I will let this joke pass, ok?"
        dj "Is my work finished here, boss?"
        y natsuAngry "Yes, yes, yes. You can go."
        y natsuPro "Bring more music from those lovers of knives for Beta 6.66, ok DJ?"
        show neometal at lhide zorder 1
        hide neometal
    else:
        y 1d "Oh, the EDM session is disabled!"
        y 1c "Well, without further introduction..."
        play music yuriStardustHue
        y natsuPro "Let the HUE HUE HUE festival start!!!"
        y "HUEHUEHUEHUEHUEHUE\nHUEHUEHUEHUEHUEHUE"
    y cuts2 "Now that the music is introduced..."
    y cuts1 "Welcome to Secretive Speedway!!!"
    y cuts2 "My own take of Stardust Speedway Zone!"
    show emerald timeStoneBlue at h31 zorder 2
    y 1k "I got an early advantage for my route. I'm colonizing Little Planet."
    y "My holy Empire of the Yurism Cult will be established here on this planet."
    y 1h "I'm renaming all the zones of this place to things that are more like me and my poetry style."
    y 1k "And I will be using this shiny Time Stones on my way to my dream."
    y "The Time Stones are special jewels from this world that can control the flow of Time, but only on Little Planet."
    y 1y3 "BUT THANKS TO THE POWER OF THE RUBY, I CAN EXPAND THEIR AREA OF EFFECT TO ALL OF SONIC'S WORLD!"
    y "And the Time Stones don't repel the power of the Ruby! In fact, I can enhance them! And also..."
    show emerald at thide zorder 1
    hide emerald
    show emerald timeStoneBlack at h31 zorder 2
    y natsuPro "I CREATED A NEW TIME STONE, THE BLACK ONE!"
    y "The black one absorbs the energy of the Ruby and enhances the original 6, and let's me colonize the base that Dr. Eggman left here on the first invasion of him."
    show emerald at thide zorder 1
    hide emerald
    y 1g "Oh, I'm missing another thing..."
    y 3c "OH YEAH! I have propaganda for my own Empire!"
    y 4e "You MUST check it out!!!"
    show poster yuriPoster1 at t11 zorder 3
    y "What do you think? This makes me feel cool in my non school outfit!"
    y "Be cool and join the Yuri Empire, bro! Feel the wave and stuff!"
    show poster yuriPoster2 at t11 zorder 3
    y "Oh! This is made by fellow followers of me!"
    y "There are inhabitants on this planet. Those cute and handsome men formed their Holy Yuri Empire!"
    y "I'm so glad of being the goddess of them! I will soon have people for trying stuff that I was doing with my pens..."
    y "And they think a LOT in me. I'm flattered. Don't you worry guys! I will satisfy your desires {i}very soon{/i}."
    show poster at thide zorder 1
    hide poster
    y 3y2 "UWAAAAAAAAAAAAAAA!"
    y 4c "OH NO, WHY MY HORMONES TREASON ME AGAIN???"
    y "I should stop filling all the ambiences with jazmine arometherapy essence..."
    y 1a "Well... anyways, the Beta 5 ends here."
    y 1b "See you soon on Beta 6.66, the revamp and expansion of my Empire!"
    show yuri 1y3 at face(y=600) with dissolve
    y "THE YURISM CULT WILL BE FORMED WITH BLOOD, JAZMINE AND PASSION!"
    y "THE HEROES AND THE ENEMIES WILL LOSE, AND THE NEW PURPLE ORDER WILL RISE!"
    show yuri 1b at face(y=600)
    y "Let's recite the Fundaments of the Yurism!"
    show yuri 1l at face(y=600)
    y "You will stay true and loyal to Yuri, and act as She would want Her followers to act."
    y "You will propagate the struggle against all enemies of the Yurians, the fucking recycle bin with legs and their followers, the Monikans."
    y "Also you will not support the Resistance, or the Eggman Empire."
    show yuri natsuPro at face(y=600)
    y "You will recognize and respect the rights of the allies to Her cause, the Natsukians, and my goddess, the lovely Cupcake Girl."
    show yuri 1r at face(y=600)
    y "You will protect and support all Yuri worshippers and devotees, both in and out of the Empire."
    y "And the most important one."
    show yuri 1y3 at face(y=600)
    y "You will submit to the desires of your goddess, Yuri, and you will bring me PENS! LOTS OF PENS!!!!"
    show yuri 4e at face(y=600)
    y "If you are loyal to me, maybe I will let you have fun with one."
    y "See you in the next build, player..."
    window hide
    $ dj_name = "Dj-Honey"
    play sound ruby
    pause 3.0
    show yuri cuts6 at face(y=600)
    pause 0.5    
    $ renpy.quit(0)
    return
