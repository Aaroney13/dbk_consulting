# dbk_consulting
Code for consulting project with the DiamondBack Newspaper
Question: What words should be used to create headlines that get more views?

# Things to do:
1. Choose additional categories to analyze
2. Download graphs/excel files with higher performing articles
3. Test, is there a correlation between higher no. keywords and views/searches?
4. Test, chi square, keywords in category vs non-keywords in category
5. Test client given keywords
6. Test performance of individual sports and 'gamers'

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