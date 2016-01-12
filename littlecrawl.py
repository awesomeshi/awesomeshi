import urllib.request
import re


class Crawl(object):
    def __init__(self):
        pass

    # get the whole HTML page of Douban Top250 moives by URL
    def getHtml(self, douban_url):
        data = urllib.request.urlopen(douban_url)
        return data.read().decode('utf-8')

    # get movies name by HTML
    def getMovie(self,douban_html):
        patt = '\<span class="title"\>(\w+)' # findall()
        compiled_patt = re.compile(patt)
        r = compiled_patt.findall(html)
        return r


if __name__ == '__main__':
    crawl = Crawl()
    html = crawl.getHtml('http://movie.douban.com/top250') #the 1st page
    # html = crawl.getHtml('http://movie.douban.com/top250?start=25&filter=') # the 2nd page
    # html = crawl.getHtml('http://movie.douban.com/top250?start=50&filter=') # the 3rd page
    movie = crawl.getMovie(html)
    print(movie)
    print(movie[9])
