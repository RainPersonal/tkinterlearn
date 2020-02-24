# -*- coding: utf-8 -*-
import tkinter  as tk
from tkinter import filedialog
from tkinter import ttk
import tkinter.messagebox as messagebox
from elements import elements, get_class_by_index, ele_button, get_index_by_symbol
import tkinter.font as tf
import json
import os, sys, shutil

file = None
treeview = None
tarview = None
# dumpflag = False
def get_screen_size(window):
    return window.winfo_screenwidth(),window.winfo_screenheight()
 
def get_window_size(window):
    return window.winfo_reqwidth(),window.winfo_reqheight()
 
def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    # print(size)
    root.geometry(size)

def change_symbol(buttons):
	if buttons[-1]['text'] == '符号':
		buttons[-1]['text'] = '名称'
		mark = True
	else:
		buttons[-1]['text'] = '符号'
		mark = False
	for i in range(len(buttons)-1):
		if mark:
			buttons[i].btn['text'] = buttons[i].dic['index']+'\n'+buttons[i].dic['zhName']
		else:
			buttons[i].btn['text'] = buttons[i].dic['index']+'\n'+buttons[i].dic['symbol']
 
# 定义元素弹框显示信息
def showelelabel(eledic):
	elelabel = tk.Toplevel()
	elelabel.title("元素：{}".format(eledic['zhName']))
	center_window(elelabel, 300, 200)
	text = ''
	for i in eledic.keys():
		text += (i + ':')
		if i == 'class':
			text += get_class_by_index(eledic[i])
		else:
			text += eledic[i]
		text += '\n'
	tk.Label(elelabel, text=text).pack()
	elelabel.focus_set()
	elelabel.bind("<Return>",lambda event:elelabel.destroy())
	elelabel.mainloop()

# 定义元素输入框信息
def get_input(eledic):
	if treeview.tag_has(eledic['index']):
		messagebox.showinfo('提示','已经存在{}元素成分，\n请删除后重新录入。'.format(eledic['symbol']))
		return
	def checknumber(content):
	    if content.replace('.','',1).isdecimal() or content=="":
	        return True
	    else:
	        return False
	elelabel = tk.Toplevel()
	comCheckNum = elelabel.register(checknumber)
	elelabel.title("元素：{}".format(eledic['zhName']))
	center_window(elelabel, 350, 140)
	elelabel.resizable(0,0)
	centerframe = ttk.Frame(elelabel, relief='flat', borderwidth=5, width=50, height=50)
	elefont = tf.Font(family='等线', size=30,weight=tf.BOLD,underline=0,overstrike=0)
	decfont = tf.Font(family='等线', size=15,weight=tf.BOLD,underline=0,overstrike=0)
	tk.Label(centerframe, text=eledic['symbol'], relief='groove', width=4,height=2, font=elefont).grid(row=1,column=0,rowspan=2,columnspan=2)
	tk.Label(centerframe, text='最小值', relief='flat', width=6,height=1, font=decfont).grid(row=1,column=3,columnspan=2)
	tk.Label(centerframe, text='最大值', relief='flat', width=6,height=1, font=decfont).grid(row=2,column=3,columnspan=2)
	min_limi = tk.Entry(centerframe,width=8,bd=3,validate='key',validatecommand=(comCheckNum, '%P'),font=decfont)
	min_limi.grid(row=1,column=5,columnspan=2)
	max_limi = tk.Entry(centerframe,width=8,bd=3,validate='key',validatecommand=(comCheckNum, '%P'),font=decfont)
	max_limi.grid(row=2,column=5,columnspan=2)
	min_limi.focus_set()
	def focus_cg(ev=None):
		max_limi.focus_set()
		max_limi.select_range(0,len(max_limi.get()))
	def updatatreeview(ev=None):
		if min_limi.get()=='':
			lower_limi = 0.0
		else:
			lower_limi = float(min_limi.get())
		try:
			upper_limi = float(max_limi.get())
		except:
			elelabel.destroy()
			return
		if upper_limi<lower_limi:
			messagebox.showerror('错误','成分上下限出错，请重新输入！')
			min_limi.focus_set()
			min_limi.select_range(0,len(min_limi.get()))
			return
		treeview.insert('','end',text=eledic['zhName'],tags=eledic['index'],values=(eledic['symbol'],lower_limi,upper_limi))
		elelabel.destroy()
	def quit_input():
		elelabel.destroy()
	min_limi.bind("<Return>", focus_cg)
	max_limi.bind("<Return>", updatatreeview)
	tk.Button(centerframe, text='确认', relief='raised', width=6,height=1,font=decfont,command=updatatreeview).grid(row=3,column=1,columnspan=2)
	tk.Button(centerframe, text='取消', relief='raised', width=6,height=1,font=decfont,command=quit_input).grid(row=3,column=5,columnspan=2)
	centerframe.pack()
	elelabel.bind("<Escape>",lambda event:elelabel.destroy())
	elelabel.mainloop()
