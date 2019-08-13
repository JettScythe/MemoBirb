# MemoBirb
A memo.cash --> twitter.com post bridge

## REQUIREMENTS:
Python (3.7 recommended) (Download here: https://www.python.org/downloads/)
<br>
pip, though that should be included in python (Download here: https://pip.pypa.io/en/stable/installing/)

## USAGE: 
Clone / download this repo
```
git clone https://github.com/JettScythe/MemoBirb.git
```
### INPUT USER INFO:
To do this you will need to create a dev app w/ twitter (https://developer.twitter.com/en/apps/create) - keep in mind the bot will only post statuses. Apply only the needed permissions. 
<br>
Once the app is created, navigate to the app --> Keys & Tokens. 
There you will find an "API Key", "API Secret Key", "Access Token" & "Access Token Secret".

Now go to "credentials.py" in your favourite code editor. There you will find the following:
```
ACCESS_TOKEN='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_SECRET='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
CONSUMER_KEY='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
CONSUMER_SECRET='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```
Replace 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' for each value with the values twitter gave you

<br>

Now go to memobirb.py in your favourite code editor - on line 33 you will find query_bitsocket: 
```
query_bitsocket({
  "v": 3,
  "q": {
    "db": ["u"],
    "find": {
      "in.e.a": "qxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "out.h1": "6d02"
    }
  },
  "r": {
    "f": ".[] | .out[] | select(.b0.op? == 106) | .s2"
  }             
}, bitsocket_handler)
```
Replace ""qxxxxxxxxxxxxxxxxxxxxxxxxxxx"" on line 38 with your memo.cash cashaddr WITHOUT the 'bitcoincash:' prefix. 
<br>
save all changes

### DEPLOY
In your terminal:
<br>

Create a Python environment

Move to memobirb folder in terminal and run:
```
python3 -m venv memobirb
```
```
source memobirb/bin/activate
```
Make sure pip is up-to-date:
```
pip install --upgrade pip
```
Make sure requirements are met:
```
pip install -r requirements.txt
```
```
pip install twitter
```

### LAST STEP:
deploy with
```
python memobirb.py
```
<br>
<br>
Special thanks to the guys in https://t.me/fountainheadcash // https://bitdb.bch.sx/
