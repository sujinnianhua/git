#__ coding=utf-8 __
#将dict格式转换成object格式是因为上一个接口的返回结果是dict类型的，而jsonschame的比较方法validator传入的参数是object类型的
class dict2objedt():
    def di2ob(self,dict):
        def __init__(self):
            self.__dict__.update(dict)