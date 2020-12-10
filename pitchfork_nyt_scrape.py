import pandas as pd
from pynytimes import NYTAPI
import datetime
import requests
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import numpy as np 
from tqdm import tqdm

# new york times API key
key = 'y3avXAFe2K37IaP1Uw5dyteIrDnYGjlA'

def send_request(date):
    """Sends a request to the NYT Archive API for given date.
    There's a five second sleep before returning the response due to the 
    rate limit of 10 searches per minute.
    """
    base_url = 'https://api.nytimes.com/svc/archive/v1/'
    url = base_url + '/' + date[0] + '/' + date[1] + f'.json?api-key={key}'
    response = requests.get(url).json()
    time.sleep(5)
    return response

def is_valid(article, date):
    """Checks if article is within date range and has a headline."""
    is_in_range = (date > start) and (date < end)
    has_headline = (type(article['headline']) == dict) and ('main' in artricle['headline'].keys())
    return is_in_range and has_headline

def parse_response(response):
    '''Parses and returns response as pandas data frame.'''
    data = {'headline': [],  
            'date': [], 
            'doc_type': [],
            'material_type': [],
            'section': [],
            'keywords_value': [],
            'keyswords_rank' : [],
            'keywords_major': [],
            '_id': [],
            'web_url': [],
            'abstract': [], 
            'snippet': [], 
            'source': [],
            'news_desk': [], 
            'multimedia_rank' :[],
            'multimedia_subtype' :[], 
            'multimedia_credit' :[],
            'multimedia_caption' :[],
            'multimedia_cropname' :[], 
            'web_url':[]}
    
    articles = response['response']['docs'] 
    for article in articles: # For each article, make sure it falls within our date range
        date = dateutil.parser.parse(article['pub_date']).date()
        if not is_valid(article, date):
            continue 
        data['date'].append(date)
        data['headline'].append(article['headline']['main']) 
        data['section'].append(get_detail(article, 'section_name'))
        data['doc_type'].append(get_detail(article, 'document_type'))
        data['material_type'].append(get_detail(article, 'type_of_material'))
        data['keywords_value'].append(get_keywords(article, 'value'))
        data['keywords_rank'].append(get_keywords(article, 'rank'))
        data['keywords_major'].append(get_keywords(article, 'major'))
        data['web_url'].append(get_detail(article, 'web_url'))
        data['abstract'].append(get_detail(article, 'abstract'))
        data['snippet'].append(get_details(article, 'snippet'))
        data['source'].append(get_details(article, 'source'))
        data['news_desk'].append(get_detail(article, 'new_desk'))
        data['_id'].append(get_detail(article, '_id'))
        data['multimedia_rank'].append(get_multimedia(article, 'rank'))
        data['multimedia_subtype'].append(get_multimedia(article, 'subtype'))
        data['multimedia_caption'].append(get_multimedia(article, 'caption'))
        data['multimedia_cropname'].append(get_multimedia(article, 'cropname'))
        data['multimedia_credit'].append(get_multimedia(article, 'credit')) 
        data['web_url'].append(get_detail(article, 'web_url'))
        
    news_df = pd.DataFrame(data, columns=list(data.keys()))
    return df

def get_multimedia(article, keyword):
    if 'multimedia' not in article:
        return None
    return get_detail(article=article, detail=keyword, multimedia=True)

def get_keywords(article, keyword):
    return [keyword[keyword] for keyword in article['keywords'] if keyword['name'] == 'subject']
    
def get_detail(article, detail, multimedia=False):
    if not multimedia:
        if detail in article:
            return article[detail]
        return None
    if multimedia:
        if detail in article['mulitmedia']:
            return article['multimedia'][keyword]
        return None
    
    
def get_nyt(dates):
    """
    Accepts the range of dates that articles will be pulled from. Requests API and parses data to be put into DataFrame.
    """
    all_articles = pd.DataFrame()
    total = 0
    print('Date range: ' + str(dates[0]) + ' to ' + str(dates[-1]))
    print(p_statement)
    doc_name = f'all-articles-range-{dates[0]}-{dates[-1]}.csv'
    for date in dates:
        response = send_request(date)
        df = parse_response(response)
        total += len(df)
        all_articles = pd.concat([all_articles, df])
    print('Number of articles collected: ' + str(total))
    all_articles.to_csv(doc_name, index=False)
    print('Table saved as CSV')
    return all_articles


