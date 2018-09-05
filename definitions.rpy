#This is a copy of definitions.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Explanation for Definitions
#This section defines stuff for the game: sprite poses for the girls, music, and backgrounds
#If you plan on adding new content, pop them over down there and mimic the appropriate lines!
define persistent.demo = False
define persistent.steam = False
define config.developer = False #Change this flag to True to enable dev tools

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    renpy.music.register_channel("ambient","sfx",True,tight=True) #This creates a new sound channel called "ambient" with looping enable

    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        if persistent.do_not_delete: return
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass
    def install_character(name):
        import os 
        try: renpy.file(config.basedir + "/characters/" + name + ".chr")
        except: open(config.basedir + "/characters/" + name + ".chr", "wb").write(renpy.file(name + ".chr").read())
    def restore_all_characters():
        try: renpy.file("../characters/monika.chr")
        except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
        try: renpy.file("../characters/natsuki.chr")
        except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
        try: renpy.file("../characters/yuri.chr")
        except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
        try: renpy.file("../characters/sayori.chr")
        except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())
        try: renpy.file("../characters/ghost.chr")
        except: open(config.basedir + "/characters/ghost.chr", "wb").write(renpy.file("ghost.chr").read())
    def restore_relevant_characters():
        restore_all_characters()
        if persistent.playthrough == 1 or (persistent.playthrough == 2 and chapter == 4):
            delete_character("sayori")
        elif persistent.playthrough == 3:
            delete_character("sayori")
            delete_character("natsuki")
            delete_character("yuri")
            delete_character("ghost")
        elif persistent.playthrough == 4:
            delete_character("monika")
    def pause(time=None):
        global _windows_hidden
        if not time:
            _windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            _windows_hidden = False
            return
        if time <= 0: return
        _windows_hidden = True
        renpy.pause(time)
        _windows_hidden = False
    # def sayori_check(trans, st, at):
    #     if renpy.loadable("../characters/sayori.chr"):
    #         persistent.sayori_helped = True
    #         renpy.say(mc, "I'm on this function")
    #         renpy.call("cinnamonOrb")
    #     else:
    #         renpy.say(sth,"NOPE!")

#Music
#The Music section is where you can reference existing DDLC audio

#You'll see this in some existing scripts as command 'play music [t1]' for example
#For easier reference, there are comments next to it so you can go DJ on the mod :)
define audio.t1 = "<loop 22.073>bgm/1.ogg"  #Main theme (title)


define audio.t2 = "<loop 4.499>bgm/2.ogg"   #Sayori theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"   #Main theme (in-game)
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"  #Poem minigame
define audio.t4g = "<loop 1.000>bgm/4g.ogg"

define audio.t5 = "<loop 4.444>bgm/5.ogg"   #Sharing poems...... 'Okay Everyone~!'
#Hey Mod team, our themes aren't defined here in the original script.
#Did some reading around and there was this + "_character" reference elsewhere.
#Anyhow, I'll try 'defining' them and see if it works!

define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" #I'm the only one with pianos x3
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" #Hxppy Thoughts with Ukelele & Snapping~!
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" #Was it always cute on purpose?
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" #Fancy harps and instruments!

#Yeah, Monika... that should be good.
#So, take it from her and if you want to define music, make sure it exists in the appropriate folder
#Define its "audio.name" and see how it goes! (this should always be .ogg too, I think)

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"  #Yuri/Natsuki theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"   #Causing trouble
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"   #Trouble resolved
define audio.t9 = "<loop 3.172>bgm/9.ogg"   #Emotional
define audio.t9g = "<loop 1.532>bgm/9g.ogg" #207% speed
define audio.t10 = "<loop 5.861>bgm/10.ogg"   #Confession
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"


define audio.m1 = "<loop 0>bgm/m1.ogg" #Monika and her spaceroom music
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" #Monika music post-deletion

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.rain = "<loop 0.0>mod_assets/sfx/rain.ogg" #the sound file that will be player when it's raining
define audio.rainindoors = "<loop 0.0>mod_assets/sfx/rain2.ogg" #a quieter version of the sound, if you want to use it while indoors use "play ambient rainindoors" isntead of "play sound rainindoors"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"
define audio.forces = "mod_assets/forcesMainTheme.ogg"
define audio.forces_justyuri = "mod_assets/speedstersMainTheme.ogg"
define audio.specialMenu = "mod_assets/specialMenu.ogg"
define audio.pumpedUpKicks = "mod_assets/pumpedUpKicks.ogg"
define audio.aiz = "mod_assets/angelIsland.ogg"
define audio.rubyMusic = "mod_assets/RubyPresence.ogg"
define audio.eggRobos = "mod_assets/eggRobos.ogg"
define audio.infiniteMusic = "<loop 0>mod_assets/infiniteMusic.ogg"
define audio.rPoem = "<loop 0>mod_assets/poemRookie.ogg"
define audio.herWorld = "mod_assets/poemgame/MIKEXE_Executionv5.ogg"
define audio.rWispon = "<loop 0>mod_assets/saveThem.ogg"
define audio.yuripls = "<loop 4.444>bgm/5_yuri2.ogg"
define audio.oatmeal = "mod_assets/monikas_oatmeal.ogg"
define audio.ghostNatsuki = "<loop 0>mod_assets/ghostNatsuki.ogg"
define audio.greenHillZ1 = "<loop 0>mod_assets/greenHill1.ogg"
define audio.chemPlant1 = "<loop 0>mod_assets/chemicalPlant1.ogg"
define audio.chemPlant2 = "<loop 0>mod_assets/chemicalPlant2.ogg"
define audio.studioP1 = "<loop 0>mod_assets/studiopolis.ogg"
define audio.studioP2 = "<loop 0>mod_assets/studiopolis2.ogg"
define audio.fBattery = "<loop 0>mod_assets/flyingBattery.ogg"
define audio.pressGarden1 = "<loop 0>mod_assets/pressGarden1.ogg"
define audio.stardust = "<loop 0>mod_assets/stardustSpeed1.ogg"
define audio.stardust2 = "<loop 0>mod_assets/stardustSpeed2.ogg"
define audio.vsMetal = "<loop 0>mod_assets/metalSonicBoss.ogg"
define audio.metalSayori = "<loop 0>mod_assets/metalSayori.ogg"
define audio.eggmanMusic = "<loop 0>mod_assets/eggmanMusic.ogg"
define audio.yuriRoute = "<loop 0>mod_assets/yuriRouteHerTheme.ogg"
define audio.monikaSong = "mod_assets/bossEggman2.mp3"
define audio.invincibility = "<loop 0>mod_assets/invincible.ogg"
define audio.bossQueen = "<loop 0>mod_assets/queenBomber.ogg"
define audio.metalDokis = "<loop 0>mod_assets/VS Metal Dokis.ogg"
define audio.sonicTheme = "<loop 0>mod_assets/sonicTheme.ogg"
define audio.finalBoss = "<loop 0>mod_assets/EggReverie.ogg"
define audio.vsSayori = "<loop 0>mod_assets/vsSayori.ogg"
define audio.hidrocity = "<loop 0>mod_assets/hidrocity.ogg"
define audio.moddersPortal = "<loop 0>mod_assets/SergCookiesTermSkull.ogg"
define audio.mikuPortal = "<loop 0>mod_assets/miku.ogg"
define audio.scp682Portal = "<loop 0>mod_assets/scp682.ogg"
define audio.himPortal = "<loop 0>mod_assets/mus_zzz_c.ogg"
define audio.himMegalovania = "<loop 0>mod_assets/backstab.ogg"
define audio.himFrisk = "<loop 0>mod_assets/mus_xpart.ogg"
define audio.mirageSaloon = "<loop 0>mod_assets/saloon.ogg"
define audio.heavyMagician = "<loop 0>mod_assets/magician.ogg"
define audio.yuriLastStand = "<loop 0>mod_assets/yuriLastStand.ogg" #Fairplay (Let There Be Love)
define audio.shadowAppears = "<loop 0>mod_assets/shadowAppears.ogg"
define audio.oilOcean1 = "<loop 0>mod_assets/oilOceanAct1.ogg"
define audio.oilOcean2 = "<loop 0>mod_assets/oilOceanAct2.ogg"
define audio.lavaReef = "<loop 0>mod_assets/lavaReef.ogg"
define audio.pumpedUpMettatons = "<loop 0>mod_assets/pumpedUpMettatons.ogg"
define audio.vsoctiboss = "<loop 0>mod_assets/octiBoss.ogg"
define audio.yuriStardustHue = "<loop 0>mod_assets/yuriStardustHue.ogg"
define audio.hilltop = "<loop 0>mod_assets/hillTop.ogg"
define audio.Emerald_word = "mod_assets/Emerald.ogg"
define audio.Ring = "mod_assets/Ring.ogg"
define audio.NegaRing = "mod_assets/NegaRing.ogg"
define audio.Uganda = "mod_assets/Uganda.ogg"
define audio.sonic1UP = "mod_assets/sonic1UP.ogg"
define audio.ruby = "mod_assets/rubySound.ogg"
define audio.destroy = "mod_assets/Destroy.ogg"
define audio.djstop = "mod_assets/djStop.ogg"
define audio.roboticizer = "mod_assets/roboticizer.ogg"
define audio.FUTURE = "mod_assets/TimeWarp.ogg"
define audio.saloonGlitched = "mod_assets/saloonGlitched.ogg" #Fairplay slowed and on an old vynil.
define audio.magicianHat = "mod_assets/MysticHat.ogg"
define audio.magicianTransform = "mod_assets/MysticTwinkle.ogg"
define audio.magicianTrick = "mod_assets/MysticHatNode.ogg"
define audio.magicianBox = "mod_assets/MysticBox.ogg"
define audio.machinegun = "mod_assets/machineGun.ogg"
define audio.sega = "mod_assets/sega.ogg"
define audio.segaGhost = "mod_assets/segaGhost.ogg"
define audio.segaGhost_sayonika = "mod_assets/segaGhost_sayonika.ogg"
define audio.drowning = "mod_assets/drowning.ogg"
define audio.endingBadYuri = "mod_assets/yoursTrulySatan_phoneticHeroOCRemix.ogg"

