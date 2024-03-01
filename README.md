# python-joke-api
A Python script accessing the JokeAPI. It works with `Python 2.7` and `Python 3.x` as well.

## Pre-Installation

You have to install following via pip. If you use `Python 2.7` you have to run

```
python -m pip install requests
```

If you use `Python 3.x` you have to run

```
python3 -m pip install requests
```

## Usage

You have to run:

```
python joke.py
```

As example you receive something like this:

```
{
    "error": false,
    "category": "Misc",
    "type": "single",
    "joke": "What does the MacBook have in common with Donald Trump?\n\nI would tell you....\nBut I don't compare apples to oranges.",
    "flags": {
        "nsfw": false,
        "religious": false,
        "political": true,
        "racist": false,
        "sexist": false,
        "explicit": false
    },
    "id": 233,
    "safe": false,
    "lang": "en"
}
```
