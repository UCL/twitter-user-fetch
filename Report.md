# Report

The application is composed by 3 modules

## Twitterfetch
Downloads last tweets from the user timeline with a limit of 3,000. 
It calls the Twitter API using Python's urllib.
This is a two-step process, it is initiated by calling `"https://api.twitter.com/oauth2/token"`
to obtain the access_token that is required to call the endpoint that serves
the user timeline `https://api.twitter.com/1.1/statuses/user_timeline.json`. 
Authentication uses HTTP BASIC method.

### Fetch Tweets

> Using Python, you will have to implement a program that is able to fetch the last 3,000 tweets of 
a designated Twitter user with a public profile. 

### Twitter API

Twitter offers a series of endpoints that can be used to retrieve tweets from a particular user. 
The `GET` method `statuses/user_timeline` 

### Resource URL

https://api.twitter.com/1.1/statuses/user_timeline.json

### References 

https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline

## Stemming

> After fetching the tweets of the user, the program should be able to rank the most frequent word 
stems in these tweets and print the top-100 together with their frequency. Standard English stop 
words should be discarded from this analysis.
By word stem, we refer to the part of the word that is common to all its infected variants, e.g. 
the stem of the word "standardise" is "standard" (up to you which stemming method is going to be 
applied).
Note, that a frequency should not represent a simple count of the stems. Instead, we are requesting 
that a stem frequency represents the average count of a stem on a monthly basis, i.e. the timing 
of the tweets matters.

There are a number of stemming algorithms implemented in Python:
- Porter
- Porter2
- Paice-Husk
- Lovins

Porter/Porter2 is the most popular. Libraries such as NLTK and Stemming offer implementations.

### References

https://pypi.python.org/pypi/stemming/1.0
https://pythonprogramming.net/stemming-nltk-tutorial/


## Frequency

Pandas is used instead of R to calculate average monthly frequencies for the final report
