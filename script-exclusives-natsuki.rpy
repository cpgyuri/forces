label natsuki_exclusive_1:
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
        y "Hey???"
        y 3y7 "You were supposed to choose ME, but for some reason, there is a problem!"
        y 3t "Something bad happened to my cupcake... I will forgive that you didn't stick with me and ask you a mission."
        y 3r "Please SAVE HER...!"
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
    show natsuki orb at t11 zorder 2
    "A strange orb appeared. It's reacting with my Wispon..."
    "What...?"
    "The orb materialized in front of me!"
    "Is one of the girls, and she's the girl with pink hair! Unbelievable! I saved her!!!"
    show natsuki 1v at t11 zorder 2
    n "Ugh, my head... The last thing I remember, we were attacked on the Literature Club and..."
    n "..."
    n 6f "I REMEMBER!!! HA HAHAHAHAHA!"
    n 6o "Wait."
    n 6b "Who the HELL are you? What are YOU looking AT?"
    "OK... What is happening here?"
    mc "First relax! I'm not your enemy, and I'm not..."
    n "Shut THE FUCKING up!!!"
    n 6i "I don't know who are you, where are my friends???"
    n 6n "AND WHAT IS THIS PLACE????"
    mc "Lady, if you let me explaining!"
    "I explained to this girl what happened when Infinite attacked her classroom."
    "Her expression changed MORE when I mentioned she was the only one I could revive."
    n 6m "So, I'm in a sort of LIMBO or shit like that?"
    n 6l "Well... at least my dear friends..."
    play music t7g
    show noise zorder 99:
        alpha 0.0
        linear 3.0 alpha 0.25
    n 6c "WILL NEVER KNOW WHAT STUFF I DID TO MY PAPA!!!"
    n 6h "I WAS SO DONE OF THE ABUSE! I WAS SO DONE OF HIM REJECTING EVERY SINGLE SHIT I DO RIGHT!"
    n "I WAS SO FUCKING DONE OF HIM DISLIKING MY FRIENDS AND MY MANGA!!!"
    n 6d "But now, there is no Papa. No more..."
    "WHOAH hard stuff! Does this imply that she was suffering serious abuse in her world???"
    "It's obvious why she is acing so weird after I revived her..."
    n wispon "I did it with a special toy I encounter in my house!"
    n "And then I started to kill those weird robots with it! I felt so powerful!!!"
    "How did this happened???"
    "THIS GIRL PULLED A {i}WISPON{/i} OUT OF NOWHERE!!! OH NO NONONONONONONONONONONO..."
    "Girl, WHAT DID YOU DO WITH THAT WISPON? YOU ARE NOT SUPPOSED TO HAVE SOMETHING LIKE THAT!!!"
    "Rookie, think and act fast!"
    "SAVE HER GODDAMIT, THINK ON SOMETHING!!!"
    n 6l "If you are wondering how I got this weapon... let's say a weird person gived it to me before the invasion."
    n 6f "That weird person looks like Sayori, but with a weird bloody hat."
    n "She told me that today was the anniversary of my school, and that a weird robot invasion would happen."
    n 6d "In that moment, I, Natsuki, the most pro girl ever, would use MY SHINY NEW TOY TO DESTROY EVERYONE!!!"
    n 6s "Because everyone was already a fucking robot, even my dad and friends of the club!!!"
    mc "So your name is Natsuki then!!! What a cute name."
    n 6h "I. HATE. BEING. CALLED. CUTE!!!!"
    mc "HEY! This is how you will say thank you for me saving you?"
    mc "I had to make the effort of making a poem, load it on my Wispon and fire!!!"
    mc "Then you appeared here."
    n 6j "A poem..."
    n 6a "Oh yeah! I had to show my special poem! You, read this!"
    call showpoem(poem_n5, music=False, revert_music=False, paper="images/bg/poem_y2.jpg")
    show natsuki 6h at face with dissolve
    n "I hope you loved this poem. Now say goodbye."
    mc "Not so fast, Natsuki! I don't want to die here on Null Space!"
    mc "Get closer to me was your last mistake, take this!!!"
    "I had to hit her in the head with my Wispon, with all my strenght!"
    show natsuki 1v at t11 zorder 2
    n "Ugh, my head... I think... I need... some rest..."
    "Natsuki collapsed..."
    pause 5.0
    $ skip_transition = True
        
    scene bg nullspace
    stop music
    play music t9
    show natsuki 12f at t11 zorder 2
    "After some minutes, or hours, passed, no idea how the time works here, Natsuki woke up, and I did helped her to stay on her feet."
    "I could get that Natsuki was very malnourished and had a lot of abuse in her home world. She has her arms and shoulders bruised."
    "I pulled from my Wispon one of my favourite onion rings sandwiches and gived it to her."
    "I explained to this girl, again, what happened when Infinite attacked her classroom, my name, and how I saved her."
    mc "It's ok to cry, Natsuki. It seems life treated you very hard, but I'm here to help you! That's what a Resistance soldier do!"
    n "Rookie... I can't remember our conversation, but I swear to you that I'm not evil!"
    mc "I believe you, Natsuki. I felt some weird energy emanating from your orb."
    mc "Probably was an illusion that ocurred because we are in this strange place."
    mc "For now, we must concentrate in saving your friends, like how I did with you and my poem."
    mc "And you can keep that Wispon you have."
    n 1i "True. true. I'm pro at this, Rookie, I will do a REAL poem for you. Watch it!"
    n "And thanks for letting me keep this weapon."
    "Natsuki wrote a simple poem on a paper she had in her pocket, then she gives me the paper sheet gently."
    call showpoem(poem_n4)
    "I said simple, but if you read it, you can feel the feelings this girl is having."
    "Well, I'm not an expert in poetry anyways."
    "But it seems this poem was directed to someone else... Maybe is one of the girls? We are open minded in our world, so if she is in love with one of them, I can't complain..."
    "I loaded the poem on the Wispon and prepared to fire..."
    mc "Wish me good luck, Natsuki. We will save them."
    "The Wispon fired a beam again..."
    "After I fired the Wispon, three coloured orbs appeared..."
    show monika orb at t44 zorder 5
    show sayori orb at t43 zorder 4
    show natsuki scream at t42 zorder 3
    show yuri orb1 at t41 zorder 2
    "Then the other three girls materialized!"
    mc "Unbelievable! I need to report this to Tails when I come back to our Headquarter!"

    "You got 400 rings for saving Natsuki!"
    $ persistent.ringCount += 400
    if persistent.yuriKnife == True:
        y "You also got 6000 rings for helping Natsuki in her hard moment. Courtesy of Yuri."
        $ persistent.ringCount += 6000
    play sound Ring
    "You now have [persistent.ringCount] Rings!\n{i}Click to continue...{/i}"
    return