#EDM Session Revamped
define audio.studioPCKG1 = "mod_assets/EDMSessionRevamped/Studiopolis1.ogg"
define audio.aizPCKG = "mod_assets/EDMSessionRevamped/angelIslandPCKG.ogg"
define audio.eggRobosPCKG = "mod_assets/EDMSessionRevamped/eggRobosPCKG.ogg"
define audio.infiniteJoke = "mod_assets/EDMSessionRevamped/infiniteJokePCKG.ogg"
define audio.nullSpacePCKG = "mod_assets/EDMSessionRevamped/nullSpacePCKG.ogg"
define audio.greenHillPCKG = "mod_assets/EDMSessionRevamped/GreenHill2.ogg"
define audio.chemPlantPCKG = "mod_assets/EDMSessionRevamped/ChemPlantPCKG.ogg"
define audio.jokePCKG = "mod_assets/EDMSessionRevamped/joke.ogg"
define audio.yuriRoutePCKG = "mod_assets/EDMSessionRevamped/yuriRoutePCKG.ogg"
define audio.eggmanPCKG = "mod_assets/EDMSessionRevamped/BossEggman1.ogg"
define audio.ghostNPCKG = "mod_assets/EDMSessionRevamped/ghostNatsukiPCKG.ogg"
define audio.metalDokisPCKG = "mod_assets/EDMSessionRevamped/vsMetalDokisPCKGD.ogg"
define audio.lovePCKG = "mod_assets/EDMSessionRevamped/love.ogg"
define audio.fBatteryPCKG = "mod_assets/EDMSessionRevamped/FlyingBattery2.ogg"
define audio.pulpSolstice = "mod_assets/EDMSessionRevamped/pulpSolstice1.ogg"
define audio.muffledStardust = "<loop 0>mod_assets/EDMSessionRevamped/muffledStardust.ogg"
define audio.vsMetalPCKG = "mod_assets/EDMSessionRevamped/MetalSonic.ogg"
define audio.speedwayPCKG = "mod_assets/EDMSessionRevamped/StardustSpeedway2.ogg"
define audio.soundTestM = "mod_assets/EDMSessionRevamped/soundTest.ogg"
define audio.hidrocityPCKG = "mod_assets/EDMSessionRevamped/Hydrocity2.ogg"
define audio.rPoemPCKG = "<loop 0>mod_assets/EDMSessionRevamped/poemRookiePCKG.ogg"
define audio.mirageSaloonPCKG = "<loop 0>mod_assets/EDMSessionRevamped/MirageSaloon1K.ogg"
define audio.heavyMagicianPCKG = "<loop 0>mod_assets/EDMSessionRevamped/magicianPCKG.ogg"
define audio.oilOcean1PCKG = "mod_assets/EDMSessionRevamped/OilOcean1PCKG.ogg"
define audio.oilOcean2PCKG = "mod_assets/EDMSessionRevamped/OilOcean2PCKG.ogg"
define audio.lavaReefPCKG = "mod_assets/EDMSessionRevamped/LavaReef1.ogg"
define audio.vsoctibossPCKG = "<loop 0>mod_assets/EDMSessionRevamped/octiBossPCKG.ogg"
define audio.yuriStardustKP = "mod_assets/EDMSessionRevamped/yuriStardustKP.ogg"
define audio.avicii = "mod_assets/EDMSessionRevamped/avicii.ogg"

# Backgrounds
image black = "#000000"
image red = "#ff0000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image rubypink = "#f10198c8"
image sayoricolor = "#59b2f4"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png"
image bg class_day = "bg/class.png"
image bg corridor = "bg/corridor.png"
image bg club_day = "bg/club.png"
image bg club_day2 = "bg/club-skill.png"
image bg closet = "bg/closet.png"
image bg bedroom = "bg/bedroom.png"
image bg sayori_bedroom = "bg/sayori_bedroom.png"
image bg house = "bg/house.png"
image bg kitchen = "bg/kitchen.png"

