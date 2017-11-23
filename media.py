import webbrowser

class Movie():
    """Used to sort info from each provided variable passed into it"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_rating, movie_length):
        """Sorts a given list out into separate variables"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating
        self.length = movie_length

    def show_trailer(self):
        """Opens the browser, directing to the defined url"""
        webbrowser.open(self.trailer_youtube_url)
