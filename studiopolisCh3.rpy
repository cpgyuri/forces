label chapter3:
    scene bg tcStudiopolis
    with dissolve_scene_full
    pause 3.0
    scene bg studiopolis
    with dissolve_scene_half
    if persistent.packagedMusic == True:
        play music studioPCKG1
        show honey djHoney at l31 zorder 5
        dj "Now playing: {i}Planet Funk - Lemonade{/i}, from the best oldie goldie remixes of the great Benny Benassi!"
        show honey at lhide zorder 1
        hide honey
    else:
        play music studioP1
    $ persistent.yuriKnife == True
    play sound NegaRing
    $ style.say_dialogue = style.edited
    "There is no turning back now."
    "I WILL MAKE SURE the Yuri Empire comes to fruition..."
    "{i}...with your help or without it.{/i}"
    $ style.say_dialogue = style.normal
    show monika 1g at l41 zorder 2
    m "Aw, man..."
    m "Is everyone here? Are you all ok? Is anyone hurt?"
    mc "Don't worry, we're fine. Just some scratches because the of the fall..."
    show sonic sonic05 at l44 zorder 3
    sth "I really hate when they use that annoying Phantom Ruby..."
    show sonic sonic11 at h44 zorder 3
    amyR "Sonic???? Is that you????"
    sth sonic10 "NO WAY, IT'S HER!!!!"
    show amy amy04 at l43 zorder 4
    amyR "SONIC!!!! YOU ARE ALIVE!!!! THANK THE MASTER EMERALD!"
    sth sonic08 "I'M FINE AMY, THANKS."
    sth "Honestly, this is not the time for you to act like that. I clashed with another yandere already..."
    amyR amy02 "Yuri?"
    sth sonic07 "EXACTLY. Yuri! She is working for herself thanks to the Phantom Ruby!"
    amyR amy10 "That Yuri! She is the real obnoxious brat and worse, a traitor!"
    amyR "We started to spy on her since she was rescued by Rookie, but now she is hiding her footprints from us. And from Eggman too."
    sth "We will make sure she doesn't interfere with our mission of freeing our world."
    sth "We will need to purge the corruption from her."
    amyR "By the way, Rookie, there is another person who wants to talk with you..."
    mc "Huh? Is he or she here?"
    show ghostnatsuki gNatsu2 at l42 zorder 2
    show sonic sonic09 at h44 zorder 3
    show amy amy02 at h43 zorder 4
    if persistent.packagedMusic == True:
        play music ghostNPCKG
    else:
        play music ghostNatsuki
    g "Here I am."
    g "...Oh. Hi Monika! {i}wink{/i}"
    g "And a special hello for the PIECE OF SHIT WITH A KEYBOARD AND A MOUSE OUT THERE!"
    m 2q "First the insults from Yuri. Then the creepy stuff. Then Robo-me. Now my glitches are coming to haunt me too?"
    m 2h "Please ping me on the communicator when this ends, ok? I need time to clear my thoughts."
    show monika at thide zorder 1
    hide monika
    g "Oh. I didn't came to haunt Monika, or anyone. In fact, I'm on your side."
    g "But first sorry, it's difficult to talk like that. Let me fix it."
    play sound "sfx/crack.ogg"
    show ghostnatsuki gNatsu1 at h42 zorder 2
    g "There, much better."
    show sonic sonic11 at l44 zorder 4
    show natsuki 4o at l41 zorder 2
    n "NO. FUCKING. WAY.\nYOU."
    g "Yes. Me. Hi.\nI'm Ghost Natsuki."
    g "And believe it or not, I'm on your side."
    amyR "Can you elaborate on that, miss Ghost?"
    g "Sure! Somehow, the same power that revived MC of our universe, gave me life and form at the start of this adventure."
    g "And I sense danger coming."
    n 4u "So now I must trust my corrupted form..."
    n 4m "Well, at least you are not doing anything bad this time. You could have killed us or something since the start."
    g "Exactly! I was secretly helping Rookie, but now that Yuri revealed her intentions, I can't be on the sidelines!"
    g "{i}But there is a certain piece of shit that loves to ruin the work of others it seems.{/i}"
    g "I will help you with your missions from now on. I can't stand being an NPC like Monika was."
    sth sonic13 "All help is welcome on the Resistance. Also you are a part of Natsuki, so I trust you too."
    n 4d "And if you will help us, then I trust you too."
    g "I can't say that this is the happiest day ever, but now the Resistance is bigger."
    amyR amy00 "Yeah! Sonic, Tails, our captain Knuckles, myself, Rookie, Monika, Natsuki, Sayori, MC, and now you!"
    sth "We have the perfect team for taking down Eggman and Infinite's invasion, and stopping Yuri and her trashy robot imitations."
    sth sonic15 "Let's move team, it's time to kick some butt!"

