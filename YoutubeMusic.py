import pygetwindow as gw
import pyautogui
import keyboard

# default hotkey for toggling like button on YouTube music is shift + =.  If that changes, this will need updated.

def toggleLikeSong(): 
    gameWindow = gw.getActiveWindowTitle()

    windows = gw.getAllTitles()
    for title in windows: #used to find new title.  Window title will change with song, this refreshes to the new title each time.
        if 'Firefox' in title: # if Firefox is not being used can change this name.  
            musicWindow = title

    gw.getWindowsWithTitle(musicWindow)[0].activate()
    # TODO add prompt on script launch to get browser name app will be running in.
    # TODO implmement tab switching so it can find the correct tab if not already on that tab.

    pyautogui.hotkey('shift', '=')

    gw.getWindowsWithTitle(gameWindow)[0].activate()

runkey = ']' # if you want a different hotkey you can change this
# TODO add prompt on script launch to get hotkey user wants to use.

keyboard.add_hotkey(runkey, toggleLikeSong)

keyboard.wait('[') # key you want to press to stop the script.
# TODO add prompt for this as well.