# 新建性能
def creat_mec_pro():
	if len(treeview.tag_has("Tension_property"))>=2:
		messagebox.showinfo('提示','性能数据已经存在，\n请删除后重新录入。')
		return
	def checknumber(content):
	    if content.replace('.','',1).isdecimal() or content=="":
	        return True
	    else:
	        return False
	Ten_Pro = tk.Toplevel()
	decfont = tf.Font(family='等线', size=13,weight=tf.BOLD,underline=0,overstrike=0)
	comCheckNum = Ten_Pro.register(checknumber)
	Ten_Pro.title("拉伸性能")
	center_window(Ten_Pro, 280, 125)
	Ten_Pro.resizable(0,0)
	centerframe = ttk.Frame(Ten_Pro, relief='groove', borderwidth=5, width=50, height=50)
	tk.Label(centerframe, text='棒拉伸MPa', relief='flat', width=8,height=1, font=decfont).grid(row=0,column=2,columnspan=2)
	tk.Label(centerframe, text='延伸率%', relief='flat', width=8,height=1, font=decfont).grid(row=0,column=4,columnspan=2)
	tk.Label(centerframe, text='室温性能', relief='flat', width=8,height=1, font=decfont).grid(row=1,column=0,columnspan=2)
	tk.Label(centerframe, text='高温性能', relief='flat', width=8,height=1, font=decfont).grid(row=2,column=0,columnspan=2)
	room_min = tk.Entry(centerframe,width=8,bd=3,validate='key',validatecommand=(comCheckNum, '%P'),font=decfont)
	room_min.grid(row=1,column=2,columnspan=2)
	room_max = tk.Entry(centerframe,width=8,bd=3,validate='key',validatecommand=(comCheckNum, '%P'),font=decfont)
	room_max.grid(row=1,column=4,columnspan=2)
	high_min = tk.Entry(centerframe,width=8,bd=3,validate='key',validatecommand=(comCheckNum, '%P'),font=decfont)
	high_min.grid(row=2,column=2,columnspan=2)
	high_max = tk.Entry(centerframe,width=8,bd=3,validate='key',validatecommand=(comCheckNum, '%P'),font=decfont)
	high_max.grid(row=2,column=4,columnspan=2)
	def focus_rm(curr_ent):
		curr_ent.focus_set()
		curr_ent.select_range(0,len(curr_ent.get()))
	def updatatreeview(ev=None):
		if (room_mech := room_min.get()) != '' and (room_exten := room_max.get()) != '':
			# print(room_mech,room_exten)
			tarview.insert('','end',text='室温性能',tags='Tension_property',values=('室温性能',float(room_mech),float(room_exten)))
		if (high_mech := high_min.get()) != '' and (high_exten := high_max.get()) != '':
			# print(high_mech,high_exten)
			tarview.insert('','end',text='高温性能',tags='Tension_property',values=('高温性能',float(high_mech),float(high_exten)))
		Ten_Pro.destroy()
	def quit_input():
		Ten_Pro.destroy()
	room_min.focus_set()
	room_min.bind("<Return>", lambda event:focus_rm(room_max))
	room_max.bind("<Return>", lambda event:focus_rm(high_min))
	high_min.bind("<Return>", lambda event:focus_rm(high_max))
	high_max.bind("<Return>", updatatreeview)
	tk.Button(centerframe, text='确认', relief='raised', width=6,height=1,font=decfont,command=updatatreeview).grid(row=3,column=1,columnspan=2)
	tk.Button(centerframe, text='取消', relief='raised', width=6,height=1,font=decfont,command=quit_input).grid(row=3,column=3,columnspan=2)
	centerframe.pack()
	Ten_Pro.bind("<Escape>",lambda event:Ten_Pro.destroy())
	Ten_Pro.mainloop()

