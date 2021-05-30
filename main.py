import twitter
import random
import time

limitTweets = 300
limitSearchs = 180
tweets = 0
searchs = 0

api = twitter.Api(consumer_key="mVR4RiKk2t10ikmLRJ5KxaYAN",
                    consumer_secret="HYNVe4liGqsOujNKAFYnSWJ3TYPA7LbmmTBFCBCn96MmXtN4K5",
                    access_token_key="1398791214388887552-YZ7gSrmzAPszwBQyoXVnYrevsnTrrP",
                    access_token_secret="pQjvvW60Mz2wnBYKrEifuGn5aZ4l1H9SQcvAoJuhfE8rV")

doseDamour = ["Pouf!! Voila une petite dose d'amour pour toi, il sufisait de demander", "Sache que tu es aimé par quelqu'un quelque part <3 Passes une bonne journée", "Je suis là pour te donner un peu d'amour ça tombe bien <3", "Et hop!! un peu d'amour pour toi aussi (tu as cru que j'allais pas pensé à toi avoue)", "Pas de soucis je suis là pour toi <3", "Besoin d'amour ? Pas de soucis en voila pour toi <3", "En manque d'amour ? Pas de soucis en voila pour toi <3"]

def replyToStatus(content, idToReply):
    global tweets
    tweets += 1
    reply = api.PostUpdate(content,in_reply_to_status_id=idToReply)

def search():
    global searchs
    searchs += 1
    results = api.GetSearch(raw_query="q=besoin%20d%27amour%20&src=typed_query&&f=live&result_type=recent&count=100")
    for search in results:
        replyToStatus(("@" + search.user.screen_name + " " + random.choice(doseDamour)), search.id)

search()

def start():
    global searchs
    global tweets
    global limitTweets
    global limitSearchs
    stop = False
    while(not stop):
        try:
            search()
        except:
            print("Erreur (probablement de quota, on arrete)")
            stop = True
        if(searchs >= limitSearchs):
            print("Limite atteinte des searchs")
            stop = True
        elif(tweets >= limitTweets):
            print("Limite atteinte des tweets")
            stop = True
        print(f"On a tweeté {str(tweets)} fois !")
        time.sleep(5)
    print("Fini, on attend 3H maintenant et on reprend.")

start()
