from tkinter import *
import json
import pygeoip
import requests

#Dataset:- The Data will be fetched from .json file.
data=json.load(open("data.json","r"))

def strategy():
	#my_ip_addr=input('please enter the ip to be searched: ')
	my_ip=word.get()
	gip=pygeoip.GeoIP('C:\\Users\\asus\\Downloads\\GeoliteCity.dat')
	res=gip.record_by_addr(my_ip)
	for key,val in res.items():
				print(f'{key}:{val}')
	#my_ip=requests.get('https://whatismyipaddress.com/ip-lookup').text
	#print (my_ip)

def mean():
	m=word.get()
	m.lower()
	if(m in data):
	   yo=data[m]     #yo is a variable assigned to fetch from data.json
	   t.insert(END,yo)
	else:
	   yo1="This IP Doesnt Exist in Database. It can be V-IP" #yo1 throws exception of not getting IP.
	   t.insert(END,yo1)

def reset():    #reset button assigned to reset box
	word.set("")
	t.delete(1.0,END)

def exit1():  #exit1 button assigned to exit from box.
	window.destroy()



window=Tk()
window.title("VPN/PROXY DETECTOR")
window.configure(background='black')

#LAbel1:- This displays label DETECTOR in window
a=Label (window,text="Detector")
a.config(font=(40))
a.grid(row=0,column=0)


#LAbel2 
b=Label (window,text="Enter Input")  # LAbel 2 shows ENtering IP to besearched.
b.config(font=(30))
b.grid(row=1,column=1)

#Entry

word=StringVar() #Especially taking string value and not int for offline services.
e=Entry(window,textvariable=word,width=50)
e.grid(row=2,column=1)

#Button
bu=Button(window,text="SEARCH",bg="orange",width="20",command=mean) #This is a button to refer to 
bu.grid(row=3,column=1)

#Button
bu1=Button(window,text="GeoLocation",bg="orange",width="20",command=strategy)
bu1.grid(row=5,column=1)

#textbox
t=Text(window,height=10,width=60)
t.grid(row=4,column=1)

#Button2=reset
r=Button(window,text="RESET",bg="orange",width="10",command=reset)
r.grid(row=5,column=0)

#button3=exit
ex=Button(window,text="EXIT",bg="orange",width="10",command=exit1)
ex.grid(row=5,column=2)



window.mainloop()