# 新建性能
def temp_mec_pro():
	def checknumber(content):
	    if content.replace('.','',1).isdecimal() or content=="":
	        return True
	    else:
	        return False
	Ten_Pro = tk.Toplevel()
	decfont = tf.Font(family='等线', size=13,weight=tf.BOLD,underline=0,overstrike=0)
	comCheckNum = Ten_Pro.register(checknumber)
	Ten_Pro.title("拉伸性能")
	center_window(Ten_Pro, 280, 98)
	Ten_Pro.resizable(0,0)
	centerframe = ttk.Frame(Ten_Pro, relief='groove', borderwidth=5, width=50, height=50)
	tk.Label(centerframe, text='温度℃', relief='flat', width=8,height=1, font=decfont).grid(row=0,column=0,columnspan=2)
	tk.Label(centerframe, text='棒拉伸MPa', relief='flat', width=8,height=1, font=decfont).grid(row=0,column=2,columnspan=2)
	tk.Label(centerframe, text='延伸率%', relief='flat', width=8,height=1, font=decfont).grid(row=0,column=4,columnspan=2)
	Temperature = tk.Entry(centerframe,width=8,bd=3,validate='key',validatecommand=(comCheckNum, '%P'),font=decfont)
	Temperature.grid(row=1,column=0,columnspan=2)
	Tension = tk.Entry(centerframe,width=8,bd=3,validate='key',validatecommand=(comCheckNum, '%P'),font=decfont)
	Tension.grid(row=1,column=2,columnspan=2)
	Elongation = tk.Entry(centerframe,width=8,bd=3,validate='key',validatecommand=(comCheckNum, '%P'),font=decfont)
	Elongation.grid(row=1,column=4,columnspan=2)
	def focus_rm(curr_ent):
		curr_ent.focus_set()
		curr_ent.select_range(0,len(curr_ent.get()))
	def updatatreeview(ev=None):
		Tem = Temperature.get()
		Ten = Tension.get()
		Elong = Elongation.get()
		if Tem == '':
			Tem = 20.0
		if Ten != '' and Elong != '':
			tarview.insert('','end',text='拉伸性能',tags='Tension_property',values=(float(Tem),float(Ten),float(Elong)))
		Ten_Pro.destroy()
	def quit_input():
		Ten_Pro.destroy()
	Temperature.focus_set()
	Temperature.bind("<Return>", lambda event:focus_rm(Tension))
	Tension.bind("<Return>", lambda event:focus_rm(Elongation))
	Elongation.bind("<Return>", updatatreeview)
	tk.Button(centerframe, text='确认', relief='raised', width=6,height=1,font=decfont,command=updatatreeview).grid(row=3,column=1,columnspan=2)
	tk.Button(centerframe, text='取消', relief='raised', width=6,height=1,font=decfont,command=quit_input).grid(row=3,column=3,columnspan=2)
	centerframe.pack()
	Ten_Pro.bind("<Escape>",lambda event:Ten_Pro.destroy())
	Ten_Pro.mainloop()

def callbackClosetop(window):
	global file
	if file != None and messagebox.askyesno('提示', '需要保存文件吗？'):
		dump2file()
	elif file != None:
		file.close()
		file=None
	window.destroy()

def delete_item():
	for i in treeview.selection():
		treeview.delete(i)
	for i in tarview.selection():
		tarview.delete(i)

# def ini_con_data():
# 	print("初始化合金参数")

