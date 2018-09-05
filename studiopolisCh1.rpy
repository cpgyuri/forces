# Chapter 1 static content. Poem responses called from here are in script-poemresponses.rpy

label chapter1:
    scene bg nullspace
    with dissolve_scene_half
    if persistent.packagedMusic == True:
        play music nullSpacePCKG
    else:
        play music mend
    
    #Exclusive scene starts here
    if poemwinner[0] == "monika":
        $ forces.evil_monika()
        $ forces.send_temporary_notification("Waifu Club", "You found the Doki Doki Waifu Club mod easter egg!\nGo to http://http://www.clubwaifu.tk/ and choose your waifu!", action=Return(1))
        if persistent.packagedMusic == True:
            play music nullSpacePCKG
        else:
            play music mend
    mc "Very well, this is not the thing I was expecting when I joined the Resistance haha."
    "I wrote a poem of sorts."
    "I'm not an expert on writing (neither am I in combat), but I put all my effort into it."
    "Thanks to the magic energy of the Wisps that this weapon uses, anything can be fired from the Wispons."
    mc "Tails told me that I must insert this poem on the Wispon and then shoot."
    mc "If I got lucky, one of the girls will materialize again, and she will help me to save the others."
    mc "I hope I chose the correct one for this kind of situation..."
    "I proceeded to fire the Wispon..."
    
    #Call exclusive scene
    $ nextscene = poemwinner[0] + "_exclusive_" + "1"
    call expression nextscene from _call_expression_2

    #After exclusive scene, we go back to chapter
    scene bg nullspace
    with dissolve_scene_half
    stop music fadeout 2.0
    show monika 1d at t44 zorder 5
    show sayori 1m at t43 zorder 4
    show natsuki scream at t42 zorder 3
    show yuri 1y2 at t41 zorder 2
    $ install_character("sayori")
    $ install_character("natsuki")
    $ install_character("yuri")
    $ install_character("monika")
    mc "I can't believe this! All of you are alive! I saved all of you after all!"
    if persistent.yuriKnife:
        play music t6g
        pause 2.0
        show yuri 2crazy at t41 zorder 2
        "AAAARGH! MY EARS! WHAT THE FUCK HAPPENED WITH THE MUSIC? IS THE PIANIST DRUNK OR SOMETHING?"
    else:
        play music t6
    if persistent.genderMale == True:
        m 5a "Thanks for saving us handsome!"
    else:
        n 5d "Yeah! Girl power! Thanks for saving us, partner!"
    show monika 5a at t44 zorder 5
    show sayori 1a at t43 zorder 4
    show natsuki 5d at t42 zorder 3
    if persistent.yuriKnife == True:
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
        show boss2 metalMonika at t42 zorder 5
        show monika 5scary at t44 zorder 5
        show sayori metalDark at t43 zorder 5
        show yuri cuts7 at t41 zorder 5
        y "The fun starts now! JOIN THE YURI EMPIRE!"
        "Wait what...{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
        show boss2 at thide zorder 1
        show boss3 at thide zorder 1
        hide boss2
        hide boss3
    show monika 5a at t44 zorder 5
    show sayori 1a at t43 zorder 4
    show natsuki 5d at t42 zorder 3
    show yuri 1a at t41 zorder 2
    "All the girls are smiling at me. This is the best day ever."
    show monika 2g at t44 zorder 5
    show sayori 1m at t43 zorder 4
    show natsuki 4p at t42 zorder 3
    show yuri 2j at t41 zorder 2
    show emerald red at h11 zorder 6
    "And with the girls, the red Chaos Emerald appeared too! What a nice bonus!"
    $ persistent.emeraldCount += 1
    play sound Emerald_word
    "{i}You won a Chaos Emerald!\n(Click to continue...){/i}"
    stop music fadeout 2.0
    m "What is that shiny jewel?"
    s "IT'S SO PRETTY!!!!"
    n 5x "That is a Chaos Emerald, Monika, you jerk!"
    n 5w "You didn't pay attention to my assignment on the Creativity Focus Group!"
    n 4v "I explained everything about Sonic games! These gems are the most important artefact there!"
    m 2r "Jeez, Natsuki! I didn't want to lose your asignment. I'm sorry. That day I had to talk with the teachers about the plans of our Club."
    m "And let us listen to the explanation."
    mc "Yeah! The Chaos Emeralds are the most powerful objects in my world!"
    mc "{i}The servers are the seven Chaos.{/i}"
    mc "{i}Our hearts intensify their power.{/i}"
    mc "{i}The controller serves to unify the Chaos.{/i}"
    mc "{i}The seven Chaos Emeralds take what is in our hearts and turn it into power.{/i}"
    m 2j "Oh! That sounds like a nice poem! I'm very interested on these Chaos Emerald now! Please continue!"
    mc "The Chaos Emeralds are seven ancient emeralds and mystical relics tied to the Master Emerald and Knuckles' ancient tribe."
    mc "Those that hold the Chaos Emeralds can use their powers for a variety of things, such as initiating a super transformation, powering machines, and warping time and space."
    mc "Anyone who combines all seven Chaos Emeralds can control ultimate power."
    mc "That's why it's very important that the Chaos Emeralds don't appear in the wrong hands!"
    if persistent.yuriKnife == True:
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
        y 3y3 "SAD THAT THOSE SHITTY JEWELS WILL BE USELESS WHEN THE RUBY IS READY AT FULL POWER..."
        m 1m "Yuri, did you say something?"
        m 2m "And also, why the game stopped suddendly...?"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
    else:
        y 2j "What a nice jewel, and so powerful!"
    mc "For now, we will save this jewel on the secret compartiment of my Wispon."
    mc "If we can escape from here, this compartiment will transport the Emerald to our Headquarters. They will be safe there."
    "And so, I saved the Emerald on the secret compartiment of my Wispon..."
    "And also I give to the girl with the red ribbon my special onion rings sandwich."
    "Now we have [persistent.emeraldCount] Chaos Emerald!"
    show emerald at thide zorder 1
    hide emerald
    play music t6
    show monika 5a at t44 zorder 5
    show sayori 1a at t43 zorder 4
    show natsuki 5d at t42 zorder 3
    show yuri 1a at t41 zorder 2
    mc "Weeeell... As now everyone is alive, and I explained everything about the Chaos Emeralds, I must present myself."
    mc "My name is [player], but in my world, everyone calls me Rookie."
    mc "And before the destruction of the world, I read a sheet of paper in the door of your classroom."
    mc "You were a Literature Club and your names are Monika, Sayori, Natsuki and Yuri."
    show monika 5a at f44 zorder 5
    m "I'm Monika, the President of the Club."
    show sayori 1a at f43 zorder 4
    s "I'm Sayori, the Vice President!"
    show natsuki 5d at f42 zorder 3
    n "I'm Natsuki, punk!"
    show yuri 1a at f41 zorder 2
    y "And my name is Yuri."
    show yuri 1a at t41 zorder 2
    y "So, are you from another world then? What is the favourite book in your world?"
    show natsuki 5d at t42 zorder 3
    n "Do the people of your world bake cupcakes and sweets?"
    show sayori 1a at t43 zorder 4
    s "Has it beautiful places, like beaches or forests?"
    show monika 5a at t44 zorder 5
    m "Do your world need a Literature Club?"
    mc "Well... thanks to Infinite and Eggman, our world was conquered and almost destroyed."
    "The small girl looked at me, surprised."
    show monika at thide zorder 1
    show sayori at thide zorder 1
    show yuri at thide zorder 1
    hide monika
    hide sayori
    hide yuri
    show natsuki 4p at t11 zorder 2
    n "Wait a minute! If you mentioned Eggman and the Chaos Emerald appeared..."
    play sound sonic1UP
    n 4z "I knew it! That means the world of the spiky rodent is completely REAL! This is the best day ever!"
    n 4y "See Yuri? You were wrong when you said that alternate realities don't exist."
    if persistent.yuriKnife == True:
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
        show natsuki 4y at t22 zorder 3
        show yuri 3y7 at t21 zorder 2
        stop music
        y "Who cares about that Natsuki!"
        "What the... screen tearing x2..."
        y 3y1 "You are always trying to prove that you are right in every topic you like about."
        show natsuki 5o at t22 zorder 3
        y 3y4 "Do you started to love Rookie now?"
        y "Are you trying to show your cuteness exposing your vast knowledge about Sonic?"
        y "Which is a {i}HEDGEHOG{/i}, not a rodent, as you say stupidly everytime."
        show natsuki 5m at h22 zorder 3
        n "Yuri, what is happening to you? Why are you saying those things? You are scaring me..."
        show yuri 3y4 at t31 zorder 3
        show monika 3g at h32 zorder 3
        show natsuki 5u at t33 zorder 3
        m "Yuri..."
        m "I don't know what is happening to you, but please, I want to ask you very nicely that you stop fighting with Natsuki."

        "How those girls know about Sonic if they never saw him before?"
        "Wait! [player], focus!"
        "It seems that saving Yuri first triggered something in her."
        "And in the game, because this game is still using the scripts of the Literature Club's world."
        "But as I'm from Sonic's world, I'm not 100%% affected to the things Yuri is doing to the scripts."
        "That means..."
        "OH NO! Now I need to worry about Yuri, the script AND our mission to stop Eggman. Congratulations [player]."
        mc "Eeeeeeeh... Girls! Tails is trying to communicate with me again!"
        "Thanks Tails for your good timing."
        pause 0.5
        show natsuki at thide zorder 1
        hide natsuki
        show monika at thide zorder 1
        hide monika
        show yuri 3y3 at t11 zorder 2
        y "Where do you think you are going? Stay with me a little..."
        window hide
        pause 3.0
        show yuri 3y2 at h33 zorder 2
        call screen dialog("Yuri, please, I still have some skills from our world.\nStop what you are trying to do, please.\nI don't really want to have to stop you the hard way.", ok_action=Return())
        show yuri at thide zorder 1
        hide yuri
    else:
        show natsuki 4y at t22 zorder 3
        show yuri 3u at t21 zorder 2
        y "You are right Natsuki, I was wrong. And this discovery opens a world of multiple possibilities and poetry inspiration."
        mc "Oh yeah, but first, we need to contact with the Resistance and escape from this weird place."
        "How do those girls know about Sonic if they have never seen him before?"
        stop music fadeout 2.0
        mc "Wait! Tails is trying to communicate with me again!"
        show natsuki at thide zorder 1
        show yuri at thide zorder 1
        hide natsuki
        hide yuri
    if persistent.packagedMusic == True:
        play music nullSpacePCKG
    else:
        play music rWispon
    show tails tailsCom at t22 zorder 2
    show sayori 4m at t21 zorder 3
    mtp "Rookie! Did it work?"
    show tails tailsCom at t22 zorder 2
    show sayori 4s at h21 zorder 2
    play sound sonic1UP
    s "OMG IS TAILS!!! HE IS REAL!!!"
    mtp "..."
    mtp "I don't understand what are you trying to say about {i}real{/i}. I'm as real as you can see on this communicator."
    mtp "Rookie, are those girls in school uniform the people you wanted to save?"
    s 2p "Yes, we are. Our names are Monika, Yuri, Natsuki, and my name is Sayori."
    s 3i "We are not \"School girls in uniform\"."
    show sayori at thide zorder 1
    hide sayori
    show monika 2c at t21 zorder 2
    m "I'm Monika, the President of the Literature Club."
    m "As you can see, our world was destroyed by that weird thing called Infinite."
    m "Thanks to us that Rookie was here and saved us. Floating without a body in space is chilling."
    mtp "Pleased to meet you Monika, and welcome to the Resistance, all of you."
    mtp "OK, everyone: Rookie, turn 90° around and shoot your Wispon when ready."
    mtp "This will open a portal of sorts and you will come back to our world."
    show monika 5b at h21 zorder 2
    m "Wait a minute...!{nw}"
    mtp "Make sure you enter the portal with your new friends."
    mtp "If this goes right, you will be back on Green Hill Zone."
    mtp "When you are on Green Hill, I will teleport some handy stuff for Monika and her friends!"
    if persistent.yuriKnife == True:
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
        mtp "Did it work?"
        mtp "I did it, I hacked the script!"
        mtp "Now we can fight at the same pace, Yuri."
        mtp "According to my analysis, Natsuki is not affected by the interruptions and she reacts to them."
        mtp "Also, every character from our world, including Rookie."
        mtp "This is an interesting info. Sadly I stopped Rookie and the girls for this test, so..."
        mtp "Now I'm calibrating my hacking to not affect my friends and Natsuki. I think she will be useful."
        mtp "Wait, Knuckles is calling me for something important! Resuming the script."
        mtp "{i}And no, Monika, I didn't stole your catchphrase.{/i}"
    show tails at thide zorder 1
    hide tails
    show monika 5b at h11 zorder 2
    m "HEY, THE FOX STOLE MY PATENTED CATCHPHRASE!"
    show monika at thide zorder 1
    hide monika
    "I did exactly what Tails told me to do."
    "I fired my Wispon one last time and, as predicted, a portal opened."
    mc "Ok! We will enter my world now! If we can win against the Eggman Empire..."
    mc "We will save it and hopefully we will restore yours also!"
    mc "Are you ready, Literature Club?"
    show monika 1a at t44 zorder 5
    show sayori 4a at t43 zorder 4
    show natsuki 1a at t42 zorder 3
    show yuri 2a at t41 zorder 2
    m 5b "Ready and armed with our best poems!"
    s 5b "Ready and still hungry!"
    n 1d "WE WILL BEAT THE SHIT OUT OF INFINITE, PUNK!"
    if persistent.yuriKnife == True:
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
        stop music
        y 3y3 "I CAN'T WAIT TO STAB INFINITE WITH MY SHINY KNIFE..."
        m 5b "Okay, Yuri, this is enough, I swear, what is happening with you?"
        y 3y7 "HEY, CAN YOU STOP RUINING MY MOMENTS, PRESIDENTIAL TRASH CAN WITH LEGS?"
        m 16ad "Listen to me, you stupid moron!"
        m "We are friends but you are acting very out of character, and this time this wasn't my fault!!!"
        m "So you don't have any right to insult me!"
        m 5b "Rookie! Am I the only one who is noticing this?"
        y "There she goes, abusing of her powers and charisma to bother the main character!"
        m 16ad "SHUT UP YURI!"
        m "Rookie, you saved her first! Did something bad happen? What did you do to her???"
        mc "Wait, Monika, please, I'm trying to think on something!"
        "NOT AGAIN."
        "If I don't take action the other two girls with catch up on this and these other two girls will end killing themselves."
        "This means that my friends WILL notice this weird stuff when we arrive on Green Hill Zone."
        "It seems that the game will resume... Smile!"
        m "*Sigh*..."
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
    else:
        y 2r "Let the winds of the battle and the victory lift our spirits up, everyone."
        stop music
    show natsuki at thide zorder 1
    show yuri at thide zorder 1
    show sayori at thide zorder 1
    hide natsuki
    hide yuri
    hide sayori
    show monika 5b at t11 zorder 2
    m "AND STOP STEALING MY CATCHPHRASES!"
    show monika 2g at t44 zorder 5
    show sayori 1h at t43 zorder 4
    show natsuki 1c at t42 zorder 3
    show yuri 1f at t41 zorder 2
    "But before we can go, I made a signal for all the girls to stop."
    m "Eh? Rookie? What's wrong?"
    mc "Please wait, my MILESELECTRIC is receiving another call!"
    mc "But this time, is not Tails the one who's calling me!"
    show ghostnatsuki gCom at h11 zorder 6
    g "IS THERE A bzzt RECEIVE bzzt CALL???"
    g "THERE bzzt bzzt bzzt INTEREFERENCE..."
    g "...bzzt TRAPPED bzzt RUBY bzzt ISLAND WITH BEACH!"
    g "I THINK bzzt SEND COORDINATES... SENDING!!!"
    g "PLEASE COME TO SAVE ME, PIECE OF SHIT!!! I KNOW THERE SOMEONE THERE!!!"
    "There is another person screaming..."
    if persistent.ddlc_femc:
        femc "Help! Help! I'm trapped with a weird version of Natsuki!"
        femc "That doesn't mean that the original Natsuki wasn't weird already..."
        n 4o "WHAT???"
        femc "Anyways, we are trapped on a capsule!!!"
        femc "Sayori, my love, if you are there, please come to save me!!!"
        femc "I miss you... I miss your hugs... I miss your kis..."
        femc "Whoops! I'm not alone here!"
    else:
        mc2 "Help! Help! I'm trapped with a weird version of Natsuki!"
        mc2 "That doesn't mean that the original Natsuki wasn't weird already..."
        n 4o "WHAT???"
        mc2 "Anyways, we are trapped on a capsule!!!"
        mc2 "Sayori, if you are there, please come to save me!!!"
        mc2 "And I was supposed to be there for protecting you... I'm a failure as a boyfriend..."
        mc2 "Don't be an airhead and come faster!"
    show ghostnatsuki at thide zorder 1
    hide ghostnatsuki
    "The transmission ended here."
    mc "Why this person reminds me a lot of Natsuki???"
    n 4o "WHAT DID YOU SAID, ROOKIE???"
    if persistent.ddlc_femc:
        s "That was [femc_name]!"
        s "I need to go to save her!!!"
        s "Rookie, please!!! She is the most important person to me!!!"
    else:
        s "That was [mc2_name]!"
        s "I need to go to save him!!!"
        s "Rookie, please!!! He is the most important person to me!!!"
    m "My last club member and one of my glitch creations are trapped, is my duty as a President to go there and save them."
    m "Your Green Hill zone can wait, Rookie, right?"
    mc "Well... the weird Natsuki sent the coordinates to me... everything seems to indicate that they were trapped in Angel Island."
    mc "So... it's a thing of clicking some buttons here and here and..."
    mc "Bingo! The portal is now set to Angel Island!"
    mc "Let's go girls! Our first mission together!"
    n "I'M NOT WEIRD!!!"
    show natsuki at thide zorder 1
    show yuri at thide zorder 1
    show sayori at thide zorder 1
    show monika at thide zorder 1
    hide natsuki
    hide yuri
    hide sayori
    hide monika
    "One by one the girls started to enter the portal."
    if persistent.yuriKnife == True:
        "But before I can enter it, the script stops again, and Monika, now calmed, took advantage of that and speak."
        show monika 4h at h11 zorder 2
        m "Okay, Rookie. Now we have some quality time, alone."
        m 1h "First: thanks for saving us, I really appreciate this."
        m "But now, I need some very convincing explanations about what is happening to Yuri."
        m "It seems only you and me are noticing the weird attitude of her. And the game's screen tearing."
        m 5b "What did you do to Yuri?"
        mc "Monika, please, don't say anything yet to your friends or my friends when we arrive at Green Hill Zone."
        mc "I swear I did nothing to Yuri, and the only thing I really don't want is Tails noticing this..."
        "I really hope Tails didn't noticed..."
        mtp "Always so innocent, Rookie..."
        "OH NO! Tails is calling me!"
        show monika 2ad at t22 zorder 3
        show tails tailsCom at t21 zorder 2
        mtp "Rookie, I'm not so stupid as you think. You know it. I'm the smartest of the team."
        mtp "The MilesElectric software is detecting the script interruptions since the moment I loaded your Wispon with MilesPOEM"
        mtp "So stop trying to hide vital information!"
        mtp "This is a very serious problem, so I'm with you and Monika on this."
        m "So, mister Tails, can I have an explanation about why Yuri is acting weird, please?"
        m "I still have some form of control of the game files, and I will not hesitate to delete her if..."
        mtp "DON'T YOU DARE TO TRY SOMETHING EXTREME WITH YURI, MONIKA!!!"
        show monika 1l at h22 zorder 3
        m "Ahaha~ why the scream all of a sudden...?"
        mtp "Monika, Rookie, I will try to get all the info I can about this weird events."
        mtp "As a scientist and technician, its my duty to investigate and then solve problems."
        mtp "If you will take the easy way of destroying what is bothering you, then you are not so different than Dr. Eggman."
        mtp "And what Yuri is doing it's even a danger for {i}Eggman and Infinite{/i} now, and I'm sure it's thanks to the Phantom Ruby."
        mtp "Rookie, call Yuri and talk with her as the corrupted script says, or else she will suspect."
        mtp "For now, I alerted Amy and Knuckles, and he, as the Captain of the Resistance, declared a Yellow alert."
        mtp "Obviously, finding and saving Sonic still is priority one, but now, thanks to our meddling in this world, we gained a new risk."
        mtp "You know what Yellow Alert means, Rookie. Tails, out!"
        mtp "OH! And I know you are going to Angel Island too. Changing the coordinates of the portal was something impressive."
        mtp "Please take care, everyone."
        mtp "And I will be watching you, Monika."
        m 4m "And is better that I enter the portal now..."
        show tails at thide zorder 1
        hide tails
        show monika at thide zorder 1
        hide monika
        "And what I was afraid of is now reality."
        "Yuri is compromising our mission. I never believed we will get a Yellow alert without Eggman being the reason."
        "Well, Tails told me that the script must continue, so..."
        "I call Yuri aside before she enters the portal."
        mc "Yuri what the fuck with the screen tearing and your bizarre comments? Even Natsuki catches it!"
        show yuri 4c at t11 zorder 2
        play music t10y
        y "Sorry, you deserve an explanation..."
        y "As I said, I like knives and these kind of stuff."
        y "And... I cut myself out of nervous and pleasure."
        y "I tried to stop these feelings with my second hobbie: escaping from reality with my books."
        y "But even books weren't enough to stop myself from doing that."
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
        show yuri cuts at h11 zorder 2
        "NO. WAY..."
        y "Ow! This hurts! I did those recently, before Infinite's attack!"
        y 4d "But try to understand me!"
        y 4e "Those knives don't deserve to be lonely."
        y "They deserve care and love and attention, each one of them."
        show yuri 1y3 at face(y=600) with dissolve
        y "DON'T YOU THINK THE SAME?"
        y "AND THESE FEELINGS ARE MAKING ME ACT OUT OF CHARACTER!"
        y "BUT I LOVE HOW I AM RIGHT NOW..."
        y "DON'T YOU LOVE THIS TOO?"
        mc "GET. OUT. OF. MY. FACE!"
        show yuri 1y2 at t11 zorder 2
        mc "Yuri: I will be seriously watching you if we made missions together."
        show yuri 4d at t11 zorder 2
        mc "If you try some weird stuff with your knife again, your friends WILL KNOW about this!"
        mc "For now I will let it pass, because reaching the Resistance's Headquarters is more important."
        mc "And I will assume your reaction was because I told you that I didn't save your friends at that time."
        show yuri 4c at t11 zorder 2
        mc "BUT DON'T YOU DARE TO TRY SOMETHING STUPID IN FRONT OF TAILS, AMY OR KNUCKLES."
        mc "OR IN FRONT OF SONIC, IF WE SAVE HIM."
        mc "If you do, my friends will notice. And Natsuki {i}will request a lot of answers from you{/i}..."
        y "Promise."
        "And so, I let Yuri enter the portal..."
        pause 1.5
        y 4e "Don't count on that promise I did to Rookie. That was a lie."
        y "Keep choosing me on MilesPOEM minigame, fellow Yurist."
        y "The cult of the Yurism will born from the ashes of Sonic's world."
        y 3y3 "And soon that world, the Literature Club and all the universe will be MINE TO CONTROL!"
        y "JOIN THE YURI EMPIRE!"
    play sound ruby
    pause 1.0
    show yuri orb2 at t11 zorder 2
    pause 5.0
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    "You got 250 rings for ending the Prologue!"
    "You got 250 rings for ending Chapter 1!"
    "You got 400 rings for saving the girls!"
    "You got 500 rings for getting a Chaos Emerald!"
    play sound Ring
    $ persistent.ringCount += 1400
    "You now have [persistent.ringCount] Rings!\n{i}Click to continue...{/i}"
    $ mikEXEPoemChapter = 1
    pause 3.0

    window hide
    call screen confirm("You have unlocked a special poem.\nWould you like to read it?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + "1" from _call_expression_20
        scene black with Dissolve(1.0)
    else:
        pass
    return

