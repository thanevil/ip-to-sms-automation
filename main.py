from twilio.rest import Client
import urllib.request


external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
with open('IP.txt', 'r') as file:
    current_ip = file.read().rstrip()
# print(external_ip) #testing
# print(current_ip)  #testing

if external_ip == current_ip:
    # print("same")  #testing
    pass
else:
    with open('IP.txt', "w") as file:
        file.write(external_ip)
    # print("sms")  #testing
    client = Client("ssid", "auth token")
    client.messages.create(to=["+your number"], from_="+twillo number", body=external_ip)
