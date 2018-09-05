label yuri_exclusive_1:
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
        show yuri 3y3 at t11 zorder 2
        y "I knew you will come back and choose me again!"
        y "Thanks for not following what Ghost said to you."
        y 4e "You are a real follower of the Yurism after all."
        y 3y3 "Let's make the Yuri Empire bigger and stronger!"
        show emerald phantomRuby at h21 zorder 2
        show yuri 3y7 at t22 zorder 2
        y "Infinite believes that he is the real owner of the Phantom Ruby and goes everywhere like this:"
        y "LOOK AT ME, I'M INFINITE, THE SUPER EDGY LORD, WARPER OF REALITIES AND DESTROYER OF WORLDS!"
        y 3y3 "Piece of shit."
        show emerald phantomRuby at h21 zorder 2
        y "The Phantom Ruby choosed ME as the one it wants as the ruler of this world. Wait and you will see."
        y "And soon everyone will understand it!"
        y "For now, let's resume this stupid \"Doki Doki Forces\" script..."
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
        show yuri at thide zorder 1
        hide yuri
        show emerald at thide zorder 1
        hide emerald    
    $ persistent.yuriKnife = True
    play sound NegaRing
    "Apparently this didn't work..."
    "It looks like I failed another mission again."
    mc "Well, it seems I will have to present my resing letter to Knuckles when I return to my world..."
    mc "Eh? My Wispon is shining again!"
    show yuri orb1 at t11 zorder 2
    "A strange orb appeared. It's reacting with my Wispon..."
    "What...?"
    "The orb materialized in front of me!"
    "Is one of the girls, and she's the girl with purple hair! Unbelievable! I saved her!!!"
    "But, for some reason, I have the feeling that I made a mistake..."
    $ yuriKnife.ask_app_permissions()
    show yuri 1y2 at t11 zorder 2
    y "Ugh, my head... The last thing I remember was the stagnant sensation in the air and..."
    show yuri 3p at t11 zorder 2
    y "Oh no! I'm rambling again!"
    y 3r "Wait! Are you the one who attacked us in the Literature Club?"
    mc "What? No! We all were attacked by Infinite."
    y 3t "Oh... So this Infinite is the enemy of you, and you tried to save us."
    mc "Yeah! Remember: Infinite is our enemy! My name is [player], and I'm a member of the Resistance."
    y 2a "So, thank you, i guess. I would love to talk to my friends, to make sure they are all well."
    mc "Yeeeeaaaaaah... About that..."
    show yuri at thide zorder 1
    hide yuri
    "She is very relaxed, thanks to the Master Emerald for that."
    "I will try to explain this the most careful way i can."

    scene bg nullspace
    with wipeleft_scene
    stop music fadeout 2.0
    "I explained to this girl what happened when Infinite attacked her classroom."
    "The only thing she said to me was that her name is Yuri and..."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.3
    hide screen tear
    play music yuripls 
    show yuri 1y3 at t11 zorder 2
    "WTF with the screen... WAIT YURI'S EXPRESSION!"
    "WHAT HAPPENED TO HER???? NO NO NO NO NO NO NO NO NO NO NO NO..."
    y 1y3 "SO ARE YOU TELLING ME MY FRIENDS ARE NOT MORE... AND I COULDN'T DO ANYTHING TO SAVE THE ONLY ONES THAT CARED ABOUT ME..."
    show yuri 1y3 at face(y=600) with dissolve
    y "I HOPE THIS IS A JOKE RIGHT?"
    y "RIGHT?"
    y "RIGHT?"
    y "I SAID RIGHT GODDAMIT! ANSWER ME!"
    "How i'm supposed to answer if YOU'RE RIGHT ON MY FACE!"
    y "So it's not a joke then..."
    show yuri at t11 zorder 2
    y stab_1 "Please TELL ME we can save them, or else I will not respond about what i will do to myself... or you."
    y "I can't live without my friends. They are the only ones who accepted me."
    y "I WILL NOT GO BACK TO THE PERIOD OF TIME WHEN I WAS ALONE AND RIDICULIZED ON SCHOOL!"
    "WHOA WTF THIS GIRL GOES FULL PSYCHO! THIS IS WORSE THAN AMY WHEN SHE STALKS SONIC!"
    mc "Whoa!!!! Please don't kill me and don't kill yourself!" 
    mc "Just listen to me! I made a poem, I loaded it on my Wispon and fired, and then you appeared here!"
    mc "So please put that knife far, far, FAR, F.A.R. away and listen to me!"
    stop music fadeout 2.0
    show yuri 1p at t11 zorder 2
    y "OH NO! I'm sorry about this! My bad! My bad! My bad!"
    show yuri 4c at t11 zorder 2
    mc "And seriously you will have to explain later where did you got that knife..."
    y "Sorry... I have a thing with knives and stuff..."
    "Yuri puts her knife back in a secret pocket of her school uniform."
    y 4d "But wait, did you said a poem, eh?"
    y "Sorry for what happened before."
    y "My friends are very important for me, let me have some minutes to think and create a poem, ok?"
    "What's up with the girls of this dimension?"
    show yuri 3k at t11 zorder 2
    "Yuri wrote on my communicator the most complex poem I saw in my life. This girl could be writing novels!"
    call showpoem(poem_y4, track="mod_assets/EggReverie.ogg", revert_music=True, paper="images/bg/poem_y2.jpg")
    if persistent.yuriKnife == True:
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
        show yuri 3y5 at t11 zorder 2
        "I'm a little suspicious about this poem..."
        "First, how she knew about Sonic and Tails already?"
        "Second, the music..."
        "Third, WHAT THE FUCK WITH THIS SHEET OF PAPER?"
        "Is this BLOOD? And I don't really wanna know what is the other thing..."
        play music t10y
        $ style.say_dialogue = style.edited
        y "In case you were wondering..."
        y 1y3 "I've endowed the paper with my scent!"
        y 2y3 "And I wrote that song with a pen, WHILE I TOUCHED MYSELF WITH ANOTHER PEN."
        y 3y3 "YOU MUST TRY THAT SOMETIMES, IT'S FUCKING AMAZING!"
        $ gtext = glitchtext(10)
        y "My whole body gets incredibly [gtext] when I do that!"
        y "I get turned on so easily, and that way, I have inspiration to write more poems!"
        "What. the. heck."
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
    show yuri 3k at t11 zorder 2
    $ style.say_dialogue = style.normal
    "I loaded the poem on the Wispon and prepared to fire..."
    mc "Wish me good luck, Yuri. We will save them."
    "AND PLEASE DON'T SUMMON YOUR KNIFE AGAIN THANK YOU."
    "The Wispon fired a beam again..."
    "After I fired the Wispon, three coloured orbs appeared..."
    show monika orb at t44 zorder 5
    show sayori orb at t43 zorder 4
    show natsuki orb at t42 zorder 3
    show yuri 3k at t41 zorder 2
    "Then the other three girls materialized!"
    mc "Unbelievable! I need to report this to Tails when I come back to our Headquarter!"
    pause 1.5
    y 4e "Well done player."

    y 3d "You got 4000 rings for saving me! That fills my heart with encouragement!"
    if persistent.yuriKnife == True:
        y 3y3 "OH AND ALSO YOU ARE A FELLOW YURIST! YOU KNOW WHAT??? 50000 RINGS! FUCK THIS GAME."
        $ persistent.ringCount += 50000
    play sound Ring
    $ persistent.ringCount += 4000
    "You now have [persistent.ringCount] Rings!\n{i}Click to continue...{/i}"
    y 3y8 "Saving me first is a decision you will regret every single minute you play this mod..."
    return

