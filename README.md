<img src="https://www.forumcinemas.lt/files/fclogo/naujas/FC_logo_3.png" alt="ForumCinemas logo" width="200" height="100">

# Forum Cinemas Webscraper
A simple Python 3 webscraper for forumcinemas.lt. Gets upcoming movie data (name, director, duration, genre, image link, etc.) and data in the news section (title, description and link of the news). The data is saved to data.db file, as well as JSON files in package/data.

Uses requests and BeautifulSoup packages. Features regular, as well as multithreaded/multiprocessed versions of webscraping (for better performance).

# Instructions
Install requests and BeautifulSoup packages via pip.
```
pip install requests bs4
```
Then, simply run the webscraper.py file.
```
python3 webscraper.py
```

You can run either the regular, multithreaded or multiprocessed versions (or all of them, to compare performance and operation times) by typing in "regular", "multithreaded", "multiprocessed" or "all" into the console respectively (without quotation marks).
