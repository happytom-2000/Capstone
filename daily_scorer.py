import csv
import pandas as pd

def load_file(filename):
	'''
	loads the file with all the tagged tweets.
	'''

	f = open(filename, 'rb')
	df = pd.read_csv(f)
	print(df.head(3))
	print(df.tail(3))
	return df

def score_catcher(df):
	'''
	finds out the net positively and negatively tagged tweets for each day.
	'''
	data = []
	dates = []
	record = {}
	for item in df:
		if not len(dates):
			dates.append(str(item.Date))
			pos = 0
			neg = 0
		elif len(dates) and item.Date not in dates:
			dates.append(str(item))
			# TODO: call func to calculate net sentiment for the day
			record = {"Date": dates[len(dates)-1], "sentiment": sentiment}
			data.append(record) 
			pos = 0
			neg = 0
		
		if item.Date in dates:
			if int(item.sentiment) == 1:
				pos += 1
			elif int(item.sentiment) == 0:
				neg += 1
	return data


def make_file(data):
	'''
	make a csv file for the processed data.
	'''
	final_df = pd.DataFrame(data)
	pd.to_csv("./daily_twitter_sentiment.csv", columns=('Date', 'Sentiment'))
	return

def main():
	'''
	the binder of all functions in a meaningful sequence.
	'''
	df = load_file('./TaggedData.csv')
	data = score_catcher(df)
	make_file(data)
	return

if __name__ == '__main__':

	main()


