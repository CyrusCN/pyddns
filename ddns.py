# pyddns 更改记录动态解析（定时任务自己去加）
import os
##通过调用系统指令并将内容赋予a##
a = os.popen('ip addr | grep inet6').readlines()
##打印a的类型(运行后输出为 list)##
print (type(a))
##从打印的list中选取某一元素（具体看你系统的输出结果，我的第三个结果也就是012的2）
if len(a) >3 :
        valuev6 = a[2]
        print (valuev6)
        print (type(valuev6))
else:
        print (a)
##从打印的未经过滤的v6截取字符##
endloc = valuev6.find('scope') - 4
##经测试第十个字符到关键字符'scope' - 4为ipv6地址
value = valuev6[10:endloc]
print (value)
#curl a str value from ipaddr6#通过解析商提供的方式传递修改域名，本人为dnspodcn
os.system("curl -X POST https://dnsapi.cn/Record.Ddns -d 'login_token=你自己的&format=json&domain_id=86420473&record_id=1458570518&record_type=AAAA&record_line_id=10%%3D0&sub_domain=ddns&value=%s'" % value)
#其他信息通过以下指令获取（具体看自己的服务商）
#用户域名列表
#curl -X POST https://dnsapi.cn/Domain.List -d 'login_token=你的&format=json'
#记录列表
#curl -X POST https://dnsapi.cn/Record.List -d 'login_token=你的&format=json&domain_id=前一个指令获取的'