label natsuki_exclusive_2:
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
    m 1b "Natsuki!"
    show knuckles knucklesCom at t33 zorder 2
    show monika 1b at t32 zorder 3
    show natsuki 5z at l31 zorder 4
    "Natsuki almost look like if she is about to explode. She looks super happy and excited."    
    n "YES! YES! FRICKIN' YES! THIS IS MY BEST DAY EVER AFTER THE CLUB'S CREATION!"
    n 5y "You will be almost as pro as ME, Rookie! I know all this places from heart and soul!"
    n 4l "We will save Sonic in no time! HE WILL PRAISE ME! OMG!"
    m 3b "And I will give you directions from here, guys."
    mc "And with that, Captain, I think we are ready to go. I have my partner, they have the Extreme Gears, and Monika will command from here."
    n 4g "Thanks Rookie and mr. Knuckles for trusting in me. WE WILL SAVE MY FAVOURITE RODENT AND MAKE EGGMAN EAT THE UNTASTY CUPCAKE OF THE DEFEAT."
    kte "Excellent, then! Operation: Rescue is officially starting!"

    "You got 400 rings for your poem for Natsuki!"
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
    show natsuki 1e at l11 zorder 2
    "Natsuki and I are on Chemical Plant now."
    "I can see Natsuki is excited for being here, but also is worried."
    n "This is it, [player], we will rescue Sonic!"
    n 42c "I hope Eggman is listening to me. WE WILL RESCUE SONIC, EGGHEAD!"
    n 42g "Do you trust me, Rookie, yes?"
    mc "Of course, Natsuki! It's time to explore the level. We are searching for a hidden passage to Eggman's Prison."
    mc "And thanks for opening your feelings to me. I hope you can be like this with Sonic too!"
    n "Sonic is my idol, Rookie."
    n "I knew you asked before, so I will tell you the answer."
    n 4t "Your universe exists in our universe, as videogames."
    n "I'm an avid player of Sonic the Hedgehog videogames. I know all their secrets, routes and developer tricks and codes."
    n 42f "I even wrote a poem for Sonic, if someday I could encounter him in real life. I have this poem with me since the day I wrote it."
    n "Obviously you will see it only when I give it to Sonic, but..."
    n "I couldn't let my friends see this, or how I react! They would be dissapointed in me!"
    mc "That's curious, Natsuki!"
    n 4h "Eh? What are you talking about?"
    mc "There is a visual novel videogame that is popular here, is called Doki Doki Literature Club..."
    mc "And the main characters are four girls that looks and act the same as you and your friends! They even have the same names!"
    mc "And guess what...?"
    mc "SONIC ADMIRES YOU, NATSUKI! YOU ARE HER FAVOURITE ONE IN THE GAME! HE TALKS ABOUT YOU EVERYWHERE!"
    mc "HE EVEN CALLED HIS EXTREME GEAR SKATEBOARD \"NATSUKI'S FASTCAKE\"!"
    mc "And he made a poem for you too!"
    n 1f "WHAAAA---"
    n 1r "This can't be..."
    n 12h "So, my hero admires me, and I'm his heroine..."
    n "..."
    n 12f "I can't believe this day would come..."
    n "WE REALLY NEED TO START OUR SEARCH, [player]!"
    n "WE WILL NOT FAIL OUR BLUE HERO!"
    mc "THAT'S THE ATTITUDE, NATSUKI!" 
    mc "SONIC, HERE WE GO!"
    show natsuki 1v at h11 zorder 2
    n "WAIT YOU STUPID!!!!"
    n 5x "This will be beaten with passion and dedication, not by working to reach the goal too fast!"
    n "I know it's difficult to understand, because this world works with a going fast mentality, but..."
    n 1h "Do you have a way to climb to the top of this loop? I need something from there."
    mc "My Wispon has a hook and a rope, so I can climb to there, wait here!"
    "And so I climbed the loop, and surprise!"
    show natsuki 1d at h22 zorder 2
    show monitors invincible at h21 zorder 3
    play sound Ring
    "AMAZING! Natsuki and I found an Invincibility Monitor!"
    "We will save it for later!"
    mc "Good job Natsuki! I didn't have any idea about that secret monitor!"
    mc "This will surely come in handy!"
    n 4z "I TOLD YOU! I knew all this places like if I was born here!"
    n 2b "Now let's search for the secret entrance."

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
    show natsuki 5o at h22 zorder 2
    show monitors invincible at h21 zorder 3
    n "NOW ROOKIE, THROW ME THE MONITOR!"
    "I did what she told me to do."
    "The background music changed to the empowered melody."
    show monitors at thide zorder 1
    hide monitors
    "Natsuki started to run towards the EggPawns!\n{i}(Click to continue!!!){/i}"
    play music invincibility
    show natsuki natsuInvincible at h11 zorder 2
    pause 3.0
    show natsuki natsuInvincible at h22 zorder 2
    show eggpawn eggpawn1 at l21 zorder 3
    pause 3.0
    play sound destroy
    show natsuki natsuInvincible at h21 zorder 2
    show eggpawn eggpawn1 at l22 zorder 3
    pause 3.0
    play sound destroy
    show natsuki natsuInvincible at h22 zorder 2
    show eggpawn eggpawn1 at l21 zorder 3
    pause 3.0
    play sound destroy
    show natsuki natsuInvincible at h21 zorder 2
    show eggpawn eggpawn1 at l22 zorder 3
    pause 3.0
    play sound destroy
    show natsuki natsuInvincible at h22 zorder 2
    show eggpawn eggpawn1 at l21 zorder 3
    pause 3.0
    play sound destroy
    show natsuki natsuInvincible at h21 zorder 2
    show eggpawn eggpawn1 at l22 zorder 3
    pause 3.0
    play sound destroy
    show natsuki natsuInvincible at h22 zorder 2
    show eggpawn eggpawn1 at l21 zorder 3
    pause 3.0
    play sound destroy
    stop music fadeout 2.0
    show eggpawn at thide zorder 1
    hide eggpawn
    show natsuki 1z at h11 zorder 2
    "And so, the powerup faded out. And the way is clear for both of us. Amazing."
    "She destroyed the robots only by ramming through them!"
    play sound Ring
    "Animals and rings dropped of the robots, so I made sure to collect all the rings."
    "Natsuki is very athletic and strong. Quite the opposite to her female figure. And the invincibility powerup empowered her."
    "She disposes of all the EggPawns that were surrounding the area, and of the Chemical Plants robots too."
    "So, the way to Sonic's prison cell is clear!"
    return

