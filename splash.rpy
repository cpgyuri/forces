#This is a copy of splash.rpy from DDLC.
#Use this as a reference for DDLC's normal game flow.
#The version of splash.rpy in the /game folder is better as a base for modding.

init python:
    menu_trans_time = 1
    splash_message_default = "I would highly advise that you silence yourself\nbefore I boil you in your own blood."
    splash_messages = [
    "You know when the moment comes\nTo be strong, to RESISTANCE\nAnd that is what\nWe're lead to believe.",
    "No copyright law in the universe is going to stop me!",
    "I won't let him down! I WON'T GIVE UP!",
    "We're fighting to get our world back now.\nDon't stop, don't look back!\nJust focus on the task ahead no matter what!\nLet's do this, everyone!!!",
    "I never fail my mission.",
    "You have to learn how to fake your confidence.",
    "I want breakfast.",
    "You really need to...beat...the crap out of it!",
    "The Resistance will yield to the Phantom Ruby's power.\n\nAll will submit.",
    "The world will be nothing but ashes,\nfrom which a glorious Eggman Empire will rise!",
    "Touching myself all night with your bloody stylus pen.",
    "I will pull your skin open\nand savour the taste of your defeat.\nI will crawl inside you\nand spend the eternity in my own world.",
    "Can you hear them? They're trying to tell you something.",
    "Only you can hear me, summoner.\nWhat masterpiece shall we play today?",
    "Proudly supported by the angelic gal, Alice Angel!",
    "All the other kids with the pumped up kicks\nYou'd better run, better run, out run my gun\nAll the other kids with the pumped up kicks\nYou'd better run, better run, faster than my bulli.",
    "https://discord.gg/a5rRbCM"
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

# image menu_bg:
#     topleft
#     #"gui/menu_bg.png"
#     "mod_assets/menu_bg.png"
#     #menu_bg_move

# image menu_bg_ghost:
#     topleft
#     #"gui/menu_bg.png"
#     "mod_assets/menu_bg_ghost.png"
#     #menu_bg_move

image number1crate = "mod_assets/number1crate.png"

image menu_bg:
    pause 2.0
    topleft
    "mod_assets/menu_bg_ddf.png"
    menu_bg_move

image menu_bg2:
    pause 2.0
    pause 3.625
    topleft
    "mod_assets/menu_bg_ddf.png"
    menu_bg_loop2

image menu_bg_yuri:
    pause 2.0
    topleft
    "mod_assets/menu_bg_justyuri.png"
    menu_bg_move

image menu_bg2_yuri:
    pause 2.0
    pause 3.625
    topleft
    "mod_assets/menu_bg_justyuri.png"
    menu_bg_loop2

image menu_bg_ghost:
    pause 2.0
    topleft
    "mod_assets/menu_bg_ddf_ghost.png"
    menu_bg_move

image menu_bg_ghost2:
    pause 2.0
    pause 3.625
    topleft
    "mod_assets/menu_bg_ddf_ghost.png"
    menu_bg_loop2

image game_menu_bg:
    topleft
    #"gui/menu_bg.png"
    "mod_assets/menu_bg.png"
    #menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_n2:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_y2:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s2:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_y_ghost2:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_m_ghost2:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_n_ghost2:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_art_y_red:
    subpixel True
    "mod_assets/menu_art_y2old.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_red:
    subpixel True
    "mod_assets/menu_art_n2old.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_m_red:
    subpixel True
    "mod_assets/menu_art_m2old.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_nav:
    "mod_assets/main_menu.png"
    menu_nav_move

image menu_red:
    "mod_assets/game_menu2.png"

image menu_logo:
    #"gui/logo.png"
    "mod_assets/logo.png"
    subpixel True
    xcenter 640#240
    ycenter 360#120
    zoom 0.85#0.60
    menu_logo_move

image menu_logoYuriKnife:
    #"gui/logo.png"
    "mod_assets/logoYuriKnife.png"
    subpixel True
    xcenter 640#240
    ycenter 360#120
    zoom 0.85#0.60
    menu_logo_move

image menu_logo_ghost:
    "mod_assets/logo1.png"
    subpixel True
    xcenter 640
    ycenter 360
    zoom 0.85
    glitchloop

image menu_logo_edmsession:
    #"gui/logo.png"
    "mod_assets/EDMSessionRevamped/logo_dokiNation.png"
    subpixel True
    xcenter 640#240
    ycenter 360#120
    zoom 0.85#0.60
    menu_logo_move

image menu_logo_edmsessionY:
    #"gui/logo.png"
    "mod_assets/EDMSessionRevamped/logo_dokiNationY.png"
    subpixel True
    xcenter 640#240
    ycenter 360#120
    zoom 0.85#0.60
    menu_logo_move

image menu_insanity:
    topleft
    "mod_assets/insanity_01.png"

image menu_insanity_02:
    topleft
    "mod_assets/insanity_02.png"
    glitchloop2

image menu_particles:
    2.481
    xpos 640#224
    ypos 360#104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=20, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

# transform menu_bg_move:
#     subpixel True
#     topleft
#     parallel:
#         xoffset 0 yoffset 0
#         linear 3.0 xoffset -200 yoffset -200
#         repeat
#     parallel:
#         ypos 0
#         time 0.65
#         ease_cubic 2.5 ypos -500

# transform menu_bg_loop:
#     subpixel True
#     topleft
#     parallel:
#         xoffset 0 yoffset 0
#         linear 3.0 xoffset -200 yoffset -200
#         repeat

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 8.0 xoffset 0 yoffset -1320
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos 0

transform menu_bg_loop2:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 720
        linear 8.0 xoffset 0 yoffset -600
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos 0

transform menu_logo_move:
    subpixel True
    yoffset -750#-300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

transform glitchloop:
    "mod_assets/logo2.png"
    subpixel True
    xcenter 640 ycenter 360
    pause 0.10
    "mod_assets/logo3.png"
    subpixel True
    xcenter 640 ycenter 360
    pause 0.10
    "mod_assets/logo4.png"
    subpixel True
    xcenter 640 ycenter 360
    pause 0.10
    "mod_assets/logo1.png"
    subpixel True
    xcenter 640 ycenter 360
    pause 2
    "mod_assets/logo2.png"
    subpixel True
    xcenter 640 ycenter 360
    pause 0.10
    "mod_assets/logo3.png"
    subpixel True
    xcenter 640 ycenter 360
    pause 0.10
    "mod_assets/logo4.png"
    subpixel True
    xcenter 640 ycenter 360
    pause 0.10
    "mod_assets/logoYuriKnife.png"
    subpixel True
    xcenter 640 ycenter 360
    pause 2
    #jump glitchloop
    repeat

transform glitchloop2:
    "mod_assets/insanity_02.png"
    subpixel True
    pause 1
    "mod_assets/insanity_03.png"
    subpixel True
    pause 1
    #jump glitchloop
    repeat

# image intro:
#     truecenter
#     "white"
#     0.5
#     "bg/splash.png" with Dissolve(0.5, alpha=True)
#     2.5
#     "white" with Dissolve(0.5, alpha=True)
#     0.5

# image intro2:
#     truecenter
#     "white"
#     0.5
#     "bg/splash-glitch2.png" with Dissolve(0.5, alpha=True)
#     2.5
#     "white" with Dissolve(0.5, alpha=True)
#     0.5

image intro:
    truecenter
    "white"
    0.5
    "mod_assets/splash_monika.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image intro2:
    truecenter
    "white"
    0.5
    "mod_assets/splash_monika.png" with Dissolve(0.5, alpha=True)
    0.5
    "mod_assets/splash-glitch2.png"
    0.5
    "mod_assets/splash-glitch.png"
    0.5
    "mod_assets/splash-white.png"
    1.0
    "white" with Dissolve(0.5, alpha=True)
    0.5

image intro_yuri:
    truecenter
    "white"
    0.5
    "mod_assets/splash_yuri.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image introJumpscare:
    truecenter
    "black"
    0.25
    "red"
    0.25
    "black"
    0.25
    "red"
    0.25
    "black"
    0.25
    "red"
    0.25
    "black"
    0.25
    "red"
    0.25
    "black"
    0.25
    "red"
    0.25
    "black"
    0.25
    "red"
    0.25
    "black"
    0.25
    "red"
    0.25
    "black"
    0.25
    "red"
    0.25
    "black"
    0.25
    "red"
    0.25
    "black"
    0.25
    "red"
    0.25
    "black"
    0.25
    "red"
    0.25
    "black"
    0.25
    "red"
    0.25
    "black"
    0.25
    "red"
    0.25
    "black"
    0.25
    "red"
    0.25
    "black"
    0.25
    "red"
    0.25
    "black"
    0.25
    "red"
    0.25
    "white" with Dissolve(0.5, alpha=True)
    0.25

image introSega:
    truecenter
    "white"
    0.5
    "mod_assets/segalogo.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image introSegaGhost:
    truecenter
    "white"
    0.5
    "mod_assets/segalogoGhost.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image introSegaGhost_yuri:
    truecenter
    "white"
    0.5
    "mod_assets/segalogoGhost_yuri.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image introSegaGhost_sayonika:
    truecenter
    "white"
    0.5
    "mod_assets/segalogoGhost_sayonika.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image introSega_yuri:
    truecenter
    "white"
    0.5
    "mod_assets/segalogo_yuri.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image introSega_yuriKnife:
    truecenter
    "white"
    0.5
    "mod_assets/segalogo_yuriKnife.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "mod_assets/warning.png" #"bg/warning.png"
image tos2 = "mod_assets/warning2.png" #"bg/warning2.png"
image tos2b = "mod_assets/warning2b.png" #"bg/warning2.png"

# Make sure character files are in place
init python:
    #if not persistent.do_not_delete:
    s_kill_early = None
    y_kill_early = None
    jumpscare_flag = None
    if persistent.playthrough == 2:
        try: renpy.file("../characters/yuri.chr")
        except: y_kill_early = True
        try: renpy.file("../mod_assets/EDMSessionRevamped/angelIslandPCKG.ogg")
        except: persistent.edmfiles_flag = True
    if not y_kill_early:
        if persistent.playthrough <= 2:
            try: renpy.file("../characters/monika.chr")
            except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
        if persistent.playthrough <= 2 or persistent.playthrough == 4:
            try: renpy.file("../characters/natsuki.chr")
            except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
            try: renpy.file("../characters/yuri.chr")
            except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
        if persistent.sayori_kill == False:#persistent.playthrough == 0 or persistent.playthrough == 4:
            try: renpy.file("../characters/sayori.chr")
            except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())


