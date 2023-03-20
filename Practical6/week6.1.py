import matplotlib.pyplot as plt
election_data = {'Comedy': 73, 'Action': 42, 'Romance': 38, 'Fantasy': 28, 
'Science-fiction': 22, 'Horror': 19, 'Crime': 18, 'Documentary': 12, 
'History': 8, 'War': 7}
explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Movie_genre= [key for key in election_data]
The_number_of_students_for_which_this_genre_is_their_favourite= [value for value in election_data.values()]
plt.figure(figsize=(10,10), dpi=100)
plt.pie(The_number_of_students_for_which_this_genre_is_their_favourite,labels=Movie_genre,autopct="%1.1f%%",explode=explode,shadow=False,startangle=90)
plt.axis('equal')
plt.show()