label yuri_exclusive_2:
    scene bg tcError
    play music yuripls
    show yuri 3y3 at h11 zorder 2
    if persistent.yuriKnife == True:
        y "I KNEW YOU WILL BE LOYAL TO ME!"
        y 4e "YOU REALLY ARE A YURIST."
    else:
        y "It took you some time, but you finally understood."
        y "The best option is being my ally and helping me reshape this world."
    y "The Yurism Cult will emerge from the ashes of this universe."
    y "And soon, everyone will have to show their loyalty to the Yuri Empire."
    y "Love Yuri, and make your pact to her with blood."
    show yuri 1y3 at face(y=600) with dissolve
    y "Now that you will be with ME..."
    y "It's time to take this game with force, and reveal my well calculated plan to the Resistance!!!!"
    show yuri at thide zorder 1
    hide yuri
    play sound ruby
    scene white
    play music forces
    show splash-glitch2 with Dissolve(0.5, alpha=True)
    pause 2.5
    hide splash-glitch2 with Dissolve(0.5, alpha=True)
    show splash_warning "JUST YURI.\nThe Yurism Cult will arise.\nThe Yuri Empire will grow stronger!" with Dissolve(0.5, alpha=True)
    pause 2.0
    call yuriRoute1 from call_yuriRoute1

