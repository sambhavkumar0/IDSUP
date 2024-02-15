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

num_users=len(users)
avg_connections=total_connections/num_users

print(avg_connections)


number_of_friends_by_id=[(user['id'],number_of_friends(user)) for user in users]
print(number_of_friends_by_id)

number_of_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1],reverse=True)

print(number_of_friends_by_id)                         





def foaf_ids_bad(user):
    user_id=user["id"]
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]
            if foaf_id!=user_id
            and foaf_id not in friendships[user_id]]
print(foaf_ids_bad({"id":0,"name":"Hero"}))




