user_list = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0,
                          "Norah Jones": 4.5, "Phoenix": 5.0,
                          "Slightly Stoopid": 1.5,
                          "The Strokes": 2.5, "Vampire Weekend": 2.0},

             "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5,
                      "Deadmau5": 4.0, "Phoenix": 2.0,
                      "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},

             "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0,
                      "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5,
                      "Slightly Stoopid": 1.0},

             "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0,
                     "Deadmau5": 4.5, "Phoenix": 3.0,
                     "Slightly Stoopid": 4.5, "The Strokes": 4.0,
                     "Vampire Weekend": 2.0},

             "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0,
                        "Norah Jones": 4.0, "The Strokes": 4.0,
                        "Vampire Weekend": 1.0},

             "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0,
                        "Norah Jones": 5.0, "Phoenix": 5.0,
                        "Slightly Stoopid": 4.5, "The Strokes": 4.0,
                        "Vampire Weekend": 4.0},

             "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0,
                     "Norah Jones": 3.0, "Phoenix": 5.0,
                     "Slightly Stoopid": 4.0, "The Strokes": 5.0},

             "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0,
                          "Phoenix": 4.0, "Slightly Stoopid": 2.5,
                          "The Strokes": 3.0}
             }


def get_user_list():
    return user_list


def minkowski(user_rating1, user_rating2, r):
    distance = 0
    has_common = False
    for item in user_rating1:
        if item in user_rating2:
            has_common = True
            distance += pow(abs(user_rating1[item] - user_rating2[item]), r)
    if has_common:
        return pow(distance, 1 / r)
    else:
        return 0


def compute_nearest_neighbour(username, user_list, r):
    distances = []
    for user in user_list:
        if user != username:
            distances.append((user, minkowski(user_list[user], user_list[username], r)))
    distances.sort(key=lambda x: x[1], reverse=False)
    return distances

def recommand_nearest_neighbour(username,user_list,r):
    distances=compute_nearest_neighbour(username,user_list,r)
    user_ratings=user_list[username]
    neighbour_ratings=user_list[distances[0][0]]
    recommandations=[]
    for item in neighbour_ratings:
        if item not in user_ratings:
            recommandations.append((item,neighbour_ratings[item]))
    return recommandations


