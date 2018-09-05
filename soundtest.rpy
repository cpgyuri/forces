#label audiotesting:
                
init python:

    items = [(_("Enable/Disable EDM Session"),"edmsession")
        ,(_("Angel Island Intro"),"angelisland")
        ,(_("Menu Theme"),"menutheme")
        ,(_("Infinite's Theme"),"infinite")
        ,(_("Null Space - I Still Love You (DDLC)"),"nullspace")
        ,(_("Save the Dokis!"),"savedokis")
        ,(_("MILESPoem.exe"),"milespoem")
        ,(_("ŔŗñĮ¼»ŧþŀÂŻŕěōì«"),"mik")
        ,(_("Poem Panic (DDLC)"),"panic")
        ,(_("Play with Me (DDLC)"),"playwithme")
        ,(_("Green Hill"),"greenhill")
        ,(_("Ghost Natsuki's Theme"),"ghostnatsuki")
        ,(_("Sayonara (DDLC)"),"noose")
        ,(_("My Feelings (DDLC)"),"feelings")
        ,(_("Chemical Plant 1"),"chemicalplant1")
        ,(_("Chemical Plant 2 (Prison)"),"prison")
        ,(_("Queen Buzz Bomber"),"queenboss")
        ,(_("Metal Trashy's Theme"),"metaltrashy")
        ,(_("Sonic's Theme"),"sonic")
        ,(_("Studiopolis 1"),"studiopolis1")
        ,(_("Studiopolis 2"),"studiopolis2")
        ,(_("Monika's Weather Machine (Sonic Mania mod)"),"sonicmania")
        ,(_("VS Metal Trashy"),"metaltrashy2")
        ,(_("Flying Battery"),"flyingbattery")
        ,(_("Press Garden"),"pressgarden")
        ,(_("Dr. Eggman's Theme"),"eggman")
        ,(_("Stardust Speedway (Past)"),"stardust1")
        ,(_("Stardust Speedway (Present)"),"stardust2")
        ,(_("VS Metal Sonic"),"metalsonic")
        ,(_("Metal Sayori"),"metalsayori")
        ,(_("Save Sayori! / Vs. Metal Sayori"),"vssayori")
        ,(_("Hydrocity"),"hidrocity")
        ,(_("Monika's Portal: Miku Crash Fever"),"miku")
        ,(_("Natsuki's Portal: DDLC Modders Paradise"),"sexyserg")
        ,(_("Ghost's Portal: SCP-682 The Hard to Destroy Reptile"),"scp682")
        ,(_("Yuri's Portal: FIGHT HIM"),"chara")
        ,(_("Yuri's Portal: DETERMINATION."),"frisk")
        ,(_("My Confession (DDLC)"),"confession")
        ,(_("Mirage Saloon"),"saloon")
        ,(_("Heavy Magician Theme"),"magician")
        ,(_("Shadow Appears! (All Hail Shadow!)"),"shadow")
        ,(_("Sayori's SOUL Song"),"fairplay")
        ,(_("Oil Ocean 1"),"ocean1")
        ,(_("Oil Ocean 2"),"ocean2")
        ,(_("Submarine Illussion"),"illusion")
        ,(_("Yuri's Last Stand - OctiBoss"),"octiboss")
        ,(_("Lava Reef"),"lava")
        ,(_("Yuri x Natsuki Dance"),"yurinatsu")
        ,(_("Yuri's Evil Feelings (DDLC)"),"yuripls")
        ,(_("Yuri's Theme"),"yuriroute")
        ,(_("Yuri's Final Boss"),"finalboss")]

    import subprocess
    import os
    process_list = []
    if renpy.windows:
        try:
            process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
        except:
            pass
        try:
            renpy.file("../mod_assets/EDMSessionRevamped/angelIslandPCKG.ogg")
        except:
            persistent.edmfiles_flag = True

