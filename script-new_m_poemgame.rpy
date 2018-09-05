#This code was made by jadebenn
#You must credit me in your mod if you use this code!

image m_sticker smile:
    "m_sticker"
    pause 0.1
    xoffset monikaOffset xzoom monikaZoom
    "gui/poemgame/m_sticker_2.png"

image s_sticker smile:
    "s_sticker"
    pause 0.1
    xoffset sayoriOffset xzoom sayoriZoom
    "gui/poemgame/s_sticker_2.png"
    
image y_sticker smile:
    "y_sticker"
    pause 0.1
    xoffset yuriOffset xzoom yuriZoom
    "gui/poemgame/y_sticker_2.png"
    
image n_sticker smile:
    "n_sticker"
    pause 0.1
    xoffset natsukiOffset xzoom natsukiZoom
    "gui/poemgame/n_sticker_2.png"

image soraka_sticker:
    "mod_assets/poemgame/Chibi_EliteKrAZyFan_Stand.png"
    xoffset sorakaOffset xzoom sorakaZoom
    block:
        function randomPauseSoraka
        parallel:
            sticker_move_n
        parallel:
            function randomMoveSoraka
        repeat

image soraka_sticker hop:
    "mod_assets/poemgame/Chibi_EliteKrAZyFan_Excited.png"
    xoffset sorakaOffset xzoom sorakaZoom
    hyperbouncySayori_hop
    xoffset 0 xzoom 1
    "soraka_sticker"

image soraka_sticker smile:
    "soraka_sticker"
    pause 0.1
    xoffset sorakaOffset xzoom sorakaZoom
    "mod_assets/poemgame/Chibi_EliteKrAZyFan_Excited.png"

image s_sticker_glitch:
    "mod_assets/poemgame/s_sticker_glitch.png"
    xoffset sayoriOffset xzoom sayoriZoom
    block:
        function randomPauseSayori
        parallel:
            sticker_move_n
        parallel:
            function randomMoveSayori
        repeat

image n_sticker_glitch:
    "mod_assets/poemgame/n_sticker_glitch_1.png"
    xoffset natsukiOffset xzoom natsukiZoom
    block:
        function randomPauseNatsuki
        parallel:
            sticker_move_n
        parallel:
            function randomMoveNatsuki
        repeat

image y_sticker_glitch:
    "gui/poemgame/y_sticker_2g.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
             function randomMoveYuri
        repeat

image m_sticker_glitch:
    "mod_assets/poemgame/m_sticker_glitch.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat
    
