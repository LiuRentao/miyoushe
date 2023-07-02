from selenium import webdriver
import time
import random


def visit_sr_sheaf(url):
    # 启动浏览器访问详情页
    web = webdriver.Chrome()
    web.get(url)
    time.sleep(random.uniform(3, 5))

    return web

def get_text(web):
    selector_data = '''#__layout > div > div.root-page-container > div > div.mhy-layout__main > div.mhy-article-page__main.mhy-container > div.mhy-article-page__content > div > div'''
    element = web.find_element_by_css_selector(selector_data)
    print(element.text)

if __name__ == '__main__':
    driver = visit_sr_sheaf('https://www.miyoushe.com/sr/article/39913074')


    #get_text(driver)


    xpath_data = '''//*[@id="__layout"]/div/div[2]/div/div[1]/div[1]/div[2]/div/div'''
    element = driver.find_element_by_xpath(xpath_data)
    print(element.text)
