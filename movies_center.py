########################################## 
# Project       : Movie Website
# Date Started  : 11/18/2016
# Date Completed: 11/25/2016
# Submitted by  : Carlos Barillas
########################################## 

####################### Movies Center ##############################
# Description:  This file allow us create multiple instance of movies
#               for create the web page trailer you must have the media 
#               class (media.py) and the html generator file 
#               (fresh_tomatoes_with_tooltip) in the same folder, and
#               import these modules.
####################################################################

import media
import fresh_tomatoes_with_tooltip

# Deadpool movie
deadpool = media.Movie(
                    "Deadpool",
                    "A former Special Forces operative turned mercenary \
                     is subjected to a rogue experiment that leaves him \
                     with accelerated healing powers, adopting the alter \
                     ego Deadpool.",
                    "http://cdn.foxplay.com/sites/common/objects/img/movies/resized/320x480/218170_poster_600_888_20161028050253.jpg",  # noqa
                    "https://www.youtube.com/watch?v=ZIM1HydF9UA")

# Wolverine movie
wolverine = media.Movie(
                    "Wolverine",
                    "Wolverine es un mutante que busca venganza \
                     contra Sabertooth, despu&eacute;s de que \
                     &eacute;ste asesinara a su novia. En su \
                     b&uacute;squeda termina en una unidad \
                     secreta llamada X-Men, muy confundido con su pasado.",
                    "http://cdn.foxplay.com/sites/common/objects/img/movies/resized/320x480/150800_poster_600_888_20130521175402.jpg",  # noqa
                    "https://www.youtube.com/watch?v=g7kdUy5_WlI")

# X-men movie
xmen = media.Movie(
                    "X-MEN",
                    "Los X-Men deber&aacute;n luchar a trav&eacute;s \
                     de dos per&iacute;odos de tiempo, y cambiar un \
                     importante evento hist&oacute;rico, en una batalla \
                     &eacute;pica para salvar el futuro de \
                     humanos y mutantes.",
                    "http://cdn.foxplay.com/sites/common/objects/img/movies/resized/320x480/198209_poster_600_888_20150227100059.jpg",  # noqa
                    "https://www.youtube.com/watch?v=pK2zYHWDZKo")

# The revenant movie
revenant = media.Movie(
                    "The Revenant",
                    "Un hombre de la frontera en una expedici&oacute;n \
                     para buscar pieles en el 1820 lucha por sobrevivir \
                     luego de ser mutilado por un oso y dado por muerto \
                     por miembros de su propio equipo de cacer&iacute;a.",
                    "http://cdn.foxplay.com/sites/common/objects/img/movies/resized/320x480/218166_poster_600_888_20160930050629.jpg",  # noqa
                    "https://www.youtube.com/watch?v=QRfj1VCg16Y")

# Bridge of spies movie
bridge_of_spies = media.Movie(
                    "Bridge of Spies",
                    "La historia de James Donovan, un abogado de Brooklyn \
                     que termina en medio de la Guerra Fria cuando la CIA \
                     lo envia con la tarea casi imposible de negociar la \
                     liberacion de un piloto estadunidense capturado.",
                    "http://cdn.foxplay.com/sites/common/objects/img/movies/resized/320x480/218156_poster_600_888_20160730050431.jpg",  # noqa
                    "https://www.youtube.com/watch?v=7JnC2LIJdR0")

# Fantastic four movie
fantastic_four = media.Movie(
                    "Fantastic Four",
                    "Cuatro j&oacute;venes viajan a un peligroso \
                     universo alterno que cambia su aspecto f&iacute;sico \
                     y les otorga poderes. Ahora, los cuatro \
                     fant&aacute;sticos deber&aacute;n aprovechar \
                     sus nuevas habilidades para salvar la Tierra de \
                     alguien que alguna vez fue su amigo.",
                    "http://cdn.foxplay.com/sites/common/objects/img/movies/resized/320x480/228361_poster_600_888_20160628050038.jpg",  # noqa
                    "https://www.youtube.com/watch?v=_rRoD28-WgU")