def get_name(Alloycont,Alloyprop):
	def submit(ev = None):
		global file
		filename = Alloy_name.get()
		if not os.path.exists('data'):
			os.mkdir('data')
		if not os.path.exists(os.path.join('data',filename+'.txt')):
			mode = 'w+'
			# print("w")
		else:
			mode = 'r+'
			# print("r")
		# print("filepath:",os.path.abspath(filepath)==os.path.abspath(os.path.join('data',filename+'.txt')))
		if filepath != None and os.path.abspath(filepath) != os.path.abspath(os.path.join('data',filename+'.txt')):
			# print("come in")
			shutil.copyfile(filepath,os.path.join('data',filename+'.txt'))
		file = open(os.path.join('data',filename+'.txt'),mode,encoding="utf-8")
		if treeview != None and tarview != None:
			for line in file.readlines():
				dic = json.loads(line)
				# print(dic['text'],type(dic['text']))
				if type(dic['tags'][0]) is int:
					treeview.insert('','end',text=dic['text'],tags=dic['tags'],values=dic['values'])
					# print(type(dic['tags'][0]),dic,dic['tags'][0]) 
				if type(dic['tags'][0]) is str:
					tarview.insert('','end',text=dic['text'],tags=dic['tags'],values=dic['values'])
		Alloycont.set(filename+'合金成分')
		Alloyprop.set(filename+'合金性能')
		name_win.quit()
		name_win.destroy()
	def openfile():
		path = filedialog.askopenfilename(initialdir=os.path.join('data'),filetypes=[("文本文档",".txt"),("所有文件","*")])
		fpath,fname = os.path.split(path)
		# print(type(fpath),"....",fname)
		name_win.focus_set()
		if fpath != '' and fname != '':
			Alloy_name.set(fname.replace('.txt',''))
			nonlocal filepath
			filepath = path
	if file != None:
		# print("duquwenjian")
		dump2file()
	filepath = None
	ftinput_name = tf.Font(family='等线', size=15,weight=tf.BOLD,underline=0,overstrike=0)
	Alloy_name = tk.StringVar()
	name_win = tk.Toplevel()
	name_win.title('合金牌号录入')
	center_window(name_win, max_width*0.2, max_height*0.1)
	name_frame=ttk.Frame(name_win,relief='flat')
	tk.Label(name_frame,text='请输入新合金牌号',font = ftinput_name).grid(row=0,column=0,columnspan=2)
	Alloy = tk.Entry(name_frame,textvariable=Alloy_name)
	Alloy.focus_set()
	Alloy.grid(row=1,column=0,columnspan=2)
	tk.Button(name_frame, text = '载入', font = ftinput_name, command = openfile).grid(row=2,column=0)
	tk.Button(name_frame, text = '确认', font = ftinput_name, command = submit).grid(row=2,column=1)
	name_frame.pack()
	Alloy.bind("<Return>", submit)
	# name_win.bind("<Escape>",lambda event:name_win.destroy())
	# print("get_name6")
	name_win.mainloop()

def dump2file():
	# print(treeview.identify_column(0))
	# file.seek(0)
	# file.truncate()
	global file
	file.seek(0)
	file.truncate()
	for i in treeview.get_children():
		# print(type(treeview.item(i)))
		file.write(json.dumps(treeview.item(i),ensure_ascii=False)+'\n')
		treeview.delete(i)
		file.flush()
	for i in tarview.get_children():
		file.write(json.dumps(tarview.item(i),ensure_ascii=False)+'\n')
		tarview.delete(i)
		file.flush()
	file.close()
	file = None

def short_key(event,value,func,Alloycont,Alloyprop):
		# print("test comein",value.get())
		if event.keycode == 13:  #回车键判断，进行弹窗
			if len(string:=value.get().upper())>0:
				elenamestr = ''
				num = ''
				for i in string: # 建立循环取出数字和字母
					if i.isalpha():
						elenamestr += i
					if i.isdigit():
						num  += i
				value.set('')
				if len(num) >0:
					ele_index = int(num)-1
					if ele_index < len(elements) and ele_index>=0: # 通过数字打开输入框
						func(elements[ele_index])
						return
				if elenamestr in get_index_by_symbol.keys():  # 通过字母打开输入框
					func(elements[get_index_by_symbol[elenamestr]-1])
					return
				elif len(elenamestr)>0:
					return
				if ele_index < 0 and tarview != None: # 若为0则输入性能
					# creat_mec_pro()
					temp_mec_pro()
					return
			else:
				get_name(Alloycont,Alloyprop)
				return
		elif event.char.isdecimal():
			value.set(value.get()+event.char)
			return
		elif 64 < event.keycode < 91:
			value.set(value.get()+event.char)
			return
		elif event.keycode == 27 or event.keycode == 8:
			value.set('')
			return

