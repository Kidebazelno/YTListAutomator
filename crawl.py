from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import selenium

import pdfx

from argparse import ArgumentParser

#login
def login_youtube(args,browser):
    browser.get("https://www.youtube.com")
    WebDriverWait(browser,15).until(EC.presence_of_all_elements_located((By.TAG_NAME,'a')))
    login = browser.find_element(By.XPATH,"//a[@aria-label='登入']")
    login.click()
    WebDriverWait(browser,15).until(EC.presence_of_all_elements_located((By.TAG_NAME,'input')))
    account = browser.find_element(By.XPATH,"//input[@type='email']")
    account.send_keys(args.account)
    account.send_keys(Keys.ENTER);
    WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,"//input[@type='password']")))

    # browser.implicitly_wait(10)
    password = browser.find_element(By.XPATH,"//input[@type='password']")
    password.send_keys(args.password)
    password.send_keys(Keys.ENTER);

def get_urls(args) -> list:  #Modify this part to fit into your application
    pdf = pdfx.PDFx(args.file)
    urls = pdf.get_references_as_dict()['url']
    return urls

def add_yt_list(args,browser,create_list = True):
    urls = get_urls(args)
    for url in urls:
        browser.get(url)
        WebDriverWait(browser,15).until(EC.visibility_of_any_elements_located((By.XPATH,"//div[@id='above-the-fold']//div[@id='actions']//button[@aria-label='其他動作']")))
        elem = browser.find_elements(By.XPATH,"//div[@id='above-the-fold']//div[@id='actions']//button[@aria-label='其他動作']")
        for i in elem:
            try:
                i.click()
                break
            except selenium.common.exceptions.ElementNotInteractableException:
                continue
        try:
            WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,"//yt-formatted-string[contains(text(),'儲存')]")))
            elem = browser.find_element(By.XPATH,"//yt-formatted-string[contains(text(),'儲存')]")
            elem.click()
        except selenium.common.exceptions.TimeoutException:
            WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,"//div[@id='primary']//div[@id='above-the-fold']//button[@aria-label='儲存至播放清單']")))
            elem = browser.find_element(By.XPATH,"//div[@id='primary']//div[@id='above-the-fold']//button[@aria-label='儲存至播放清單']")
            elem.click()
        # input()
        if create_list:
            WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,"//yt-formatted-string[contains(text(),'建立新的播放清單')]")))
            elem = browser.find_element(By.XPATH,"//yt-formatted-string[contains(text(),'建立新的播放清單')]")
            elem.click()
            WebDriverWait(browser,15).until(EC.presence_of_all_elements_located((By.XPATH,"//input[@placeholder='輸入播放清單名稱...']")))
            elem = browser.find_element(By.XPATH,"//input[@placeholder='輸入播放清單名稱...']")
            elem.send_keys(args.listname)
            elem.send_keys(Keys.ENTER)
            create_list = False
        else:
            WebDriverWait(browser,15).until(EC.visibility_of_any_elements_located((By.XPATH,f"//ytd-add-to-playlist-renderer//div[@id='checkbox-label']//yt-formatted-string[@aria-label='{args.listname} 私人']")))
            elem = browser.find_elements(By.XPATH,f"//ytd-add-to-playlist-renderer//div[@id='checkbox-label']//yt-formatted-string[@aria-label='{args.listname} 私人']")
            for i in elem:
                try:
                    i.click()
                    break
                except selenium.common.exceptions.ElementNotInteractableException:
                    continue
        
        

parser = ArgumentParser()
parser.add_argument('-a', '--account',type=str,help="The Youtube account you want to login")
parser.add_argument('-p', '--password',type=str,help="The Youtube account's password")
parser.add_argument('-l','--listname',default="new_list",type=str,help="The playlist name")
parser.add_argument('-n','--newlist',default=0,type=int,help="Whether to create a new playlist or not")
parser.add_argument('-f', '--file',type=str,help="Path to the URL file")

if __name__ == '__main__':
    args = parser.parse_args()
    browser = webdriver.Chrome()
    login_youtube(args,browser)
    add_yt_list(args,browser,create_list=(args.newlist!=0))