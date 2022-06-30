from selenium.webdriver.common.by import By


class BasePageLocators:
    HEADER = (By.CSS_SELECTOR, '.header__top')
    SHOPPING_CART_MODAL_WINDOW = (By.CSS_SELECTOR, '.in .modal-dialog')
    NEWS_WINDOW = (By.CSS_SELECTOR, '.new-adv-user__content')
    NEWS_WINDOW_TITLE = (By.CSS_SELECTOR, '.top-text__adv-user')
    AUTHORIZATION_BTN = (By.CSS_SELECTOR, ".header-bottom__login")
    WISHLIST_BTN = (By.CSS_SELECTOR, ".header-bottom__favorites-icon.header-bottom__icon")


class HomePageLocators:
    PRODUCT_CARD = (By.XPATH, "//p[contains(text(), 'Передпродажі')]/../../div//div[@class='owl-item'][1]")
    PRODUCT_TITLE = (By.XPATH, "//p[contains(text(), 'Передпродажі')]/../..//a[@class='product__name']")

    # SLIDER BLOCK
    SLIDER_BLOCK = (By.CSS_SELECTOR, '.main-slider.js-main-slider')
    RIGHT_ARROW_SB = (By.CSS_SELECTOR, '.main-slider .icon-arrow_right')
    LEFT_ARROW_SB = (By.CSS_SELECTOR, '.main-slider .icon-arrow_left')
    PAGINATION_BLOCK = (By.CSS_SELECTOR, '.main-slider .owl-pagination')
    PAGINATION_POINTS = (By.CSS_SELECTOR, '.main-slider .owl-page')
    DETAILED_INFO_BTN = (By.CSS_SELECTOR, '.main-slider__btn.button')

    # PRE-ORDER BLOCK
    PRE_ORDER_BLOCK = (By.XPATH, "//p[contains(text(), 'Передпродажі')]/../..")
    RIGHT_ARROW_PO = (By.XPATH, "//p[contains(text(), 'Передпродажі')]/../../div//div[@class='owl-next']")
    LEFT_ARROW_PO = (By.XPATH, "//p[contains(text(), 'Передпродажі')]/../../div//div[@class='owl-prev']")
    SEE_ALL_LINK_PO = (By.XPATH, "//p[contains(text(), 'Передпродажі')]/../a[contains(text(), 'Дивитись усі')]")
    FEEDBACK_LINK_PO = (By.XPATH, "//p[contains(text(), 'Передпродажі')]/../../div//div[@class='product__testimonial']")
    PRE_ORDER_BTN_PO = (By.XPATH,
                        "//p[contains(text(), 'Передпродажі')]/../../div//a[@class='button product__btn']")

    # PERSONAL FOR YOU BLOCK
    PERSONAL_FOR_YOU_BLOCK = (By.XPATH, "//p[contains(text(), 'Персонально для вас')]/../..")
    RIGHT_ARROW_PFY = (By.XPATH, "//p[contains(text(), 'Персонально для вас')]/../../div//div[@class='owl-next']")
    LEFT_ARROW_PFY = (By.XPATH, "//p[contains(text(), 'Персонально для вас')]/../../div//div[@class='owl-prev']")
    PRODUCT_TITLE_PFY = (By.XPATH, "//p[contains(text(), 'Персонально для вас')]/../..//a[@class='product__name']")
    ORDER_BTN_PFY = (By.XPATH,
                     "//p[contains(text(), 'Персонально для вас')]/../../div//a[@class='button product__btn']")

    # NOVELTY BLOCK
    NOVELTY_BLOCK = (By.XPATH, "//p[contains(text(), 'Новинки')]/../..")
    RIGHT_ARROW_N = (By.XPATH, "//p[contains(text(), 'Новинки')]/../../div//div[@class='owl-next']")
    LEFT_ARROW_N = (By.XPATH, "//p[contains(text(), 'Новинки')]/../../div//div[@class='owl-prev']")
    SEE_ALL_LINK_N = (By.XPATH, "//p[contains(text(), 'Новинки')]/../a[contains(text(), 'Дивитись усі')]")
    FEEDBACK_LINK_N = (By.XPATH, "//p[contains(text(), 'Новинки')]/../../div//div[@class='product__testimonial']")
    PRODUCT_TITLE_N = (By.XPATH, "//p[contains(text(), 'Новинки')]/../..//a[@class='product__name']")
    ORDER_BTN_N = (By.XPATH, "//p[contains(text(), 'Новинки')]/../../div//a[@class='button product__btn']")

    # TOP BLOCK
    TOP_BLOCK = (By.XPATH, "//p[contains(text(), 'Топ')]/../..")
    RIGHT_ARROW_T = (By.XPATH, "//p[contains(text(), 'Топ')]/../../div//div[@class='owl-next']")
    LEFT_ARROW_T = (By.XPATH, "//p[contains(text(), 'Топ')]/../../div//div[@class='owl-prev']")
    SEE_ALL_LINK_T = (By.XPATH, "//p[contains(text(), 'Топ')]/../a[contains(text(), 'Дивитись усі')]")
    FEEDBACK_LINK_T = (By.XPATH, "//p[contains(text(), 'Топ')]/../../div//div[@class='product__testimonial']")
    PRODUCT_TITLE_T = (By.XPATH, "//p[contains(text(), 'Топ')]/../..//a[@class='product__name']")
    ORDER_BTN_T = (By.XPATH, "//p[contains(text(), 'Топ')]/../../div//a[@class='button product__btn']")

    # STORE RECOMMENDED BLOCK
    STORE_RECOMMENDED_BLOCK = (By.XPATH, "//p[contains(text(), 'Книгарня рекомендує')]/../..")
    RIGHT_ARROW_SR = (By.XPATH, "//p[contains(text(), 'Книгарня рекомендує')]/../../div//div[@class='owl-next']")
    LEFT_ARROW_SR = (By.XPATH, "//p[contains(text(), 'Книгарня рекомендує')]/../../div//div[@class='owl-prev']")
    SEE_ALL_LINK_SR = (By.XPATH, "//p[contains(text(), 'Книгарня рекомендує')]/../a[contains(text(), 'Дивитись усі')]")
    FEEDBACK_LINK_SR = (By.XPATH,
                        "//p[contains(text(), 'Книгарня рекомендує')]/../../div//div[@class='product__testimonial']")
    PRODUCT_TITLE_SR = (By.XPATH, "//p[contains(text(), 'Книгарня рекомендує')]/../..//a[@class='product__name']")
    ORDER_BTN_SR = (By.XPATH, "//p[contains(text(), 'Книгарня рекомендує')]/../../div//a[@class='button product__btn']")

    # BLOG BLOCK
    BLOG_BLOCK = (By.XPATH, "//a[@class = 'title' and contains(text(), 'Блог')]/../.. ")
    BLOG_LINK = (By.XPATH, "//a[@class = 'title' and contains(text(), 'Блог')]")
    BLOG_SECTION_TITLE = (By.XPATH,
                          "//a[@class = 'title' and contains(text(), 'Блог')]/../..//a[@class = 'blog_section-link']")
    BLOG_TOPIC_IMAGE = (By.XPATH,
                        "//a[@class = 'title' and contains(text(), 'Блог')]/../..//img[@class = 'preview_picture']")
    BLOG_TOPIC_TITLE = (By.XPATH,
                        "//a[@class = 'title' and contains(text(), 'Блог')]/../..//a[@class = 'blog_item-link']")

    # INFO ABOUT STORE BLOCK
    STORE_ADVANTAGES_BLOCK = (By.CSS_SELECTOR, ".advantages.clearfix")
    INFO_ABOUT_STORE_BLOCK = (By.CSS_SELECTOR, ".ceo.js-content")
    FULL_INFO_ABOUT_STORE_BTN = (By.CSS_SELECTOR, ".ceo__icon.icon-down-arrow.js-arrow")

    # BOOK LOVERS CLUB BLOCK
    BOOK_LOVERS_CLUB_BLOCK = (By.CSS_SELECTOR, ".club-link-but.footer-club-but")

    # MOST POPULAR QUERIES
    MOST_POPULAR_QUERIES_BLOCK = (By.XPATH, "//nav[@role ='navigation']")
    POPULAR_QUERY = (By.CSS_SELECTOR, ".categories_book")


