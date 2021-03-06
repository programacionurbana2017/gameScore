from generador import Generador
import cherrypy,os


class goodAndDevil(object):
	@cherrypy.expose
	def index(self):
		text = '''
	<!DOCTYPE html>
	<html lang="en">
	<head>

	<script src="static/js/jav.js"></script>
	<link rel="stylesheet" href="static/css/st.css">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>G&D</title>

    <link href="static/css/bootstrap.min.css" rel="stylesheet">
    <link href="static/css/stylish-portfolio.css" rel="stylesheet">
    <link href="static/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,700,300italic,400italic,700italic" rel="stylesheet" type="text/css">
	</head>

	<body>


    
    <script language="javascript">
        function doSearch()
        {
            var tableReg = document.getElementById('tabla');
            var searchText = document.getElementById('searchTerm').value.toLowerCase();
            var cellsOfRow="";
            var found=false;
            var compareWith="";
 
            for (var i = 1; i < tableReg.rows.length; i++)
            {
                cellsOfRow = tableReg.rows[i].getElementsByTagName('td');
                found = false;
                
                for (var j = 0; j < cellsOfRow.length && !found; j++)
                {
                    compareWith = cellsOfRow[j].innerHTML.toLowerCase();
                    if (searchText.length == 0 || (compareWith.indexOf(searchText) > -1))
                    {
                        found = true;
                    }
                }
                if(found)
                {
                    tableReg.rows[i].style.display = '';
                } else {
                    
                    tableReg.rows[i].style.display = 'none';
                }
            }
        }
    </script>



    <a id="menu-toggle" href="#" class="btn btn-dark btn-lg toggle"><i class="fa fa-bars"></i></a>
    <nav id="sidebar-wrapper">
        <ul class="sidebar-nav">
            <a id="menu-close" href="#" class="btn btn-light btn-lg pull-right toggle"><i class="fa fa-times"></i></a>
            <li class="sidebar-brand">
                <a href="#top" onclick=$("#menu-close").click();>Good and Devil</a>
            </li>
            <li>
                <a href="#top" onclick=$("#menu-close").click();>Home</a>
            </li>
        </ul>
    </nav>

    <!-- Header -->
    <header id="top" class="header">
        <div class="text-vertical-center">
            <h1>GOOD &amp; DEVIL</h1>
            <!-- <h3>A Game for known your Real Personality</h3> -->
            <br>
            <a href="#about" class="btn btn-dark btn-lg">Coming soon</a>
        </div>
    </header>

        
	'''
		text1 = """<!-- About -->
        <section id="about" class="about">
            <div >
                <div>
                    <div class="col-lg-12 text-center">
					
                    """    
		text2 = """				
					
                      
                    </div>
						
                </div>
                <!-- /.row -->
            </div>
            <!-- /.container -->
        </section>
		
	 <div id="demo"	class="demo">
	 <li>
		<ul> Estadisticas </>
		<ul> Partidas Jugadas : 10 </ul>
		<ul> Experiencia : 1500 xp </ul>
		<ul> Nivel: Destrozador </ul>
		<ul> Tiempo Jugado : 10 Horas </ul>
		<ul> Logros Conseguidos : 75/200 </ul>
		<ul> Estrellas encontradas : 4/5</ul>
		<ul> <img src="/static/img/rey3.png" style="width:250px;height:250px;"></ul>
	</li>	
		
	<div id="cerrar" class="cerrar" onclick="clic1()"> 	x </div>
	</div>
	
		 <div id="demo1"	class="demo1">	 <li>
		<ul> Estadisticas </>
		<ul> Partidas Jugadas : 8 </ul>
		<ul> Experiencia : 1300 xp </ul>
		<ul> Nivel: Fulminante </ul>
		<ul> Tiempo Jugado : 10 Horas </ul>
		<ul> Logros Conseguidos : 40/200 </ul>
		<ul> Estrellas encontradas : 3/5</ul>
		<ul> <img src="/static/img/rey1.png" style="width:250px;height:250px;"></ul>
	</li> 
	
	<div id="cerrar1" class="cerrar1" onclick="clic4()"> 	x </div>
	</div>
	
	
		 <div id="demo2"	class="demo2">	
			 <li>
		<ul> Estadisticas </>
		<ul> Partidas Jugadas : 7 </ul>
		<ul> Experiencia : 1250 xp </ul>
		<ul> Nivel: Arrasador </ul>
		<ul> Tiempo Jugado : 11 Horas </ul>
		<ul> Logros Conseguidos : 37/200 </ul>
		<ul> Estrellas encontradas : 3/5</ul>
		<ul> <img src="/static/img/rey.png" style="width:250px;height:250px;"></ul>
	</li> 
	<div id="cerrar2" class="cerrar2" onclick="clic5()"> 	x </div>
	</div>

	<div id="img1" class="log1" > <img src="/static/img/espadas.png" style="width:260px;height:260px;"></div>
	<div id="img2" class="log2" > <img src="/static/img/espada1.png" style="width:260px;height:260px;"></div>
	<div id="img3" class="log3" ><img src="/static/img/toma.png" style="width:260px;height:260px;"></div>
	<div id="imgc" class="logc" ><img src="/static/img/cupido.png" style="width:260px;height:260px;"></div>

    <!-- jQuery -->
	<script src="static/js/jquery.js"></script>

	<!-- Bootstrap Core JavaScript -->
	<script src="static/js/bootstrap.min.js"></script>

	<!-- Custom Theme JavaScript -->
	<script>
	// Closes the sidebar menu
	$("#menu-close").click(function(e) {
    e.preventDefault();
    $("#sidebar-wrapper").toggleClass("active");
	});
	// Opens the sidebar menu
	$("#menu-toggle").click(function(e) {
    e.preventDefault();
		$("#sidebar-wrapper").toggleClass("active");
	});
	// Scrolls to the selected menu item on the page
	$(function() {
    $('a[href*=#]:not([href=#],[data-toggle],[data-target],[data-slide])').click(function() {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') || location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html,body').animate({
                    scrollTop: target.offset().top
                }, 1000);
                return false;
            }
        }
    });
	});
	//#to-top button appears after scrolling
	var fixed = false;
	$(document).scroll(function() {
    if ($(this).scrollTop() > 250) {
        if (!fixed) {
            fixed = true;
            // $('#to-top').css({position:'fixed', display:'block'});
            $('#to-top').show("slow", function() {
                $('#to-top').css({
                    position: 'fixed',
                    display: 'block'
                });
            });
        }
    } else {
        if (fixed) {
            fixed = false;
            $('#to-top').hide("slow", function() {
                $('#to-top').css({
                    display: 'none'
                });
            });
        }
    }
	});
	// Disable Google Maps scrolling
	// See http://stackoverflow.com/a/25904582/1607849
	// Disable scroll zooming and bind back the click event
	var onMapMouseleaveHandler = function(event) {
    var that = $(this);
    that.on('click', onMapClickHandler);
    that.off('mouseleave', onMapMouseleaveHandler);
    that.find('iframe').css("pointer-events", "none");
	}
	var onMapClickHandler = function(event) {
        var that = $(this);
        // Disable the click handler until the user leaves the map area
        that.off('click', onMapClickHandler);
        // Enable scrolling zoom
        that.find('iframe').css("pointer-events", "auto");
        // Handle the mouse leave event
        that.on('mouseleave', onMapMouseleaveHandler);
    }
		// Enable map zooming with mouse scroll when the user clicks the map
	$('.map').on('click', onMapClickHandler);
	</script>

	</body>

	</html>

	"""
		migenerador = Generador()
		archivo = open("nombres.txt","r")
		tabla = migenerador.Tabla(archivo)
		return text + text1 + tabla + text2
if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.config.update({'server.socket_host': '127.0.0.1', })
    cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')), })
    cherrypy.quickstart(goodAndDevil(), '/', conf)
