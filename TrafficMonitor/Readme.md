1. You need python (i use 3.11.9) and add it to PATH, you also need to install module psutil
2. start traffic.pyw, it will get the internet speed and save it to config.xml and updating it every second without opening console window
3. start Start_LocalHost.vbs, it will start the Start_LocalHost.bat without opening console window
4. test_nouse_startlocalehost.py is not used, it just the test py
5. fork windhawk clock mod, go to line 12 and add this at the end -lruntimeobject
6. go to line 638, change the g_settings.webContentsUpdateInterval * 60 to g_settings.webContentsUpdateInterval * 1
7. compile the mod
8. then use the forked mod (that you just compile), put http://localhost:8000/config.xml to its web content and set everything necessary
9. and/or copy and paste the content of Taskbar Clock Customization.txt into mod advanced tab
10. Save
