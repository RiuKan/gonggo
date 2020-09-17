from bs4 import BeautifulSoup
import requests
import lxml
from datetime import datetime
import json


now = datetime.now()
data = """<?xml version="1.0" encoding="UTF-8"?>
<Root xmlns="http://www.nexacroplatform.com/platform/dataset">
<Parameters>
        <Parameter id="_ga">GA1.3.1263763937.1599781034</Parameter>
        <Parameter id="_gid">GA1.3.194345206.1599781034</Parameter>
        <Parameter id="_fbp">fb.2.1599781061325.1589399029</Parameter>
        <Parameter id="_gat_gtag_UA_133417796_16">1</Parameter>
        <Parameter id="NetFunnel_ID" />
</Parameters>
<Dataset id="dsSch">
        <ColumnInfo>
                <Column id="PAN_NM" type="STRING" size="256"  />
                <Column id="CNP_CD" type="STRING" size="256"  />
                <Column id="PG_SZ" type="STRING" size="256"  />
                <Column id="PAGE" type="STRING" size="256"  />
                <Column id="CS_CD" type="STRING" size="256"  />
                <Column id="PAN_ST_DT" type="STRING" size="256"  />
                <Column id="PAN_ED_DT" type="STRING" size="256"  />
                <Column id="CLSG_ST_DT" type="STRING" size="256"  />
                <Column id="CLSG_ED_DT" type="STRING" size="256"  />
                <Column id="UPP_AIS_TP_CD" type="STRING" size="256"  />
                <Column id="PAN_SS" type="STRING" size="256"  />
                <Column id="AIS_TP_CD" type="STRING" size="256"  />
                <Column id="PREVIEW" type="STRING" size="256"  />
                <Column id="SCH_TY" type="STRING" size="256"  />
                <Column id="SCH_ARA" type="STRING" size="256"  />
                <Column id="SCH_PAN_SS" type="STRING" size="256"  />
                <Column id="AIS_TP_CD_INT" type="STRING" size="256"  />
                <Column id="MVIN_QF" type="STRING" size="256"  />
        </ColumnInfo>
        <Rows>
                <Row>
                        <Col id="CNP_CD" />
                        <Col id="PG_SZ">100</Col>
                        <Col id="PAGE">1</Col>
                        <Col id="CS_CD">CNP_CD</Col>
                        <Col id="PAN_ST_DT">20200711</Col>
                        <Col id="PAN_ED_DT">20200911</Col>
                        <Col id="CLSG_ST_DT" />
                        <Col id="CLSG_ED_DT" />
                                <Col id="UPP_AIS_TP_CD">06</Col>
                                <Col id="PAN_SS">접수중</Col>
                                <Col id="AIS_TP_CD">10</Col>
                                <Col id="PREVIEW">N</Col>
                                <Col id="SCH_TY">0</Col>
                                <Col id="SCH_ARA">0</Col>
                                <Col id="SCH_PAN_SS">2</Col>
                                <Col id="AIS_TP_CD_INT" />
                                <Col id="MVIN_QF" />
                        </Row>
                </Rows>
        </Dataset>
</Root>"""
data = data.encode("utf-8")
response = requests.post("https://apply.lh.or.kr/lhCmcNoSessionAdapter.lh?serviceID=OCMC_LCC_SIL_SILSNOT_L0001",data=data,headers={'Content-Type':'text/xml'})
soup = BeautifulSoup(response.text, 'xml')

nameList = [i.text for i in soup.select('Row > #PAN_NM')]
endList = [i.text for i in soup.select('Row > #CLSG_DT')]
locationList = [i.text for i in soup.select('Row > #CNP_CD_NM')]
ondateList = [i.text for i in soup.select('Row > #PAN_NT_ST_DT')]
numlist = []
alllist = []
target1 = '서울특별시'
target2 = '경기도'
if locationList.count(target1) != 0:
    index = -1
    for _ in range(locationList.count(target1)):
        index = locationList.index(target1, index + 1)
        numlist.append(index)
if locationList.count(target2) != 0:
    index = -1
    for _ in range(locationList.count(target2)):
        index = locationList.index(target2, index + 1)
        numlist.append(index)
if numlist != []:
    for i in numlist:
        alllist.append("%s %s %s" % (nameList[i], locationList[i], endList[i]))
