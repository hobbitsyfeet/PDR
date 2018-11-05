# PDR

Python Documentation Recommender extracts and recommends documentation based on a comment written in code. Equipped with a plugin for Sublime Text 3


SETUP:

1 Install dependencies:

    - Make sure Pip is installed (see https://pip.pypa.io/en/stable/installing/)
    - Go to PDR/ directory
    - Type: pip install -r requirements.txt

2 Sublime plugin

    A. Copy PDR into the directory where sublime is installed.
    Default Installation Paths:
       - Windows: This is usually C:/SublimeText3
       - Mac OS: This can be accessed by going to /Applications sublime is installed, right click and click Show Contents
                /Applications/SublimeText.app/Contents/MacOS
    Custom Installation Paths
       - You find where by opening sublime -> View -> show Console
       - In this console you should see Current Working Direcotry:
   
    Paste PDR/ folder into the specified direcotry.
    
    
    B. Copy the contents from PDR/plugin
        - Open Sublime Text 3
             - Windows go to Preferences->Browse Packages...
             - Mac OS go to SublimeText menu -> Preferences -> Browse Packages...
        - Go into User/
        - Paste the contents into User
        - Restart Sublime Text 3
