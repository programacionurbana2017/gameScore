class Generador:

	def Tabla(self,tabla):
		contador = 1
		aux = 1
		tabla1 = '''	<tr class="titulo1">
			<td  class="titulo1">POSICION</td>
			<td class="titulo1" >NOMBRE</td>
			<td class="titulo1">PUNTUACION</td>
			<td class="titulo1">TIEMPO JUGADO</td>
			<td class="titulo1">NACIONALIDAD</td>
			<td class="titulo1"></td></tr>'''
		codigo = ""
		for i in tabla:
			if contador == 1:
				codigo = codigo + '''<tr>'''
				codigo = codigo + ''' <td class = "posicionuno">''' + str(contador) + '''.</td>'''
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
					if aux == 1:
						codigo = codigo + '''<td class="posicionuno" >'''+ '''<div class="divuno" id="div1" onclick="clic()" onmouseover="agrandar()"  onmouseout="encojer()">''' + "Aniquilador" +  "</div></td>"
						aux = aux + 1
					else:
						codigo = codigo + '''<td class="posicionuno" >'''+ '''<div class="divuno">''' + j +  "</div></td>"
				else:
					if contador == 2:
						if aux == 2:
							 codigo = codigo + '''<td class="posiciondos" >'''+ '''<div class="divdos" id="div2" onclick="clic2()" onmouseover="agrandar1()"  onmouseout="encojer1()">''' + j +  "</div></td>"
							 aux = aux + 1
						else:
							codigo = codigo + '''<td class="posiciondos" id="titulo1">'''+ '''<div class="divdos">''' + j +  "</div></td>"
					else:
						if contador == 3:
							if aux == 3:
								codigo = codigo + '''<td class="posiciontres" >''' + '''<div class="divtres" id="div3" onclick="clic3()" onmouseover="agrandar2()"  onmouseout="encojer2()">''' + j +  "</div></td>"
								aux = aux + 1
							else:
								codigo = codigo + '''<td class="posiciontres" >''' + '''<div class="divtres" id="div3">''' + j +  "</div></td>"
								
						else:	
							codigo = codigo + '''<td class="comun" onmouseover="agrandarcomun()"  onmouseout="encojercomun()" id="comun1">''' + j +  "</td>" 
			
			if contador == 1:				
				codigo = codigo + ''' <td class = "posicionuno"> ''' + '''<img src="/static/img/n1.png" style="width:80px;height:80px;">''' + '''</td></tr>'''
			else:
				if contador == 2:
				
					codigo = codigo + ''' <td class = "posiciondos"> ''' + '''<img SRC="/static/img/n2.png" style="width:70px;height:70px;">''' + '''</td></tr>'''
				else:
					if contador == 3:
					
						codigo = codigo + ''' <td class = "posiciontres"> ''' + '''<img SRC="/static/img/n3.png" style="width:60px;height:60px;">''' + '''</td></tr>'''
					else:
					
						codigo = codigo + ''' <td class="comun"> ''' + '''<img SRC="/static/img/n4.png" style="width:40px;height:40px;">''' + '''</td></tr>'''
			contador = contador + 1	 
		codigo = codigo + "</tr>"
		codigo = '''  <table class="tabla">''' + tabla1 +codigo +"</table>"
		return codigo
		
		
		



