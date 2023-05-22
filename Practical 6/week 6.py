# Favourite movie genres among Chinese university students
import matplotlib.pyplot as plt
# create dictionary with movie genres and number of students
movie_genres = {'Comedy': 73, 'Action': 42, 'Romance': 38, 'Fantasy': 28, 'Science-fiction': 22, 'Horror': 19, 'Crime': 18, 'Documentary': 12, 'History': 8, 'War': 7}
# create pie chart
explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Movie_genre= [key for key in movie_genres]
The_number_of_students_for_which_this_genre_is_their_favourite= [value for value in movie_genres.values()]
plt.figure(figsize=(10,10), dpi=100)
plt.pie(The_number_of_students_for_which_this_genre_is_their_favourite,labels=Movie_genre,autopct="%1.1f%%",explode=explode,shadow=False,startangle=90)
plt.axis('equal')
plt.show()
# print number of students who prefer a given movie genre
genre = 'Comedy' # replace with desired genre
print(f"{movie_genres[genre]} students prefer {genre} movies.")

# Olympic Costs
import numpy as np
costs = [1, 8, 15, 7, 5, 14, 43, 40]

# print sorted list of Olympic costs
sorted_costs = sorted(costs)
print(sorted_costs)

# create bar plot of sorted Olympic costs
data = [1, 8, 15, 7, 5, 14, 43, 40]
plt.bar(range(len(sorted_costs)), sorted_costs)
labels = ["Los Angeles 1984", "Seoul 1988", "Barcelona 1992", "Atlanta 1996", "Sydney 2000", "Athens 2003", "Beijing 2008", "London 2012"]
plt.title('Cost of Hosting Summer Olympic Games')
plt.xticks(range(len(data)),labels,rotation=18)
plt.ylabel('Cost (in $ billions)')
plt.show()

