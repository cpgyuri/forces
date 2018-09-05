label monika_exclusive_1:
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
        y 3y2 "You were supposed to choose ME!"
        y 3y7 "You were a follower of the Yurism cult... That's it! You will feel sorry!!!!!"
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
    show monika orb at t11 zorder 2
    "A strange orb appeared. It's reacting with my Wispon..."
    "What...?"
    "The orb materialized in front of me!"
    "Is one of the girls, and she's the leader! Unbelievable! I saved her!!!"
    play music tmonika 
    show monika 2q at t11 zorder 2
    m "Ugh, my head... This Infinite dude sure has a nasty attitude."
    if persistent.genderMale == True:
        m 2c "And who are you? What kind of... strange dog are you. Did you tinted your hair with strawberries?"
        mc "I'm a {i}wolf{/i}, not a dog, thanks. And this is my real skin color."
    else:
        m 2c "And who are you? What kind of... strange bat are you. Did you tinted your hair with blackberries?"
        mc "I'm a {i}cat{/i}, not a bat, thanks. And this is my real skin color."
    m "Are you friends with that ugly Infinite?"
    mc "No! Infinite is our enemy! My name is [player], and I'm a member of the Resistance."
    mc "Which is not the same as your club, because we joined for a war and we are fighting together."
    mc "And you seem to be the leader of this {i}Literature Club{/i} group of sorts..."
    m 3a "Oh! A Resistance. That sounds very poetic. Thanks for rescuing me then."
    m 2l "And I'm not {i}the leader{/i} of the club, I'm the President. But I love to share and listen to the opinions of my friends."
    m 2b "I'm not as confident as a President like everyone in my school thinks."
    m "But I always try to do my best on everything I do. And my friends trust and support me."
    m 5a "I promised to a very special person that I will never do anything to harm my friends and make them lose their trust in me."
    m 2a "So, now, the only thing is missing is getting back to the club room and share some of Natsuki's cupcakes and Yuri's tea with you."
    m 2d "Because my friends are here somewhere and you rescued them too, right?"
    mc "Well... about that..."
    if persistent.yuriKnife == True:
        $ style.say_dialogue = style.edited
        m help "But come on! Who am I trying to lie?"
        m "I'm a failure."
        m "As friend, as a lover, as President of the Club, as a human being."
        m "I don't know why people think so high about me."
        m help2 "And I will prove to you, Rookie, that I'm useless."
        m "IF YOU HAD CHOSEN YURI, YOU WOULD NOT HAD TO LISTEN TO MY PROBLEMS."
        m "BUT HERE YOU ARE, WITH THE RECYCLE BIN WITH LEGS."
        m "ENJOY YOUR MOTHERFUCKING PRECIOUS MONIKA WHILE YOU CAN."
        m "AHAHAHAHAHAHAHAHAHAHAHAHA..."
        mc "What is happening...???"
        $ style.say_dialogue = style.normal
        $ skip_transition = True

    scene bg nullspace
    with wipeleft_scene
    stop music fadeout 2.0
    play music t9 
    show monika 2o at t11 zorder 2
    if persistent.yuriKnife == True:
        mc "What the hell did happened...?"
    "I explained to this girl what happened when Infinite attacked her classroom."
    "As the President of them, she obviously deserved a very detailed explanation of the power Infinite has and the risk of this situation."
    "Her expression changed when I mentioned she was the only one I could revive."
    m "And again, the President of the club failed to do something right for her friends and herself."
    m "Now I understand why sometimes that special person I love doesn't respond my feelings back in full force."
    mc "Hey! Don't be sad! As Knuckles says to us when we lose a battle: The war doesn't end until the credits roll."
    mc "Not that I understand what does that mean..."
    mc "I saved you by writing a poem and firing it with my Wispon. Maybe if you write a poem..."
    show monika 5a at t11 zorder 2
    m "That actually is a good idea! Let's do this!"
    "The girl wrote a poem that it seems is very abstract, but she looks very proud and determined, so..."
    call showpoem(poem_m5)
    "This poem... now I can say it! This is a poem for her love!"
    "It was easy for me to understand! Hoorray! Cheers for me!"
    "I loaded the poem on the Wispon and prepared to fire..."
    m 4b "By the way, my name is Monika."
    mc "Wish me good luck then, Monika! We will save your friends."
    "The Wispon fired a beam again..."
    "After I fired the Wispon, three coloured orbs appeared..."
    show monika 1d at t44 zorder 5
    show sayori orb at t43 zorder 4
    show natsuki orb at t42 zorder 3
    show yuri orb1 at t41 zorder 2
    "Then the other three girls materialized!"
    mc "Unbelievable! I need to report this to Tails when I come back to our Headquarter!"
    
    "You got 400 rings for saving Monika!"
    play sound Ring
    $ persistent.ringCount += 400
    "You now have [persistent.ringCount] Rings!\n{i}Click to continue...{/i}"
    return

