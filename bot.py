import tweepy

import keys

API_KEY = '7xtFYya5kF9DMdhC9kwgSTKZs'
API_SECRET = '2CRoBWpT8ketjLHH8G4gb9glSKhkDpApcBp7TdjK3bQlpgMv3A'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAMiBaAEAAAAAhdoTx2hg%2BwDnllwKVVoMXBZ%2BU2Q%3DpOGn6A340G9i0yDtW9lgiB26FgUGUwA7LE9GboPadtBFkKQ6qI'
ACCESS_TOKEN = 'ZTY3U2w0MmRkV2pwNnppM04yUzU6MTpjaQ'
ACCESS_SECRET = '0VbmvmiLMLYavFQZK0syjDeDH4ZW6db9JOS6TKtS26qQANr3iQ'

#client = tweepy.Client(bearer_token=BEARER_TOKEN)
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    bearer_token=BEARER_TOKEN,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)



client.follow_user(target_user_id=client.get_user(username="wrmf_"))
client.create_tweet(text="test")
