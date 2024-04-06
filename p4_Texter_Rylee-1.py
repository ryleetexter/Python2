# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 15:40:39 2024

@author: rylee
"""

##Problem 4


#file one: imdb-top-rated.csv, Rank,Title,Year,IMDB Rating
#file two: imdb-top-grossing.csv, Rank,Title,Year,USA Box Office
#file three: imdb-top-casts.csv, Title,Year,Director,Actor1,Actor2,Actor3,Acotr4,Actor5

import csv

#displays the ranking of tuples (director, actor, # of Movies) for movies in which
#the director and actor worked together and the movie is also rated in the top
#rated movie list
def display_top_collaborations():
    ranking_of_tuples = []
    sortedTuples = []
    collabs = []
    
    #opens two cvs files
    file3 = open("imdb-top-casts.csv", 'r', encoding="utf-8")
    file2 = open("imdb-top-grossing.csv", 'r', encoding="utf-8")
    reader = csv.reader(file3)
    reader2 = csv.reader(file2)
    
    #loops through each line of the file and assigns connections in 
    #list 'collabs'
    for line in reader:
       director = line[2]
       actor1 = line[3]
       actor2 = line[4]
       actor3 = line[5]
       actor4 = line[6]
       actor5 = line[7]
       movie = line[0]
       
       connection1 = (director, actor1, movie)
       connection2 = (director, actor2, movie)
       connection3 = (director, actor3, movie)
       connection4 = (director, actor4, movie)
       connection5 = (director, actor5, movie)
       
       connections = [connection1, connection2, connection3, connection4, connection5]
       for connection in connections:
           collabs.append(connection)
        
    ##loops through each collab and removes movies that are not on the top
    #grossing list
    for collab in collabs:
        movie = collab[2]
        isHere = False
        for line in reader2:
            if movie == line[1]:
                isHere = True
        if(isHere == False):
            collabs.remove(collab)
      
    #loops through collabs and appends tuples containing the movie director, 
    #actor, and the number of movies together
    for collab in collabs:
        director = collab[0]
        actor = collab[1]
        #count is number of movies together
        count = 0
        for connection in collabs:
            if connection[0] == director and connection[1] == actor:
                count = count + 1
        
        tup = (director, actor, count)
        ranking_of_tuples.append(tup)
    
    nums = []
    
    #loops through the tuples to append the movies to nums
    #same number of movies is removed in nums
    for i in ranking_of_tuples:
        movieCount = i[2]
        isHere = False
        if movieCount in nums:
            isHere = True
        if(isHere == False):
            nums.append(movieCount)
            
    ##sorts nums inr reverse
    nums.sort(reverse=True)
    
    #sorts the data using nums
    for num in nums:
        for tup in ranking_of_tuples:
            if tup[2] == num:
                sortedTuples.append(tup)
    
    
    #prints top ten tuples
    for i in range(0,10):
        print(sortedTuples[i])
        
        
        
#displays the ranking of actors from the top grossing list ordered by the
#total box office money they acted in
def display_top_actors():
    
    actorsBoxOffice = {}
    movies = []
    movies_boxoffice = {}
    actors = []
    file3 = open("imdb-top-casts.csv", 'r', encoding="utf-8")
    file2 = open("imdb-top-grossing.csv", 'r', encoding="utf-8")
    reader = csv.reader(file2)
    
    #loops through top grossing list and appends every movie to a list movies
    # movie: boxOffice is also added here to movies_boxOffice dictionary
    for line in reader:
        movie = line[1]
        movies.append(movie)
        movies_boxoffice[movie] = line[3]
        
    
    reader = csv.reader(file3)
    

    #updates actors list with new actors and updates actorsBoxOffice dictionary
    #with actor :box office
    for line in reader:
        if line[0] in movies:
            current_actors = []
            current_actors.append(line[3])
            current_actors.append(line[4])
            current_actors.append(line[5])
            current_actors.append(line[6])
            current_actors.append(line[7])
            for an_actor in current_actors: 
                if an_actor in actors:
                    actorsBoxOffice[an_actor] += movies_boxoffice[line[0]]
                else:
                    actors.append(an_actor)
                    actorsBoxOffice[an_actor] = movies_boxoffice[line[0]]
       
   
    issorted = (sorted(actorsBoxOffice.items(), key = lambda item:float(item[1]), reverse=True))

    #prints the sorted values
    
    for actor,money in issorted:
         print("{}:{}".format(actor, money))
    
    
def main():
    print("display top collaborators: (first ten)")
    display_top_collaborations()
    
    print("display top actors")
    display_top_actors()

main()