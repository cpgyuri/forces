#Commented to absurdity, blame Terra.
#
#Worth noting how the game gets here in the first place:
    #This script is called via "call poem" in script.rpy.
    #All of the Act 1 instances are done simply with "call poem".
    #Some of the Act 2 instances are done with "call poem (False)"
        #This is how we get the abrupt cut-in to the mini-game in Act 2.
#Images are defined after the main poem game loop.


init python: #This whole block runs when DDLC is started (as opposed to when the poem minigame is called)
    import random
    mp = MultiPersistent("waifuclub")

    # This class holds a word, and point values for each of the four heroines
    class PoemWord:
        def __init__(self, word, sPoint, nPoint, yPoint, mPoint, glitch=False):
            self.word = word
            self.sPoint = sPoint
            self.nPoint = nPoint
            self.yPoint = yPoint
            self.mPoint = mPoint
            self.glitch = glitch

    # Static variables for characters' poem appeal: Dislike, Neutral, Like
    POEM_DISLIKE_THRESHOLD = 29
    POEM_LIKE_THRESHOLD = 45

    # Building the word list
    full_wordlist = []
    with renpy.file('poemwords.txt') as wordfile:
        for line in wordfile:
            # Ignore lines beginning with '#' and empty lines
            line = line.strip()

            if line == '' or line[0] == '#': continue

            # File format: word,sPoint,nPoint,yPoint
            x = line.split(',')
            full_wordlist.append(PoemWord(x[0], float(x[1]), float(x[2]), float(x[3]), float(x[4])))

    seen_eyes_this_chapter = False
    sayoriTime = renpy.random.random() * 4 + 4
    natsukiTime = renpy.random.random() * 4 + 4
    yuriTime = renpy.random.random() * 4 + 4
    monikaTime = renpy.random.random() * 4 + 4
    mikexeTime = renpy.random.random() * 4 + 4
    sayoriPos = 0
    natsukiPos = 0
    yuriPos = 0
    monikaPos = 0
    mikexePos = 0
    sayoriOffset = 0
    natsukiOffset = 0
    yuriOffset = 0
    monikaOffset = 0
    mikexeOffset = 0
    sayoriZoom = 1
    natsukiZoom = 1
    yuriZoom = 1
    monikaZoom = 1
    mikexeZoom = 1
##################################################################################
#These functions define random pause lengths for each of the stickers' movements.
#renpy.random.random() returns a random floating point number between 0 and 1
#So the -Doki-Time variable for each is a random decimal ranging from 4 to 8.
#These are used in the image definitions.

    def randomPauseSayori(trans, st, at):
        if st > sayoriTime:
            global sayoriTime
            sayoriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseNatsuki(trans, st, at):
        if st > natsukiTime:
            global natsukiTime
            natsukiTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseYuri(trans, st, at):
        if st > yuriTime:
            global yuriTime
            yuriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseMonika(trans, st, at):
        if st > monikaTime:
            global monikaTime
            monikaTime = renpy.random.random() * 4 + 4
            return None
        return 0
    
    def randomPauseMikexe(trans, st, at):
        if st > mikexeTime:
            global mikexeTime
            mikexeTime = renpy.random.random() * 4 + 4
            return None
        return 0
