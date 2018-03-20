#-- coding=utf-8 --
#第一种方法
'''def getvalue(dic,st):
    if "." in st:
        a=st.split(".",1)
        if isinstance(dic[a[0]],dict):
            return getvalue(dic[a[0]],a[1])
        else:
            return "返回结果有误"
    else:
        return dic[st]

a=getvalue({"code":200,"message":"success","result":{"token":"d875dfe298ef420b961df80d6d952aba"}},"result.token")
print a'''
#第二种方法
def enco(val):
    pr={}
    if isinstance(val,dict):
        for k,v in val.items():
            k=k.encode("utf-8")
            if isinstance(v,dict):
              pr[k]=enco(v)
            else:
                if isinstance(v,int):
                    pr[k]=v
                else:
                    pr[k]=v.encode("utf-8")
    else:
        val=val.encode("utf-8")
    return gese(pr)
class gese(dict):
    def __getattribute__(self, key):
        try:
          return self[key]
        except KeyError as k:
            raise AttributeError(k)
    def __setattr__(self, key, value):
           self[key]=value
    def __delattr__(self, key):
        try:
          del self[key]
        except KeyError as k:
            raise AttributeError(k)
    def __repr__(self):
        return dict.__repr__(self)

