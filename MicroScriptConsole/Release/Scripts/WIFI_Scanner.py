import time
import network
import gc
gc.enable()
from console import Display

class WiFiScanner:
    def __init__(self):
        self.name = ''
        self.strength = ''
        self.status = ''
        self.kanaal = ''
        self.oled = Display()
        self.wlan = network.WLAN(network.STA_IF)
        self.prepare_wifi()
        time.sleep_ms(5000)
        self.oled.print_wrapped("Performing scan...")
        time.sleep(0.5)
        self.oled.clear(0, 1)
        self.format()

    def prepare_wifi(self):
        if not self.wlan.active():
            self.oled.print_wrapped("Turning the WiFi ON.")
            time.sleep(0.5)
            self.oled.clear(0, 1)
            self.wlan.active(True)
        elif self.wlan.active() and self.wlan.isconnected():
            self.oled.print_wrapped("Disconnecting from WiFi connection.")
            time.sleep(0.5)
            self.oled.clear(0, 1)
            self.wlan.disconnect()

    def format(self):
        try:
            wlan_list = self.wlan.scan()
        except:
            wlan_list = [['NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE']]
        for intCounter in wlan_list:
            self.name = str(intCounter[0], 'utf8')
            self.strength = str(intCounter[3]) + ' dBm'
            self.kanaal = 'Channel: ' + str(intCounter[2])
            self.status = self.get_secure(intCounter[4])
            self.show_info()
            self.oled.clear(0, 1)

    @staticmethod
    def get_secure(num):
        strReturn = ""
        try:
            if int(num) == 0:
                strReturn = 'Open wifi'
            elif int(num) == 1:
                strReturn = 'WEP'
            elif int(num) ==2:
                strReturn = 'WPA-PSK'
            elif int(num) == 3:
                strReturn = 'WPA2-PSK'
            elif int(num) == 4:
                strReturn = 'WPA/WPA2-PSK'
            else:
                strReturn = str("UNKNOWN %s" % num)

            return strReturn
        except:
            return strReturn

    def show_info(self):
        self.oled.clear(0, 1)
        if len(self.name) > 15:
            self.oled.print_on_line(self.name[0:15],0)
            self.oled.print_on_line(self.name[15:int(len(self.name))],1)
        else:
            self.oled.print_on_line(self.name,0)

        self.oled.print_on_line(self.strength, 2, 30)
        self.oled.print_on_line(self.status, 3, 30)
        self.oled.print_on_line(self.kanaal, 4, 30)
        self.oled.print_on_line((str(gc.mem_free())+ " B"), 5, 30)
        time.sleep_ms(10000)

ScannedWiFi = WiFiScanner()