def show(flag):
	fttop = tf.Font(family='等线', size=15,weight=tf.BOLD,underline=0,overstrike=0)
	fttitle = tf.Font(family='等线', size=30,weight=tf.BOLD,underline=0,overstrike=0)
	tfbutton = tf.Font(family='等线', size=14,weight=tf.BOLD,underline=0,overstrike=0)
	color = ["#0078d7","#ee6fb9","#47a8e8","#f27575","#9b85dd","#4fb180","#ff7f46","#67c3ef","#74ce18","#eba95d","#a59b78"]
	Alloycont = tk.StringVar() # 这里设置默认合金参数为GH4169
	Alloyprop = tk.StringVar()
	if flag:
		top = tk.Toplevel(get_name(Alloycont,Alloyprop))
		func = get_input  #表示获取输入框的信息
		title = '合金成分录入'
		xsize = 1240
		if len(Alloycont.get()) == 0:
			top.quit()
			top.destroy()
			return
	else:
		top = tk.Toplevel()
		func = showelelabel #表示回去显示元素信息框的标志
		title = '元素周期表'
		xsize = 1030
	# top = tk.Toplevel()0.67 1240 1030
	top.title('数据')
	center_window(top, xsize, 605)
	# print(max_width,max_height)
	top.resizable(0,0)
	tk.Label(top,relief = 'flat', text=title, font=fttitle).grid(row=0,column=0,columnspan=11)
	tk.Label(top,relief = 'flat', width=5).grid(row=1,column=0,rowspan=2)
	if flag:
		# 设置表格位置 利用fram进行组装
		# print("flag=True")
		tvframe = ttk.Frame(top,relief='groove',width=50)
		tk.Label(tvframe,relief='flat',textvariable=Alloycont,borderwidth=5,font=fttop).grid(row=0,column=0,columnspan=6)
		global treeview, tarview
		ele_columns = ("元素","最小值","最大值")
		# def selectItem(ev=None):
		#     curItem = treeview.focus()
		#     print(treeview.item(curItem))
		#     print(treeview.selection())
		treeview = ttk.Treeview(tvframe, height=15, show="headings", columns=ele_columns)
		treeview.column("元素", width=50, anchor='center') # 表示列,不显示
		treeview.column("最小值", width=80, anchor='center')
		treeview.column("最大值", width=80, anchor='center')
		treeview.heading("元素", text="元素") # 显示表头
		treeview.heading("最小值", text="最小值")
		treeview.heading("最大值", text="最大值")
		# treeview.insert('','end',text='铁',values=('Fe',0,1))
		# treeview.bind('<Button-1>', selectItem)
		treeview.grid(row=1, column=0, columnspan=6)
		tk.Label(tvframe,relief='flat',textvariable=Alloyprop,text='合金性能',borderwidth=5,font=fttop).grid(row=2,column=0,columnspan=6)
		tarview = ttk.Treeview(tvframe, height=7, show="headings")
		treeview.column("#0",width=50,anchor='center')
		tarview["columns"]=("表头","拉伸强度MPa","延伸率%")
		tarview.column("表头",width=60)
		tarview.column("拉伸强度MPa",width=85)
		tarview.column("延伸率%",width=65)
		tarview.heading("表头",text="")
		tarview.heading("拉伸强度MPa",text="拉伸强度MPa")
		tarview.heading("延伸率%",text="延伸率%")
		# tarview.insert("",0,text="室温拉伸" ,values=("室温拉伸","1","2")) #插入数据，
		# tarview.insert("",1,text="高温拉伸" ,values=("室温拉伸","1","2"))
		tarview.grid(row=3, column=0, columnspan=6)
		for line in file.readlines():
			dic = json.loads(line)
			# print(dic['text'],type(dic['text']))
			if type(dic['tags'][0]) is int:
				treeview.insert('','end',text=dic['text'],tags=dic['tags'],values=dic['values'])
				# print(type(dic['tags'][0]),dic,dic['tags'][0]) 
			if type(dic['tags'][0]) is str:
				tarview.insert('','end',text=dic['text'],tags=dic['tags'],values=dic['values'])
		# treeview.insert('','end',text= "碳", values=["C", "0.0", "0.12"],tags=[6])
		tk.Button(tvframe, relief = 'raised', text = '性能',padx=0,pady=0,width=5,height=1,font=tfbutton,command=temp_mec_pro).grid(row=4,column=0,columnspan=2)
		tk.Button(tvframe, relief = 'raised', text = '删除',padx=0,pady=0,width=5,height=1,font=tfbutton,command=delete_item).grid(row=4,column=2,columnspan=2)
		tk.Button(tvframe, relief = 'raised', text = '提交',padx=0,pady=0,width=5,height=1,font=tfbutton,command=lambda:get_name(Alloycont,Alloyprop)).grid(row=4,column=4,columnspan=2)
		tvframe.grid(row=0,column=12,rowspan=3,columnspan=6)
		#表格设置结束
	topframe = ttk.Frame(top, relief='groove', borderwidth=5, width=50, height=100)
	buttons = []
	for i in elements:
		buttons.append(ele_button(topframe, i, fttop, func))
		buttons[-1].btn.grid(row=int(i['row']),column=int(i['col']))
	buttons.append(tk.Button(topframe, relief = 'groove',text = '符号', padx=0,pady=0,width=4,
		height=1,bg=color[0],font = fttop,command=lambda:change_symbol(buttons)))
	buttons[-1].grid(row=1,column=16,columnspan=2)
	tk.Label(topframe, relief = 'flat', text = '*', padx=0,pady=0,width=4,height=2,font = fttop).grid(row=6,column=3)
	tk.Label(topframe, relief = 'flat', text = '**', padx=0,pady=0,width=4,height=2,font = fttop).grid(row=7,column=3)
	tk.Label(topframe, relief = 'flat', text = '*镧系', padx=0,pady=0,width=6,height=2,font = fttop).grid(row=8,column=1,columnspan=2)
	tk.Label(topframe, relief = 'flat', text = '**锕系', padx=0,pady=0,width=6,height=2,font = fttop).grid(row=9,column=1,columnspan=2)
	topframe.grid(row=1,column=1,columnspan=9)
	classframe = ttk.Frame(top,relief='groove', borderwidth=5, width=50, height=50)
	for i in range(10):
		tk.Label(classframe, relief = 'flat', text = get_class_by_index(i+1), 
			padx=0,pady=0,width=8,height=1,bg = color[i+1], font = fttop).grid(row=0,column=i)
	classframe.grid(row=2,column=1,columnspan=9)
	top.protocol("WM_DELETE_WINDOW", lambda:callbackClosetop(top))
	top.focus_set()
	# print(top.grid_size())
	shortcut=tk.StringVar()
	top.bind("<Key>", lambda event:short_key(event,shortcut,func,Alloycont,Alloyprop))
	top.mainloop()

root = tk.Tk()
root.title('高温合金数据录入')
max_width, max_height = get_screen_size(root)
center_window(root, max_width*0.25, max_height*0.2)
# 设置字体
ftroot = tf.Font(family='等线', size=18,weight=tf.BOLD,underline=0,overstrike=0)
root.resizable(0,0)
# root.maxsize(max_width, max_height)
# root.minsize(300, 240)
rootframe = ttk.Frame(root, relief='groove', borderwidth=5, width=50, height=50)
tk.Button(rootframe, relief = 'groove', text='创建新合金数据',width=20,height=2,font = ftroot,command=lambda:show(True)).pack(expand = tk.YES)
tk.Button(rootframe, relief = 'groove', text='元素周期表',width=20,height=2,font = ftroot,command=lambda:show(False)).pack(expand = tk.YES)
rootframe.pack(expand = tk.YES)
root.protocol("WM_DELETE_WINDOW", root.quit())
# root.bind("<Escape>",lambda event:root.destroy())
root.mainloop()
