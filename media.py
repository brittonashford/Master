import webbrowser


class Movie():
    # This class contains a constructor class used in entertainment_center.py
    # and a function that will be used in fresh_tomatoes.py

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        # This constructor creates an isntance of the object Movie which
        # contains the title, storyline, movie poster and trailer.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


def show_trailer(self):
        # This function opens a youtube video of the movie's trailer.
        webbrowser.open(self.trailer_youtube_url)
