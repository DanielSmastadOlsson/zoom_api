# An app to assign assistants with scheduling priviledge 
# API instructions from Zoom: https://marketplace.zoom.us/docs/api-reference/zoom-api/users/userassistantcreate
# "Assistants are the users to whom the current user has assigned . These assistants can schedule meeting on behalf of the current user..."

import http.client
import webbrowser
from tkinter import *


progtitle="Assistants in Zoom (V 202103102205)" # date and time to indicate version.

root=Tk()
root.title(progtitle)
a = Label(root, text="Add assistant in Zoom.")

# I use email, like: smastad@gmail.com
labelVem = Label(root, text="Who will scheduale?")
labelwho = Label(root, text="...on whos behalf of?")
labelpass = Label(root, text="JWT Token:")
eVem= Entry(root)
eWho= Entry(root)
ePass= Entry(root)

rader=0
a.grid(row=rader, column=0, columnspan=2)
rader=rader+1
labelVem.grid(row=rader, column=0)
eVem.grid(row=rader, column=1)
rader=rader+1
labelwho.grid(row=rader, column=0)
eWho.grid(row=rader, column=1)
rader=rader+1
labelpass.grid(row=rader, column=0)
ePass.grid(row=rader, column=1)
rader=rader+1

def klickarToken():
    # On this page, you will find the Token needed.
    webbrowser.open("https://marketplace.zoom.us/develop/apps/H21m5DTeM4jtnK6LZuuI/credentials")

def klickar():
    rader=5
    user=eVem.get()
    touser=eWho.get()
    password=ePass.get()
    conn = http.client.HTTPSConnection("api.zoom.us")

    
    payload = "{\"assistants\":[{\"email\":\"" + user + "\"}]}"

    headers = {
        'content-type': "application/json",
        'authorization': "Bearer" + password
    }

    conn.request("POST", "/v2/users/" + touser + "/assistants", payload, headers)

    res = conn.getresponse()
    data = res.read()

    #print(data.decode("utf-8"))
    meddelande = data.decode("utf-8")
    labelMeddelande = Label(root, text=meddelande)
    labelMeddelande.grid(row=rader, column=0, columnspan=3)





buttonVerkstall = Button(root, text="Do this now", command=klickar)
buttonHitta = Button(root, text="Find the token", command=klickarToken)
buttonVerkstall.grid(row=rader, column=1)
buttonHitta.grid(row=rader, column=0)
rader=rader+1
root.mainloop()


