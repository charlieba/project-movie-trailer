import webbrowser


class Movie():
    """ This Class provides a way to store movie releated information

        Attributes:
        title     (str): Title of the movie.
        storyline (str): Description of story line of the movie.
        poster    (str): Highlight image of the movie.
        trailer   (str): Youtube link of the trailer of the movie

        Methods:
        show_trailer (self); Open the web browser showing and playing 
        the movie trailer

    """
    def __init__(self, movie_title, movie_storyline, poster_image, 
                 trailer_youtube):  
        # Title, save the title of the movie
        self.title = movie_title  
        # Story Line, save the description of the movie
        self.storyline = movie_storyline  
        # Poster, save the highlight image of the movie
        self.poster_image_url = poster_image  
        # Trailer, save the youtube link with the trailer
        self.trailer_youtube_url = trailer_youtube 

    # This method open the web browser showing and playing the movie trailer    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
