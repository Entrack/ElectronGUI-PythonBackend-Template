from __future__ import print_function
from real_app_initer.RealAppIniter import RealAppIniter

class AppAPI(object):
    def __init__(self, ip, port):
        real_app_initer = RealAppIniter(ip, port)
        self.real_app = real_app_initer.get_real_app()
        print('AppAPI', 'inited!')
    
    def safe_call(self, function, *args):
        try:
            return function(*args)
        except Exception as e:
            return e

    def echo(self, text):
        return text

    #
    # API STARTS HERE
    #  

    def add_man_to_str(self, text):
        return self.safe_call(self.real_app.add_man_to_str, 
            text)