image bg notebook = "bg/notebook.png"
image bg notebook-glitch = "bg/notebook-glitch.png"
image bg black_ghost = "mod_assets/forces.png"
image bg club_day2_2 = "mod_assets/club-skill_slipsy.png"
image bg club_bulli = "mod_assets/club-bulli.png"
image bg corridor_creepy = "mod_assets/corridor-skill.png"
image bg oldbackground = "mod_assets/game_menu_bg.png"
image bg oldbackgroundGhost = "mod_assets/game_menu_bg_ghost.png"
image bg prologue1 = "mod_assets/prologue_bg.png"
image bg prologue2 = "mod_assets/prologue_bg2.png"
image bg prologue3 = "mod_assets/prologue_bg3.png"
image bg prologueJustYuri = "mod_assets/prologue_bg_yuri.png"
image bg studiopolis = "mod_assets/studiopolis.png"
image bg studiopolis2 = "mod_assets/studiopolis2.png"
image bg rookiePoemSonic = "mod_assets/poemgame/rookieNb.png"
image bg rookiePoemTails = "mod_assets/poemgame/rookieNb2.png"
image bg rookiePoemKnuckles = "mod_assets/poemgame/rookieNb3.png"
image bg rookiePoemShadow = "mod_assets/poemgame/rookieNb4.png"
image bg rookiePoemAmy = "mod_assets/poemgame/rookieNb5.png"
image bg rookiePoemYuri = "mod_assets/poemgame/rookieNbY.png"
image bg rookiePoemMIKEXE = "mod_assets/poemgame/rookieNb666.png"
image bg rookiePoemMIKEXEYuri = "mod_assets/poemgame/rookieNb666Y.png"
image bg rookiePoemGhostMenu = "mod_assets/poemgame/hellcity.png"
image rookiePoemMIK = "mod_assets/poemgame/rookieNb666.png"
image rookiePoemMIKYuri = "mod_assets/poemgame/rookieNb666Y.png"
image lit_club_pamphlet = "mod_assets/lit_club_panphlet.png"
image bg mikEXEWorld = "mod_assets/poemgame/hellcity.png"
image bg angelIsland_beach = "mod_assets/angelisland_beach.png"
image bg angelIsland_eggRobos = "mod_assets/angelisland_eggrobos.png"
image bg angelIsland_eggRobosRuby = "mod_assets/angelisland_eggrobos_ruby.png"
image bg angelIsland_jungle = "mod_assets/angelisland_jungle.png"
image bg ruined_residential = "mod_assets/war by cute (DDNP) (36u8CZs).png"
image bg ruined_residential_ruby = "mod_assets/Ruined_Home_ruby.png"
image bg nullspace = "mod_assets/NullSpace.png"
image bg greenHill1 = "mod_assets/greenHill.png"
image bg greenHill2 = "mod_assets/greenHil2.png"
image bg chemicalPlant = "mod_assets/chemicalPlant.png"
image bg chemicalPlant2 = "mod_assets/chemicalPlant2.png"
image bg flyingBattery = "mod_assets/flyingBattery.png"
image bg pressGarden = "mod_assets/pressGarden.png"
image bg stardust = "mod_assets/stardust.png"
image bg stardust2 = "mod_assets/stardustPresent.png"
image bg ghostBG = "mod_assets/ghostBG.png"
image bg lavaReefVS = "mod_assets/lavaReefVSSayori.png"
image bg creepyDokiForces = "mod_assets/Awesome Creepy Doki Doki Forces.png"
image bg creepyDokiForcesB = "mod_assets/Awesome Creepy Doki Doki Forces B.png"
image bg creepyDokiForcesC = "mod_assets/Awesome Creepy Doki Doki Forces C.png"
image bg hidrocity = "mod_assets/hydrocity.png"
image bg hidrocity_Boss = "mod_assets/hydrocity_AnnoyingBoss.png"
image bg crashfever = "mod_assets/crashFever.png"
image bg scp_room = "mod_assets/scp_hall.png"
image bg scp_video = "mod_assets/scp_video.png"
image bg scp_682 = "mod_assets/scp_682battle.png"
image bg undertale_corridor = "mod_assets/undertale_Corridor.png"
image bg mirageSaloonbg = "mod_assets/mirageSaloon.png"
image bg magicianRoom = "mod_assets/magicianRoom.png"
image bg closet_creepy = "mod_assets/closet_creepy.png"
image bg oilocean1 = "mod_assets/oilOcean1.png"
image bg oilocean2 = "mod_assets/oilOcean2.png"
image bg oiloceanSub = "mod_assets/oilOceanSubmarine.png"
image bg oiloceanSub2 = "mod_assets/oilOceanSubmarine2.png"
image bg octiBoss = "mod_assets/octiBoss.png"
image bg oilocean2Creepy = "mod_assets/oilOcean2Creepy.png"
image bg stardustYuri = "mod_assets/y_stardust.png"
image bg avicii01 = "mod_assets/avicii01.png"
image bg avicii02 = "mod_assets/avicii02.png"

#TitleCards
image bg tcLitClub = "mod_assets/tcLitClub.png"
image bg tcNullSpace = "mod_assets/tcNullSpace.png"
image bg tcPoem = "mod_assets/tcPoem.png"
image bg tcGreenHill = "mod_assets/tcGreenHill.png"
image bg tcChemicalPlant = "mod_assets/tcChemicalPlant.png"
image bg tcHidrocity = "mod_assets/tcHidrocity.png"
image bg tcMirageSaloon = "mod_assets/tcMirageSaloon.png"
image tcOilOcean = "mod_assets/tcOilOcean.png"
image bg tcOilOcean = "mod_assets/tcOilOcean.png"
image bg tcPressGarden = "mod_assets/tcPressGarden.png"
image bg tcStudiopolis = "mod_assets/tcStudiopolis.png"
image bg tcStardust = "mod_assets/tcStardust.png"
image bg tcAngelIsland = "mod_assets/tcAngelIsland.png"
image bg tcMetallicMadness = "mod_assets/tcMetallicMadness.png"
image bg tcVsTitanicMonarch = "mod_assets/tcTitanicMonarch.png"
image bg tcVsMetal = "mod_assets/tcVsMetal.png"
image bg tcVsMikEXE = "mod_assets/tcVsMik.png"
image bg tcHILL = "mod_assets/tcHILL.png"
image bg tcMonikaRoom = "mod_assets/tcMonikaRoom.png"
image bg tcError = "mod_assets/tcError.png"
image bg tcVsSayori = "mod_assets/tcVsSayori.png" #Lava Reef

#ChibiTV for Studiopolis scene if you played Sonic Mania with Doki Doki Studiopolis Club mod!
image bg chibiMonika = "mod_assets/chibiTV01.png"
image bg chibiMonikab = "mod_assets/chibiTV01b.png"
image bg chibiSayori = "mod_assets/chibiTV03.png"
image bg chibiNatsuki = "mod_assets/chibiTV04.png"
image bg chibiYuri = "mod_assets/chibiTV02.png"
image bg chibiYuriEmpire = "mod_assets/chibiTV02b.png"
image bg chibiEmeraldM = "mod_assets/chibiTV05.png"
image bg chibiEmeraldS = "mod_assets/chibiTV05b.png"
image bg chibiEmeraldN = "mod_assets/chibiTV05c.png"
image bg chibiEmeraldY = "mod_assets/chibiTV05d.png"
image bg chibiGhost = "mod_assets/chibiTV06.png"
image bg chibiEmeraldG = "mod_assets/chibiTV06b.png"

