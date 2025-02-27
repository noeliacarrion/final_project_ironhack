
def get_followers(user_id): #function to extract all followers from the user
    list_users = []
    while True:
        try:
            for i, user in enumerate(tweepy.Cursor(api.followers, id=user_id, count=200).pages()):
                list_users += user
            user_final = [[user.id_str, user.created_at, user.name, user.screen_name, user.location, user.description,
                           user.followers_count, user.friends_count] for user in list_users]
            with open("../output/User_csv/%s_followers.csv" % user_id, 'w') as f:
                wr = csv.writer(f)
                wr.writerows([["id", "created_at", "name", "screen_name", "location", "description", "followers_count",
                               "friends_count"]])
                wr.writerows(user_final)
            pass
        except tweepy.TweepError:
            time.sleep(60 * 15)
            continue
        break


def get_friends(user_id): #function to extract all friends(people to whom the user follows) and create a csv with
             #the information
    list_users = []
    while True:
        try:
            for i, user in enumerate(tweepy.Cursor(api.friends, id=user_id, count=200).pages()):
                list_users += user
            user_final = [[user.id_str, user.created_at, user.name, user.screen_name, user.location, user.description,
                           user.followers_count, user.friends_count] for user in list_users]
            with open("../output/User_csv/%s_friends.csv" % user_id, 'w') as f:
                wr = csv.writer(f)
                wr.writerows([["id", "created_at", "name", "screen_name", "location", "description", "followers_count",
                               "friends_count"]])
                wr.writerows(user_final)
            pass
        except tweepy.TweepError:
            time.sleep(60 * 15)
            continue
        break
