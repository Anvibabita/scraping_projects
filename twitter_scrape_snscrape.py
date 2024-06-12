import pandas as pd
from collections import Counter
import snscrape.modules.twitter as sntwitter

# Creating a user list consisting of Twitter accounts
users = [
    'shakira',
    'KimKardashian',
    'rihanna',
    'jtimberlake',
    'KingJames',
    'neymarjr',
]

# Function to get followings for a given username
def get_followings(username):
    followings = []
    for tweet in sntwitter.TwitterFollowFollowingScraper(username).get_following():
        followings.append(tweet.username)
    return followings

# Loop through users to get their followings
followings = {}
following_list = []
for person in users:
    print('#####\nStarting: ' + person + '\n#####')
    try:
        followings[person] = get_followings(person)
        following_list += followings[person]
    except:
        print('Error')

# Get the 10 most followed accounts
most_common_followed = Counter(following_list).most_common(10)

# Print the most common followed accounts
print("Most common followed accounts:")
for account, count in most_common_followed:
    print(account, count)

# Get follow relations
follow_relations = {}
for following_user in followings.keys():
    follow_relation_list = []
    for followed_user in followings.keys():
        if followed_user in followings[following_user]:
            follow_relation_list.append(True)
        else:
            follow_relation_list.append(False)
    follow_relations[following_user] = follow_relation_list

# Convert follow relations into a pandas dataframe
following_df = pd.DataFrame.from_dict(follow_relations, orient='index', columns=followings.keys())
print("\nFollow relations dataframe:")
print(following_df)
