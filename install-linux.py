import os
import platform
import sys
import subprocess
# Ew termux 
# i dont want that so detect it then get it out of here
if os.path.isdir('/data/data/com.termux/'):
    termux = True
else:
    termux = False
try:
    if os.environ["ANDROID_DATA"]:
        android = True
    android_vcheck = subprocess.run(["getprop", "ro.build.version.release"], capture_output = True,text=True)
    android_version = int(android_vcheck.stdout.strip("\n").strip(" "))
except KeyError:
    android = True
    android_version = "Unknown"
### VARIAHOLES
# Installer info (run 'info' arg to show these)
version = 1.00
# Figure out various system information
kernel_release = platform.release()
kernel_name = platform.system()
cpu_arch = platform.machine()
if sys.maxsize > 2**32:
    cpu_bits = 64
else:
    cpu_bits = 32
# ignore the following geneve convention violations:
if termux:
    system_desc = str("Android "+str(android_version)+" Termux, "+kernel_name+" "+kernel_release+" Kernel on "+cpu_arch+" ("+str(cpu_bits)+" bit)")
elif android:
    system_desc = str("Android "+str(android_version)+", "+kernel_name+" "+kernel_release+" Kernel on "+cpu_arch+" ("+str(cpu_bits)+" bit)")
else:
    system_desc = str(kernel_name+" "+kernel_release+" Kernel on "+cpu_arch+" ("+str(cpu_bits)+" bit)")
# The install type arg is not required therefore 
# we must perform some funk to tell the program that.
try:
    install_type_arg = sys.argv[0]
except IndexError:
    install_type_arg = False
# Remember what numerical order these lists are in, they are important for uhhmm... some reason.
install_type_long = ["help", "version", "uninstall", "custom", "info"]
install_type_short = ["-h", "-v", "-u", "-c", "-i"] # Yes, the prefixes are hardcoded, sue me.
print(system_desc)
