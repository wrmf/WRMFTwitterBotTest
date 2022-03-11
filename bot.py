import tweepy

import keys

api_key = keys.api_key
api_key_secret = keys.api_key_secret
access_token = keys.access_token
access_token_secret = keys.access_token_secret

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.api(authenticator)

api.create_friendship('profamymcgovern')
api.create_friendship('wrmf_')
api.update_status('I am a bot designed by @wrmf_. Please do not message me, I do not currently support ')