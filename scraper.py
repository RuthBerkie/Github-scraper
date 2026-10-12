#using an open-source framework(selenium)to automate web browsers
from selenium import webdriver                         #webdriver controls the browser
from selenium.webdriver.chrome.service import Service  #manages the lifecycle of the browser driver executable
from selenium.webdriver.common.by import By            #specify how to search for HTML elements(classname)
import time

scrape = input("What github page would you like to scrape?:  ") #prompts for a github link with the username

cdp = r"C:\Developer\chromedriver.exe"      #local path of the chromedriver
service = Service(executable_path=cdp)      #loads the chromedriver
driver = webdriver.Chrome(service=service)  #Launches an automated window of the Google Chrome browser.
driver.get(scrape)                          #open and load the GitHub profile URL that was typed in.
repo = scrape

def going_for_raw(raw_page_url):            #custom function that handles reading code inside a specific file
    driver.get(raw_page_url)
    
    # Using driver.page_source on a /raw/ link retrieves ONLY plain text code
    html = driver.page_source
    lines = html.splitlines()               #Splits the large block of text into a Python list of individual, line-by-line strings.

  # Loops through every single line of code in the file,if the word password is found print an alert detailing the file's location and the line of code  
    for line in lines:
        if "password" in line:
            print(f"\n[!] Found matching line in {raw_page_url}:")
            print(f"-> {line.strip()}")

#navigating inside a single repository directory view and finding target files.   
def loop(next_page):
    driver.get(next_page)
    
    #(Link--primary)class corresponds to the clickable names of files and folders.
    elements = driver.find_elements(By.CLASS_NAME, "Link--primary")
    #A list comprehension that extracts the plain text name (e.g., main.py, script.js) from each found web element and saves them as stable strings
    file_names = [el.text for el in elements if el.text]
    
    #Iterate cleanly over strings so Selenium never crashes from page navigation
    for file_text in file_names:
        if "js" in file_text or "py" in file_text:              #Checks if the item's filename contains JavaScript or Python extensions.
            # Construct a direct path to the raw text server
            raw_page = f"{next_page}/raw/main/{file_text}"
            going_for_raw(raw_page)                             #in this raw_page execute going_for_row(in the raw file look for the word password)
            
            # Reset back to the repository list page safely
            driver.get(next_page)

    # Main execution loop
#While on the user's profile view, this locates the HTML blocks hosting links to all their public repositories.
res = driver.find_elements(By.CLASS_NAME, "repo")
links = [i.text for i in res if i.text]                         #Saves all the repository names into a string list.
flink = []                                                      #Initializes an empty tracking list to hold the complete repository URLs.

for l in links:                                                 #Loops through every repository name found on the profile
    next_page = f"{repo}/{l}"                                   #Combines the profile URL and repository name to form a complete working address
    flink.append(next_page)                                     #store this in the flink list holder
    loop(next_page)                                             #Hands this repository link off to the directory scanner function to inspect its contents


print("\nScanned repositories:")                    
#Outputs of every directory URL scanned during the session.
print(flink) 
time.sleep(5)   
driver.quit()
