# Overview

I really wanted to try and better understand the pandas package for python and thought that tinkering with a fun dataset would be helpful.  I wanted to try and better understand how modern recommendation systems are built and used, so I decided to work with a television show dataset.  I made a pretty rudimentary recommendation system based around genre and popularity of the shows in question.


I am using a data set from TMDb, The Movie Database.  Funnily enough, my dataset has only television shows saved.  It has a lot of data about each show, including popularity, rating, and genre. [Link To TMDb Dataset](https://www.kaggle.com/datasets/asaniczka/full-tmdb-tv-shows-dataset-2023-150k-shows)
{Describe your purpose for writing this software to analyze the data.}


[Software Demo Video](http://youtube.link.goes.here)

# Data Analysis Results

Question: How do recommendation systems work?
Answer: Through my project I have found that recommendation systems take in a large set of data about the shows that you have put the most time into.  They can then infer things you might like based on the data.  I was able to do a simple recommendation based solely on the genre selection the user's liked shows had and showing shows with similar genres and high ratings.

Question: Which shows have the highest rating and amount of voters?
Answer: Through searching through the dataset by a show's rating and feeding back information with the highest amount of voters I was able to see which shows were truly the highest rated.  It was interesting to see that the closer I got to a 10/10, the less I knew the shows. It seemed that a lot of popular media sat mostly in the 8-9/10.

# Development Environment

I used Visual Studio Code as well as some help in Jupyter Notebook to visualize the data I was searching through.

I programmed in Python using the pandas package in order to organize and filter the data.

# Useful Websites

* [Stack Overflow](https://stackoverflow.com/questions/26577516/how-to-test-if-a-string-contains-one-of-the-substrings-in-a-list-in-pandas)
* [Pandas Tutorial](https://www.youtube.com/watch?v=DkjCaAMBGWM&t=616s)

# Future Work

* I want to be able to graph some of my findings, which will take a bit more research.
* Some of the data that gets pulled in is formatted strangely, especially when I pull the Overview data from some shows.
* I want to compare genre to popularity, to visualize which genres lead to the highest spike in viewership.