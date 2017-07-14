from urllib import request

goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1497390033&period2=1499982033&interval=1d&events=history&crumb=GD0Y0HOG1n8'
def downloader(csv_url):
    response = request.urlopen(csv_url)
    csv_str = str(response.read())
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line+"\n")
    fx.close()


downloader(goog_url)
