from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *
from tkinter.scrolledtext import *
import random
import requests
import socket
import bs4
import matplotlib.pyplot as plt

class MyException(Exception):
	def __init__(self,msg):
		self.msg=msg
		showerror("Failure :",str(self.msg))


root=Tk()
root.title("Student Mangement System")
root.geometry("500x400+400+200")
root.configure(background="LIGHT GREEN")

def f1():
	entrno.focus()
	adst.deiconify()
	root.withdraw()

def f2():
	stdata.delete(1.0,END)
	vist.deiconify()
	root.withdraw()
	con=None
	try:
		con=connect("test.db")
		cursor=con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		i="RNO\t|\tNAME\t|\tMARKS\n"+"-"*40+"\n"
		stdata.insert(INSERT,i)
		for d in data:
			info=info+str(d[0])+"\t|\t"+str(d[1])+"\t|\t"+str(d[2])+"\n"
		stdata.insert(INSERT,info)
	except Exception as e:
		showerror("Select issue ",e)
	finally:
		if con is not None:
			con.close()
			
def f3():
	root.deiconify()
	adst.withdraw()

def f4():
	
	root.deiconify()
	vist.withdraw()
	
def f5():
	count=0
	con=None
	try:
		con=connect("test.db")
		rno=entrno.get()
		name=entname.get()
		marks=entmarks.get()
		if rno=="":
			count=1
			raise MyException("Roll no block should not be empty")
			
		elif name=="":
			count=1
			raise MyException("Name block should not be empty")
			
		elif marks=="":
			count=1	
			raise MyException("Marks block should not be empty")

		elif int(rno)<0:
			count=1
			raise MyException("Roll no should not negative")
			
		elif len(name)<2:
			count=1
			raise MyException("Name should contain atleast os 2 letter")
		
		elif int(marks)<0 or int(marks)>100:
			count=1
			raise MyException("Invalid marks")
	
		else:
			rno=int(rno)
			marks=int(marks)
		
		args=(rno,name,marks)
		cursor=con.cursor()
		sql="insert into student values('%d','%s','%d')"
		cursor.execute(sql % args)
		con.commit()
		showinfo("Success","record added")
		
	except Exception as e:
		if count==0:
			showerror("Failure:",e)
		else:
			pass	
	finally:
		entrno.delete(0,END)
		entname.delete(0,END)
		entmarks.delete(0,END)
		if con is not None:
			con.close()
			
def f6():
	try:
		s=""
		socket.create_connection( ("www.google.com", 80))
		res = requests.get("https://ipinfo.io/")
		data=res.json()		
		city_name=data['city']
		city=city_name.replace("ā","a")
		city=city.lower()
		a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
		a2 = "&q=" + city 
		a3 = "&appid=c6e315d09197cec231495138183954bd"
		api_address =  a1 + a2  + a3 		
		res1 = requests.get(api_address)
		data1=res1.json()
		t=data1['main']
		temp=t['temp']
		
		s=s+"Location : "+str(city.upper())+"\t\t Temp : "+str(temp)
		return s
		
	except OSError as e:
		showerrror("issue ", e)

def f7():
	try:
		socket.create_connection(("www.google.com",80))

		res=requests.get("https://www.brainyquote.com/quote_of_the_day")
	
		soup=bs4.BeautifulSoup(res.text,"lxml")
	
		data=soup.find("img",{"class":"p-qotd"})
	
		motd=data['alt']
		qotd="QOTD:"+str(motd)
		
		if len(qotd)>60:
			a=qotd[0:60]
			b=qotd[60:]
			i=b.index(" ")
			qotd=a+b[0:i]+"\n"+b[i:]


		return qotd
	except Exception as e:
		showerror("Issue :",e)
	
def f8():
	uentrno.delete(0,END)
	uentname.delete(0,END)
	uentmarks.delete(0,END)
	root.withdraw()	
	upst.deiconify()

def f9():
	try:
		count=0
		con=connect("test.db")
		rno=int(uentrno.get())
		name=uentname.get()
		marks=int(uentmarks.get())
		if len(name)<2:
			count=1
			raise MyException("Name should contain atleast 2 letters")
		elif marks<0 or marks>100:
			count=1
			raise MyException("Invalid Marks (marks>=0 and mraks<=100 ")
		
		args1=(name,rno)
		cursor=con.cursor()
		sql="update student set name ='%s' where rno='%d'"
		cursor=con.cursor()
		cursor.execute(sql % args1)
		if cursor.rowcount >=1:
			con.commit()
			showinfo("Succes", "Record name Updated")
		
		args2=(marks,rno)
		cursor=con.cursor()
		sql="update student set marks ='%d' where rno ='%d'"
		cursor=con.cursor()
		cursor.execute(sql % args2)
		if cursor.rowcount >=1:
			con.commit()
			showinfo("Succes", "Record Marks Updated")
		else:
			if count==0:
				showerror("Failure","Record doesnt exists")

		entrno.delete(0,END)
		entname.delete(0,END)
		entmarks.delete(0,END)
	except Exception as e:
		if count==0:
			showerror("Update Issue :",e)
			con.rollback()
	finally:
		if con is not None:
			con.close()
			
def f10():
	root.deiconify()
	upst.withdraw()

