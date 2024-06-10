webseries = ["Breaking Bad", "Vampire Diaries", "Stranger Things", "Dark"]

# adding elements in the list

webseries.append("Mr Robot")

print(webseries)
# 2nd method --> insert adds element in the specified index

webseries.insert(2, "Game of Thrones")

print(webseries)

# 3rd method adds another list in single list

movies = ["Iron man", "Thor", "Captain America", "Avengers"]

webseries.extend(movies)

print(webseries)

# removing elements from list

webseries.remove("Mr Robot")

print(webseries)

# removing using pop 

webseries.pop(5)

print(webseries)

webseries.pop()

print(webseries)

# using del keyword

del webseries[2]

print(webseries)

# using clear keyword

webseries.clear()

print(webseries)
print(len(webseries))