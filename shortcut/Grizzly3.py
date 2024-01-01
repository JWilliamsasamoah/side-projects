from tkinter import *
import webbrowser
import subprocess

root = Tk()

root.title('Grizzly Assistant')
photo = PhotoImage(file='gazz.png')
photo2 = PhotoImage(file='bs.png')


def tab1():
    def tab2():
        label.destroy()
        b.destroy()
        labelpp = Label(root, image=photo)
        labelpp.grid()
        b2 = Button(root, text="Social media", command=open_social_media, width=127, bg="black", fg="white")
        b2.grid()
        b3 = Button(root, text="Entertainment", command=open_entertainment, width=127, bg="black", fg="white")
        b3.grid()
        b4 = Button(root, text="Anime", command=open_Anime, width=127, bg="black", fg="white")
        b4.grid()
        b5 = Button(root, text="Ordering food", command=open_ordering_food, width=127, bg="black", fg="white")
        b5.grid()
        b7 = Button(root, text="Shopping", command=open_shopping, width=127, bg="black", fg="white")
        b7.grid()
        b8 = Button(root, text="Productivity and Finance", command=open_productivity_and_finance, width=127, bg="black",
                    fg="white")
        b8.grid()
        bgames = Button(root, text="Games", command=games, width=127, bg="black", fg="white")
        bgames.grid()
        b11 = Button(root, text="Exit", command=root.quit, width=127, bg="black", fg="white")
        b11.grid()

    # My function for the buttons
    # Function for Social Media
    def instagram():
        webbrowser.open("https://www.instagram.com/")

    def snapchat():
        webbrowser.open("https://www.snapchat.com/")

    def facebook():
        webbrowser.open("https://www.facebook.com/")

    def twitter():
        webbrowser.open("https://twitter.com/")

    def tiktok():
        webbrowser.open("https://www.tiktok.com/")

    def discord():
        subprocess.call('C://Users//asamo//AppData//Local//Discord//app-1.0.9002//Discord.exe')

    # function for entertaiment

    def youtube_button():
        webbrowser.open("https://www.youtube.com/")

    def twitch_button():
        webbrowser.open("https://www.twitch.tv/")

    def netflix_button():
        webbrowser.open("https://www.netflix.com/ca/")

    def disneyplus_button():
        webbrowser.open("https://www.disneyplus.com/")

    def Primevideo_button():
        webbrowser.open("https://www.primevideo.com/")

    # Anime
    def funimation():
        webbrowser.open("https://www.funimation.com/")

    def crunchyroll():
        webbrowser.open("https://www.crunchyroll.com/")

    # ordering food
    def uber_eats():
        webbrowser.open("https://www.ubereats.com/ca")

    def skipthedishs():
        webbrowser.open("https://www.skipthedishes.com/")

    def foodora():
        webbrowser.open("https://www.foodora.com/")

    def door_dash():
        webbrowser.open("https://www.doordash.com/")

    # shopping
    def google_button():
        webbrowser.open("https://www.google.com/")

    def amazon_button():
        webbrowser.open("https://www.amazon.ca/")

    def bestbuy():
        webbrowser.open("https://www.bestbuy.ca/")

    def walmart():
        webbrowser.open("https://www.walmart.ca/")

    def apple():
        webbrowser.open("https://www.apple.com/")

    def microsoft():
        webbrowser.open("https://www.microsoft.com/")

    def footlocker():
        webbrowser.open("https://www.footlocker.ca/")

    def costco():
        webbrowser.open("https://www.costco.ca/")

    # productivity
    # tabs
    def td():
        webbrowser.open("https://www.td.com/")

    def sbank():
        webbrowser.open("https://www.scotiabank.com/")

    def linkedin():
        webbrowser.open("https://ca.linkedin.com/")

    def Gmail():
        webbrowser.open("https://mail.google.com/")

    def outlook():
        webbrowser.open("https://outlook.live.com/")

    def google_dssf():
        webbrowser.open("https://www.google.ca/docs/about/")

    def Overwatch():
        subprocess.call('E://Games//Overwatch//Overwatch Launcher.exe')

    def Black_ops_Cold_War():
        subprocess.call('E://Games//Call of Duty Black Ops Cold War//Black Ops Cold War Launcher.exe')

    def gtav():
        subprocess.call('E://Games//Launcher//Launcher.exe')

    def Warzone():
        subprocess.call('E://Call of Duty Modern Warfare//Modern Warfare Launcher.exe')

    def Fortnite():
        subprocess.call('E://Games//Fortnite//FortniteGame//Binaries//Win64//FortniteClient-Win64-Shipping.exe')

    def steam():
        subprocess.call('E://steam//steam.exe')

    def Epic():
        subprocess.call('E://Games//Epic Games//Launcher//Portal//Binaries//Win64//EpicGamesLauncher')

    def Battle():
        subprocess.call('C://Program Files (x86)//Battle.net//Battle.net.exe')

    def open_social_media():
        top = Toplevel()
        top.title('Grizzly Assistant')

        labelp = Label(top, image=photo)
        labelp.grid()
        bg = Button(top, command=google_button, width=127, text='Google', bg="black", fg="white")
        bg.grid()

        bi = Button(top, command=instagram, width=127, text="Instagram", bg="black", fg="white")
        bi.grid()

        bsc = Button(top, command=snapchat, width=127, text="Snapchat", bg="black", fg="white")
        bsc.grid()

        bfb = Button(top, command=facebook, width=127, text="Facebook", bg="black", fg="white")
        bfb.grid()

        btw = Button(top, command=twitter, width=127, text="Twitter", bg="black", fg="white")
        btw.grid()

        btk = Button(top, command=tiktok, width=127, text="Tiktok", bg="black", fg="white")
        btk.grid()

        bdc = Button(top, command=discord, width=127, text="Discord", bg="black", fg="white")
        bdc.grid()

    def open_entertainment():
        top2 = Toplevel()
        top2.title('Grizzly Assistant')

        label3 = Label(top2, image=photo)
        label3.grid()
        by = Button(top2, command=youtube_button, width=127, text="Youtube", bg="black", fg="white")
        by.grid()

        bt = Button(top2, command=twitch_button, width=127, text="Twitch", bg="black", fg="white")
        bt.grid()

        bn = Button(top2, command=netflix_button, width=127, text="Netflix", bg="black", fg="white")
        bn.grid()

        bd = Button(top2, command=disneyplus_button, width=127, text="Disney++", bg="black", fg="white")
        bd.grid()

        bp = Button(top2, command=Primevideo_button, width=127, text="Prime Video", bg="black", fg="white")
        bp.grid()

    def open_Anime():
        top2 = Toplevel()
        top2.title('Grizzly Assistant')

        label4 = Label(top2, image=photo)
        label4.grid()
        bfa = Button(top2, command=funimation, width=127, text="Funimation", bg="black", fg="white")
        bfa.grid()
        bcr = Button(top2, command=crunchyroll, width=127, text="Crunchyroll", bg="black", fg="white")
        bcr.grid()

    def open_ordering_food():
        top3 = Toplevel()
        top3.title('Grizzly Assistant')

        label5 = Label(top3, image=photo)
        label5.grid()

        bue = Button(top3, command=uber_eats, width=127, text="Uber eats", bg="black", fg="white")
        bue.grid()

        bfd = Button(top3, command=foodora, width=127, text="Foodora", bg="black", fg="white")
        bfd.grid()

        bsd = Button(top3, command=skipthedishs, width=127, text="skip the dishes", bg="black", fg="white")
        bsd.grid()

        bdd = Button(top3, command=door_dash, width=127, text="Door dash", bg="black", fg="white")
        bdd.grid()

    def open_shopping():
        top5 = Toplevel()
        top5.title('Grizzly Assistant')

        label6 = Label(top5, image=photo)
        label6.grid()
        baz = Button(top5, command=amazon_button, width=127, text="Amazon", bg="black", fg="white")
        baz.grid()
        bb = Button(top5, command=bestbuy, width=127, text="Best buy", bg="black", fg="white")
        bb.grid()
        bw = Button(top5, command=walmart, width=127, text=" Walmart ", bg="black", fg="white")
        bw.grid()
        bap = Button(top5, command=apple, width=127, text=" Apple ", bg="black", fg="white")
        bap.grid()
        bm = Button(top5, command=microsoft, width=127, text=" Microsoft", bg="black", fg="white")
        bm.grid()
        bfl = Button(top5, command=footlocker, width=127, text="Foot locker ", bg="black", fg="white")
        bfl.grid()
        bcc = Button(top5, command=costco, width=127, text="Costco", bg="black", fg="white")
        bcc.grid()

    def open_productivity_and_finance():
        top6 = Toplevel()
        top6.title('Grizzly Assistant')

        label7 = Label(top6, image=photo)
        label7.grid()
        btd = Button(top6, command=td, width=127, text="Td ", bg="black", fg="white")
        btd.grid()
        bsb = Button(top6, command=sbank, width=127, text="Scotiabank", bg="black", fg="white")
        bsb.grid()
        blink = Button(top6, command=linkedin, width=127, text=" linkedin", bg="black", fg="white")
        blink.grid()
        bgm = Button(top6, command=Gmail, width=127, text="Gmail", bg="black", fg="white")
        bgm.grid()
        bol = Button(top6, command=outlook, width=127, text="Outlook", bg="black", fg="white")
        bol.grid()
        bgds = Button(top6, command=google_dssf, width=127, text="Goggle docs,slides,forms,sheets", bg="black",
                      fg="white")
        bgds.grid()
        boa = Button(top6, width=127, text="Other application Coming soon!", bg="black", fg="white")
        boa.grid()

    def games():
        top7 = Toplevel()
        top7.title('Grizzly Assistant')

        label8 = Label(top7, image=photo)
        label8.grid()
        bga = Button(top7, text="Overwatch", command=Overwatch, width=127, bg="black", fg="white")
        bga.grid()

        bop = Button(top7, text="Black Ops Cold War", command=Black_ops_Cold_War, width=127, bg="black", fg="white")
        bop.grid()

        bop = Button(top7, text="Gtav", command=gtav, width=127, bg="black", fg="white")
        bop.grid()
        bop = Button(top7, text=" Warzone", command=Warzone, width=127, bg="black", fg="white")
        bop.grid()
        bop = Button(top7, text=" Fortnite", command=Fortnite, width=127, bg="black", fg="white")
        bop.grid()

        bop = Button(top7, text="Steam", command=steam, width=127, bg="black", fg="white")
        bop.grid()
        bep = Button(top7, text="Epic Games", command=Epic, width=127, bg="black", fg="white")
        bep.grid()
        bba = Button(top7, text="Battle Net", command=Battle, width=127, bg="black", fg="white")
        bba.grid()

    label = Label(image=photo)
    label.grid(column=0, row=0)
    PhotoImage(file='bs.png')
    b = Button(root, image=photo2, command=tab2, fg='white', bg='black',
               )
    b.grid(column=0, row=0)


tab1()

root.mainloop()