label edmsession:
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe", "camrecorder.exe", "eescreen.exe"]
    if persistent.edmfiles_flag:
        $ persistent.packagedMusic = False
    elif list(set(process_list).intersection(stream_list)):
        $ persistent.packagedMusic = False
    else:
        if persistent.packagedMusic == True:
            $ persistent.packagedMusic = False
        else:
            $ persistent.packagedMusic = True
    jump musictest#audiotesting

label angelisland:
    if persistent.packagedMusic == True:
        play music aizPCKG
    else:
        play music aiz
    jump musictest#audiotesting

label menutheme:
    if persistent.ghost_menu == True:
        play music specialMenu
    else:
        play music forces
    jump musictest#audiotesting

label infinite:
    if persistent.packagedMusic == False:
        play music infiniteMusic
    else:
        play music infiniteJoke
    jump musictest#audiotesting

label nullspace:
    play music mend
    jump musictest#audiotesting

label savedokis:
    play music rWispon
    jump musictest#audiotesting

label milespoem:
    if persistent.packagedMusic == True:
        play music rPoemPCKG
    else:
        play music rPoem
    jump musictest#audiotesting

label mik:
    play music herWorld
    $ mikEXESurprise = True
    jump musictest#audiotesting

label panic:
    play music t7
    jump musictest#audiotesting

label playwithme:
    play music t6
    jump musictest#audiotesting

label greenhill:
    if persistent.packagedMusic == True:
        play music greenHillPCKG
    else:
        play music greenHillZ1
    jump musictest#audiotesting

label ghostnatsuki:
    if persistent.packagedMusic == True:
        play music ghostNPCKG
    else:
        play music ghostNatsuki
    jump musictest#audiotesting

label noose:
    play music td
    jump musictest#audiotesting

label feelings:
    play music t9
    jump musictest#audiotesting

label chemicalplant1:
    if persistent.packagedMusic == True:
        play music chemPlantPCKG
    else:
        play music chemPlant1
    jump musictest#audiotesting

label prison:
    if persistent.packagedMusic == False:
        play music chemPlant2
    else:
        play music chemPlantPCKG
    jump musictest#audiotesting

label queenboss:
    play music bossQueen
    jump musictest#audiotesting

label metaltrashy:
    if persistent.packagedMusic == True:
        play music jokePCKG
    else:
        play music metalDokis
    jump musictest#audiotesting

label sonic:
    play music sonicTheme
    jump musictest#audiotesting

label studiopolis1:
    if persistent.packagedMusic == True:
        play music studioPCKG1
    else:
        play music studioP1
    jump musictest#audiotesting

label studiopolis2:
    if persistent.packagedMusic == True:
        play music studioPCKG1
    else:
        play music studioP2
    jump musictest#audiotesting

label sonicmania:
    play music monikaSong
    jump musictest#audiotesting

label metaltrashy2:
    if persistent.packagedMusic == True:
        play music metalDokisPCKG
    else:
        play music metalDokis
    jump musictest#audiotesting

label flyingbattery:
    if persistent.packagedMusic == True:
        play music fBatteryPCKG
    else:
        play music fBattery
    jump musictest#audiotesting

label pressgarden:
    if persistent.packagedMusic == True:
        play music pulpSolstice
    else:
        play music pressGarden1
    jump musictest#audiotesting

label eggman:
    if persistent.packagedMusic == True:
        play music eggmanPCKG
    else:
        play music eggmanMusic
    jump musictest#audiotesting

label stardust1:
    if persistent.packagedMusic == True:
        play music muffledStardust
    else:
        play music stardust
    jump musictest#audiotesting

label stardust2:
    if persistent.packagedMusic == True:
        play music speedwayPCKG
    else:
        play music stardust2
    jump musictest#audiotesting

label metalsonic:
    if persistent.packagedMusic == True:
        play music vsMetalPCKG
    else:
        play music vsMetal
    jump musictest#audiotesting

