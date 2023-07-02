from selenium import webdriver
import time
import random


def visit_sr_mian():
    # 启动浏览器访问米游社
    web = webdriver.Chrome()
    web.get("https://www.miyoushe.com/sr/")
    time.sleep(random.uniform(3, 5))

    # 关闭广告弹窗
    xpath_box_close = '''/html/body/div[4]/div/div/img'''
    element = web.find_element_by_xpath(xpath_box_close)
    element.click()

    return web


def load_more_sheaf(web):
    # 点击加载更多
    # noinspection PyBroadException
    try:
        print('执行加载更多楼层')
        selector_data = "#__layout > div > div.root-page-container > div > div > div > div.mhy-layout__main > " \
                        "div.mhy-article-list.mhy-home-article-list.mhy-container > " \
                        "div.mhy-container__footer.mhy-article-list__footer > div > div > button"
        element = web.find_element_by_css_selector(selector_data)
        element.click()
        time.sleep(random.uniform(1, 3))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    except Exception as e:
        load_more_sheaf(web)


def get_sheaf_urls(web, sheaf_num):
    # 获取所有详情页的链接
    # noinspection PyBroadException
    try:
        print('获取楼层url:' + str(sheaf_num))
        xpath_data = '''//*[@id="__layout"]/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div[$num]/a'''
        element = web.find_element_by_xpath(xpath_data.replace("$num", str(sheaf_num))).get_attribute("href")

        return element
    except Exception as e:
        get_sheaf_urls(web, sheaf_num)


if __name__ == '__main__':
    driver = visit_sr_mian()

    for i in range(0, 10000):
        url = get_sheaf_urls(driver, i + 1)

        with open('./urls/mhy_sheaf_urls_20230605.txt', mode='a+') as f:
            f.write(url + '\n')

        print(url)

        if (i + 1) % 19 == 0:
            load_more_sheaf(driver)

    driver.close()