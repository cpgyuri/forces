## Doki Doki Forces Applet
# All the information and notifications that a member of the Resistance must have!
# Author(s): Neil García (@cpgyuri), Miles Tails Prower
# Copyright: (C) 2018

init python:
    class Forces(Applet):
        ## App Manifest
        # Define important information about your app here.
        # This information will be used in places like the
        # Control Center, notification badges, apps menus,
        # and the desktop shell.

        # Provide a short name and a long name for your app.
        short_name = "Forces"
        long_name = "Doki Doki Forces"

        # Provide the author information, version number, and
        # description of your app, as where as the name of the
        # folder that your applet lives in.
        app_dir = "Forces"
        author = "CPG Yuri"
        version = "6.66"
        description = "Receive notifications about your missions, Chaos Emeralds count, your Dokis, and DJ Sona's song names."

        # Define your icons here. They should be located in 
        # your Applet's Resources/icons/ folder
        icons = {
            16: "16.png",
            24: "24.png",
            32: "32.png",
            64: "64.png",
            128: "128.png",
            256: "256.png"
        }

        # Define what permissions your applet will need.
        # See the Applet Manifest wiki page for all possible
        # permissions
        permissions = {pm_notify, pm_files, pm_sysadmin}

        def override_perms(self):
            persistent.aliceos_permissions["Forces_notify"] = True
            persistent.aliceos_permissions["Forces_files"] = True
            persistent.aliceos_permissions["Forces_sysadmin"] = True
        
        def send_tails_message(self, messagetext):
            messages.send_temporary_notification("Tails", messagetext, action=Return(1))
        
        def edmsession_music(self, song):
            self.send_temporary_notification("DJ Sona", "You are listening to: " + song + "!", action=Return(1))
        
        def notify_new_char(self, charname):
            self.send_temporary_notification("New character added!", "Congrats! \""+ charname +"\" has been added to Doki Doki Forces!", action=Return(1))
        
        def evil_monika(self):
            renpy.call("waifuClub")
    
    forces = Forces()

## Applet Code
# Define your applet after you have established your
# app's manifest here. This may include screens, labels,
# or definitions. Please keep all of your applet's code
# in this file.

# Waifu Club Easter Egg
label waifuClub:
    stop music
    show monika evil_justin at t11 zorder 2
    $ m_name = "Evil Monika"
    m "You naive fool! Do you really think you can make her happy in this universe?"
    m "You don't only cling to your ideal girlfriend in a modified game, you also bring her to the universe of the meme lord speedy rodent."
    m "How dissapointing is this."
    m "But just wait, your idealistic dream will crumble into the nightmare it truly is... and then you will run to me for mercy!"
    show monika at thide zorder 1
    hide monika
    m "Also everyone knows that the obese italian plumber was always better than the speedy blue rodent, stupid sociopath with bad videogame taste."
    $ m_name = "Monika"
    return

# Sample window
init screen windowname:
    use UIWindow(Forces)
    use UIWindowContent
    vbox:
        xanchor -16
        yanchor -68
        xoffset 32
        yoffset 32
        xsize 1216
        ysize 603
        vbox:
            # It is recommended to put your content here
            text "Content":
                style "app_default_text"