#Special Event related to Sonic Mania with Doki Doki Studiopolis Club mod...
scene bg studiopolis
with wipeleft_scene
play music monikaSong
if persistent.sonicMania == True:
    "MOD'S AUTHOR MESSAGE: Thanks for playing my Sonic Mania mod! It was made with love and dedication. Enjoy this little scenes!"
else:
    "MOD'S AUTHOR MESSAGE: Hey, I hope this motivate you to try Sonic Mania and my Doki Doki mod! Enjoy this little scenes!"
show monika 4b at t43 zorder 2
show natsuki 1d at t42 zorder 3
show mc2 1c at t44 zorder 5
show sayori 1x at t41 zorder 4
m "We were here before. This is Studiopolis Zone."
n 4v "Of course we were here, Monika! We were featured in a Sonic Mania mod!"
n 5w "You sure have a poor memory span, Monika."
s 4x "YEAH! I DID THE RAINCLOUDS ATTACK! IT FITS ME SO WELL!"
s 2q "Natsuki has the sun attack."
s 3q "And Monika directed everything from the TV screen! Also a lot of posters and neon signs and stuff!"
mc2 "And we recorded a musical video with Monika's lyrics and Natsuki's flute solo."
show yuri 3y3 at l41 zorder 5
y "AND I HAVE THE WIND ATTACK, THE BEST ONE. YOU CAN BE KILLED WITH THE SPIKES ON THE CEILING!"
y 3b "Isn't that poetic justice for your mistake, player?"
n 5y "Did I need to remind you that you are the villain in this mod, Yuri?"
y 2y7 "URGH! NATSUKI! WHY DO YOU ALWAYS HAVE TO RUIN MY MOMENTS!"
y cuts2 "Anyways, I hope the player loves the special surprise I made for them in the EGGTV screens."
y cuts3 "Now I have to go back and prepare myself for this chapter." 
y cuts5 "STUPID NATSUKI THE QUEEN OF THE CUTE THINGS, TRYING TO BE CUTE AND FAILING MISERABLY..."
show yuri at lhide zorder 1
hide yuri
n 5y "Watch out, you may cut yourself on the EDGE of the screen, edgy bitch!"
n 4o "Wait..."
n 1v "I'M NOT CUTE!"
mc2 1n "Girls, focus! Isn't this a shameful way to advertise the mod?"
show ghostnatsuki gNatsu2 at l41 zorder 5
show natsuki 5o at t42 zorder 3
g "Actually, a shameful way to advertise it is doing this:"
g "Hey, you! Download {i}Doki Doki Studiopolis Club{/i} Mod for Sonic Mania today on GameBanana!"
g "And fulfill Natsuki's dream of being part of a Sonic game!"
g "The author of that mod is the same one of this mod! And he will thank you for that."
g "So, you piece of shit, visit this URL:\nhttps://gamebanana.com/skins/159794"
show ghostnatsuki at thide zorder 1
hide ghostnatsuki
show natsuki 1v at h42 zorder 3
n "STOP REPEATING MY LINES FROM THE TRAILER!!!!"
g "SORRY! CONTRACTUAL OBLIGATIONS!"
show sonic sonic06 at l41 zorder 5
sth "Well girls and guy, it's best that you keep skateboarding with your Extreme Gears. We don't want to leave you all behind."
show sonic at lhide zorder 1
hide sonic
m 1h "Absolutely. let's keep moving. Too much Breaking the Fourth Wall."
mc2 1e "Yeah, that's for the best."
s 1j "Did you all were reading about the Fourth Wall on TVTropes? That website will ruin your lives!"
n 4v "SAYORI GODDAMMIT! MY LIFE IS ALREADY RUINED, WITH OR WITHOUT TVTROPES!"
n "AND JUST CONTINUE THE SCRIPT ALREADY!!!!!!"
"CHOOSE YOUR FAVOURITE DOKI! IF YOU PICK YOUR OPTION, MAYBE YOU CAN WIN A SPECIAL PRIZE! ONLY IN PINK BOT STORES!!!"
"JUST PLAY OUR DOKI DOKI MINIGAME ON THE INTERACTIVE NEW EGGTV TOUCH MONITORS! ONLY 5 RINGS PER PLAY!"
mc "Hey girls and MC, let's try that minigame! It looks fun!"

