# Code Institute - Milestone Project 5 - Rick-will-fix-it
#### by Patrick Doherty

To fulfill the requirements of this project I gave the website a theme of Rick and Morty. 
It is a popular television program where Rick is a Godlike inventor/scientist.
Users can have avatars of characters of the show and they will report bugs i.e 
problems for Rick to fix for them. The urgency of such fixes is dependant upon upvotes of each bug.
If users want a new feature they can start a kickstarter and raise the funds from the community in order for Rick to produce the new feature. 
The more financial backing a feature has the more time will be spent building it after it has reached its funding goal.
Updates on the sites progress can be seen from the homepage where a blog will detail 
updates on current bugs and features. Users can check site statistics to examine workflow and bug or feature status.

Every bug and feature page will have a comment section allowing for the community to discuss the problems and hopefully this will encourage memes from 
the television series. 

## UX
####User stories
- Bugs - Morty has noticed that everyone is acting strange at school and has decided to create a bug post. This will be seen by developers and other users of the site.
The problem can be discussed with other users and developers who will upvote the bug to determine its urgency. Morty at this point has the ability to edit his bug post in light of 
the discussion. When waiting for the bug to be fixed Morty can check the workflow statistics to see how it is divided based on urgency. Once the problem has been solved the developers
or Rick will close the bug post and release an update addressing it. 

- Features - Krombopulous Michael, an assassin who needs an anti-matter ray-gun for his next target decides to raise a new feature request on the site. He cannot raise a bug
as his problems are his alone and Rick must be paid for this service. KM posts a request for a new feature which automatically goes to 'awaiting pricing', lead times are given 
and the feature request cannot be seen by other users until a price has been decided upon. Once it has been decided upon the post will be visible on the site. If KM can meet 
the price himself, work on the feature can begin. If he cannot, contributions by other interested users can help him meet his goal. Once the price has been met it will be 
subject to the workflow priorities. The feature with the most contributions will be given priority and KM can follow this with the site's workflow statistics. 

- Anonymous user - This user can read all bugs, features and blogs however they cannot post anything be that bugs, features, comments, upvotes etc. Most of the options will be
unavailable to them, however, if they do attempt to do so they will be redirected to a login page. From here they can also register.

- Rick/Developer - Once a developer has worked on a bug for a certain amount of time i.e 60 minutes, they must fill out a timesheet in the admin panel. These timesheets will
then be used as data for the site's workflow statistics. Once they have finished with a bug or feature or even just decide to update on its progress they can post a blog
from the admin panel linking to the original post. 
 
## Features

### Existing Features
- Bugs - For raising tickets when a problem is encountered and other users can discuss this in a forum. Priority is given by upvotes.
- Features - Essentially the same as Bugs but for new feature proposals, and replacing upvotes with monetary contributions.
- Blog - Simple blog app detailing updates on Bugs or Features, only developers can create these.
- Cart - Shopping cart app where users can choose a feature and the amount they wish to contribute. 
- Checkout - Processes payments from users.
- Stats - Serializes information from models and uses this to create statistical charts displaying bug/feature/workflow statistics.

### Features Left to Implement
- Quiz - Users can upload quiz questions, if they are approved they can be added to a bank of questions. Users can then take a quiz made from these questions and compare results
on a scoreboard.


## Technologies used:
##### HTML - hypertext markup language
##### CSS - cascading style sheets 
##### Javascript - client side scripting language
##### Python - Programming Language
##### Git Bash & GitHub -for version control and backup of code
##### Bootstrap - A framework for developing responsive, mobile 1st websites.
##### Django - python web framework
##### Libraries i needed to install
- pillow (https://pillow.readthedocs.io/en/5.2.x/)
    - needed for using images
- django rest framework (http://www.django-rest-framework.org/)
    - for providing json information for statistics
- crossfilter (https://github.com/crossfilter/crossfilter)
    - to parse and compare data
- d3 (https://d3js.org/)
    - to create charts from data
- dc (https://dc-js.github.io/dc.js/)
    - to create charts from data
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- 

##### Plugin - Coverage - I needed during my testing of code. It generates reports which show you how much of your code you have tested.


## Testing
## Django Test Suite
##### For testing I used the Django Test Suite to cover all my apps and then used Coverage to report on what code had or had not been tested. After 
##### some persistence I eventually got the report up to 99%. I had difficulty testing the checkout views due to stripe using javascript. However when I 
##### found the correct tokens to use for form validation I was pleased. 99 Tests, 1823 statements with 22 missing. I also used Travis to test my builds,
##### finding great difficulty at first due to permissions regarding building databases. I overcame this with an if statement in settings.py that looks for 
##### 'Travis' in the environment and chooses to use the prebuilt database. The build now passes. 



- Accounts App: test\_app.py, test\_forms.py, test\_models.py and test\_views.py 
- Cart App: test\_app.py and test\_views.py and test\_forms.py
- Checkout App: test\_app.py, test\_forms.py, test\_models.py and test\_views.py 
- Bugs App: test\_apps.py, test\_forms.py, test\_models.py and test\_views.py 
- Features App: test\_apps.py, test\_models.py and test\_views.py and test\_forms.py
- Blog App: test\_apps.py and test\_views.py and test\_models.py
- Stats: test\_apps.py, test\_models.py and test\_views.py 

![Django Testing](/static/img/coverage1.png)
![Django Testing](/static/img/coverage2.png)




[![Build Status](https://travis-ci.org/Bad-Gandalf/Unicorn-Attractor.svg?branch=master)](https://travis-ci.org/Bad-Gandalf/Unicorn-Attractor)