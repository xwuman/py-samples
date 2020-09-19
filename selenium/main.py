from selenium import webdriver
import time

def main():
    browser = webdriver.Chrome(executable_path='chromedriver.exe') # 声明chrome浏览器
    # 修改浏览器窗口
    print("设置浏览器宽480、高800显示")
    browser.set_window_size(480, 800)

    browser.get("http://localhost:9580/nmc/login.php")


    qx_nmc_uname = browser.find_element_by_id("qx_nmc_uname")
    qx_nmc_uname.send_keys("root")

    qx_nmc_pwd = browser.find_element_by_id("qx_nmc_pwd")
    qx_nmc_pwd.send_keys("")


    time.sleep(5)

    btn = browser.find_element_by_xpath("//img[@onclick='submit_login()']")
    btn.click()

    time.sleep(5)
    browser.quit()


if __name__ == "__main__":
    main()