#Other image backgrounds
image ghostMenuFull = "mod_assets/gMenuFull.png"
image sonicEXE = "mod_assets/iamgod.png"
image sonic_exe_scene = "mod_assets/sonic_exe_scene.png"
image mik_exe_scene = "mod_assets/mik_exe_scene.png"
image mirageSaloon_glitch1 = "mod_assets/mirageSaloon_glitch1.png"
image mirageSaloon_glitch2 = "mod_assets/mirageSaloon_glitch2.png"
image mirageSaloon_glitch3 = "mod_assets/mirageSaloon_glitch3.png"
image mirageSaloon_glitch4 = "mod_assets/mirageSaloon_glitch4.png"
image mirageSaloon_glitch5 = "mod_assets/mirageSaloon_glitch5.png"
image yuriMessedUp = "mod_assets/yuriMessedUp.png"
image poemPanic = "mod_assets/poemCompetition.png"
image poster yuriPoster1 = "mod_assets/YuriEmpirePoster001.png"
image poster yuriPoster2 = "mod_assets/YuriEmpirePoster002.png"

#image bg soundTest = "mod_assets/soundTest_a.png"
image bg soundTest:
    choice:
        "mod_assets/soundTest_a.png"#EDM Disabled
    choice:
        "mod_assets/soundTest_b.png"#Just Yuri
    choice:
        "mod_assets/soundTest_b1.png"#Dead Sayori
    choice:
        "mod_assets/soundTest_b3.png"#Crazy Monika
    choice:
        "mod_assets/soundTest_b2.png"#Glitched Natsuki
    choice:
        "mod_assets/soundTest_b4.png"#I can see you
#image bg soundTestb = "mod_assets/soundTest_a2.png"
image bg soundTestb:
    choice:
        "mod_assets/soundTest_a2.png"#EDM Enabled
    choice:
        "mod_assets/soundTest_b.png"#Just Yuri
    choice:
        "mod_assets/soundTest_b1.png"#Dead Sayori
    choice:
        "mod_assets/soundTest_b3.png"#Crazy Monika
    choice:
        "mod_assets/soundTest_b2.png"#Glitched Natsuki
    choice:
        "mod_assets/soundTest_b4.png"#I can see you
image bg soundTestc = "mod_assets/soundTest_b5.png"#Mik.exe

image bg glitch = LiveTile("bg/glitch.jpg")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

#------------------------------------------------From hereon, the girl's bodies are defined along with their heads.
#-----------------------------------------here's reference for the left half------the right half--------the head
# Sayori
image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")

image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat

# Natsuki
image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 41 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3.png")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3.png")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3.png")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3.png")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3.png")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3.png")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3.png")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3.png")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3.png")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3.png")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3.png")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3.png")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3.png")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3.png")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3.png")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3.png")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3.png")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3.png")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3.png")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3.png")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3.png")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")
#image natsuki 52 = im.Composite((960, 960), (0, 0), "natsuki/3.png", (0, 0), "natsuki/4t.png")


image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3b.png")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3b.png")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3b.png")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3b.png")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3b.png")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3b.png")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3b.png")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3b.png")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3b.png")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3b.png")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3b.png")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3b.png")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3b.png")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3b.png")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3b.png")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3b.png")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3b.png")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3b.png")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3b.png")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3b.png")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")

# Natsuki legacy
image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")

image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"

# Yuri
image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")

image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

image yuri eyes_base = "yuri/eyes1.png"

image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"

#------------------------------------------------Our beloved Monika only has her school uniform here, but that can change!

# Just Monika
image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.png")

image monika 1a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 1b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 1c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 1d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 1e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 1f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 1g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 1h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 1i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 1n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 1o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 1p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 2a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 2b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 2c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 2d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 2e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 2f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 2g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 2h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 2i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 2n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 2o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 2p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 3a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 3b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 3c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 3d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 3e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 3f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 3g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 3h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 3i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 3n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 3o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 3p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 4a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 4b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 4c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 4d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 4e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 4f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 4g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 4h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 4i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 4n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 4o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 4p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 5a = im.Composite((960, 960), (0, 0), "monika/3a.png")
image monika 5b = im.Composite((960, 960), (0, 0), "monika/3b.png")

image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

