users=[{"id":0,"name":"Hero"},
       {"id":1,"name":"Dunn"},
       {"id":2,"name":"sue"},
       {"id":3,"name":"lol"},
       {"id":4,"name":"lola"},
       {"id":5,"name":"surya"},
       {"id":6,"name":"spacee"},
       {"id":7,"name":"chi chi"}
       ]
frienship_pairs=[(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7)]

friendships={user["id"]:[] for user in users}

for i,j in frienship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

print(friendships)

def number_of_friends(user):
    user_id=user["id"]
    friend_id=friendships[user_id]
    return len(friend_id)

print(number_of_friends({"id":0,"name":"Hero"}))


total_connections=sum(number_of_friends(user) for user in users)
print(total_connections)







