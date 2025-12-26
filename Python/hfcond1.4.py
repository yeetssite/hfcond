#!/usr/bin/python
# Built for Python 3.12 on Linux.
# Probably can be run in Python on Windows and most likely will run in Python on Mac OS or any Unix or Linux-like 
# system

# Copyleft (c) 2025 mangolover1899("itsyeetsup")




from urllib import request    # To get wwv.txt
import datetime               # To get a timestamp
import time   # For other time stuff, like time.sleep() <https://docs.python.org/3/library/time.html#time.sleep>
from datetime import timezone # For less typing(use "timezone()" instead of "datetime.timezone()"
import sys          # Mostly for working with STDOUT: <https://docs.python.org/3/library/sys.html#sys.stdout>
import os
registered_headers = ["Solar Activity", "Solar Wind", "Energetic Particles", "Geospace", "Energetic Particle"] # Yes, this is a manually updated list of terms used in NOAA's discussion. Kill me then.

def successful_connection():
    try:
        request.urlopen("https://swpc.noaa.gov/")
        return True
    except:
        try:
            request.urlopen("https://google.com")
            return True 
        except:
            return False

# Script info
version = 1.030

exitScript = False

# Get flags

args = sys.argv[0:] # Get a list of options/arguments/flags passed through the shell
if "-n" in args or "--no-style" in args: # Run without printing ANSI escape codes
    styled = False
else:
    styled = True
if "-t" in args or "--tts" in args: # Print wwv text for a Text-To-Speech engine
    for_tts = True
    styled = False
else:
    for_tts = False
try:
    if sys.argv[1] == "-d" or sys.argv[1] == "--discussion":
        forecast_discussion = True
    else:
        forecast_discussion = False
    if sys.argv[1] == "-w" or sys.argv[1] == "--whatsnew":
        whats_new = True
    else:
        whats_new = False
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        help = """USAGE:
hfcond [ OPTION ] [ FLAG ]
hfcond -d [ FLAG ]

OPTIONs:
*   Note: these HAVE to come BEFORE any flags for them to be used.
    -h, --help          Shows this message, then exits.
    -v, --version       Shows version info, then exits.
    -d, --discussion    Get the forecast discussion instead of HF conditions.
    -w, --whatsnew      Shows what's new with hfcond. Pulled from
                        <https://yeetssite.github.io/shortwave/hfc-whatsnew.txt>
FLAGs:
    -n, --no-style      Output without ANSI escape styles.
    -t, --tts           Output text for a text-to-speech engine to say.

Examples:
    Show the forecast discussion without style: 
        hfcond -d -n
    Show the HF conditions for a TTS engine to speak out loud:
        hfcond -t
"""
        print(help)
        if not successful_connection():
            print("[41;1;37m No internet connection detected [0m")
            print("[31m- HFcond needs an internet connection to work")
            print("- Check how tightly your Ethernet cables are connected")
            print("- Check any Firewall/Proxy settings")
            print("- Check your WiFi connection")
            print("- The service we use for forecasts may be down[0m")

        exitScript = True
    if sys.argv[1] == "-v" or sys.argv[1] == "--version":
        print("hfcond version " + str(version))
        exitScript = True
except:
    forecast_discussion = False
    whats_new = False

if exitScript:
    sys.exit(0)
if not successful_connection():
    print("[41;1;37m Could not connect to the internet [0m")
    print("[31m- Check how tight any ethernet cables are connected")
    print("- Check your Firewall/Proxy")
    print("- The service we use for our forecasts may be down")
    print("- Check that your WiFi/Mobile Data is turned on[0m")
    sys.exit(0)

# Make a human readable UTC(+00:00) timestamp
run_time = datetime.datetime.now(timezone.utc)
ep_time = run_time.timestamp()                   # Get UTC in UNIX epoch time
time_stamp = datetime.datetime.fromtimestamp(ep_time, datetime.UTC)
formatted_time = time_stamp.strftime('%H:%M:%S') # Format the time like a digital clock(HH:MM:SS)

# Print the UTC timestamp
if not for_tts:
    if styled:
        print(str("[1;30mCurrent time(UTC+00:00): " + "[33m" + formatted_time + "[0m"))
    elif not styled:
        print(str("Current time(UTC+00:00): " + formatted_time))