init python:
    import random
    from datetime import datetime
    display_words = []
    poemgame_glitch = False
    played_baa = False

    import subprocess
    import os
    process_list = []
    if renpy.windows:
        try:
            process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
        except:
            pass
    
    #I might actually want to move this to definitions, this could be REALLY useful later
    class CooldownTimer:
        def __init__(self, cooldown):
            self.init_time = datetime.min
            self.cooldown = cooldown
        def start(self):
            self.init_time = datetime.now()
        def hasFinished(self):
            current_time = datetime.now()
            if self.init_time > current_time:
                self.init_time = current_time #If you somehow went back in time, we fix that.
            elapsed_time = current_time - self.init_time
            if elapsed_time.total_seconds() >= self.cooldown:
                return True
            else:
                return False

    # This class holds a word, and point values for each of the four heroines
    class NewPoemWord:
        def __init__(self, word, sPoint, nPoint, yPoint, mPoint, glitch=False):#mPoint
            self.word = word
            self.sPoint = sPoint
            self.nPoint = nPoint
            self.yPoint = yPoint
            self.mPoint = mPoint
            self.glitch = glitch

    # Building the word list
    full_new_wordlist = []
    with renpy.file('poemwords.txt') as wordfile:
        for line in wordfile:
            # Ignore lines beginning with '#' and empty lines
            line = line.strip()

            if line == '' or line[0] == '#': continue

            # File format: word,sPoint,nPoint,yPoint,mPoint
            x = line.split(',')
            full_new_wordlist.append(NewPoemWord(x[0], float(x[1]), float(x[2]), float(x[3]), float(x[4])))
                
    #This function draws the poemwords
    def draw_words(cTimer):
        ystart = 160
        pstring = str(progress)
        ui.text("Progress: " + pstring + "/" + str(numWords), style="poemgame_text_forces", xpos=470, ypos=80, color='#00ff00')
        for j in range(2):
            if j == 0: x = 460
            else: x = 690
            ui.vbox()
            for i in range(5):
                z = i + (j * 5)
                if not poemgame_glitch and not played_baa and progress < numWords and random.randint(1, 6) == 4:
                    word = NewPoemWord(glitchtext(10), 3, 3, 3, 3, True) #This gives a chance for a random word in Act 2 to be the glitched word.
                    played_baa = True
                else:
                    word = random.choice(wordlist)
                    wordlist.remove(word)
                ui.textbutton(word.word, clicked=Function(select_doki, word, cTimer, _update_screens=False), hovered=Function(show_doki, word, cTimer, "smile"), unhovered=Function(show_doki, word, cTimer), text_style="poemgame_text_forces", xpos=x, ypos=i * 56 + ystart)
            ui.close()
        
    #This function shows the dokis
    def show_doki(t, cTimer, action = ""):
        if action == "hop" or cTimer.hasFinished():
            if not poemgame_glitch:
                if t.sPoint >= 3:
                    renpy.show("s_sticker " + action)
                if t.nPoint >= 3:
                    renpy.show("n_sticker " + action)
                if t.yPoint >= 3:
                    if t.word == "YURI EMPIRE":
                        renpy.show("y_sticker hopg")
                    else:
                        renpy.show("y_sticker " + action)
                if t.mPoint >= 3:
                    renpy.show("m_sticker " + action)
            else:
                renpy.show("soraka_sticker " + action)        
    
    #This function selects the doki and the correct word and saves the score change
    def select_doki(t, cTimer, action = "hop"):
        if not poemgame_glitch:
            if t.word == "C.Emerald":
                renpy.play("mod_assets/Emerald.ogg")
            elif t.word == "Sonic":
                renpy.play("mod_assets/Ring.ogg")
            elif t.word == "Tails":
                renpy.play("mod_assets/Ring.ogg")
            elif t.word == "Knuckles":
                renpy.play("mod_assets/Ring.ogg")
            elif t.word == "Amy":
                renpy.play("mod_assets/Ring.ogg")
            elif t.word == "Shadow":
                renpy.play("mod_assets/Ring.ogg")
            elif t.word == "Rookie":
                renpy.play("mod_assets/Ring.ogg")
            elif t.word == "Avatar":
                renpy.play("mod_assets/Ring.ogg")
            elif t.word == "ring":
                renpy.play("mod_assets/Ring.ogg")
            elif t.word == "YURI EMPIRE":
                renpy.play("mod_assets/NegaRing.ogg")
            else:
                renpy.play(gui.activate_sound)
        else:
            if t.word == "C.Emerald":
                renpy.play("mod_assets/Emerald.ogg")
            elif t.word == "YURI EMPIRE":
                renpy.play("mod_assets/NegaRing.ogg")
            else:
                renpy.play("sfx/giggle.ogg")
        store.sPointTotal += t.sPoint
        store.nPointTotal += t.nPoint
        store.yPointTotal += t.yPoint
        store.mPointTotal += t.mPoint
        store.progress += 1
        #Added stuff that is important to only do on selection
        show_doki(t, cTimer, action) #Show the animation
        cTimer.start() #Start cooldown timer
        if not poemgame_glitch:
            if t.glitch: #Make stuff go to SONIC.EXE world if the game glitches
                poemgame_glitch = True
                renpy.play("mod_assets/poemgame/weirdscream.ogg")
                renpy.music.play("mod_assets/poemgame/MIKEXE_Executionv5.ogg")
                renpy.scene()
                renpy.show("rookiePoemMIK")
                renpy.show("s_sticker_glitch", at_list=[sticker_leftest])
                renpy.show("n_sticker_glitch", at_list=[sticker_lmid])
                renpy.show("m_sticker_glitch", at_list=[sticker_rightest])
                renpy.show("y_sticker_glitch", at_list=[sticker_rmid])
                renpy.show("soraka_sticker", at_list=[sticker_m_glitch_2])
        return ui.returns() #End the UI interaction
      
