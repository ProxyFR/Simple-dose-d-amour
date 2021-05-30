import twitter
import random
import time

limitTweets = 300
limitSearchs = 180
tweets = 0
searchs = 0
tweetsAlreadyReplyedTo = []

api = twitter.Api(consumer_key="mVR4RiKk2t10ikmLRJ5KxaYAN",
                    consumer_secret="HYNVe4liGqsOujNKAFYnSWJ3TYPA7LbmmTBFCBCn96MmXtN4K5",
                    access_token_key="1398791214388887552-YZ7gSrmzAPszwBQyoXVnYrevsnTrrP",
                    access_token_secret="pQjvvW60Mz2wnBYKrEifuGn5aZ4l1H9SQcvAoJuhfE8rV")

doseDamour = ["Pouf!! Voila une petite dose d'amour pour toi, il sufisait de demander",
            "Sache que tu es aimé par quelqu'un quelque part <3 Passes une bonne journée",
            "Je suis là pour te donner un peu d'amour ça tombe bien <3",
            "Et hop!! un peu d'amour pour toi aussi (tu as cru que j'allais pas pensé à toi avoue)",
            "Pas de soucis je suis là pour te donner de l'amour <3",
            "Besoin d'amour ? Pas de soucis en voila pour toi <3",
            "En manque d'amour ? Pas de soucis en voila pour toi <3",
            "Tu as demandé de l'amour ? En voila c'est aussi simple que ça!",
            "Sache que je t'aime! Qui que tu sois, où que tu sois <3",
            "Et si je te donnais de l'amour moi ?! Aller tiens <3",
            "Une petite dose d'amour pour la 2 et en vitesse! Oui oui c'est pour toi",
            "Souviens toi qu'il y aura toujours quelqu'un pour te donner de l'amour, en attendant ça viens de moi <3",
            "Il y a de l'amour pour tout le monde!! En voila une petite dose pour toi <3",
            "Hop une petite dose d'amour pour toi parce que je t'aime <3 oui oui sincèrement!!",
            "PSSSST!! Le dis à personne mais voila un peu d'amour pour toi <3",
            "Tu m'érites tout l'amour du monde c'est certain <3",
            ]

def replyToStatus(content, idToReply):
    global tweets
    reply = api.PostUpdate(content,in_reply_to_status_id=idToReply)
    tweets += 1

def search():
    global searchs
    global tweets
    global tweetsAlreadyReplyedTo
    results = api.GetSearch(raw_query="q=besoin%20d%27amour%20&src=typed_query&&f=live&result_type=recent&count=200")
    for search in results:  
        searchs += 1
        if(search.id in tweetsAlreadyReplyedTo):
            pass

        elif((search.id in tweetsAlreadyReplyedTo) == False):
            tweetsAlreadyReplyedTo.append(search.id)
            replyToStatus(("@" + search.user.screen_name + " " + random.choice(doseDamour)), search.id)

def start():
    global searchs
    global tweets
    global limitTweets
    global limitSearchs
    stop = False
    while(not stop):
        search()
        print(searchs)
        print(tweets)
        if(searchs >= limitSearchs):
            print("Limite atteinte des searchs")
            print("Fini, on attend 12H maintenant et on reprend.")
            time.sleep(43200)
            print("C'est reparti!")
        elif(tweets >= limitTweets):
            print("Limite atteinte des tweets")
            print("Fini, on attend 12H maintenant et on reprend.")
            time.sleep(43200)
            print("C'est reparti!")
        print(f"On a donné de l'amour à {str(tweets)} personnes !")
        time.sleep(5)

start()