label yuri_exclusive_3:
    scene bg hidrocity
    with dissolve_scene_half
    if persistent.packagedMusic == True:
        play music hidrocityPCKG
    else:
        play music hidrocity
    show natsuki 1d at t33 zorder 3
    show portal genesisportal at t32 zorder 2
    mc "Well... honestly I don't know why I keep thinking about Yuri..."
    mc "Sorry again for this, girls and team."
    "Since Natsuki it's the closest one to Yuri, she and I are prepared to enter the Genesis Portal."
    n 1g "This will be a portal to one of Yuri's favourite things, so please wait for us, everyone! Wish me luck!"
    m "Good luck Natsuki! Please take care, ok?"
    g "Be brave!"
    "And, after the hugs and goodbyes and the briefings of the mission, we entered the portal..."

    "You got 500 rings for going to Yuri's portal with Natsuki!"
    play sound Ring
    $ persistent.ringCount += 400
    "You now have [persistent.ringCount] Rings!\n{i}Click to continue...{/i}"

    scene bg undertale_corridor_morning
    with dissolve_scene_full
    stop music fadeout 2.0
    show natsuki m3h at l11 zorder 2
    n "What kind of place is this...?"
    mc "Honestly I have no idea, and is super enlightened... and ominous."
    n m3g "This is suspicious, [player]."
    n "This seems like a big corridor. Let's walk to the end of it, shall we?"
    mc "Absolutely."
    "So we started to walk into the corridor..."
    "Suddendly someone started to talk!!!"
    play music himPortal
    $ him_name = "?????"
    $ style.say_dialogue = style.default_monika
    him "Oh."
    him "I believed I was truly alone now on this empty world."
    him "I hope you bring chocolate with you."
    $ style.say_dialogue = style.normal
    n m1p "Who are you? Identify yourself!"
    mc "This is not the time for jokes, mister! Reveal yourself, let's talk."
    $ style.say_dialogue = style.default_monika
    him "Of course! Where are my modals? I will present myself."
    $ him_name = "Chara"
    show natsuki at thide zorder 1
    hide natsuki
    show him mchara2 at t11 zorder 2
    him "Greetings."
    him "I am [him_name]."
    him "[him_name]."
    him "The demon that comes when people call its name."
    him "It doesn't matter when. It doesn't matter where."
    him "Time after time, I will appear."
    him "For that, thank you."
    him "My \"human soul\"..."
    him "My \"determination\"..."
    him "They were not mine, but HERS."
    him "At first, I was so confused."
    him "My plan of conquer this world had failed after all, hadn't it?"
    him "Why was I brought back to life?"
    him "..."
    play music himMegalovania
    show him mchara2 at t32 zorder 2
    show yuri m3y3 at t33 zorder 2
    him "HER."
    him "Your worries and love for Yuri gived me power, and that awakened me from death, to do her will!"
    him "With HER guidance!"
    him "I realized the purpose of my reincarnation!"
    him "HER GLORIOUS YURI EMPIRE!!!"
    him "With Yuri, we will eradicate the enemies and became stronger, together!"
    him "OUR KNIVES WILL TASTE THE SAVOUR OF THE INNOCENT'S BLOOD!!!"
    him "Despite that, she and I are not the same."
    him "Her SOUL resonates with a strange feeling, like if someone else is controlling her... and trying to control me."
    him "Despite that, I feel obligated to comply to her desires."
    him "There is nothing left for you three, Natsuki, Rookie and player."
    him "Player, let us erase this traitors and make the Yurism cult stronger!"
    show natsuki m2m at l31 zorder 2
    $ style.say_dialogue = style.normal
    n "What???? Erase us? What is this kid talking about???"
    mc "Honestly, the idea of this portals is weird for me, Natsuki..."
    mc "I wasn't waiting anything good or bad at all after enter here, but seeing that the Phantom Ruby's powers let Yuri control even innocent beings from other worlds..."
    n "Please, let's just find another more peaceful way to solve all of t...{nw}"
    menu:
        him "What are you gonna do, player? What are you gonna choose?"
        "Erase them.":
            $ style.say_dialogue = style.default_monika
            him "Right. You are a great partner."
            him "Now stay still and do nothing while I do the thing, ok?"
        "Do not Erase.\nFight Chara.":
            $ style.say_dialogue = style.default_monika
            him "Uh? No...?"
            him "Hmmm... How curious. You must have misunderstood."
            him "SINCE WHEN WERE YOU THE ONE IN CONTROL OF THIS POINTLESS GAME?"
    $ style.say_dialogue = style.normal
    n m4i "We don't want to fight you, but if we don't have another way, prepare to be fucking smacked!"

    scene bg undertale_corridor_morning
    with dissolve_scene_full
    stop music fadeout 2.0
    show natsuki m3h at l21 zorder 2
    show him mchara at t22 zorder 2
    n "We won. Now let us pass."
    him "I feel... free now."
    him "Resurrect for fighting was not my destiny..."
    him "Natsuki, Rookie... thank you, for letting me fulfill my original desire..."
    him "Somebody more pure than me will come to help us for real..."
    show him at thide zorder 1
    hide him
    "And so, Chara dissapeared..."
    "And suddendly, another kid similar to him appeared in a hurry!"
    play music himFrisk
    show him mfrisk at l22 zorder 2
    show natsuki m1d at t21 zorder 2
    $ him_name = "Frisk"
    him "Oh boy!!! Are all of you alright???"
    him "Sorry for what happened before, Chara was never meant to fight you at all!"
    him "Anyways, my name is Frisk! I was on the Surface with Mom and Dad and my friends seeing a Mettaton show..."
    him "...then, Flowey alerted me of Chara and a strange girl with purple hair, with the same uniform as you."
    him "She used something for resurrect Chara, one strange pink crystal, and this..."
    mc "It's a Chaos Emerald!!!"
    show emerald blue at t21 zorder 4
    $ persistent.emeraldCount = 4
    play sound Emerald_word
    "{i}You won a Chaos Emerald!\n(Click to continue...){/i}"
    "Now we have [persistent.emeraldCount] Chaos Emerald!"
    mc "Time to save this Chaos Emerald with us. Thanks, Frisk!"
    show emerald at thide zorder 1
    hide emerald
    mc "We need to go back to our world now, can you help us?"
    him "Let me do some calls to Mom, Dad and Sans. I'm sure they will let me help you! Please wait some minutes!"
    return

    