label natsuki_exclusive_3:
    scene bg hidrocity
    with dissolve_scene_half
    if persistent.packagedMusic == True:
        play music hidrocityPCKG
    else:
        play music hidrocity
    show natsuki 1d at t33 zorder 3
    show portal genesisportal at t32 zorder 2
    "Natsuki and I are prepared to enter the Genesis Portal."
    n "Be ready and wait for us, everyone! Wish me luck!"
    m "Good luck Natsuki! Please take care, ok?"
    g "Be brave!"
    "And, after the hugs and goodbyes and the briefings of the mission, we entered the portal..."

    "You got 500 rings for going to the portal with Natsuki!"
    play sound Ring
    $ persistent.ringCount += 400
    "You now have [persistent.ringCount] Rings!\n{i}Click to continue...{/i}"

    scene bg corridor_night
    with dissolve_scene_full
    stop music fadeout 2.0
    show natsuki n3h at l11 zorder 2
    n "Wait... this is our school? But how?"
    mc "I don't get it... your world was destroyed, I saw and survived it!"
    n n3g "This is suspicious, [player]."
    n "This is the corridor, and that door is the door to the Literature Club classroom."
    mc "And it's night time. It's weird, let's check if the door opens and take a look."
    "And so, to our surprise, the door opened..."

    scene bg club_night
    with dissolve_scene_full
    n "Is anybody here, hello?"
    mc "Is this the Literature Club room?"
    ser "Oh! Do you two are coming to our night party???"
    "Suddendly, four people appeared in front of us!"
    play music moddersPortal
    show cookies ncookieSprite at l41 zorder 2
    show oneterm ntermSprite at l42 zorder 3
    show skull nskullSprite at l43 zorder 2
    show serg nsergSprite at l44 zorder 2
    ser "Welcome to the Literature Club!"
    show cookies ncookieSprite at f41 zorder 2
    show oneterm ntermSprite at t42 zorder 3
    show skull nskullSprite at t43 zorder 2
    show serg nsergSprite at t44 zorder 2
    coo "Serg! Wait! Don't you see something?"
    show cookies ncookieSprite at t41 zorder 2
    show oneterm ntermSprite at t42 zorder 3
    show skull nskullSprite at f43 zorder 2
    show serg nsergSprite at t44 zorder 2
    skl "I don't think he can see any shit, Cookie, it's night!"
    show cookies ncookieSprite at t41 zorder 2
    show oneterm ntermSprite at f42 zorder 3
    show skull nskullSprite at t43 zorder 2
    show serg nsergSprite at t44 zorder 2
    onT "Skull and his amazing jokes, again..."
    show cookies ncookieSprite at t41 zorder 2
    show oneterm ntermSprite at t42 zorder 3
    show skull nskullSprite at f43 zorder 2
    show serg nsergSprite at t44 zorder 2
    skl "Well, at least my jokes aren't gay, like your hair style..."
    show cookies ncookieSprite at t41 zorder 2
    show oneterm ntermUWASprite at f42 zorder 3
    show skull nskullSprite at t43 zorder 2
    show serg nsergSprite at t44 zorder 2
    onT "I'M NOT GAY LIKE YOU AND SERG!"
    show cookies ncookieSprite at f41 zorder 2
    show oneterm ntermUWASprite at t42 zorder 3
    show skull nskullSprite at t43 zorder 2
    show serg nsergSprite at t44 zorder 2
    coo "Please don't fight, friends. I don't like fights. And besides, we have visitors, remember."
    show cookies ncookieSprite at t41 zorder 2
    show oneterm ntermSprite at f42 zorder 3
    show skull nskullSprite at t43 zorder 2
    show serg nsergSprite at t44 zorder 2
    onT "Yeah. We have to give a good first impression to them."
    onT "Let me bring some memes and creepy pictures, ok?"
    show cookies ncookieSprite at t41 zorder 2
    show oneterm ntermSprite at t42 zorder 3
    show skull nskullSprite at t43 zorder 2
    show serg nsergSprite at f44 zorder 2
    ser "Not that kind of impression, Term, haha."
    ser "Anyways, who are you two?"
    ser "The girl with the pink hair looks cute, and she seems oddly familiar. And we don't remember that the Night Gay Party was with cosplays of furries."
    show cookies ncookieSprite at t41 zorder 2
    show oneterm ntermUWASprite at f42 zorder 3
    show skull nskullSprite at t43 zorder 2
    show serg nsergSprite at t44 zorder 2
    show natsuki n1v at l41 zorder 3
    nT "WE ARE NOT CUTE!!!!!!"
    onT "WHY, SERG, WHY????"
    skl "And also Manga is NOT Literature."
    nT "WHAT!!!!!"
    mc "Here we go, as Sonic says. Natsuki has the mood of an atomic bomb."
    nT "MANGA IS LITERATURE!!!!!!"
    n n1x "Even on alternate universes people finds me cute when I'm not, and despise manga!!!"
    n "UGGGGGHHHH..."
    n n1l "Anyways, I'm glad that see that, at least in another universe, the Literature Club keeps existing."
    n "My name is Natsuki, and this friend here is called [player], but everybody calls them Rookie also."
    show natsuki at lhide zorder 1
    hide natsuki
    show cookies ncookieSprite at t41 zorder 2
    show oneterm ntermSprite at t42 zorder 3
    show skull nskullSprite at t43 zorder 2
    show serg nsergSprite at f44 zorder 2
    ser "NATSUKI? The REAL Natsuki? And the furry looks like those Gemini0's Sonic sprites, haha."
    ser "Hey guys! Today is our lucky day!!!! We have the original Natsuki here on our room. Let me present everyone."
    ser "My name is Serg."
    show cookies ncookieSprite at t41 zorder 2
    show oneterm ntermSprite at t42 zorder 3
    show skull nskullSprite at f43 zorder 2
    show serg nsergSprite at t44 zorder 2
    ser "This here is my partner and mate, Skull. We both moderate the DDMC Discord Server, and we were about to troll in the community channel."
    skl "Hey, both of you! Please to meet you."
    show cookies ncookieSprite at t41 zorder 2
    show oneterm ntermSprite at f42 zorder 3
    show skull nskullSprite at t43 zorder 2
    show serg nsergSprite at t44 zorder 2
    ser "This right there is Term, say hi to Term! He is a cool dude too, like everyone here."
    ser "And gay too{nw}"
    onT "It's an honour to meet the original Natsuki. It's like a dream come true, don't you think, dear Blue Eyes Toon Dragon?"
    "The dragon makes happy dragon noises."
    show cookies ncookieSprite at f41 zorder 2
    show oneterm ntermSprite at t42 zorder 3
    show skull nskullSprite at t43 zorder 2
    show serg nsergSprite at t44 zorder 2
    ser "The one right there is Cookies, our lovely friend and sunshine. He always gifts sunny days and nice words to everyone, and he is super friendly. Everyone loves him on our community."
    coo "It's fine, Serg! I have love for, and I care about the happiness of everyone also. If everyone is happy, I'm happy too."
    coo "And pleased to meet you, Natsuki and Rookie."
    show cookies at lhide zorder 1
    show oneterm at lhide zorder 1
    show skull at lhide zorder 1
    hide skull
    hide oneterm
    hide cookies
    show serg nsergSprite at t44 zorder 2
    ser "By the way! There's still one more person we wanna present to both of you."
    show philoso nphiloSprite at t42 zorder 2
    show natsuki n1n at t43 zorder 2
    ser "This is Philosoraptor, the visible face and founder of this Club."
    phil "Pleased to meet you."
    phil "I'm the visible face of both this wonderful Literature Girl and the mod in which we will starring soon."
    phil "And also I'm the favourite of the kids of 31 Minutes tv show."
    phil "So, if you need assistance or help, please count with all the boys, ok?"
    phil "I'm glad you choosed to arrive here, now if you excuse me, I'm in the best part of Logokas' trolling."
    phil "He already yelled STOP POSTING YOUR HORRENDOUS FAN ART ON THE MOD_ART CHANNEL. THIS IS FOR USABLE ART STUFF ON MODS ONLY!!! AAAARRRRGGGGHHHHH!"
    phil "By the way, how is Sayori and the rest of the girls?."
    n n4f "Why he had to ask about Sayori...?"
    n n4r "Urgh..."
    n n42f "Sayori was transformed into a robot by Dr. Eggman, and our world was destroyed thanks to a shit thing called Phantom Ruby."
    n "We arrived at this portal seeking for help. If we don't have all the help we can, Sonic's world will be destroyed too and we will never recover Sayori and Yuri..."
    show philoso at lhide zorder 1
    hide philoso
    show natsuki at lhide zorder 1
    hide natsuki
    show cookies ncookieSprite at f41 zorder 2
    show oneterm ntermSprite at t42 zorder 3
    show skull nskullSprite at t43 zorder 2
    show serg nsergSprite at t44 zorder 2
    coo "OH NO! This is terrible, I'm really sorry about that!"
    onT "That is the worst thing ever!"
    skl "Goddamit, that was like a punch in that zone!"
    show natsuki n42f at l41 zorder 3
    show serg nsergSprite at f44 zorder 2
    ser "That is terrible..."
    ser "Guys, we need to find some form of helping."
    onT "Dragon tells me that I must gift this thing he found yesterday to Natsu and Rookie..."
    n n42h "That is... a Chaos Emerald..."
    show emerald blue at t21 zorder 4
    $ persistent.emeraldCount = 4
    play sound Emerald_word
    "{i}You won a Chaos Emerald!\n(Click to continue...){/i}"
    "Now we have [persistent.emeraldCount] Chaos Emerald!"
    mc "Time to save this Chaos Emerald with us. Thanks Term!"
    show emerald at thide zorder 1
    hide emerald
    show natsuki at lhide zorder 1
    hide natsuki
    onT "Always glad to give friends a hand."
    show cookies ncookieSprite at t41 zorder 2
    show oneterm ntermSprite at t42 zorder 3
    show skull nskullSprite at t43 zorder 2
    show serg nsergSprite at f44 zorder 2
    ser "Well, guys. Our night party was almost ending anyways."
    ser "We trolled Gemini0 already, made Logokas scream \"YOU CAN'T POST YOUR SHITTY MEMES ON THE MOD_ART CHANNEL!\"..."
    ser "CPG Yuri sent me his daily virtual hug and I had a long chat with my sweetheart Destiny, so..."
    ser "What about going with Natsuki and help her?"
    "Everyone smiled and did a little dance. It's seems we have four new people for the price of one portal."
    show oneterm ntermHappySprite at f42 zorder 3
    show cookies ncookieSprite at t41 zorder 2
    onT "LET'S GO TO KICK SOME ASSES!!!!"
    coo "Term! LANGUAGE! No bulli and swearing, this is a Christian Club!"
    onT "Sorry Cookies!!!!"
    "And so, after everyone laughed, the six of us went to the exit portal, that was located at the end of the school hall..."
    return

