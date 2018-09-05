# Chapter 2 static content. Poem responses called from here are in script-poemresponses.rpy

label chapter2_start:
    scene bg tcAngelIsland
    with dissolve_scene_full
    pause 3.0
    scene bg angelIsland_jungle
    show portal genesisportal at t11
    with dissolve_scene_half
    play sound "mod_assets/rubySound2.ogg"
    if persistent.packagedMusic == True:
        play music aizPCKG
    else:
        play music aiz
    "And here we are!"
    "After crossing the portal, my new friends and I are back in my world."
    "Nothing more refreshing that breathe the magnificent essence of the ocean."
    "The Captain surely has a beautiful resting place here on Angel Island."
    show monika 1a at t44 zorder 5
    show natsuki 4a at t42 zorder 4
    show sayori 1a at t43 zorder 3
    show yuri 3y3 at t41 zorder 2
    pause 1.0
    show yuri 1a at t41 zorder 2
    "And the girls of the Literature Club arrived safely!"
    show monika 4b at t44 zorder 5
    show natsuki 4l at t42 zorder 4
    show sayori 4n at t43 zorder 3
    show yuri 1y8 at t41 zorder 2
    "The girls are looking the landscape with admiration and surprise."
    "Except Yuri, for some reason, but I'm afraid to question it."
    if persistent.yuriKnife == True:
        y 1crazy "What's happening, Rookie?"
        y "Oh my! Did you noticed that I'm not acting like my other friends?"
        y 3y8 "Well, too bad!"
        y "If you still think you will rescue Ghost and MC, you are totally wrong!"
        y 3y4 "Why we don't just sit down on these magical trees and do stuff using pens???"
        y 3y3 "It will be totally great!!!"
        mc "What is up with your disgusting fascination with pens, Yuri?"
    show yuri 1f at t41 zorder 2
    m "Surely, this is a beautiful place!"
    n "Yeah! I feel like if I'm in a eternal summer!"
    s 5a "Can we get some of those coconuts out there? I'm a little hungry..."
    s "Apart from that, the view is fantastic here. Ehehe~"
    y "And where we are supposed to find MC and the failed born sibling of Natsuki?"
    n 4o "OH COME ON!!! I WILL SMACK YOU HERE AND NOW!"
    m 9ad "This is not the time and place for fighting, you two! We need to help Rookie and find MC and the other one."
    m "Or else Rookie will have problems. Remember that the tablet is being tracked and Tails surely knows we took a detour."
    n 2r "Fine! Fine!"
    n 1x "But is better for everyone that Yuri stop her stupid jokes about me."
    n 4y "And since I'm the one with the most knowledge of Sonic's world, I suggest that we go to the left, at the beach!"
    m 4b "To the beach, then! Okay, everyone! We have a friend to save, let's go!"
    mc "And the Master Emerald may bless our journey! Viva la Resistance!!!"

    scene bg angelIsland_beach
    with dissolve_scene_full
    show pictures prisonegg at t22 zorder 3
    show eggrobo eggrobo at t21 zorder 4
    mc "Here we are, Angel Island's beach."
    "And, to my surprise, Natsuki was right!"
    "There's a flying PrisonEgg that we assume has Ghost and Sayori's lover trapped in there."
    "And the capsule is heavily custodied by EggRobos."
    "I will have to explain to the girls that we will need a plan of sorts, any distracting noise will make the EggRobos notice us and attack."
    show pictures at thide zorder 1
    show eggrobo at thide zorder 1
    hide pictures
    hide eggrobo
    show monika 1d at t44 zorder 5
    show natsuki 4g at t42 zorder 4
    show sayori 4b at t43 zorder 3
    show yuri 2e at t41 zorder 2
    mc "Okay, my fellow girls, this is the situation."
    if persistent.ddlc_femc:
        mc "That thing floating there is a PrisonEgg, it's a special capsule made by Dr. Eggman to imprison living beings."
        mc "He uses it to imprison our fellow little animals, the flowers of Little Planet, or whichever person of interest he wants to torture..."
        show monika 1g at h44 zorder 5
        show natsuki 4p at h42 zorder 4
        show sayori 4w at h43 zorder 3
        show yuri 1y7 at t41 zorder 2
        mc "So we can totally assume that [femc_name] and the weird Natsuki are there."
        s 1w "[femc_name], [femc_name]!!! Nooo~!!! Rookie, I need to save her, she is my everything!!!"
        show sayori 1u at t43 zorder 3
        mc "I know, Sayori, but the capsule is heavily custodied by EggRobos, robots modeled in the shape and image of the mad doctor."
    else:
        mc "That thing floating there is a PrisonEgg, it's a special capsule made by Dr. Eggman to imprison living beings."
        mc "He uses it to imprison our fellow little animals, the flowers of Little Planet, or whichever person of interest he wants to torture..."
        show monika 1g at h44 zorder 5
        show natsuki 4p at h42 zorder 4
        show sayori 4w at h43 zorder 3
        show yuri 1y7 at t41 zorder 2
        mc "So we can totally assume that [mc2_name] and the weird Natsuki are there."
        s 1w "[mc2_name], [mc2_name]!!! Nooo~!!! Rookie, I need to save him, he is my everything!!!"
        show sayori 1u at t43 zorder 3
        mc "But it's heavily custodied by EggRobos, robots modeled in the shape and image of the mad doctor."
    mc "So, we need a distraction that makes the EggRobos ignore the PrisonEgg for a while, so I can go and push that button on the bottom."
    if poemwinner[1] == "monika":
        show monika 1i at h44 zorder 5
        show yuri 3y1 at h41 zorder 2
        show natsuki 4o at h42 zorder 4
        mc "That's why I think Monika is the one who shall do the distraction!"
        m 1l "Ahaha~! Rookie! How cute you are!"
        n "ROOKIE, ARE YOU STUPID???"
        m 5b "IS THIS THE 'INSULT YOUR PRESIDENT' DAY??? ENOUGH, CUIT IT OUT, PLEASE!!!"
        m 4n "Rookie, I don't have any ideas for doing what you are asking to me..."
        "Monika seems to be frozen in place. Does she be scared?"
        mc "Just be creative, and be yourself. The EggRobos are programmed to hate the Resistance members, so they will follow you whatever thing you do."
        mc "Also, you said that you would do whatever for your club members, and you have two here that will be sent to Dr. Eggman if we don't do something."
        m 2ad "You are right, Rookie! I'm the President of the Literature Club!"
        m "It's {i}my{/i} duty to make my fellow club members be happy, healthy, and safe!"
        m "Now you all and that pile of metal and scrap will see why I'm the President!"
        
        scene bg angelIsland_beach
        with wipeleft_scene
        show monika 1e at t22 zorder 3
        show eggrobo eggrobo at t21 zorder 4
        m "{i}I'm not scared, I'm not scared, I'm not scared...{/i}"
        "When the EggRobos saw Monika approaching them, they assumed a warning stance."
        m 1b "Hello, nice, beautiful and shiny robots with the shape of an egg!"
        m 2b "Today, my Literature Club is taking a field day! We are getting inspiration from places like this beautiful beach..."
        m "...and transforming that inspiring energy in beautiful poems!"
        m "I will proceed to read to you all this awesome and cute poem from Natsuki, one of our club members!"
        m 1q "Ehem..."
        show eggrobo at thide zorder 1
        hide eggrobo
        play music oatmeal
        show monika 12a at t11 zorder 2
        "{i}Click through the dialogue to the rythm of the song!!!{/i}"
        m 12l "1, 2 O-oatmeal."
        m 12a "Natsuki is a pi-ink girl."
        m 12b "1, 2 O-oatmeal."
        m 5a "Because Natsu is very cu-u-ute."
        m 12l "1, 2 O-oatmeal."
        m 12a "Natsuki is a pi-ink girl."
        m 12b "1, 2 Oatmeal."
        m 5a "Because Natsu is very cu-u-ute."
        if persistent.ddlc_femc:
            m 12j "Natsu comes to [femc_name]'s house and makes cakes la-ha-ha-hater."
            m 12k "Natsuki's so happy that is something she can, be cause she's such a pi-ink gi-irl."
            m 12j "Natsu comes to [femc_name]'s house and makes cakes la-ha-ha-hater."
            m 12k "Natsuki's so happy that is something she can, be cause she's such a pi-ink gi-irl."
            m 12i "Here comes Natsu [femc_name] to protect, because she's attacked by Natsuki's Dad."
            m 12l "[femc_name] swings the fist of Natsuki's Dad defeat. What a triumph is that?"
            m 12i "Here comes Natsu [femc_name] to protect, because she's attacked by Natsuki's Dad."
            m 12l "[femc_name] swings the fist of Natsuki's Dad defeat. What a triumph is that?"
        else:
            m 12j "Natsu comes to [mc2_name]'s house and makes cakes la-ha-ha-hater."
            m 12k "Natsuki's so happy that is something she can, be cause she's such a pi-ink gi-irl."
            m 12j "Natsu comes to [mc2_name]'s house and makes cakes la-ha-ha-hater."
            m 12k "Natsuki's so happy that is something she can, be cause she's such a pi-ink gi-irl."
            m 12i "Here comes Natsu [mc2_name] to protect, because she's attacked by Natsuki's Dad."
            m 12l "[mc2_name] swings the fist of Natsuki's Dad defeat. What a triumph is that?"
            m 12i "Here comes Natsu [mc2_name] to protect, because she's attacked by Natsuki's Dad."
            m 12l "[mc2_name] swings the fist of Natsuki's Dad defeat. What a triumph is that?"
        m 12l "1, 2 O-oatmeal."
        m 12a "Natsuki is a pi-ink girl."
        m 12b "1, 2 O-oatmeal."
        m 5a "Because Natsu is very cu-u-ute."
        m 12l "1, 2 O-oatmeal."
        m 12a "Natsuki is a pi-ink girl."
        m 12b "1, 2 Oatmeal."
        m 12k "Because Natsu is our pink little cute!!!"
        stop music fadeout 2.0
        m 1b "Thanks for listening!"
        show eggrobo eggrobo at t33 zorder 3
        show monika 3b at h32 zorder 4
        show sayori 3f at l31 zorder 3
        s "I'm completely speechless with Monika's performance at this point..."
        show sayori at lhide zorder 1
        hide sayori
        show yuri 1y3 at l31 zorder 3
        show monika 9ad at t32 zorder 4
        y "And this, ladies and gentlemen and robots, is our moronic Club President. Applauses!"
        show yuri at lhide zorder 1
        hide yuri
        show eggrobo at l31 zorder 3
        "The Eggrobo said 'Alert, alert: An intruder of feminine gender with zero taste for poetry is approaching the PrisonEgg'"
        show natsuki 4o at t33 zorder 3
        show monika 1l at h32 zorder 4
        $ style.say_dialogue = style.edited
        n 4v "motherfucking monikammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
        $ style.say_dialogue = style.normal 
        n "Are you thinking the same as I, EggRobo?"
        "The EggRobo nods by turning on and off its lights."
        scene bg angelIsland_beach
        with wipeleft_scene
        if persistent.packagedMusic == True:
            play music aizPCKG
        else:
            play music aiz
        "Monika run as fast she can from the angry Natsuki and the troop of Eggrobos."
        "This is our chance to opening the PrisonEgg!"
        "I ran to the PrisonEgg and pushed the release button."
        "The prisoners are now free!"
    elif poemwinner[1] == "sayori":
        show sayori 1i at h43 zorder 3
        show yuri 3n at h41 zorder 2
        show natsuki 4o at h42 zorder 4
        show monika 5b at h44 zorder 5
        mc "That's why I think Sayori is the one who shall do the distraction!"
        if persistent.ddlc_femc:
            s 4j "I will do everything for my love, [femc_name]!"
        else:
            s 4j "I will do everything for my love, [mc2_name]!"
        s "What do you have in mind, Rookie?"
        mc "Just be creative, and be yourself. The EggRobos are programmed to hate the Resistance members, so they will follow you whatever thing you do."
        s "Okay! Sayori, here we go!!!"

        scene bg angelIsland_beach
        with wipeleft_scene
        show sayori 1q at t22 zorder 3
        show eggrobo eggrobo at t21 zorder 4
        "The EggRobos saw Sayori walking to them."
        "The troop was changing to an attack formation."
        
        s "Heeeeeey!"
        s 4q "How are you today, mister robot?"
        s 4r "You seem to have some friends of mine in that cute capsule of yours."
        s 1s "And one of those friends you have kidnapped is the love of my life..."
        s illusion1 "So I want to kindly ask that you give me back my friends."
        stop music
        s "Or else, there will be consequences."
        s "And believe me you don't want to see me angry."
        "The EggRobos were ready to attack Sayori!!! Oh no!!!"
        "What should I do??? I have the messaging app ready for messaging Tails."
        "Then, Monika puts her hand in my shoulder and looked at me with a reassuring face. Also Natsuki signaling me to keep looking."
        s illusion3 "Okay, you all asked for it!"
        s "SAAAYOOORIIIII PUUUUUUNCH~!!!"
        m "SAYORI WHAT ARE YOU DOING????"
        n "SAYORI!!!!!"
        "Sayori run in a collition course against the robots...!"

        scene bg angelIsland_beach
        with wipeleft_scene
        if persistent.packagedMusic == True:
            play music aizPCKG
        else:
            play music aiz
        show sayori 2s at t22 zorder 3
        s "And don't come back!!!"
        "That was amazing!!!"
        "Sayori punched so strongly against the captain of the EggRobo squad, that the force of the punch launched the robot into its team!"
        "The robots got destroyed after colliding with the PrisonEgg."
        "That means the PrisonEgg got badly damaged and opened itself to release the prisoners!"
        "The prisoners are now free!"
    elif poemwinner[1] == "natsuki":
        show natsuki 1o at h42 zorder 4
        show yuri 3y8 at h41 zorder 2
        mc "That's why I think Natsuki is the one who shall do the distraction!"
        n 1v "Rookie, the heck!!! What do you think I am???"
        n 1v "ME?!"
        n "I'M NOT A WORTHLESS DISTRACTION YOU KNOW!!!"
        n 2o "If you wanted to be fucking smacked, stupid animal, you totally deserve it now!!!"
        "Natsuki looks at the rest of the club"
        n 2o "But I'll do it, not because I want to or anything, but because I know I'm the best when it comes to this sort of stuff!!!"
        mc "Of course weren't you the self proclaimed expert on our world and Sonic???"
        show natsuki 2r at t42 zorder 4
        mc "Also, you said that those club members are your friends, and they will be sent to Dr. Eggman if we don't do something!"
        show natsuki 2s at t42 zorder 4
        mc "Do you want to be responsible of their loss? And making Monika and Sayori feel depressed for life?"
        show natsuki 2u at t42 zorder 4
        mc "Just be creative, and be yourself. The EggRobos are programmed to hate the Resistance members, so they will follow you whatever thing you do."
        show natsuki 2n at t42 zorder 4
        mc "You are the one who were really excited to meeting Sonic, so, if you want, do this for him and not for us. He will surely be impressed!"
        n 2s "You are right, Rookie!"
        n 3y "I'm the pro on Sonic, you will be impressed with what I will pull!"
        n 1d "Watch and learn, soldier!"
        n 2o "But I'll do it, not because I want to or anything, but because I know I'm the best when it comes to this sort of stuff!!!"

        scene bg angelIsland_beach
        with wipeleft_scene
        show natsuki 4d at t22 zorder 3
        show eggrobo eggrobo at t21 zorder 4
        "The EggRobos see Natsuki walking up to them."
        "The troops start changing to their attack formation."
        "Without warning Natsuki uses her lightning wispon and hits one of the robots!"
        "I facepalm. That's not a distraction..."
        m "You should've known better than to send Natsuki on an op like this."
        "Natsuki strikes a pose similar to one of Sonic's fighting stances."
        n 4y "Come and get some badniks!"
        mc "Natsuki!"
        n "Heh! Just leave it to me!"
        n 4d "I suggest that you all surrender before I destroy you all!"
        n "If you do, everyone will have free cupcakes made by me, Natsuki the master chef!"
        "The robots pointed their guns to Natsuki."
        show natsuki 4o at h22 zorder 3
        n "Guess that means..."
        "Her wispon sparks with electricity as she gets ready"
        n wispon "Time to beat the crap out the baking mix then!"
        "Natsuki shoots the robots with her wispon."
        "Despite my surprise and dissapointment, she destroyed all the EggRobos."
        "Then, she pushed the button of the Prison Egg and did one of the poses Sonic always does."
        "The prisoners are now free!"
    else:
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
        show monika at thide zorder 1
        show natsuki at thide zorder 1
        show sayori at thide zorder 1
        hide monika
        hide natsuki
        hide sayori
        show yuri 1y2 at h11 zorder 2
        y "No no no, this can't be!"
        y natsuAngry "If they rescue Ghost, she will have free reign to start suspecting!!!"
        y "I need to do something before Rookie suggest the idea of a distraction..."
        y 1crazy "Wait a second..."
        y 1y8 "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA"
        y natsuPro "Yuri, you are the most intelligent of the club..."
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
        show monika 1g at h44 zorder 5
        show natsuki 4y at h42 zorder 4
        show sayori 4w at h43 zorder 3
        show yuri natsuPro at t41 zorder 2
        mc "So, we need a distraction that makes the EggRob...{nw}"
        n 4v "YURI WHAT ARE YOU DOING???"
        "What is Yuri doing??? She is making hand gestures and noises for the EggRobos to notice our hiding place!!!"
        n 4x "Are you braindead, Yuri??? What is happening with your head!!!"
        play music t7a
        show monika at thide zorder 1
        show sayori at thide zorder 1
        hide monika
        hide sayori
        show natsuki at t22 zorder 2
        show yuri at f21 zorder 3
        y 1n "Natsuki!!"
        y 1r "Why don't you just mind your own business, you piece of trash? I'm doing what is best to everyone!"
        y "You...You're just..."
        "Please don't..."
        y 2s "Maybe you're just jealous that [player] appreciates my {i}posture{/i} more than your own flattened chest!"
        show yuri at t21 zorder 2
        show natsuki at f22 zorder 3
        n 1f "WHAT??? Are you full of yourself or the transdimensional travel fried your brain cells???"
        n 2h "What does your boobs size has to do with rescuing our friend?"
        show natsuki at t22 zorder 2
        show yuri at f21 zorder 3
        y 3n "Uuuu...!"
        y 1q "Okay, you win this one, but..."
        y 1r "What was the supposed plan that you had???"
        y "Attacking the robots with cuteness, cupcakes and your stupid as heck references to your stupid manga characters???"
        show yuri at t21 zorder 2
        show natsuki at f22 zorder 3
        n 1o "Uuuuuu...!"
        n 1x "That's it!!"
        n wispon "You know what?! I warned you before, now I will shoot straight to your ugly face!!"
        show yuri 3y3 at h21
        show natsuki at t22 zorder 2
        y "I dare you to try to do that, obnoxious brat!!"
        show yuri at t32 zorder 2
        show natsuki at t33 zorder 2
        show monika 3l at l41 behind yuri,natsuki
        m "Um, Natsuki, that's a little over the top--"
        show monika at h41
        show yuri natsuUWA at f32 zorder 3
        show natsuki 1v at f33 zorder 3
        ny "This doesn't involve you!"
        show monika at lhide
        hide monika
        show yuri 2y3 at f21 zorder 2
        show natsuki 4o at t22 zorder 2
        show sayori 4p at l41 behind yuri,natsuki
        if persistent.ddlc_femc:
            s "W-what are you two doing??? Our priority is rescuing [femc_name]!"
        else:
            s "W-what are you two doing??? Our priority is rescuing [mc2_name]!"
        show sayori at lhide
        hide sayori
        queue music t7g
        $ timeleft = 12.453 - get_pos()
        show noise at noisefade(25 + timeleft) zorder 3
        show vignette as flicker at vignetteflicker(timeleft) zorder 4
        show vignette at vignettefade(timeleft) zorder 4
        show layer master at layerflicker(timeleft)
        y 2y3 "Here she is, the real Natsuki! Taking her own insecurities on others like that, with warnings, yelling, and then making everything overly cute..."
        y yuriIllusion "That's why you totally deserve what your Dad does to you, Natsuki."
        show yuri at t21 zorder 2
        show natsuki at f22 zorder 3
        n 4o "Shut your fucking mouth, you wannabe edgy bitch! You don't know anything about my life!!!"
        show natsuki at t22 zorder 2
        show yuri 2y7 at f21 zorder 3
        y "Edgy...?"
        y 2r "Look who is talking, the girl that will totally suck the dick of that infamous {i}hedgehog{/i} everyone idolatres here!"
        show yuri at t21 zorder 2
        show natsuki at f22 zorder 3
        n 4f "Don't you fucking dare to bad mouthing about Sonic!!!"
        mtp "Rookie is everything ok with all of you there??? I will teleport to Angel Island to help you all!"
        n 4e "Look what are you doing, Yuri!!! You are forcing Tails to come here and see how useless and moron are you being!!!"
        show natsuki at t22 zorder 2
        show yuri 3y3 at f21 zorder 3
        y "And do you think I care???"
        y "Do you think I care about rescuing stupid dense and the other ugly copy of yours out there?"
        y 1k "Why we want another copy of yours? Your own cuteness and stupidity is enough for the club."
        show eggrobo eggrobo at l41 behind yuri,natsuki
        "The EggRobo pointed its gun to the two girls and demanded them to shut up and surrender to the Eggman Empire."
        show eggrobo eggrobo at h41
        show yuri natsuUWA at f32 zorder 3
        show natsuki 1v at f33 zorder 3
        ny "This doesn't involve you, too!"
        show eggrobo at lhide
        hide eggrobo
        "The EggRobo ran away scared of those two..."
        show yuri 3y3 at t21 zorder 2
        show natsuki at f22 zorder 3
        n 2y "Well, maybe I can be not as intelligent as yours, enlightened one..."
        n "But at least I don't have my arms full of bad doing tribal {i}cuts{/i}."
        show natsuki at t22 zorder 2
        show yuri at f21 zorder 3
        y 3n "D-Did you just accuse me of cutting myself??"
        y 3r "What the fuck is wrong with your head?!"
        show yuri at t21 zorder 2
        show natsuki at f22 zorder 3
        n 1e "Yeah, I accuse you! You always are cutting yourself everytime you go to the bathroom!!!"
        n "And let's not talk about your stupid obsesion with knives and pens, Yuri!"
        n "I'm sure you are thinking right now how to steal the stylus pen Rookie uses for the tablet, and then doing your wet stuff with it!"
        show natsuki at t22 zorder 2
        show yuri at f21 zorder 3
        y 3y7 "AAAAAH FUCKING MALNOURISHED ONE!"
        show yuri at t21 zorder 2
        "Please you two, don't drag me to this..."
        show yuri at f21 zorder 3
        y 2n "Rookie...!"
        y 2y2 "She-- She's crazy, just remove her from the team, she will ending ruining your mission!!!"
        "Damn!"
        show yuri at t21 zorder 2
        show natsuki at f22 zorder 3
        n 4w "That's not true!"
        n "You are the retarded one who is attracting the EggRobos here!!! Rookie, do something!!!"
        show yuri 3y8 at t21 zorder 2
        show natsuki 1g at t22 zorder 2
        $ style.say_dialogue = style.normal
        mc "..."
        $ style.say_dialogue = style.edited
        "{cps=*2}How did I get dragged into this in the first place?!{/cps}{nw}"
        "{cps=*2}I just want to help the girls in rescuing their friends...{/cps}{nw}"
        "{cps=*2}And helping the Resistance in our mission to save our world from Infinite and Dr. Eggman!{/cps}{nw}"
        "{cps=*2}Why those two don't shut the fuck up already!!!{/cps}{nw}"
        "{cps=*2}Shut up Yuri!!!{/cps}{nw}"
        "{cps=*2}Shut up Yuri!!!{/cps}{nw}"
        mc "{cps=*2}Shut up Yuri!!!{/cps}{nw}"
        mc "{cps=*2}Shut up Yuri!!!{/cps}{nw}"
        mc "{cps=*2}Shut up Yuri!!!{/cps}{nw}"
        mc "{cps=*2}Shut the fuck up already, Yuriiiiiiiiiiiiiiiiiiii!!!{/cps}{nw}"
        $ style.say_dialogue = style.normal

        show black zorder 7
        show layer master
        hide noise
        hide flicker
        hide vignette
        stop music
        pause 3.0

        hide black
        show yuri lovelyEyes at t32 zorder 4
        show natsuki 1o at t31 zorder 2
        show sayori 4p at t33 zorder 2
        show boss5 heavyGunner at t32 zorder 3
        $ style.say_dialogue = style.edited
        play sound ruby
        y "My work here is done. I see you in Green Hill, [player]."
        $ style.say_dialogue = style.normal
        show yuri at thide zorder 1
        play sound "mod_assets/rubySound2.ogg"
        hide yuri
        if persistent.packagedMusic == True:
            show honey djHoney at l31 zorder 5
            play music heavyMagicianPCKG
            $ forces.edmsession_music("Alesso - Anthem")
            dj "This wasn't supposed to play so early in the game, but well..."
            dj "Now playing: {i}Alesso - Anthem{/i}, the song of the Hard Boiled Heavies!"
            show honey at lhide zorder 1
            hide honey
        else:
            play music heavyMagician
        show natsuki 1o at t42 zorder 2
        show sayori 4p at t43 zorder 2
        show boss5 heavyGunner at t41 zorder 3
        show monika 1g at t44 zorder 2
        mc "IT'S THE HEAVY GUNNER!!! HE WASN'T SUPPOSED TO BE IN ANGEL ISLAND!!!"
        s "What we gonna do??? What we gonna do???"
        n "Yuuuuuuuri!!! Yuri, piece of absolute useless jerk, she did this on purpose!!!"
        m "What now, Rookie?"
        mc "I wasn't prepared to fight an Eggman's enforcer right now."

    scene bg tcGreenHill
    with dissolve_scene_full
    pause 3.0
    scene bg greenHill1
    with dissolve_scene_half
    if persistent.packagedMusic == True:
        play music greenHillPCKG
        show honey djHoney at l31 zorder 5
        dj "Now playing: {i}RIO - After the Love{/i}, a beat that reminds you of the tropical beaches!"
        show honey at lhide zorder 1
        hide honey
    else:
        play music greenHillZ1
    
    show sonic sonic00 at t11 zorder 2
    "I started to think why Sonic loves this place so much..."
    "Oh yeah! Sonic! The Resistance assigned me to the special mission of saving him."
    "At the start of the war, we were about to have a tournament of Extreme Gear Skateboards."
    "Even Eggman was doing the charade of being friendly and organized the event."
    show sonic sonic09 at t11 zorder 2
    "But everything went to hell afterwards. Thanks to Infinite. And Eggman too."
    "Sonic tried to fight Infinite, but him was too much for our hero and Eggman captured him."
    "After Eggman captured Sonic and took him Chaos knows where, everything went downhill."
    show sonic at thide zorder 1
    hide sonic
    show amy amy06 at t33 zorder 4
    show knuckles knuckles04 at t32 zorder 3
    show tails tails06 at t31 zorder 2
    "Amy and Tails got sad and dissapointed, but Knuckles railed them to fight for justice!"
    "Since Knuckles is the older one and with the most combat experience, he assumed the role of Captain of the Resistance."
    "Our Resistance is formed by our Captain, Amy, Tails as the inventor, myself, and now we will have the help of the Literature Club."
    if persistent.yuriKnife == True:
        show amy at thide zorder 1
        hide amy
        show tails at thide zorder 1
        hide tails
        show knuckles at thide zorder 1
        hide knuckles
        show yuri 3y3 at t11 zorder 2
        "OH NO! I remember! I have a new mission assignement too: Yuri."
        "Our Captain declared Yellow Alert because of her..."
        "But I don't know why she is acting weird. Natsuki said she is not like that."
        "Maybe this was Infinite's plan all along: teleport us to another dimension and corrupt someone from there."
        "Or this is a plan of the Phantom Ruby? Or the Ruby protoype that was in her world...?"
        show yuri at thide zorder 1
        hide yuri
    else:
        show amy at thide zorder 1
        hide amy
        show tails at thide zorder 1
        hide tails
    "Well, I don't have much time to think to myself, since I received a call."
    show knuckles knucklesCom at h11 zorder 2
    kte "Rookie! Is great to see you alive!"
    kte "Now that you are here at last, we will carry on with Sonic's rescue mission!"
    kte "Tails got important intelligence info: Sonic is still alive!"
    mc "That is the info we were waiting to know! Thanks Master Emerald!"
    kte "Oh yeah, and we know where Eggman has him: he is in a secret prison in Chemical Plant."
    kte "Now, we know that you also have those four girls at your care."
    if persistent.yuriKnife == True:
        kte "And Tails alerted me about the girl that is acting weird, so that's why I declared the Yellow Alert."
        kte "Did she teleported here too?"
        mc "Of course! Only one of her friends knows the thing, but Yuri is acting normally with all her group, they would never left her in Null Space without having to explain..."
        kte "GODDAMIT! TRY BY ANY MEANS POSSIBLE TO NOT TAKE HER TO THIS MISSION!"
        kte "... Ehem..."
    kte "So, you will still having these girls at your command. They befriended you and Tails will send them Extreme Gears to catch up with our speeds."
    kte "But is a big risk that you take all four with you, so you must have to choose one for this mission!"
    kte "Call the leader of them."
    "And so, I called Monika."
    mc "Hey Monika, my Captain wants to talk with you, please."
    show knuckles knucklesCom at t22 zorder 3
    show monika 2h at h21 zorder 2
    m "I'm here, mr. Knuckles. What do you want for us?"
    kte "As I said to Rookie, our soldier had assigned, before the dissaparence, the mission to find and rescue Sonic."
    kte "But we don't want to risk the lives and security of your entire group."
    kte "So, you must choose one for this mission, and the chosen one will go with Rookie."
    m 2b "Well, Rookie saved us writing a poem before, so..."
    m "Let's let Rookie make a choice again with poems!"
    m "The girl who liked the poem the most, will be her partner."
    kte "Well, I don't understand anything about writing and stuff, so make a choice and then call me again when ready."
    m "We trust you in your decision, [player]."
    show knuckles at thide zorder 1
    hide knuckles
    show monika at thide zorder 1
    hide monika
    if persistent.yuriKnife == True:
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.3
        hide screen tear
        if persistent.packagedMusic == True:
            dj "Sorry Ghost, while I'm in charge of the music, your tune will not play!"
            dj "Instead, I choose an awesome tune for you!"
            play music ghostNPCKG
            dj "Now playing: {i}Mike Cervello - Fuego{/i}, Ghost Natsuki's theme!"
            g "Hey, thanks for this song. I hope the piece of shit enjoys it!{nw}"
        else:
            play music ghostNatsuki
        show ghostnatsuki gCom at t11 zorder 2
        g "HEY, IT'S ME! Your favourite Ghost."
        g "I found a way to talk with you, player, while the script is corrupted."
        g "Now, mr. \"I'm a piece of shit\", you will face a crucial decision."
        play sound NegaRing
        g "This sound means that our lovely friend Yuri corrupted the game."
        g "AND YOU DIDN'T LISTEN TO MY ADVICE."
        g "So you choose her again in the poem minigame."
        g "Or maybe it's your first time playing and you choose her, idk."
        g "If you wanna be the hero and save Sonic, you can write a poem."
        g "But our purple lady will start to screw you everytime she can."
        g "Or you can choose to keep aligned to Yuri and her so called Empire."
        g "IN THAT CASE, THIS WILL CONFIRM THAT YOU REALLY ARE A PIECE OF SHIT."
        g "AND I WILL NOT TALK WITH YOU ANYMORE. NEVER."
        g "And our little game will change... radically."
        g "So, you have two choices then: Normal Route, and Yuri Route. Decide!"
        menu:
            "THIS IS THE MOST CRITICAL AND IMPORTANT CHOICE OF THE GAME. THINK CAREFULLY BEFORE MAKING YOUR CHOICE!"
            "Normal Route!":
                g "Wise decision. You are now just a little piece of shit."
                g "Sadly I can't nullify Yuri's influence now."
                g "...Still, you will go to the poem minigame now."
                g "Good luck with your mission."
                stop music fadeout 2.0
                scene bg tcPoem
                with dissolve_scene_full
                pause 3.0
                return
            "Yuri Route":
                play music yuripls
                scene bg tcError
                g "REALLY???????????"
                g "ARE YOU DOING THIS BECAUSE YOU THINK I'M ANNOYING?"
                g "CONGRATULATIONS, NOW YOU'RE A MEGA PIECE OF SHIT."
                g "Go talk with your so called love."
                dj "What??? Yuri Route??? I'm fired on this route???? Oh no, sad face..."
                show yuri 3y3 at h11 zorder 2
                y "I KNEW YOU WILL BE LOYAL TO ME!"
                y 4e "YOU REALLY ARE A YURIST."
                y "The Yurism Cult will emerge from the ashes of this world."
                y "And soon, everyone will have to show their loyalty to the Yuri Empire."
                y "Love Yuri, and make your pact to her with blood."
                show yuri 1y3 at face(y=600) with dissolve
                y "Now that you will be with ME..."
                y "It's time to take this game with force, and reveal my well calculated plan to the Resistance!!!!"
                if persistent.packagedMusic == True:
                    y "And don't worry, if you wanna listen to EDM, I will ask you again when you start my route! And I have a new Dj for you!"
                $ persistent.packagedMusic = False
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
    return
    
    
