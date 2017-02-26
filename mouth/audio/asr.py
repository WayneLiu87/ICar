import os
import json
from watson_developer_cloud import SpeechToTextV1
from os.path import join, dirname


class asrer:
    def __init__(self):
        self.bin = "../../../cplus/deep-scorer-client/asr-client-file"

        self.cmd_head = self.bin + " asr.meta 192.168.10.252 8281 /llcup/stream/upload "

        self.speech_to_text = SpeechToTextV1(
            username='78319c2f-f9e9-4bef-9afd-a40f1f8812df',
            password='OoQ1jcSJ4lwY',
            x_watson_learning_opt_out=False)


    def recongnize(self, input):
        cmd = self.cmd_head + input + " data/out.json"

        print cmd

        p = os.popen(cmd)

        result = p.read()
        p.close()
        try:
            line = json.loads(result)
            print result
            return line["decoded"]
        except:
            return ""


    def ibm_recongnize(self, input):

        try:
            with open(join(dirname(__file__), input),
                      'rb') as audio_file:
                line = self.speech_to_text.recognize(
                    audio_file, content_type='audio/wav', timestamps=True,
                    word_confidence=True)["results"][0]["alternatives"][0]["transcript"]
                #print line
                return line
        except:
            return ""



    def test(self):
        test_file = "data/hello.wav"
        print self.recongnize(test_file)

if __name__ == "__main__":
    test_asr = asrer()
    test_asr.test()
