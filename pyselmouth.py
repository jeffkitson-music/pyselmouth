from appJar import gui
from PIL import Image, ImageTk
from pyseltongue import PlaintextToHexSecretSharer

def shard():
    # 192 seems to be the hard limit on number of characters for now.
    # Need to augment the standard primes list... 
    text = app.getTextArea("t1")
    print(text)
    app.clearTextArea("t1")
    shares = PlaintextToHexSecretSharer.split_secret(text, 2, 3)
    s = ""
    for share in shares:
        s += share + "\n" + "\n"
    app.setTextArea("t1",s)

def reform():
    text = app.getTextArea("t1")
    shards = text.split("\n")
    print(shards)
    cleanshards = [x for x in shards if x] #list comprehension ftw
    print(cleanshards)
    recovered = PlaintextToHexSecretSharer.recover_secret(cleanshards)
    app.clearTextArea("t1")
    app.setTextArea("t1",recovered)

def clear():
    app.clearTextArea("t1")
################################################################################################################
# GUI STARTS HERE
################################################################################################################

with gui("pyselmouth", "700x700", bg='#5d5d5d', font={'family':'Parseltongue','size':40}) as app:
    app.label("pyselmouth", bg='#1a472a', fg='white')
    photo = ImageTk.PhotoImage(Image.open("snake.png"))
    app.addImageData("pic", photo, fmt="PhotoImage")
    app.setPadding(15,15)
    app.addTextArea("t1")
    app.buttons(["Shard", "Reform","Clear", "Quit"], [shard, reform, clear, app.stop])