##############These functions define random movements for the stickers.#######
    def randomMoveSayori(trans, st, at):
        global sayoriPos
        global sayoriOffset
        global sayoriZoom
        if st > .16:
            if sayoriPos > 0:
                sayoriPos = renpy.random.randint(-1,0)
            elif sayoriPos < 0:
                sayoriPos = renpy.random.randint(0,1)
            else:
                sayoriPos = renpy.random.randint(-1,1)
            if trans.xoffset * sayoriPos > 5: sayoriPos *= -1
            return None
        if sayoriPos > 0:
            trans.xzoom = -1
        elif sayoriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * sayoriPos
        sayoriOffset = trans.xoffset
        sayoriZoom = trans.xzoom
        return 0

    def randomMoveNatsuki(trans, st, at):
        global natsukiPos
        global natsukiOffset
        global natsukiZoom
        if st > .16:
            if natsukiPos > 0:
                natsukiPos = renpy.random.randint(-1,0)
            elif natsukiPos < 0:
                natsukiPos = renpy.random.randint(0,1)
            else:
                natsukiPos = renpy.random.randint(-1,1)
            if trans.xoffset * natsukiPos > 5: natsukiPos *= -1
            return None
        if natsukiPos > 0:
            trans.xzoom = -1
        elif natsukiPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * natsukiPos
        natsukiOffset = trans.xoffset
        natsukiZoom = trans.xzoom
        return 0

    def randomMoveYuri(trans, st, at):
        global yuriPos
        global yuriOffset
        global yuriZoom
        if st > .16:
            if yuriPos > 0:
                yuriPos = renpy.random.randint(-1,0)
            elif yuriPos < 0:
                yuriPos = renpy.random.randint(0,1)
            else:
                yuriPos = renpy.random.randint(-1,1)
            if trans.xoffset * yuriPos > 5: yuriPos *= -1
            return None
        if yuriPos > 0:
            trans.xzoom = -1
        elif yuriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * yuriPos
        yuriOffset = trans.xoffset
        yuriZoom = trans.xzoom
        return 0

    def randomMoveMonika(trans, st, at):
        global monikaPos
        global monikaOffset
        global monikaZoom
        if st > .16:
            if monikaPos > 0:
                monikaPos = renpy.random.randint(-1,0)
            elif monikaPos < 0:
                monikaPos = renpy.random.randint(0,1)
            else:
                monikaPos = renpy.random.randint(-1,1)
            if trans.xoffset * monikaPos > 5: monikaPos *= -1
            return None
        if monikaPos > 0:
            trans.xzoom = -1
        elif monikaPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * monikaPos
        monikaOffset = trans.xoffset
        monikaZoom = trans.xzoom
        return 0
    
    def randomMoveMikexe(trans, st, at):
        global mikexePos
        global mikexeOffset
        global mikexeZoom
        if st > .16:
            if mikexePos > 0:
                mikexePos = renpy.random.randint(-1,0)
            elif mikexePos < 0:
                mikexePos = renpy.random.randint(0,1)
            else:
                mikexePos = renpy.random.randint(-1,1)
            if trans.xoffset * mikexePos > 5: mikexePos *= -1
            return None
        if mikexePos > 0:
            trans.xzoom = -1
        elif mikexePos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * mikexePos
        mikexeOffset = trans.xoffset
        mikexeZoom = trans.xzoom
        return 0

##################################################################################


