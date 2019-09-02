import tkinter
import webbrowser
from selenium import webdriver



def combine(list1):
	txt = ""
	for i in list1:
		txt = txt + i
	f = open('New_Chart.html','w') 
	f.write(txt)
	print("done")


damage_color = "#8B2323"
netural_color = "#36648B"
rank_bar_back_color = "rgba(0, 197, 205, 0.1)"
rank_bar__rank_color = "rgb(255, 127, 36)"
rank_boxplot_color = "rgba(255, 127, 36,0.8)"



def changeColor(new_colorlist):
	htmlf=open('ChartColorTest.html','r',encoding="utf-8")
	htmlcont=htmlf.read()


	color = htmlcont.split('//color')

	#print(color[1])
	new_color = []
	colorlist = []
	s = 0 
	n = 0 
	for i in color:
		if len(i.strip()) < 40:
			print(i.strip())
			templist = i.strip().split(": '")
			tempstr = templist[0] + ": '" + new_colorlist[s] + "'" + ","
			colorlist.append(n)
			new_color.append(tempstr)
			s =s + 1
		n = n +1
	print(colorlist)
	print(new_color)
	combine_list = []
	n = 0 
	for j in range(len(color)):
		if j not in colorlist:
			combine_list.append(color[j])
		else:
			combine_list.append(new_color[n])
			n = n + 1


	combine(combine_list)






	#combine(color)

def getcolor():
	colorlist = []

	damage_color = "#8B2323"
	netural_color = "#36648B"
	rank_bar_back_color = "rgba(0, 197, 205, 0.1)"
	rank_bar_rank_color = "rgb(255, 127, 36)"
	rank_boxplot_color = "rgba(255, 127, 36,0.8)"
		
	color1 = en1.get()
	if not color1:
		color1 = "#8B2323"
	print(color1)
	la.insert("insert","damage color is ")
	la.insert("insert",color1)
	la.insert("insert","\n")


	color2 = en2.get()
	if not color2:
		color2 = "#36648B"
	print(color2)
	la.insert("insert","netural color is ")
	la.insert("insert",color2)
	la.insert("insert","\n")

	color3 = en3.get()
	if not color3:
		color3 = "rgba(0, 197, 205, 0.1)"
	print(color3)
	la.insert("insert","rank bar back color is ")
	la.insert("insert",color3)
	la.insert("insert","\n")

	color4 = en4.get()
	if not color4:
		color4 = "rgb(255, 127, 36)"
	print(color4)
	la.insert("insert","rank bar rank color is ")
	la.insert("insert",color4)
	la.insert("insert","\n")

	color5 = en5.get()
	if not color5:
		color5 = "rgba(255, 127, 36,0.8)"
	print(color5)
	la.insert("insert","rank boxplot color is ")
	la.insert("insert",color5)
	la.insert("insert","\n")

	colorlist.append(color1)
	colorlist.append(color2)
	colorlist.append(color3)
	colorlist.append(color4)
	colorlist.append(color4)
	colorlist.append(color3)
	colorlist.append(color5)
	colorlist.append(color5)

	changeColor(colorlist)
	la.insert("insert","\n")
	la.insert("insert","change color complete!")
	

	webbrowser.open("New_Chart.html")





###grid#####

top = tkinter.Tk()
top.title("color change")
top.geometry("1000x800")

L1 = tkinter.Label(top, text="damage_color")
L1.grid(row=0,column=0)
en1 = tkinter.Entry(top,show =None)
en1.grid(row=0,column=1)
L2 = tkinter.Label(top, text="netural_color")
L2.grid(row=1,column=0)
en2 = tkinter.Entry(top,show =None)
en2.grid(row=1,column=1)
L3 = tkinter.Label(top, text="rank_bar_back_color")
L3.grid(row=2,column=0)
en3 = tkinter.Entry(top,show =None)
en3.grid(row=2,column=1)
L4 = tkinter.Label(top, text="rank_bar__rank_color")
L4.grid(row=3,column=0)
en4 = tkinter.Entry(top,show =None)
en4.grid(row=3,column=1)
L5 = tkinter.Label(top, text="rank_boxplot_color")
L5.grid(row=4,column=0)
en5 = tkinter.Entry(top,show =None)
en5.grid(row=4,column=1)

B = tkinter.Button(top, text ="change color!", command = getcolor, bg = "pink")
B.grid(row=6)

la = tkinter.Text(top,height = 15)
la.grid(row=7)

la.insert("insert","open New_chart.html to test it!")
la.insert("insert","\n")
la.insert("insert","exmaple: rgba(0, 197, 205, 0.1) , rgb(225,255,35) , blue , #36648B")
la.insert("insert","\n")

la.insert("insert","\n")

###grid end#####



top.mainloop()