#1
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

selected_genres = genres[1:4]  # From Rock to Classical

# Loop through the selected slice
for genre in selected_genres:
    print("Selective play: " + genre)

#2
music_genres = [genre + " Music" for genre in genres]
print(music_genres)

#3
for number in range(10, 0, -1):
    print(number)
print("The beat drops now!")