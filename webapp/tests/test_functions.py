import pytest
import pandas as pd
import sys
sys.path.append("..")
from main.app import sorting_tweet 

df = pd.read_csv('../dataset/tweets_clean.csv', index_col=0)

def test_sorting_tweet_isnt_none():
    assert (sorting_tweet("Hello", df) is not None)