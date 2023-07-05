from allure_commons.types import Severity
import allure
from selene import by, be
from selene.support.shared import browser


@allure.story('selene')
@allure.label('owner', 'Amalia')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
def test_github_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number("#76")


@allure.step('Открываем GitHub')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type(repo)
    browser.element('.header-search-input').press_enter()


@allure.step('Переходим в репозиторий {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открываем issues-tab')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Находим элемент с номером 76')
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).should(be.visible)