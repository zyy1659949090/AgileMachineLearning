Main Repo for Agile Machine Learning class.


## Installation

 1. Clone this repo
 1. Optional: set up virtualenv to house this project
 1. Run `python tests.py` and install things including all the following:
 1. Get copy of CrossValidated database
 1. Create stats database, and import CrossValidated dump
 1. `pip install -r requirements.txt`


## The Data


[StackExchange](www.stackexchange.com) is a network of crowd-curated q/a sites.
with plenty of years behind them.  That network includes everything from the very-well-known StackOverflow to a continuously updated pile of specialty sites for specific skill niches.
 
As a programmer, they have been the single biggest asset for finding expert-written solutions to problems I faced as I faced them.  What's more exciting is that they release all their data openly.  It's available through [an online database interface](http://data.stackexchange.com/), as a [large dump in a torrent](http://data.stackexchange.com/help) (click "Download Data Dumps" for most current version), or through [an api](https://api.stackexchange.com/).

We're going to be using data from the site from their [CrossValidated](http://stats.stackexchange.com/) site, known in the data at `stats`.  It's one of the more established not-StackOverflow sites, and also has pretty on-topic questions/answers for this class.  :)


## TDD
For the sake of adventure, we're going to try out Test Driven Development in our machine learning word.  This will mean some combination of random data generation and finding a small set of data we know really well.  You'll find a few tests within the `tests` folder.  To run all tests, call `python test.py` from this project's root folder.  Note that, as you add new files to the `tests` directory, you'll have to import them into that same in-root `test.py`.

