from utils.signer import Argus, Ladon, Gorgon, md5
from urllib.parse import urlencode
import requests, json, string,time, random,re, secrets,os
ts = str(int(time.time() * 1000))
tss =str(int(time.time()))
def xor(string: str) -> str:
 return "".join([hex(ord(_) ^ 5)[2:] for _ in string])
class SizaGod:
    def __init__(self) -> None:
        self.registered = 0
    def sign(self, params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "v04.04.05-ov-android", sdk_version: int = 134744640, platform: int = 0, unix: int = None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        if not unix: unix = int(time.time())    
        return Gorgon(params, unix, payload, cookie).get_value() | {"x-ladon":Ladon.encrypt(unix, license_id, aid),"x-argus":Argus.get_sign(params, x_ss_stub, unix,platform=platform,aid=aid,license_id=license_id,sec_device_id=sec_device_id,sdk_version=sdk_version_str,sdk_version_int=sdk_version)}
    def report(self) -> None:
        params={'owner_id':id,'object_id':id,'report_type': "user",'extra_log_params': "{\"last_from_group_id\":\""+str(random.randint(1000000000000000000, 9999999999999999999))+"\",\"search_id\":\"\"}",'enter_from': "others_homepage",'isFirst': "1",'no_hw': "1",'report_desc': "",'uri': "",'reason': "9004",'category': "",'request_tag_from': "h5",'iid': f"{random.randint(1000000000000000000, 9999999999999999999)}",'device_id': f"{random.randint(1000000000000000000, 9999999999999999999)}",'ac': "WIFI",'channel': "googleplay",'aid': "1233",'app_name': "musical_ly",'version_code': "350304",'version_name': "35.3.4",'device_platform': "android",'os': "android",'ab_version': "35.3.4",'ssmix': "a",'device_type': "CPH2121",'device_brand': "OPPO",'language': "en",'os_api': "31",'os_version': "12",'openudid': "3e57b1286e16a0d1",'manifest_version_code': "2023503040",'resolution': "1080*2158",'dpi': "480",'update_version_code': "2023503040",'_rticket':ts,'is_pad': "0",'current_region': "CA",'app_type': "normal",'sys_region': "CA",'last_install_time':str(int(tss)-random.randint(50000, 100000)),'timezone_name': "Africa/Algiers",'carrier_region_v2': "603",'residence': "CA",'app_language': "en",'carrier_region': "CA",'ac2': "wifi",'uoo': "0",'op_region': "CA",'timezone_offset': "3600",'build_number': "35.3.4",'host_abi': "arm64-v8a",'locale': "en",'region': "CA",'ts':tss,'cdid': "840ea37f-a4a2-4398-a3eb-bf33da899438"}
        headers = {'User-Agent': "com.zhiliaoapp.musically/2023503040 (Linux; U; Android 12; en; CPH2121; Build/SP1A.210812.016; Cronet/TTNetVersion:711894ae 2024-06-04 QuicVersion:5f987023 2024-05-10)",'x-tt-dm-status': "login=0;ct=0;rt=7",'sdk-version': "2",'tt-ticket-guard-iteration-version': "0",'tt-ticket-guard-version': "3",'passport-sdk-settings': "x-tt-token,sec_user_id",'passport-sdk-sign': "x-tt-token,sec_user_id",'passport-sdk-version': "6010290",'x-tt-bypass-dp': "1",'x-vc-bdturing-sdk-version': "2.3.8.i18n",'content-type': "application/x-www-form-urlencoded; charset=UTF-8",}
        headers.update(self.sign(urlencode(params)))
        response = requests.get(url = "https://api31-normal-useast1a.tiktokv.com/aweme/v2/aweme/feedback/",params = params,headers = headers,)
        if response.json()['status_message'] == '':
         print(f'[√] Success : {response.json()}')
        else:
         print(f'[×] Error : {response.text}')
id=str(input('Target ID : '))
while True:
 SizaGod().report()
