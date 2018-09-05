## Doki Doki Forces - YuriKnife
# I can feel the tenderness of my skin though the knife,
# as if it were an extension of my sense of touch.
# My body gets high and overly excited.
# There are voices, incredibly faint,
# that scream: "Resist this pleasure, Yuri!!!",
# voices that are trying to make me stop...
# but I can already tell that the pleasure is too much.
# I can't... And I won't stop myself!
# My Third Eye is drawing me closer.
# The Ruby is drawing us closer.
# Your lust continues to linger through my body and veins, AND I WILL NOT STOP IT!!!
# Author(s): Neil García (@cpgyuri), Yuri
# Copyright: (C) 2018

init python:
    class YuriKnife(Applet):
        ## App Manifest
        # Define important information about your app here.
        # This information will be used in places like the
        # Control Center, notification badges, apps menus,
        # and the desktop shell.

        # Provide a short name and a long name for your app.
        short_name = "Yuri"
        long_name = "Yuri_Knife"

        # Provide the author information, version number, and
        # description of your app, as where as the name of the
        # folder that your applet lives in.
        app_dir = "YuriKnife"
        author = "CPG Yuri"
        version = "6.66"
        description = "I love you so much that I even touch myself with the pen I stole from you."

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
            persistent.aliceos_permissions["Yuri_notify"] = True
            persistent.aliceos_permissions["Yuri_files"] = True
            persistent.aliceos_permissions["Yuri_sysadmin"] = True
        
        def send_yuri_message(self, messagetext):
            messages.send_temporary_notification("Yuri", messagetext, action=Return(1))
        
        def yuri_notifications(self, messagetext):
            self.send_temporary_notification("Yuri has a message for you!", messagetext, action=Return(1))
    
    yuriKnife = YuriKnife()

## Applet Code
# Define your applet after you have established your
# app's manifest here. This may include screens, labels,
# or definitions. Please keep all of your applet's code
# in this file.

# Sample window
init screen windowname:
    use UIWindow(renpyApp)
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