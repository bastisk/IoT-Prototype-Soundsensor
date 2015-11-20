#!/usr/bin/python
import alsaaudio, time, audioop, requests, math

# =============== VARIBLES AND DEFINITIONS =====================

# Set Card to your Microphone, run arecord -L to list recording devices
card = 'sysdefault:CARD=Device'

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, card)
inp.setchannels(1)
inp.setrate(8000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(320)

openhab_host = 'localhost'
openhab_port = '8080'


# ================= FUNCTIONS =================================


def put_status(openhab_host, openhab_port, key, value):
    """ Put a status update to OpenHAB  key is item, value is state """
    url = 'http://%s:%s/rest/items/%s/state'%(openhab_host,
                                openhab_port, key)
    req = requests.put(url, data=value)
    if req.status_code != requests.codes.ok:
        req.raise_for_status()    

def basic_header(self):
    """ Header for OpenHAB REST request - standard """
    self.auth = base64.encodestring('%s:%s'
                       %(self.username, self.password)
                       ).replace('\n', '')
    return {
            "Authorization" : "Basic %s" %self.auth,
            "Content-type": "text/plain"}

# ================== CODE =====================================
print "Sound Sensor started."

while True:
	l, data = inp.read()
	if l:
		try:
			value =  audioop.max(data, 2)
			if(value > 0): 
				vu = math.log10(value) * 20
				put_status(openhab_host, openhab_port, 'VolumeSensor', str(vu))
		except audioop.error, e:
			if e.message != "not a whole number of frames":
				raise e
	time.sleep(.050)



