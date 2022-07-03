import pandas as pd

from baidu_index import Client
client = Client(cookie_str='BIDUPSID=D40A46C68FF98D743B8206FEDCE14937; PSTM=1641184684; BAIDUID=D40A46C68FF98D74CD138FB699D2757B:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; __yjs_duid=1_838732d8ae18360646b7f044a304d13e1641195776728; BAIDUID_BFESS=9C9C6A3837226E4955B6C1D464280171:FG=1; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1641268369; BDUSS=jlxS0t6M1V5NjAtS1BTVHM1aDYwREVBZFFoeTItZm03S1RuSFJNQ3l0UENUfnRoRVFBQUFBJCQAAAAAAAAAAAEAAAA7BWZTYmFiebzCtq-1xND9wskAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMLC02HCwtNhd; BDUSS_BFESS=jlxS0t6M1V5NjAtS1BTVHM1aDYwREVBZFFoeTItZm03S1RuSFJNQ3l0UENUfnRoRVFBQUFBJCQAAAAAAAAAAAEAAAA7BWZTYmFiebzCtq-1xND9wskAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMLC02HCwtNhd; CHKFORREG=d23adee8df7b969300c17f244c8b8d66; bdindexid=19vp8to16mk91bq8upnr834jt3; H_PS_PSSID=35105_35631_35457_34584_35491_35689_35644_26350_35478_22157; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1641272429; ab_sr=1.0.1_MDAzYjE4M2M4MzEzMDg0ODEzZmFiZWY2YWU4NmViMTBhYWIwZGUyMTJhYjBlMDRiNTk1NzQzOTRkN2RiNTBmZjNiNGZjYWE2YzQ5OTM1MDlkMGQxMWEzYjM1ZWFjYjExYWZhYTgwMDMxMTIzYjhhMzY1OWFlNzNhMGEzNjhjYzIwYzFjZWI1MDBmZWFhNGY0NzNhMjgyYTIyN2UzYTVmNQ==; __yjs_st=2_NTBhZjhjYjE3OWQ2Y2M4ZjJjYWViZDYwNzU0MjM3NGJiMDY5ZjY1OWFiZWY4MmY0MjM1OGQ5NTY0ZTRjZDBlZDc4NjYxYjk5MjExMTMwOWE4Nzc1ODIzNGI4MmI0ZWM3ZGMzZDExYjFlNmZhNDhlZGM3YTkwMTZhMmY4YjA1Y2QzYmJjNmI5MTU0NTQ1YjVhZGFhZGI0MjY3NjY1YzM0MDI0MjIxMjk0MzM2OTY2MzI0MzQzYTBhYjk1ZTBkMmI1ODI3MDU0NjY3NmI4YmI0M2U5OWJjZTk0YzdiY2VkYTYwZjI5NWE2OTIwYjlmYzc0OTBjNzgyYzVlMTc2NDJlMF83XzQ1NjdhMzNm; RT="z=1&dm=baidu.com&si=gs67jqxfugv&ss=kxzockm2&sl=i&tt=2mtv&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=reh4"')


data = pd.read_excel("D:\Davion\目的地关键词.xlsx")

data["第1天"] = None
data["第2天"] = None
data["第3天"] = None
data["第4天"] = None
data["第5天"] = None
data["第6天"] = None
data["第7天"] = None
data["第8天"] = None
data["第9天"] = None
data["第10天"] = None
data["第11天"] = None
data["第12天"] = None
data["第13天"] = None
data["第14天"] = None
data["第15天"] = None
data["第16天"] = None
data["第17天"] = None
data["第18天"] = None
data["第19天"] = None
data["第20天"] = None
data["第21天"] = None
data["第22天"] = None
data["第23天"] = None
data["第24天"] = None
data["第25天"] = None
data["第26天"] = None
data["第27天"] = None
data["第28天"] = None
data["第29天"] = None
data["第30天"] = None
data["第31天"] = None
data.index = range(len(data))
for i in range(len(data)):
    keywords = data["关键词"][i]
    print(keywords)
    startdate = data["起始时间"][i].strftime('%Y%m%d')
    enddate = data["结束时间"][i].strftime('%Y%m%d')
    result = client.search(keywords, startdate, enddate)
    try:
        res = list(result[0]["all"].values())
        print(res)
        data["第1天"][i] = res[0]
        data["第2天"][i] = res[1]
        data["第3天"][i] = res[2]
        data["第4天"][i] = res[3]
        data["第5天"][i] = res[4]
        data["第6天"][i] = res[5]
        data["第7天"][i] = res[6]
        data["第8天"][i] = res[7]
        data["第9天"][i] = res[8]
        data["第10天"][i] = res[9]
        data["第11天"][i] = res[10]
        data["第12天"][i] = res[11]
        data["第13天"][i] = res[12]
        data["第14天"][i] = res[13]
        data["第15天"][i] = res[14]
        data["第16天"][i] = res[15]
        data["第17天"][i] = res[16]
        data["第18天"][i] = res[17]
        data["第19天"][i] = res[18]
        data["第20天"][i] = res[19]
        data["第21天"][i] = res[20]
        data["第22天"][i] = res[21]
        data["第23天"][i] = res[22]
        data["第24天"][i] = res[23]
        data["第25天"][i] = res[24]
        data["第26天"][i] = res[25]
        data["第27天"][i] = res[26]
        data["第28天"][i] = res[27]
        data["第29天"][i] = res[28]
        data["第30天"][i] = res[29]
        data["第31天"][i] = res[30]
    except:
        print(result)
        continue


data.to_excel("D:\Davion\输出结果.xlsx")










