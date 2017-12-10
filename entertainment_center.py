import media
import fresh_tomatoes

#below are six instances of the object Movie which is defined in media.py
eraserhead = media.Movie("Eraserhead",
                         "A surreal tale of a man named Henry and his existential troubles",
                         "https://s3.amazonaws.com/criterion-production/shop_product_images/734-79885c85c59cb6da1aedfc1ac5b33197/CTA_1143_original.jpg",
                         "https://youtu.be/oK-2_OsBe0s")

nosferatu = media.Movie("Nosferatu",
                        "A stylish and early adaptation of Bram Stoker's Dracula",
                        "https://upload.wikimedia.org/wikipedia/en/9/92/Nosferatuposter.jpg",
                        "https://youtu.be/ZxlJxDr26mM")

dr_caligari = media.Movie("The Cabinent of Dr. Calagari",
                          "A German Expressionist film about an insane hypnotist who uses a somnambulist to commit murders",
                          "https://i0.wp.com/www.posterconnection.com/blogs/images/caligari_stahl%20arpke.gif",
                          "https://youtu.be/Y9TQkh6F4ZU")

wild_strawberries = media.Movie("Wild Strawberries",
                                "A pensive doctor picks up some hitch-hikers on his wayto receive an award. What follows is pensive nostalgia.",
                                "http://img.moviepostershop.com/wild-strawberries-movie-poster-1957-1010460666.jpg",
                                "https://youtu.be/n_ZbPHJH2w4")

there_will_be_blood = media.Movie("There Will Be Blood",
                                  "A man becomes a morally corrupt oil tycoon",
                                  "https://images-na.ssl-images-amazon.com/images/I/71sSoV%2B-DoL._AC_UL320_SR228,320_.jpg",
                                  "https://youtu.be/OjZ1rUQQKxY")

metropolis = media.Movie("Metropolis",
                         "An early dystopian sci-fi movie about class division and oppression of the working class",
                         "http://imgc.allpostersimages.com/img/posters/metropolis-german-movie-poster-1926_u-L-P99V9N0.jpg",
                         "https://youtu.be/on2H8Qt5fgA")

#this array contains the Movie objects created above and is passed into the fresh_tomatoes.open_movies_page() function defined in fresh tomatoes.py
movies = [eraserhead, nosferatu, dr_caligari, wild_strawberries, there_will_be_blood, metropolis]
fresh_tomatoes.open_movies_page(movies)

                          
                          
