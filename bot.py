import tweepy

all_keys = open('keys', 'r').read.splitlines()
api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.api(authenticator)

api.create_friendship('profamymcgovern')
api.create_friendship('wrmf_')
api.update_status('I am a bot designed by @wrmf_. Please do not message me, I do not currently support ')