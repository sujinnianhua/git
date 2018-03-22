#__ coding=utf-8 __
import re
from config import Config
from getval1 import getvalue
import json
a = Config()
logger = a.getlog()
class Varible1():

    def __init__(self,body):

        if not body:
            self.replacement=None
        else:
            #self.replacement=dict((name, getattr(body, name)) for name in body)这种方法行不通，因为Resp 对象不能迭代

            self.replacement=body
            logger.info(self.replacement)
            logger.info(type(self.replacement))
    patter = re.compile("\%(.+?)\%")
    def vari_to(self,var):


        if not var:
            return None
        if isinstance(var,str):
            if self.juge(var ) and self.replacement:
                al=Varible1.patter.findall(var)
                bl=var.replace("%","")
                for n in al:
                    if "@" in n:
                        #下面这种方法不能取到嵌套的值如result.token，所以还要想办法去获取
                        cl=n.replace("@",".")
                        a=getvalue(self.replacement,cl)
                        bl=bl.replace(n,str(a))
                    else:
                        a = getvalue(self.replacement, n)
                        bl=bl.replace(n,str(a))
                logger.info("替换后的结果bl")
                logger.info(bl)
                return bl
            logger.info("替换后的结果var")
            logger.info(var)
            return var
        elif isinstance(var,dict):
            for k in var.keys():
                if self.juge(var[k]) and self.replacement:
                    al=Varible1.patter.findall(var[k])
                    var.update({k:var[k].replace("%","")})
                    for n in al:
                        if "@" in  n:
                            cl = n.replace("@", ".")
                            a = getvalue(self.replacement, cl)
                            var.update({k:var[k].replace(n,str(a))})
                        else:
                            a = getvalue(self.replacement, n)
                            var.update({k:var[k].replace(n,str(a))})
                    logger.info("替换后的结果var-dict")
                    logger.info(var)
                    return  var
        else:
            logger.info("替换后的结果var-dict")
            logger.info(var)
            return var

#判断变量中是否有%，有%就进行转换
    def juge(self,varia):
        if isinstance(varia,str) and "%" in varia:
            return "True"
        else:
            return "False"