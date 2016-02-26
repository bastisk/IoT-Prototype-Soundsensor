# IoT-Prototype-Soundsensor
A script that reads the volume from an USB Microphone connected to Raspberry Pi.
It then sends this data into [OpenHab](https://github.com/openhab/openhab).

The script uses the python libraries for alsaaudio

# Prerequisites
Get a nice USB Microphone for your Pi. We used [that one] (http://www.amazon.com/Kinobo-Microphone-Desktop-Recognition-Software/dp/B00IR8R7WQ). It works just fine :)

Next you should nstall the needed packages on your Pi by running
<pre>sudo apt-get install python-alsaaudio </pre> 
note to myself: add other needed packages, stay tuned.

# How to run
To use this script you could simply execute it by running
<pre>sudo python sound.py</pre>

# Autostart and execution as a service
WARNING: The autostart-script currently ends the sound.py script by running <code>killall python</code>, which is a very dirty way of doing it. Make sure to only use it if this is the only python script running on your Pi. 

If you wish to add this script to autostart or simply want to add start and stop actions to it you can use the provided init.d Script to do so.

Simple copy the "sound" file to etc/init.d/sound by running:
<pre>sudo cp /your/clone/dir/sound /etc/init.d/sound</pre>
Next edit the file in the line containing <code>python /home/pi/Documents/Scripts/sound.py &</code> and replace the path by the location where you saved the file.

Then make it executable by running 
<pre>sudo chmod +x /etc/init.d/sound</pre>
If done you can now start or stop the script by running
<pre>sudo /etc/init.d/sound start //this will start the script
sudo /etc/init.d/sound stop //this will kill the script
</pre>

Feel free to contribute a better option for this script ;)

# Configuration in OpenHab
[to be documented]
