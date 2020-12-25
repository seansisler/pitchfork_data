## Background
In this project I'm going to use Pitchfork Music Reviews and the New York Times archive to look at how the news and current events shape the trends that we see in music being put out by artists. I had started the project wanting to use lyrics from artists whose albums were in the Billboard Top 200. The issue with using lyrics to find comparisons to current events and news over time is lyrical interpretation. Even if a song was making a political statement, the statement would normally be masked by some writing technique: metaphor, simile, or personal sentiment. For example, Taylor Swift released a song she wrote after realizing that politics has the ability to make individuals and whole populations feel alienated. She wrote it about how you cannot disagree with the government without being labeled as someone who hates the United States.(footnote) Lyrically, the song presents this by comparing politics to high school and using alientation as a theme and the government as an antagonist that ostrocizes people that aren't like them. "My team is losing, battered and bruising; Now I see the high fives between the bad guys; Leave with my head hung," would not be lyrics that we could pick up the political statement and undertones in.

Rather than use lyrics I used every Pitchfork review that had been published since it's launch in 1999. 


## Setup
The first group of tasks that I completed for this project was creating a project in GCP where I would have all the tools that I would need to complete my project. I created a compute instance and cloned my GitHub repo for the project so I would transfer files from my local to the virual environment or vice versa. The entirety of this project was completed in Google Cloud Platform.

## Data

The two sets of data that I used for this project came from the New York Times API and Pitchfork.com. From the NYT API, all articles published from 1995 to the present day were pulled. I found a dataset online of Pitchfork album reviews but the data stopped after 2017. Since the point of this project was to see the interactions and effect that the news and current events has on music being produced and released, cutting the data off in 2017 right after the Trump administration entered office would be losing an entire year of data that could have helpful insights. Instead I wrote a program that would pull all of the album reviews from Pitchfork so that I could have the entire archive of reviews for analysis. 

The Pitchfork reviews required little cleaning after removing HTML tags and getting columns formatted. The only issue that I ended up having with the program that scraped all the album reviews was that it didn't take the year that album was from and only got the date that the review was published. Coming back to this project in the future I would rerun the program after fixing the error that resulted in not aquiring this data. For my project, I continued on using the articles for analysis by the date which they were published. Pitchfork is known online for being pretentious and the focus of their reviews not totally about the music there is to be listened to but external factors also written into the reviews. 

Every Sunday, for example, starting in 2016 Pitchfork would publish a review for an album that was released in the past that had not been reviewed before. These reviews typically have some relevance with what is going on currently in the music world or have relevance with current events and the news. An example being that in January 2020, Pitchfork's review that they chose to do for their flashback Sunday was "Home" by the Dixie Chicks (months later, The Chicks). The Dixie Chicks were planned to release an album at some point in 2020 after a long hiatus from music (after getting cancelled and ostracized by the American public for political statements about George W. Bush). The first half of the review creates parallels to the way that "Home" became the album that it is. It was the product of a lawsuit battle they were having with a record label that was holding out on royalties owed to the Dixie Chicks. The context of the album fits much the same as the story that would lead up to their upcoming album. The review draws parallels to the political climate when "Home" was released in 2002 and currently. It discusses the tracks on the album in the context that the tracks would be discussed in a 2020 anaylsis of its contents. 

Due to relevant nature that Pitchfork writes reviews about older albums that they review, I'm going to be using all of the albums that were pulled from Pitchfork without concern of their actual release date. 

## Preprocessing

I used the same preprocessing for the Pitchfork reviews and the NYT Opinion pieces' abstracts. 

I made four sets of token that could have been used for analysis: (1) all of the tokens, unigram, with no stopwords removed; (2) unigram tokens with stopwords removed; (3) unigram tokens with stopwords removed and lemmatized; (4) bigram tokens produced from the tokens with stop words removed; (5) the previously mentioned bigram tokens lemmatized. 

## Analysis

Before starting with topic modelling, I used a default dictionary to see the most frequently occuring tokens that appeared in the NYT article abstracts and the Pitchfork reviews, using the lemmatized unigrams. There were very few simillarities between the two sets of tokens.

(insert picture of NYT with all tokens)
(insert picture of Pitchfork with all tokens)

I did the same process again but the second time only counting words with more than four characters. As would be expected, the Pitchfork tokens were music focused with words that have to do with the creative aspect of the album's production and songwriting. The NYT top tokens were much more distinct than those that were any length of characters and look like they would have good potential for making coherent topics. 

(insert picture of NYT with > 4)
(insert picture of Pitchfork with > 4)

For topic modeling, I tried several different topic modelling algorithms on the NYT tokens to see the topics that would be produced. I used the lemmatized unigrams and filtered out any token that had four characters or less. Because there wasn't much simillarity between the NYT top tokens and the Pitchfork tokens, I topic modelled the Pitchfork documents to see the results that they would produce but I used the mentioned set of tokens because I knew that the best chance I had to find simillarities between the two sets of documents would using the results from the NYT set with CorEx for a semi-supervised topic modelling of the Pitchfork reviews. 

### Topic Modeling 

Topic modelling was my primary interest for this probjust. My goal was to use the topic modelling of the two sets of documents, Pitchfork reviews and NYT opinion pieces, and find the correlation between current events and trends in music. I started topic modelling with latent Dirichlet allocation (LDA) because of the success I had with it in a previous project (the opinion abstracts being simillar is size and structure to the documents used in that project). I removed a few more stop words that were frequently appearing, most common tokens that were more to do with the structure of the news paper rather than the actual content (for example: 'article', 'photo', 'include') and I removed other words that I didn't think would effect the results of the topic modelling (example: 'month', 'would', 'could').

Before running a LDA model I used the coherence score of LDA models, looping through the range of 10 to 90 incrementing by 5. I had more then a million documents of NYT abstracts that streched about 25 years. I filtered the dictionary of tokens to get rid of any tokens that appeared in 100 or less documents and no tokens that appeared in more than 60% of the documents. The topic coherence score measurement helps distinguish between topics that are semantically interpretable topics and topics that are artifacts of statistical inference.


## Results

You can check out the Tableau visualization that I made for my findings from my analysis. 

I have also included below some visualizations while I was working on the project.


