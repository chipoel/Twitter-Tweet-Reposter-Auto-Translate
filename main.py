import tweepy
from time import sleep
from translate import Translator

translator= Translator(to_lang="ID") #Translate tweet to other language by changing to_lang value

consumer_key="xxx"
consumer_secret="xxx"

access_token="xxx"
access_token_secret="xxx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

last_id = None

def get_user_latest_tweet(screen_name):
    user_tweets = api.user_timeline(screen_name=screen_name, tweet_mode = "extended")
    if user_tweets:
        return user_tweets[0].full_text
    else:
        return None

def get_user_latest_tweet_id(screen_name):
    user_tweets = api.user_timeline(screen_name=screen_name)
    if user_tweets:
        return user_tweets[0].id
    else:
        return None

def tweet(text):
    translation = translator.translate(text)
    api.update_status(translation)
    print(translation)


def clout_chase_tweet(famous_person):
    famous_person_latest_tweet = get_user_latest_tweet(famous_person)
    famous_person_latest_tweet_id = get_user_latest_tweet_id(famous_person)
    global last_id
    if famous_person_latest_tweet_id != last_id:
        try:
            tweet(famous_person_latest_tweet)
            last_id = famous_person_latest_tweet_id
            print("Reposted: ", last_id)
        except tweepy.TweepyException as e:
            print(e.api_messages)
    else:
        print("Already Reposted!")

def tweet_loop():
    famous_people = ["username"] #your target username
    for famous_person in famous_people:
        clout_chase_tweet(famous_person)


while True:
    tweet_loop()
    sleep(90)
