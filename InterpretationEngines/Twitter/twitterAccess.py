import tweepy


#These get me the APP and my personal key
access_token = "2980642296-DhGM52aqKOiv1ujIgbxOdOCc1g8DgSoi9LnAFXT"
access_token_secret = "YaVrJNeEdp7O5ulWkXmbzcSzS4JkK85BWgQvN2Qq95Pat"
consumer_key =  "ES9oS0bpmdZQHhje1XrfPpqFx"
consumer_secret = "sUucyVHDSCjKtMWzf6K7h5S77k6XTgFwZrHrFQG7ShcO5JyEdW"


#Gets authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#The api object has now been created. We totally wait for rate limits to refresh I guess?
api = tweepy.API(auth_handler=auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