class AuthorizationModalWindowLocators:
    REGISTRATION_LINK = (By.CSS_SELECTOR, ".auth-popup__bottom-link.login-to-register")
    TERMS_OF_USE_LINK = (By.CSS_SELECTOR, ".check__registration-text-link")
    REGISTRATION_NAME_FIELD = (By.CSS_SELECTOR, "[placeholder='Ваше ім’я']")
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "[placeholder='Ваша пошта']")
    REGISTRATION_PHONE_NUMBER_FIELD = (By.CSS_SELECTOR, "[placeholder='Телефон']")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "[placeholder='Пароль не менше 6 символів']")
    REGISTRATION_BTN = (By.CSS_SELECTOR, "[value = 'Зареєструватись']")
    REGISTRATION_ERROR_MESSAGE = (By.CSS_SELECTOR, ".register-form .error.submit-error")

    LOG_IN_EMAIL_OR_PHONE_FIELD = (By.CSS_SELECTOR, "[placeholder='Ваша пошта або телефон']")
    LOG_IN_PASSWORD = (By.CSS_SELECTOR, "[name='USER_PASSWORD']")
    LOG_IN_BTN = (By.CSS_SELECTOR, "[value='Увійти']")
    LOG_IN_GREETING_TEXT = (By.XPATH, "//span[contains(text(), 'Вітаємо, ')]")
    LOG_IN_ERROR_MESSAGE = (By.CSS_SELECTOR, "#login-modal .error.submit-error")


