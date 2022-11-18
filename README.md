<img src="https://raw.githubusercontent.com/Aaroney13/dbk_consulting/main/dbk_logo.PNG">
Code repository for client project with the Diamondback newspaper 

Primary scope: How can we help the Diamondback make more successful articles

# Preliminary steps

Automated finding of most popular headlines for each time period (quarter):
- Automate_Regression.py
- downloaded graphs to Top_Headlines folder
- generated toplist.xlsx providing each categories' top headlines for each time period

Automated wordcloud generation to visually find appealing words for hypothesis testing
- word_cloud_generator.py
- output word clouds to word_clouds folder

# What we discovered:
- Many articles at the Diamondback are **hit or miss.**
- While most articles may recieve a couple views, a significant percentage **do not receive organic searches**
- This can be seen with the following bimodal distribution of log(Organic Searches)
<img src="https://raw.githubusercontent.com/Aaroney13/dbk_consulting/main/bimodal_distribution.png">

# How we plan to change this
- We categorized the articles as "hit" or "miss" depending on if they recieved more than 1 organic search within our timeframe.
- We then used a tensorflow LSTM layered model to predict with a given article title whether or not that article would end up as a hit or miss.
- Currently, our model has around an **80% accuracy** rate based on the test train split. This represents a significant change from a random choice of 50%.
