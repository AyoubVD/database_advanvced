# Databases Advanced
# Read Me 😢

<h1> Web scraping python script </h1>

<h2> Intro </h2>
This script will scrape the website: https://www.blockchain.com/btc/unconfirmed-transactions <br>
and print the highest value on the console while also writing it down in a log file. <br>

<h2> Requirements </h2>
Obviously you need Python to be able to run this script, so I'm assuming that you've already have it up and running. <br>
If you don't, you can simply install python with the help of a youtube tutorial. Keep in mind that we're using Python 3.8. <br>
I do reccomend to use the latest version of Python. <br>
You need to install pandas and bs4 if you haven't done so already, otherwise the script won't run. <br>
You can do so simply by using the pip install command in the terminal of your operating system. <br>
<ul>
  <li> pip install pandas </li>
  <li> pip install bs4 </li>
</ul>

<h2> Usage </h2>
<h3>If you are on a Ubuntu OS you can use the command git clone to download this repository. </h3>
<ul>
  <li> git clone https://github.com/AyoubVD/database_advanvced.git </li>
</ul>
You need to run this script on python, it will keep running until you press <b>ctrl + c</b>. <br>
To use it you need to specify to your terminal that you want to use Python to execute this script. <br>
<ol>
  <li> Open the terminal </li>
  <li> Navigate to the python file location using the cd command 
  <ul> <li> If you don't know the full name of the directory by heart you can use the command dir to show you the possible paths to take </li> </ul></li></li>
  <li> Python3 part1.py</li>
</ol>

<h3> Windows OS </h3>
<ol>
  <li> Open the cmd </li>
  <li> Navigate to the python file location using the cd command 
  <ul> <li> If you don't know the full name of the directory by heart you can use the command dir to show you the possible paths to take </li> </ul></li>
  <li> Once you're there you cans use the command
    <ul> <li> python part1.py </li> </ul>
  </li>
 </ol>
Once again if you want to stop the program you need to press <b>ctrl + c</b>. <br>



<h2> Use of this script </h2>
This script scrapes the website mentoined above, and returns the highest value each minute whilst putting it in a log file.
