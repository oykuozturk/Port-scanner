import socket,sys,threading,time
from tkinter import *

ip_s = 0
ip_f = 0
log = []
ports = []
target = ''

def scanPort(target, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(4)
		c = s.connect_ex((target, port))
		if c == 0:
			m = ' Port %d \t[open]' % (port,)
			log.append(m)
			ports.append(port)
			listbox.insert("end", str(m))
			updateResult()
		s.close()
	except OSError: print('Too many open sockets. Port ' + str(port))
	except:
		c.close()
		s.close()
		sys.exit()
	sys.exit()
	
def updateResult():
	rtext = " [ " + str(len(ports)) + " / " + str(ip_f) + " ] ~ " + str(target)
	L27.configure(text = rtext)

def startScan():
	global ports, log, target, ip_f
	clearScan()
	log = []
	ports = []
	ip_s = int(L24.get())
	ip_f = int(L25.get())
	log.append('Port Scanner')
	log.append('='*14 + '\n')
	log.append(' Target:\t' + str(target))
	
	try:
		target = socket.gethostbyname(str(L22.get()))
		log.append(' IP Adr.:\t' + str(target))
		log.append(' Ports: \t[ ' + str(ip_s) + ' / ' + str(ip_f) + ' ]')
		log.append('\n')
		while ip_s <= ip_f:
			try:
				scan = threading.Thread(target=scanPort, args=(target, ip_s))
				scan.setDaemon(True)
				scan.start()
			except: time.sleep(0.01)
			ip_s += 1
	except:
		m = 'Target ' + str(L22.get()) + ' not found.'
		log.append(m)
		listbox.insert(0, str(m))

def clearScan():
	listbox.delete(0, 'end')

gui = Tk()
gui.title('Port Scanner')
gui.geometry("400x600+20+20")

m1c = '#c44949'
bgc = '#222222'
dbg = '#000000'
fgc = '#111111'

gui.tk_setPalette(background=bgc, foreground=m1c, activeBackground=fgc, activeForeground=bgc)

L11 = Label(gui, text = "PORT SCANNER",  font=("Verdana 10 italic", 16))
L11.place(x = 16, y = 30)

L21 = Label(gui, text = "Target: ")
L21.place(x = 16, y = 90)

L22 = Entry(gui)
L22.place(x = 100, y = 90)


L23 = Label(gui, text = "Ports: ")
L23.place(x = 16, y = 158)

L24 = Entry(gui)
L24.place(x = 100, y = 158, width = 95)

L25 = Entry(gui)
L25.place(x = 220, y = 158, width = 95)

L26 = Label(gui, text = "Results: ")
L26.place(x = 16, y = 220)

L27 = Label(gui)
L27.place(x = 180, y = 220)

frame = Frame(gui)
frame.place(x = 16, y = 275, width = 370, height = 215)
listbox = Listbox(frame, width = 40, height = 13)
listbox.place(x = 0, y = 0)
listbox.bind('<<ListboxSelect>>')

B11 = Button(gui, text = "START", command=startScan)
B11.place(x = 16, y = 520, width = 170)

gui.mainloop()







