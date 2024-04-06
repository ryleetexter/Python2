# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:15:24 2024

@author: rylee
"""

import csv


##adds a user to a social network dictionary username: (fullname, [friends])
def add_user(sn, username, fullname):
    if username in sn:
        print("Username Already Exists")
        return False
    sn[username] = (fullname, [])
    return True

#adds connections between users
def add_friend(sn, user1, user2):
    try: 
        if user1 in sn and user2 in sn:
            sn[user1][1].append(user2)
            sn[user2][1].append(user1)
            return True
        else: return False
    except Exception:
        print("User does not exist")
        return(False)
    
##returns a list of friends which come from the user's friends - friend's
def get_friends(sn, user1, distance):
    friends = []
    
    #loops through friends of the user and adds them all to the friends list
    #subtracts distance to keep count of round number
    for user in sn[user1][1]:
        friends.append(user)
        dist = distance -1
    
    
    while(dist > 0):
        friends_copy = []
        
        #makes a copy of list friends
        for friend in friends:
            friends_copy.append(friend)
            
        #goes through the copied list of friends and adds friends from list
        for friend in friends_copy:
            for user in sn[friend][1]:
                if user != user1 and user not in friends:
                    friends.append(user)
                
        dist = dist - 1
    
        
    return(friends)

#saves a dictionary to a csv file 
def save_network(filename, sn):
    ##returns a CSV File 
    try:
        csv_file = open(filename, 'w')
        writer = csv.writer(csv_file)
        #loops through social network and writes it to the csv file
        for (username, friends) in sn.items():
            writer.writerow([username] + [friends[0]]+ [friends[1]])
    except FileNotFoundError:
        raise FileNotFoundError("No file found")
    except Exception as e:
        raise e
        
##returns a dictionary from a filename
def load_network(filename):
    try:
        
        social_network = {}
        csv_file = open(filename, 'r')
        reader = csv.reader(csv_file)
        
        #reads the file, and adds the username key and (fullname, friends) as values
        #in the dictionary
        for line in reader:
            if len(line)<1:
                continue
            username = line[0]
            fullname = line[1]
            friends = line[2]
            social_network[username] = (fullname, friends)
        return(social_network)
    
    except FileNotFoundError:
        raise FileNotFoundError("No File was found")
    except Exception as e:
        raise e
        
def main():
    social_network = {}
    
    ## adding users to the dictionary social_network
    add_user(social_network, "rylee", "Rylee Texter")
    print("add_user():")
    print("social network before")
    print(social_network)
    add_user(social_network, "maddie", "Madison Gamache")
    print("social network after: ")
    print(social_network)
    print()
    
    ## adding connections between those users
    print("add_friend()")
    print("before add_friend()")
    print(social_network)
    add_friend(social_network, "rylee", "maddie")
    print("after add_friend")
    print(social_network)
    print()


    add_user(social_network, "amy", "Amy Texter")
    add_user(social_network, "tyler", "Tyler Broyles")
    add_user(social_network, "celina", "Celina O")
    add_user(social_network, "arwen", "Arwen Finwells")
    add_user(social_network, "ash", "Ash Irvine")
    add_user(social_network, "megan", "Megan Cooley")
    add_user(social_network, "dylan", "Dylan Vargo")
    

    add_friend(social_network, "rylee", "ella")
    add_friend(social_network, "rylee", "amy")
    add_friend(social_network, "rylee", "tyler")
    add_friend(social_network, "maddie", "celina")
    add_friend(social_network, "amy", "arwen")
    add_friend(social_network, "ash", "tyler")
    add_friend(social_network, "megan", "arwen")
    add_friend(social_network, "ash", "dylan")
    
    #finding friends at a distance of 3
    print("get_friends()")
    friends = get_friends(social_network, "rylee",3)
    print("friends: {}".format(friends))
    print()
    
    #saving social_network to a csv_file
    print("save_network()")
    print("network saved")
    save_network("socialNetowrk0", social_network)
    print()
    
    #loading the file and returning the dictionary
    print("load_network()")
    sn1 = load_network("socialNetowrk0")
    print(sn1)
    
    
main()
