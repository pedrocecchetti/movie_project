import movies
import fresh_tomatoes

avatar = movies.Movie("Avatar", 162,"https://www.youtube.com/watch?v=5PSNL1qE6VY","A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.", "https://resizing.flixster.com/Yq4pN3qojAZDF6QJFd_yE2Zmr1o=/206x305/v1.bTsxMTE3Njc5MjtqOzE3ODU5OzEyMDA7ODAwOzEyMDA")
moana  = movies.Movie("Moana",107,"https://www.youtube.com/watch?v=LKFuXETZUsI", "In Ancient Polynesia, when a terrible curse incurred by the Demigod Maui reaches Moana's island, she answers the Ocean's call to seek out the Demigod to set things right.","https://m.media-amazon.com/images/M/MV5BMjI4MzU5NTExNF5BMl5BanBnXkFtZTgwNzY1MTEwMDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg")
it = movies.Movie("It",135,"https://www.youtube.com/watch?v=FnCdOQsX5kc","In the summer of 1989, a group of bullied kids band together to destroy a shapeshifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.","https://m.media-amazon.com/images/M/MV5BZDVkZmI0YzAtNzdjYi00ZjhhLWE1ODEtMWMzMWMzNDA0NmQ4XkEyXkFqcGdeQXVyNzYzODM3Mzg@._V1_SY1000_CR0,0,666,1000_AL_.jpg")
the_conjuring = movies.Movie("The Conjuring", 134,"https://www.youtube.com/watch?v=VFsmuRPClr4","Ed and Lorraine Warren travel to North London to help a single mother raising 4 children alone in a house plagued by a supernatural spirit.", "https://m.media-amazon.com/images/M/MV5BZjU5OWVlN2EtODNlYy00MjhhLWI0MDUtMTA3MmQ5MGMwYTZmXkEyXkFqcGdeQXVyNjE5MTM4MzY@._V1_SY1000_CR0,0,674,1000_AL_.jpg")
wall_e = movies.Movie("Wall-E",98,"https://www.youtube.com/watch?v=pATSLKKeKVY","In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.","https://m.media-amazon.com/images/M/MV5BMjExMTg5OTU0NF5BMl5BanBnXkFtZTcwMjMxMzMzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg")
get_out = movies.Movie("Get Out", 104, "https://www.youtube.com/watch?v=DzfpyUB60YY","A young African-American visits his white girlfriend's parents for the weekend, where his simmering uneasiness about their reception of him eventually reaches a boiling point.","https://m.media-amazon.com/images/M/MV5BMjUxMDQwNjcyNl5BMl5BanBnXkFtZTgwNzcwMzc0MTI@._V1_SY1000_CR0,0,675,1000_AL_.jpg")


movie_array = [avatar,moana,it,wall_e,get_out,the_conjuring]

fresh_tomatoes.open_movies_page(movie_array)