# -- coding: utf-8 --
import sys
from fit.Fixture import Fixture
import requests
import json
from jsonschema import validate
from variable import Varible
#from lastdata import Resp
from config import  Config
a = Config()
logger = a.getlog()
reload(sys)
sys.setdefaultencoding("utf_8")

#设置数据结构

class Core(Fixture):
    _typeDict={}
    def __init__(self):
        Fixture.__init__(self)
        self._url=""
        self._headers={}
        self._data=None
        self._params=None
        self._expect_result=None
        self._actual_result=None
        self._validator=""
        self._code=None
        self._last_response=None
        self._diff_result=None

    _typeDict["url"]="String"
    def url(self,s):
        self._url=s
    _typeDict["headers"]="Dict"
    def headers(self,s):
        self._headers=s
    _typeDict["data"]="Dict"
    def data(self,s):
        self._data=s
    _typeDict["params"]="Dict"
    def params(self,s):
        self._params=s
    _typeDict["expect_result"]="Dict"
    def expect_result(self,s):
        self._expect_result=s
    _typeDict["actual_result"]="String"
    def actual_result(self):
        return self._actual_result
    _typeDict["validator"]="String"
    def validator(self,s):
        self._validator=s
    _typeDict["code"]="Integer"
    def code(self):
        return self._code
    _typeDict["last_response"]="Default"
    def last_response(self,s):
        self._last_response=s
    _typeDict["diff_result"]="String"
    def diff_result(self):
        return self._diff_result


    #请求的传递方式
    '''_typeDict["get"] = "Default"
    def get(self):
        self.subvalue()
        r=requests.get(self._url, params=self._params, headers=self._headers)
        #r.content是string类型
        response_context=json.loads(r.content)
        self.last_response(response_context)
        #r.text类型是unicode类型
        self._actual_result=r.text.decode("unicode_escape")
        self._diff_result=self.compa(self._expect_result,response_context)
        self._code = response_context["code"]'''




    _typeDict["get"] = "Default"
    def get(self):
        self.subvalue()
        r = requests.get(self._url, params=self._params, headers=self._headers)
        response_context = json.loads(r.content)
        #self._actual_result = recursive_json_loads(r.text.decode("unicode_escape"))
        logger.info(eval(r.content))
        self.last_response(response_context)

        self._actual_result = r.text.decode("unicode_escape")
        self._diff_result = self.compa(self._expect_result, response_context)
        self._code = eval(r.content)["code"]

    _typeDict["post_by_dict"] = "Default"
    def post_by_dict(self):
        self.subvalue()
        r=requests.post(self._url,params=self._params,headers=self._headers,data=self._data)
        response_context=json.loads(r.content)
        logger.info(response_context)
        self.last_response(response_context)

        self._actual_result=r.text.decode("unicode_escape")
        self._diff_result=self.compa(self._expect_result,response_context)
        self._code=response_context["code"]

    _typeDict["post"] = "Default"
    def post(self):
        self.subvalue()
        r=requests.post(self._url,params=self._params,headers=self._headers,data=json.dumps(self._data))
        #下面这个类型是dictionary类型
        response_context=json.loads(r.content)
        logger.info(response_context)
        self.last_response(response_context)

        #这个类型是unicode类型
        self._actual_result=r.text.decode("unicode_escape")
        self._diff_result=self.compa(self._expect_result,response_context)
        self._code = response_context["code"]
#对预期结果和实际结果进行比较

    def compa(self,obj1,obj2):
        #obj1是jsonschame格式的数据即我们这里的self._expect_result 期望结果
        #obj2是需要比较的结果即实例，self._actual_result

        a= validate(obj2,obj1)
        if not a:
            return "PASS"
        else:
            return str(a)
#定义函数连通上一个接口的返回结果和变量的替换

    '''def set_last_respon(self,body):
        self.last_response(body)'''



        #这个的返回结果是str类型的

#处理可能出现的下一个接口使用上一个接口的返回值
    def subvalue(self):
        if self._last_response:
            logger.info(self._last_response)
            a = Varible(self._last_response)
            if self._url:
                self.url(a.vari_to(self._url))
            if self._headers:
                self.headers(a.vari_to(self._headers))
            if self._params:
                self.params(a.vari_to(self._params))
            if self._data:
                self.data(a.vari_to(self._data))
#将str类型转换成dict,然后转化成object





#__main__函数
if __name__=="__main__":
    core = Core()

