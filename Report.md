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

The application is configured to retrieve the tweets from the Twitter handle uclnews

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

There are a number of stemming algorithms implemented in Python, being Porter and Snowball two general-purpose options
that are commonly used. Libraries such as NLTK and Stemming offer implementations for these algorithms.

In order to transform each word by stemming, the text of the tweet is tokenised using TweetTokenizer from NLTK, 
filtering out the tweet handles. This list of tokens is then filtered to exclude words matching the items in the set of 
English stop words available in NLTK Corpus.

`tweet_text -> twitter_tokenizer -> stop_words_filter -> stemming`  

The application uses both Porter and Snowball stemming.

https://pythonprogramming.net/stemming-nltk-tutorial/

## Frequency

Pandas is used instead of R to calculate average monthly frequencies for the final report

https://pandas.pydata.org/pandas-docs/stable/api.html

## twitterUserFetch

The #main() method executes the following tasks:

- Retrieves a filtered representation of the JSON obtained from the Twitter API endpoint, including only the 
`created_at` timestamp field and the `text` field containing the actual tweet. 

```
timeline_list = get_tweets_for_user(twitter_handle)
```

This timeline list has the following format:

```
[{'text': "Text content of the Tweet", 'created_at': 'Thu Oct 19 11:53:24 +0000 2017'}]
```

* Create a `DateAndStemDataList()` object to be used as a data frame for the calculation of frequencies

* Each `text` field is tokenised, filtered (for stop words and punctuation characters) and stemmed. The result is stored
together with the timestamp in the `DateAndStemDataList()` object.

* The populated `DateAndStemDataList()` object is passed to the `Calculate()` object. The constructor parses and 
converts the string `created_at` to a Python datetime

```
date_format = "%a %b %d %H:%M:%S %z %Y"
self.df['timestamp'] = self.df['date_created'].apply(lambda x: datetime.strptime(x, self.date_format))
```

* `Calculate()` uses Pandas data frames to perform the following calculations:

    * extracts year and month from the datetime calculated in the previous step
    
    * groups the rows by year, month and stem to calculate frequencies per stem (`count()`)
    
    * calculates the average (`mean()`) from the previous step
    
    * sorts the results in descending order of average frequency
    
* Finally the application trims the results to the first 100 rows    
    

## Known Issues

* Porter and Snowball algorithms assume words are in American spelling

## Example 

```
(python3) david@infimm:~/Documents/PycharmProjects/twitter-user-fetch$ python3 twitterUserFetch.py 
[nltk_data] Downloading package stopwords to /home/david/nltk_data...
[nltk_data]   Package stopwords is already up-to-date!

twitterUserFetch.py - Calculate the average monthly frequency of word stems using NLTK and Panda
Twitter handle: @uclnews

Author: David Guzman <d.guzman@ucl.ac.uk>


Average monthly frequency of word stems using Porter
================================================================================
stem  stem_freq
            rt       28.0
         studi       18.0
         world       17.0
           ucl       16.0
       univers       15.0
       student       13.0
            pm       12.0
            dr       12.0
          find       12.0
            uk       12.0
          meet       10.0
           abe        9.0
         peopl        9.0
          help        9.0
           top        9.0
      research        9.0
        reveal        9.0
           new        8.5
          prof        8.0
           fee        8.0
         today        8.0
          educ        8.0
     professor        7.0
          mean        7.0
          head        7.0
         human        7.0
          rank        7.0
           1st        7.0
        launch        7.0
           see        7.0
           say        6.0
           get        6.0
       discuss        6.0
         women        6.0
      bentham'        6.0
     scientist        6.0
     congratul        6.0
         could        6.0
         among        6.0
         great        6.0
       exhibit        6.0
        academ        5.0
           one        5.0
           led        5.0
          time        5.0
             3        5.0
        scienc        5.0
            us        5.0
        jeremi        5.0
           law        5.0
          http        5.0
       england        5.0
           may        5.0
       podcast        5.0
        social        5.0
 #ordinaryanim        5.0
          work        5.0
          tabl        5.0
          talk        4.5
        public        4.0
           use        4.0
        featur        4.0
 https://t.co…        4.0
       explain        4.0
        confer        4.0
       british        4.0
         repay        4.0
       medicin        4.0
          anim        4.0
          come        4.0
      influenc        4.0
        review        4.0
         engin        4.0
#brexitassembl        4.0
         audit        4.0
         thank        4.0
          race        4.0
        shinzo        4.0
         pupil        4.0
      dementia        4.0
        dispar        4.0
      #univers        4.0
         white        4.0
          show        4.0
       provost        3.5
          link        3.0
         onlin        3.0
        comput        3.0
        london        3.0
       announc        3.0
          ucl'        3.0
     transport        3.0
        cheryl        3.0
       comment        3.0
        member        3.0
          star        3.0
         black        3.0
          best        3.0
          test        3.0
      strength        3.0

Average monthly frequency of word stems using Snowball
================================================================================
stem  stem_freq
            rt       28.0
           ucl       19.0
         studi       18.0
         world       18.0
       univers       15.0
            pm       13.0
            uk       13.0
       student       13.0
          find       12.0
            dr       12.0
          meet       10.0
      research        9.0
           abe        9.0
          help        9.0
           top        9.0
        reveal        9.0
         peopl        9.0
           new        8.5
           fee        8.0
          prof        8.0
          educ        8.0
         today        8.0
       bentham        8.0
           see        7.0
          rank        7.0
          mean        7.0
           1st        7.0
     professor        7.0
          head        7.0
        launch        7.0
         human        7.0
           may        6.0
         among        6.0
     congratul        6.0
         women        6.0
         could        6.0
         great        6.0
       exhibit        6.0
       discuss        6.0
           get        6.0
     scientist        6.0
           say        6.0
            us        5.0
        academ        5.0
           law        5.0
       england        5.0
        scienc        5.0
           one        5.0
           led        5.0
        jeremi        5.0
          time        5.0
           bbc        5.0
          tabl        5.0
        social        5.0
       podcast        5.0
             3        5.0
          work        5.0
 #ordinaryanim        5.0
          talk        4.5
#brexitassembl        4.0
          anim        4.0
       medicin        4.0
        shinzo        4.0
         engin        4.0
        featur        4.0
        confer        4.0
         audit        4.0
           use        4.0
        review        4.0
       explain        4.0
      #univers        4.0
 https://t.co…        4.0
         thank        4.0
      influenc        4.0
         white        4.0
          show        4.0
          come        4.0
        public        4.0
        dispar        4.0
          race        4.0
         pupil        4.0
      tomorrow        4.0
      dementia        4.0
         repay        4.0
       british        4.0
       provost        3.5
      collabor        3.0
     contribut        3.0
       anxieti        3.0
          link        3.0
         decad        3.0
         boost        3.0
           dog        3.0
        london        3.0
        museum        3.0
        design        3.0
         don't        3.0
           win        3.0
         black        3.0
         onlin        3.0

```
