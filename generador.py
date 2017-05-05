class Generador:
	def titulo(self,titulo,parrafo):
		titulo = "<h1>" + titulo + "</h1>"
		parrafo = "<p>" + parrafo + "</p>"
		return titulo+parrafo
			
	def Lista(self,lista):
		codigo = ""
		for i in lista:
			codigo = codigo + "<li>" +i+ "</li>"		
		codigo = "<ol>" + codigo + "</ol>"
		return  codigo
	
	def Tabla(self,tabla):
		codigo = ""
		for i in tabla:
			codigo = codigo + "<tr>"		
			for j in i.split(","):
				 codigo = codigo + "<td>" + j +  "</td>" 
		codigo = codigo + "</tr>"
		codigo = "<table>"+codigo +"</table>"
		return codigo