### CPG Yuri definitions ###
#Sonic related definitions
image honey djHoney = "mod_assets/EDMSessionRevamped/djSona.png" #EDM Session Revamped, DJ Sona
image neometal djNeo = "mod_assets/EDMSessionRevamped/djNeoMetal.png" #EDM Session Revamped
image infinite infinite0 = "mod_assets/infinite0.png"
image infinite infinite1 = "mod_assets/infinite1.png"
image infinite infinite2 = "mod_assets/infinite2.png"
image infinite infinite3 = "mod_assets/infinite3.png"
image infinite infinite4 = "mod_assets/infinite4.png"
image infinite infinite5 = "mod_assets/infinite5.png"
image infinite infinite6 = "mod_assets/infinite6.png"
image infinite infinite7 = "mod_assets/infinite7.png"
image avatar avatarMale = "mod_assets/avatarMale.png"
image avatar avatarFemale = "mod_assets/avatarFemale.png"
image amy amyCom = "mod_assets/amyCom.png"
image amy amy00 = "mod_assets/amy00.png"
image amy amy01 = "mod_assets/amy01.png"
image amy amy02 = "mod_assets/amy02.png"
image amy amy03 = "mod_assets/amy03.png"
image amy amy04 = "mod_assets/amy04.png"
image amy amy05 = "mod_assets/amy05.png"
image amy amy06 = "mod_assets/amy06.png"
image amy amy07 = "mod_assets/amy07.png"
image amy amy08 = "mod_assets/amy08.png"
image amy amy09 = "mod_assets/amy09.png"
image amy amy10 = "mod_assets/amy10.png"
image amy amyGlitch = "mod_assets/amyGlitch.png"
image eggman eggman00 = "mod_assets/eggman00.png"
image eggman eggman01 = "mod_assets/eggman01.png"
image eggman eggman02 = "mod_assets/eggman02.png"
image eggman eggman03 = "mod_assets/eggman03.png"
image eggman eggman04 = "mod_assets/eggman04.png"
image eggman eggman05 = "mod_assets/eggman05.png"
image eggman eggman06 = "mod_assets/eggman06.png"
image eggman eggman07 = "mod_assets/eggman07.png"
image knuckles knucklesCom = "mod_assets/knucklesCom.png"
image knuckles knuckles00 = "mod_assets/knuckles00.png"
image knuckles knuckles01 = "mod_assets/knuckles01.png"
image knuckles knuckles02 = "mod_assets/knuckles02.png"
image knuckles knuckles03 = "mod_assets/knuckles03.png"
image knuckles knuckles04 = "mod_assets/knuckles04.png"
image knuckles knuckles05 = "mod_assets/knuckles05.png"
image knuckles knuckles06 = "mod_assets/knuckles06.png"
image knuckles knucklesGlitch = "mod_assets/knucklesGlitch.png"
image sonic sonic00 = "mod_assets/sonic00.png"
image sonic sonic01 = "mod_assets/sonic01.png"
image sonic sonic02 = "mod_assets/sonic02.png"
image sonic sonic03 = "mod_assets/sonic03.png"
image sonic sonic04 = "mod_assets/sonic04.png"
image sonic sonic05 = "mod_assets/sonic05.png"
image sonic sonic06 = "mod_assets/sonic06.png"
image sonic sonic07 = "mod_assets/sonic07.png"
image sonic sonic08 = "mod_assets/sonic08.png"
image sonic sonic09 = "mod_assets/sonic09.png"
image sonic sonic10 = "mod_assets/sonic10.png"
image sonic sonic11 = "mod_assets/sonic11.png"
image sonic sonic12 = "mod_assets/sonic12.png"
image sonic sonic13 = "mod_assets/sonic13.png"
image sonic sonic14 = "mod_assets/sonic14.png"
image sonic sonic15 = "mod_assets/sonic15.png"
image sonic sonicglitch1 = "mod_assets/sonicglitch1.png"
image sonic sonicglitch2 = "mod_assets/sonicglitch2.png"
image sonic sonicEXE = "mod_assets/exeller01.png"
image exeller exeller01 = "mod_assets/exeller01.png"
image exeller exeller02 = "mod_assets/exeller02.png"
image exeller exeller03 = "mod_assets/exeller03.png"
image exeller exeller04 = "mod_assets/exeller04.png"
image exeller exeller05 = "mod_assets/exeller05.png"
image exeller exeller06 = "mod_assets/exeller06.png"
image exeller exeller07 = "mod_assets/exeller07.png"
image tails tailsCom = "mod_assets/tailsCom.png"
image tails tails00 = "mod_assets/tails00.png"
image tails tails01 = "mod_assets/tails01.png"
image tails tails02 = "mod_assets/tails02.png"
image tails tails03 = "mod_assets/tails03.png"
image tails tails04 = "mod_assets/tails04.png"
image tails tails05 = "mod_assets/tails05.png"
image tails tails06 = "mod_assets/tails06.png"
image tails tails07 = "mod_assets/tails07.png"
image tails tails08 = "mod_assets/tails08.png"
image tails tailsGlitch = "mod_assets/tailsGlitch.png"
image monitors invincible = "mod_assets/invincibilityMonitor.png"
image eggpawn eggpawn1 = "mod_assets/EggPawn.png"
image eggpawn2 eggpawn2 = "mod_assets/EggPawn2.png"
image eggpawn3 eggpawn3 = "mod_assets/EggPawn4.png"
image eggrobo eggrobo = "mod_assets/EggRobo.png"
image boss1 queenBomber = "mod_assets/queenBomber.png"
image boss2 metalMonika = "mod_assets/metalMonika.png"
image boss3 metalNatsuki = "mod_assets/metalNatsuki.png"
image boss4 heavyMagician = "mod_assets/heavyMagician.png"
image boss5 heavyGunner = "mod_assets/heavyGunner.png"
image boss6 heavyKing = "mod_assets/heavyKing.png"
image metal metal00 = "mod_assets/metal00.png"
image metal metal01 = "mod_assets/metal01.png"
image pictures futureStarpost = "mod_assets/futurePost.png"
image pictures starPost = "mod_assets/starPost.png"
image pictures prisonegg = "mod_assets/prisonEgg.png"
image shadow shadow00 = "mod_assets/shadow00.png"
image shadow shadow01 = "mod_assets/shadow01.png"
image shadow shadow02 = "mod_assets/shadow02.png"
image shadow shadow03 = "mod_assets/shadow03.png"
image shadow shadow04 = "mod_assets/shadow04.png"
image shadow shadow05 = "mod_assets/shadow05.png"
image shadow shadow06 = "mod_assets/shadow06.png"
image shadow shadow07 = "mod_assets/shadow07.png"
image shadow shadowGlitch = "mod_assets/shadowGlitch.png"

image pictures yuriXnatsu = "mod_assets/YuriXNatsu.png"

#IT'S ME, PIECE OF SHIT, GHOSTSUKI!!!
image ghostnatsuki gNatsu1 = Image("mod_assets/ghost/ghost1.png")#Standard grin Ghost
image ghostnatsuki gNatsu2 = Image("mod_assets/ghost/ghost2.png")#Neck snap!
image ghostnatsuki gNatsu3 = Image("mod_assets/ghost/ghost3.png")#Left hand on hip
image ghostnatsuki gNatsu4 = Image("mod_assets/ghost/ghost4.png")#Right hand on hip
image ghostnatsuki gNatsu5 = Image("mod_assets/ghost/ghost5.png")#Hands on hips
image ghostnatsuki gNatsu6 = Image("mod_assets/ghost/ghost6.png")#Cute fang Ghost
image ghostnatsuki gNatsu7 = Image("mod_assets/ghost/ghost7.png")#Scared Ghost
image ghostnatsuki gNatsu8 = Image("mod_assets/ghost/ghost8.png")#Ashamed Ghost
image ghostnatsuki gNatsu9 = Image("mod_assets/ghost/ghost9.png")#Sad Ghost
image ghostnatsuki gNatsu10 = Image("mod_assets/ghost/ghost10.png")#Concerned Ghost
image ghostnatsuki gNatsu11 = Image("mod_assets/ghost/ghost11.png")#Proud Ghost
image ghostnatsuki gNatsu12 = Image("mod_assets/ghost/ghost12.png")#Ghost crying blood
image ghostnatsuki gNatsu13 = Image("mod_assets/ghost/ghost13.png")#Ghost with pose 5
image ghostnatsuki gNatsu14 = Image("mod_assets/ghost/ghost14.png")#Unamused Ghost
image ghostnatsuki gCom = "mod_assets/ghostCom.png"
image ghostnatsuki wispon = "mod_assets/ghostWispon.png"

#Chaos Emeralds + Phantom Ruby
image emerald yellow = "mod_assets/chaosEmeraldY.png"
image emerald green = "mod_assets/chaosEmeraldG.png"
image emerald red = "mod_assets/chaosEmeraldR.png"
image emerald blue = "mod_assets/chaosEmeraldB.png"
image emerald turquoise = "mod_assets/chaosEmeraldT.png"
image emerald purple = "mod_assets/chaosEmeraldP.png"
image emerald white = "mod_assets/chaosEmeraldW.png"
image emerald allEmeralds = "mod_assets/chaosEmeraldAll.png"
image emerald phantomRuby = "mod_assets/phantomRuby.png"
image emerald rubyProto = "mod_assets/rubyPrototype.png"