def get_artist(review):
    return review.find('ul', class_='artist-list review__title-artist')

def get_album(review):
    return review.find('h2', class_="review__title-album")

def get_date(review):
    return pd.to_datetime(review.find('time')['datetime'])

def get_link(review):
    link = review.find('a', href=True, class_="review__link")['href']
    return f'https://www.pitchfork.com{link}'

def get_author(review):
    return review.find('ul', class_="authors")

def get_genre(review):
    return review.find('li', class_="genre-list__item")

def get_page_reviews(soup):
    return soup.find_all('div', class_='review')

def get_coverart(review):
    return review.find('img', src=True)['src']
    
def get_webpage(url):
    response = requests.get(url)
    if response.status_code != 200:
        return False
    return bs(response.text, 'html.parser')

def get_author_title(review):
    return review.find('span', class_="authors-detail__title")

def get_review_abstract(review):
    return review.find('div', class_="review-detail__abstract")

def get_review(review):
    paragraphs = review.find('div', class_="review-detail__text clearfix").find_all('p')
    return ' '.join([paragraph.text for paragraph in paragraphs if not clean_review(paragraph)])

def clean_review(line):
    if line.text is None:
        return True
    if line.text == 'Buy: Rough Trade':
        return True
    if line.text == '(Pitchfork earns a commission from purchases made through affiliate links on our site.)':
        return True
    if line.text == 'Catch up every Saturday with 10 of our best-reviewed albums of the week. Sign up for the 10 to Hear newsletter here.':
        return True
    return False

def get_score(review):
    return review.find('span', class_="score")

def get_record_label(review):
    return review.find('ul', class_="labels-list single-album-tombstone__meta-labels")

def get_album_year(review):
    year = review.find('span', class_="single-album-tombstone__meta-year")
    
    
#    .text
#    return year.replace('•', '').strip()
    

def get_pitchfork_review(start_page=False, stop_page=False):
    redo = []
    new_pitchfork =  {'artist': [], 
                      'album': [], 
                      'score': [],
                      'genre':[], 
                      'date': [], 
                      'record_label': [], 
                      'year_release': [],
                      'author': [], 
                      'author_position': [], 
                      'review_abstract': [],
                      'review': [],  
                      'link': [], 
                      'coverart': []}
    for page in range(start_page, stop_page):
        stop = False
        url = f"https://www.pitchfork.com/reviews/albums/?page={page}"
        time.sleep(5)
        soup = get_webpage(url)
        time.sleep(5)
        if not soup:
            redo.append(page)
            print(f'{page} had issue')
            continue
        reviews = get_page_reviews(soup)
        for review in reviews:
            if stop:
                break
            link = get_link(review)
            date = get_date(review)
            new_pitchfork['artist'].append(get_artist(review))
            new_pitchfork['album'].append(get_album(review))
            new_pitchfork['genre'].append(get_genre(review))
            new_pitchfork['date'].append(date)
            new_pitchfork['author'].append(get_author(review))
            new_pitchfork['link'].append(link)
            new_pitchfork['coverart'].append(get_coverart(review))
            time.sleep(3)
            review_soup = get_webpage(link)
            time.sleep(2)
            if not review_soup:
                new_pitchfork['author_position'].append(None)
                new_pitchfork['review_abstract'].append(None)
                new_pitchfork['review'].append(None)
                new_pitchfork['year_release'].append(None)
                new_pitchfork['record_label'].append(None)
                new_pitchfork['score'].append(None)
                continue
            new_pitchfork['author_position'].append(get_author_title(review_soup))
            new_pitchfork['review_abstract'].append(get_review_abstract(review_soup))
            new_pitchfork['review'].append(get_review(review_soup))
            new_pitchfork['year_release'].append(get_album_year(review_soup))
            new_pitchfork['record_label'].append(get_record_label(review_soup))
            new_pitchfork['score'].append(get_score(review_soup))
            if date == '1999-01-05':
                stop = True
        if stop:
            break
    return pd.DataFrame(new_pitchfork), redo
    