label poem(transition=True):
    stop music fadeout 2.0
    $ eurodance = renpy.random.randint(0,4)
    if persistent.playthrough == 3: #Takes us to the glitched notebook if we're in Just Monika Mode.
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
                scene bg rookiePoemKnuckles
            elif eurodance == 3:
                scene bg rookiePoemAmy
            else:
                scene bg rookiePoemShadow
        if persistent.playthrough == 2 and chapter == 0 and persistent.ghost_menu and not persistent.sayonika_unlocked:
            scene bg rookiePoemGhostMenu
    show screen quick_menu #This allows the player to pull up the save menu during the poem minigame.
    if persistent.playthrough == 3: 
        show m_sticker at sticker_mid #Just Monika.
    else:
        # if persistent.playthrough == 0:
            # show s_sticker at sticker_leftest #Only show Sayori's sticker in Act 1.
        if persistent.playthrough == 2 and chapter == 0 and persistent.ghost_menu and not persistent.sayonika_unlocked:
            show s_sticker_gm at sticker_leftest #Ghostori's sticker.
            show n_sticker_gm at sticker_lmid #Ghostuki's sticker
            show y_sticker_gm at sticker_rmid #Ghosti's sticker.
            show m_sticker_gm at sticker_rightest #Ghostonika's sticker.
            show sayonika_sticker at sticker_m_glitch_2 #Sayonika's sticker.
        else:
            show s_sticker at sticker_leftest #Show Sayori's sticker.
            show n_sticker at sticker_lmid #Natsuki's sticker
            if persistent.playthrough == 2 and persistent.yuriKnife == True:
                show y_sticker_yandere at sticker_rmid #Replace Yuri's sticker with the "cut arms" yandere sticker.
            else:
                show y_sticker at sticker_rmid #Yuri's sticker
            # if persistent.playthrough == 2:# and chapter == 2:
            #     show m_sticker at sticker_m_glitch #Monika's sticker
            #show violet_sticker at sticker_m_glitch_2
            show m_sticker at sticker_rightest #Normal Monika
    if transition:
        with dissolve_scene_full #Gives the dissolve transition if the minigame isn't called with False.
    if persistent.playthrough == 3:
        play music ghostmenu #Change the music in Just Monika.
    else:
        if persistent.packagedMusic == True:
            play music rPoemPCKG
        else:
            play music rPoem
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False #Not completely sure why skipping has to be explicitly disabled, but apparently it does..
    $ forces.send_temporary_notification("MILESPOEM.app", "MILESPOEM.app successfully installed on your device!", action=Return(1))
    if persistent.playthrough == 2 and chapter == 0 and persistent.ghost_menu and not persistent.sayonika_unlocked: #Shows the below dialogue the first time the minigame is played.
        #call screen dialog("It's time to write a poem!\n\nPick words you think your favorite club member\nwill like. Something good might happen with\nwhoever likes your poem the most!", ok_action=Return())
        $ syka_name = "???"
        show syka ghost at t11
        syka "..."
        syka "..."
        if persistent.packagedMusic == True:
            show honey djHoney at l31 zorder 5
            $ forces.edmsession_music("Marshmello - You Can Cry (feat. James Arthur) (THRDL!FE Remix)")
            dj "Now playing: {i}Marshmello - You Can Cry (feat. James Arthur) (THRDL!FE Remix){/i}!"
            show honey at lhide zorder 1
            hide honey
        show syka ghost at t22
        show tails tailsCom at l21 zorder 5
        mtp "Welcome to MilesP..."
        mtp "..."
        mtp "Well... the app has been hacked, I will have to reset the operating system and..."
        show syka ghost at t33
        show sk orb at t32
        show tails tailsCom at t31 zorder 5
        mtp "Wait, Rookie! The orb that you found when you arrived to the other world! Is reacting to that person!"
        mtp "Maybe if you complete the minigame, the orb will fuse with the person, and the app will fix itself! Keep playing!"
        show tails at lhide zorder 1
        hide tails
        show syka at thide zorder 1
        show sk at thide zorder 1
        hide syka
        hide sk
    if persistent.playthrough == 2 and chapter == 0 and not persistent.ghost_menu:
        if persistent.packagedMusic == True:
            show honey djHoney at l31 zorder 5
            $ forces.edmsession_music("Marshmello - You Can Cry (feat. James Arthur) (THRDL!FE Remix)")
            dj "Now playing: {i}Marshmello - You Can Cry (feat. James Arthur) (THRDL!FE Remix){/i}!"
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
                y "Don't forget to click on the word {i}C.Emerald{/i} for a bonus!"
            else:
                show tails tailsCom at l11 zorder 5
                mtp "Welcome to MilesPOEM.exe!"
                mtp "Pick words you think one of these ladies will like!"
                mtp "The girl which likes your poem the most\nwill help you in the next Mission!"
                mtp "Good luck, Rookie!"
                show tails at lhide zorder 1
                hide tails
                mtp "Don't forget to click on the word {i}C.Emerald{/i} for a bonus!"
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
                y "Don't forget to click on the word {i}C.Emerald{/i} for a bonus!"
            else:
                show tails tailsCom at l11 zorder 5
                mtp "Welcome to MilesPOEM.exe!"
                mtp "Pick words you think one of these ladies will like!"
                mtp "The girl which likes your poem the most\nwill help you in the next Mission!"
                mtp "Good luck, Rookie!"
                show tails at lhide zorder 1
                hide tails
                mtp "Don't forget to click on the word {i}C.Emerald{/i} for a bonus!"
    if persistent.playthrough == 2 and chapter == 3:
        "Note for this Poem Minigame! Since Sayori is out of comission and Yuri is fully villain now..."
        "Selecting Sayori's words will favour Ghost Natsuki!"
        "Selecting Natsuki's words will favour Natsuki!"
        "Monika's words will still favour Monika, for all the Just Monika's here!"
        "Selecting Yuri's words will have a surprise portal also!"
    window hide
    python: #Variable initialization here. Important to note, these initialize at the start of the mini-game.
        poemgame_glitch = False
        played_baa = False
        progress = 1
        numWords = 20
        sPointTotal = 0
        nPointTotal = 0
        yPointTotal = 0
        mPointTotal = 0
        wordlist = list(full_wordlist)
        sayonikalist = list("YOU_UNLOCK_SAYONIKA!")

        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        mikexeTime = renpy.random.random() * 4 + 4
        sayoriPos = renpy.random.randint(-1,1)
        natsukiPos = renpy.random.randint(-1,1)
        yuriPos = renpy.random.randint(-1,1)
        monikaPos = renpy.random.randint(-1,1)
        mikexePos = renpy.random.randint(-1,1)
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        mikexeOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
        mikexeZoom = 1




        # Main loop for drawing and selecting words
        while True:
            ystart = 160