data = """<?xml version="1.0" encoding="UTF-8"?>
<Root xmlns="http://www.nexacroplatform.com/platform/dataset">
    <Parameters>
        <Parameter id="_ga">GA1.3.1263763937.1599781034</Parameter>
        <Parameter id="_fbp">fb.2.1599781061325.1589399029</Parameter>
        <Parameter id="_gid">GA1.3.1122758519.1599958349</Parameter>
        <Parameter id="_gat_gtag_UA_133417796_16">1</Parameter>
        <Parameter id="NetFunnel_ID">5002%3A200%3Akey%3DD83DB44C858FC80C4A6609964638C4167C19E30855CF1E58C00F29E923B3A0CCAC0CBDC9C1AA005AC86D71C44C8F121501211FFC405404391FAEADDF71AA05A831B69E520A7729F6DB03099B15C588B2A0FB572843A7C76FA9217D419DDCB578D8CABE77EB10151EE39B54F9739C824431372C312C30%26nwait%3D0%26nnext%3D0%26tps%3D0%26ttl%3D0%26ip%3Dntfnnl.myhome.go.kr%26port%3D443</Parameter>
    </Parameters>
    <Dataset id="dsSch">
        <ColumnInfo>
            <Column id="PAN_NM" type="STRING" size="256"  />
            <Column id="CNP_CD" type="STRING" size="256"  />
            <Column id="PG_SZ" type="STRING" size="256"  />
            <Column id="PAGE" type="STRING" size="256"  />
            <Column id="CS_CD" type="STRING" size="256"  />
            <Column id="PAN_ST_DT" type="STRING" size="256"  />
            <Column id="PAN_ED_DT" type="STRING" size="256"  />
            <Column id="CLSG_ST_DT" type="STRING" size="256"  />
            <Column id="CLSG_ED_DT" type="STRING" size="256"  />
            <Column id="UPP_AIS_TP_CD" type="STRING" size="256"  />
            <Column id="PAN_SS" type="STRING" size="256"  />
            <Column id="AIS_TP_CD" type="STRING" size="256"  />
            <Column id="PREVIEW" type="STRING" size="256"  />
            <Column id="SCH_TY" type="STRING" size="256"  />
            <Column id="SCH_ARA" type="STRING" size="256"  />
            <Column id="SCH_PAN_SS" type="STRING" size="256"  />
            <Column id="AIS_TP_CD_INT" type="STRING" size="256"  />
            <Column id="MVIN_QF" type="STRING" size="256"  />
        </ColumnInfo>
        <Rows>
            <Row>
                <Col id="CNP_CD" />
                <Col id="PG_SZ">50</Col>
                <Col id="PAGE">1</Col>
                <Col id="CS_CD">CNP_CD</Col>
                <Col id="PAN_ST_DT">20200713</Col>
                <Col id="PAN_ED_DT">20200913</Col>
                <Col id="CLSG_ST_DT" />
                <Col id="CLSG_ED_DT" />
                <Col id="UPP_AIS_TP_CD">06</Col>
                <Col id="PAN_SS">접수중</Col>
                <Col id="AIS_TP_CD">07</Col>
                <Col id="PREVIEW">N</Col>
                <Col id="SCH_TY">0</Col>
                <Col id="SCH_ARA">0</Col>
                <Col id="SCH_PAN_SS">2</Col>
                <Col id="AIS_TP_CD_INT" />
                <Col id="MVIN_QF" />
            </Row>
        </Rows>
    </Dataset>
</Root>"""
data = data.encode("utf-8")
response = requests.post("https://apply.lh.or.kr/lhCmcNoSessionAdapter.lh?serviceID=OCMC_LCC_SIL_SILSNOT_L0001",data = data,headers ={"Content-Type":"text / xml"})
soup2 = BeautifulSoup(response.text, 'xml')

nameList = [i.text for i in soup2.select('Row > #PAN_NM')]
endList = [i.text for i in soup2.select('Row > #CLSG_DT')]
locationList = [i.text for i in soup2.select('Row > #CNP_CD_NM')]
ondateList = [i.text for i in soup2.select('Row > #PAN_NT_ST_DT')]

numlist = []
alllist2 = []
if locationList.count(target1) != 0:
    index = -1
    for _ in range(locationList.count(target1)):
        index = locationList.index(target1, index + 1)
        numlist.append(index)
if locationList.count(target2) != 0:
    index = -1
    for _ in range(locationList.count(target2)):
        index = locationList.index(target2, index + 1)
        numlist.append(index)

if numlist != []:
    for i in numlist:
        alllist2.append("%s %s %s" % (nameList[i], locationList[i], endList[i]))