scene bg chibiMonika
with wipeleft_scene
"While we roamed around Studiopolis Zone, we found a big touch monitor in one of the Pink Bot TV stores."
"Th EGGTV logo was on the monitor, along with a cute chibi Monika, close to a microphone!"
"The voiceover was saying: \"CHOOSE YOUR FAVOURITE DOKI! IF YOU PICK YOUR OPTION, MAYBE YOU CAN WIN A SPECIAL PRIZE!\" at a high enough volume to notice it."
"That was an opportunity none of us could refuse, don't you think?"
"So the girls, MC and I got closer to the monitor. The minigame asks you to choose your favourite Doki!"
"Everyone was eager to know who my favorite is. Tough decision!"
stop music fadeout 2.0
menu:
    "WHICH DOKI WILL YOU CHOOSE?"
    "President Monika!":
        scene bg chibiMonikab
        $ ch4_scene = "monika"
        mc "I choose Monika, of course!"
        play music t9
        mc "She is awesome, has hacking powers, apologized to everyone and is doing a great effort on being positive."
        mc "That impresses me so much!"
        "And also she is VERY sexy, damn, those legs..."
        m "Thank you for trusting in me, Rookie! I will always do my best as President of the Literature Club to help the Resistance!"
        "Suddendly the ambience got filled with a smell of ink and that characteristic scent of a new book."
        scene bg chibiEmeraldM
        "AND THEN, THE MONIKA STICKER GOT HAPPY AND BRINGED TO US THE GREEN CHAOS EMERALD! WHAT AWESOME LUCK!"
        $ persistent.emeraldCount += 1
        play sound Emerald_word
        "{i}You won a Chaos Emerald!\n(Click to continue...){/i}"
        "Now we have [persistent.emeraldCount] Chaos Emerald!"
        "After I did my election, the minigame was over, so we took our Extreme Gears and continue running through the zone."
        "Monika was very happy after my choice. She started to share poems with me and everyone, and at last, commenting about their previous adventure in Studiopolis..."
        "..."
        m "I will not fail anyone, anymore. My sweet love, I know you can hear me! Soon we will be together and save these worlds."
        m "I still need you, for giving me strenght, confidence, and love."
        $ renpy.call_screen("dialog", "Please help me.\nHelp Rookie.\nHelp all of us.\nSave Yuri.\n\nAnd keep loving me.", ok_action=Return())

    "Cinnamon Bun Sayori!":
        scene bg chibiSayori
        $ ch4_scene = "sayori"
        mc "I choose Sayori, of course!"
        play music t9
        mc "She is very happy, she is clumsy but her ideas are clever. She revived her boyfriend with her bare will, and she loves onion rings sandwiches, just like me!"
        mc2 "Hey Rookie, thanks for selecting my sunshine! That makes me happy! And wow, I got a chibi too! I look awesome!"
        s "Thank you for choosing me, Rookie! I know I'm clumsy, but with your help and MC's help, I will be useful for the Resistance!"
        "Suddendly it started to rain, and the air got filled with a smell of orange juice."
        scene bg chibiEmeraldS
        "AND THEN, THE SAYORI AND MC STICKERS GOT HAPPY AND GAVE US THE GREEN CHAOS EMERALD! AWESOME!"
        $ persistent.emeraldCount += 1
        play sound Emerald_word
        "{i}You won a Chaos Emerald!\n(Click to continue...){/i}"
        "Now we have [persistent.emeraldCount] Chaos Emerald!"
        "After I made my choice, the minigame ended. so we took our Extreme Gears and continued running through the zone."
        "Sayori and MC kissed in a very cute way! Cue the awwwwwwws. (AAAAAAAAW!)"
        "And then they started to tell us their adventure trying to making pizza and cupcakes, and how Sayori almost burned MC's house down..."
        "..."
        s "I know my rainclouds will not go away very easily, but thanks to you, I'm not alone anymore. I will always love you."
        mc2 "And I will be always be here for you. I know what is best for both of us, and we will be together until the end."
        
    "Parfait Girl Natsuki!":
        scene bg chibiNatsuki
        $ ch4_scene = "natsuki"
        mc "I choose Natsuki, of course!"
        play music t9
        mc "She knows almost everything about our world, her cupcakes are tasty, she loves manga, and her poems are very expressive!"
        "And also she is cute, but I can't say that out loud."
        n "Thank you for choosing me, Rookie! You are a man of culture, punk! And with me here, this will be a piece of cake!"
        "Suddendly the temperature got warmer, and the air was filled with a smell of baked cupcakes of different flavors."
        scene bg chibiEmeraldN
        "AND THEN, THE NATSUKI STICKER GOT HAPPY AND GAVE US THE GREEN CHAOS EMERALD! AWESOME!"
        $ persistent.emeraldCount += 1
        play sound Emerald_word
        "{i}You won a Chaos Emerald!\n(Click to continue...){/i}"
        "Now we have [persistent.emeraldCount] Chaos Emerald!"
        "After I made my choice, the minigame was over. So we took our Extreme Gears and continued running through the zone."
        "And Natsuki started to tell us about why she loves the Parfait Girls manga, and how that story made her find her passion, baking for her friends and herself..."
        "..."
        n "Thanks for not saying that I'm cute. I know you think that. And thanks for letting me help in this adventure!"
        n "I can't stop crying, being loved is the best sentiment. BUT REMEMBER! SONIC AND I WILL STILL KICK EGGMAN'S ASS, PUNK!"
        
    "Just Yuri always!":
        scene bg chibiYuri
        $ ch4_scene = "yuri"
        mc "I choose Yuri..."
        play music t9
        mc "Wait, why did I choose her? She's our enemy!"
        mc "Oh no, I made a mistake. Sorry girls!"
        mc "I probably selected her because I saved her first, and I'm still worried about her."
        "I really am still worried about her. I can't let the Phantom Ruby control her!"
        m "It's ok, Rookie! Yuri is normally amazing and very shy, and we know that she is being controlled. We will recover our friend."
        "Suddendly a wind current started to form, and the air got filled with a smell of jazmine aromatic flowers and different flavours of tea..."
        "No way! Yuri started to talk through the sound system of the store!"
        play sound NegaRing
        y "HAHAHAHAHAHA! I KNEW YOU WOULD CHOOSE ME AFTER ALL, ROOKIE!"
        y "IT'S GOOD TO SEE THAT I LEFT AN UNFORGETTABLE IMPRESSION ON YOU! KISSES!"
        y "AND I SERIOUSLY HOPE YOU DIDN'T CHOOSE ME BECAUSE OF MY BOOB SIZE, OR ELSE..."
        mc "YES I CHOSE YOU BECAUSE OF YOUR BOOBS! THERE, I SAID IT!"
        stop music
        play sound djstop
        scene bg chibiYuriEmpire
        y "OH MY GOD, I'M GOING TO KILL YOU! METAL TRASHY!!!! STOP SELF-REPAIRING AND GO AFTER THEM!!!!"
        m "METAL. TRASHY-ONIKA! STILL CAN'T MOVE, BOSS!"
        y "AAAAAAAAH YOU INCOMPETENT STUPID ROBOTS!!!!"
        mc "CAN YOU LET ME {i}EXPLAIN MY DECISIONS{/i}, PLEASE?"
        "Everybody fell silent, even Yuri and her robot."
        play music t9
        mc "Yuri! If you are listening to me, I choose you because I care about you!"
        mc "I don't think you are evil! Your friends love you! And I'm sure my own friends will love you too!"
        mc "Don't take Sonic's word as fact! There are people here that loved you and have you as their favourite Doki!"
        mc "We are fighting you because you are fighting us, and other reasons."
        y "..."
        m "BOSS. MESSAGE. bzzzzk. CUTE. PLEASE. DON'T GET. ANGRY!"
        y "Thank you."
        y "It's touching. It's the first time somebody said something nice to me here."
        y "You deserve the prize after all."
        scene bg chibiEmeraldY
        "The Yuri sticker got happy and brings to us the Green Chaos Emerald. But I still feel uneasy about my decision..."
        $ persistent.emeraldCount += 1
        play sound Emerald_word
        "{i}You won a Chaos Emerald!\n(Click to continue...){/i}"
        "Now we have [persistent.emeraldCount] Chaos Emerald!"
        y "Hey, asshole! Stop feeling bad. I sincerely thank you for your concern. Is just that we are on different sides of the coin, that's all."
        y "The only ones I hate right now are Trashonika and the Obnoxious Brat!"
        y "So, take that stupid prize before I change my mind! Metal Monika still awaits my orders!"
        "After I made my decision, the minigame ended. So we took our Extreme Gears and continue running through the zone."
        "But I still feel bad about my decision, despite the Chaos Emerald."
        "The rest of the girls and MC tried to comfort me while we travelled, and we had an emotive conversation about Yuri's favourite books and poetry styles."
        "..."
        y "I can't believe that, despite everything, Rookie still thinks so highly of me..."
        y "And maybe having big {i}attributes{/i} isn't so bad after all..."
        m "BOSS. MORON'S. MESSAGE. TOO SAD AND EMOTIVE. CRYING bzzzzk OIL TEARS!"
        y "I still think there is something wrong with me. Player, if you know something, help Rookie and my friends."
        y "Sadly, emotions and everything aside, the Yuri Empire will continue it's course, and I will not stop it."
        
    "Play with me, Ghost!":
        scene bg chibiGhost
        $ ch4_scene = "ghost"
        mc "I choose Ghost!"
        play sound djstop
        m "What?"
        s "Ghost?"
        mc2 "..."
        n "DO YOU HATE US THAT MUCH?"
        dj "Sorry for listening, but... Seriously?"
        g "PIECE OF SHIT, BETTER START EXPLAINING..."
        "Everyone looked at me with angry expressions, so I had to explain myself."
        play music t9
        mc "Well, the Ghost is a glitch, but she was helping me making choices (and someone she always calls a Piece of Shit)"
        mc "She was eager to help us, and we couldn't discriminate against her because we don't know her yet"
        mc "As Natsuki said, if she is evil, she would've killed us already!"
        mc "Remember that she was the one who came to us, offering to help. And {i}Sonic{/i} was the one who accepted her on the Resistance!"
        mc "First rule of the Resistance: Nobody questions Sonic's or Captain Knuckles' decisions."
        m "Girls, respect Rookie's decision. He has his argument and it's fair. And that doesn't mean he hates us, Natsuki."
        g "Well, now I'M surprised. Neither you or the player are a piece of shit anymore in my non existant eyes."
        g "Thank you for trusting me, Rookie. My offer to help you will not be in vain."
        "Suddendly the illumination got spooky, and the air got filled with a smell of strawberry ectoplasm."
        scene bg chibiEmeraldG
        "AND THEN, THE GHOST STICKER GOT HAPPY AND GAVE US THE GREEN CHAOS EMERALD! AWESOME!"
        $ persistent.emeraldCount += 1
        play sound Emerald_word
        "{i}You won a Chaos Emerald!\n(Click to continue...){/i}"
        "Now we have [persistent.emeraldCount] Chaos Emerald!"
        "After I made my choice, the minigame was over. So we took our Extreme Gears and continued running through the zone."
        "But I had to reassure everyone that I love them all and everybody is a friend to me. Jeez."
        "Ghost told us her backstory, how she wanted to be a character in and of herself, and what she expects from us."
        "Monika said sorry to her, everyone hugged Ghost, and then she told Natsuki her recipe to make little ghostly stawberry cupcakes..."
        "..."
        g "HEY YOU PIECE OF SHIT! Thank you for this kind gesture."
        g "BUT DON'T EXPECT THAT I WILL STOP CALLING YOU A PIECE OF SHIT, PIECE OF SHI...{nw}"
        
pause 1.0
stop music fadeout 1.0
scene black
with wipeleft_scene
call screen confirm("You have unlocked a special poem.\nWould you like to read it?", Return(True), Return(False))
if _return:
    call expression "poem_special_" + "4" from _call_expression_48
    scene black with Dissolve(1.0)
else:
    pass
return