#MIK.EXE
image gfm rexe1 = Image("mod_assets/sayori/MikEXE Death.png")
image gfm rexe2 = Image("mod_assets/sayori/MikEXE Death2.png")
image gfm rexe3 = Image("mod_assets/sayori/MikEXE Rage.png")
image gfm rexe4 = Image("mod_assets/sayori/MikEXE Remember.png")
image gfm rexe5 = Image("mod_assets/sayori/MikEXE Remember2.png")
image gfm rexe6 = Image("mod_assets/sayori/MikEXE Smile.png")
image gfm rexe7 = Image("mod_assets/sayori/MikEXE.png")
image gfm rexe8 = Image("mod_assets/sayori/MikEXE Ecstatic.png")
image gfm rexe9 = Image("mod_assets/sayori/MikEXE Suspicious.png")
image gfm rexe10 = Image("mod_assets/sayori/EliteKrAZyFan Ecstatic.png")
image gfm rexe11 = Image("mod_assets/sayori/EliteKrAZyFan Grin.png")
image gfm rexe12 = Image("mod_assets/sayori/EliteKrAZyFan.png")
image wings wingRed = Image("mod_assets/sayori/wings_exe.png")

#Special Portals
image portal genesisportal = "mod_assets/genesisPortal.png"
image pictures crashfeveregg = "mod_assets/crashfeverEgg.png"
image cookies cookieSprite = "mod_assets/COOKIES.png"
image oneterm termSprite = "mod_assets/OneTerm.png"
image oneterm termUWASprite = "mod_assets/OneTermUwa.png"
image oneterm termHappySprite = "mod_assets/OneTermHappy.png"
image serg sergSprite = "mod_assets/Sergmanny.png"
image skull skullSprite = "mod_assets/SKULL.png"
image cookies ncookieSprite = night(im.Composite((960, 960), (0, 0), "mod_assets/COOKIES.png"))
image oneterm ntermSprite = night(im.Composite((960, 960), (0, 0), "mod_assets/OneTerm.png"))
image oneterm ntermUWASprite = night(im.Composite((960, 960), (0, 0), "mod_assets/OneTermUwa.png"))
image oneterm ntermHappySprite = night(im.Composite((960, 960), (0, 0), "mod_assets/OneTermHappy.png"))
image serg nsergSprite = night(im.Composite((960, 960), (0, 0), "mod_assets/Sergmanny.png"))
image skull nskullSprite = night(im.Composite((960, 960), (0, 0), "mod_assets/SKULL.png"))
image miku mikuSprite = "mod_assets/pureSongstressMiku.png"
image scp scpLizard682 = "mod_assets/lizard.png"
image philoso philoSprite = "mod_assets/Philosoraptor.png"
image philoso nphiloSprite = night(im.Composite((960, 960), (0, 0), "mod_assets/Philosoraptor.png"))
image him chara = "mod_assets/chara.png"
image him mchara = morning(im.Composite((960, 960), (0, 0), "mod_assets/chara.png"))
image him chara2 = "mod_assets/chara2.png"
image him mchara2 = morning(im.Composite((960, 960), (0, 0), "mod_assets/chara2.png"))
image him frisk = "mod_assets/frisk.png"
image him mfrisk = morning(im.Composite((960, 960), (0, 0), "mod_assets/frisk.png"))

image glitch illusionMonika = "mod_assets/illusionMonika.png"
image glitch sayoriGhost = "mod_assets/s_ghost.png"
image glitch sayoriRed = "mod_assets/s_red.png"
image tsun 8yu = Image("mod_assets/8yu.png")

image n_glitch_head:
    "mod_assets/zan.png"
    0.15
    "mod_assets/zbn.png"
    0.15
    "mod_assets/zcn.png"
    0.15
    "mod_assets/zdn.png"
    0.15
    repeat

image m_glitch_head:
    "mod_assets/zam.png"
    0.15
    "mod_assets/zbm.png"
    0.15
    "mod_assets/zcm.png"
    0.15
    "mod_assets/zdm.png"
    0.15
    repeat

image s_glitch_head:
    "mod_assets/zas.png"
    0.15
    "mod_assets/zbs.png"
    0.15
    "mod_assets/zcs.png"
    0.15
    "mod_assets/zds.png"
    0.15
    repeat

image t_glitch_head:
    "mod_assets/zat.png"
    0.15
    "mod_assets/zbt.png"
    0.15
    "mod_assets/zct.png"
    0.15
    "mod_assets/zdt.png"
    0.15
    repeat

#DDLC-MC
image mc2 1 = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/a.png")
image mc2 1a = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/a.png")
image mc2 1b = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/b.png")
image mc2 1c = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/c.png")
image mc2 1d = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/d.png")
image mc2 1e = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/e.png")
image mc2 1f = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/f.png")
image mc2 1g = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/g.png")
image mc2 1h = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/h.png")
image mc2 1i = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/i.png")
image mc2 1j = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/j.png")
image mc2 1k = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/k.png")
image mc2 1l = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/l.png")
image mc2 1m = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/m.png")
image mc2 1n = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/n.png")
image mc2 1o = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/o.png")
image mc2 1p = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/p.png")
image mc2 1q = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/q.png")
image mc2 1r = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/r.png")
image mc2 1s = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/s.png")
image mc2 1t = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/t.png")
image mc2 1u = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/u.png")
image mc2 1v = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/v.png")
image mc2 1w = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/w.png")
image mc2 1x = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/x.png")
image mc2 1y = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/y.png")
image mc2 1z = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/z.png")
image mc2 1error = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/error.png")
image mc2 1error1 = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/error1.png")
image mc2 1shock = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/shock.png")

image mc2 2 = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/a.png")
image mc2 2a = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/a.png")
image mc2 2b = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/b.png")
image mc2 2c = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/c.png")
image mc2 2d = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/d.png")
image mc2 2e = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/e.png")
image mc2 2f = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/f.png")
image mc2 2g = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/g.png")
image mc2 2h = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/h.png")
image mc2 2i = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/i.png")
image mc2 2j = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/j.png")
image mc2 2k = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/k.png")
image mc2 2l = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/l.png")
image mc2 2m = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/m.png")
image mc2 2n = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/n.png")
image mc2 2o = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/o.png")
image mc2 2p = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/p.png")
image mc2 2q = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/q.png")
image mc2 2r = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/r.png")
image mc2 2s = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/s.png")
image mc2 2t = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/t.png")
image mc2 2u = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/u.png")
image mc2 2v = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/v.png")
image mc2 2w = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/w.png")
image mc2 2x = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/x.png")
image mc2 2y = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/y.png")
image mc2 2z = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/z.png")
image mc2 2error = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/error.png")
image mc2 2error1 = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/error1.png")
image mc2 2shock = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/shock.png")

