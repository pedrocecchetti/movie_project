import webbrowser


# Creating Video Class to use as a Superclass to Movies and
class Video():
    """The class Video is used as a Superclass of Movies and Series classes

    Attributes:
    -----------
    title: String
        The title of the Movie in English

    duration: int
        The duration of the Movie in minutes

    trailer_youtube_url: String
        The Youtube URL for the movie trailer

    Methods:
    -----------
    show_trailer()
        This method will play the youtube trailer of the selected Movie
    """
    def __init__(self, title, duration, trailer_youtube_url):
        self.title = title
        self.duration = duration
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


# Creating Movie class that inherits from Video
class Movie(Video):

    """The class Movie is used to generate Movies objects
     These objects will be used in the HTML page to generate the layout and
    the users will be able to see information and play the youtube Trailer

    Attributes(Inherited from Video):
    -----------
    title: String
        The title of the Movie in English

    duration: int
        The duration of the Movie in minutes

    trailer_youtube_url: String
        The Youtube URL for the movie trailer

    Attributes:
    -----------
    storyline: String
        This is a short text describing the storyline of the movie

    poster_image_url: String
        This is an URL to a HD image of the movie Poster

    Methods(Inherited from Video):
    -----------
    show_trailer()
        This method will play the youtube trailer of the selected Movie
    """
    def __init__(self, title, duration, trailer_youtube_url, storyline,
                 poster_image_url):
        Video.__init__(self, title, duration, trailer_youtube_url)
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


# Creating Series class with different arguments, but didn't used it Yet
class Series(Video):
    """The class Series is used to generate Series objects
     These objects will be used in the HTML page to generate the layout and
     the users will be able to see information and play the youtube Trailer

     Attributes(Inherited from Video):
     -----------
     title: String
        The title of the Movie in English

     duration: int
        The duration of the Movie in minutes

     trailer_youtube_url: String
        The Youtube URL for the movie trailer

     Attributes:
     -----------
     num_of_episodes: int
        This is an int with the total number of episodes of the series

     num_of_seasons: int
        This is an int with the total number of seasons of the series

     Methods(Inherited from Video):
     -----------
     show_trailer()
        This method will play the youtube trailer of the selected Movie
    """
    def __init__(self, title, duration, trailer_youtube_url, storyline,
                 num_of_episodes, num_of_seasons, poster_image_url):
        Video.__init__(self, title, duration, trailer_youtube_url)
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.num_of_episodes = num_of_episodes
        self.num_of_seasons = num_of_seasons



