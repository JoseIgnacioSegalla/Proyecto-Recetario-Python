from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import BdConexion as bd


def AgregarModificar():
	global IdReceta
	global IdIngrediente
	global IdProcedimiento
	
	if Btn_AgregarModificar['text'] == "Modificar":
		
		Btn_Eliminar['state'] = "normal"
		Btn_AgregarModificar['text'] = "Agregar"
		
		if Txt_Receta.get():
			
			bd.ModificarReceta(IdReceta,Txt_Receta.get().strip())
			
			Txt_Procedimiento['state'] = "normal"
			Txt_Procedimiento['bg'] = "white"
			Txt_Procedimiento['fg'] = "black"
			Txt_Ingrediente['state'] = "normal"
			Lista_Receta['state'] = "normal"
			Lista_Ingrediente['state'] = "normal"
			Lista_Procedimiento['state'] = "normal"
			
			Lista_Receta.delete(0,END)
			for item in bd.MostrarRecetas():
				Lista_Receta.insert(0,item)
			
			Txt_Receta.delete(0,END)
			
		elif Txt_Ingrediente.get():
			
			bd.ModificarIngrediente(IdReceta,IdIngrediente,Txt_Ingrediente.get().strip())
		
			Txt_Procedimiento['state'] = "normal"
			Txt_Procedimiento['bg'] = "white"
			Txt_Procedimiento['fg'] = "black"
			Txt_Receta['state'] = "normal"
			Lista_Receta['state'] = "normal"
			Lista_Ingrediente['state'] = "normal"
			Lista_Procedimiento['state'] = "normal"
			
			Lista_Ingrediente.delete(0,END)
			for item in bd.MostrarIngredientesXReceta(IdReceta):
				Lista_Ingrediente.insert(0,item)
			
			Txt_Ingrediente.delete(0,END)
			
		elif Txt_Procedimiento.get(1.0,3.0):
			
			bd.ModificarProcedimiento(IdReceta,IdProcedimiento,Txt_Procedimiento.get(1.0,3.0).strip())
			
			Txt_Ingrediente['state'] = "normal"
			Txt_Receta['state'] = "normal"
			Lista_Receta['state'] = "normal"
			Lista_Ingrediente['state'] = "normal"
			Lista_Procedimiento['state'] = "normal"
			
			Lista_Procedimiento.delete(0,END)
			for item in bd.MostrarProcedimientosXReceta(IdReceta):
				Lista_Procedimiento.insert(0,item)
			
			Txt_Procedimiento.delete(1.0,END)
			
	else:
		if Txt_Receta.get().strip():
			
			receta = Txt_Receta.get().strip()
			bd.AgregarReceta(receta)
			Lista_Receta.delete(0,END)
			for item in bd.MostrarRecetas():
				Lista_Receta.insert(0,item)
			
			Txt_Receta.delete(0,END)
			
		if Txt_Ingrediente.get().strip() and Lista_Receta.curselection():
			
			ingrediente = Txt_Ingrediente.get().strip()
			bd.AgregarIngredientesXReceta(IdReceta,ingrediente)
			Lista_Ingrediente.delete(0,END)
			for item in bd.MostrarIngredientesXReceta(IdReceta):
				Lista_Ingrediente.insert(0,item)
			
			Txt_Ingrediente.delete(0,END)
				
			
		if Txt_Procedimiento.get(1.0,2.0).strip() and Lista_Receta.curselection():
			
			procedimiento = Txt_Procedimiento.get(1.0,3.0).strip()
			bd.AgregarProcedimientosXReceta(IdReceta,procedimiento)
			Lista_Procedimiento.delete(0,END)
			
			for item in bd.MostrarProcedimientosXReceta(IdReceta):
				Lista_Procedimiento.insert(0,item)
			
			Txt_Procedimiento.delete(1.0,END)
 
