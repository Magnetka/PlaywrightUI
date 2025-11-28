# Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
# Заполнить форму регистрации и нажать на кнопку "Registration"
# Сохранить состояние браузера
# Создать новую сессию браузера. В контекст необходимо подставить сохраненное состояние
# Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses. Страница "Courses" должна открыться без авторизации
# Проверить наличие и текст заголовка "Courses"
# Проверить наличие и текст блока "There is no results"
# Проверить наличие и видимость иконки пустого блока
# Проверить наличие и текст описания блока: "Results from the load test pipeline will be displayed here"


from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path="storage-state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="storage-state.json")
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_icon).to_be_visible()

    courses_title_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_title_text).to_be_visible()
    expect(courses_title_text).to_have_text('There is no results')

    courses_description_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_description_text).to_be_visible()
    expect(courses_description_text).to_have_text('Results from the load test pipeline will be displayed here')

    page.wait_for_timeout(3000)
