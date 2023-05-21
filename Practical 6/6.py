# Favourite movie genres among Chinese university students
import matplotlib.pyplot as plt

# create dictionary with movie genres and number of students
movie_genres = {'Comedy': 73, 'Action': 42, 'Romance': 38, 'Fantasy': 28, 'Science-fiction': 22, 'Horror': 19, 'Crime': 18, 'Documentary': 12, 'History': 8, 'War': 7}

# create pie chart
plt.pie(movie_genres.values(), labels=movie_genres.keys())
plt.title('Favourite Movie Genres Among Chinese University Students')
plt.show()

# print number of students who prefer a given movie genre
genre = 'Comedy' # replace with desired genre
print(f"{movie_genres[genre]} students prefer {genre} movies.")

# Olympic Costs
costs = [1, 8, 15, 7, 5, 14, 43, 40]

# print sorted list of Olympic costs
sorted_costs = sorted(costs)
print(sorted_costs)

# create bar plot of sorted Olympic costs
plt.bar(range(len(sorted_costs)), sorted_costs)
plt.title('Cost of Hosting Summer Olympic Games')
plt.xlabel('Olympic Games')
plt.ylabel('Cost (in $ billions)')
plt.show()

