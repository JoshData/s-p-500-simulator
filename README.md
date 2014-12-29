S&P 500 Investor Simulator
==========================

Question
--------

An [article in Quartz](http://qz.com/317958/how-you-could-have-turned-1000-into-billions-of-dollars-by-perfectly-trading-the-sp-500-in-2014/) by [David Yanofsky](http://qz.com/author/davidyanofskyquartz/) (December 26, 2014) observed that the lucky trader to have bought and sold the best S&P 500 stock each day in 2014 would have turned $1 K into $179 B.

The likelihood of doing that by chance, 500 to the 248th power, is astronomical. It's also not possible. Yanofsky notes that by the middle of the year you would have earned so much that each (re)investment would alter the market itself, making the result completely counterfactual.

I wondered how lucky the luckiest plausible person would get.

Methods
-------

To find out, I ran 10,000,000 simulations where an investor starts with the same $1 K and invests in a random S&P 500 stock at market opening, sells it at closing, and repeats this every day for a year. The simulation took about 10 minutes.

I used one year of [2009-2010 historical data from pages.swcp.com/stocks](http://pages.swcp.com/stocks) because it was readily availalbe. I have no idea if the data is accurate, but I assume it's good enough. It runs from Aug 21, 2009 -Aug 20, 2010. Obviously the market was different then than in 2014, but the comparison is good enough to get an idea. There were 245 trading days in that time period and, as expected, an average of 500 possible stock picks each day (hence the name S&P 500).

Results
-------

To compare with Yanofsky's analysis, choosing the best stock each day during my time period results in an ending cash balance of $22.7 B. So 2009-2010 was less profitable for this lucky guy but it is in the same ballpark as 2014.

The average trader comes out just above even (the mean return was 3.3%, the median 0.7%).

The top 10% of traders come out ahead with 34% gains. The top 1% come out with 70% gains.

The top 0.1% of investors doubles their money (200% gains).

The top 0.0001% of investors --- or one in a million --- triples their money (300% gains).

So say there are about a million people investing in the S&P 500, we'd expect just one to triple their money.

