import sys
import csv
from selenium import webdriver
from selenium.webdriver import ActionChains


sys.path.append('~/PythonProjects/autologin/venv/lib/python3.7/site-packages')


options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

# options.add_argument('--user-data-dir=/Users/aaronbrandhagen/Library/Application\ Support/Google/Chrome/Default')

driver = webdriver.Chrome('/Users/aaronbrandhagen/Downloads/chromedriver', chrome_options=options)
options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

coptions = options.add_argument
coptions('window-size=1280x800')
coptions('remote-debugging-port=9222')
coptions('disable-gpu')
coptions('--no-sandbox')

# /Users/aaronbrandhagen/Library/Application Support/Google/Chrome/Default
css = driver.find_element_by_css_selector
id = driver.find_element_by_id
actions = ActionChains(driver)

def find_tags():
    with open('htmltags.csv', newline='') as tags:
        with open('passwordscsv.csv', newline='') as cfile:
            login_sites = csv.reader(cfile, delimiter=',')
            login_tags = csv.reader(tags, delimiter=',')
            for site, user, passwd in login_sites:
                driver.get(str(site))
                for _, usertag, passwdtag in login_tags:
                    # TODO return site from password csv file first

                    loginButton = id('loginbutton').click()

                    driver.execute_script("window.open('new_window')")
                    driver.switch_to.window(driver.window_handles[-1])


def parse_csv():
    sites = []
    with open('passwordscsv.csv', newline='') as cfile:
        login_sites = csv.reader(cfile, delimiter=',')
        for site, user, passwd in login_sites:
            # driver.get(str(site))
            # append sites for tags funtion to search for tag nams
            sites.append(site)

    return sites


def tags():

    for sites in parse_csv():
        driver.get(sites)
        # Check to see if page has a login button to be clicked before input fields show
        if driver.find_element_by_link_text("Login"):
            for names in driver.find_elements_by_tag_name('input'):
                print(names.get_attribute('name'))

            # If not, find the input tag names
            # use headless mode to find the tagsv or buttons and then open browser
            # if not driver.find_element_by_tag_name('button'):
                # for names in driver.find_elements_by_tag_name('input'):
                #     print(names)




tags()
