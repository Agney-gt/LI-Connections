import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def authorize_api(file_name):
    # Authorize the API
    scope = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file'
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)
    client = gspread.authorize(creds)
    return client

def fetch_google_sheet(client, sheet_name):
    # Fetch Google Sheet
    sh = client.open(sheet_name)
    return sh

def connect_with_profile(driver, message):
    try:
        more = driver.find_elements(By.XPATH, '//button[contains(@aria-label, "More")]')
        more[1].click()
        time.sleep(5)
        connect = driver.find_elements(By.XPATH, '//span[contains(text(), "Connect")]')
        connect[1].click()
        time.sleep(5)

    except Exception as e:
        print("Could not find Connect Inside More (Mutual Connection Exists)")
        try:
            driver.find_element(By.XPATH, '//div[contains(@class, "top-card")]//button[contains(@aria-label, "Invite")]').click()
        except Exception as e:
            print(e)
            pass
        print(e)
        pass
    try:
        reason = driver.find_element(By.XPATH, '//button[contains(@aria-label, "Other")]')
        print(reason)
        reason.click()

        time.sleep(2)
        con = driver.find_element(By.XPATH, '//button[contains(@aria-label, "Connect")]')
        con.click()
        time.sleep(5)
        con2 = driver.find_element(By.XPATH, '//button[contains(@aria-label, "Connect")]')

        con2.click()

        time.sleep(5)

    except Exception as e:
        print(e)

        try:
            first = driver.find_elements(By.XPATH, '//button[contains(@aria-label, "Invite")]')
            first[1].click()

        except Exception as e:
            print(e)

            pass
        pass
    driver.find_element(By.XPATH, '//button[contains(@aria-label, "Add a note")]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//textarea[contains(@class, "text-area")]').send_keys("", message)
    sheet.update_cell(y + 2, 7, textA)
    time.sleep(5)
    driver.find_element(By.XPATH, '//button[contains(@aria-label, "Send")]').click()
    sheet.update_cell(y + 2, 8, d1)

def process_profiles(master_df):
    for j, i in enumerate(master_df['Account Name'].to_list()):
        y = master_df['Count'][j]
        sheet = sh.worksheet(i)
        df = pd.DataFrame(sheet.get_all_records())
        url = df['Lead URL'].to_list()

        # Set up Selenium WebDriver
        chrome_options = Options()
        chrome_options.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
        # chrome_options.add_argument("--headless") # For AWS/GCP
        driver = webdriver.Chrome(options=chrome_options, executable_path='D:/Downloads/chromedriver.exe')
        driver.delete_all_cookies()
        driver.maximize_window()
        action = webdriver.ActionChains(driver)

        # Login to LinkedIn
        driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        sleep(2)
        cookies = pickle.load(open(i+"-cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        sleep(5)

        # Get list of LinkedIn conversations
        driver.get('https://www.linkedin.com/messaging')
        sleep(2)
        names = driver.find_elements(By.XPATH, "//ul//li[contains(@class,'msg-conversation-listitem')]")
        nameList = []
        for name in names[:50]:
            action.move_to_element(name).perform()

        names = driver.find_elements(By.XPATH, "//ul//li[contains(@class,'msg-conversation-listitem')]//h3")
        for name in names:
            nameList.append(name.text)
        indexList = []
        for name in nameList:
            idx = df['Lead Name'].loc[lambda x: x == name].index.tolist()

            try:
                indexList.append(idx[0])
            except Exception as e:
                pass
        for i in indexList:
            sheet.update_cell(i + 2, 9, "Accepted")
        df_followups = pd.DataFrame(sheet.get_all_records())
        df_followups = df_followups[(df_followups['Status'] == 'Accepted') & (df_followups['Followups'] != 1)]
        followups = df_followups['Lead URL'].to_list()
        followup_indexList = []
        for followup in followups:
            try:
                driver.get(followup)
                time.sleep(5)
                driver.find_elements(By.XPATH, "//button[contains(@aria-label,'Message ')]")[-1].click()
                time.sleep(15)
                n = len(driver.find_elements(By.XPATH, "//p[contains(@class,'msg-s-event-listitem')]"))
                if n < 2:
                    driver.find_element(By.XPATH, "//div[contains(@aria-label,'Write a message')]").send_keys("", followup_message)
                    time.sleep(2)
                    driver.find_element(By.XPATH, "//button[@type='submit']").click()
                    time.sleep(2)
                driver.find_elements(By.XPATH, "//button//li-icon[@type='close']")[-1].click()
                idx = df['Lead URL'].loc[lambda x: x == followup].index.tolist()
                try:
                    followup_indexList.append(idx[0])
                except Exception as e:
                    pass
            except Exception as e:
                    pass
        try:
            for i in followup_indexList:
                sheet.update_cell(i + 2, 11, 1)
        except Exception as e:
            pass

        for k in url[y:y + 20]:
            try:
                print(k)
                driver.get(k)
                sleep(5)
                name = driver.find_elements(By.XPATH, '//h1[contains(@class, "text")]')[0].text.split(" ")[0]
                #pickle.dump( driver.get_cookies() , open("Rohit-cookies.pkl","wb"))
                sleep(2)
                try:
                    connect_with_profile(driver, message)
                except Exception as e:
                    pass
                y += 1
            except Exception:
                y += 1
                pass
        master.update_cell(int(j) + 2, 2, int(y))
        driver.quit()

# Authorize API and fetch Google Sheet
file_name = 'gsheets-key.json'
client = authorize_api(file_name)
sheet_name = 'LinkedinTest'
sh = fetch_google_sheet(client, sheet_name)
master = sh.worksheet("Master")
master_df = pd.DataFrame(master.get_all_records())

# Define variables
textA = ""  # Add your message here
d1 = ""  # Add your date here
followup_message = ""  # Add your follow-up message here

# Process profiles
process_profiles(master_df)