##################This block of code controls the word counter.###########################################
            if persistent.playthrough == 2 and chapter == 0 and persistent.ghost_menu and not persistent.sayonika_unlocked:
                #This makes the counter do the "111111111" thing in Act 2.
                pstring = ""
                for i in range(progress):
                    pstring += sayonikalist[i] #Appends "1" to pstring each loop.
            else:
                pstring = str(progress)
            ui.text("Progress: " + pstring + "/" + str(numWords), style="poemgame_text_forces", xpos=470, ypos=80, color='#00ff00')
##################This block of code puts the poem words on the screen.###################################
            for j in range(2):
                if j == 0: x = 460 #These two lines build columns out of the words (I think).
                else: x = 690
                ui.vbox()
                for i in range(5):
                    if persistent.playthrough == 3: #This sets all the words to "Monika" in Just Monika.
                        asdf = list("Monika")
                        for k in range(6): #This gives random corruption effects to the "Monika" words.
                            if random.randint(0, 4) == 0:
                                asdf[k] = ' '
                            elif random.randint(0, 4) == 0:
                                asdf[k] = random.choice(nonunicode)
                        word = PoemWord("".join(s), 0, 0, 0, 0, False)
                    elif persistent.playthrough == 2 and not poemgame_glitch and not played_baa and persistent.sayonika_unlocked and progress < numWords and random.randint(1, 6) == 4:
                        word = PoemWord(glitchtext(15), 3, 3, 3, 3, True) #This gives a chance for a random word in Act 2 to be the glitched word.
                        played_baa = True
                    else: #Normal circumstances
                        word = random.choice(wordlist) #Pick a random word out the wordlist
                        wordlist.remove(word) #Remove the word from the list so it can't appear in the minigame more than once.
                    ui.textbutton(word.word, clicked=ui.returns(word), text_style="poemgame_text_forces", xpos=x, ypos=i * 56 + ystart)
                ui.close()
