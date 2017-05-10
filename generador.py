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
		tabla1 = '''	<tr class="titulo">
			
			<td class="titulo1">NOMBRE</td>
			<td class="titulo1">PUNTUACION</td>
			<td class="titulo1">TIEMPO JUGADO</td></tr>'''
		codigo = ""
		for i in tabla:
			codigo = codigo + '''<tr class ="">'''		
			for j in i.split(","):
				 codigo = codigo + '''<td class="">''' + j +  "</td>" 
		codigo = codigo + "</tr>"
		codigo = '''  <table class="tabla">''' + tabla1 +codigo +"</table>"
		return codigo
		
		
		



