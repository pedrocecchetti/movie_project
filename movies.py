import webbrowser


class Video():
    def __init__(self, title, duration, trailer_youtube_url):
        self.title = title
        self.duration = duration
        self.trailer_youtube_url = trailer_youtube_url
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    

class Movie(Video):
    def __init__(self, title, duration, trailer_youtube_url, storyline, poster_image_url):
        Video.__init__(self, title, duration, trailer_youtube_url)
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
    
class Series(Video):
    def __init__(self, title, duration, trailer_youtube_url, 
                num_of_episodes,num_of_seasons, poster_image_url):
            Video.__init__(self, title, duration, trailer_youtube_url)
            self.num_of_episodes = num_of_episodes
            self.num_of_seasons = num_of_seasons
            self.poster_image_url = poster_image_url
