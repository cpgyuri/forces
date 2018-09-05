#This is a copy of script.rpy from DDLC.
#Use this as a reference for DDLC's normal game flow.
#The version of script.rpy in the /game folder is better as a base for modding.
label start:

    # Set the ID of this playthrough
    $ anticheat = persistent.anticheat

    # We'll keep track of the chapter we're on for poem response logic and other stuff
    $ chapter = 0
    $ persistent.playthrough = 2

    #If they quit during a pause, we have to set _dismiss_pause to false again (I hate this hack)
    $ _dismiss_pause = config.developer

    # Each of the girls' names before the MC learns their name throughout ch0.
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    #    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    if flag == 1:
        $ persistent.yuriRoute = True
    else:
        $ persistent.yuriRoute = False

    if persistent.playthrough == 2:
        # Intro
        $ chapter = 0
        if persistent.yuriRoute:
            call yuriRoute1 from call_yuriRoute1
        else:
            #call YuriSong from _call_YuriSong
            #call testingMonikaRoom from _call_testingMonikaRoom
            call prologue from _call_prologue

            # Poem minigame 0
            if persistent.ghost_menu and not persistent.sayonika_unlocked:
                call poem(False)
            else:
                call poem

            # Day 1
            $ chapter = 1
            call chapter1 from _call_chapter1
            #call poemresponse_start
            #call ch1_end
            # Poem minigame 1
            call poem from _call_poem_2

            # Day 2
            $ chapter = 2
            call chapter2_start from _call_chapter2_start
            # Poem minigame 2
            call poem from _call_poem_6

            call chapter2_mid from _call_chapter2_mid
            #call MonikaSong from _call_MonikaSong
            #call DEMO from _call_DEMO
            #call poemresponse_start
            #call ch2_end

            # Day 3
            $ chapter = 3
            call chapter3 from _call_chapter3

            call chapter3_mid from _call_chapter3_mid
            #call DEMO from _call_DEMO
            #call poemresponse_start from _call_poemresponse_start
            #call ch3_end from _call_ch3_end
            # Poem minigame 3
            #call poem from _call_poem_2
            if chapter3decision == "FB":
                call chapter4FB from _call_chapter4FB
            else:
                call chapter4PG from _call_chapter4PG

            call chapter4 from _call_chapter4
            # Poem minigame 3
            call poem
            $ chapter = 4
            call chapter4_mid from _call_chapter4_mid

            #python:
            #    try: renpy.file(config.basedir + "/hxppy thxughts.png")
            #    except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
            $ chapter = 5
            call chapter5start from _call_chapter5start
        
            $ chapter = 6
            call chapter6start from _call_chapter6start

            #call endgame from _call_endgame

        return

    elif persistent.playthrough == 1:
        $ chapter = 0
        call ch10_main from _call_ch10_main
        jump playthrough2


    elif persistent.playthrough == 0:
        # Intro
        $ chapter = 0
        call ch20_main from _call_ch20_main

        label playthrough2:

            # Poem minigame 1
            call poem from _call_poem_3
            python:
                try: renpy.file(config.basedir + "/CAN YOU HEAR ME.txt")
                except: open(config.basedir + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())

            # Day 1
            $ chapter = 1
            call ch21_main from _call_ch21_main
            call poemresponse_start from _call_poemresponse_start_1
            call ch21_end from _call_ch21_end

            # Poem minigame 2
            call poem(False) from _call_poem_4
            python:
                try: renpy.file(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
                except: open(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())

            # Day 2
            $ chapter = 2
            call ch22_main from _call_ch22_main
            call poemresponse_start from _call_poemresponse_start_2
            call ch22_end from _call_ch22_end

            # Poem minigame 3
            call poem(False) from _call_poem_5

            # Day 3
            $ chapter = 3
            call ch23_main from _call_ch23_main
            if y_appeal >= 3:
                call poemresponse_start2 from _call_poemresponse_start2
            else:
                call poemresponse_start from _call_poemresponse_start_3

            if persistent.demo:
                stop music fadeout 2.0
                scene black with dissolve_cg
                "End of demo"
                return

            call ch23_end from _call_ch23_end

            return

    elif persistent.playthrough == 3:
        jump ch30_main

    elif persistent.playthrough == 4:

        $ chapter = 0
        call ch40_main from _call_ch40_main
        jump credits

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