label ghost_exclusive_3:
    scene bg hidrocity
    with dissolve_scene_half
    if persistent.packagedMusic == True:
        play music hidrocityPCKG
    else:
        play music hidrocity
    show ghostnatsuki gNatsu1 at t33 zorder 3
    show portal genesisportal at t32 zorder 2
    "Ghost and I are prepared to enter the Genesis Portal."
    g "Wish us luck, girls, I have a good feeling about this one!"
    n "Good luck, alternate me!"
    m "Be brave!"
    "And, after the hugs and goodbyes and the briefings of the mission, we entered the portal..."

    "You got 500 rings for going to the portal with Ghost!"
    play sound Ring
    $ persistent.ringCount += 400
    "You now have [persistent.ringCount] Rings!\n{i}Click to continue...{/i}"

    scene bg scp_room
    with dissolve_scene_full
    stop music fadeout 2.0
    play music ghostmenu
    "What a strange world is this!"
    "We are in a strange building. It looks dark. Everything looks dark and gloomy."
    "I can see the letters C and P on a big letter at the left, and it looks like the big hall before the Literature Club classroom, but evil..."
    "And... it seems like {i}something{/i} is there..."
    show ghostnatsuki gNatsu1 at l22 zorder 2
    g "OH BOY! This is a dream come true for me!"
    g "Welcome, Rookie, to one of my favourite places in the world!"
    g "This is one of the headquarters of the SCP Foundation!"
    g "Secure. Contain. Protect. And save the world from Euler and Kepler and shitty dangers to this thinner and fragile planet."
    mc "Sure thing, but this place seems dark. Why we are here?"
    g gNatsu2 "I think that we are here because there is one specific creature on this world that can help us in the mission."
    g "If this portal can sense the things we want and love, then we are in the right prison then."
    g "The creature I'm looking for needs very specific containment procedures that can only be fulfilled in this exact prison. Let's enter that door, it seems it's the Security Room."
    g "Oh, and don't pay attention to that creature there. It's SCP-163 and is somehow dangerous. We don't want him to be following us all the building, just keep looking at me, Rookie."

    scene bg scp_video
    with dissolve_scene_half
    g "THERE IT IS, ROOKIE!"
    mc "Whoa! What is that... thing?"
    "Ghost pulls one of the computers and accesed some kind of secret files using a password from certain Dr. Light, and showed me a strange creature on one of the security feed cameras."
    g "SCP-682: The Hard to Destroy Reptile, or as some others call it, The Invincible Lizard!"
    mc "WAIT GHOST! DID YOU LET THE PORTAL TRANSPORT US HERE TO TALK OR FIGHT WITH AN {i}INVINCIBLE{/i} THING? ARE YOU CRAZY?"
    g "CAN YOU JUST LISTEN TO ME, PIECE OF SHIT?"
    g "According to the files, SCP-682 appears to have a hatred of all life, which has been expressed in several interviews during containment."
    g "But if you forgot, I'M NOT ALIVE. I'm a Ghost and a Glitch, I'm not a 100%% living being, so I'm sure this Lizard will help me."
    mc "I still think that you are crazy, but sure, it's your idea and I promised to trust everyone of you."
    g "THAT'S THE SPIRIT! LET'S GO TO THE LIZARD'S CONTAINMENT PRISON!"

    scene bg scp_682
    with dissolve_scene_half
    play music scp682Portal
    "And here we are."
    "Using the glitchy abilities of Ghost, we trespassed a lot of rooms and buildings, and arrived at this place."
    "According to what Ghost explained to me, SCP-682 is a large, vaguely reptile-like creature of unknown origins, and for some luck, they discover that maybe it's female."
    "To this date, successful breaches of the lizard have numbered at 6, and a big quantity of attempted escape from SCP's buildings."
    "It seems SCP-682 it's eating... the skeleton of a poor person. Ghost said that they are called D-Class personnel, and are asshole humans to start, so she said that this was justice."
    "AND SCP-682 NOTICED US!"
    liz "I... HATE... LIVING BEINGS... AND YOU ARE ONE OF THEM!!!!"
    show scp scpLizard682 at t22 zorder 2
    show ghostnatsuki gNatsu1 at t21 zorder 3
    g "SCP-682. My name is Ghost Natsuki, and I'm here to free you from this containment and asking you for help..."
    liz "YOU... ARE... WITH... A DISGUSTING BEING!!!!"
    liz "I... HATE... LIVING BEINGS!!!!"
    liz "DO YOU KNOW WITH WHO ARE TREATING, WEAKLINGS???"
    g gNatsu2 "SURE THING, UGLY STUPID ASSHOLE LIZARD OF THE DEMON! I BELIEVED YOU WERE MORE INTELLIGENT BUT YOU ARE THE SAME PIECE OF SHIT AS ROOKIE AND THE PLAYER!"
    g "FIGHT WITH US! I'M NOT AFRAID OF YOU!!!!"
    mc "WHAT THE FUCK ARE YOU DOING, GHOST?????????"
    liz "OH. A CHALLENGE. VERY WELL. SURVIVE, AND MAYBE I WILL PAY ATTENTION TO YOUR PETITION."
    "Great, now we have to fight with the invulnerable thing. Congratulations, stupid portal."

    scene bg scp_682
    with dissolve_scene_half
    show scp scpLizard682 at t22 zorder 2
    show ghostnatsuki gNatsu1 at t21 zorder 3
    g "And we survived! What did I told you?"
    "I try to give Ghost a natural smile, but I'm still scared about the power of that creature, and it's terrifying resistance to everything."
    liz "WELL, WELL, WELL... THE DISGUSTING THING... SURVIVED."
    liz "YOU, GHOST, AND THE DISGUSTING THING HAVE MY COMPLETE ATTENTION."
    "Ghost explained to SCP-682 about the problem in my world, and she suggested the Lizard that it can have Infinite as a delicious lunch."
    "In exchange, Ghost will give the Lizard some hours of freedom from the assholes of the SCP Foundation."
    liz "Disgusting weakling living being called Rookie."
    liz "You... proved to me... to be strong."
    liz "And because you are freeing me, I will be loyal to your cause."
    liz "Bring me to the place when I can destroy things and eat more weaklings!!!"
    liz "And I will show that asshole Infinite why they call me {i}The Hard to Destroy Reptile{/i}."
    mc "Very well, SCP-682, let's hurry. The portal moved to another place and we will have to run from some other rooms right now."
    liz "OH. BY THE WAY. This weakling D-class shit had a shiny rock with him. I think you are more worthy of that."
    show emerald blue at t21 zorder 4
    g "HEY PIECE OF SHIT! IT'S ONE OF THOSE SHINY ROCKS! DIDN'T TOLD YOU THIS WOULD BE A SUCCESSFULL MISSION?"
    $ persistent.emeraldCount = 4
    play sound Emerald_word
    "{i}You won a Chaos Emerald!\n(Click to continue...){/i}"
    "Now we have [persistent.emeraldCount] Chaos Emerald!"
    mc "Time to save this Chaos Emerald with us. Thanks, SCP-682."
    show emerald at thide zorder 1
    hide emerald
    liz "SAY. THANKS. LATER. WHEN I CAN FEAST OF INFINITE'S REMAINS."
    g gNatsu2 "My favourite creepy creature and me! This is a dream come true! HAHAHAHA!"
    "And so, the three of us went to the exit portal..."
    
    return
