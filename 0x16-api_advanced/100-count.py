#!/usr/bin/python3
"""
parses the title of all hot articles, 
and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list):
