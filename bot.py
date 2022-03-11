import tweepy

import keys

api_key = keys.api_key
api_key_secret = keys.api_key_secret
access_token = keys.access_token
access_token_secret = keys.access_token_secret

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

client = tweepy.Client(bearer_token=keys.bearer_token, access_token=access_token,
                       access_token_secret=access_token_secret)
users = client.get_users(usernames=["wrmf_", "profamymcgovern"])
for n in users:
    print(n)

client.follow_user(target_user_id=1387140155149013002, user_auth=False)