label metalsayori:
    play music metalSayori
    jump musictest#audiotesting

label vssayori:
    play music vsSayori
    jump musictest#audiotesting

label hidrocity:
    if persistent.packagedMusic == True:
        play music hidrocityPCKG
    else:
        play music hidrocity
    jump musictest#audiotesting

label miku:
    play music mikuPortal
    jump musictest#audiotesting

label sexyserg:
    play music moddersPortal
    jump musictest#audiotesting

label scp682:
    play music scp682Portal
    jump musictest#audiotesting

label chara:
    play music himMegalovania
    jump musictest#audiotesting

label frisk:
    play music himFrisk
    jump musictest#audiotesting

label confession:
    play music t10
    jump musictest#audiotesting

label saloon:
    if persistent.packagedMusic == True:
        play music mirageSaloonPCKG
    else:
        play music mirageSaloon
    jump musictest#audiotesting

label magician:
    if persistent.packagedMusic == True:
        play music heavyMagicianPCKG
    else:
        play music heavyMagician
    jump musictest#audiotesting

label shadow:
    play music shadowAppears
    jump musictest#audiotesting

label fairplay:
    play music yuriLastStand
    jump musictest#audiotesting

label ocean1:
    if persistent.packagedMusic == True:
        play music oilOcean1PCKG
    else:
        play music oilOcean1
    jump musictest#audiotesting

label ocean2:
    if persistent.packagedMusic == True:
        play music oilOcean2PCKG
    else:
        play music oilOcean2
    jump musictest#audiotesting

label illusion:
    play music pumpedUpMettatons
    jump musictest#audiotesting

label octiboss:
    if persistent.packagedMusic == True:
        play music vsoctibossPCKG
    else:
        play music vsoctiboss
    jump musictest#audiotesting

label lava:
    if persistent.packagedMusic == True:
        play music lavaReefPCKG
    else:
        play music lavaReef
    jump musictest#audiotesting

label yurinatsu:
    play music lovePCKG
    jump musictest#audiotesting

label yuripls:
    play music t10y
    jump musictest#audiotesting

label yuriroute:
    if persistent.packagedMusic == True:
        play music yuriRoutePCKG
    else:
        play music yuriRoute
    jump musictest#audiotesting

label finalboss:
    play music finalBoss
    jump musictest#audiotesting

define adj = ui.adjustment()
define gui.tutorial_button_width = 500
define gui.tutorial_button_height = None
define gui.tutorial_button_tile = False
define gui.tutorial_button_borders = Borders(25, 5, 25, 5)
define gui.tutorial_button_text_font = gui.default_font
define gui.tutorial_button_text_size = gui.text_size
define gui.tutorial_button_text_xalign = 0.0
define gui.tutorial_button_text_idle_color = "#ffffff"#"#000"
define gui.tutorial_button_text_hover_color = "#ffff00"#"#fa9"
style tutorial_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing 5

style tutorial_button is default:
    properties gui.button_properties("tutorial_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style tutorial_button_text is default:
    properties gui.button_text_properties("tutorial_button")
    outlines []

screen soundoptions(items):
        fixed:

            area (125, 40, 600, 450)

            bar adjustment adj style "vscrollbar" xalign -0.05

            viewport:
                yadjustment adj
                mousewheel True

                vbox:

                    for i_caption,i_label in items:
                        textbutton i_caption:
                            action Return(i_label)

                    null height 20

                    textbutton _("Back to Main Menu") action Return(False)

label musictest:
    hide screen main_menu
    #stop music fadeout 2.0
    if mikEXESurprise == True:
        scene bg soundTestc
        $ mikEXESurprise = False
    elif persistent.packagedMusic == False:
        scene bg soundTest
    else:
        scene bg soundTestb
    #play music soundTestM
    with dissolve_scene_full
    call screen soundoptions(items)
    if _return is False:
        call screen main_menu
    call expression _return from _call_expression
    jump soundoptions
    return