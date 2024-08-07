1. start traffic.pyw, it will get the internet speed and save it to config.xml and updating it every second without opening console window
2. start Start_LocalHost.vbs, it will start the Start_LocalHost.bat without opening console window
3. test_nouse_startlocalehost.py is not used, it just the test py
4. fork windhawk clock mod, go to line 12 and add this at the end -lruntimeobject
5. go to line 638, change the g_settings.webContentsUpdateInterval * 60 to g_settings.webContentsUpdateInterval * 1
6. compile the mod
7. then use the forked mod (that you just compile), put http://localhost:8000/config.xml to its web content and set everything necessary