label monika_exclusive_2:
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
    m 4g "..."
    m 2e "... This must be a joke, right?"
    m 1p "I can't believe you did a poem for me again..."
    m "I don't deserve this, [player]..."
    show monika 2o at t21 zorder 3
    "Why Monika got so sad all of a sudden? I believed she will enjoy this..."
    kte "Lady, sorry for interrumpting your monologue, but..."
    kte "If people is trusting you (and specially Rookie!), that means you are doing a good job."
    kte "Look at your friends! They are happy that you will go to rescue Sonic!"
    show natsuki 5y at l31 zorder 4
    n "And I will give you directions from here, Monika!"
    n "You will be almost as pro as ME!"
    show natsuki at thide zorder 1
    hide natsuki
    mc "And with that, Captain, I think we are ready to go. I have my partner, they have the Extreme Gears, and Natsuki will command from here instead of Monika."
    m 1n "Thanks Rookie and mr. Knuckles for trusting in me. I will give my best... for you all, my friends and the Club."
    kte "Excellent, then! Operation: Rescue is officially starting!"

    "You got 400 rings for your poem for Monika!"
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
    show monika 1c at l11 zorder 2
    "Monika and I are on Chemical Plant now."
    "I can see that Monika is worried. She really didn't looked anything on the level, she was only looking down all the time."
    "Natsuki is talking to us using Tails' communicator."
    n "This is it, [player], Monika and you will rescue Sonic!"
    n "Wait... Monika, what happen? WHY ARE YOU SO DOWN?"
    m 2g "Eh! Oh... hmmm... nothing, Natsuki, nothing..."
    m 2r "Who I'm trying to lie?"
    m 2p "Natsuki, Rookie, I don't feel that I'm capable to do this mission. What if we don't find this Sonic? What if we are ambushed by Eggman?"
    mc "Stop being worried, Monika. We are searching for a hidden passage to Eggman's Prison."
    mc "And we told you we trust you! Also Natsuki and Knuckles are checking on us. If something happens, they will teleport to help us."
    mc "So stop being worried, and enjoy the visuals! Even if this is an Eggman's building, everything has its charm."
    m 5b "NOBODY UNDERSTANDS ME!"
    m 2p "I, as the President of the Literature Club, had special powers in my world."
    m "I could change everything at my will. At first I did nasty things to my friends..."
    m "But then I promised our lovely fifth integrant of the clb to not use my powers in a bad way again!"
    n "And also we forgive you, Monika! Now we are more friends than ever!"
    m "I know it, Natsuki. But after the destruction of our world and Rookie's help..."
    m "I don't have my powers anymore."
    m 1p "And I have the idea that they would have been useful for this adventure."
    mc "DID YOU HAD HACKING POWERS IN YOUR WORLD?"
    mtp "This is Tails! Did you promise that you will not do anything to harm your friends and the members of the Resistance?"
    m 1r "I PROMISE! I REALLY PROMISE! AND I'M SO SORRY OF THIS!"
    mc "Monika, thanks for opening your feelings to us! I admire you more and more!"
    m 2g "Really, [player]?"
    m "You remind me a lot of my special and only love..."
    m "..."
    m 5a "Thanks, Rookie! I must start to trust in myself more then!"
    mtp "And I gived you access to MILESELECTRIC software! If you need to search for your special powers, you can do it from now. And also you can apply them to you!"
    mtp "I hope the remained data of your world is not so corrupted."
    m "Thanks, my friends! If this works, you will know what I'm capable to do."
    m 4b "And look! There is what seems to be the secret entrance, let's follow those robots!"

    scene bg chemicalPlant2
    with dissolve_scene_half
    if persistent.packagedMusic == False:
        play music chemPlant2
    "And so, we found the secret entrance to the prison."
    "It was hidden in the second part of the Chemical Plant, in the Liquid Process Section."
    show eggpawn eggpawn1 at t11 zorder 2
    "And as soon as we appeared, a troop of EggPawns started to ambush us!"
    show eggpawn at thide zorder 1
    hide eggpawn
    show monika 5b at h11 zorder 2
    mc "EGG PAWNS! Monika, watch out! This robots are..."
    m "Relax Rookie! {i}I HAVE A PLAN...{/i}"
    "What is Monika thinking? She seems relaxed."
    "Anyways, I prepared my Wispon and shoot at the group."
    play sound destroy
    "I released the animals of a pair of robots."
    "Monika just walked cautiosly to the bigger troop of Eggpawns."
    "Her walk and figure are pristine and sexy, if you let me comment on that."
    "Can I be distracted 5 seconds on this beautiful woman or not?"
    "Anyways, Monika looked at the robots..."
    m 4k "Hello beautiful group of robots! I like your color style!"
    m 4j "Can all of you serve me for some minutes?"
    $ consolehistory = []
    call updateconsole("MILES ELECTRIC SYSTEM ONLINE", "User: Monika.")
    pause 1.5
    call updateconsole("Searching: Monika's DDLC privileges", "Searching...")
    pause 1.5
    call updateconsole("Searching: Monika's DDLC privileges", "Data recovered! Downloading...")
    pause 1.5
    call updateconsole("Apply.privileges.President", "Monika has DDLC's presidential powers!")
    pause 1.5
    call updateconsole("renpy.control(eggpawns)", "Eggpawns are now in Monika's control.")
    pause 1.5
    m 1j "Neat, eh?"
    mc "Monika! That was amazing!"
    n "GOOD JOB PRESIDENT! OUR LOVELY MONIKA IS BACK! HOORRAY!!!"
    m 2b "Now, Eggpawns, take us to Sonic's prison cell, and then autodestruct."
    m "And also give to us all your rings."
    play sound Ring
    "Rings dropped of the robots, so I made sure to collect all."
    "So, the way to Sonic's prison cell is clear, and better: the Eggpawns are guiding us to him!"
    return

