from urllib import request    # To get wwv.txt
import datetime               # To get a timestamp
import time   # For other time stuff, like time.sleep() <https://docs.python.org/3/library/time.html#time.sleep>
from datetime import timezone # For less typing(use "timezone()" instead of "datetime.timezone()"
import sys          # Mostly for working with STDOUT: <https://docs.python.org/3/library/sys.html#sys.stdout>

# Make a human readable UTC(+00:00) timestamp
run_time = datetime.datetime.now(timezone.utc)
ep_time = run_time.timestamp()                   # Get UTC in UNIX epoch time
time_stamp = datetime.datetime.fromtimestamp(ep_time, datetime.UTC)
formatted_time = time_stamp.strftime('%H:%M:%S') # Format the time like a digital clock(HH:MM:SS)

# Print the UTC timestamp
print(str("[1;30mCurrent UTC: " + "[35m" + formatted_time + "[0m"))

# Get the HF conditions text from wwvtext_src
wwvtext_src = 'https://services.swpc.noaa.gov/text/wwv.txt' # Url where wwv.txt is located
wwvtext = request.urlopen(wwvtext_src)                      # Get wwv.txt from the url

# Print/parse the HF conditions line-by-line:
for line in wwvtext:
    line = line.strip(b"\n") # Remove those stupit newline bytes because they make random empty lines
    line = line + b"[0m"   # Reset the style with each line(sometimes terminals shit their pants and act like there
#                              was never a reset(^[[0m) escape code.
    printline = True         # Prints the current line if still set to "True"
    if line.startswith(b"#"):
        printline = False    # Doesn't print any lines starting with "#". Kind of like a comment in this code.
    if line.startswith(b":Product:"): # Deletes ugly ":Product:" instances in the current line after detecting them
        printline = False             # Also prints a styled line with a white background. We don't want the line
#                                       to print twice, so we make it so the unstyled line won't print.
        line = line.strip(b":Product: ")
        time.sleep(0.005)
        print("[30;47m" + line.decode('UTF-8'))
        sys.stdout.flush()
    if line.startswith(b":Issued:"):  # Same as above, but instead of ":Product:" intances, it's ":Issued:" instances.
        line = line.strip(b":Issued:")
        printline = False    
        time.sleep(0.005)    
        print("[1mIssued:" + line.decode('UTF-8'))
        print("---------------------------------------------------") # Visually seperate headings/titles from the body
        sys.stdout.flush()   
    if printline:            # Prints an unstyled line if "printline" is set to True
        time.sleep(0.005)
        print(line.decode('UTF-8'))
        sys.stdout.flush()


