label chapter6start:
    scene bg club_day with wipeleft_scene
    show noise at noise_alpha zorder 100
    show vignette at vignetteflicker(-2.030) zorder 100
    play music t2
    $ m_name = "Just Monika"
    $ mc2_name = "Dense"
    $ s_name = "Dummy"
    $ sth_name = "Sanik"
    show monika 5 at t21 zorder 2
    m "MC!"
    m "You're the first one here."
    m "Thanks for being early!"
    show mc2 1 at t22 zorder 2
    mc2 "That's funny, I thought at least one of the other girls would be here by now."
    m 1d "I'm surprised you didn't bring Sayori with you."
    mc2 1h "Yeah, she overslept again... That dummy."
    mc2 "You'd think that on days this important, she'd try a little harder..."
    mc2 1g "{i}Wait! Remember what Sayori told me yesterday...{/i}"
    m 1k "Ahaha."
    m 4b "You should take a little responsibility for her, specially after your exchange with her yesterday..."
    stop music
    m "{i}You kind of left her hanging this morning, you know?{/i}"
    show monika 4a
    play music t2
    mc2 1o "Exchange...? Monika-- You know about that??"
    m 2a "Of course I do. I'm the club president, after all."
    mc2 1i "You don't know the full story at all, so..."
    stop music
    m 2j "I probably know a lot more than you think."
    play music t2
    m 5 "Hey, do you want to check out the pamphlets? They came out really nice!"
    mc2 1j "Oh yeah, they really did."
    mc2 "Something like this will definitely help people take the club more seriously."
    m 1a "Yeah, I thought so too!"
    mc2 1m "I recognize the poems of Natsuki and Yuri, and your poem looks good too, as always..."
    mc2 1f "What's this...?"
    call showpoem(poem_s6, music=False) from _call_showpoem_7
    mc2 "What is this...?\n{i}I got a pit in my stomach all of a sudden.{/i}"
    m 1d "What's wrong?"
    mc2 1p "This poem feels completely different from everything else Sayori's written!"
    mc2 "I-I changed my mind!"
    mc2 "I'm going to go get Sayori!!!"
    scene bg corridor with wipeleft
    show noise at noise_alpha zorder 100
    show vignette at vignetteflicker(-2.030) zorder 100
    stop music
    m "Don't strain yourself~"
    
    scene bg residential_day with wipeleft_scene
    show noise at noise_alpha zorder 100
    show vignette at vignetteflicker(-2.030) zorder 100
    play music t2
    show mc2 1o at t11 zorder 2
    mc2 "What was I thinking?"
    mc2 "I should have tried a little bit harder for Sayori."
    mc2 "It's not a big deal to at least wait for her, or help her wake up."
    mc2 "Even the simple gesture of walking her to school makes her really happy."
    mc2 "And I told her yesterday that things will be the same as they always have been."
    mc2 "That's all she needs, and what I want to give her."

    scene bg house with wipeleft
    show noise at noise_alpha zorder 100
    show vignette at vignetteflicker(-2.030) zorder 100
    mc2 "Sayori! Are you there???"
    mc2 "No answer..."
    mc2 "I'm going in!"
    scene black with wipeleft
    show noise at noise_alpha zorder 100
    show vignette at vignetteflicker(-2.030) zorder 100
    stop music
    mc2 "Sayori?"
    mc2 "She really is a heavy sleeper..."
    mc2 "I can't believe I ended waking you up in your own house, dummy..."
    mc2 "That really is something that a boyfriend would do, isn't it?"
    mc2 "Wake up, dummy..."
    mc2 "There's no response."
    mc2 "You really leave me no choice."
    mc2 "I gently open the door."
    mc2 "{cps=30}.......Sayo--{/cps}{nw}"
    window hide(None)
    window auto
    hide noise
    hide vignette
    play music td
    show s_kill_bg
    show s_kill_sonic at s_kill_start
    pause 4.0
    stop music
    play sound djstop
    python:
        try: sys.modules['renpy.error'].report_exception("Trollface!!!", False)
        except: pass
    pause 2.0

    play music t7
    show sayori 1p at t44 zorder 5
    show mc2 1h at t43 zorder 5
    mc2 "..."
    mc2 "What the hell, Sayori...? Seriously?"
    s 5a "Sorry, MC...!"
    sth "Can somebody release me from this stupid rope? Thank you!"
    show mc2 1j at t43 zorder 5
    show sayori 1r at t44 zorder 5
    s "Welcome to the conclusion of Doki Doki Forces!"
    mc2 "We hope you enjoy the last stop of this weird travel."
    sth "And now, can somebody release me?"
    show mc2 1n at t43 zorder 5
    show sayori 4l at t44 zorder 5
    show ghostnatsuki gNatsu1 at l41 zorder 5
    $ m_name = "Monika"
    $ mc2_name = "MC"
    $ s_name = "Metal-Sayori"
    $ sth_name = "Sonic"
    g "And that was the story of the Sayori suicide in another dimension!"


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

    