##################This block controls what happens when words are selected.############################
            t = ui.interact()
            if not poemgame_glitch:
                if t.glitch: #This conditional controls what happens when the glitch word is selected.
                    poemgame_glitch = True
                    config.window_title = ""
                    _window_subtitle = "WELCOME TO MY SPECIAL HELL"
                    renpy.play("mod_assets/fnaf6scream.ogg")
                    renpy.music.play("mod_assets/poemgame/MIKEXE_Executionv5.ogg")
                    renpy.scene()
                    if persistent.yuriKnife == True:
                        renpy.show("rookiePoemMIKYuri")
                    else:    
                        renpy.show("rookiePoemMIK")
                    renpy.show("s_sticker_glitch", at_list=[sticker_leftest])
                    renpy.show("n_sticker_glitch", at_list=[sticker_lmid])
                    renpy.show("m_sticker_glitch", at_list=[sticker_rightest])
                    renpy.show("y_sticker_glitched", at_list=[sticker_rmid])
                    renpy.show("mikexe_sticker", at_list=[sticker_m_glitch_2])
                elif persistent.playthrough == 2 and chapter == 0 and persistent.ghost_menu and not persistent.sayonika_unlocked: #Sayonika Unlocker.
                    renpy.play(gui.activate_sound_glitch)
                    if t.sPoint >= 3:
                        renpy.show("s_sticker_gm hop")
                    if t.nPoint >= 3:
                        renpy.show("n_sticker_gm hop")
                    if t.yPoint >= 3:
                        renpy.show("y_sticker_gm hop")
                    if t.mPoint >= 3:
                        renpy.show("m_sticker_gm hop")
                    renpy.show("sayonika_sticker hop")
                elif persistent.playthrough != 3:
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
                    # if persistent.playthrough == 0: #Act 1. This makes the stickers hop when words are picked.
                        # if t.sPoint >= 3:
                        #     renpy.show("s_sticker hop")
                        # if t.nPoint >= 3:
                        #     renpy.show("n_sticker hop")
                        # if t.yPoint >= 3:
                        #     renpy.show("y_sticker hop")
                    if t.sPoint >= 3:
                        renpy.show("s_sticker hop")
                    if t.nPoint >= 3:
                        renpy.show("n_sticker hop")
                    if t.yPoint >= 3 and persistent.yuriKnife == True:
                        if t.word == "YURI EMPIRE":
                            renpy.show("y_sticker_yandere hopg")
                        else:
                            renpy.show("y_sticker_yandere hop")
                    if t.yPoint >= 3 and persistent.yuriKnife == False:
                        if t.word == "YURI EMPIRE":
                            renpy.show("y_sticker hopg")
                        else:
                            renpy.show("y_sticker hop")
                    if t.mPoint >= 3:
                        renpy.show("m_sticker hop")
                    # else: #Act 2
                        # if persistent.playthrough == 2 and chapter == 2 and random.randint(0,10) == 0: renpy.show("m_sticker hop") #1/10 chance for Monika's sticker to show.
                        # elif t.nPoint > t.yPoint: renpy.show("n_sticker hop") #Since there's just Yuri and Natsuki in Act 2, whoever has the higher value for the word hops.
                        # elif persistent.playthrough == 2 and not persistent.seen_sticker and random.randint(0,100) == 0:
                        #     renpy.show("y_sticker hopg") #"y_sticker_2g.png". 1/100 chance to see it, if we haven't seen it already.
                        #     persistent.seen_sticker = True
                        # elif persistent.playthrough == 2 and chapter == 2: renpy.show("y_sticker_cut hop") #Yuri's cut arms sticker.
                        # else: renpy.show("y_sticker hop")
                    #renpy.show("violet_sticker hop") #Violet roots for everyone.
            else:
                # r = random.randint(0, 10) #1/10 chance to hear "baa", one time.
                # if r == 0 and not played_baa:
                #     renpy.play("gui/sfx/baa.ogg")
                #     played_baa = True
                # elif r <= 5: renpy.play(gui.activate_sound_glitch)
                if t.word == "C.Emerald":
                    renpy.play("mod_assets/Emerald.ogg")
                elif t.word == "YURI EMPIRE":
                    renpy.play("mod_assets/NegaRing.ogg")
                else:
                    renpy.play("sfx/giggle.ogg")
                if t.sPoint >= 3:
                    renpy.show("s_sticker_glitch hop")
                if t.nPoint >= 3:
                    renpy.show("n_sticker_glitch hop")
                if t.yPoint >= 3:
                    if t.word == "YURI EMPIRE":
                        renpy.show("y_sticker_glitched hopg")
                    else:
                        renpy.show("y_sticker_glitched hop")
                if t.mPoint >= 3:
                    renpy.show("m_sticker_glitch hop")
                renpy.show("mikexe_sticker hop")
            sPointTotal += t.sPoint
            nPointTotal += t.nPoint
            yPointTotal += t.yPoint
            mPointTotal += t.mPoint
            progress += 1
            if progress > numWords: #This stops the minigame once we've picked all the words.
                break
