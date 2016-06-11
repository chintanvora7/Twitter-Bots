<h1>Twitter Bots</h1>

<h2>Software Dependancies</h2>
<ul>
  <li>Python v 2.7</li>
  <li>Tweepy v 3.3.0</li>
  <li>VirtualEnv v 12.0.7</li>
  <li>Beautiful Soup v 4.3.2</li>
  <li>Lxml v 3.4.3</li>
  <li>Pillow v 2.8.1 (maybe also: freetype, libjpeg, and libpng, or freetype-devel etc.) </li>
</ul>

<h2>Instructions</h2>
<p> Please add the above dependancies to make sure the project works. Also, make sure you have a valid Twitter API key & Google API key that is added in the code itself (instructions given in each of the internal bots readme).
<p> Steps to get the content from github
<ul>
  <li>Clone the github directory from the link https://github.com/comp-journalism/news_bots</li>
  <li>(Optional) Create a vitrual env in a folder as it makes things easier to install</li>
  <li>(Optional) Instructions on installing virtualenv and creating a virtual directory are given <a href="http://simononsoftware.com/virtualenv-tutorial/"> here </a>
  <li>Install the aforementioned dependancies</li>
  <li>Follow individual deployment steps mentioned below for each bot</li>
</ul>  
  
<h2>History/Protest Bot</h2>
<p> The history bot works on the conecept of Information dissemination. The bot is configurable to listen to any keywords/#hashtags/user and will be able to reply with a random fact scraped from Wikipedia. 

<p><b>Workflow</b>
<ul>
  <li> Pre-Processor Module: Scraping.py script is the pre-processor script. It scrapes events from Wikipedia matching certain critera (see comments in the script scraping.py)</li>
  <li> Tweet Listerner Module: Stream.py script has the configuration for changing the listening parameter. Please see code documentation in stream.py.</li>
  <li> Editorial Logic Module: This is present in the stream_reader.py file. It houses logic of retrieving a random fact from the wikipedia scraped items.</li>
  <li> Reply Module: stream_reader.py also contains the module which helps in replying. It has a Text-to-Image convertor which allows replying with facts that are greater than 140 characters thereby bypassing the Twitter limit</li>
</ul>

<p><b> How to Run </b>
<ul>
  <li> Make sure all the dependancies are installed</li>
  <li> cd into the HistoryBot Folder</li>
  <li> Execute following command: <b>python historybot.py</b></li>
</ul>

<h2>Custom Search Bot</h2>
<p> Custom Search engine can be built on top of google which allow you to target particular sites for focused information. This bot allows you to easily configure your own custom search engine. It then uses the Twitter Direct Message interface to recieve queries and then it replies you with the search results in the form of an Email.

<p><b> Configuration of input.txt</p></b>
<ul>
  <li> <b>input.txt</b> is the main configuration file. This has a Search Engine ID which can be configured using Google Custom Search Engine Dashboard. It also has the ability to configure what thing one is looking for such as fileType, restrict search results by date and the number of results</li>
  <li> If one doesn't want to set the internal filters such as fileType, one can leave it blank (please don't leave any spaces after the '=' sign</li>
  <li> An example of date restrict would be if I wanted to see the results of the past 3 months, I would add "m3" and it would bring back results from the past 3 months. For day use 'd' and for year use 'y'</li>
</ul>

<p><b>Workflow</b>
<ul>
  <li> Pre-Processor Module: Here there is no script for pre-processing however it requires manual work of going to Google Custom Search Dashboard and creating a Custom Search Engine (CSE). Add all the sites you want to focus on in the CSE and copy the CSE id and add it to the input.txt file asking for the CSE id field</li>
  <li> Tweet Listerner Module: bot.py has the listener module. Since we do not want the queries to the bot to be public, plese DM the bot using twitter DM option. The DM should be a query (In order to DM you must be subscribed to the bot and the bot must be subscribed to you</li>
  <li> Editorial Logic Module: The Editorial logic here is to search the CSE and return valid results. This is present in the 'search.py' script.</li>
  <li> Reply Module: The reply module here is present in the script 'mail.py'. This has a pre-configured email id to send the replies back to of the results sent by the Editorial Logic.</li>
</ul>

<p><b> How to Run </b>
<ul>
  <li> Make sure all the dependancies are installed</li>
  <li> cd into the CustomSearchBot Folder</li>
  <li> Execute following command: <b>python bot.py</b></li>
</ul>