label splashscreen:
    default persistent.first_run = False
    # Logic for detecting if the game has been reinstalled
    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass
    if not firstrun: #renpy.loadable("10"):
        if persistent.first_run:# and not persistent.do_not_delete:
            $ quick_menu = False
            scene bg mikEXEWorld
            menu:
                "A previous save file has been found. Would you like to delete your save data and start over?"
                "Yes, delete my existing data.":
                    if persistent.yuriKnife == True:
                        show ghostnatsuki gNatsu1 at h11 zorder 2
                        $ style.say_dialogue = style.edited
                        g "YAY! YOU FOLLOWED MY ADVICE! GOOD JOB!"
                        g "WE WILL RESET YURI AND THE GAME NOW."
                        g "EVERYTHING WILL BE OK."
                        g "DON'T MAKE ANOTHER MISTAKE AGAIN, YOU IDIOT."
                        show ghostnatsuki at thide zorder 1
                        hide ghostnatsuki
                        $ style.say_dialogue = style.normal
                    #$ style.say_dialogue = style.normal
                    "Deleting save data...{nw}"
                    ### You don't need to set everything to false.
                    ### renpy.loadsave.location.unlink_persistent() will reset everything
                    #$ persistent.genderMale = False
                    #$ persistent.yuriKnife = False
                    #$ persistent.sonicMania = False
                    #$ persistent.packagedMusic = False
                    #$ persistent.seenPrologue = False
                    #$ persistent.ringCount = 0
                    #$ persistent.emeraldCount = 0
                    #$ persistent.sayori_kill = False
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "No, continue where I left off.":
                    pass

        python:
            if not firstrun:
                with open(config.basedir + "/game/firstrun", "w") as f:
                    f.write("1")
            #filepath = renpy.file("firstrun").name
            #open(filepath, "a").close()

    if not persistent.first_run:
        $ quick_menu = False
        call oem_boot_screen
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        play music "mod_assets/EncoreMenu.ogg"
        pause 1.0
        call screen alert("Your MILESELECTRIC software has been tampered!", "AliceOS is restoring and running the last system restore point.", ok_action=Return(1))
        kte "For everyone here that is listening: this is Knuckles, the Captain of the Resistance, with some important info!"
        kte "This is a DDLC mod that is not affiliated with Team Salvato. It's designed to be played only after the official game has been completed."
        kte "If you still not play the original Doki Doki Literature Club, download a fresh copy at: http://ddlc.moe and play it!"
        kte "The Sonic the Hedgehog characters, names, backgrounds, sprites, music and sounds that are used on this mod are copyright of SEGA, Sonic Team, Christian Whitehead, Headcannon, Pagoda West Games and Hyperkinetic."
        kte "Attention new recruits!\nThis war is not suitable for: children under 13, soldiers with anxiety or depression, or those who will be easily disturbed by this war!"
        $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe", "camrecorder.exe", "eescreen.exe"]
        if persistent.edmfiles_flag:
            call screen alert("AliceOS", "The EDM Music files are missing. Skipping the EDM routines.", ok_action=Return(1))
            kte "Okay soldier, Tails is telling me that you don't seem to have the EDM music files installed."
            kte "Install the files first, and you will be able to make your choice in the Sound Test menu."
            $ persistent.packagedMusic = False
        elif list(set(process_list).intersection(stream_list)):
            show honey djHoney at l32 zorder 5
            $ dj_name = "DJ Sona"
            $ style.say_window = style.window_Sona
            call screen alert("Transmission software running on the background!", "Skipping the EDM routines while in transmission mode.", ok_action=Return(1))
            dj "Only you can hear me, summoner. Which masterpiece shall we play today?"
            dj "I'm DJ Sona from the world of Runeterra, and I was commisioned by the Resistance to streaming the EDM Session for today."
            dj "Since you are recording this mod for Youtube or streaming, I will lock the choice to the default music, so you don't get copyright strikes in your video."
            dj "If you kindly stop recording or streaming, I will let you make your choice in the Sound Test menu. Thanks for understanding."
            $ persistent.packagedMusic = False
            $ style.say_window = style.window
            show honey at lhide zorder 1
            hide honey
        else:
            menu:
                kte "Question time! Will you fight while listening to EDM music?"
                "Yes! Let's try it!":
                    $ persistent.packagedMusic = True
                    $ dj_name = "DJ Sona"
                    show honey djHoney at l32 zorder 5
                    $ style.say_window = style.window_Sona
                    dj "Only you can hear me, summoner. Which masterpiece shall we play today?"
                    dj "I'm DJ Sona from the world of Runeterra, and I was commisioned by the Resistance to streaming the EDM Session for today."
                    dj "If you change your mind while playing, you can change your choice in the Sound Test menu."
                    $ style.say_window = style.window
                    show honey at lhide zorder 1
                    hide honey
                "No.":
                    $ persistent.packagedMusic = False
                    kte "Okay, if you change your mind while playing, you can change your choice in the Sound Test menu."
        menu:
            kte "By playing this mod, you will join the Resistance and fight against the Eggman Empire! Also we need to know if you are a Man or a Woman."
            "I'm a Man, and I will join the Resistance!":
                $ persistent.genderMale = True
                pass
            "I'm a Woman, and I will join the Resistance!":
                $ persistent.genderMale = False
                pass
        $ persistent.first_run = True
        $ s_kill_early = True
        $ jumpscare_flag = True
        scene tos2
        with Dissolve(1.5)
        pause 3.0
        stop music fadeout 2.0
        show emerald phantomRuby at t11 zorder 6
        pause 0.1
        show white zorder 7:
            alpha 0.6
            linear 0.25 alpha 0.0
        scene tos2b
        show emerald phantomRuby at t11 zorder 6
        play sound ruby
        pause 1.5
        scene white
        with Dissolve(1.5)
        play sound "mod_assets/rubySound2.ogg"
        call screen alert("AliceOS System Restore", "AliceOS is restarting your MILESELECTRIC.", ok_action=Return(1))

    if not persistent.special_poems:
        python hide:
            #persistent.special_poems = [0,0,0]
            persistent.special_poems = [1,2,3,4,5,6,7]
            #a = range(1,12)
            #a = range(1,6)
            #for i in range(3):
                #b = renpy.random.choice(a)
                #persistent.special_poems[i] = b
                #a.remove(b)
            #for i in range(4):
                #b = renpy.random.choice(a)
                #persistent.special_poems[i] = b
                #a.remove(b)

    $ basedir = config.basedir.replace('\\', '/')

    #jump credits
    # Cases for final playthrough when we skip splash/menu (autoload)
    if persistent.autoload and not _restart:
        jump autoload


    # Start splash logic
    $ config.allow_skipping = False
    # Ghost menu
    if persistent.playthrough == 0 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
        show black
        $ config.main_menu_music = audio.ghostmenu
        $ persistent.seen_ghost_menu = True
        $ persistent.ghost_menu = True
        $ renpy.music.play(config.main_menu_music)
        pause 1.0
        show end with dissolve_cg
        pause 3.0
        $ config.allow_skipping = True
        return
    
    if y_kill_early:
        show black
        play music "<loop 0>mod_assets/pumpedUpMettatonsSlow.ogg"#"bgm/s_kill_early.ogg"
        $ pause(1.0)
        show end with dissolve_cg
        $ pause(3.0)
        scene white
        show expression "mod_assets/y_kill_early.png":#images/cg/s_kill_early.png":
            yalign -0.05
            xalign 0.25
            #dizzy(1.0, 4.0)
        show white as w2:
            choice:
                ease 0.25 alpha 0.1
            choice:
                ease 0.25 alpha 0.125
            choice:
                ease 0.25 alpha 0.15
            choice:
                ease 0.25 alpha 0.175
            choice:
                ease 0.25 alpha 0.2
            choice:
                ease 0.25 alpha 0.225
            choice:
                ease 0.25 alpha 0.25
            choice:
                ease 0.25 alpha 0.275
            choice:
                ease 0.25 alpha 0.3
            pass
            choice:
                pass
            choice:
                0.25
            choice:
                0.5
            choice:
                0.75
            repeat
        show noise:
            alpha 0.1
        with Dissolve(1.0)
        show expression Text("We've only just begun.\nI'll never let you leave.\nI'll never let you rest.\nNo matter how many times they try to revive you first!\nI'LL NEVER. LET YOU. LEAVE.", style="yuri_text"):
            xalign 0.25#0.8
            yalign 0.1#0.5
            alpha 0.0
            10
            linear 60 alpha 0.5
        pause
        $ renpy.quit()
    
    if s_kill_early:
        call oem_boot_screen
        scene white
        pause 0.5
        scene bg angelIsland_beach
        with dissolve_scene_full
        $ SystemUIServer.send_temporary_notification("Restoring from Backup", "AliceOS is restoring and playing the backup file.", action=Return(0))
        show sonic sonic00 at t42
        show tails tails01 at t41
        show amy amy03 at t43
        show knuckles knuckles05 at t44
        if persistent.packagedMusic == True:
            play music aizPCKG
            show honey djHoney at l31 zorder 5
            $ forces.ask_app_permissions()
            $ forces.edmsession_music("Charly Black - Party Animal")
            dj "Now playing: Charly Black - Party Animal. Enjoy the sweet surfing waves of Angel Island."
            dj "I will inform you about the song's names here too, in case you disabled the notifications!"
            show honey at lhide zorder 1
            hide honey
        else:
            play music aiz
        "WELCOME TO THIS SPECIAL EDITION OF THE ANNUAL EXTREME GEARS COMPETITION!"
        "THIS YEAR'S COMPETITION IS KINDLY SUPPORTED BY THE GENEROUS DONATION OF DR. IVO ROBOTNIK, A.K.A. DR. EGGMAN!"
        "FIRST THREE CONTESTANTS THAT END THIS MEGA RACE FOR ANGEL ISLAND WILL ENTER THE PODIUM, AND FIRST PLACE WILL RECEIVE THE SPECIAL CUP!"
        "RACERS, PREPARE YOURSELVES! GET READY AND APPROACH THE STARTING LINE!!!"
        "IT'S RAAAAAAAAAAAAAAAAACING TIIIIIIIIIIIIIIIIME!!!!!!"
        mtp "Oh boy! I'm eager to test the new additions of my Extreme Gear!"
        kte "Yeah, yeah. Just try to not destroy the sacred ruins of Marble Garden or my Sanctuary, everyone."
        kte "If you do that, maybe I can let you be in the second place."
        amyR "This time you will eat the dust and savour the defeat, Sonic." 
        amyR "I practiced a lot, and everyone of us is more confident in our skills!"
        sth "I wanna see you trying it, Amy!"
        sth "Tails, Knuckles, Amy, friends! May the best win the race!"
        sth "And obviously, the best is me, the fastest thing alive! Haha!"
        kte "I'm still suspicious about Egghead being the main sponsor of this event. I secured the Master Emerald in a secret place, just in case."
        mtp "And I have cameras that will do surveilance in Launch Base, so there's nothing to fear."
        mtp "C'mon guys! Just five minutes to go! Let's relax and enjoy this!"
        scene bg angelIsland_jungle
        with dissolve_scene_full
        show eggman eggman00 at t21
        show infinite infinite0 at t22
        inf "The plan is ready to start, master."
        egg "Excellent! EggRobo squad! Start digging in the given coordinates!"
        egg "Hopefully the distraction will attract the stupid rodent and their friends, so my secret weapon can remove them from the map!"
        egg "Operation: World Conquer begins! OH HOHOHOHOHOHOHOHO~!"
        scene bg angelIsland_beach
        with dissolve_scene_full
        stop music fadeout 2.0
        "{i}Earth shaking noises, rumble noises, digging noises and trembles.{/i}"
        show sonic sonic11 at t42
        show tails tails03 at t41
        show amy amy10 at t43
        show knuckles knuckles02 at t44
        if persistent.packagedMusic == True:
            play music eggRobosPCKG
        else:
            play music eggRobos
        mtp "What is that noise???"
        kte "I KNEW I COULDN'T TRUST EGGMAN! I'M SURE HE IS TRYING TO FIND THE MASTER EMERALD!!!"
        amyR "Why we can't enjoy peace and a friendly competition???"
        amyR "*Sigh* Let's help Knuckles in protecting his home and the Master Emerald, guys!"
        sth sonic07 "Egghead! It's time to stop your plans again!"
        sth "Let's do it to it, guys!"
        scene bg angelIsland_eggRobos
        with dissolve_scene_full
        show sonic sonic07 at t42
        show tails tails07 at t41
        show amy amy10 at t43
        show knuckles knuckles02 at t44
        mtp "SONIC! THOSE EGGROBOS ARE DIGGING SOMETHING FROM THE GROUND!"
        mtp "Wha~..."
        mtp "What are these weird lectures from the Miles Electric?"
        amyR "The robos extracted something!!!"
        play music rubyMusic
        show emerald phantomRuby at t11 zorder 6
        sth "What is this thing?"
        kte "Watch out! It's doing somethi...{nw}"
        play sound ruby
        scene bg angelIsland_eggRobosRuby
        with dissolve_scene_full
        show rubypink zorder 99:
            alpha 0.0
            easein 4.0 alpha 0.5 
        show sonic sonic09 at t42
        show tails tails03 at t41
        show amy amy08 at t43
        show knuckles knuckles04 at t44
        sth "What is happening???"
        mtp "I can't move!!!"
        amyR "Sonic! I'm so scared!!!"
        kte "YOU WILL PAY FOR THIS, EGGHEAD!!!"
        hide ruby
        show black
        play sound ruby
        stop music
        pause 3.0
        scene bg angelIsland_jungle
        show portal genesisportal at t11
        with dissolve_cg
        "Sonic and his friends were forcefully transported out of Angel Island..."
        "Some months later..."
        "Eggman conquered 99%% of the world with the help of Infinite and the Ruby."
        "Also, the mad doctor captured Sonic and sent him to one of his secret prisons."
        "The Ruby started to open special portals to gather resources for Eggman to help in the war."
        egg "This portal seems very interesting."
        egg "I can get a vast amount of resources from the world of this open portal, but first..."
        egg "I will use my systems to interfere with the heart of that world, and make my invasion way easier! Oh hohohoho!"
        $ consolehistory = []
        call updateconsole("EGGMAN SYSTEM ONLINE", "...")
        pause 0.5
        call updateconsole("Hacking portal", "DDLC set to persistent.act 2!")
        pause 0.5
        egg "Now is the time! Badniks! Eggpawns! Start the invasion! Steal of the resources of that world and expand the glorious Eggman Empire!"
        play sound ruby
        call hideconsole
        window hide
        $ s_kill_early = False
        pause 2.0
        call screen alert("AliceOS System Restore", "AliceOS is restarting your MILESELECTRIC.", ok_action=Return(1))
        # python:
        #     renpy.utter_restart()

    # Actual splash screen
    call oem_boot_screen
    show white
    $ persistent.ghost_menu = False
    if renpy.random.randint(0, 3) == 3:
        $ splash_message = splash_message_default
    else:
        $ splash_message = renpy.random.choice(splash_messages)
    if splash_message == "I would highly advise that you silence yourself\nbefore I boil you in your own blood.":
        $ config.main_menu_music = audio.specialMenu
        $ persistent.ghost_menu = True
        $ _window_subtitle = " NATSUKI IS COMING FOR YOU"
        if not persistent.sayonika_unlocked:
            show introSegaGhost_sayonika with Dissolve(0.5, alpha=True)
            play sound segaGhost_sayonika
            pause 2.5
            hide introSegaGhost_sayonika with Dissolve(0.5, alpha=True)
        elif persistent.yuriRoute == True:
            show introSegaGhost_yuri with Dissolve(0.5, alpha=True)
            play sound segaGhost
            pause 2.5
            hide introSegaGhost_yuri with Dissolve(0.5, alpha=True)
        else:
            show introSegaGhost with Dissolve(0.5, alpha=True)
            play sound segaGhost
            pause 3.0
            hide introSegaGhost with Dissolve(0.5, alpha=True)
        if jumpscare_flag == True:
            show black with Dissolve(0.5, alpha=True)
            $ _window_subtitle = " ?????"
            play sound "mod_assets/Frog05.ogg"
            pause 7.0 
            show introJumpscare
            $ _window_subtitle = " NUMBER 1 CRATE!!!! :D"
            show number1crate zorder 99
            play sound "mod_assets/boom2.ogg"
            pause 2.0
            hide number1crate with Dissolve(0.5, alpha=True)
            hide introJumpscare with Dissolve(0.5, alpha=True)
            hide black with Dissolve(0.5, alpha=True)
            show white
            $ _window_subtitle = " NATSUKI IS COMING FOR YOU"
            $ jumpscare_flag = False
        $ renpy.music.play(config.main_menu_music)
        show intro2 with Dissolve(0.5, alpha=True)
        pause 2.5
        hide intro2 with Dissolve(0.5, alpha=True)    
    else:
        if persistent.yuriRoute == True:
            $ config.main_menu_music = audio.forces
            show introSega_yuri with Dissolve(0.5, alpha=True)
            play sound sega
            pause 2.5
            hide introSega_yuri with Dissolve(0.5, alpha=True)
            if jumpscare_flag == True:
                show black with Dissolve(0.5, alpha=True)
                $ _window_subtitle = " ?????"
                play sound "mod_assets/Frog05.ogg"
                pause 7.0 
                show introJumpscare
                $ _window_subtitle = " NUMBER 1 CRATE!!!! :D"
                show number1crate zorder 99
                play sound "mod_assets/boom2.ogg"
                pause 2.0
                hide number1crate with Dissolve(0.5, alpha=True)
                hide introJumpscare with Dissolve(0.5, alpha=True)
                hide black with Dissolve(0.5, alpha=True)
                show white
                $ _window_subtitle = ""
                $ jumpscare_flag = False
            $ renpy.music.play(config.main_menu_music)
            show intro_yuri with Dissolve(0.5, alpha=True)
            pause 2.5
            hide intro_yuri with Dissolve(0.5, alpha=True)
        elif persistent.yuriKnife == True:
            $ config.main_menu_music = audio.forces
            show introSega_yuriKnife with Dissolve(0.5, alpha=True)
            play sound sega
            pause 2.5
            hide introSega_yuriKnife with Dissolve(0.5, alpha=True)
            if jumpscare_flag == True:
                show black with Dissolve(0.5, alpha=True)
                $ _window_subtitle = " ?????"
                play sound "mod_assets/Frog05.ogg"
                pause 7.0 
                show introJumpscare
                $ _window_subtitle = " NUMBER 1 CRATE!!!! :D"
                show number1crate zorder 99
                play sound "mod_assets/boom2.ogg"
                pause 2.0
                hide number1crate with Dissolve(0.5, alpha=True)
                hide introJumpscare with Dissolve(0.5, alpha=True)
                hide black with Dissolve(0.5, alpha=True)
                show white
                $ _window_subtitle = ""
                $ jumpscare_flag = False
            $ renpy.music.play(config.main_menu_music)
            show intro_yuri with Dissolve(0.5, alpha=True)
            pause 2.5
            hide intro_yuri with Dissolve(0.5, alpha=True)
        else:
            $ config.main_menu_music = audio.forces
            show introSega with Dissolve(0.5, alpha=True)
            play sound sega
            pause 2.5
            hide introSega with Dissolve(0.5, alpha=True)
            if jumpscare_flag == True:
                show black with Dissolve(0.5, alpha=True)
                $ _window_subtitle = " ?????"
                play sound "mod_assets/Frog05.ogg"
                pause 7.0 
                show introJumpscare
                $ _window_subtitle = " NUMBER 1 CRATE!!!! :D"
                show number1crate zorder 99
                play sound "mod_assets/boom2.ogg"
                pause 2.0
                hide number1crate with Dissolve(0.5, alpha=True)
                hide introJumpscare with Dissolve(0.5, alpha=True)
                hide black with Dissolve(0.5, alpha=True)
                show white
                $ _window_subtitle = ""
                $ jumpscare_flag = False
            $ renpy.music.play(config.main_menu_music)
            show intro with Dissolve(0.5, alpha=True)
            pause 2.5
            hide intro with Dissolve(0.5, alpha=True)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    return

