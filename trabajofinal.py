from tkinter import *
from tkinter import ttk,messagebox,simpledialog
from msilib.schema import ComboBox
from optparse import Values
from email import message
from turtle import title

ven=Tk()

g=0
u=0
x=0



ven.config(width=800,height=375)
ven.title("Servicio de grúa")
fondo = PhotoImage(file = "grua.png")
lblfondo=Label(ven,image=fondo)
lblfondo.place(x=-2,y=0)

def agregar():
    #try:
        global g
        pa=en1.get()
        mod=cbomodelo.get()
        co=cbocolor.get()
        mot=cbomotivo.get()
        ori=en2.get()
        des=en3.get()

        if cbomarca.current()==0 or cbomodelo.current()==0 or cbocolor.current()==0 or cbomotivo.current()==0 or ori=="" or des=="" or cbomarca.get()==("Seleccione marca...") or cbomodelo.get()==("Seleccione modelo...") or cbocolor.get()==("Seleccione color...") or cbomotivo.get()==("Seleccione motivo...") or cbomodelo.get()==(""):
            messagebox.showerror(title="Error",message="Hay campos incompletos. Debe llenar todos los campos.")

        elif len(pa)<6 or len(pa)>7:
            messagebox.showerror(title="Error", message="La patente debe tener entre 6 y 7 dígitos.")
        else:
            lista.insert(g,pa+" - "+ma+" - "+mod+" - "+co+" - "+mot+" - "+ori+" - "+des)
            
            g=g+1
            en1.delete(0,END)
            en2.delete(0,END)
            en3.delete(0,END)
            cbomarca.set("Seleccione marca...")
            cbomodelo["values"]=[""]
            cbomodelo.set("Seleccione modelo...")      
            cbocolor.set("Seleccione color...")
            cbomotivo.set("Seleccione motivo...")

    #except:
        #messagebox.showerror(title="Error",message="Hay campos incompletos. Debe llenar todos los campos.")


def buscaryelim(y,ls):
    global g
    x=0
    z=0
    while x!=ls:
        if lista.get(x)[0:6]==y or lista.get(x)[0:7]==y:
            lista.delete(x)
            
            
            g=g-1
            z=1
        x=x+1  
    if z==1:
            messagebox.showinfo(title="Eliminar registro",message="Todo registro con esa patente se eliminó exitosamente.")
    if z==0:
            messagebox.showerror(title="Error",message="No hay ningún registro con esa patente.")

def terminar():
    global g,ls
    if lista.curselection()!=():
        pos=lista.curselection()
        lista.delete(pos)
        g=g-1
    
    else:
        ls=lista.size()
                
        y=simpledialog.askstring(title="Eliminar",prompt="También puede eliminar seleccionando de la lista y pulsando el botón 'Eliminar servicio'. Si desea eliminar según el número de patente, ingréselo a continuación:",parent=ven)
        if len(y)<6 or len(y)>7:
            messagebox.showerror(title="Error", message="La patente debe tener entre 6 y 7 dígitos.")
        else:
            buscaryelim(y,ls)
            
        
        
       

def selmarca(event):
    global ma
    ma=cbomarca.get()
    
    
    lisfiat=["Seleccione modelo...","Palio","Argo","Mobi","Cronos","Uno", "Strada", "Fiorino"]
    lisren=["Seleccione modelo...", "Duster", "Logan","Captur","Koleos","Stepway","Kangoo","Sandero"]
    lischev=["Seleccione modelo...", "Onix", "Camaro","Cruze","Equinox","Tracker","Joy", "Spin"]
    lisfor=["Seleccione modelo...", "Falcon","Kuga","Mustang","Ecosport","Territory","Mondeo","Nueva F-150"]
    lispeu=["Seleccione modelo...","308","208","Partner","408","5008","SUV 2008","Expert"]
    lisniss=["Seleccione modelo...","X TRAIL","Versa", "Kicks","Murano","Sentra","Leaf","Frontier"]
    liscit=["Seleccione modelo...","C3","C4","C5 Aircross","C4 Cactus","Berlingo","C4 Lounge","Jumpy"]


    if ma=="Fiat":
        cbomodelo["values"]=lisfiat
    if ma=="Renault":
        cbomodelo["values"]=lisren
    if ma=="Chevrolet":
        cbomodelo["values"]=lischev
    if ma=="Ford":
        cbomodelo["values"]=lisfor
    if ma=="Peugeot":
        cbomodelo["values"]=lispeu
    if ma=="Nissan":
        cbomodelo["values"]=lisniss
    if ma=="Citroën":
        cbomodelo["values"]=liscit
    if ma==None or ma=="":
        cbomodelo["values"]=None
    cbomodelo.set("Seleccione modelo...")

lbl1=Label(ven,text="Control de Servicio de grúa")
lbl1.config(width=20,height=1)
lbl1.place(x=415, y=10)
lbl1.config(fg="white", bg="blue",font=("Arial",24)) 

en1=Entry(ven)
en1.config(width=15)
en1.place(x=700,y= 60)

cbomarca=ttk.Combobox(ven, values= [ "Seleccione marca...","Fiat", "Renault", "Chevrolet", "Ford","Peugeot","Nissan","Citroën"])
cbomarca.set("Seleccione marca...")
cbomarca.place(x=650,y=90)

cbomarca.bind("<<ComboboxSelected>>", selmarca)




cbomodelo=ttk.Combobox(ven)

cbomodelo.set("Seleccione modelo...")
cbomodelo.place(x=650,y=120)

cbocolor=ttk.Combobox(ven, values= [ "Seleccione color...","Blanco", "Gris", "Negro", "Rojo","Azul","Verde","Bordo"])
cbocolor.set("Seleccione color...")
cbocolor.place(x=650,y=150)





cbomotivo=ttk.Combobox(ven, values= [ "Seleccione motivo...","Desperfecto mecánico","Desperfecto neumáticos","Desperfecto eléctrico","Desperfecto batería","Desperfecto choque"])
cbomotivo.set("Seleccione motivo...")
cbomotivo.place(x=650,y=180)


en2=Entry(ven)
en2.config(width=30)
en2.place(x=610,y= 210)


en3=Entry(ven)
en3.config(width=30)
en3.place(x=610,y= 240)


lbl2=Label(ven,text="Patente:")
lbl2.place(x=635, y=60)

lbl3=Label(ven,text="Marca:")
lbl3.place(x=600, y=90)

lbl4=Label(ven,text="Modelo:")
lbl4.place(x=592, y=120)

lbl5=Label(ven,text="Color:")
lbl5.place(x=604, y=150)

lbl6=Label(ven,text="Motivo:")
lbl6.place(x=596, y=180)

lbl7=Label(ven,text="Origen:")
lbl7.place(x=554, y=210)

lbl8=Label(ven,text="Destino:")
lbl8.place(x=550, y=240)

lista=Listbox(ven, width=95, height=6)
lista.place(x=220,y=267)

btn1=Button(ven,text="Agregar servicio",command=agregar)
btn1.config(fg="black", bg="#84BE68",font=("Arial",13))
btn1.place(x=220,y=230)

btn2=Button(ven,text="Terminar servicio",command=terminar)
btn2.config(fg="black", bg="#A268BE",font=("Arial",13))
btn2.place(x=360,y=230)




ven.mainloop()