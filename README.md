# Twitter User Fetch

Author
: David Guzman <d.guzman@ucl.ac.uk>

Python 3.x application for downloading a list of 3,000 tweets from a specified Twitter handle and calculating the 
average monthly frequency of the word stems present in the tweet text. The stemming process is done with NLTK.

## Requirements 

* python 3.x
* nltk==3.2.5
* pandas==0.20.3

Install with 

```
pip install -r requirements.txt
```

## Credentials

Access to Twitter API requires two credentials

* consumer_key
* consumer_secret

These are configured in `config/twitter.py`. Valid credentials are provided by email.

## Tests

Python's unittest has been used in all tests.

```
 python3 -m unittest discover test  
```

## Run

Run the application with the command

```
 python3 twitterUserFetch.py  
```

## Report

Basic architecture describing the components of the application in section [Report](Report.md)
