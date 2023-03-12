import tkinter as tk
from tkinter import *

def mainwindow() :
  root = tk.Tk()
  root.title("Week 6 : Menu Widget By Patiphan Arphorn")
  root.geometry('800x800')
  root.option_add('*font','garamond 14')
  root.config(bg='pink')
  return(root)
def productmenu():
  frame1 = tk.Frame(root,bg='#FFE7CC')
  frame1.place(x=0,y=0,width=800,height=800)
  frame1.columnconfigure((0,1),weight=1)
  frame1.rowconfigure((0,1,2),weight=1)
  pos = 0
  for i,menu in enumerate(menu1) :
      tk.Label(frame1,bg="#FFE7CC",text=menu,fg="blue").grid(row=pos,column=0,pady=10)
      tk.Label(frame1,bg="#FFE7CC",image=cakes[i],fg="blue").grid(row=pos+1,column=0,pady=10)
      tk.Label(frame1,bg="#FFE7CC",text="Price :"+str(price1[i]),fg="blue").grid(row=pos+2,column=0,pady=10)
      tk.Spinbox(frame1,from_=0,to=100,width=15,justify="center",textvariable=amt1[i]).grid(row=pos+3,column=0,pady=10)
      pos += 4
  pos = 0
  for i,menu in enumerate(menu2) :
      tk.Label(frame1,bg="#FFE7CC",text=menu,fg="blue").grid(row=pos,column=1,pady=10)
      tk.Label(frame1,bg="#FFE7CC",image=drinks[i],fg="blue").grid(row=pos+1,column=1,pady=10)
      tk.Label(frame1,bg="#FFE7CC",text="Price :"+str(price2[i]),fg="blue").grid(row=pos+2,column=1,pady=10)
      tk.Spinbox(frame1,from_=0,to=100,width=15,justify="center",textvariable=amt2[i]).grid(row=pos+3,column=1,pady=10)
      pos += 4
           
def checkout() :
  global total1,total2
  total1,total2 = 0,0
  frame2 = tk.Frame(root,bg='#F8CBA6')
  frame2.place(x=0,y=0,width=800,height=800)
  frame2.rowconfigure((0,1,2,3,4,5,6),weight=1)
  frame2.columnconfigure((0,1,2,3),weight=1)
  menulist = ["Menu List","Amount","Price","Total(Bahts)"]
  productlist = ['Strawberry Cake',"Cheese Cake","DIY Cake",'Strawberry Mixed','Orange Mixed',"Coffee"]
  #type your code here
  for i ,title in enumerate(menulist) :
     tk.Label(frame2,bg="#F8CBA6",text=title).grid(row=0,column=i)
     
  for i ,title in enumerate(productlist) :
     
     tk.Label(frame2,bg="#F8CBA6",text=productlist[i],fg="blue").grid(row=i+1,column=0,sticky="e")
  pos = 1   
  for i,menu in enumerate(menu1) :
     tk.Label(frame2,bg="#F8CBA6",text=str(amt1[i].get())).grid(row=pos,column=1)
     tk.Label(frame2,bg="#F8CBA6",text=str(price1[i])).grid(row=pos,column=2)
     totalcake = amt1[i].get() * price1[i]
     total1 += totalcake
     tk.Label(frame2,bg="#F8CBA6",text=str(totalcake)).grid(row=pos,column=3)
     pos += 1
  for i,menu in enumerate(menu2) :
     tk.Label(frame2,bg="#F8CBA6",text=str(amt2[i].get())).grid(row=pos,column=1)
     tk.Label(frame2,bg="#F8CBA6",text=str(price2[i])).grid(row=pos,column=2)
     totaldrink = amt2[i].get() * price2[i]
     total2 += totaldrink
     tk.Label(frame2,bg="#F8CBA6",text=str(totaldrink)).grid(row=pos,column=3)
     pos += 1
       
  
  tk.Label(frame2,bg='#F8CBA6',fg='blue',font=("Garamond",22,'bold'),textvariable=output).grid(row=pos+2,pady=10,columnspan=4)
  total = total1 + total2
  print("Total = ",total)
  output.set("Total price = %0.2f"%total)
  def click() :
      if spy.get() :
         total =(total1 + total2) - (total1 + total2) * 0.1
         output.set("Total price = %0.2f"%total)
         
  Checkbutton(frame2,text="HAVE A MEMBER : (Click) YES (Discount 10%)or (Blank) NOT A MEMBER",bg="#F7C8E0",command=click,variable=spy).grid(row=7,columnspan=4,sticky="news",pady=20,ipady=10) 
  
    
def createmenu(root) :
  menubar = tk.Menu(root)
  #use method add_command to add menu and take user action from click
  menubar.add_command(label="productmenu",command=productmenu)
  menubar.add_command(label="checkout",command=checkout)
  menubar.add_command(label="Exit Program",command=root.quit)
  root.configure(bg="pink",menu=menubar)
root = mainwindow()
img1 = tk.PhotoImage(file="image/myshop.png")
img2 = tk.PhotoImage(file="image/drink1.png")
img3 = tk.PhotoImage(file="image/drink2.png")
img4 = tk.PhotoImage(file="image/coffee3.png")
img5 = tk.PhotoImage(file="image/cake1.png")
img6 = tk.PhotoImage(file="image/cake2.png")
img7 = tk.PhotoImage(file="image/cake3.png")
drinks = [img2,img3,img4]
cakes = [img5,img6,img7]
menu1 = ['Strawberry Cake',"Cheese Cake","DIY Cake"]
menu2 = ['Strawberry Mixed','Orange Mixed',"Coffee"]
price1 = [85,95,100]
price2 = [120,140,80]
amt1 = [tk.IntVar() for x in menu1] #spy of cake
amt2 = [tk.IntVar() for x in menu2] #spy of drink
total = 0.0
total1 = 0.0            #to correct total of cake price
total2 = 0.0            #to correct total of drink price
output = tk.StringVar() #spy of output label
createmenu(root)        #call function to create menubar
spy = tk.IntVar()
root.mainloop()