#!/bin/sh
python ./SpiderTest.py | awk -F"</span>" '{print $6}' | awk -F"<span>" '{print $2}' >> Covid-19-Iran.txt
python Uniquizer.py
cat CovidFinal.txt

