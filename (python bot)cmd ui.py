import tweepy, time, sys
 
CONSUMER_KEY = 'put consumer key here'
CONSUMER_SECRET = 'put secret key here'
ACCESS_KEY = 'put access key here'
ACCESS_SECRET = 'put access secret key here'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
a = api.get_status(912886007451676672, tweet_mode='extended')
#functions
def tweet():
    to_tweet = True
    tweet_text = input("Enter your tweet content below... Only the first 140 characters will be   used.\n>>> ")
    api.update_status(tweet_text[0:140])
    print("You tweeted \n'" + tweet_text[0:140] + "'")
    restart = input("Do you want to tweet again? (Y/N)\n>>> ")
    if restart.lower() == "y":
        tweet()
    else:
        print("Returning to the menu")

def keyword_follow():
    search_phrase = input("What do you want to search for?\n>>> ").strip()
    search_number = input("How many results do you want to return?\n>>> ")
    search_result = api.search(search_phrase, rpp=search_number)
    j=0;
    
    
    for i in search_result:
            user = api.get_user(1088398616)
            print(i.user.screen_name + " said " + i.text + "\n")
            to_follow = input("Do you want to follow " + i.user.screen_name + "? (Y/N)\n>>> ")
            if to_follow.lower() == "n":
                print(i.user.screen_name + " was not followed!")
    
            else:
                api.create_friendship(i.user.screen_name)
                print("You followed " + i.user.screen_name + "!\n")

def keyword_retweet():
    search_phrase = input("What do you want to search for?\n>>> ").strip()
    search_number = input("How many results do you want to return?\n>>> ")
    search_result = api.search(search_phrase, rpp=search_number)
    for i in search_result:
        user = api.get_user(1088398616)
        print(i.user.screen_name + " said " + i.text + "\n")
        to_retweet = input("Do you want to retweet" + i.user.screen_name + "? (Y/N)\n>>> ")
        if to_retweet.lower() == "n":
            print (i.user.screen_name + " was not retweeted!")
        else:
            api.retweet(i.id)
            print ("Retweeted!\n")
            again = input("See more? (Y/N)\n>>> ")
            if again.lower() == "n":
                break       
    
    restart = input("Do you want to search again? (Y/N)\n>>> ")
    if restart.lower() == "n":
        print ("Returning to the Main Menu...\n")
    else:
        return keyword_retweet()


#main menu        
keep_running = True
while keep_running:
    print("Main Menu")
    print("---------\n")
    selection = input("(1)Tweet  | (2)Keyword Follow |  (3)Keyword Retweet | (4)End\n\n>>> ")
    if selection == "1":
        print("New Tweet")
        print("---------\n")
        tweet()
    elif selection == "2":
        print("Keyword Follow")
        print("--------------\n")
        keyword_follow()
    elif selection == "3":
        print("Keyword Retweet")
        print("---------------\n")
        keyword_retweet()
    
    else:
        print("BYE!\n\n")
        keep_running = False