label monika_exclusive_3:
    scene bg hidrocity
    with dissolve_scene_half
    if persistent.packagedMusic == True:
        play music hidrocityPCKG
    else:
        play music hidrocity
    show monika 2e at t33 zorder 3
    show portal genesisportal at t32 zorder 2
    "Monika and I are prepared to enter the Genesis Portal."
    m 2b "Be ready and wait for us, everyone! Wish me luck!"
    n "Good luck Monika!"
    g "Be brave!"
    "And, after the hugs and goodbyes and the briefings of the mission, we entered the portal..."

    "You got 500 rings for going to the portal with Monika!"
    play sound Ring
    $ persistent.ringCount += 400
    "You now have [persistent.ringCount] Rings!\n{i}Click to continue...{/i}"

    stop music fadeout 2.0
    show white
    with dissolve_scene_full
    show monika_room_day
    show monika 26a at i11 zorder 2
    m "Where... where are we?"
    mc "Hey, this is a classroom!"
    m 26b "Why are we here in this room???"
    mc "Monika, are you feeling well? What's up?"
    m "I don't understand, Rookie. Even with my admin powers back, I couldn't..."
    m "I didn't have control or power to create this room anymore..."
    m 26c "In which place my room is in? It's warm, almost hot, and it looks like a lot of mountains there on the windows..."
    mc "Well... we are on Hill Top Zone, if I recall correctly..."
    m 26a "But I still can't believe that we are here... let me test something!!!"
    play music hilltop
    mc "Yeah, Monika, this is the song of this level! You did it!"
    m 26b "It can be... I can control the music again..."
    m "My abilities are back."
    m 26d "I don't understand... don't understand..."
    "I think that it's amazing that Monika entered her room by using the Genesis portal. I don't understand why is she so worried."
    "I was about to put my Wispon on the ground, when suddendly I found a poem on the floor."
    "Uh? It's a message from Tails!"
    mc "Monika, you need to listen to this!"
    m 26a "Rookie, it's a poem! Read it, please!"
    call showpoem(poem_m6)
    play music hilltop
    m 26e "Now I understand why Sayori loves the little furry fox."
    m "Thank you."
    m 26a "Please put my special one on screen, Rookie! I can't hold this anymore!"
    "I did as Tails said on the letter. A touch of a button, and something special happened."
    "I decided to not say anything until Monika finishes her talk."
    m 26f "Hey, my lovely special one! It's me, your girlfriend!"
    m "Thanks for being here with me in this adventure!"
    m "I know you are the one helping Rookie. Rookie, say hi to my boyfriend, he will not be jealous, I swear."
    mc "Hello wonderful person out there! Please, help me. Give strenght and peace to Monika."
    m 26g "As you can see, Rookie is a lovely person! I can say with total certain that Rookie loves my company."
    m "And you know that your super girlfriend is doing an excellent job kicking everyone's ass!"
    m "Hahahahahaha..."
    m 26h "Ha. Ha. Ha..."
    play music mend
    m 26b "Who I'm trying to say lies?"
    m "I can't do anything, my love."
    m "Since I entered this world, I don't know how to help."
    m "My insecurities, my doubts, my weak confidence and self-steem..."
    m "Everything is killing me inside."
    m 26h "Remember when I told you that I must show myself as a brave and confident person?"
    m 26i "Well, now I CAN'T. I REALLY JUST CAN'T!"
    m "Everything is my fault. Yuri is a villain, Sayori is a robot, MC is blacked out, even Ghost suffered too."
    m "The only one that is almost enjoying this is Natsuki, but she did something before that I didn't noticed!"
    m "I don't deserve to be President of the Club. I don't deserve my friends. I don't deserve the trust and support of Sonic and company."
    m 26j "I'm useless..."
    menu:
        "No!":
            pass
    menu:
        "I will always love you, Monika!":
            pass
    menu:
        "You will always be my true love.":
            pass
    menu:
        "I know you can do it!\nYou are not useless!":
            m 26b "..."
            m 26e "Thank you, my love!"
            m 26i "Don't you know how much I needed to listen this from you!"
            m 26j "I will always love you too, no mather what things happen!"
            m "I will not dissapoint you, my true love. Your girilfriend will keep being special for you!"
    
    m 26k "I feel less stressed now. You are a magician, my love."
    m 26l "I feel like I can do this!"
    mc "I'm glad that Monika is happy now! Thanks, kind person."
    menu:
        "Protect Monika, Rookie.":
            mc "Eh? Are you talking to me?"
            mc "Sure thing! I will do it!"
    
    m 26n "My love, Rookie, everyone."
    m "Thank you."
    play music hilltop
    m 26m "You know what? Let me enjoy the music of this world!"
    m "It doesn't have pianos, but is so different and funny."
    m "I love it!"
    m "I believe I can fly now!"
    m "I need to write something to conmemorate this sweet moment with my true love and Rookie!"
    menu:
        "DOKI-DOKI HEROES":
            pass

    m 26h "Sweetheart, Doki-Doki Heroes... sounds too cheesy..."
    mc "But Sonic has his SONIC HEROES catchphrase and stuff!!!"
    mc "He always believes in the power of friendship and says this a lot, and it works!"
    m 26l "Doki-Doki Heroes, eh?"
    m "Well then!"
    m 26o "WE ARE SONIC HEROES!!!"
    m "No, no... I said it wrong, hahaha!"
    m "WE ARE DOKI-DOKI HEROES!!!"
    "I captured a photo of this moment with my Wispon. Monika looks so cute! I will make sure to make it available for you!"
    "After this conversation, the intended portal appeared, and we followed it..."
    $ renpy.call_screen("dialog", "Thanks for helping me!\n\nKeep loving me.\nMy true love.", ok_action=Return())

    scene bg crashfever
    with dissolve_scene_full
    stop music fadeout 2.0
    "What a strange world is this!"
    "It's very colorful, and full of energy and positivity!"
    "Suddenly, somebody runs eager to us!"
    play music mikuPortal
    show miku mikuSprite at l21 zorder 3
    show monika 1b at l22 zorder 2
    mik "Welcome to the world of ALICE, you two!"
    mik "For this two weeks, we are running the Hatsune Miku Crossover Event in Crash Fever!"
    mik "And the star is me! Hatsune Miku in person!"
    mik "I hope you enjoy my wonderful music!!!"
    mik "What are your names?"
    m 5a "I can't believe that she is the real Hatsune Miku! Natsuki would be happy here!"
    m 2b "By the way, the friend here is called [player], but everyone calls them Rookie!"
    m "And my name is Monika, the President of the Literature Club!"
    mik "And my name, as you know, is Hatsune Miku! Why are you two here? You don't seem to be a new ALICE unit..."
    mik "Did something happened to you? Those strange portals started to appear recently. Turing and Mobius are already investigating the source of this strange things..."
    show monika 9s at t22 zorder 2
    "Monika explained to Miku the problem in our world. According to what I understand, Monika keeps thinking in her other club members and friends."
    "That's why she ended in a place that is more like a thing Natsuki would like."
    "Miku payed attention to everything Monika said."
    "It's the first time I saw Monika sad and almost crying"
    m "I'm worried about my friends and everytime I have that sensation that I'm useless and I fail my friends everytime."
    m "Do you think that you could help us, miss Miku?"
    mik "It's ok! Worry not, Monika and Rookie! Hatsune Miku is here to help both of you!"
    mik "You are a wonderful person, Monika!"
    mik "But first..."
    show miku at lhide zorder 1
    hide miku
    m 2s "Sorry for being sad, [player], I needed that."
    mc "It's ok, Monika! I admire you more because your honesty and your feelings."
    mc "And if you let express myself without being angry, your legs are beautiful..."
    m 5b "Rookie!!!! What are you seeing?????"
    m 2s "I'm joking, Rookie, thank you..."
    show monika 2s at face(y=600) with dissolve
    m "You remind me a lot of my special person, Rookie."
    m "Thanks for helping me before entering this world."
    mc "It's ok, Monika, you can trust in us!!"
    m 11s "Thank you, Rookie!"
    m 1b "I will not dissapoint you and my true love. Your friend will keep being special for you!"
    mc "Thanks for helping me to give strenght to Monika before, player!"
    show monika 1b at t22 zorder 2
    "And Miku is back!"
    show miku mikuSprite at l21 zorder 3
    mik "Sorry for making you wait!!!!"
    mik "I was getting something that I think is more useful for you than everyone here..."
    mik "Please, let me gift you that something! Tra lala!"
    "Suddendly, an strange rainbow egg appeared in front of Monika!"
    show pictures crashfeveregg at t22 zorder 4
    m 12d "Oh! What is this? This is new and pretty."
    "Monika touched the Egg."
    show pictures at thide zorder 1
    hide pictures
    show emerald blue at t22 zorder 4
    mik "What a wonderful shiny rock!!!! It's your lucky day!"
    mc "Hooray! We found a Chaos Emerald!"
    $ persistent.emeraldCount = 4
    play sound Emerald_word
    "{i}You won a Chaos Emerald!\n(Click to continue...){/i}"
    "Now we have [persistent.emeraldCount] Chaos Emerald!"
    show monika 9a at t22 zorder 2
    mc "Time to save this Chaos Emerald with us. Thanks, Miku!"
    show emerald at thide zorder 1
    hide emerald
    mik "Pleased to help! Tra lalala lala!"
    mik "Now, shall be going to your world and help you? My concert was over some hours ago, and now it's Rin and Len's turn to sing."
    mik "I don't wanna see your friend sad again! Ok?"
    m 10b "Glad that you can help us, Miku! If this portal opened here, that means every single world is in danger!"
    mc "Then, let's stop waiting! I see an escape portal some meters ahead, let's go there and go back to our world!"
    "And so, the three of us went to the exit portal..."
    
    return
