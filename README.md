# WhatsApp Chat Sentiment Analysis

This Python script performs sentiment analysis on a WhatsApp chat conversation exported as a text file. It extracts messages along with their date, time, and author, and then calculates the sentiment score (positive, negative, and neutral) for each message using the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool.

## Requirements
- Python 3
- pandas
- nltk (Natural Language Toolkit)
- wordcloud
- matplotlib
- emoji

## Installation
1. Install Python 3 from [python.org](https://www.python.org/downloads/).
2. Install required packages using pip:


Sure, here's a basic README file for your code:

markdown
Copy code
# WhatsApp Chat Sentiment Analysis

This Python script performs sentiment analysis on a WhatsApp chat conversation exported as a text file. It extracts messages along with their date, time, and author, and then calculates the sentiment score (positive, negative, and neutral) for each message using the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool.

## Requirements
- Python 3
- pandas
- nltk (Natural Language Toolkit)
- wordcloud
- matplotlib
- emoji

## Installation
1. Install Python 3 from [python.org](https://www.python.org/downloads/).
2. Install required packages using pip:
pip install pandas nltk wordcloud matplotlib emoji

arduino
Copy code
3. Download the VADER lexicon by running the following command in Python:
```python
import nltk
nltk.download('vader_lexicon')
Usage
Export your WhatsApp chat conversation as a text file.
Save the text file in the same directory as the Python script.
Update the conversation variable in the script with the filename of your chat text file.
Run the script. It will analyze the chat and display the predominant sentiment (positive, negative, or neutral).
Functionality
The script extracts date, time, author, and message content from the chat text file.
It performs sentiment analysis using VADER to determine the positivity, negativity, and neutrality of each message.
The sentiment scores are aggregated to calculate the overall sentiment of the chat.
The predominant sentiment (positive, negative, or neutral) is then printed.
File Structure
whatsapp_sentiment_analysis.py: The main Python script for performing sentiment analysis.
chat.txt: Sample WhatsApp chat text file for testing purposes.
