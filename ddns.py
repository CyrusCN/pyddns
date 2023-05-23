import os
#调用系统函数生成list
a = os.popen('ip addr | grep inet6').readlines()
#筛选符合关键字列
keyword = '240'
b = [row for row in a if keyword in row]
#打印new list
print (b)
#in b list select str(默认选择第一列)
valuev6 = b[1]
print (valuev6)
#筛选location与ip
stloc = valuev6.find('inet6') + 6
endloc = valuev6.find('scope') - 4
value = valuev6[stloc:endloc]
print (value)
#curl a str value from ipaddr6
#以下post包请根据对应dns解析商自行构建
os.system("curl -X POST https://dnsapi.cn/Record.Ddns -d 'login_token=,,&value=%s'" % value)>