def Eliminar():

	if Lista_Receta.curselection():
		for i in Lista_Receta.curselection():
			
			bd.EliminarProcedimientos(Lista_Receta.get(i)[0])
			bd.EliminarIngredientes(Lista_Receta.get(i)[0])
			bd.EliminarReceta(Lista_Receta.get(i)[0])
		
		Lista_Receta.delete(0,END)
		Lista_Ingrediente.delete(0,END)
		Lista_Procedimiento.delete(0,END)
		for i in bd.MostrarRecetas():
			Lista_Receta.insert(0,i)
			
				
			
	elif Lista_Ingrediente.curselection():
		IdReceta = 0
		for i in Lista_Ingrediente.curselection():
			print(Lista_Ingrediente.get(i)[0],Lista_Ingrediente.get(i)[1])
			IdReceta = Lista_Ingrediente.get(i)[0]
			bd.EliminarIngrediente(Lista_Ingrediente.get(i)[0],Lista_Ingrediente.get(i)[1])
			
		
		Lista_Ingrediente.delete(0,END)
		for x in bd.MostrarIngredientesXReceta(IdReceta):
				Lista_Ingrediente.insert(0,x)	
			
		
			
	elif Lista_Procedimiento.curselection():
		IdReceta = 0
		for i in Lista_Procedimiento.curselection():
			IdReceta = Lista_Procedimiento.get(i)[0]
			bd.EliminarProcedimiento(Lista_Procedimiento.get(i)[0],Lista_Procedimiento.get(i)[1])
			
		
		Lista_Procedimiento.delete(0,END)
		for x in bd.MostrarProcedimientosXReceta(IdReceta):
				Lista_Procedimiento.insert(0,x)	

def Mostrar_receta(event):
	global IdReceta
	IdReceta = 0
	
	if Lista_Receta.curselection():
		for i in Lista_Receta.curselection():
			IdReceta = Lista_Receta.get(i)[0]
	
		if Lista_Ingrediente.size():
			
			Lista_Ingrediente.delete(0,END)
			for i in bd.MostrarIngredientesXReceta(IdReceta):
				
				Lista_Ingrediente.insert(0,i)
		else:
			for i in bd.MostrarIngredientesXReceta(IdReceta):
				Lista_Ingrediente.insert(0,i)
		if Lista_Procedimiento.size():
		
			Lista_Procedimiento.delete(0,END)
			for i in bd.MostrarProcedimientosXReceta(IdReceta):
				Lista_Procedimiento.insert(0,i)
		else:
			for i in bd.MostrarProcedimientosXReceta(IdReceta):
				Lista_Procedimiento.insert(0,i)

def Anterior_receta(event):
	print("entro")
	
	
def Modificar_receta(event):
	global IdReceta
	IdReceta = 0
	if Lista_Receta.curselection():
		
		Txt_Ingrediente.delete(0,END)
		Txt_Procedimiento.delete(1.0,3.0)
			
		Btn_AgregarModificar['text'] = "Modificar"
		Txt_Procedimiento['state'] = "disabled"
		Txt_Procedimiento['bg'] = "#dddddd"
		Txt_Procedimiento['fg'] = "#dddddd"
		Txt_Ingrediente['state'] = "disabled"
		Lista_Receta['state'] = "disabled"
		Lista_Ingrediente['state'] = "disabled"
		Lista_Procedimiento['state'] = "disabled"
		Btn_Eliminar['state'] = "disabled"
		Txt_Receta.focus_set()
		
		for i in Lista_Receta.curselection():
			Txt_Receta.insert(0,Lista_Receta.get(i)[1])
			IdReceta = Lista_Receta.get(i)[0]
			
		
		
		for i in bd.MostrarProcedimientosXReceta(IdReceta):
			Lista_Procedimiento.insert(0,i)
	
	
	