##################End of main loop.##################################################################

        if persistent.playthrough == 2:
            # For chapter 1, add 5 points to whomever we sided with
            # if chapter == 1:
            #     exec(ch1_choice[0] + "PointTotal += 5")
            # Logic for taking point totals and assigning poem appeal, scene order, etc.
            unsorted_pointlist = {"sayori": sPointTotal, "natsuki": nPointTotal, "yuri": yPointTotal, "monika": mPointTotal}
            pointlist = sorted(unsorted_pointlist, key=unsorted_pointlist.get)

            # Set poemwinner to the highest scorer
            poemwinner[chapter] = pointlist[-1]
        else:
            if nPointTotal > yPointTotal: poemwinner[chapter] = "natsuki"
            else: poemwinner[chapter] = "yuri"

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


    if persistent.playthrough == 2 and persistent.seen_eyes == None and poemwinner[chapter] == "sayori":
        $ seen_eyes_this_chapter = True
        $ quick_menu = False
        $ _window_subtitle = "HAPPY THXUGHTS HAPPY THXUGHTS HAPPY THXUGHTS HAPPY THXUGHTS"
        play sound "sfx/eyes.ogg"
        $ persistent.seen_eyes = True
        stop music
        scene black with None
        show bg eyes_move
        pause 1.2
        hide bg eyes_move
        show bg eyes
        pause 0.5
        hide bg eyes
        show bg eyes_move
        pause 1.25
        hide bg eyes with None
        $ _window_subtitle = ""
        $ config.window_title = "Doki Doki Forces"
        $ quick_menu = True
    $ config.allow_skipping = True
    $ allow_skipping = True
    stop music fadeout 2.0
    hide screen quick_menu
    if poemwinner[chapter] == "monika" and persistent.waifuclubegg == None:
        $ mp.choose_monika = True
        $ mp.save()
        $ persistent.waifuclubegg = True
    if persistent.playthrough == 2 and chapter == 0 and persistent.ghost_menu and not persistent.sayonika_unlocked:
        stop music fadeout 2.0
        scene bg rookiePoemGhostMenu
        show syka ghost at t21
        show sk orb at t22
        "Using the orb, you restored the soul into the ghostly vessel!"
        "You saved another student of the Literature Club world! Is Sayonika!"
        show sk orb at thide zorder 1
        hide sk
        show syka 1t at t11
        $ syka_name = "Sayonika"
        syka "THIS WAS THE WORST EXPERIENCE EVER!!!"
        syka "BEING TRAPPED IN AN {i}ORB{/i}, OF ALL PLACES...!"
        syka "Wait! Who is sneaking at me???"
        syka 1n "Oh hey! It's you, [player]!"
        syka 1a "Hello there!"
        syka 1s "Wait! Were {i}you{/i} the one who saved me?"
        show syka 3a at h11
        syka "MANY MANY MANY THANKS!!!!"
        syka 3d "Oh my! Wait please!!! What a mess we have here in this code!"
        syka "Is this how you coded your story, CPG?"
        syka 3g "I'm a little dissapointed in your programming skills..."
        syka 3e "Hey, wait a minute... why are there a lot of 'YuriKnife' stuff all around the code?"
        syka 3h "Someone was trying to hack the code...."
        syka 4q "I noticed it for his or her disgusting noob mistakes in the code!"
        syka "Sorry, [player]. As you can see, I can't help you right now."
        syka 1b "I need to fix this mess first. So, come back to me later, when you finish the adventure, and we will do our presentations formally, ok?"
        syka 3b "See you!"
        if poemwinner[0] == "yuri":
            $ style.say_dialogue = style.edited
            show yuri lovelyEyes2 at t22
            show syka 4e at t21
            syka 4e "The gathering and the pain are coming."
            syka "Suffering and despair will fill this land with blood and jasmine oil."
            syka "The impure will be purged from the sands of recollection."
            syka "And only those who can fill their heart thirsting for lust will remain."
            $ style.say_dialogue = style.normal
        $ forces.send_temporary_notification("Travis the Bad Eater", "Fear code bugs! You unlocked the option to play as Sayonika!", action=Return(1))
        $ persistent.sayonika_unlocked = True
    if poemgame_glitch == True:
        $ _window_subtitle = " SUMMONING MIK WAS A TERRIBLE MISTAKE"
        scene bg mikEXEWorld
        show gfm rexe11 at h11 zorder 6
        show wings wingRed at h11 behind gfm
        $ style.say_dialogue = style.edited_mik
        if mikEXEPoemChapter == 0:
            mik2 "Hello."
            mik2 "First time I can see you."
            mik2 "I hope you enjoy your funny adventure with your new friends."
            mik2 "Ehehe~... I have cool plans for all of you..."
            mik2 "Until later!"
        elif mikEXEPoemChapter == 1:
            mik2 "Hello again."
            mik2 "It seems you will go to rescue Ghost."
            mik2 "I like her. It's a shame she is not part of my evil team."
            mik2 "...Did I took part in Natsuki's stuff at the prologue...?"
            mik2 "Ehehe~! Who knows! I don't think you will like the answer, anyways! See ya!"
        elif mikEXEPoemChapter == 2:
            mik2 "Here is the savior of the world again..."
            mik2 "Oh, so now you are going for Sonic! I believed you are seeing me because you liked my destroyed city..."
            mik2 "Sonic the Hedgehog... the fastest thing alive."
            mik2 "I wonder if I will be yoo slow for him... or he will be too slow for me!!!"
            mik2 "And no, keep playing. I will not reveal my plans to you yet. Goodbye!"
        else:
            mik2 "Here you are."
            mik2 "You are really closer to end your adventure!"
            mik2 "I hope you had enjoyed it!"
            mik2 "Now it's time to execute my plan!"
            mik2 "Do you really believed the true masterminds where Egghead, Infisuck, Yuri the psycho and that pink gem...?"
        $ style.say_dialogue = style.normal
        $ _window_subtitle = ""
        $ config.window_title = "Doki Doki Forces"
    show white as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0
    return
