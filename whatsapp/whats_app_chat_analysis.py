import re
import pandas as pd
import numpy as np
import emoji
from collections import Counter
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

# Extract the Date time
def date_time(s):
    pattern = r'^(\d{1,2}/\d{1,2}/\d{2}), (\d{1,2}:\d{2})\s?(AM|PM|am|pm)? -'
    result = re.match(pattern, s)
    if result:
        return True
    return False

# Extract contacts
def find_contact(s):
    s = s.split(":")
    if len(s) == 2:
        return True
    else:
        return False

# Extract Message
def getMassage(line):
    splitline = line.split(' - ')
    datetime = splitline[0]
    date, time = datetime.split(', ')
    message = " ".join(splitline[1:])

    if find_contact(message):
        splitmessage = message.split(": ")
        author = splitmessage[0]
        message = splitmessage[1]
    else:
        author = None
    return date, time, author, message

data = []
conversation = '/content/chat.txt'

with open(conversation, encoding="utf-8") as fp:
    fp.readline()
    messageBuffer = []
    date, time, author = None, None, None
    while True:
        line = fp.readline()
        if not line:
            break
        line = line.strip()
        if date_time(line):
            if len(messageBuffer) > 0:
                data.append([date, time, author, ''.join(messageBuffer)])
            messageBuffer.clear()
            date, time, author, message = getMassage(line)
            messageBuffer.append(message)
        else:
            messageBuffer.append(line)

# Create DataFrame
df = pd.DataFrame(data, columns=["Date", "Time", "Contact", "Message"])
df['Date'] = pd.to_datetime(df['Date'])

# Drop rows with missing values
df = df.dropna()

# Initialize SentimentIntensityAnalyzer
sentiments = SentimentIntensityAnalyzer()

# Perform sentiment analysis
df["Positive"] = [sentiments.polarity_scores(i)["pos"] for i in df["Message"]]
df["Negative"] = [sentiments.polarity_scores(i)["neg"] for i in df["Message"]]
df["Neutral"] = [sentiments.polarity_scores(i)["neu"] for i in df["Message"]]

# Display the first few rows of the DataFrame
# Display the first few rows of the DataFrame without index numbers
print(df.head().to_string(index=False))
x = df["Positive"].sum()
y = df["Negative"].sum()
z = df["Neutral"].sum()

def score(a, b, c):
    if (a > b) and (a > c):
        print("Positive")
    if (b > a) and (b > c):
        print("Negative")
    if (c > a) and (c > b):
        print("Neutral")

score(x, y, z)

###########################################################
df.Contact.unique()

###########################################################

import regex

# Regular expression pattern to match emojis
emoji_pattern = regex.compile(r'\p{So}')

# Function to count emojis in a text
def count_emojis(text):
    return len(emoji_pattern.findall(text))

# Apply the function to count emojis in each message and create a new 'emoji_count' column
df['emoji_count'] = df['Message'].apply(count_emojis)

# Sum the 'emoji_count' column to get the total count of emojis
total_emojis = df['emoji_count'].sum()

# Print the first 50 rows of the DataFrame
print(df.head(50))

# Print the total count of emojis
print("Total number of emojis:", total_emojis)

###########################################################
text = " ".join(review for review in df.Message)
print ("There are {} words in all the messages.".format(len(text)))
stopwords = set(STOPWORDS)
# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
# Display the generated image:
# the matplotlib way:
plt.figure( figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()