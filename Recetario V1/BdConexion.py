import sqlite3

#Recetas
def MostrarRecetas():
	conn = sqlite3.connect('Rec.db')
	c = conn.cursor()
	c.execute("select * from Recetas order by IdReceta DESC")
	x = c.fetchall()
	conn.close()
	return x

def AgregarReceta(Nombre):
	conn = sqlite3.connect('Rec.db')
	c = conn.cursor()
	c.execute("Insert into Recetas (Nombre) values ('"+Nombre+"')")
	conn.commit()
	conn.close()

def ModificarReceta(IdReceta,Nombre):
	conn = sqlite3.connect('Rec.db')
	c = conn.cursor()
	c.execute("Update Recetas SET Nombre ='"+Nombre+"' where IdReceta = "+str(IdReceta))
	conn.commit()
	conn.close()

def EliminarReceta(IdReceta):
	conn = sqlite3.connect('Rec.db')
	c = conn.cursor()
	c.execute("Delete from Recetas where IdReceta = "+str(IdReceta))
	conn.commit()
	conn.close()
	
#Ingredientes	
def MostrarIngredientesXReceta(IdReceta):
	conn = sqlite3.connect('Rec.db')
	c = conn.cursor()
	c.execute("select * from Ingredientes where IdReceta =" + str(IdReceta)+ " order by IdIngrediente DESC")
	x = c.fetchall()
	conn.close()
	return x

def AgregarIngredientesXReceta(IdReceta,NombreReceta):
	conn = sqlite3.connect('Rec.db')
	c = conn.cursor()
	c.execute("Insert into Ingredientes (IdReceta,Nombre) values ("+str(IdReceta)+",'"+NombreReceta+"')")
	conn.commit()
	conn.close()
	
def ModificarIngrediente(IdReceta,IdIngrediente,Nombre):
	conn = sqlite3.connect('Rec.db')
	c = conn.cursor()
	c.execute("Update Ingredientes SET Nombre ='"+Nombre+"' where IdReceta = "+str(IdReceta)+" and IdIngrediente ="+str(IdIngrediente))
	conn.commit()
	conn.close()
	
def EliminarIngredientes(IdReceta):
	conn = sqlite3.connect('Rec.db')
	c = conn.cursor()
	c.execute("Delete from Ingredientes where IdReceta ="+str(IdReceta))
	conn.commit()
	conn.close()

def EliminarIngrediente(IdReceta,IdIngrediente):
	conn = sqlite3.connect('Rec.db')
	c = conn.cursor()
	c.execute("Delete from Ingredientes where IdReceta ="+str(IdReceta)+ " and IdIngrediente ="+str(IdIngrediente))
	conn.commit()
	conn.close()
#Procedimientos
def MostrarProcedimientosXReceta(IdReceta):
	conn = sqlite3.connect('Rec.db')
	c = conn.cursor()
	c.execute("select * from Procedimientos where IdReceta =" + str(IdReceta)+ " order by IdProcedimiento DESC")
	x = c.fetchall()
	conn.close()
	return x

def AgregarProcedimientosXReceta(IdReceta,Nombre):
	conn = sqlite3.connect('Rec.db')
	c = conn.cursor()
	c.execute("Insert into Procedimientos (IdReceta,Descripcion) values ("+str(IdReceta)+",'"+Nombre+"')")
	conn.commit()
	conn.close()

def ModificarProcedimiento(IdReceta,IdProcedimiento,Descripcion):
	conn = sqlite3.connect('Rec.db')
	c = conn.cursor()
	c.execute("Update Procedimientos SET Descripcion ='"+Descripcion+"' where IdReceta = "+str(IdReceta)+" and IdProcedimiento ="+str(IdProcedimiento))
	conn.commit()
	conn.close()

def EliminarProcedimientos(IdReceta):
	conn = sqlite3.connect('Rec.db')
	c = conn.cursor()
	c.execute("Delete from Procedimientos where IdReceta ="+str(IdReceta))
	conn.commit()
	conn.close()

def EliminarProcedimiento(IdReceta,IdProcedimiento):
	conn = sqlite3.connect('Rec.db')
	c = conn.cursor()
	c.execute("Delete from Procedimientos where IdReceta ="+str(IdReceta)+" and IdProcedimiento ="+str(IdProcedimiento))
	conn.commit()
	conn.close()
