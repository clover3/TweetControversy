import datetime as dt
import os
from odd_scorer import OddScore
scorer = OddScore()

def read_text(month,date,keyword):
  year = 2018
  date_str ="%04d-%02d-%02d" % (year,month,date)
  out_path = "C:\work\Data\cont_company_tweets\\text\\{}_{}".format(keyword,date_str)
  docs = open(out_path, "r", encoding="utf-8").readlines()
  return docs


def get_cont(keyword):
    year = 2018
    x = []
    y = []
    for month in range(1, 7):
        for date in range(1, 32):
            try:
                date_str = "%04d-%02d-%02d" % (year, month, date)
                new_x = dt.datetime.strptime(date_str, '%Y-%m-%d').date()

            except ValueError:
                continue
            docs = read_text(month, date, keyword)
            scores = list([scorer.predict(doc) for doc in docs])
            num_tweets = len(scores)
            avg_scores = sum(scores) / num_tweets

            x.append(new_x)
            y.append(avg_scores)
    return x,y