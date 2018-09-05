#This art is a color correction of Monika in the classroom during the day
#and an alternative animation for the window that shows a bluish white haze
#instead of the standard space scene.
#Credit: Monika After Story Team

#Spaceroom in the day without Monika
image monika_room_day = "mod_assets/DaytimeMonikaRoom/monika_day_room.png"
#Spaceroom in the day with Monika
image monika_bg_day = "mod_assets/DaytimeMonikaRoom/monika_day_bg.png"

#Daytime styled window animations
image room_mask3 = Movie(channel="window_3", play="mod_assets/DaytimeMonikaRoom/window_3.webm",mask=None,image="mod_assets/DaytimeMonikaRoom/window_3_fallback.png")
image room_mask4 = Movie(channel="window_4", play="mod_assets/DaytimeMonikaRoom/window_4.webm",mask=None,image="mod_assets/DaytimeMonikaRoom/window_4_fallback.png")

#This art adds sprite art with expressions for monika in the spaceroom scene
#both in twilight and daytime varieties. To use, place monika in a scene as
#usual and use poses 6 and 7 for day and night monika, respectively.
#Credit: Monika After Story Team
image monika 26 = im.FactorScale("mod_assets/MonikaSittingExpressions/room11.png",0.625)
image monika 26a = im.FactorScale("mod_assets/MonikaSittingExpressions/room01.png",0.625)
image monika 26b = im.FactorScale("mod_assets/MonikaSittingExpressions/room02.png",0.625)
image monika 26c = im.FactorScale("mod_assets/MonikaSittingExpressions/room03.png",0.625)
image monika 26d = im.FactorScale("mod_assets/MonikaSittingExpressions/room04.png",0.625)
image monika 26e = im.FactorScale("mod_assets/MonikaSittingExpressions/room05.png",0.625)
image monika 26f = im.FactorScale("mod_assets/MonikaSittingExpressions/room06.png",0.625)
image monika 26g = im.FactorScale("mod_assets/MonikaSittingExpressions/room07.png",0.625)
image monika 26h = im.FactorScale("mod_assets/MonikaSittingExpressions/room08.png",0.625)
image monika 26i = im.FactorScale("mod_assets/MonikaSittingExpressions/room09.png",0.625)
image monika 26j = im.FactorScale("mod_assets/MonikaSittingExpressions/room10.png",0.625)
image monika 26k = im.FactorScale("mod_assets/MonikaSittingExpressions/room11.png",0.625)
image monika 26l = im.FactorScale("mod_assets/MonikaSittingExpressions/room12.png",0.625)
image monika 26m = im.FactorScale("mod_assets/MonikaSittingExpressions/room11.png",0.625)
image monika 26n = im.FactorScale("mod_assets/MonikaSittingExpressions/room14.png",0.625)
image monika 26o = im.FactorScale("mod_assets/MonikaSittingExpressions/room15.png",0.625)