label warningscreen:
    hide intro
    show warning
    pause 3.0

label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal
    # If we load during yuri_kill
    if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
        if persistent.yuri_kill >= 1380:
            $ persistent.yuri_kill = 1440
        elif persistent.yuri_kill >= 1180:
            $ persistent.yuri_kill = 1380
        elif persistent.yuri_kill >= 1120:
            $ persistent.yuri_kill = 1180
        elif persistent.yuri_kill >= 920:
            $ persistent.yuri_kill = 1120
        elif persistent.yuri_kill >= 720:
            $ persistent.yuri_kill = 920
        elif persistent.yuri_kill >= 660:
            $ persistent.yuri_kill = 720
        elif persistent.yuri_kill >= 460:
            $ persistent.yuri_kill = 660
        elif persistent.yuri_kill >= 260:
            $ persistent.yuri_kill = 460
        elif persistent.yuri_kill >= 200:
            $ persistent.yuri_kill = 260
        else:
            $ persistent.yuri_kill = 200
        jump expression persistent.autoload
    # If we load a save file from a different playthrough (impossible without cheating)
    elif anticheat != persistent.anticheat:
        stop music
        scene bg mikEXEWorld
        "The save file could not be loaded."
        "Are you trying to cheat?"
        $ m_name = "Monika"
        $ sth_name = "Sonic"
        show monika 1 at t21
        show sonic sonicEXE at t22
        if persistent.playername == "":
            m "What are you trying to do? Don't cause more harm!"
            sth "RESETING YOUR GAME!"
        else:
            m "What are you trying to do, [persistent.playername]? Don't cause more harm!"
            sth "FOUND YOU, [persistent.playername]! GOODBYE!"
        $ renpy.utter_restart()
    else:
        if persistent.playthrough == 2 and not persistent.first_load and not config.developer:
            $ persistent.first_load = True
            call screen dialog("Hint: You can use the \"Skip\" button to\nfast-forward through text you've already read.", ok_action=Return())
    return



