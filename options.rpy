## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = "Doki Doki Forces"
define config.window_title = "Doki Doki Forces"
define _window_subtitle = ""


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "DokiDokiForcesBeta6"


## Text that is placed on the game's about screen. To insert a blank line
## between paragraphs, write \n\n.

define gui.about = _("\n{a=https://discord.gg/vGzQtZs}Join our beloved fans at Doki Doki Forces Discord here!{/a}\nSpecial thanks for emotional support: My beloved one Super Sayori 117 <3, Thespeedyraisin (Sonic Mania Mod), Sergmanny, OneTerm, Skull, Darklyre, Pokefan4200, {a=https://www.reddit.com/r/DDLCMods/}DDLCMods reddit{/a}, {a=https://discord.gg/gdNvXVf}our Holy Yuri Empire Discord server{/a} and {a=https://discord.gg/KHZ2And}DDMC Discord.{/a}\n\nDiscord friends and buddies Special Thanks:\nPepehound: Original fanfic translation.\n6thirthyAM: Final Boss Music.{a=https://soundcloud.com/6thirtyam}Visit his Soundcloud!{/a}\nSuper Sayori 117: Apply proofreadings to the scripts.\nPokefan4200: Proofreading and reviews.\nDarklyre: Proofreading and Ending boss sprites.\nsteveatron9000: Proofreading.\nZeusKrAZy: Sound Test code.\njadebenn: Poem Minigame's hover and new code.\nFL13: Programming and build distribution help.\nkoppien: Programming help and red sprites.\nKoya-Sato: Time of the day codes.\nMAS team: MAS Monika's Room sprites.\nBucket: Monika, Natsuki's poems, Sayori's second poem, Yuri's secret poem.\nTR_18: Sayori's Poem.\nCynthius: Yuri's secret poem.\ngreenbean01: MC sprites.\npaulchartres (CykaDev): DDRC's Yuri Creepy sprite.\nDepressed Lolli: Yuri's Horny CG.\nSudoki: Serg and Cookies sprites.\nAjrm43 and Cakeman: OneTerm sprites.\nSkull: Skull sprite.\nsammamish: Yandere expressions.\nLeoDeCaprio: Metal Sayori's expressions.\nddlcmoddev: Glitchy Monika sprite and Monika room sprites.\ndracodraco100: Mind-Broken Doki Heads.\nEzfi: No face Dokis.\nTsunKrAZy: Insane Natsuki expressions.\nyuri.chr [DDYAS]: Creepy Closet BG.\nYuushi (DDNG+): Sayori sprite\n\nReddit Special Thanks:\nYuri's Final Boss Sprite: Times_Vengeance on Reddit.\nSpecial Poem 4 and Yuri image: YouCantSeeMii on Reddit.\nShadow Monika sprite: MonikaTheModder on Reddit.\nSayori's expressions: DeliRoxe on Reddit.\n\nOther Sprites and Stuff:\nBad future sprites: Nibroc-Rock on Deviantart.\nMC chibi: gyletotherescue on Deviantart.\nDJ Honey sprite: elesis_knight on Deviantart.\nSonic CD's Future Starpost: geibuchan on Tumblr.\nSonic.EXE sprite: Retro-Red on Deviantart.\nSCP-682 sprite: CheezBugerz on Deviantart.\nJerry Stuff (Ro): Pumped Up Kicks with Mettaton's It's Showtime! sound font OGG.\n{a=https://www.youtube.com/watch?v=0x40d3-x8zg}Monika and Sayori glitches (images): AngeloTheAngelo on Youtube.{/a}\n{a=http://agentss.tumblr.com/post/165458336922/an-au-were-custom-character-is-actually-an-evil}Rookie glitch (image): Agentskull on Tumblr.{/a}\nSpringingTraps - Yuri's swapped Natsuki expression.\nSteven-The-GOAT - Sound Test image.\n\nDoki Doki Forces idea, some sprites, backgrounds and programming by CPG Yuri -Nurse Raphaela.\nThis mod is created and distributed according to Team Salvato's IP Guidelines.\n The Sonic the Hedgehog characters, names, backgrounds and music are property of SEGA, Sonic Team, Christian Withehead, Headcannon, Pagoda West Games and Tee Lopes. Some sprites ripped from Sonic Free Riders. Music from Sonic Mania and Sonic Forces, and some commercial music.")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "DokiDokiForces"

## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

if persistent.yuriKnife == True:
    define config.main_menu_music = audio.forces_justyuri
else:
    define config.main_menu_music = audio.forces


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur. Each
## variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = Dissolve(.5)


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 50


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15

default preferences.music_volume = 0.75
default preferences.sfx_volume = 1

## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Generally the same as your build name
## Should always be a literal string and not an expression

define config.save_directory = "Forces"


## Icon
## ########################################################################'

## The icon displayed on the taskbar or dock.

define config.window_icon = "logo.png.ico"

## Custom configs ##############################################################

define config.allow_skipping = True
define config.has_autosave = False
define config.autosave_on_quit = False
define config.autosave_slots = 0
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.image_cache_size = 64
define config.predict_statements = 50
define config.rollback_enabled = config.developer
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"
#define config.gl_resize = False

init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') # em dash
        s = s.replace(' - ', u'\u2014') # em dash
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)

    #config.adjust_view_size = force_integer_multiplier

## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.
## These settings create a set of files suitable for distributing as a mod.

init python:

    ## By default, renpy looks for archive files in the game and common directories
    ## Mac needs to check in the install directory instead.
    #if renpy.mac:



    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory,
    ## "game/**.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    ## This is the archive of data for your mod
    #build.archive(build.name, "all")

    ## These files get put into your data file
    build.package(build.directory_name + "source",'zip','source',description='Source Code Archive')
    build.package(build.directory_name + "Mod",'zip',build.name,description='DDLC Compatible Mod')

    # Declare archives
    build.archive("scripts",build.name)
    build.archive("mod_assets",build.name)
    #build.archive("submods",build.name)

    ##Optionally include a zip file with all source code
    build.classify('**.rpy','source')

    ## These files get put into your data file
    build.classify("game/mod_assets/**","mod_assets")
    #build.classify("game/**.rpy",build.name)
    build.classify("game/**.rpyc","scripts")
    build.classify("game/**.txt","scripts")
    build.classify("game/**.chr","scripts")
    build.classify("README.html",build.name)

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('**.rpa',None)

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    build.documentation('*.md')

    build.include_old_themes = False



## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "..."