data = """<?xml version="1.0" encoding="UTF-8"?>
<Root xmlns="http://www.nexacroplatform.com/platform/dataset">
    <Parameters>
        <Parameter id="_ga">GA1.3.1263763937.1599781034</Parameter>
        <Parameter id="_fbp">fb.2.1599781061325.1589399029</Parameter>
        <Parameter id="_gid">GA1.3.1122758519.1599958349</Parameter>
        <Parameter id="_gat_gtag_UA_133417796_16">1</Parameter>
        <Parameter id="NetFunnel_ID">5002%3A200%3Akey%3DD83DB44C858FC80C4A6609964638C4167C19E30855CF1E58C00F29E923B3A0CCAC0CBDC9C1AA005AC86D71C44C8F121501211FFC405404391FAEADDF71AA05A831B69E520A7729F6DB03099B15C588B2A0FB572843A7C76FA9217D419DDCB578D8CABE77EB10151EE39B54F9739C824431372C312C30%26nwait%3D0%26nnext%3D0%26tps%3D0%26ttl%3D0%26ip%3Dntfnnl.myhome.go.kr%26port%3D443</Parameter>
    </Parameters>
    <Dataset id="dsSch">
        <ColumnInfo>
            <Column id="PAN_NM" type="STRING" size="256"  />
            <Column id="CNP_CD" type="STRING" size="256"  />
            <Column id="PG_SZ" type="STRING" size="256"  />
            <Column id="PAGE" type="STRING" size="256"  />
            <Column id="CS_CD" type="STRING" size="256"  />
            <Column id="PAN_ST_DT" type="STRING" size="256"  />
            <Column id="PAN_ED_DT" type="STRING" size="256"  />
            <Column id="CLSG_ST_DT" type="STRING" size="256"  />
            <Column id="CLSG_ED_DT" type="STRING" size="256"  />
            <Column id="UPP_AIS_TP_CD" type="STRING" size="256"  />
            <Column id="PAN_SS" type="STRING" size="256"  />
            <Column id="AIS_TP_CD" type="STRING" size="256"  />
            <Column id="PREVIEW" type="STRING" size="256"  />
            <Column id="SCH_TY" type="STRING" size="256"  />
            <Column id="SCH_ARA" type="STRING" size="256"  />
            <Column id="SCH_PAN_SS" type="STRING" size="256"  />
            <Column id="AIS_TP_CD_INT" type="STRING" size="256"  />
            <Column id="MVIN_QF" type="STRING" size="256"  />
        </ColumnInfo>
        <Rows>
            <Row>
                <Col id="CNP_CD" />
                <Col id="PG_SZ">50</Col>
                <Col id="PAGE">1</Col>
                <Col id="CS_CD">CNP_CD</Col>
                <Col id="PAN_ST_DT">20200713</Col>
                <Col id="PAN_ED_DT">20200913</Col>
                <Col id="CLSG_ST_DT" />
                <Col id="CLSG_ED_DT" />
                <Col id="UPP_AIS_TP_CD">06</Col>
                <Col id="PAN_SS">접수중</Col>
                <Col id="AIS_TP_CD">08</Col>
                <Col id="PREVIEW">N</Col>
                <Col id="SCH_TY">0</Col>
                <Col id="SCH_ARA">0</Col>
                <Col id="SCH_PAN_SS">2</Col>
                <Col id="AIS_TP_CD_INT" />
                <Col id="MVIN_QF" />
            </Row>
        </Rows>
    </Dataset>
</Root>"""
data = data.encode("utf-8")
response = requests.post("https://apply.lh.or.kr/lhCmcNoSessionAdapter.lh?serviceID=OCMC_LCC_SIL_SILSNOT_L0001",data = data,headers ={"Content-Type":"text / xml"})
soup3 = BeautifulSoup(response.text, 'xml')

nameList = [i.text for i in soup3.select('Row > #PAN_NM')]
endList = [i.text for i in soup3.select('Row > #CLSG_DT')]
locationList = [i.text for i in soup3.select('Row > #CNP_CD_NM')]
ondateList = [i.text for i in soup3.select('Row > #PAN_NT_ST_DT')]

numlist = []
alllist3 = []
if locationList.count(target1) != 0:
    index = -1
    for _ in range(locationList.count(target1)):
        index = locationList.index(target1, index + 1)
        numlist.append(index)
if locationList.count(target2) != 0:
    index = -1
    for _ in range(locationList.count(target2)):
        index = locationList.index(target2, index + 1)
        numlist.append(index)

if numlist != []:
    for i in numlist:
        alllist3.append("%s %s %s" % (nameList[i], locationList[i], endList[i]))




text = "행복주택 접수중\n%s \n\n국민임대 접수중\n%s \n\n공공임대 접수중\n%s " % ('\n'.join(["%s"%i for i in alllist]), '\n'.join(["%s"%i for i in alllist2]),'\n'.join(["%s"%i for i in alllist3]))
iteration = 0
while not iteration == (len(text)//200)+1:

        r = datetime.today().weekday()
        talk_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
        with open("kakao_tokens.json", "r") as fp:
            tokens = json.load(fp)
        header = {
            "Authorization": "Bearer {%s}" % tokens["access_token"]}
        post = {
            "object_type": "text",
            "text": text[iteration*200:],
            "link": {
                "web_url": "https://developers.kakao.com",
                "mobile_web_url": "https://developers.kakao.com"
            },
            "button_title": "바로 확인"
        }
        data = {"template_object": json.dumps(post)}
        res = requests.post(talk_url, headers=header, data=data)
        if res.json().get('result_code') == 0:
            print('메시지를 성공적으로 보냈습니다.')
            iteration = iteration + 1
        else:
            refresh_tokens = "%s" % tokens["refresh_token"]
            url = "https://kauth.kakao.com/oauth/token"
            API_token = ''
            data = {
                "grant_type": "refresh_token",
                "client_id": API_token,
                "refresh_token": refresh_tokens
            }
            response = requests.post(url, data=data)
            new_accesstoken = response.json()
            tokens["access_token"] = new_accesstoken["access_token"]
            with open("kakao_tokens.json", "w") as fp:
                json.dump(tokens, fp)

