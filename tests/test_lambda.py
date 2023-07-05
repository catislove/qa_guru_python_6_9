import json

from allure_commons.types import Severity
from selene import by, be
from selene.support.shared import browser
import allure
from allure import attachment_type


@allure.story('test_lambda')
@allure.label('owner', 'Amalia')
@allure.tag('web')
@allure.severity(Severity.MINOR)
def test_github_for_with_allure():
    allure.attach('Home work 06 09', name='Text', attachment_type=attachment_type.TEXT)
    allure.attach('<h1>Home work 06 09</h1>', name='Html', attachment_type=attachment_type.HTML)
    allure.attach(json.dumps({'first': 1, 'second': 2}), name='Json', attachment_type=attachment_type.JSON)

    with allure.step('Open main page'):
        browser.open('https://github.com')

    with allure.step('Find repositories'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').type('eroshenkoam/allure-example')
        browser.element('.header-search-input').press_enter()

    with allure.step('Go to repository link'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Open tab Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Check availability Issues with number 76'):
        browser.element(by.partial_text('#76')).should(be.visible)