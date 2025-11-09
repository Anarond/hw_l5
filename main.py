from selene import browser, have
import time

def test_form():
    browser.open("https://demoqa.com/automation-practice-form")



    browser.element('#firstName').type('JOE')
    browser.element('#firstName').should(have.value('JOE'))

    browser.element('#lastName').type('PEACH')
    browser.element('#lastName').should(have.value('PEACH'))

    browser.element('#userEmail').type('joe@peach.com')
    browser.element('#userEmail').should(have.value('joe@peach.com'))

    browser.element('#userNumber').type('5550199045')
    browser.element('#userNumber').should(have.value('5550199045'))

    #browser.element('#gender-radio-1').click()
    #browser.element('#gender - radio - 1').should(have.value('5550199045'))

    #browser.element('#dateOfBirthInput').click()

    browser.element('#subjectsInput').click().type('M')
    #browser.element('#subjectsContainer').should(have.value('Defense Against the Dark Arts'))

    html = browser.driver.page_source
    file_path = r'D:\page_source2.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
       file.write(html)

    time.sleep(11)

