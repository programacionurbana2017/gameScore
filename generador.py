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
		tabla1 = '''	<tr class="titulo1">
			<td class="titulo1">POSICION</td>
			<td class="titulo1" >NOMBRE</td>
			<td class="titulo1">PUNTUACION</td>
			<td class="titulo1">TIEMPO JUGADO</td>
			<td class="titulo1">NACIONALIDAD</td></tr>'''
		codigo = ""
		for i in tabla:
			if contador == 1:
				codigo = codigo + '''<tr>'''
				codigo = codigo + ''' <td class = "posicionuno"> ''' + str(contador) + '''.</td>'''
			else:
				if contador == 2:
					codigo = codigo + '''<tr>'''
					codigo = codigo + ''' <td class = "posiciondos"> ''' + str(contador) + '''.</td>'''
				else:
					if contador == 3:
						codigo = codigo + '''<tr >'''
						codigo = codigo + ''' <td class = "posiciontres"> ''' + str(contador) + '''.</td>'''
					else:
						codigo = codigo + '''<tr class ="comun">'''
						codigo = codigo + ''' <td class="comun"> ''' + str(contador) + '''.</td>'''
			
			for j in i.split(","):
				if contador == 1:
					codigo = codigo + '''<td class="posicionuno">''' + j +  "</td>"
				else:
					if contador == 2:
						codigo = codigo + '''<td class="posiciondos">''' + j +  "</td>"
					else:
						if contador == 3:
							codigo = codigo + '''<td class="posiciontres">''' + j +  "</td>"
						else:	
							codigo = codigo + '''<td class="comun">''' + j +  "</td>" 
			
			contador = contador + 1	 
		codigo = codigo + "</tr>"
		codigo = '''  <table class="tabla">''' + tabla1 +codigo +"</table>"
		return codigo
		
		
		



