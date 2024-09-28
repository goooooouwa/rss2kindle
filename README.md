# Read your favourite blog on your Kindle

blog2kindle is a little Python script that can turn RSS feeds into ebooks which can be read on ebook readers, such as Kindle, Apple Books.

It's based on code from [news2kindle](https://github.com/goooooouwa/news2kindle) which will read a list of blog RSS feeds, package them as a MOBI file, and then send it to your kindle via kindle mail address and Amazon's whispersync. 

See examples of feeds.txt & mp3-urls.txt generated by blog2kindle [here](https://github.com/goooooouwa/crawling-results).

## How to use

### 1. Load env

`export $(cat .env | xargs)`

### 2. Generate ebook from blog RSS feed in feeds.txt

```
# RSS feed is in config/feeds.txt
python3 ./src/news2kindle.py "blog title"
```

If the blog RSS feed is split into multiple feeds, you can run:

```
for i in {0..4}
do
echo "https://raw.githubusercontent.com/goooooouwa/out/master/out/slice-$i.xml" > config/slice-$i.txt
python3 src/news2kindle.py "blog title" $i
done
```
