#!/usr/bin/env python3

from app.twitterfetch import user_timeline
from app.stemming import preprocess, wordstem
from app.frequency import calculate, datalist
import sys
sys.path.append('config')

twitter_handle = "uclnews"
horizontal_sep = "="*80


def main():
    """Main entry point for the application"""
    print()
    print("twitterUserFetch.py - Calculate the average monthly frequency of word stems using NLTK and Panda")
    print("Twitter handle: @uclnews")
    print()
    print("Author: David Guzman <d.guzman@ucl.ac.uk>")
    print()
    timeline_list = get_tweets_for_user(twitter_handle)
    timeline_datalist = datalist.DateAndStemDataList()
    for tweet in timeline_list:
        stems = get_word_stems(tweet['text'], 'porter')
        timeline_datalist.append_to_datalist(tweet['created_at'], stems)
    print()
    print('Average monthly frequency of word stems using Porter')
    print(horizontal_sep)
    print(get_avg_monthly_frequency(timeline_datalist.datalist)[:100].to_string(index=False))
    timeline_datalist.datalist.clear()
    for tweet in timeline_list:
        stems = get_word_stems(tweet['text'], 'snowball')
        timeline_datalist.append_to_datalist(tweet['created_at'], stems)
    print()
    print('Average monthly frequency of word stems using Snowball')
    print(horizontal_sep)
    print(get_avg_monthly_frequency(timeline_datalist.datalist)[:100].to_string(index=False))
    print()
    timeline_datalist.datalist.clear()


def get_tweets_for_user(user):
    """Return tweets for specified user"""
    timeline = user_timeline.UserTimeline()
    return timeline.get_tweets(user)


def get_word_stems(tweet_text, stemming_type):
    """Return the word stems from the tweet text"""
    preprocessor = preprocess.PreProcess()
    preprocess_list = preprocessor.remove_stopwords_and_punctuation(tweet_text)
    stemmer = wordstem.WordStem()
    if stemming_type == 'porter':
        return [stemmer.get_porter_stem(stem) for stem in preprocess_list]
    elif stemming_type == 'snowball':
        return [stemmer.get_snowball_stem(stem) for stem in preprocess_list]
    else:
        raise ValueError('stemming_type must be either "porter" or "snowball"')


def get_avg_monthly_frequency(datalist):
    """Return the average monthly frequency table from the list of stems and dates provided"""
    calculator = calculate.Calculate(datalist)
    return calculator.get_average_monthly_frequency_descending()


if __name__ == '__main__':
    sys.exit(main())
