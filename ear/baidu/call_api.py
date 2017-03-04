#encoding=utf-8
import urllib, urllib2

class caller:
    def __init__(self, url_head):
        self.url_head = url_head

    def call(self, action):

        url = self.url_head + "/" + action
        print url
        handler = urllib2.urlopen(url)
        print handler.read()


    def act(self, text):
        if(text.find('前') >= 0 or text.find('进') >= 0):
            action = "forward"

        elif(text.find('后') >= 0 or text.find('退') >= 0):
            action = "reverse"

        elif(text.find('右') >= 0):
            action = "right"

        elif(text.find('左') >= 0):
            action = "left"
        else:
            action = ""

        if action == "":
            print "no action"
        else:
            self.call(action)
