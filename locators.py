from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GSFI = (By.XPATH, '//input[@name="q"]')
    BUTTON = (By.XPATH, '//input[@name="btnK"]')

class SearchResultsPageLocators(object):
    LINK = (By.XPATH, '//a[@href="https://www.cbr.ru/"]')

class CBRPageLocators(object):
	TITLE = (By.TAG_NAME, 'title')
	RECEPTION = (By.XPATH, '//a[@href="/Reception/"]')
	MSG = (By.XPATH, '//a[@href="/Reception/Message/Register?messageType=Gratitude"]')
	GRATITUDE = (By.ID, "MessageBody")
	AGREE = (By.ID, "_agreementFlag")
	BURGER = (By.CSS_SELECTOR, "span.burger")
	ABOUT = (By.CSS_SELECTOR, '.for_branch_11377')
	WARNING = (By.XPATH, '//a[@href="/About/warning/"]')
	WARNING_TEXT = (By.TAG_NAME, 'p')
	ENG = (By.CSS_SELECTOR, '.langs a')