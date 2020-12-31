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

I had a difficult time getting topics that were up to the standard that I wanted to use for analysis. This is probably in part because LDA is a probablistic approach to topic modelling and because the documents weren't very long to begin and many documents had a small number of tokens for analysis the topics that were being created were blurry. I changed the values for no_below and no_above parameter to filter the Gensim dictionary which led to good results when no_below was set to 200 and no_above was set to .25 and removing commonly occuring stop words that were creating problems. Once I had better topics from the dictionary filtering, I increased the number of iterations from the default, 50, to 200. 




Topic 1: [?] release, attack, death, leave, damage, soldier, suicide, stand, russian, hospital, police, train, family, office, victory, medical, federal, trial, wound, authority, effort, early, force, capital, control




Topic 2: [covid] child, cancer, immigrant, woman, abuse, border, virus, treatment, migrant, illegal, detainee, force, death, vaccine, percent, disease, spread, federal, immigration, company, return, continue, political, family, authority



Topic 3: [foriegn affairs] israeli, palestinian, peace, attack, suicide, korean, security, bombing, force, woman, wound, soldier, syrian, money, group, militant, south, issue, troop, agreement, violence, bomber, north, political, shoot

Topic 4: chinese, child, prison, increase, prisoner, missile, young, leave, human, percent, family, woman, abuse, arrest, political, release, system, nation, military, lawyer, defense, remain, school, charge, court

Topic 5: police, charge, officer, shoot, murder, prosecutor, election, worker, suspect, trial, evidence, arrest, death, federal, member, corruption, accuse, raise, cabinet, party, black, system, leave, political, chief

Topic 6: election, woman, political, public, primary, early, voter, mother, national, result, governor, campaign, death, democratic, support, elect, company, republican, think, child, decision, announce, party, electoral, receive

Topic 7: election, candidate, voter, attack, democratic, ballot, result, party, campaign, republican, terrorist, leave, primary, voting, early, night, issue, continue, network, black, count, return, federal, president, threat

Topic 8: economic, economy, price, percent, market, sanction, support, business, growth, effort, increase, promise, raise, saudi, family, attack, group, benefit, company, fight, worker, force, leave, peace, world

Topic 9: election, political, campaign, climate, change, raise, fight, visit, family, offer, public, party, support, ensure, effort, democratic, trial, global, member, group, action, palestinian, reporter

Topic 10: doctor, health, issue, patient, medical, marriage, policy, political, animal, woman, record, couple, federal, trial, charge, public, family, hearing, german, child, practice, heart, member, decision, foreign

Topic 11: trump, crime, sexual, issue, church, policy, woman, nation, abuse, thing, military, president, effort, group, peace, charge, foreign, catholic, bring, public, world, political, election, leave, priest

Topic 12: nuclear, program, company, energy, weapon, administration, power, change, plant, federal, nation, campaign, proposal, agency, industry, policy, system, increase, spend, decision, large, climate, issue, major, environmental

Topic 13: group, federal, arrest, member, party, nuclear, weapon, election, political, attack, terrorist, judge, effort, program, militant, suspect, charge, support, security, agent, police, public, secret, money, announce

Topic 14: death, pandemic, woman, trial, political, federal, penalty, judge, court, issue, accuse, military, child, effort, execution, change, crisis, prosecutor, policy, group, problem, election, family, worker, release

Topic 15: school, teacher, lawyer, college, federal, charge, offer, internet, security, allow, child, program, family, medium, class, trial, public, social, member, woman, change, virus, income, victim, computer

Topic 16: troop, force, iraqi, water, nation, attack, power, military, college, public, political, world, resident, russian, administration, fight, afghan, member, crisis, group, large, mission, remain, provide, fighter

Topic 17: school, public, college, system, black, attack, worker, police, effort, education, strike, death, health, force, weapon, military, nation, measure, child, earthquake, support, raise, campaign, union, large

Topic 18: debate, political, voter, republican, money, campaign, candidate, party, immigration, politic, percent, election, nation, scandal, second, night, large, support, conservative, change, fight, budget, world, measure, leave

Topic 19: campaign, trump, child, democratic, president, republican, party, voter, convention, conservative, group, parent, political, election, nomination, public, early, candidate, spend, attack, member, world, leave, issue, speak

Topic 20: budget, court, federal, republican, system, campaign, spending, issue, reform, political, policy, limit, deficit, president, change, public, discuss, money, candidate, lawmaker, effort, justice, decision, action, black

Topic 21: military, force, attack, soldier, violence, fight, iraqi, police, rebel, troop, afghan, policy, civilian, group, officer, border, leave, battle, security, foreign, continue, relief, issue, family, change

