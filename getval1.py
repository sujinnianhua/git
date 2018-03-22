#__ coding=utf-8 __
def getvalue(dic,st):
    if "." in st:
        a=st.split(".",1)
        if isinstance(dic[a[0]],dict):
            return getvalue(dic[a[0]],a[1])
        else:
            return "返回结果有误"
    else:
        return dic[st]

a=getvalue({"code":200,"message":"success","result":{"token":"d875dfe298ef420b961df80d6d952aba"}},"result.token")
print a