def Modificar_ingrediente(event):
	
	global IdReceta
	global IdIngrediente
	IdReceta = 0
	IdIngrediente = 0
	Txt_Receta.delete(0,END)
	Txt_Procedimiento.delete(1.0,3.0)
	
	Btn_AgregarModificar['text'] = "Modificar"
	Txt_Procedimiento['state'] = "disabled"
	Txt_Procedimiento['bg'] = "#dddddd"
	Txt_Procedimiento['fg'] = "#dddddd"
	Txt_Receta['state'] = "disabled"
	Lista_Receta['state'] = "disabled"
	Lista_Ingrediente['state'] = "disabled"
	Lista_Procedimiento['state'] = "disabled"
	Btn_Eliminar['state'] = "disabled"
	Txt_Ingrediente.focus_set()
	
	for i in Lista_Ingrediente.curselection():
		Txt_Ingrediente.insert(0,Lista_Ingrediente.get(i)[2])
		IdIngrediente = Lista_Ingrediente.get(i)[1]
		IdReceta = Lista_Ingrediente.get(i)[0]
		
	
	
	
def Modificar_procedimiento(event):
	
	global IdReceta
	global IdProcedimiento
	IdReceta = 0
	IdProcedimiento = 0
	Txt_Receta.delete(0,END)
	Txt_Ingrediente.delete(0,END)
	
	Btn_AgregarModificar['text'] = "Modificar"
	Txt_Ingrediente['state'] = "disabled"
	Txt_Receta['state'] = "disabled"
	Lista_Receta['state'] = "disabled"
	Lista_Ingrediente['state'] = "disabled"
	Lista_Procedimiento['state'] = "disabled"
	Btn_Eliminar['state'] = "disabled"
	Txt_Procedimiento.focus_set()
	
	for i in Lista_Procedimiento.curselection():
		Txt_Procedimiento.insert(1.0,Lista_Procedimiento.get(i)[2])
		IdProcedimiento = Lista_Procedimiento.get(i)[1]
		IdReceta = Lista_Procedimiento.get(i)[0]
		

"""
---Formato receta/ingrediente cantidad medida(a evaluar)
---Si modificamos la cantidad en la receta, modificar la cantidad en los ingredientes de esa receta(a evaluar)"""


root = Tk(className='Recetario')
root.title("Recetario")

Tit_Receta = Label(root,text="Receta:")
Tit_Receta.grid(column=0,row=0,sticky="W")
Txt_Receta = Entry(root)
Txt_Receta.grid(column=0,row=1,sticky="W")
Tit_Ingrediente = Label(root,text="Ingrediente:")
Tit_Ingrediente.grid(column=1,row=0,sticky="W")
Txt_Ingrediente = Entry(root)
Txt_Ingrediente.grid(column=1,row=1,sticky="W")


Lista_Receta = Listbox(root,width=30)
Lista_Receta.grid(column=0,row=4)

for item in bd.MostrarRecetas():
	Lista_Receta.insert(0,item)
	

Lista_Ingrediente = Listbox(root,width=30)
Lista_Ingrediente.grid(column=1,row=4)
Tit_Procedimiento = Label(root,text="Procedimiento:")
Tit_Procedimiento.grid(column=0,row=5,sticky="W")
Txt_Procedimiento = Text(root,width=60,height=3)
Txt_Procedimiento.grid(column=0,row=6,columnspan=4)
Lista_Procedimiento = Listbox(root,width=60)
Lista_Procedimiento.grid(column=0,row=7,columnspan=4)
Btn_AgregarModificar =Button(root,text="Agregar",width=57,command=AgregarModificar)
Btn_AgregarModificar.grid(column=0,row=8,columnspan=2)
Btn_Eliminar = Button(root,text="Eliminar",width=57,command=Eliminar)
Btn_Eliminar.grid(column=0,row=9,columnspan=2)

# teclado y mouse
Lista_Receta.bind('<Double-1>', Modificar_receta)
Lista_Receta.bind('<ButtonRelease-1>', Mostrar_receta)
Lista_Receta.bind('<Return>',Anterior_receta)
Lista_Ingrediente.bind('<Double-1>', Modificar_ingrediente) 	
Lista_Procedimiento.bind('<Double-1>', Modificar_procedimiento)


root.mainloop()
