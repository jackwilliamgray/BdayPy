# BdayPy
a lil python script that uses selenium to automatically post happy birthday to all your friends on facebook.
probably could be better optimised but oh well does the job.

 ## Installation & Setup
Install [Python](https://www.python.org/downloads/)
Download [ChromeDriver](chromedriver.chromium.org/downloads)
Install [Selenium](https://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium) (only need step 1.2)

Change samplesettings.json to settings.json
Fill out account information under settings.json
Add chromedriver location
Pick a suitable delay between actions, would recommend around 5 seconds. (will add proper waiting for page to load etc if i get bored)

Then use a scheduler to make this run every day (ensure this only runs once, will repost on walls if ran more than once).