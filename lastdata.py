#__ coding=utf-8 __
class last_respon(object):
    def __init__(self):
        self.raw = ""
    @property
    def body(self):
        if not self.raw:
            return "None"
        else:
            return self.raw
    @body.setter
    def body(self,raw_body):
        self.raw=raw_body
#@property 和@respon.setter不写上的话，def respon(self,raw_body)会报错
class Resp(last_respon):
    def __init__(self,raw):
        super(Resp, self).__init__()
        self.body=raw
        self._status_code=None

    @property
    def status_code(self):
        return self._status_code
    @status_code.setter
    def status_code(self,code):
        self._status_code=code
    def __str__(self):
        return "{self._status_code},{self.body}".format(self=self)
#实际这一模块可以不要