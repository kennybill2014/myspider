#!/bin/bash

#echo "Init File Done."
index=0;
while true;
do
   cd ../news_spider
   echo "Start Crawl..."${index++}
   scrapy crawl toutiao
   echo "Crawl Data Done."
   cd ../tools
   python news2db.py
   python Init.py
done
#python preprocess.py
#cd ../web
#python main.py 1111
