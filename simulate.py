import csv, random, math, numpy
from multiprocessing import Pool

def load_data():
	# Load the CSV into memory in a data structure like this:
	# data["YYYYMMDD"] = [ (ticker, open_price, close_price), . . . ]
	data = { }
	for date, ticker, price_open, price_high, price_low, price_close, volume \
		in csv.reader(open("sp500hst.txt")):
		data.setdefault(date, []).append((ticker, float(price_open), float(price_close)))
	return data

def simulate_one(mode):
	global stock_days
	cash = 1.0
	for date, prices in stock_days.items(): # order doesn't matter
		if mode == "randomdaily":
			# choose randomly
			stock, open_price, close_price = random.choice(prices)
		elif mode == "bestdaily":
			# choose best pick of the day
			stock, open_price, close_price = max(prices, key = lambda x : x[2]/x[1])
		cash *= (close_price/open_price)
	return cash

def simulate_many(mode, n):
	with Pool() as pool:
		ret = list(pool.imap_unordered(simulate_one, [mode for dummy in range(n)], chunksize=50))
		print(mode)
		print(len(ret), "simulations")
		print(sum(ret)/len(ret), "average return")
		percentiles = [50] + [100-100*math.pow(10, -x) for x in range(1, round(math.log(n)/math.log(10))) ]
		for p, v in zip(percentiles, numpy.percentile(ret, percentiles)):
			print(str(p)+"th", v)
		print()

if __name__ == "__main__":
	stock_days = load_data()
	print(len(stock_days), "days")
	print(round(sum([len(x) for x in stock_days.values()]) / len(stock_days)), "avg choices per day")
	print()

	simulate_many("bestdaily", 1)
	simulate_many("randomdaily", 10000000)
