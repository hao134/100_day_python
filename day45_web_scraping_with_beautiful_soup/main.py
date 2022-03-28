from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)

##### list all text's title
# title_name = soup.find_all(class_="titlelink")
# for text_title in title_name:
#     print(text_title.getText())

###### get the first text's title
first_title_name = soup.find(class_="titlelink")
print(first_title_name.getText())

article_link = first_title_name.get("href")
print(article_link)

first_title_score = soup.find(name="span",class_="score")
article_upvote = first_title_score.getText()
print(article_upvote)

###### get the all texts'
articles = soup.find_all(class_="titlelink")
article_texts= []
article_links=  []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

max_upovte_index = article_upvotes.index(max(article_upvotes))
max_upvote_text = article_texts[max_upovte_index]
print(max_upvote_text)





















####  teach document, uncomment it to see how it  work
# import lxml
#
# with open("website.html") as file:
#     text = file.read()
#
# soup = BeautifulSoup(text,"lxml")
# # print(soup.title)
# # print(soup.title.string)
# #print(soup.p)
# # print(soup.prettify())
#
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# # for tag in all_anchor_tags:
# #     print(tag.getText())
# #     print(tag.get("href"))
#
# # heading = soup.find(name="h1", id="name")
# # print(heading)
# #
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)
# #
# # company_url = soup.select_one(selector="p a")
# # print(company_url)
# #
# # name = soup.select_one(selector="#name")
# # print(name)
#
# headings = soup.select(".heading")
# print(headings)