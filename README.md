# Tweeffinity

Final project - Ironhack Data Analytics Bootcamp. 

#### Tweeffinity is a program that discovers the affinity between two twitter users. 

## Process

I have obtained all the tweets from each user with Tweepy, a Python library for the Twitter API. After cleaning the database I have used natural language processing to determine the main words and vectorized each tweet to perform machine learning techniques. HDBSCAN has been the cluster model selected because it determines for itself the most suitable cluster number.

Finally, the program returns an affinity percentage based on shared content.

## Folders

#### - Requirements.txt

This file contains all the dependencies to run the program

### - src

It contains all the files to run the program. It is only necessary to run the main.py file in the terminal by entering two twitter users. Here, there is an example: 

<img width="260" alt="Captura de pantalla 2019-08-13 a las 15 21 36" src="https://user-images.githubusercontent.com/49640612/63044921-8d524e80-becf-11e9-9568-a3dd5d196648.png">

### - input

It contains 2 csv files with all tweets from both users.

### - output

It contains the result after running the program:

- Two wordclouds from user1 and user2 with the most used words 

<img width="667" alt="Captura de pantalla 2019-08-14 a las 20 24 08" src="https://user-images.githubusercontent.com/49640612/63046399-a0b2e900-bed2-11e9-9403-d8b4da62466d.png">

- An image with all the tweets from user1 grouped by the the type of content.

<img width="944" alt="Captura de pantalla 2019-08-14 a las 20 33 32" src="https://user-images.githubusercontent.com/49640612/63046496-d2c44b00-bed2-11e9-823d-1ecaac4ce28e.png">

- An image with the comparison between both users.

<img width="1059" alt="Captura de pantalla 2019-08-14 a las 20 31 56" src="https://user-images.githubusercontent.com/49640612/63046434-b6281300-bed2-11e9-8b6e-730de1d98791.png">

### - jupyter notebook

It contains the different tests that have been done to test the best machine learning model of clustering.
