#encoding=utf-8

import wave
import urllib, urllib2, pycurl
import base64
import json
import PyBaiduYuyin as pby
## get access token by api key & secret key

YOUR_APP_KEY = "nfVCafIaaCgBN5kzeAlcB78s"
YOUR_SECRET_KEY = "36e782a296dde6fcc85960d4a5a450be"

def get_token():
    apiKey = "nfVCafIaaCgBN5kzeAlcB78s"
    secretKey = "36e782a296dde6fcc85960d4a5a450be"

    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;

    res = urllib2.urlopen(auth_url)
    json_data = res.read()
    return json.loads(json_data)['access_token']

def dump_res(buf):
    print buf


## post audio to server
def use_cloud(token, filename):
    fp = wave.open(filename, 'rb')
    nf = fp.getnframes()
    f_len = nf * 2
    audio_data = fp.readframes(nf)

    cuid = "1234567894321" #my xiaomi phone MAC
    srv_url = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token=' + token
    http_header = [
        'Content-Type: audio/pcm; rate=16000',
        'Content-Length: %d' % f_len
    ]

    c = pycurl.Curl()
    c.setopt(pycurl.URL, str(srv_url)) #curl doesn't support unicode
    #c.setopt(c.RETURNTRANSFER, 1)
    c.setopt(c.HTTPHEADER, http_header)   #must be list, not dict
    c.setopt(c.POST, 1)
    c.setopt(c.CONNECTTIMEOUT, 30)
    c.setopt(c.TIMEOUT, 30)
    c.setopt(c.WRITEFUNCTION, dump_res)
    c.setopt(c.POSTFIELDS, audio_data)
    c.setopt(c.POSTFIELDSIZE, f_len)
    c.perform() #pycurl.perform() has no return val

    #print "result:", result



def baidu_asr(token, speech_file):
    with open(speech_file, 'rb') as f:
        speech_data = f.read()

        cuid = "1234567894321"

        speech_base64=base64.b64encode(speech_data).decode('utf-8')
        speech_length=len(speech_data)
        data_dict = {'format':'wav', 'rate':16000, 'channel':1, 'cuid':cuid, 'token':token, 'lan':'zh', 'speech':speech_base64, 'len':speech_length}
        json_data = json.dumps(data_dict).encode('utf-8')
        json_length = len(json_data)

        request = urllib2.Request(url='http://vop.baidu.com/server_api')
        request.add_header("Content-Type", "application/json")
        request.add_header("Content-Length", json_length)
        fs = urllib2.urlopen(url=request, data=json_data)

        result_str = fs.read().decode('utf-8')
        json_resp = json.loads(result_str)['result'][0]
        return json_resp


def baidu_say(text):
    tts = pby.TTS(app_key=YOUR_APP_KEY, secret_key=YOUR_SECRET_KEY)
    tts.say(text)


if __name__ == "__main__":
    token = get_token()
    #use_cloud(token, "data/test.wav")
    #print asrapi("data/hello.wav")
    print baidu_asr(token, "data/test.wav")
    baidu_say("你好")