class ProductPageLocators:
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.card__title')
    FEEDBACK_BTN = (By.XPATH, "//li/a[contains(text(), 'Відгуки')]/..")
    BUY_BTN = (By.CSS_SELECTOR, '.button.button--width.card__button')
    ADD_PRODUCT_TO_WISHLIST_LINK = (By.CSS_SELECTOR, '.desire__text')
    READ_THE_PASSAGE_LINK = (By.CSS_SELECTOR, '.preview__label.preview__label--position')
    READ_THE_PASSAGE_MODAL_WINDOW = (By.CSS_SELECTOR, '.modal-content.modal-content--height')
    SHOP_ADDRESSES_LINK = (By.XPATH, "//a[contains(text(), 'Адреси магазинів')]")
    DELIVERY_TEXT = (By.XPATH, "//span[contains(text(), 'Доставка')]")
    INFO_ABOUT_DELIVERY = (By.XPATH, "//p[contains(text(), 'відділення Нової Пошти')]")
    PAYMENT_TEXT = (By.XPATH, "//span[contains(text(), 'Оплата')]")
    INFO_ABOUT_PAYMENT = (By.XPATH, "//p[contains(text(), 'Післяплата (оплата на пошті')]")
    LEFT_ARROW_IN_PRODUCT_PICTURE_FIELD = (By.CSS_SELECTOR, ".preview-carousel .owl-prev")
    NEW_PRODUCT_PICTURE = (By.CSS_SELECTOR, ".card__preview-wrap div[class='owl-item']:last-child")


class PromotionsPageLocators:
    PROMOTIONS_CARDS = (By.CSS_SELECTOR, '.news_promotions')


class CatalogPageLocators:
    FILTER_SIDE_BAR = (By.CSS_SELECTOR, '.section-listing .col-md-3')


class ShoppingCartLocators:
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.checkout__name')


class BlogPageLocators:
    BLOG_MENU = (By.CSS_SELECTOR, '.container.about-us .blog-menu')
    TITLE_IN_SEARCH_TREE = (By.CSS_SELECTOR, '.breadcrumbs__elem.active')


class BookLoversClubPageLocators:
    TOPIC_LIST = (By.CSS_SELECTOR, '.ye-club-container.row')


class WishlistPageLocators:
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.book-info__name')


class ContactsLocators:
    CONTACTS_PHONE_NUMBER = (By.CSS_SELECTOR, '.art-info__tel')
