#Rollcode.com


 


import sys,subprocess,urllib


 


def getSpeech(phrase):
	googleAPIurl="http://tts-api.com/tts.mp3?"
	param={'q':phrase}
	data=urllib.urlencode(param)
	googleAPIurl+=data
	# Append the parameters
	print googleAPIurl
	return googleAPIurl


 


def raspberryTalk(text):
	# This will call mplayer and will play the sound
	subprocess.call(["mplayer",getSpeech(text)],shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)


 


if __name__ =="__main__":
    raspberryTalk("Hello little P ,How are you?Where are you from?My name is Raspberry Pi,nice to meet you!")
