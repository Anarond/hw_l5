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

    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#gender-radio-1').should(have.attribute('checked'))

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().type('1999').press_enter()
    browser.element('.react-datepicker__month-select').click().type('april').press_enter()
    browser.element('.react-datepicker__day--013').click()

    browser.element('#subjectsInput').click().type('ma').press_enter()
    browser.element('#subjectsContainer').should(have.text('Maths'))

    #browser.element('#hobbies-checkbox-1').click()
    #browser.element('#hobbies-checkbox-2').click()
    #browser.element('#hobbies-checkbox-3').click()

    #html = browser.driver.page_source
    #file_path = r'D:\page_source2.txt'
    #with open(file_path, 'w', encoding='utf-8') as file:
    #   file.write(html)

    time.sleep(3)