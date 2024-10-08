# Read your favourite blogs on your Kindle

blog2kindle is a little Python script that can turn RSS feeds of your favourite websites (e.g. blogs, news articles) into ebooks which can be read on ebook readers, such as Kindle, Apple Books.

It's based on code from [news2kindle](https://github.com/goooooouwa/news2kindle) which reads a list of RSS feeds, package them as a MOBI file, and then send it to your kindle via kindle mail address and Amazon's whispersync.

## Demo: ebook for blog [Coding Horror](https://blog.codinghorror.com/)

![Screen Shot 2021-11-25 at 6 49 02 PM](https://user-images.githubusercontent.com/1495607/143427994-5eea1a37-2b73-4c71-9858-eed10ea09abd.png)

![Screen Shot 2021-11-25 at 6 48 48 PM](https://user-images.githubusercontent.com/1495607/143427976-0fa33f81-93e6-4271-8562-53cce35bd1e1.png)

## Prerequsites:

1. Python 3.8.20 (recommend install with [pyenv](https://github.com/pyenv/pyenv))
2. ~~Calibre which provides 'ebook-convert' command (no longer necessary as Amazon now accpets sending ePub instead of Mobi files)~~

## Usage

`python3 ./src/news2kindle.py [blog title] [slice number]`

## RSS feeds preparation

### 1. Generate RSS feeds and publish as public URLs

You can use [blog_crawler](https://github.com/goooooouwa/blog_crawler) to crawl any website and generate RSS feeds from them. See how it works [here](https://github.com/goooooouwa/blog_crawler/blob/master/README.md).

### 2. Publish the generated RSS feeds online (as news2kindle reads content of RSS feeds from a list of URLs)

For example, you can publish the RSS feed to a Github repo (like [this one](https://github.com/goooooouwa/rss-feeds/tree/master/codinghorror)):

```bash
git add ./out  # folder with RSS feeds slice-[0-9].xml
git commit -m "publish blog feeds"
git push origin master   # publish the RSS file somewhere online to get a public URL
```

### 3. Save public URLs of RSS feeds into `config` folder as `slice-[0-9].txt` for new2kindle to read

**Not to be confused of slice-[0-9].xml, which are actual files with RSS feeds content, where as slice-[0-9].txt consists of only links to slices-[0-9].xml files**. slice-[0-9].txt is equivalent to feeds.txt, output of blog_crawler's "render" command, like this [feeds.txt](https://github.com/goooooouwa/rss-feeds/tree/master/codinghorror).

See examples of slice-[0-9].txt files [here](https://github.com/goooooouwa/blog2kindle/blob/master/config).

## Run

### 4. Setup environment variables from `.env` file

`export $(cat .env | xargs)`

### 5. Generate ebook from RSS feed and send it to Kindle

```
python3 ./src/news2kindle.py "blog title" 0 # which fetches the content of each RSS feeds linked in config/slice-0.txt, package them as a MOBI file, and then send it to your kindle via kindle mail address and Amazon's whispersync.
```

To generate multiple books in batch, you can run:

```
for i in {0..9}
do
echo "https://raw.githubusercontent.com/goooooouwa/rss-feeds/master/codinghorror/slice-$i.xml" > config/slice-$i.txt
python3 ./src/news2kindle.py "blog title" $i
done
```

Now you will have your favourite blog sent to your Kindle, waiting for you to pick up.