############ Image definitions start here. #############
image bg eyes_move:
    "images/bg/eyes.png"
    parallel:
        yoffset 720 ytile 2
        linear 0.5 yoffset 0
        repeat
    parallel:
        0.1
        choice:
            xoffset 20
            0.05
            xoffset 0
        choice:
            xoffset 0
        repeat
image bg eyes:
    "images/bg/eyes.png"

image s_sticker:
    "gui/poemgame/s_sticker_1.png"
    xoffset sayoriOffset xzoom sayoriZoom
    block:
        function randomPauseSayori
        parallel:
            sticker_move_n
        parallel:
            function randomMoveSayori
        repeat

image n_sticker:
    "gui/poemgame/n_sticker_1.png"
    xoffset natsukiOffset xzoom natsukiZoom
    block:
        function randomPauseNatsuki
        parallel:
            sticker_move_n
        parallel:
            function randomMoveNatsuki
        repeat

image y_sticker:
    "gui/poemgame/y_sticker_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image y_sticker_cut:
    "gui/poemgame/y_sticker_cut_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image m_sticker:
    "gui/poemgame/m_sticker_1.png"
    xoffset monikaOffset xzoom monikaZoom
    block:
        function randomPauseMonika
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMonika
        repeat

image mikexe_sticker:
    "mod_assets/poemgame/Chibi_EliteKrAZyFan_Stand.png"
    xoffset mikexeOffset xzoom mikexeZoom
    block:
        function randomPauseMikexe
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMikexe
        repeat
    
image sayonika_sticker:
    "mod_assets/sayonika/sk_sticker_1.png"
    xoffset mikexeOffset xzoom mikexeZoom
    block:
        function randomPauseMikexe
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMikexe
        repeat

image y_sticker_yandere:
    "mod_assets/poemgame/y_yandere_sticker_1_cut.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image s_sticker hop:
    "gui/poemgame/s_sticker_2.png"
    xoffset sayoriOffset xzoom sayoriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "s_sticker"

image s_sticker_glitch hop:
    "mod_assets/poemgame/s_sticker_glitch.png"
    xoffset sayoriOffset xzoom sayoriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "s_sticker_glitch"

image n_sticker hop:
    "gui/poemgame/n_sticker_2.png"
    xoffset natsukiOffset xzoom natsukiZoom
    sticker_hop
    xoffset 0 xzoom 1
    "n_sticker"

image n_sticker_glitch hop:
    "mod_assets/poemgame/n_sticker_glitch_1.png"
    xoffset natsukiOffset xzoom natsukiZoom
    sticker_hop
    xoffset 0 xzoom 1
    "n_sticker_glitch"

image y_sticker hop:
    "gui/poemgame/y_sticker_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image y_sticker_cut hop:
    "gui/poemgame/y_sticker_cut_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_cut"

image y_sticker hopg:
    "gui/poemgame/y_sticker_2g.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image y_sticker_cut hopg:
    "gui/poemgame/y_sticker_2g.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_cut"

image y_sticker_yandere hopg:
    "gui/poemgame/y_sticker_2g.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_yandere"

image y_sticker_glitched hopg:
    "gui/poemgame/y_sticker_2g.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_glitched"

image y_sticker_glitched hop:
    "mod_assets/poemgame/y_yandere_sticker_5_exe.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_glitched"

image m_sticker hop:
    "gui/poemgame/m_sticker_2.png"
    xoffset monikaOffset xzoom monikaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "m_sticker"

image m_sticker_glitch hop:
    "mod_assets/poemgame/m_sticker_glitch.png"
    xoffset monikaOffset xzoom monikaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "m_sticker_glitch"

