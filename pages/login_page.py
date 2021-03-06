from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_RPASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "accounts/login/" in self.url, "Login link is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Registration email is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS), "Registration password is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_RPASS), "Registration password repeat is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_BUTTON), "Registration button is not presented"
