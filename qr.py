import qrcode

wifi_name = input("Enter wifi name:").strip()
password = input("Enter password").strip()
name = input("give beautiful name:").strip()
print(wifi_name)
print(password)

data = "WIFI:S:" + wifi_name + ";T:WPA;P:" + password + ";;"

img = qrcode.make(data)
img.save(name+".png")