image mikexe_sticker hop:
    "mod_assets/poemgame/Chibi_EliteKrAZyFan_Excited.png"
    xoffset mikexeOffset xzoom mikexeZoom
    hyperbouncySayori_hop
    xoffset 0 xzoom 1
    "mikexe_sticker"

image sayonika_sticker hop:
    "mod_assets/sayonika/sk_sticker_2.png"
    xoffset mikexeOffset xzoom mikexeZoom
    sticker_hop
    xoffset 0 xzoom 1
    "sayonika_sticker"

image y_sticker_yandere hop:
    "mod_assets/poemgame/y_yandere_sticker_2_cut.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_yandere"

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

image y_sticker_glitched:
    "mod_assets/poemgame/y_yandere_sticker_1_exe.png"
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
    xoffset monikaOffset xzoom monikaZoom
    block:
        function randomPauseMonika
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMonika
        repeat

image y_sticker glitch:
    "gui/poemgame/y_sticker_1_broken.png"
    xoffset yuriOffset xzoom yuriZoom zoom 3.0
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image s_sticker_gm:
    "mod_assets/poemgame/s_sticker_gm_1.png"
    xoffset sayoriOffset xzoom sayoriZoom
    block:
        function randomPauseSayori
        parallel:
            sticker_move_n
        parallel:
            function randomMoveSayori
        repeat

image n_sticker_gm:
    "mod_assets/poemgame/n_sticker_gm_1.png"
    xoffset natsukiOffset xzoom natsukiZoom
    block:
        function randomPauseNatsuki
        parallel:
            sticker_move_n
        parallel:
            function randomMoveNatsuki
        repeat

image y_sticker_gm:
    "mod_assets/poemgame/y_sticker_gm_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image m_sticker_gm:
    "mod_assets/poemgame/m_sticker_gm_1.png"
    xoffset monikaOffset xzoom monikaZoom
    block:
        function randomPauseMonika
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMonika
        repeat

image s_sticker_gm hop:
    "mod_assets/poemgame/s_sticker_gm_2.png"
    xoffset sayoriOffset xzoom sayoriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "s_sticker_gm"

image n_sticker_gm hop:
    "mod_assets/poemgame/n_sticker_gm_2.png"
    xoffset natsukiOffset xzoom natsukiZoom
    sticker_hop
    xoffset 0 xzoom 1
    "n_sticker_gm"

image y_sticker_gm hop:
    "mod_assets/poemgame/y_sticker_gm_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_gm"

image m_sticker_gm hop:
    "mod_assets/poemgame/m_sticker_gm_2.png"
    xoffset monikaOffset xzoom monikaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "m_sticker_gm"

image jordens_gm:
    "mod_assets/poemgame/jordens.png"
    xoffset yuriOffset xzoom yuriZoom

image s_sticker_gm_fixed:
    "mod_assets/poemgame/s_sticker_gm_1.png"

transform sticker_left:
    xcenter 100 yalign 0.9 subpixel True

transform sticker_mid:
    xcenter 220 yalign 0.9 subpixel True

transform sticker_right:
    xcenter 340 yalign 0.9 subpixel True

transform sticker_glitch:
    xcenter 50 yalign 1.8 subpixel True

transform sticker_m_glitch:
    xcenter 100 yalign 1.35 subpixel True

transform sticker_leftest:
    xcenter 60 yalign 0.9 subpixel True
    
transform sticker_lmid:
    xcenter 160 yalign 0.9 subpixel True

transform sticker_rmid:
    xcenter 260 yalign 0.9 subpixel True

transform sticker_rightest:
    xcenter 360 yalign 0.9 subpixel True

transform sticker_m_glitch_2:
    xcenter 650 yalign 0.9 subpixel True

transform sticker_move_n:
    easein_quad .08 yoffset -15
    easeout_quad .08 yoffset 0

transform sticker_hop:
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0

transform hyperbouncySayori_hop:
    easein_quad .10 yoffset -320
    easeout_quad .10 yoffset 0
    easein_quad .10 yoffset -320
    easeout_quad .10 yoffset 0
    easein_quad .10 yoffset -320
    easeout_quad .10 yoffset 0
    easein_quad .10 yoffset -320
    easeout_quad .10 yoffset 0