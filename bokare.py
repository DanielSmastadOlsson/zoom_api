#Ett program för att lägga till bokare ("assistents") i Zoom.
import http.client
import webbrowser
from tkinter import *
progtitle="Bokare i Zoom (V 202103101550)"
print(progtitle , "startar. / dos@du.se")
root=Tk()
root.title(progtitle)
a = Label(root, text="Lägg till assistent/bokare i Zoom.")

labelVem = Label(root, text="Vem ska schemalägga?")
labelwho = Label(root, text="...åt vem?")
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
    webbrowser.open("https://marketplace.zoom.us/develop/apps/H21m5DTeM4jtnK6LZuuI/credentials")

def klickar():
    rader=5
    user=eVem.get()
    touser=eWho.get()
    password=ePass.get()
    conn = http.client.HTTPSConnection("api.zoom.us")

    # user=input("Vem ska schemalägga? (användarnamn): ")
    # touser=input("Åt vem? (användarnamn): ")
    paytemp = "{\"assistants\":[{\"email\":\"" + user + "@du.se\"}]}"
    payload = paytemp

    # password="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6ImlwM1RCRU5RUTVtZHF2ekNtdklwcnciLCJleHAiOjE2MTUzODEwMDcsImlhdCI6MTYxNTM3NTYwOH0.9WEq2gW_qOozGIQezBa-3xUYXtlrrAvr0SVeJmV-d14"
    # print("https://marketplace.zoom.us/develop/apps/H21m5DTeM4jtnK6LZuuI/credentials")
    # password=input("JWT Token: ")
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer" + password
    }

    conn.request("POST", "/v2/users/" + touser + "@du.se/assistants", payload, headers)

    res = conn.getresponse()
    data = res.read()

    #print(data.decode("utf-8"))
    meddelande = data.decode("utf-8")
    labelMeddelande = Label(root, text=meddelande)
    labelMeddelande.grid(row=rader, column=0, columnspan=3)





buttonVerkstall = Button(root, text="Verkställ", command=klickar)
buttonHitta = Button(root, text="Hitta token", command=klickarToken)
buttonVerkstall.grid(row=rader, column=1)
buttonHitta.grid(row=rader, column=0)
rader=rader+1
root.mainloop()


