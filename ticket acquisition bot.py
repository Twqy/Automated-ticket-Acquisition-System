from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import NoSuchElementException

# Define number of tickets
TICKET_COUNT = 7  # Change this based on how many tickets you want

#Ticket Purchase Details
FNAME = "name"
LNAME = "here"
FULLNAME = FNAME + " " + LNAME
PEMAIL = "namehere@gmail.com"
POSTAL_CODE = "K1S 2R8"
CREDIT_CARD_NUMBER = "1234123412341234"
CREDIT_CARD_EXPIRY = "1126" #put it in mmyy format
CREDIT_CARD_CVV = "123"

# Initialize Chrome driver properly
service = Service(ChromeDriverManager().install())
driver = wd.Chrome(service=service)

#driver.get("https://wusa.ca/event/midnight-social-lucky-after-dark/")
driver.get("https://wusa.ca/event/lucky-tu-lucky-me/#tribe-tickets__tickets-form")

ticket_item = 0
for i in range(150470, 160000):
    try:
        # Attempt to find the element using the dynamic ID
        increase_tickets = driver.find_element(By.XPATH, f'//*[@id="tribe-block-tickets-item-{i}"]/div[3]/div/div/input[3]')
        print(f"Found ticket item: tribe-block-tickets-item-{i}")
        ticket_item = i
        break  # Exit loop once the element is found and interacted with
    except NoSuchElementException:
        # If element is not found, move on to the next number
        continue

for i in range(TICKET_COUNT):
    increase_tickets.click()

get_tickets = driver.find_element(By.XPATH, '//*[@id="tribe-tickets__tickets-submit"]')
get_tickets.click()

p1_name = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_tribe-tickets-plus-iac-name_1"]')
p1_email = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_tribe-tickets-plus-iac-email_1"]')
p1_waiver = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_waiver-form_1"]')

p1_name.send_keys(FULLNAME)
p1_email.send_keys(PEMAIL)
select = Select(p1_waiver)
select.select_by_visible_text("By checking this box, I confirm I have filled out the above waiver and may not be admitted to the event if I have not filled it out. You will be emailed a confirmation of your submission.")

if (TICKET_COUNT > 1):
    p2_name = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_tribe-tickets-plus-iac-name_2"]')
    p2_email = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_tribe-tickets-plus-iac-email_2"]')
    p2_waiver = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_waiver-form_2"]')

    p3_name = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_tribe-tickets-plus-iac-name_3"]')
    p3_email = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_tribe-tickets-plus-iac-email_3"]')
    p3_waiver = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_waiver-form_3"]')

    p4_name = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_tribe-tickets-plus-iac-name_4"]')
    p4_email = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_tribe-tickets-plus-iac-email_4"]')
    p4_waiver = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_waiver-form_4"]')

    p5_name = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_tribe-tickets-plus-iac-name_5"]')
    p5_email = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_tribe-tickets-plus-iac-email_5"]')
    p5_waiver = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_waiver-form_5"]')

    p6_name = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_tribe-tickets-plus-iac-name_6"]')
    p6_email = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_tribe-tickets-plus-iac-email_6"]')
    p6_waiver = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_waiver-form_6"]')

    p7_name = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_tribe-tickets-plus-iac-name_7"]')
    p7_email = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_tribe-tickets-plus-iac-email_7"]')
    p7_waiver = driver.find_element(By.XPATH, f'//*[@id="tribe-tickets_{ticket_item}_waiver-form_7"]')

    p2_name.send_keys("name here")
    p2_email.send_keys("namehere@gmail.com")
    select = Select(p2_waiver)
    select.select_by_visible_text("By checking this box, I confirm I have filled out the above waiver and may not be admitted to the event if I have not filled it out. You will be emailed a confirmation of your submission.")

    p3_name.send_keys("name here")
    p3_email.send_keys("namehere@gmail.com")
    select = Select(p3_waiver)
    select.select_by_visible_text("By checking this box, I confirm I have filled out the above waiver and may not be admitted to the event if I have not filled it out. You will be emailed a confirmation of your submission.")

    p4_name.send_keys("name here")
    p4_email.send_keys("namehere@gmail.com")
    select = Select(p4_waiver)
    select.select_by_visible_text("By checking this box, I confirm I have filled out the above waiver and may not be admitted to the event if I have not filled it out. You will be emailed a confirmation of your submission.")

    p5_name.send_keys("name here")
    p5_email.send_keys("namehere@gmail.com")
    select = Select(p5_waiver)
    select.select_by_visible_text("By checking this box, I confirm I have filled out the above waiver and may not be admitted to the event if I have not filled it out. You will be emailed a confirmation of your submission.")

    p6_name.send_keys("name here")
    p6_email.send_keys("namehere@gmail.com")
    select = Select(p6_waiver)
    select.select_by_visible_text("By checking this box, I confirm I have filled out the above waiver and may not be admitted to the event if I have not filled it out. You will be emailed a confirmation of your submission.")

    p7_name.send_keys("name here")
    p7_email.send_keys("namehere@gmail.com")
    select = Select(p7_waiver)
    select.select_by_visible_text("By checking this box, I confirm I have filled out the above waiver and may not be admitted to the event if I have not filled it out. You will be emailed a confirmation of your submission.")


checkout = driver.find_element(By.XPATH, '//*[@id="tribe-modal__attendee-registration"]/div[9]/button[2]')
checkout.click()

privacy_popup = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/a')
privacy_popup.click()

billing_fname = driver.find_element(By.XPATH, '//*[@id="billing_first_name"]')
billing_lname = driver.find_element(By.XPATH, '//*[@id="billing_last_name"]')
billing_pcode = driver.find_element(By.XPATH, '//*[@id="billing_postcode"]')
billing_email = driver.find_element(By.XPATH, '//*[@id="billing_email"]')
billing_continue = driver.find_element(By.XPATH, '//*[@id="customer_details"]/div[1]/a')


billing_fname.send_keys(FNAME)
billing_lname.send_keys(LNAME)
billing_pcode.send_keys(POSTAL_CODE)
billing_email.send_keys(PEMAIL)
billing_continue.click()

time.sleep(1)

tos_agree = driver.find_element(By.XPATH, '//*[@id="terms"]')
tos_agree.click()

place_order = driver.find_element(By.XPATH, '//*[@id="moneris_place_order"]')
place_order.click()

time.sleep(3) 

checkout_iframe = driver.find_element(By.ID, "monerisCheckout-Frame")  # Locate iframe by ID
driver.switch_to.frame(checkout_iframe)

card_holder_name = driver.find_element(By.ID, "cardholder") 
card_number = driver.find_element(By.XPATH, '//*[@id="pan"]')
card_expiry = driver.find_element(By.XPATH, '//*[@id="expiry_date"]')
card_cvv = driver.find_element(By.XPATH, '//*[@id="cvv"]')
final_checkout = driver.find_element(By.XPATH, '//*[@id="process"]')

card_holder_name.send_keys(FULLNAME)
card_number.send_keys(CREDIT_CARD_NUMBER)
card_expiry.send_keys(CREDIT_CARD_EXPIRY)
card_cvv.send_keys(CREDIT_CARD_CVV)
final_checkout.click()

input("Press Enter to close the browser...")

driver.quit()
