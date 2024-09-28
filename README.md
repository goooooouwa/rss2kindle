# Read your favourite blog on your Kindle

blog2kindle is a little Python script that can turn RSS feeds of your favourite websites (e.g. blogs, news articles) into ebooks which can be read on ebook readers, such as Kindle, Apple Books.

It's based on code from [news2kindle](https://github.com/goooooouwa/news2kindle) which reads a list of RSS feeds, package them as a MOBI file, and then send it to your kindle via kindle mail address and Amazon's whispersync. 

## Demo: ebook for blog [Coding Horror](https://blog.codinghorror.com/)

![Screen Shot 2021-11-25 at 6 49 02 PM](https://user-images.githubusercontent.com/1495607/143427994-5eea1a37-2b73-4c71-9858-eed10ea09abd.png)

![Screen Shot 2021-11-25 at 6 48 48 PM](https://user-images.githubusercontent.com/1495607/143427976-0fa33f81-93e6-4271-8562-53cce35bd1e1.png)

## Usage

### 1. Load env

`export $(cat .env | xargs)`

### 2. Generate ebook from blog RSS feed in feeds.txt

```
# RSS feed is in config/feeds.txt
python3 ./src/news2kindle.py "blog title"  # which reads a list of blog RSS feeds, package them as a MOBI file, and then send it to your kindle via kindle mail address and Amazon's whispersync.
```

To combine multiple RSS feeds into one ebook, you can run:

```
for i in {0..4}
do
echo "https://raw.githubusercontent.com/goooooouwa/out/master/out/slice-$i.xml" > config/slice-$i.txt
python3 ./src/news2kindle.py "blog title" $i
done
```

## How do I get RSS feeds for my favourite websites if it doesn't provide one?

You can use [blog_downloader](https://github.com/goooooouwa/blog_downloader) to crawl any website and generate RSS feeds from them. See how it works [here](https://github.com/goooooouwa/blog_downloader/blob/master/README.md). 