image mc2 3 = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/a.png")
image mc2 3a = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/a.png")
image mc2 3b = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/b.png")
image mc2 3c = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/c.png")
image mc2 3d = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/d.png")
image mc2 3e = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/e.png")
image mc2 3f = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/f.png")
image mc2 3g = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/g.png")
image mc2 3h = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/h.png")
image mc2 3i = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/i.png")
image mc2 3j = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/j.png")
image mc2 3k = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/k.png")
image mc2 3l = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/l.png")
image mc2 3m = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/m.png")
image mc2 3n = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/n.png")
image mc2 3o = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/o.png")
image mc2 3p = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/p.png")
image mc2 3q = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/q.png")
image mc2 3r = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/r.png")
image mc2 3s = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/s.png")
image mc2 3t = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/t.png")
image mc2 3u = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/u.png")
image mc2 3v = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/v.png")
image mc2 3w = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/w.png")
image mc2 3x = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/x.png")
image mc2 3y = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/y.png")
image mc2 3z = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/z.png")
image mc2 3error = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/error.png")
image mc2 3error1 = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/error1.png")
image mc2 3shock = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/shock.png")

image mc2 4 = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/a.png")
image mc2 4a = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/a.png")
image mc2 4b = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/b.png")
image mc2 4c = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/c.png")
image mc2 4d = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/d.png")
image mc2 4e = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/e.png")
image mc2 4f = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/f.png")
image mc2 4g = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/g.png")
image mc2 4h = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/h.png")
image mc2 4i = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/i.png")
image mc2 4j = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/j.png")
image mc2 4k = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/k.png")
image mc2 4l = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/l.png")
image mc2 4m = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/m.png")
image mc2 4n = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/n.png")
image mc2 4o = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/o.png")
image mc2 4p = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/p.png")
image mc2 4q = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/q.png")
image mc2 4r = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/r.png")
image mc2 4s = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/s.png")
image mc2 4t = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/t.png")
image mc2 4u = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/u.png")
image mc2 4v = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/v.png")
image mc2 4w = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/w.png")
image mc2 4x = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/x.png")
image mc2 4y = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/y.png")
image mc2 4z = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/z.png")
image mc2 4error = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/error.png")
image mc2 4error1 = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/error1.png")
image mc2 4shock = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/shock.png")

image mc2 5 = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/a.png")
image mc2 5a = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/a.png")
image mc2 5b = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/b.png")
image mc2 5c = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/c.png")
image mc2 5d = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/d.png")
image mc2 5e = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/e.png")
image mc2 5f = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/f.png")
image mc2 5g = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/g.png")
image mc2 5h = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/h.png")
image mc2 5i = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/i.png")
image mc2 5j = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/j.png")
image mc2 5k = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/k.png")
image mc2 5l = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/l.png")
image mc2 5m = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/m.png")
image mc2 5n = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/n.png")
image mc2 5o = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/o.png")
image mc2 5p = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/p.png")
image mc2 5q = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/q.png")
image mc2 5r = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/r.png")
image mc2 5s = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/s.png")
image mc2 5t = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/t.png")
image mc2 5u = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/u.png")
image mc2 5v = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/v.png")
image mc2 5w = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/w.png")
image mc2 5x = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/x.png")
image mc2 5y = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/y.png")
image mc2 5z = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/z.png")
image mc2 5error = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/error.png")
image mc2 5error1 = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/error1.png")
image mc2 5shock = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/shock.png")

image mc2_glitch: #MC GLITCH SPRITE
    choice:
        "mod_assets/mc/old/1.png"
    choice:
        "mod_assets/mc/old/2.png"
    choice:
        "mod_assets/mc/old/3.png"
    choice:
        "mod_assets/mc/old/4.png"
    choice:
        "mod_assets/mc/old/5.png"
    0.15
    repeat

image mc2 orb = Image("mod_assets/mc-femc_orb.png")

#DDLC-FeMC
image femc lh_1 = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/a.png")
image femc lh_1a = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/a.png")
image femc lh_1b = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/b.png")
image femc lh_1c = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/c.png")
image femc lh_1d = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/d.png")
image femc lh_1e = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/e.png")
image femc lh_1f = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/f.png")
image femc lh_1g = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/g.png")
image femc lh_1h = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/h.png")
image femc lh_1i = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/i.png")
image femc lh_1j = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/j.png")
image femc lh_1k = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/k.png")
image femc lh_1l = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/l.png")
image femc lh_1m = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/m.png")
image femc lh_1n = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/n.png")
image femc lh_1o = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/o.png")
image femc lh_1p = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/p.png")
image femc lh_1q = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/q.png")
image femc lh_1r = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/r.png")
image femc lh_1s = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/s.png")
image femc lh_1t = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/t.png")
image femc lh_1u = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/u.png")
image femc lh_1v = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/v.png")
image femc lh_1w = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/w.png")
image femc lh_1x = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/x.png")
image femc lh_1y = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/y.png")
image femc lh_1z = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/z.png")
image femc lh_1g1 = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/glitch1.png")
image femc lh_1g2 = im.Composite((960, 960), (0, 0), "mod_assets/femc/1l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/glitch2.png")

image femc lh_2 = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/a.png")
image femc lh_2a = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/a.png")
image femc lh_2b = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/b.png")
image femc lh_2c = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/c.png")
image femc lh_2d = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/d.png")
image femc lh_2e = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/e.png")
image femc lh_2f = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/f.png")
image femc lh_2g = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/g.png")
image femc lh_2h = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/h.png")
image femc lh_2i = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/i.png")
image femc lh_2j = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/j.png")
image femc lh_2k = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/k.png")
image femc lh_2l = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/l.png")
image femc lh_2m = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/m.png")
image femc lh_2n = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/n.png")
image femc lh_2o = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/o.png")
image femc lh_2p = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/p.png")
image femc lh_2q = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/q.png")
image femc lh_2r = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/r.png")
image femc lh_2s = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/s.png")
image femc lh_2t = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/t.png")
image femc lh_2u = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/u.png")
image femc lh_2v = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/v.png")
image femc lh_2w = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/w.png")
image femc lh_2x = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/x.png")
image femc lh_2y = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/y.png")
image femc lh_2z = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/z.png")
image femc lh_2g1 = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/glitch1.png")
image femc lh_2g2 = im.Composite((960, 960), (0, 0), "mod_assets/femc/2l.png", (0, 0), "mod_assets/femc/1r.png", (0, 0), "mod_assets/femc/glitch2.png")

image femc lh_3 = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/a.png")
image femc lh_3a = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/a.png")
image femc lh_3b = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/b.png")
image femc lh_3c = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/c.png")
image femc lh_3d = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/d.png")
image femc lh_3e = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/e.png")
image femc lh_3f = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/f.png")
image femc lh_3g = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/g.png")
image femc lh_3h = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/h.png")
image femc lh_3i = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/i.png")
image femc lh_3j = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/j.png")
image femc lh_3k = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/k.png")
image femc lh_3l = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/l.png")
image femc lh_3m = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/m.png")
image femc lh_3n = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/n.png")
image femc lh_3o = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/o.png")
image femc lh_3p = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/p.png")
image femc lh_3q = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/q.png")
image femc lh_3r = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/r.png")
image femc lh_3s = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/s.png")
image femc lh_3t = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/t.png")
image femc lh_3u = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/u.png")
image femc lh_3v = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/v.png")
image femc lh_3w = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/w.png")
image femc lh_3x = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/x.png")
image femc lh_3y = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/y.png")
image femc lh_3z = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/z.png")
image femc lh_3g1 = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/glitch1.png")
image femc lh_3g2 = im.Composite((960, 960), (0, 0), "mod_assets/femc/3.png", (0, 0), "mod_assets/femc/glitch2.png")

