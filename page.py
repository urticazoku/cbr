from elements import BasePageElement
from locators import MainPageLocators, SearchResultsPageLocators, CBRPageLocators
from time import sleep
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import os
from settings import login, password, mail_from, mail_to, smtp_server

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def is_google_input(self,text):
        element = self.driver.find_element(*MainPageLocators.GSFI)
        element.send_keys(text)
        if element:
            return True
        else:
            return False

    def click_search_button(self):
        element = self.driver.find_element(*MainPageLocators.BUTTON)
        sleep(3)
        element.click()


class SearchResultsPage(BasePage):
    def get_site(self):
        element = self.driver.find_element(*SearchResultsPageLocators.LINK)
        element.click()
        self.driver.switch_to_window(self.driver.window_handles[1])
        return self.driver.page_source

class CBRPage(BasePage):
    def send_mail(self,filename):
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = 'test message'
        msgRoot['From'] = mail_from
        msgRoot['To'] = mail_to
        msgRoot.preamble = 'This is a multi-part message in MIME format.'
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)
        msgText = MIMEText('This is the alternative plain text message.')
        msgAlternative.attach(msgText)
        msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Noifty!', 'html')
        msgAlternative.attach(msgText)
        fp = open(filename, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)

        smtp = smtplib.SMTP_SSL(smtp_server)
        smtp.login(login, password)
        smtp.sendmail(mail_from, mail_to, msgRoot.as_string())
        smtp.quit()
        os.remove(filename)

    def is_cbr_page(self):
        element = self.driver.find_element(*CBRPageLocators.TITLE)
        return element

    def get_reception(self):
        element = self.driver.find_element(*CBRPageLocators.RECEPTION)
        element.click()
        message_element = self.driver.find_element(*CBRPageLocators.MSG)
        message_element.click()

    def send_gratitude(self):
        gratitude_element = self.driver.find_element(*CBRPageLocators.GRATITUDE)
        gratitude_element.send_keys('случайный текст')
        self.driver.save_screenshot('screenie0.png')
        self.send_mail('screenie0.png')
        agreement_element = self.driver.find_element(*CBRPageLocators.AGREE)
        self.driver.execute_script("window.scrollBy(0, window.innerHeight)")
        agreement_element.click()
        sleep(5)        
        self.driver.save_screenshot('screenie1.png')
        self.send_mail('screenie1.png')


    def about_page(self):
        element = self.driver.find_element(*CBRPageLocators.BURGER)
        element.click()
        sleep(10)
        self.driver.execute_script("document.querySelector('.for_branch_11377').click()")
        sleep(5)
        self.driver.execute_script("document.querySelectorAll(\"a[href='/About/warning/']\")[0].click()")
        sleep(5)
        warning_text = self.driver.find_element(*CBRPageLocators.WARNING_TEXT)
        eng_element = self.driver.find_element(*CBRPageLocators.ENG)
        eng_element.click()
        eng_text = self.driver.find_element(*CBRPageLocators.WARNING_TEXT)
        if warning_text!=eng_text:
            print("Тексты предупреждений отличаются")
        self.driver.save_screenshot('screenie2.png')
        self.send_mail('screenie2.png')


        

