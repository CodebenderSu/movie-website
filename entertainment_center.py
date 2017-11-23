import media
import fresh_tomatoes

#This file is used to store data for each movie, which is then loaded dynamically
#into a webpage, defined by fresh_tomatoes.py
sucker_punch = media.Movie("Sucker Punch",
                           "A young girl is institutionalized by her abusive stepfather, retreating to an alternative reality as a coping strategy, envisioning a plan to help her escape.",
                           "https://upload.wikimedia.org/wikipedia/en/9/9f/Sucker_Punch_film_poster.jpg",
                           "https://www.youtube.com/watch?v=MnF4SpS9gUw",
                           "PG-13",
                           "1h 50min")

hua_mulan = media.Movie("Hua Mulan",
                        "The epic story of the Chinese girl-warrior, Mulan, who fights to defend her father.",
                        "https://upload.wikimedia.org/wikipedia/en/7/72/Mulan_-_Rise_of_a_Warrior_poster.jpg",
                        "https://www.youtube.com/watch?v=gTAETFTIo_I",
                        "Not Rated",
                        "1h 54min")

httydragon = media.Movie("How To Train Your Dragon",
                         "A hapless young Viking who aspires to hunt dragons becomes the unlikely friend of a young dragon himself, and learns there may be more to the creatures than he assumed.",
                         "https://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg",
                         "https://www.youtube.com/watch?v=oKiYuIsPxYk",
                         "PG",
                         "1h 38min")

harmony = media.Movie("Harmony",
                      "In an utopian, futuristic world, where humanity has acquired eternal life, a young high ranked agent of the world's leading health company investigates a wave of suicides.",
                      "https://upload.wikimedia.org/wikipedia/en/c/c2/Harmony_%282015_film%29_poster.jpeg",
                      "https://www.youtube.com/watch?v=9zsdRecN4PI",
                      "Not Rated",
                      "1h 59min")

easy_a = media.Movie("Easy A",
                     "A clean-cut high school student relies on the school's rumor mill to advance her social and financial standing.",
                     "https://upload.wikimedia.org/wikipedia/en/9/95/Easy_a_australian.jpg",
                     "https://www.youtube.com/watch?v=KNbPnqyvItk",
                     "PG-13",
                     "1h 32min")

kikis_delivery_service = media.Movie("Kiki's Delivery Service",
                                     "A young witch, on her mandatory year of independent life, finds fitting into a new community difficult while she supports herself by running an air courier service.",
                                     "https://upload.wikimedia.org/wikipedia/en/0/07/Kiki%27s_Delivery_Service_%28Movie%29.jpg",
                                     "https://www.youtube.com/watch?v=XqN6OEAXfPI",
                                     "G",
                                     "1h 43min")

lets_be_cops = media.Movie("Let's Be Cops",
                           "Two struggling pals dress as police officers for a costume party and become neighborhood sensations.",
                           "https://upload.wikimedia.org/wikipedia/en/0/08/Let%27s_Be_Cops_poster.jpg",
                           "https://www.youtube.com/watch?v=ExciLtpHp74",
                           "R",
                           "1h 44min")

potc_curse = media.Movie("Pirates of the Caribbean: The Curse of the Black Pearl",
                         "Blacksmith Will Turner teams up with eccentric pirate \"Captain\" Jack Sparrow to save his love, the governor's daughter, from Jack's former pirate allies, who are now undead.",
                         "https://upload.wikimedia.org/wikipedia/en/8/89/Pirates_of_the_Caribbean_-_The_Curse_of_the_Black_Pearl.png",
                         "https://www.youtube.com/watch?v=naQr0uTrH_s",
                         "PG-13",
                         "2h 23min")

hot_fuzz = media.Movie("Hot Fuzz",
                       "A skilled London police officer is transferred to a small town that's harbouring a dark secret.",
                       "https://t2.gstatic.com/images?q=tbn:ANd9GcSlM2Ugu41GcdkqjVA7SLQeOZD6nWibTotxJPkTasDC8GkMypRL",
                       "https://www.youtube.com/watch?v=KOddZELDPmk",
                       "R",
                       "2h 1min")

movies = [sucker_punch, hua_mulan, httydragon, harmony, easy_a,
          kikis_delivery_service, lets_be_cops, potc_curse, hot_fuzz]
fresh_tomatoes.open_movies_page(movies)
