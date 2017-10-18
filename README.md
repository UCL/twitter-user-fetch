# Twitter User Fetch

## Requirements 

* python 3.x
* nltk==3.2.5
* numpy==1.13.3
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
 python3 -m unittest test/twitterfetch/test_authenticate.py
  
```

## Report

Basic architecture describing the components of the application in section [Report](Report.md)