label new_m_poem(transition=True):
    stop music fadeout 2.0
    $ eurodance = renpy.random.randint(0,3)
    if persistent.playthrough == 3:
        scene bg notebook-glitch
    else:
        if persistent.yuriKnife == True:
            scene bg rookiePoemYuri
        else:
            if eurodance == 0:
                scene bg rookiePoemSonic
            elif eurodance == 1:
                scene bg rookiePoemTails
            elif eurodance == 2:
                scene bg rookiePoemShadow
            else:
                scene bg rookiePoemAmy
    show screen quick_menu
    if transition:
        with dissolve_scene_full
    if persistent.playthrough == 3:
        play music ghostmenu
    else:
        if persistent.packagedMusic == True:
            play music rPoemPCKG
        else:
            play music rPoem
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    if persistent.playthrough == 0 and chapter == 0:
        if persistent.packagedMusic == True:
            show honey djHoney at l31 zorder 5
            dj "Now playing: {i}SKRILLEX - Rock N' Roll (Will Take You To The Mountain){/i}! Let's make some rhythmic poems!"
            show honey at lhide zorder 1
            hide honey
            if persistent.yuriKnife == True:
                show yuri yuriCom1 at l11 zorder 5
                y "Welcome to MilesPOEM.exe!"
                y "Pick words you think one of us will like! SPECIALLY ME!"
                y "The girl which likes your poem the most will help you in the next Mission! And the Chibis will give you hints for the words!"
                y "I HOPE YOU LOVE THE BACKGROUND AND POEM I DID FOR YOU!"
                y yuriCom2 "And please, do me a favour: When you are done with your poem, GIVE ME YOUR PEN!!!!"
                show yuri at lhide zorder 1
                hide yuri
            else:
                show tails tailsCom at l11 zorder 5
                mtp "Welcome to MilesPOEM.exe!"
                mtp "Pick words you think one of these ladies will like!"
                mtp "The girl which likes your poem the most\nwill help you in the next Mission!"
                mtp "Good luck, Rookie!"
                show tails at lhide zorder 1
                hide tails
        else:
            #call screen dialog("User online: Rookie!\nWelcome to MilesPOEM.exe!\n\nPick words you think one of these ladies will like!\n(The Chibis will give you hints)\nThe girl which likes your poem the most\nwill help you in the next Mission!\n\n{i}If you see C.Emerald on the list{/i},\n{i}make sure to click it for a bonus!{/i}", ok_action=Return())
            if persistent.yuriKnife == True:
                show yuri yuriCom1 at l11 zorder 5
                y "Welcome to MilesPOEM.exe!"
                y "Pick words you think one of us will like! SPECIALLY ME!"
                y "The girl which likes your poem the most will help you in the next Mission! And the Chibis will give you hints for the words!"
                y "I HOPE YOU LOVE THE BACKGROUND AND POEM I DID FOR YOU!"
                y yuriCom2 "And please, do me a favour: When you are done with your poem, GIVE ME YOUR PEN!!!!"
                show yuri at lhide zorder 1
                hide yuri
            else:
                show tails tailsCom at l11 zorder 5
                mtp "Welcome to MilesPOEM.exe!"
                mtp "Pick words you think one of these ladies will like!"
                mtp "The girl which likes your poem the most\nwill help you in the next Mission!"
                mtp "Good luck, Rookie!"
                show tails at lhide zorder 1
                hide tails
        mtp "Don't forget to click on the word {i}C.Emerald{/i} for a bonus!"
    if persistent.playthrough == 0 and chapter == 3:
        "Note for this Poem Minigame! Since Sayori is out of comission and Yuri is fully villain now..."
        "Selecting Sayori's words will favour Ghost Natsuki!"
        "Selecting Natsuki's words will favour Natsuki!"
        "Monika's words will still favour Monika, for all the Just Monika's here!"
        "Selecting Yuri's words will have a surprise portal also!"
    show s_sticker at sticker_leftest
    show n_sticker at sticker_lmid
    show y_sticker at sticker_rmid
    show m_sticker at sticker_rightest
    window hide
    python:
        progress = 1
        numWords = 20
        sPointTotal = 0
        nPointTotal = 0
        yPointTotal = 0
        mPointTotal = 0 #added Monika!
        
        #Wordlist
        wordlist = list(full_new_wordlist)

        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sorakaTime = renpy.random.random() * 4 + 4
        sayoriPos = renpy.random.randint(-1,1)
        natsukiPos = renpy.random.randint(-1,1)
        yuriPos = renpy.random.randint(-1,1)
        monikaPos = renpy.random.randint(-1,1)
        sorakaPos = renpy.random.randint(-1,1)
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sorakaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
        sorakaZoom = 1

        # Main loop for drawing and selecting words
        hopTimer = CooldownTimer(0.72)
        while True:
            draw_words(hopTimer)
            ui.interact() #Begin a UI interaction
            if progress > numWords:
                break
                
        # Logic for taking point totals and assigning poem appeal, scene order, etc.
        unsorted_pointlist = {"sayori": sPointTotal, "natsuki": nPointTotal, "yuri": yPointTotal, "monika": mPointTotal}
        pointlist = sorted(unsorted_pointlist, key=unsorted_pointlist.get)
        
        # Set poemwinner to the highest scorer and to the chracter variable  
        poemwinner[chapter] = pointlist[-1]
        character = poemwinner[chapter]

        # Add appeal point based on poem winner
        exec(poemwinner[chapter][0] + "_appeal += 1")

        # Set poemappeal
        if sPointTotal < POEM_DISLIKE_THRESHOLD: s_poemappeal[chapter] = -1
        elif sPointTotal > POEM_LIKE_THRESHOLD: s_poemappeal[chapter] = 1
        if nPointTotal < POEM_DISLIKE_THRESHOLD: n_poemappeal[chapter] = -1
        elif nPointTotal > POEM_LIKE_THRESHOLD: n_poemappeal[chapter] = 1
        if yPointTotal < POEM_DISLIKE_THRESHOLD: y_poemappeal[chapter] = -1
        elif yPointTotal > POEM_LIKE_THRESHOLD: y_poemappeal[chapter] = 1
        if mPointTotal < POEM_DISLIKE_THRESHOLD: m_poemappeal[chapter] = -1
        elif mPointTotal > POEM_LIKE_THRESHOLD: m_poemappeal[chapter] = 1

        # Poem winner always has appeal 1 (loves poem)
        exec(poemwinner[chapter][0] + "_poemappeal[chapter] = 1")

    # #1/6 chance that we'll see creepy Happy Thoughts pic after the game in the game
    if persistent.playthrough == 0 and persistent.seen_eyes == None and poemwinner[chapter] == "sayori":
        $ seen_eyes_this_chapter = True
        $ quick_menu = False
        play sound "sfx/eyes.ogg"
        $ persistent.seen_eyes = True
        stop music
        scene black with None
        show bg eyes_move
        pause 1.2
        hide bg eyes_move
        show bg eyes_move
        pause 1.2
        hide bg eyes_move
        show bg eyes_move
        pause 1.2
        hide bg eyes with None
        $ quick_menu = True
    
    $ config.allow_skipping = True
    $ allow_skipping = True
    stop music fadeout 2.0
    if poemgame_glitch == True:
        show black 
        show gfm rexe11 at h11 zorder 6
        show wings wingRed at h11 behind gfm
        $ style.say_dialogue = style.edited_mik
        mik2 "Hello."
        mik2 "Good to see you."
        mik2 "I hope you enjoy your funny adventure with your new friends."
        mik2 "Ehehe~"
        mik2 "Until later, moron!"
        $ style.say_dialogue = style.normal
    show white as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0
    return

transform sticker_leftest:
    xcenter 60 yalign 0.9 subpixel True
    
transform sticker_lmid:
    xcenter 160 yalign 0.9 subpixel True

transform sticker_rmid:
    xcenter 260 yalign 0.9 subpixel True

transform sticker_rightest:
    xcenter 360 yalign 0.9 subpixel True

transform sticker_m_glitch_2:
    xcenter 560 yalign 0.9 subpixel True

transform hyperbouncySayori_hop:
    easein_quad .10 yoffset -320
    easeout_quad .10 yoffset 0
    easein_quad .10 yoffset -320
    easeout_quad .10 yoffset 0
    easein_quad .10 yoffset -320
    easeout_quad .10 yoffset 0
    easein_quad .10 yoffset -320
    easeout_quad .10 yoffset 0

