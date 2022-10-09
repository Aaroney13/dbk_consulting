import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# Goal:
# Generate word clouds to find interesting words in headline titles

os.chdir(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting\word_clouds")
xls = pd.ExcelFile(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting\Top_Headlines\toplist.xlsx")
categories = ['campus', 'diversions', 'news']
for category in categories:
    df1 = pd.read_excel(xls, category)
    df1['Page Title'] = df1['Page Title'].str.lower()
    word_cloud_string = ' '.join(df1['Page Title'])
    word_cloud_string =  word_cloud_string.replace('diamondback', '')

    wordcloud2 = WordCloud(background_color='white', width=1200, height=1000, collocations=False).generate(word_cloud_string)
    plt.imshow(wordcloud2)

    plt.savefig(category + '_word_cloud.png')
    plt.clf()