## Bootloader.rpy
# Boot Sequence and Splash Screen Manager
# Author: Name (@username)
# Copyright: (C) 2018

# Standard Boot Screen
label default_boot_screen:
    stop music fadeout 1.0
    scene black with fade
    show alice_os_logomark at truecenter
    show alice_boot_mascot:
        xalign 0.5
        yalign 0.3
    show boot_copyright:
        yalign 1.0
        xalign 0.5
    #Validating GOBFADU Policy Exists
    # if persistent.bootpass != 1:
    #     if renpy.exists("../game/CoreServices/gobfadu/gobfadupolicy/gobfadupolicygobfadu.rpy"):
    #         call Integrity
    #         return
    #     else:
    #         call rsod_boot
    #         #This is where a BIOS HDD/SSD will report DISK BOOT FAILURE or something similar.
    # else:
    #     pass
    $ renpy.pause(5.0)
    return

# OEM Boot Screen (should be called from splashscreen)
# Displays "Powered by AliceOS" text
label oem_boot_screen:
    stop music fadeout 1.0
    scene black with fade
    show powered_by_text:
        xalign 0.3
        yalign 0.4
    show ddf_boot_mascot:
        xalign 0.5
        yalign 0.3
    show alice_os_name at truecenter
    show boot_copyright:
        xalign 0.5
        yalign 1.0
    show forces_message:
        xalign 0.5
        yalign 0.8
    #Validating GOBFADU Policy Exists
    # if renpy.exists("../game/CoreServices/gobfadu/gobfadupolicy/gobfadupolicygobfadu.rpy"):
    #     call Integrity
    #     return
    # else:
    #     call rsod_boot
    #     #This is where a BIOS HDD/SSD will report DISK BOOT FAILURE or something similar.
    pause 5.0
    return