Topic 22: crash, sentence, plane, school, storm, charge, prison, convict, flight, pilot, military, force, daughter, respond, death, leave, control, bring, small, hurricane, child, traffic, season, arrest, problem

Topic 23: court, health, legal, service, public, appeal, trump, insurance, program, federal, system, action, lawyer, ruling, private, decision, mental, woman, group, voter, civil, political, provide, judge, coverage

Topic 24: support, police, immigration, policy, leave, political, administration, issue, conference, attack, officer, legal, republican, human, claim, suggest, chief, federal, statement, offer, immigrant, legislation, charge, marriage, investigation

Topic 25: [women rights] abortion, woman, trade, online, power, political, peace, effort, never, school, election, force, allow, divide, economic, nation, president, threat, issue, debate, fight, death, measure, follow

Topic 1: election, campaign, charge, trump, military, fight, candidate, force, troop, arrest, voter, political, iraqi, republican, group, democratic, soldier, president, peace, trial, control, rebel, expect, opposition, appear

Topic 2: police, officer, shoot, election, terrorist, service, political, attack, iraqi, world, death, close, leave, remain, sander, resign, military, family, member, local, system, suicide, travel, diplomat, force

Topic 3: research, threat, internet, group, child, cancer, attack, chinese, policy, terrorist, pandemic, political, fight, foreign, court, release, member, interest, protect, black, message, service, border, effort, company

Topic 4: charge, crash, plane, russian, guilty, public, company, accuse, security, federal, flight, plead, attack, lawyer, building, prosecutor, office, trial, member, order, passenger, rebel, airline, interview, police

Topic 5: protest, black, troop, attack, campaign, protester, force, violence, large, police, continue, military, public, close, family, woman, allow, migrant, thousand, israeli, member, policy, support, hundred, arrest

Topic 6: police, federal, court, arrest, party, charge, suspect, order, family, public, force, officer, attack, investigation, raise, political, lawyer, leave, authority, election, judge, death, local, issue, member

Topic 7: palestinian, political, industry, company, price, economic, power, agency, water, program, candidate, approve, effort, israeli, leave, federal, charge, suicide, death, television, nation, speed, budget, family, police

Topic 8: woman, child, abuse, immigrant, church, sexual, political, little, mother, member, effort, human, immigration, group, percent, recent, issue, legal, priest, campaign, raise, young, force, international, release

Topic 9: nuclear, woman, attack, afghan, soldier, leave, militant, weapon, abortion, world, online, military, force, plant, police, group, young, wound, muslim, support, party, member, peace, policy, democratic

Topic 10: court, marriage, group, immigration, decision, appeal, conservative, abortion, family, document, issue, woman, release, judge, federal, legal, couple, voter, political, justice, republican, measure, support, limit, allow

Topic 11: military, attack, victim, think, group, political, program, death, administration, party, leave, nation, force, campaign, shiite, support, jewish, child, accuse, issue, terrorist, action, world, member, money

Topic 12: candidate, debate, change, political, policy, party, republican, economy, climate, politic, economic, election, president, budget, child, democratic, crisis, voter, campaign, leave, health, speech, system, issue, start

Topic 13: percent, border, support, military, nation, korean, measure, family, large, force, power, federal, troop, approve, increase, soldier, leave, provide, ensure, north, policy, airstrike, election, chinese, system

Topic 14: school, college, public, education, system, teacher, child, money, federal, campaign, political, issue, raise, missile, nation, agree, program, black, teach, human, decision, finance, scientist, parent, propose

Topic 15: israeli, attack, political, force, syrian, palestinian, police, nation, issue, early, military, support, offer, group, opposition, peace, conservative, visit, public, decision, agree, religious, major, leave, party

Topic 16: campaign, effort, policy, world, visit, increase, issue, raise, republican, budget, trade, political, public, voter, bring, economic, energy, large, military, announce, early, election, support, deficit, system

Topic 17: company, money, worker, spend, budget, campaign, program, strike, federal, business, republican, benefit, child, health, public, political, problem, group, union, raise, election, change, private, party, spending

Topic 18: death, crime, federal, sentence, prison, program, charge, convict, attack, trial, weapon, bombing, terrorist, nation, murder, effort, penalty, group, prosecutor, administration, money, health, force, change

Topic 19 [covid] health, doctor, patient, medical, virus, hospital, issue, offer, troop, force, provide, insurance, treatment, worker, mental, company, price, allow, program, treat, coverage, effort, spread, political, system

Topic 20: campaign, leave, child, issue, effort, return, public, woman, power, school, president, political, history, democratic, place, column, parent, season, trump, enough, thing, storm, force, national, german

## Results

You can check out the Tableau visualization that I made for my findings from my analysis. 

I have also included below some visualizations while I was working on the project.


