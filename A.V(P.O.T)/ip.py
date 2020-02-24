import pygeoip
import requests

#my_ip_addr=requests.get('https://api.ipify.org').text
my_ip_addr=input('please enter the ip to be searched: ')

gip=pygeoip.GeoIP('C:\\Users\\asus\\Downloads\\GeoliteCity.dat')
res=gip.record_by_addr(my_ip_addr)
#print(res)

for key,val in res.items():
    print(f'{key}:{val}')