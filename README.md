# dbk_consulting
![Diamondback Logo](/dbk_image.png?raw=true "Title" | width=100)
Code for consulting project with the DiamondBack Newspaper.  
Question: What words should be used to create headlines that get more views?

# Things to do:
1. Keywords to analyze based on wordclouds for each category
2. Test, is there a correlation between higher no. keywords and views/searches?
3. Test, chi square, keywords in category vs non-keywords in category
4. Test client given keywords
5. Visualize performance of individual sports and 'gamers'

# Steps Taken:

Cleaned data:
- filter_data.py cleaning steps
- returned merged_titles.xlsx final dataset

Automated finding of most popular headlines for each time period (quarter):
- Automate_Regression.py
- downloaded graphs to Top_Headlines folder
- generated toplist.xlsx providing each categories' top headlines for each time period

Automated wordcloud generation to visually find appealing words for hypothesis testing
- word_cloud_generator.py
- output word clouds to word_clouds folder

Test, is there a correlation between higher no. keywords and views:
- test_keyword_occurances.py - in progress
