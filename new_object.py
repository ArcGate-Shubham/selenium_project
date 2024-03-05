class wait_till_text_appears(object):
    def __init__(self, locator, text_):
        self.locator = locator
        self.text = text_

    def __call__(self, driver):
        try:
            element_text = driver.find_element(*self.locator).text
            print('dddd' + element_text)
            return self.text in element_text
        except BaseException:
            return False
