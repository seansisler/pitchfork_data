## Background
In this project I'm going to use Pitchfork Music Reviews and the New York Times archive to look at how the news and current events shape the trends that we see in music being put out by artists. I had started the project wanting to use lyrics from artists whose albums were in the Billboard Top 200. The issue with using lyrics to find comparisons to current events and news over time is lyrical interpretation. Even if a song was making a political statement, the statement would normally be masked by some writing technique: metaphor, simile, or personal sentiment. For example, Taylor Swift released a song she wrote after realizing that politics has the ability to make individuals and whole populations feel alienated. She wrote it about how you cannot disagree with the government without being labeled as someone who hates the United States.(footnote) Lyrically, the song presents this by comparing politics to high school and using alientation as a theme and the government as an antagonist that ostrocizes people that aren't like them. "My team is losing, battered and bruising; Now I see the high fives between the bad guys; Leave with my head hung," would not be lyrics that we could pick up the political statement and undertones in.

Rather than use lyrics I used every Pitchfork review that had been published since it's launch in 1999. 


## Setup
The first group of tasks that I completed for this project was creating a project in GCP where I would have all the tools that I would need to complete my project. I created a compute instance and cloned my GitHub repo for the project so I would transfer files from my local to the virual environment or vice versa. The entirety of this project was completed in Google Cloud Platform.

## Data

I had two main sources of data for this project. I used articles from the New York Times API and a data set provided by components.one with a SQLite database with more than 20,000 Pitchfork album reviews from the beginning of 1999 up to 2019. 

## Preprocessing

I used the same preprocessing for the Pitchfork reviews and the NYT Opinion pieces' abstracts. 

## Analysis

### Topic Modeling 

Topic modelling was my primary point of interest with this project. My goal was to use the topic modelling of the two sets of documents, Pitchfork reviews and NYT opinion pieces, and find the correlation between current events and trends in music. 

I started topic modelling with latent Dirichlet allocation because of the success I had with it in a previous project (the opinion abstracts being simillar is size and structure to the documents used in that project). Before running a LDA model I wanted to figure out the ideal number of topics that I should expect to use. I had more then 200,000 documents for the opinion abstracts that streched about 25 years. I used topic coherence as a way to find the optimal number of topics for the opinion abstracts. The topic coherence score measurement helps distinguish between topics trhat are semantically interpretable topics and topics that are artifacts of statistical inference. 

Topic modelling was my main interest when it came to looking at the similarities between the opinion pieces and the Pitchfork reviews. I tried several different approaches of topic modelling. I did Non-Negative Matrix Factorization, Latent Dis Allocation, ...... The abstracts for the opinion pieces are typicially about two paragraphs. 

LSA -
pLSA - 
LDA - A super effective topic modelling technique. 
LDA in Deep Learnig - lda2vec
NMF - family of linear algebra algorithms for identifying the latent structure in data represented as a non-negative matrix. input is term-document matrix, typically TD-IDF normalized. ouput is two non-negative matrices of the original n words by k topics and those same k topics by the m original documents. LINEAR ALGEBRA for topic modeling instead of a probabilistic approach.

Once I had the topics that I was happy with and were well defined in the Opinion's abstracts I moved on to topic modelling the Pitchfork reviews. I did the same process of trying the different methods of topic modelling that I used with 

## Conclusion