label autoload:
    python:
        # Stuff that's normally done after splash
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()

        # Fix the game context (normally done when loading save file)
        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
        $ persistent.yuri_kill += 200

    # Pop the _splashscreen label which has _confirm_quit as False and other stuff
    $ renpy.pop_call()
    jump expression persistent.autoload

label autoload_yurikill:
    if persistent.yuri_kill >= 1380:
        $ persistent.yuri_kill = 1440
    elif persistent.yuri_kill >= 1180:
        $ persistent.yuri_kill = 1380
    elif persistent.yuri_kill >= 1120:
        $ persistent.yuri_kill = 1180
    elif persistent.yuri_kill >= 920:
        $ persistent.yuri_kill = 1120
    elif persistent.yuri_kill >= 720:
        $ persistent.yuri_kill = 920
    elif persistent.yuri_kill >= 660:
        $ persistent.yuri_kill = 720
    elif persistent.yuri_kill >= 460:
        $ persistent.yuri_kill = 660
    elif persistent.yuri_kill >= 260:
        $ persistent.yuri_kill = 460
    elif persistent.yuri_kill >= 200:
        $ persistent.yuri_kill = 260
    else:
        $ persistent.yuri_kill = 200
    jump expression persistent.autoload

label before_main_menu:
    if persistent.ghost_menu:
        $ config.main_menu_music = audio.specialMenu    
    else:
        $ config.main_menu_music = audio.forces
    return

label quit:
    if persistent.ghost_menu:
        stop music
        hide screen main_menu
        scene white
        play sound "mod_assets/fnaf6scream.ogg"
        show image "mod_assets/menu_art_n_ghost_forces.png":
            xpos -100 ypos -100 zoom 3.5
        pause 5
    return