# World War Z Movie
wwz = media.Movie(
                    "World War Z",
                    "Gerry Lane, empleado de las Naciones Unidas, \
                     deber&aacute; recorrer el mundo en una \
                     carrera contra el tiempo. Su misi&oacute;n \
                     ser&aacute; detener una pandemia zombi que amenaza \
                     con destruir a la humanidad.",
                    "http://base.laptv.com/public/mcplay/imagenes/pub/176876_poster_600_888_20140423000029.jpg",  # noqa
                    "https://www.youtube.com/watch?v=HcwTxRuq-uk")

# Mission Impossible Movie
mission_impossible = media.Movie(
                    "Mission: Impossible - Rogue Nation",
                    "Ethan y equipo asumen su misi&oacute;n m&aacute;s \
                     imposible a&uacute;n, la erradicaci&oacute;n de la \
                     Syndicate - una organizaci&oacute;n p&iacute;caro \
                     Internacional como altamente cualificados \
                     como son, comprometido con la destrucci&oacute;n \
                     del IMF.",
                    "http://cdn.foxplay.com/sites/common/objects/img/movies/resized/320x480/218185_poster_600_888_20160430050212.jpg",  # noqa
                    "https://www.youtube.com/watch?v=gOW_azQbOjw")
# Shrek movie
shrek = media.Movie("Shrek",
                    "La princesa Fiona, recluida en la torre m&aacute;s \
                     alta de un lejano castillo, espera que su perfecto \
                     pr&iacute;ncipe azul la rescate. En cambio, su salvador \
                     resulta ser Shrek, un ogro de pantano con muy poca \
                     paciencia.",
                    "http://cdn.foxplay.com/sites/common/objects/img/movies/resized/320x480/137247_poster_600_888_20131120061919.jpg",  # noqa  
                    "https://www.youtube.com/watch?v=1_INNPR84CI")
# Casper movie
casper = media.Movie(
                    "Casper",
                    "El Dr. James Harvey y su hija Kat llegan a una \
                     mansi&oacute;n de la que deben desalojar a todos \
                     los fantasmas. Pero cuando Kat conoce a Casper, \
                     el simp&aacute;tico espectro de un joven, y a sus \
                     tres alocados t&iacute;os, la convivencia se torna \
                     muy intensa.",
                    "http://cdn.foxplay.com/sites/common/objects/img/movies/resized/320x480/138427_poster_600_888_20130615081440.jpg",  # noqa
                    "https://www.youtube.com/watch?v=BBEB9OSfeCA")
# Hitman movie
hitman = media.Movie(
                    "HITMAN",
                    "Producto de un experimento genetico que le \
                     dio inteligencia superior y habilidades \
                     sobrehumanas, el agente 47 se convirtio en \
                     una perfecta maquina de matar. En equipo \
                     con una joven misteriosa, descubrira los \
                     secretos de su origen.",
                    "http://cdn.foxplay.com/sites/common/objects/img/movies/resized/320x480/218155_poster_600_888_20160628051033.jpg",  # noqa
                    "https://www.youtube.com/watch?v=alQlJDRnQkE")
# Casper movie
casper = media.Movie(
                    "Forgetting Sarah Marshall",
                    "Un m&uacute;sico que lleva años con su novia, \
                     una estrella de televisi&oacute;n, se derrumba \
                     cuando la chica lo deja. Decidido a recuperar \
                     su vida, el joven emprende un \
                     viaje sin imaginar a qui&eacute;n se va a \
                     encontrar.",
                    "http://cdn.foxplay.com/sites/common/objects/img/movies/resized/320x480/154612_poster_600_888_20160610050138.jpg",  # noqa
                    "https://www.youtube.com/watch?v=PyVEHIO6jZ0")

# Push each movie object into an array
movies = [deadpool, wolverine, xmen, revenant, bridge_of_spies, 
          fantastic_four, wwz, mission_impossible, shrek, casper]
          
# Generating the movie trailers page .html
fresh_tomatoes_with_tooltip.open_movies_page(movies)  

# Print in console the documentation of the class Movie
print(media.Movie.__doc__)  
