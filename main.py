from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     contents = file.read()
          
# soup = BeautifulSoup(contents, "html.parser")
# all_lists = soup.find_all("li")

# for lists in all_lists:
#     #print(lists.getText())
#     pass

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

## TO FIND THE FIRST OCCURANCE USE THE CODE BELOW ##
# article_tag = soup.find(class_="titleline")
# print(article_tag)
# article_text = article_tag.get_text()
# print(article_text)
# article_link = article_tag.find("a", href=True)[0]['href']
# article_link = article_tag.get("href")
# print(article_link)
# article_upvote = soup.find(class_="score").get_text()
# print(article_upvote)

## TO FIND ALL THE ARTICLES USE THE CODE BELOW ##

articles = soup.find_all(class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.findAll("a", href=True)[0]['href']
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
print(largest_number)

# print(article_texts)
# print(article_links)
# print(article_upvotes)

