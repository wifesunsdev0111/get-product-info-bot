from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import *
from time import sleep
import re
import db


def scroll_down(driv):
    page_height = driv.execute_script("return document.body.scrollHeight")
    driv.execute_script(f"window.scrollTo(0, {page_height});")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://zilanofficial.ro/produse/aparate-din-bucatarie/")

WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[class=\"product-categories\"]")))

ul_element = driver.find_element(By.CSS_SELECTOR, "ul[class=\"product-categories\"]")
li_elements = ul_element.find_elements(By.XPATH, './*')

all_main_urls = []
for li_element in li_elements:
    all_main_urls.append(li_element.find_element(By.TAG_NAME, "a").get_attribute("href"))

for main_url in all_main_urls:
    driver.get(main_url)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[class=\"product-categories\"]")))

    initial_url = driver.current_url

    while(True):
        product_elements = driver.find_elements(By.CSS_SELECTOR, "div[class=\"product-wrapper\"]")
        product_count = len(product_elements)
        print(product_count)
        
        scroll_down(driver)
        sleep(3)
        print(driver.current_url)
        if initial_url == driver.current_url:
            break
        initial_url = driver.current_url

    print(product_count)

    product_driver = webdriver.Chrome()
    product_driver.maximize_window()

    product_elements = driver.find_elements(By.CSS_SELECTOR, "div[class=\"product-wrapper\"]")
    print(len(product_elements))
    for product_element in product_elements:
        product_url = product_element.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
        print(product_url)

        product_driver.get(product_url)

        WebDriverWait(product_driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span[class=\"sku\"]")))

        sku = product_driver.find_element(By.CSS_SELECTOR, "span[class=\"sku\"]").text
        print(f"SKU: {sku}")
        title_text = product_driver.find_element(By.CSS_SELECTOR, "h1[class=\"product_title entry-title wd-entities-title\"]").text
        title = title_text
        # title = title_text[:title_text.find(',')]
        print(f"Title: {title}")
        short_description = title_text[title_text.find(',') + 2:title_text.rfind('/')]
        print(f"Short Description: {short_description}")
        description = product_driver.find_element(By.CSS_SELECTOR, "div[class=\"wc-tab-inner\"]").text[10:]
        print(f"Description: {description}")
        stock_text = product_driver.find_element(By.CSS_SELECTOR, "meta[property=\"product:availability\"]").get_attribute('content')
        stock = 0
        if stock_text == "instock":
            stock = 1
        print(f"Stock: {stock}")

        weight = ""
        length = ""
        width = ""
        height = ""

        lines = description.splitlines()

        for line in lines:
            print(line)
            if "Greutate" == line:
                weight = line.replace("Greutate", "").strip()
            if "Inaltime" == line:
                height = line.replace("Inaltime", "").strip()
            if "Lungime" == line:
                length = line.replace("Lungime", "").strip()
            if "Latime" == line:
                width = line.replace("Latime", "").strip()
            if "Diametru suprafata gatire" in line:
                length = re.findall(r'\d+ cm', line)[0]
                width = length

        
        attribute_1_name = attribute_1_value = ""
        attribute_2_name = attribute_2_value = ""
        attribute_3_name = attribute_3_value = ""
        attribute_4_name = attribute_4_value = ""
        attribute_5_name = attribute_5_value = ""
        attribute_6_name = attribute_6_value = ""
        attribute_7_name = attribute_7_value = ""
        attribute_8_name = attribute_8_value = ""
        attribute_9_name = attribute_9_value = ""
        attribute_10_name = attribute_10_value = ""
        attribute_11_name = attribute_11_value = ""
        attribute_12_name = attribute_12_value = ""
        attribute_13_name = attribute_13_value = ""
        attribute_14_name = attribute_14_value = ""
        attribute_15_name = attribute_15_value = ""
        attribute_16_name = attribute_16_value = ""
        attribute_17_name = attribute_17_value = ""
        attribute_18_name = attribute_18_value = ""
        attribute_19_name = attribute_19_value = ""
        attribute_20_name = attribute_20_value = ""
        attribute_21_name = attribute_21_value = ""
        attribute_22_name = attribute_22_value = ""
        attribute_23_name = attribute_23_value = ""
        attribute_24_name = attribute_24_value = ""

        attribute_1_visibility = attribute_1_global = ""
        attribute_2_visibility = attribute_2_global = ""
        attribute_3_visibility = attribute_3_global = ""
        attribute_4_visibility = attribute_4_global = ""
        attribute_5_visibility = attribute_5_global = ""
        attribute_6_visibility = attribute_6_global = ""
        attribute_7_visibility = attribute_7_global = ""
        attribute_8_visibility = attribute_8_global = ""
        attribute_9_visibility = attribute_9_global = ""
        attribute_10_visibility = attribute_10_global = ""
        attribute_11_visibility = attribute_11_global = ""
        attribute_12_visibility = attribute_12_global = ""
        attribute_13_visibility = attribute_13_global = ""
        attribute_14_visibility = attribute_14_global = ""
        attribute_15_visibility = attribute_15_global = ""
        attribute_16_visibility = attribute_16_global = ""
        attribute_17_visibility = attribute_17_global = ""
        attribute_18_visibility = attribute_18_global = ""
        attribute_19_visibility = attribute_19_global = ""
        attribute_20_visibility = attribute_20_global = ""
        attribute_21_visibility = attribute_21_global = ""
        attribute_22_visibility = attribute_22_global = ""
        attribute_23_visibility = attribute_23_global = ""
        attribute_24_visibility = attribute_24_global = ""

        attribute_name_array = []
        attribute_value_array = []

        additional_infromation = product_driver.find_element(By.CSS_SELECTOR, "div[class=\"wc-tab-inner\"]")
        all_table_tr = additional_infromation.find_elements(By.TAG_NAME, "tr")
        if len(all_table_tr) != 0:
            try:
                index = 0
                attribute_name_array = []
                attribute_value_array = []
                for _ in range(len(all_table_tr)):
                    print(f'{all_table_tr[index].find_elements(By.TAG_NAME, "td")[0].text} : {all_table_tr[index].find_elements(By.TAG_NAME, "td")[1].text}')
                    attribute_name_array.append(all_table_tr[index].find_elements(By.TAG_NAME, "td")[0].text)
                    attribute_value_array.append(all_table_tr[index].find_elements(By.TAG_NAME, "td")[1].text)
                    index += 1
                index = 0
                for _ in range(24 - len(attribute_name_array)):
                    attribute_name_array.append("")
                    attribute_value_array.append("")
                    index += 1
            except:
                pass

        try:
            additional_infor_tab = product_driver.find_element(By.CSS_SELECTOR, "li[class=\"additional_information_tab\"]")
            additional_infor_tab.click()

            additional_infromation = product_driver.find_elements(By.CSS_SELECTOR, "div[class=\"wc-tab-inner\"]")[1]
            all_table_th = additional_infromation.find_elements(By.TAG_NAME, "th")
            all_table_td = additional_infromation.find_elements(By.TAG_NAME, "td")
            index = 0
            attribute_name_array = []
            attribute_value_array = []
            for _ in range(len(all_table_th)):
                print(f"{all_table_th[index].text} : {all_table_td[index].text}")
                attribute_name_array.append(all_table_th[index].text)
                attribute_value_array.append(all_table_td[index].text)
                index += 1
            index = 0
            for _ in range(24 - len(attribute_name_array)):
                attribute_name_array.append("")
                attribute_value_array.append("")
                index += 1

            index = 0
            for _ in range(len(attribute_name_array)):
                if "Greutate" == attribute_name_array[index]:
                    weight = attribute_value_array[index]
                if "Inaltime" == attribute_name_array[index]:
                    height = attribute_value_array[index]
                if "Lungime" == attribute_name_array[index]:
                    length = attribute_value_array[index]
                if "Latime" == attribute_name_array[index]:
                    width = attribute_value_array[index]
                index += 1

        except:
            pass

        try:
            attribute_1_name = attribute_name_array[0]
            attribute_1_value = attribute_value_array[0]
            if attribute_1_value != "":
                attribute_1_visibility = attribute_1_global = 1
            attribute_2_name = attribute_name_array[1]
            attribute_2_value = attribute_value_array[1]
            if attribute_2_value != "":
                attribute_2_visibility = attribute_2_global = 1
            attribute_3_name = attribute_name_array[2]
            attribute_3_value = attribute_value_array[2]
            if attribute_3_value != "":
                attribute_3_visibility = attribute_3_global = 1
            attribute_4_name = attribute_name_array[3]
            attribute_4_value = attribute_value_array[3]
            if attribute_4_value != "":
                  attribute_4_visibility = attribute_4_global = 1
            attribute_5_name = attribute_name_array[4]
            attribute_5_value = attribute_value_array[4]
            if attribute_5_value != "":
                attribute_5_visibility = attribute_5_global = 1
            attribute_6_name = attribute_name_array[5]
            attribute_6_value = attribute_value_array[5]
            if attribute_6_value != "":
                attribute_6_visibility = attribute_6_global = 1
            attribute_7_name = attribute_name_array[6]
            attribute_7_value = attribute_value_array[6]
            if attribute_7_value != "":
                attribute_7_visibility = attribute_7_global = 1
            attribute_8_name = attribute_name_array[7]
            attribute_8_value = attribute_value_array[7]
            if attribute_8_value != "":
                attribute_8_visibility = attribute_8_global = 1
            attribute_9_name = attribute_name_array[8]
            attribute_9_value = attribute_value_array[8]
            if attribute_9_value != "":
                attribute_9_visibility = attribute_9_global = 1
            attribute_10_name = attribute_name_array[9]
            attribute_10_value = attribute_value_array[9]
            if attribute_10_value != "":
                attribute_10_visibility = attribute_10_global = 1
            attribute_11_name = attribute_name_array[10]
            attribute_11_value = attribute_value_array[10]
            if attribute_11_value != "":
                attribute_11_visibility = attribute_11_global = 1
            attribute_12_name = attribute_name_array[11]
            attribute_12_value = attribute_value_array[11]
            if attribute_12_value != "":
                attribute_12_visibility = attribute_12_global = 1
            attribute_13_name = attribute_name_array[12]
            attribute_13_value = attribute_value_array[12]
            if attribute_13_value != "":
                attribute_13_visibility = attribute_13_global = 1
            attribute_14_name = attribute_name_array[13]
            attribute_14_value = attribute_value_array[13]
            if attribute_14_value != "":
                attribute_14_visibility = attribute_14_global = 1
            attribute_15_name = attribute_name_array[14]
            attribute_15_value = attribute_value_array[14]
            if attribute_15_value != "":
                attribute_15_visibility = attribute_15_global = 1
            attribute_16_name = attribute_name_array[15]
            attribute_16_value = attribute_value_array[15]
            if attribute_16_value != "":
                attribute_16_visibility = attribute_16_global = 1
            attribute_17_name = attribute_name_array[16]
            attribute_17_value = attribute_value_array[16]
            if attribute_17_value != "":
                attribute_17_visibility = attribute_17_global = 1
            attribute_18_name = attribute_name_array[17]
            attribute_18_value = attribute_value_array[17]
            if attribute_18_value != "":
                attribute_18_visibility = attribute_18_global = 1
            attribute_19_name = attribute_name_array[18]
            attribute_19_value = attribute_value_array[18]
            if attribute_19_value != "":
                attribute_19_visibility = attribute_19_global = 1
            attribute_20_name = attribute_name_array[19]
            attribute_20_value = attribute_value_array[19]
            if attribute_20_value != "":
                attribute_20_visibility = attribute_20_global = 1
            attribute_21_name = attribute_name_array[20]
            attribute_21_value = attribute_value_array[20]
            if attribute_21_value != "":
                attribute_21_visibility = attribute_21_global = 1
            attribute_22_name = attribute_name_array[21]
            attribute_22_value = attribute_value_array[21]
            if attribute_22_value != "":
                attribute_22_visibility = attribute_22_global = 1
            attribute_23_name = attribute_name_array[22]
            attribute_23_value = attribute_value_array[22]
            if attribute_23_value != "":
                attribute_23_visibility = attribute_23_global = 1
            attribute_24_name = attribute_name_array[23]
            attribute_24_value = attribute_value_array[23]
            if attribute_24_value != "":
                attribute_24_visibility = attribute_24_global = 1
        except:
            pass
                
        print(f"Weight: {weight}")
        print(f"Length: {length}")
        print(f"Width: {width}")
        print(f"Height: {height}")


        price = product_driver.find_element(By.CSS_SELECTOR, "p[class=\"price\"]").text
        sale_price = price.split(" ")[1]
        print(f"Sale price: {sale_price}")
        regular_price = price.split(" ")[0]
        print(f"Regular price: {regular_price}")

        categories_parent_element = product_driver.find_element(By.CSS_SELECTOR, "div[class=\"wd-breadcrumbs\"]")
        categories_element = categories_parent_element.find_elements(By.TAG_NAME, "a")
        categories_element = categories_element[1:]
        categories = ""
        for category_element in categories_element:
            categories += (category_element.text + " > ")
        categories = categories[:-3]
        print(f"Categories: {categories}")


        image_array = []
        thumb_nail_images_elements = product_driver.find_elements(By.CLASS_NAME, "product-image-thumbnail.slick-slide")
        for thumb_nail_images_element in thumb_nail_images_elements:
            image_array.append(thumb_nail_images_element.find_element(By.TAG_NAME, "img").get_attribute('src').replace("-150x150", ""))

        images = ', '.join(image_array)
        print(f"Images: {images}")

        db.insert_data(
                sku, title, short_description, description, stock, weight, length, width, height, sale_price, regular_price, categories, images, product_driver.current_url,
                attribute_1_name, attribute_1_value, attribute_1_visibility, attribute_1_global,
                attribute_2_name, attribute_2_value, attribute_2_visibility, attribute_2_global,
                attribute_3_name, attribute_3_value, attribute_3_visibility, attribute_3_global,
                attribute_4_name, attribute_4_value, attribute_4_visibility, attribute_4_global,
                attribute_5_name, attribute_5_value, attribute_5_visibility, attribute_5_global,
                attribute_6_name, attribute_6_value, attribute_6_visibility, attribute_6_global,
                attribute_7_name, attribute_7_value, attribute_7_visibility, attribute_7_global,
                attribute_8_name, attribute_8_value, attribute_8_visibility, attribute_8_global,
                attribute_9_name, attribute_9_value, attribute_9_visibility, attribute_9_global,
                attribute_10_name, attribute_10_value, attribute_10_visibility, attribute_10_global,
                attribute_11_name, attribute_11_value, attribute_11_visibility, attribute_11_global,
                attribute_12_name, attribute_12_value, attribute_12_visibility, attribute_12_global,
                attribute_13_name, attribute_13_value, attribute_13_visibility, attribute_13_global,
                attribute_14_name, attribute_14_value, attribute_14_visibility, attribute_14_global,
                attribute_15_name, attribute_15_value, attribute_15_visibility, attribute_15_global,
                attribute_16_name, attribute_16_value, attribute_16_visibility, attribute_16_global,
                attribute_17_name, attribute_17_value, attribute_17_visibility, attribute_17_global,
                attribute_18_name, attribute_18_value, attribute_18_visibility, attribute_18_global,
                attribute_19_name, attribute_19_value, attribute_19_visibility, attribute_19_global,
                attribute_20_name, attribute_20_value, attribute_20_visibility, attribute_20_global,
                attribute_21_name, attribute_21_value, attribute_21_visibility, attribute_21_global,
                attribute_22_name, attribute_22_value, attribute_22_visibility, attribute_22_global,
                attribute_23_name, attribute_23_value, attribute_23_visibility, attribute_23_global,
                attribute_24_name, attribute_24_value, attribute_24_visibility, attribute_24_global
            )