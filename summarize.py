from gensim.summarization import keywords
from gensim.summarization.summarizer import summarize
import re
from newspaper import Article
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
# for scraping the webpage

# for removing square brackets

# Gensim summarizer

# For extracting the keywords

# downloads the article and parses the html, uses lxml parser


def downloadwebpage(url):
    # downloads the whole webpage
    article = Article(url)
    article.download()

    # parses the downloaded html
    article.parse()
    text = article.text
    return text


def sum_it_up(url):
    # url = 'https://en.wikipedia.org/wiki/Elon_Musk'

    content = downloadwebpage(url)

    # remove the reference numbers
    re.sub(r'\[.+\]', '', content)

    # finds a list of 10 important keywords, usses lemmetatization instead of stemming
    k = keywords(content, words=10, lemmatize=True).split('\n')
    kwords = ', '.join(k)

    # computes summary and reduces size by 20%
    return(summarize(content, 0.2), kwords)