elif for_tts:
        print("The time is " + formatted_time + " Coordinated universal time.")


# Get the HF conditions text from wwvtext_src
if forecast_discussion:
    wwvtext_src = 'https://services.swpc.noaa.gov/text/discussion.txt' 
elif whats_new:
    wwvtext_src = 'https://yeetssite.github.io/hfcond/whatsnew.txt'
else:
    wwvtext_src = 'https://services.swpc.noaa.gov/text/wwv.txt'
wwvtext = request.urlopen(wwvtext_src)                      

# Print/parse the HF conditions line-by-line:
for line in wwvtext:
    line = line.strip(b"\n") # Remove those stupit newline bytes because they make random empty lines
    line = line.strip(b"\r")
    if styled:
        line = line + b" [0m"   # Reset the style with each line(sometimes terminals shit their pants and act like there
#                              was never a reset(^[[0m) escape code.
    printline = True         # Prints the current line if still set to "True"
    if line.startswith(b"#"):
        printline = False # Doesn't print any lines starting with "#". Kind of like a comment in this code.
    if for_tts:
        line = line.replace(b"UTC", b"Coordinated Universal Time")
        line = line.replace(b"?", b"unknown")
    for item in registered_headers:
        if item.encode('UTF-8') in line:
            if styled:
                printline = False
                forecast_type_heading = "[45;1;37m " + item + " [0m"
                line = line.replace(item.encode('UTF-8'), forecast_type_heading.encode('UTF-8'))
                print(line.decode('UTF-8'))
    if line.startswith(b"."):
        if styled:
            printline = False
            print("[1;34m" + line.decode('UTF-8') + "[0m")
    if line.startswith(b":Product:"): # Deletes ugly ":Product:" instances in the current line after detecting them
        printline = False             # Also prints a styled line with a white background. We don't want the line
#                                       to print twice, so we make it so the unstyled line won't print.
        line = line.strip(b":Product: ")
        time.sleep(0.005)
        if not for_tts:
            if styled:
                print("[1;44;37m " + line.decode('UTF-8'))
            if not styled:
                if line.endswith(b".tx"):
                    print(line.decode('UTF-8') + "t") # For some reason the unstyled text cuts off ".txt" by one letter
                else:
                    print(line.decode("UTF-8"))
        elif for_tts:
            line = line.strip(b"wwv.txt")
            print(line.decode('UTF-8'))
        sys.stdout.flush()
    if line.startswith(b":Issued:"):  # Same as above, but instead of ":Product:" intances, it's ":Issued:" instances.
        line = line.strip(b":Issued:")
        printline = False    
        time.sleep(0.005)
        if not for_tts:
            if styled:
                print("[1;35mIssued:" + line.decode('UTF-8'))
            if not styled:
                print("Issued:" + line.decode('UTF-8'))
            print("———————————————————————————————————————————————————")
        elif for_tts:                                                        
            line = line.replace(b"UTC", b"Coordinated universal time.")
            noaa_time1 = list()                                            
            for word in line.decode('UTF-8').split():                
                if str(word).isdigit():
                    noaa_time1.append(word)
            today = datetime.datetime.now().strftime("%B %d, %Y")
            noaa_time1 = noaa_time1[2]
            noaa_time1 = [int(i) for i in str(noaa_time1)]
            itercounter = 0
            noaa_timestamp = str()
            replace_timestamp = str()
            for item in noaa_time1:
                itercounter = itercounter + 1
                item = str(item)
                if itercounter == 3:
                    noaa_timestamp.replace("00", "zero")
                    noaa_timestamp = noaa_timestamp + " hours, "
                noaa_timestamp = noaa_timestamp + item
                replace_timestamp = replace_timestamp + item
            noaa_timestamp = noaa_timestamp + " minutes, Coordinated Universal Time."
            line = today + " at " + noaa_timestamp
            line = line.replace("00", "zero")
            print("Issued on " + line)


        sys.stdout.flush()   
    if printline:            # Prints an unstyled line if "printline" is set to True
        time.sleep(0.005)
        print(line.decode('UTF-8'))
        sys.stdout.flush()


