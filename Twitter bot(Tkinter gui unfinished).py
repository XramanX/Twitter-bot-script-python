from tkinter import *
import tweepy
from tweepy import API
CONSUMER_KEY = 'put consumer key here'
CONSUMER_SECRET = 'put secret key here'
ACCESS_KEY = 'put access key here'
ACCESS_SECRET = 'put access secret key here'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api: API = tweepy.API(auth)
a = api.get_status(912886007451676672, tweet_mode='extended')


class mainclass:
    def __init__(self):
        frame = Frame(bg='sky blue')
        frame.pack()
        root.geometry("250x170")
        root.title("Twitter Bot")
        self.button1 = Button(frame, text="Tweet", command=self.tweet,height = 3, width = 33,bg ='sky blue')
        self.button1.grid(row=0)
        self.button2 = Button(frame, text="Keyword Follow", command=self.key_follow,height = 3, width = 33,bg ='sky blue')
        self.button2.grid(row=2, sticky=W)
        self.button3 = Button(frame, text="Retweet", command=self.retweet,height = 3, width = 33,bg ='sky blue')
        self.button3.grid(row=1)

    def tweet(self):
        rootA = Tk()
        rootA.geometry("250x170")
        rootA.title("Tweet")
        frame1 = Frame(rootA,bg='sky blue')
        frame1.pack()
        label1 = Label(frame1, text="Enter the tweet(word limit = 140)",height = 2, width = 33,bg='sky blue')
        label1.pack()
        self.entry1 = Entry(frame1,bg='white',fg='black')
        self.entry1.pack()
        to_tweet = True

        self.button4 = Button(frame1, text="Tweet",height = 3, width = 33,bg ='sky blue')
        self.button4.pack()
        self.button4.bind("<Button-1>", self.click)

    def click(self, event):
        api.update_status(self.entry1.get())
        win = Toplevel()
        win.geometry("")
        win.wm_title("Window")
        b = Button(win, text="Tweet done", command=win.destroy)
        b.pack()

    def key_follow(self):
        rootB = Tk()
        rootB.geometry("250x170")
        rootB.title("Follow")
        frame = Frame(rootB,bg='sky blue')
        frame.pack()
        label1 = Label(frame, text="What do you want to search?",height = 2, width = 33,bg='sky blue')
        label1.pack()
        self.entry1 = Entry(frame)
        self.entry1.pack()
        label2 = Label(frame, text="how many results do you want?",height = 2, width = 33,bg='sky blue')
        label2.pack()
        self.entry2 = Entry(frame)
        self.entry2.pack()
        self.button2 = Button(frame, text="Find", command=self.follow_click,height = 3, width = 33,bg ='sky blue')
        self.button2.pack()

    def follow_click(self):
        self.num = self.entry2.get()
        self.find = self.entry1.get()
        search_result = api.search(self.find, count=self.num)
        rootC = Tk()
        rootC.geometry("700x500")
        self.frame4 = Frame(rootC)
        self.frame4.pack()
        self.text4 = Text(self.frame4)
        self.text4.grid(row=0, column=0)
        self.button3 = Button(self.frame4, text="Follow", command=self.follow,height = 3, width = 33,bg ='sky blue')
        label5 = Label(self.frame4, text="Enter username to follow",height = 2, width = 33,bg='sky blue')
        label5.grid(row=3, column=0)
        self.entry5 = Entry(self.frame4)
        self.entry5.grid(row=4, column=0)
        self.button3.grid(row=5, column=0)
        user = api.get_user(1088398616)

        for i in search_result:
            tweet = i.user.screen_name + " " + "said" + " " + i.text
            char_list = [tweet[j] for j in range(len(tweet)) if ord(tweet[j]) in range(65536)]
            tweet = ''
            for j in char_list:
                tweet = tweet + j
            self.show_res(tweet)

    def follow(self):
        self.uname = self.entry5.get()
        api.create_friendship(self.uname)
        win = Toplevel()
        win.geometry("")
        win.wm_title("Window")
        b = Button(win, text="Follow done", command=win.destroy,height = 3, width = 33,bg ='sky blue')
        b.pack()

    def show_res(self, content):

        self.text4.insert("1.0", content + "\n\n")

    def retweet(self):

        rootD = Tk()
        rootD.geometry("250x170")
        rootD.title("Follow")
        frame = Frame(rootD,bg='sky blue')
        frame.pack()
        label1 = Label(frame, text="What do you want to search?",height = 2, width = 33,bg='sky blue')
        label1.pack()
        self.entry6 = Entry(frame)
        self.entry6.pack()
        label2 = Label(frame, text="how many retweets do you want?", height=2, width=33, bg='sky blue')
        label2.pack()
        self.entry7 = Entry(frame)
        self.entry7.pack()
        self.button2 = Button(frame, text="Find", command=self.find, height=3, width=33, bg='sky blue')
        self.button2.pack()
    def find(self):
        print("unfinished")





root = Tk()
ob = mainclass()
root.mainloop()
