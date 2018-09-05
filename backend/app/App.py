from __future__ import print_function
import numpy as np
import time
#import pathlib2 as pathlib

class App():
    def __init__(self, client):
        self.client = client
        self.update_time = 2.0
        print('App inited!')

    def run(self):
        while True:
            self.update()

    def update(self):
        self.do()
        time.sleep(self.update_time)

    def do(self):
        print('do')

        # Calls update_event function on frontend server
        self.client.update_event()

        # Calls empty function on frontend server
        # self.client.empty()

        # Calls with_reply function on frontend server
        # and writes the response to file (enable import pathlib)
        # reply = self.client.with_reply('Chen')
        # file = open('sc_test.txt', 'w')
        # file.write(str(reply))          
        # file.close()
        return

    def add_man_to_str(self, text):
        return text + ', man.'