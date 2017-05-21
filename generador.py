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
		contador = 1
		tabla1 = '''	<tr class="titulo">
			<td class="titulo1">POSICION</td>
			<td class="titulo1">NOMBRE</td>
			<td class="titulo1">PUNTUACION</td>
			<td class="titulo1">TIEMPO JUGADO</td>
			<td class="titulo1">NACIONALIDAD</td></tr>'''
		codigo = ""
		for i in tabla:
			codigo = codigo + '''<tr class ="">'''
			codigo = codigo + ''' <td> ''' + str(contador) + '''</td>'''
			
			for j in i.split(","):
				 codigo = codigo + '''<td class="">''' + j +  "</td>" 
			
			contador = contador + 1	 
		codigo = codigo + "</tr>"
		codigo = '''  <table class="tabla">''' + tabla1 +codigo +"</table>"
		return codigo
		
		
		