def f11():
	con=None
	try:
		con=connect("test.db")
		
		rno=int(dentrno.get())
		args=(rno)
		cursor=con.cursor()
		sql="delete from student where rno ='%d'"
		cursor.execute(sql % args)
		if cursor.rowcount >=1:
			con.commit()
			showinfo("Success:","Record Deleted")
		else:
			showerror("Failure:","Roll No doesnt exists")
	except Exception as e:
		showerror("delete Issue :",e)
		con.rollback()
	finally:
		dentrno.delete(0,END)
		if con is not None:
			con.close()
			
def f12():
	root.deiconify()
	dest.withdraw()
def f13():
	dentrno.focus()
	root.withdraw()
	dest.deiconify()

def f14():
	marks=[]
	name=[]
	colors=[]
	con=None
	try:
		con=connect("test.db")
		cursor=con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		data=cursor.fetchone()
		while data:
			marks.append(data[2])
			name.append(data[1])
			data=cursor.fetchone()
		color_list=["red","green","blue","orange","pink","purple"]
		for i in range(0,len(marks)):
			r=random.randrange(len(color_list))
			colors.append(color_list[r])
		plt.bar(name,marks,color=colors)
		plt.title("Batch Information!")
		plt.xlabel("Name")
		plt.ylabel("Marks")
		plt.show()
	except Exception as e:
		showerror("select issue",e)

	finally:
		if con is not None:
			con.close()
			


btnAdd=Button(root,text="Add",font=("arial",12,"bold"),width=10,command=f1)
btnView=Button(root,text="View",font=("arial",12,"bold"),width=10,command=f2)
btnUpdate=Button(root,text="Update",font=("arial",12,"bold"),width=10,command=f8)
btnDelete=Button(root,text="Delete",font=("arial",12,"bold"),width=10,command=f13)
btnCharts=Button(root,text="Charts",font=("arial",12,"bold"),width=10,command=f14)
lblloc=Label(root,text=f6(),font=("arial",18),bg="LIGHT GREEN",borderwidth=4,width=40,relief="ridge")
lblQuote=Label(root,text=f7(),font=("arial",10,"bold"),bg="LIGHT GREEN",borderwidth=4,width=60,relief="ridge")

btnAdd.pack(pady=5)
btnView.pack(pady=5)
btnUpdate.pack(pady=5)
btnDelete.pack(pady=5)
btnCharts.pack(pady=5)
lblloc.pack(pady=30)
lblQuote.pack(pady=5)
adst=Toplevel(root)
adst.title("Add Student")
adst.geometry("500x500+400+200")

adst.withdraw()
lblrno=Label(adst,text="Enter Roll No.",font=("arial",18,"bold"))
entrno=Entry(adst,bd=5,font=("arial",18,"bold"))
lblname=Label(adst,text="Enter Name:",font=("arial",18,"bold"))
entname=Entry(adst,bd=5,font=("arial",18,"bold"))
lblmarks=Label(adst,text="Enter marks:",font=("arial",18,"bold"))
entmarks=Entry(adst,bd=5,font=("arial",18,"bold"))
btnsave=Button(adst,text="Save",font=("arial",18,"bold"),width=5,command=f5)
btnback=Button(adst,text="Back",font=("arial",18,"bold"),width=5,command=f3)
lblrno.pack(pady=10)
entrno.pack(pady=10)
lblname.pack(pady=10)
entname.pack(pady=10)
lblmarks.pack(pady=10)
entmarks.pack(pady=10)
btnsave.pack(pady=10)
btnback.pack(pady=10)

vist=Toplevel(root)
vist.title("View Students")
vist.geometry("500x400+400+200")
vist.withdraw()

lblrecord=Label(vist,text="STUDENTS RECORD",font=("arial",18,"bold"))
stdata=ScrolledText(vist,width=60,height=10)
btnvback=Button(vist,text="Back",font=("arial",18,"bold"),width=10,command=f4)

lblrecord.pack(pady=10)
stdata.pack(pady=10)
btnvback.pack(pady=10)

upst=Toplevel(root)
upst.title("Update Student")
upst.geometry("500x500+400+200")
upst.withdraw()
ulblrno=Label(upst,text="Enter Roll No.",font=("arial",18,"bold"))
uentrno=Entry(upst,bd=5,font=("arial",18,"bold"))
ulblname=Label(upst,text="Enter Name:",font=("arial",18,"bold"))
uentname=Entry(upst,bd=5,font=("arial",18,"bold"))
ulblmarks=Label(upst,text="Enter marks:",font=("arial",18,"bold"))
uentmarks=Entry(upst,bd=5,font=("arial",18,"bold"))
ubtnsave=Button(upst,text="Save",font=("arial",18,"bold"),width=5,command=f9)
ubtnback=Button(upst,text="Back",font=("arial",18,"bold"),width=5,command=f10)

ulblrno.pack(pady=10)
uentrno.pack(pady=10)
ulblname.pack(pady=10)
uentname.pack(pady=10)
ulblmarks.pack(pady=10)
uentmarks.pack(pady=10)
ubtnsave.pack(pady=10)
ubtnback.pack(pady=10)

dest=Toplevel(root)
dest.title("Delete Record")
dest.geometry("500x500+400+200")
dest.withdraw()
dlblrno=Label(dest,text="Enter roll no",font=("arial",18,"bold"))
dentrno=Entry(dest,bd=5,font=("arial",18,"bold"))
dbtndel=Button(dest,text="Delete",font=("arial",18,"bold"),width=5,command=f11)
dbtnback=Button(dest,text="Back",font=("arial",18,"bold"),width=5,command=f12)

dlblrno.pack(pady=10)
dentrno.pack(pady=10)
dbtndel.pack(pady=10)
dbtnback.pack(pady=10)

root.mainloop()