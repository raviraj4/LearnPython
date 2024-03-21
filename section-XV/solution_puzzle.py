# my solution to the puzzle
# 1 TASK: Import any libraries you think you'll need to scrape a website.
import bs4
import requests

# 2 Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HMTL text from the homepage.
request = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(request.text, 'lxml')

# 3 TASK: Get the names of all the authors on the first page.
all_auth = []
for auth in soup.select(".author"):all_auth.append(auth.contents)
# print(all_auth)


# 4 TASK: Create a list of all the quotes on the first page.
listof_quotes = []
for text in soup.select(".text"):listof_quotes.append(text.contents) 
# print(listof_quotes)

# 5 TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...).

list_of_ten_tags = []
for tags in soup.select(".tag-item>.tag"):list_of_ten_tags.append(tags.contents)
# for i in range(len(list_of_ten_tags)):
    # print("".join(list_of_ten_tags[i]))

# 6 TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website. Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check that your loop is on the last page with quotes. For debugging purposes, I will let you know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough that it wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!
url_base = "http://quotes.toscrape.com/page/{}/"
# print(url_base.format(3))
subreq = request.get(url_base.format())
subsoup = bs4.BeautifulSoup(subreq.text)