image femc orb = Image("mod_assets/mc-femc_orb.png")

###### Character Variables ######
# These configure the shortcuts for writing dialog for each character.
define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define mc2 = DynamicCharacter('mc2_name', image='mc2', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define femc = DynamicCharacter('femc_name', image='femc', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define dj = DynamicCharacter('dj_name', image='honey', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define inf = DynamicCharacter('inf_name', image='infinite', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define mtp = DynamicCharacter('mtp_name', image='tails', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define amyR = DynamicCharacter('amyR_name', image='amy', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define egg = DynamicCharacter('egg_name', image='eggman', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define kte = DynamicCharacter('kte_name', image='knuckles', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define sth = DynamicCharacter('sth_name', image='sonic', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define exe = DynamicCharacter('exe_name', image='exeller', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define g = DynamicCharacter('g_name', image='ghostnatsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define met = DynamicCharacter('met_name', image='metal', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define coo = DynamicCharacter('coo_name', image='cookies', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define onT = DynamicCharacter('onT_name', image='oneterm', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ser = DynamicCharacter('ser_name', image='serg', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define skl = DynamicCharacter('skl_name', image='skull', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define phil = DynamicCharacter('phil_name', image='skull', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define mik = DynamicCharacter('mik_name', image='miku', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define mik2 = DynamicCharacter('gfm_name', image='gfm', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define liz = DynamicCharacter('liz_name', image='scp', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define him = DynamicCharacter('him_name', image='him', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define sha = DynamicCharacter('sha_name', image='shadow', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define krazy = DynamicCharacter('t_name', image='tsun', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define syka = DynamicCharacter('syka_name', image='syka', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define char = DynamicCharacter('chara_name', image='chara', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define sil = DynamicCharacter('silver_name', image='silver', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define tsun = DynamicCharacter('t_name', image='tsun', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define vi = DynamicCharacter('violet_name', image='violet', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define mio = DynamicCharacter('mio_name', image='mio', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define nsth = Character('Nat & Sonic', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define nT = Character('Nat & Term', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define _dismiss_pause = config.developer

###### Persistent Variables ######
# These values are automatically loaded/saved on game start and exit.
# These exist across all saves

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 2
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.genderMale = False
default persistent.yuriKnife = False
default persistent.sonicMania = False
default persistent.edmfiles_flag = None
default persistent.packagedMusic = False
default persistent.seenPrologue = False
default persistent.ringCount = 0
default persistent.emeraldCount = 0
default persistent.sayori_kill = False
default persistent.sayori_helped = False
default persistent.yuriRoute = False
default persistent.ddlc_femc = None #True= FeMC, False= MC
default persistent.waifuclubegg = None 
default persistent.tsun_unlocked = None
default persistent.violet_unlocked = None
default persistent.chara_unlocked = None
default persistent.sayonika_unlocked = None
default persistent.mio_unlocked = None
default persistent.silver_unlocked = None

###### Other global variables ######
# It's good practice to define global variables here, just so you know what you can call later

default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None
default enterPortal = False
default portalName = ""
default chapter3decision = ""
default mikEXESurprise = False
default mikEXEPoemChapter = 0
default flag = 0

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"
default dj_name = "DJ Sona"
default inf_name = "Infinite"
default mtp_name = "Tails"
default amyR_name = "Amy"
default egg_name = "Dr Eggman"
default kte_name = "Knuckles"
default sth_name = "Sonic"
default g_name = "Ghost"
default mc2_name = "MC"
default femc_name = "FeMC"
default met_name = "Metal-Sonic"
default exe_name = "Exeller"
default coo_name = "Cookies"
default onT_name = "OneTerm"
default ser_name = "Serg"
default skl_name = "Skull"
default mik_name = "Miku"
default gfm_name = "Mik.Exe"
default liz_name = "SCP-682"
default phil_name = "Philosoraptor"
default him_name = "Chara"
default sha_name = "Shadow"
default t_name = "TsunKrAZy"
default syka_name = "Sayonika"
default chara_name = "Chara"
default silver_name = "Silver"
default violet_name = "Violet"
default mio_name = "Mio"

# Instantiating variables for poem appeal. This is how much each character likes the poem for each day.
# -1 = Dislike, 0 = Neutral, 1 = Like
default n_poemappeal = [0, 0, 0, 0, 0, 0]
default s_poemappeal = [0, 0, 0, 0, 0, 0]
default y_poemappeal = [0, 0, 0, 0, 0, 0]
default m_poemappeal = [0, 0, 0, 0, 0, 0]

# The last winner of the poem minigame.
default poemwinner = ['sayori', 'sayori', 'sayori', 'sayori', 'sayori', 'sayori']

# Keeping track of who read your poem when you're showing it to each of the girls.
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

# Used in poemresponse_start because it's easier than checking true/false on everyone's read state.
default poemsread = 0

# The main appeal points. Whoever likes your poem the most gets an appeal point for that chapter.
# Appeal points are used to keep track of which exclusive scene to show each chapter.
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

# We keep track of whether we watched Natsuki's and sayori's second exclusive scenes
# to decide whether to play them in chapter 3.
default n_exclusivewatched = False
default y_exclusivewatched = False

# Yuri runs away after the first exclusive scene of playthrough 2.
default y_gave = False
default y_ranaway = False

# We choose who to side with in chapter 1.
default ch1_choice = "sayori"

# If we choose to help Sayori in ch3, some of the dialogue changes.
default help_sayori = None
default help_monika = None

# We choose who to spend time with in chapter 4.
default ch4_scene = "yuri"
default ch4_name = "Yuri"
default sayori_confess = True

# We read Natsuki's confession poem in chapter 23.
default natsuki_23 = None

#paste this at the end of your definitions.rpy
label rain: #use "call rain" to start the rain with a 5 seconds fade
    play ambient rain fadein 5.0
    show rain zorder 5 with Dissolve(5.0)
    return

label instant_rain: #use "call instant_rain" to start the rain immediately
    play ambient rain
    show rain zorder 5
    return

label rain_stop: #use call rain_stop to stop the rain with a 5 seconds fade
    stop ambient fadeout 5.0
    hide rain with Dissolve(5.0)
    return

label instant_rain_stop: #use call instant_rain_stop to stop the rain immediately
    stop ambient fadeout 5.0
    hide rain with Dissolve(5.0)
    return

# label cinnamonOrb:
#     $ currentsong = renpy.music.get_playing(channel='music')
#     stop music fadeout 2.0
#     show sayoricolor zorder 90:
#         alpha 0.0
#         easein 4.0 alpha 0.5
#     show sayori orb at t11 zorder 91
#     "Oh! What is this...? I feel like if the time has stopped."
#     "An strange orb appeared in front of me. I can't remember which person this orb represents, but it feels calm..."
#     "...like a childhood friend... I think that is very appropiate for me to keep this orb and see what it unlocks."
#     show sayori at thide zorder 1
#     hide sayori
#     hide sayoricolor
#     return
