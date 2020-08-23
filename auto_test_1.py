from selenium import webdriver


def test_fill_forms(company_name, register_email, register_name, register_phone, register_plain_password):
    driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')

    driver.get('https://dev-1.clicktrans.pl/register-test/courier')
    driver.maximize_window()

    driver.find_element_by_id("user_register_company_name").send_keys(company_name)
    driver.find_element_by_id("user_register_email").send_keys(register_email)
    driver.find_element_by_id("user_register_name").send_keys(register_name)
    driver.find_element_by_id("user_register_phone").send_keys(register_phone)
    driver.find_element_by_id("user_register_plainPassword").send_keys(register_plain_password)

    driver.find_element_by_id("user_register_settings_agreementRegulations").click()
    driver.find_element_by_id("user_register_settings_agreementPersonalData").click()
    driver.find_element_by_id("user_register_settings_agreementMarketing").click()
    driver.find_element_by_id("user_register_submit").click()
    success_message = driver.find_element_by_xpath("/html/body/div[6]/div").text

    driver.save_screenshot("screenshot-login.png")
    driver.quit()

    assert success_message == "OK - some registration logic is mocked"


if __name__ == '__main__':
    test_fill_forms(
        company_name="The Dog",
        register_email="dog@dog.pl",
        register_name="Dog Dog",
        register_phone="555555555",
        register_plain_password="thedog11",
    )
