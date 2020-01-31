# Processing
import numpy as np
import pandas as pd

#scraping
from newsapi import NewsApiClient


# Init
newsapi = NewsApiClient(api_key='596dcf2e27f84163872da82a6cbf4bd2')


#get all information

#iterates through the code 500 times
for x in range(499):
    #takes headline, sources, start and end date, language, and how to sort the articles and grabs such articles
    top_headlines = newsapi.get_everything(
                                            q = 'Trump',
                                            sources = 'abs-news, bbc-news, cbs-news, cnbc, fox-news, google-news, msnbc, nbc-news,new-york-magazine, politico, the-american-conservative, the-hill, the-huffington-post, the-wall-street-journal, the-washington-post, the-washington-times, time, usa-today',
                                            from_param='2019-12-31',
                                            to='2020-01-31',
                                            language='en',
                                            sort_by='relevancy',
                                            page = x + 1)
    print('Writing to CSV page number ', x)
    df = pd.DataFrame(top_headlines)
    #new file if it is the first one of the loop
    if x == 0:
        df.to_csv(r'newsapiScrapedData.csv')
    else:
        df.to_csv(r'newsapiScrapedData.csv', mode='a', header = False)
