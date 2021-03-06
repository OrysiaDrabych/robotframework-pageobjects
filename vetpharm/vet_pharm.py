from robotpageobjects import Page, robot_alias
from robot.utils import asserts
from time import sleep
from random import randint, choice
from string import ascii_lowercase
from itertools import islice
import uuid
from datetime import datetime


class VetoPharmHomePage(Page):
    """ Models the VetoPharm home page at:
        HOST:http://veto-pharm.devel.vetopharm.quintagroup.com"""


    # Allows us to call this page
    # something other than the default "VetDoc Home Page"
    # at the end of keywords.
    name = "VetoPharm"
    email = 'hostmaster@vetpharm.fr'
    password = '6V9Dwa3ryiCBeEViSNdqEmpBG4EeSEeJ'
    TLDS = ('com net org mil edu de biz de ch at ru de tv com'
    'st br fr de nl dk ar jp eu it es com us ca pl')
    # inheritable dictionary mapping human-readable names
    # to Selenium2Library locators. You can then pass in the
    # keys to Selenium2Library actions instead of the locator
    # strings.
    selectors = {
        "login or register": "id=login_link",
        "input username": "id=id_login-username",
        "input password": "id=id_login-password",
        "register": "xpath=(//span[contains(text(),'Register')])",
        "registration email": "id=id_registration-email",
        "registration password": "id=id_registration-password1",
        "confirm password": "id=id_registration-password2",
        "login submit": "xpath=(//button[@class='btn btn-md btn-primary'])",
        "registration submit": "xpath=(//button[@class='btn btn-lg btn-primary'])",
        "back to site": "xpath=(//i[@class='icon-home'])",
        "log out": "id=logout_link",
        "all products": "xpath=(//a[contains(text(),'All products')])",
        "list of products": "xpath=(//div[@class='row product-list'])",
        "add to basket": "xpath=(//li[@class='my-basket']/a)",
        "delete from basket": "xpath=(//div[@class='remove_butt col-md-1']//i[@class='fa fa-times'])",
        "list of wishlists": "xpath=(//li[@class='my-wishlist'])",
        "wishlist view": "xpath=(//a[@class='btn btn-default'][contains(text(),'View')])",
        "product quantity": "id=id_lines-0-quantity",
        "update quantity": "id=update-wish-quantities",
        "wishlist settings": "xpath=(//i[@class='fa fa-chevron-down'])",
        "delete product": "xpath=(//a[contains(text(),'Remove')])",
        "remove from wishlist": "xpath=(//button[@type='submit'][contains(text(),'Remove')])",
        "create new wishlist": "xpath=(//div[@class='wish_butt'])",
        "wishlist name": "id=id_name",
        "save wishlist": "xpath=(//button[@class='btn btn-lg btn-primary'])",
        "wishlists": "xpath=(//table[@class='table table-bordered'])",
        "delete wishlist": "xpath=(//button[@class='btn btn-danger btn-lg'])",
        "health center": "xpath=(//div[@class='health_centre health-centre-nav-menu'])",
        "animals": "xpath=(//a[@href='/en-gb/health_centre/animals/'])",
        "add animal": "xpath=(//a[@href='/en-gb/health_centre/animal/create'])",
        "species": "xpath=(//span[@class='select2-arrow'])",
        "species list": "id=select2-results-1",
        "selected species": "id=select2-chosen-1",
        "breed":"xpath=(//div[@id='s2id_id_breed']//span[@class='select2-arrow'])",
        "breed list": "id=select2-results-2",
        "sex": "id=id_sex",
        "sex list": "id=select2-results-3",
        "selected breed": "id=select2-chosen-2",
        "questions list": "xpath=(//div[@class='helth-info col-sm-6'])",
        "all animals": "xpath=(//a[contains(text(),'My animals')])",
        "my prescriptions": "xpath=(//a[@href='/en-gb/health_centre/prescriptions/'])",
        "add prescription": "xpath=(//a[@class='btn btn-primary'])",
        "prescription title": "id=id_title",
        "save prescription": "id=ajax-save-prescription",
        "prescription date": "id=id_created_date",
        "calendar": "xpath=(//div[@class='datetimepicker-days'])",
        "add animals": "id=add-animals-under",
        "list of animals": "xpath=(//div[@class='animals-container container'])",
        "select animal": "id=add-animals-groups",
        "add veterinarian": "id=add-veterinarian",
        "list of vets": "xpath=(//div[@class='vet-search-results'])",
        "select veterinarian": "xpath=(//button[@class='btn btn-default link_site_style'][contains(text(),'Close')])",
        "add products": "id=add-products-under",
        "search field": "xpath=(//div[@class='']/input[@id='id_title'])",
        "search products": "id=ajax-search",
        "products list": "xpath=(//div[@class='products_list'])",
        "select product": "xpath=(//*[@id='add-products']/div/div/div[3]/button)",
        "en button": "id=en-gb-comp",
        "fr button": "id=fr-comp",
        "widgets-list": "xpath=(//i[@class='fa fa-caret-down'])",
        "currency-widget": "id=currency-widget",
        "currency": "xpath=(//li[@id='currency-widget']//a[@class='trigger'])",
        "currency logo": "xpath=(//a[@class='dropdown-toggle']//i[@class='curr_logo'])",
        "selected currency": "xpath=(//div[@class='product_price']//i[@class='curr_logo'])",
        "user account": "xpath=(//div[@class='user-account'])",
        "my profile": "xpath=(//a[contains(text(),'My profile')])",
        "edit profile": "xpath=(//a[contains(text(),'Edit profile')])",
        "delete profile": "id=delete_profile",
        "account pasword": "id=id_password",
        "delete account": "xpath=(//button[@class='btn btn-lg btn-danger'][contains(text(),'Delete')])",
        "shipping country": "xpath=(//li[@id='shipping-widget']//a[contains(@class, 'trigger')])",
        "tax dropdown":  "xpath=(//ul[@class='tax_dropdown'])",
        "view prices": "xpath=(//span[contains(text(),'View prices')])",
        "search filters": "xpath=(//div[contains(text(),'FILTERS')])",
        "availability filter": "xpath=(//button[@class='filter-button']/span[contains(text(),'Availability')])",
        "availiable product": "xpath=(//span[@class='item-name'][contains(text(),'Available')])",
        "prescription filter": "xpath=(//button[@class='filter-button']/span[contains(text(),'Prescription ?')])",
        "no prescription": "xpath=(//span[@class='item-name'][contains(text(),'Issuance without prescription')])"
    }

    def gen_name(self, length):
        """Generate a random name with the given number of characters."""
        return ''.join(choice(ascii_lowercase) for _ in xrange(length))

    def email_generator(self):
        """Generate fake e-mail addresses."""
        user = self.gen_name(randint(3, 10))
        host = self.gen_name(randint(4, 20))
        return '%s@%s.%s' % (user, host, choice(self.TLDS.split()))

    def gen_password(self):
        password= uuid.uuid4().hex
        return password

    @robot_alias("maximize__window")
    def maximize_browser_window(self):
        self._current_browser().maximize_window()
        return self

    @robot_alias("Login__into__user__account")
    def successful_login(self):
        self.login_into_acc(self.email, self.password)
        self.body_should_contain_text('Welcome back', 
            'Login failed for user')
        return self

    @robot_alias("Try__to__login__with__incorrect__credentials")
    def unsuccessful_login(self):
        self.login_into_acc(self.email_generator(), self.gen_password())
        self.body_should_contain_text('Please enter a correct username and password. Note that both fields may be case-sensitive', 
            'No alert message about incorrect credentials')
        return self

    def login_into_acc(self, email, password):
        self.click_element("login or register")
        self.type_in_box(email, "input username")
        self.type_in_box(password, "input password")
        self.click_button("login submit")
        return self

    @robot_alias("Logout__from__account")
    def log_out(self):
        self.click_element("user account")
        self.click_element("log out")
        self.body_should_contain_text('Login or register',
            'Logout failed')
        return self

    @robot_alias("Return__to__site")
    def back_to_website(self):
        self.click_element("back to site")
        self.body_should_contain_text('All products', 'Return to site button does not work')
        return self

    @robot_alias("Try__to__register__already__taken__email")
    def taken_email_registration(self):
        self.register(self.email, self.password)
        self.body_should_contain_text('A user with that email address already exists', 
            'Successful registration for already taken email')
        return self

    @robot_alias("Try__to__register__the __invalid__email")
    def invalid_email_registration(self):
        self.register(self.email_generator()[:-5])
        self.body_should_contain_text('Enter a valid email address',
            'Successful registration for invalid email address')
        return self

    @robot_alias("Use__too__short__password")
    def invalid_password_registration(self):
        self.register(self.email_generator(), self.gen_password()[:3])
        self.body_should_contain_text('Ensure this value has at least 6 characters (it has',
            'No alert message about insecure password')
        return self

    @robot_alias("Unsuccessful__password__confirmation")
    def wrong_password_confirmation(self):
        self.click_element("login or register")
        self.click_element("register")
        sleep(2)
        self.type_in_box(self.email_generator(), "registration email")
        self.type_in_box(self.password, "registration password")
        self.type_in_box(self.gen_password(), "confirm password")
        self.click_button("registration submit")
        self.body_should_contain_text('The two password fields didn\'t match.',
            'No alert message about password confirmation fail')
        return self

    def register_account(self):
        password=self.register()     
        self.body_should_contain_text('Thanks for registering!',
            'Registration Failed')
        return password 

    def register(self, email=None, password=None):
        if password==None: 
            password= self.gen_password()
        if email==None:
            email= self.email_generator()
        self.click_element("login or register")
        self.click_element("register")
        sleep(2)
        self.type_in_box(email, "registration email")
        self.type_in_box(password, "registration password")
        self.type_in_box(password, "confirm password")
        self.click_button("registration submit")
        return password

    @robot_alias("Delete__profile")
    def delete_account(self, password):
        self.click_element("user account")
        self.click_element("my profile")
        self.click_element("edit profile")
        self.click_element("delete profile")
        self.type_in_box(password, "account pasword")
        self.click_element("delete account")
        self.body_should_contain_text("Your profile has now been deleted. Thanks for using the site", "Profile was not deleted")
        return self    

    def type_in_box(self, txt, search_box):
        for i in range(len(txt)):
            self.input_text(search_box, txt[0:i+1])
        return self
        
    def body_should_contain_text(self, str, error_message, ignore_case=True):
        result_msg = str.lower() if ignore_case else str
        result_msg = result_msg.encode("utf-8")
        body_txt = self.get_text("css=body").encode("utf-8").lower()
        asserts.assert_true(result_msg in body_txt, error_message)
        return self

    @robot_alias("switch__between__languages")
    def change_language(self):
        self.click_element("fr button")
        self.body_should_contain_text("Tous les produits", "French was not selected")
        self.click_element("en button")
        self.body_should_contain_text("All products", "English was not selected")
        return self

    @robot_alias("select__currency")
    def change_currency(self):
        self.click_element("widgets-list")
        self.click_element("currency-widget")
        currency_widget=self.find_element("currency-widget")
        currency_list=currency_widget.find_elements_by_tag_name("li")
        currency= choice(currency_list)
        selected_currency= self.get_text(currency)
        self.click_element(currency)
        self.click_element("widgets-list")
        self.element_text_should_be("currency", selected_currency)
        currency_logo= self.get_text("currency logo")
        self.element_text_should_be("selected currency", currency_logo)
        return self

    @robot_alias("select__shipping__country")
    def select_country(self):
        self.click_element("shipping-widget")
        shipping_widget=self.find_element("shipping-widget")
        counrty_list= shipping_widget.find_elements_by_tag_name("li")
        selected_country = choice(counrty_list)
        country = self.get_text(selected_country)
        self.click_element(selected_country)
        self.click_element("widgets-list")
        self.element_text_should_be("shipping country", country)
        return self

    @robot_alias("select__prices__view")
    def view_prices(self):
        self.click_element("view prices")
        tax_dropdown=self.find_element("tax dropdown")
        tax_list=tax_dropdown.find_elements_by_tag_name("li")
        selected_tax= choice(tax_list)
        price_view= self.get_text(selected_tax).lower()
        self.click_element(selected_tax)
        product= self.select_product()
        tax= product.find_element_by_tag_name("sup")
        asserts.assert_true(self.get_text(tax).lower() in price_view, 
            'Price view does not include tax information')
        return self

    @robot_alias("Add__product__to__wishlist")
    def add_to_wishlist(self):
        product = self.select_product()
        self.mouse_over(product)
        wishlist= product.find_elements_by_tag_name('i')
        default_wishlist= product.find_elements_by_tag_name('label')
        pr_name = self.product_name(product)
        self.click_element(wishlist[0])
        sleep(2)
        self.click_element(default_wishlist[0])
        self.click_element("list of wishlists")
        self.click_element("wishlist view")
        self.body_should_contain_text(pr_name, 'Selected product was not added to wishlist')
        return self

    @robot_alias("Update__quantity__in__whishlist")
    def update_quantity(self):
        self.type_in_box('3', "product quantity" )
        self.click_element("update quantity")
        box_value= self.find_element("product quantity").get_attribute('value')
        asserts.assert_true(box_value =='3', 
            "The product quantity was not updated")
        return  self


    @robot_alias("Delete__product__from__wishlist")
    def delete_wishlist_product(self):
        self.click_element("wishlist settings")
        self.click_element("delete product")
        self.click_element("remove from wishlist")
        self.body_should_contain_text('was removed from your \'Default\' wish list', 'Selected product was not removed from the wishlist')
        return self

    @robot_alias("Create_new_wishlist")
    def create_wishlist(self):
        self.click_element("list of wishlists")
        self.click_element("create new wishlist")
        self.type_in_box('For my cat', "wishlist name")
        self.click_element("save wishlist")
        self.body_should_contain_text('Your wishlist has been created', 'Wishlist was not created')
        self.click_element("list of wishlists")
        self.body_should_contain_text('For my cat', 'Wishlist was not created')
        return self

    @robot_alias("Delete__the__wishlist")
    def delete_wishlist(self):
        wishlists= self.find_element("wishlists")
        last_wishlist= wishlists.find_elements_by_tag_name('td')[-1]
        dropdown_toggle= last_wishlist.find_element_by_tag_name("button")
        self.click_element(dropdown_toggle)
        delete_btn=last_wishlist.find_elements_by_tag_name("li")[-1]
        self.click_element(delete_btn)
        self.click_element("delete wishlist")
        self.body_should_contain_text("Your 'For my cat' wish list has been deleted", '')
        body_txt = self.get_text("css=body").encode("utf-8").lower()
        asserts.assert_false('For my cat' in body_txt, 'Wishlist was not created')
        return self

    @robot_alias("Add__product__to__basket")
    def add_to_basket(self):
        product = self.select_product()
        pr_name = self.product_name(product)
        self.mouse_over(product)
        add_to_basket=product.find_elements_by_tag_name("button")[-1]
        self.click_element(add_to_basket)
        self._current_browser().back()
        self.click_element("add to basket")
        self.body_should_contain_text(pr_name, 'Selected product was not added to basket')
        return self

    @robot_alias("Remove__product__from__basket")
    def delete_product(self):
        self.click_element("delete from basket")
        self.body_should_contain_text('Your basket is empty.', 'Selected product was not deleted from basket')
        return self

    def select_product(self):
        self.click_element("all products")
        self.click_element("search filters")
        self.click_element("availability filter")
        self.click_element("availiable product")
        self.click_element("search filters")
        self.click_element(("prescription filter"))
        self.click_element("no prescription")
        products_list= self.find_element("list of products")
        products= products_list.find_elements_by_tag_name("article")
        product= choice(products)
        return product

    def product_name(self, product_locator):
        pr_name= product_locator.find_element_by_tag_name('h3')
        product_name= self.get_text(pr_name)
        return product_name


    @robot_alias("Add__an__animal")
    def add_animal(self):
        self.click_element("health center")
        self.click_element("animals")
        self.click_element("add animal")
        self.type_in_box('Ivanka', 'id=id_name')
        self.select_from_dropdown("species", "species list", "selected species")
        self.select_from_dropdown("breed", "breed list", "selected breed")
        self.type_in_box('20',"id=id_weight")
        self.specify_invalid_date()
        self.type_date_of_birth(str(datetime.now().day),
            str(datetime.now().month),
            str(datetime.now().year))
        self.type_in_box(self.gen_password(), "id=id_identification_number")
        self.select_from_dropdown("sex", "sex list", "id=select2-chosen-3")
        self.answer_questions()
        self.click_button("id=save-button")
        self.click_element("all animals")
        self.body_should_contain_text('Ivanka', 'The animal was not added')
        return self

    @robot_alias("Create__a__group")
    def create_group(self):
        self.click_element("xpath=(//a[contains(text(),'My groups')])")
        self.click_element("xpath=(//a[@class='btn btn-lg btn-info add-group-button button_site_style'])")
        self.type_in_box('Quintagroup', 'id=id_name')
        self.click_element("id=s2id_id_species")
        for element in self.find_element("xpath=(//input[@class='select2-input select2-focused])"):
            self.type_in_box('12', "id=id_number_of_animals")
            self.click_element("xpath=(//i[@class='fa fa-plus'])")
        animal_block=self.find_element("xpath=(//div[@class='animals-container container'])")
        list_of_animals=animal_block.find_elements_by_tag_name("img")
        animal= choice(list_of_animals)
        self.click_element(animal)
        self.click_element("xpath=(//div[@class='modal-header'])//i[@class='fa fa-times']")
        self.click_element("id=save-button")
        self.body_should_contain_text('Quintagroup', 'The group was not created')
        return self

    @robot_alias("Delete__the__group")
    def delete_group(self):
        self.click_element("xpath=(//a[contains(text(),'Quintagroup')])")
        self.click_element("xpath=(//div[@class='delete-group']//i[@class='fa fa-times'])")
        self.is_visible("xpath=(//button[@class='btn btn-danger'])")
        self.click_element("xpath=(//button[@class='btn btn-danger'])")
        body_txt = self.get_text("css=body").encode("utf-8").lower()
        asserts.assert_false('quintagroup' in body_txt, 'The group was not deleted')
        return self


    @robot_alias("Delete__the__animal")
    def delete_animal(self):
        self.click_element("xpath=(//span[contains(text(),'Ivanka')])")
        self.click_element("xpath=(//*[@id='profile']/div/div/a)")
        sleep(5)
        self.is_visible("xpath=(//button[@class='btn btn-danger'])")
        self.click_element("xpath=(//button[@class='btn btn-danger'])")
        body_txt = self.get_text("css=body").encode("utf-8").lower()
        asserts.assert_false('ivanka' in body_txt, 'The animal was not deleted')
        return self


    @robot_alias("Add__the__prescription")
    def add_prescription(self):
        self.click_element("my prescriptions")
        self.click_element("add prescription")
        self.type_in_box('Best prescription', "prescription title")
        self.fill_in_prescription_form("prescription date", "calendar", "td")
        self.fill_in_prescription_form("add animals", "list of animals", "img", "select animal")
        self.fill_in_prescription_form("add veterinarian", "list of vets", "i", "select veterinarian")
        self.click_element("add products")
        self.type_in_box('food for mature dog', "search field")
        self.fill_in_prescription_form("search products","products list", "i","select product")
        self.click_element("save prescription")
        self.body_should_contain_text('A scan or photo of your prescription is required', 
            'Prescription was created without attached photo')
        return self


    def fill_in_prescription_form(self, add_btn, items, tag, close_btn=None):
        self.click_element(add_btn)
        info_block= self.find_elements(items)
        list_of_items=info_block[0].find_elements_by_tag_name(tag)
        item=choice(list_of_items)
        self.click_element(item)
        if close_btn is not None:
            self.click_element(close_btn)
            self.body_should_contain_text(self.get_text(item),
            'Required information was not added to prescription')
        sleep(3)
        return self

    def specify_invalid_date(self):
        self.date_validation('32',str(datetime.now().month), str(datetime.now().year))
        self.date_validation(str(datetime.now().day), '13', str(datetime.now().year))
        self.date_validation(str(datetime.now().day), str(datetime.now().month), '3954')
        return self 


    def date_validation(self, day, month, year):
        self.type_date_of_birth(day, month, year)
        self.click_button("id=save-button")
        self.body_should_contain_text('Date is incorrect! Example: 01/01/2017', 'dfs')
        return self

    def type_date_of_birth(self, day, month, year):
        self.type_in_box(day,"id=id_date_of_birth")
        self.type_in_box(month, "id=birth-month")
        self.type_in_box(year,"id=birth-year")
        return self


    def select_from_dropdown(self, menu_arrow, dropdown_variants, field):
        self.click_element(menu_arrow)
        dropdown_menu = self.find_element(dropdown_variants)
        element = dropdown_menu.find_elements_by_tag_name("li")
        selected_element=choice(element)
        a= self.get_text(selected_element)
        self.click_element(selected_element)
        asserts.assert_true(a in self.get_text(field), 'Value was not selected')
        return self

    def answer_questions(self):
        questions_list = self.find_element("questions list")
        questions = questions_list.find_elements_by_tag_name("div")
        for question in questions[1:5]:
            answer = question.find_elements_by_tag_name("label")
            self.click_element(choice(answer))
        return self
