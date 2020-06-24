import requests

def FindInfo(string_text, html):
	u = html.split(string_text)[1]
	w = u.split("td")[0].split(">")[1].split("<")[0]
	return w
def FindWIFIInfo(GHz, html):
	if GHz == 2:
		u = html.split("Wi-Fi 2.4GHz")[1].split("th")[1]
		Transmit = u.split("Transmit")[1].split("tr")[0].split("<td>")[1].split("</td")[0]
		Receive = u.split("Receive")[1].split("tr")[0].split("<td>")[1].split("</td")[0]
		Total = [Transmit, Receive]
	if GHz == 5:
		u = html.split("Wi-Fi 5GHz")[1].split("th")[1]
		Transmit = u.split("Transmit")[1].split("tr")[0].split("<td>")[1].split("</td")[0]
		Receive = u.split("Receive")[1].split("tr")[0].split("<td>")[1].split("</td")[0]
		Total = [Transmit, Receive]
	return Total
def Combine(Array):
	return int(Array[0]) + int(Array[1])
def ConvertBytes(Byte, Type="GB"):
	if Type =="KB":
		return Byte/1024
	if Type =="MB":
		return Byte/1024/1024
	if Type =="GB":
		return round(Byte/1024/1024/1024, 2)
	if Type =="TB":
		return Byte/1024/1024/1024/1024
def GetHtml():
	return requests.get('http://192.168.1.254/xslt?PAGE=C_2_0').text.split("<h2>Traffic Statistics</h2>")[1]
if __name__ == '__main__':
	html = GetHtml()
	Ethernet_1 = [FindInfo("Ethernet_1 Ethernet_1_TX BYTE", html), FindInfo("Ethernet_1 Ethernet_1_RX BYTE", html)]
	Ethernet_2 = [FindInfo("Ethernet_2 Ethernet_2_TX BYTE", html), FindInfo("Ethernet_2 Ethernet_2_RX BYTE", html)]
	Ethernet_3 = [FindInfo("Ethernet_3 Ethernet_3_TX BYTE", html), FindInfo("Ethernet_3 Ethernet_3_RX BYTE", html)]
	Ethernet_4 = [FindInfo("Ethernet_4 Ethernet_4_TX BYTE", html), FindInfo("Ethernet_4 Ethernet_4_RX BYTE", html)]
	Ethernet_Total = [FindInfo("ETH_TOTAL ETH_TO_TX BYTE", html), FindInfo("ETH_TOTAL ETH_TO_RX BYTE", html)]
	WiFi_2d4GHz = FindWIFIInfo(2, html)
	WiFi_5GHz = FindWIFIInfo(5, html)
	print("Ethernet 1: " + str(ConvertBytes(Combine(Ethernet_1))))
	print("Ethernet 2: " + str(ConvertBytes(Combine(Ethernet_2))))
	print("Ethernet Total: " + str(ConvertBytes(Combine(Ethernet_1)+Combine(Ethernet_2)+Combine(Ethernet_3)+Combine(Ethernet_4))))
	print("Wi-Fi 2.4GHz: " + str(ConvertBytes(Combine(WiFi_2d4GHz))))
	print("Wi-Fi 5GHz: " + str(ConvertBytes(Combine(WiFi_5GHz))))
	print("Wi-Fi Total: " + str(ConvertBytes(Combine(WiFi_2d4GHz)+Combine(WiFi_5GHz))))
	print("Total Data: " + str(ConvertBytes(Combine(WiFi_2d4GHz)+Combine(WiFi_5GHz)+Combine(Ethernet_1)+Combine(Ethernet_2)+Combine(Ethernet_3)+Combine(Ethernet_4))))