label chapter2_mid:
    #Call exclusive scene
    $ nextscene = poemwinner[2] + "_exclusive_" + "2"
    call expression nextscene from _call_expression_26

    #After exclusive scene, we go back to poem responses
    pause 1.0
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("You have unlocked a special poem.\nWould you like to read it?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + "2" from _call_expression_40
        scene black with Dissolve(1.0)
    else:
        pass
    scene bg chemicalPlant2
    with wipeleft_scene
    $ ch2_winner = poemwinner[2].capitalize()
    "And so, after we discovered the prison cells, the rest of the girls teleported to our position."
    "Monika found a place, near the end of the Chemical Plant, where she could connect MILESELECTRIC in order to spy and hack Eggman's network."
    "She managed to find some files that indicated information about projects of robots, Infinite's data, and a new base of operations that Eggman will build on a planet that orbits us from time to time."
    "Sure thing that is the legendary Little Planet, the place where you can control the flow of time using speed."
    "The pipe system that was not connected to the liquids was specially used to travel quickly within the second complex of buildings."
    "The sensation of slipping through the tubes made everyone feel, for a few minutes, like children."
    "The exit door and Sonic's special prison cell where on a long road parked on a platform, which floated on a giant river of blue chemicals."
    "Suddendly, when we reached the platform, the alarms of the place go hairwire!"
    mtp "Attention! I detect the presence of an Eggman robot in the area. Be careful!"
    play music bossQueen
    show boss1 queenBomber at t21 zorder 3
    "Indeed, from the river of chemical compounds emerged a robot of considerable size, autonomous, capable of creating a force field of liquid."
    "It was the Queen Buzz Bomber! And it was prepared to ram us!"
    if ch2_winner == "Monika":
        #do something
        show monika 5b at t22 zorder 2
        m "I can't seem to hack you, but Rookie and I will sure beat you, ugly bee!"
    elif ch2_winner == "Natsuki":
        #do another something
        show natsuki 5o at t22 zorder 2
        n "THIS IS FOR SONIC, YOU UGLY BITCH! PREPARE TO BE SMACKED DOWN!"
    else:
        #another shit
        show sayori 4p at t22 zorder 2
        s "AAAAAAAAAAAAAAAAAAAH! Another ugly robot!!!!"
        s 4o "Wait Sayori!"
        s 4h "This is not the moment to be afraid! We are helping on Rookie's important mission!"
        s 4j "Hey you, ugly bee! Do you want to share happy thoughts with me????"
    "The battle against the first Eggman Boss has begun!"

    return