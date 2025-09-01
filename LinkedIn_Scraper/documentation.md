# This is the Documentattion to run the LinkedIn scraper
Step 1. You need to run the following commnad in the cmd
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=8000 --user-data-dir="C:\Users\hp\Desktop\Coding\LinkedIn_Scraper\Chrome_Data"
Note : Here the first part is the path to the chrome.exe which you need to find on your system(If Google chrome is not installed, then install it)
Here, Second is the port that you can specify as you like
and third is the Path to the folder/directory where you will save the data of the chrome instance

Also, step up the download path to your desired folder, I have set it up to C:\Users\hp\Desktop\Coding\LinkedIn_Scraper\Partial_ids

Step 2 : install chrome extentions
First Extention : Instant Data Scraper
Link : https://chromewebstore.google.com/detail/instant-data-scraper/ofaokhiedipichpaobibbnahnkdoiiah

Second Extention : Easy Scraper - One-click web scraper
Link : https://chromewebstore.google.com/detail/easy-scraper-one-click-we/cljbfnedccphacfneigoegkiieckjndh


Step 3 : Make a new linked in profile using temp mail (If you do not want your main Id to get banned)
Login in the chrome instance using the new Linked In ID

Step 4 : According to your needs run the following search in chrome instance
data scientist 3 year experience site:linkedin.com/in (This willl give us the profiles of the peope fitting the profile, you can modify it according to your needs)
Them,to get max id, you can do the &&num=100 at the end of the url to get 100 Id from I page


Step 5 : Using the Instant Data Scraper Scrape all the Ids and save them in a folder name Partial_ids which is the download folder that we set to.


Step 6 : Use the get_links to Turn Partial_ids in to full_ids all the code is prrivided there and use get_mouse_position.py to get the mouse position that it requires

Step 7 : Finally filter the scrambeled data using the scraper_with_ai.py and then you gave nicely formatted data for all the IDS
