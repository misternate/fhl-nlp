import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

vader = SentimentIntensityAnalyzer()
sample = 'I hate the world' 

print(vader.polarity_scores(sample))