# Save Tagged Pages on Tumblr!

This is a really small script that uses selenium webdriver to pull the html pages from specific tags on your tumblr blog and saves them. It'll require a couple things from you: 

1. install firefox mozilla, v56 at the time of this script's creation, but later versions should work as well 
2. <code>pip install selenium</code> in the terminal 
3. You also need to install geckodriver! Find the correct version according to your OS and install. Geckodriver should be in your path. If you're on Mac, use <code>echo $PATH</code> in the terminal to see which paths already exist. You won't be able to put geckodriver in the /usr/bin, but you can put in user/local/bin if it already exists. 
4. Make sure python is installed as well, a simple google search will help you install python.

You're basically all set now! Place the python script where you'd like the contents to go, and run this command in the terminal: <br>
<code> python htmlDownload.py BLOG_NAME TAG_NAME NUM_PAGES_IN_TAG </code> 

Selenium webdriver will open up Mozilla on your computer. If you have a really slow internet connection, this script might not work because the webdriver implemented here relies on an implicit wait. Please wait until the script finishes running. Mozilla will close on its own afterwards.
