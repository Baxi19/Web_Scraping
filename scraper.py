import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def parse():
    url = 'https://store.playstation.com/es-cr/category/44d8bb20-653e-431e-8ad0-c0a365f68d2f'
    result = requests.get(url)

    print(result.status_code)  # Devuelve el status code de la web if 200 ok.

    # print(result.text)            #Imprime el texto de la página (a veces no requerimos texto)
    # print(result.content)         #Devuelve el contenido en bytes
    # print(result.headers)         #Devuelve los headers
    # print(result.request.headers) #Devuelve los headers del request, aquí vemos que python hace peticiones, más adelante aprenderemos a ocultarlo.
    # print(result.request.method)  #Devuelve el método de request (get en este caso)
    # print(result.request.url)     #Devuelve la url a la que se le hace petición. Es útil cuando hay redirecciones
    soup = BeautifulSoup(result.text, 'lxml')
    """
    # print(soup.prettify())
    sections = soup.find('ul', attrs={
        'class': 'ems-sdk-product-tile-list psw-grid-x psw-grid-margin-x psw-mobile-p-up-2 psw-tablet-p-up-4 psw-tablet-l-up-6 psw-hd-up-8'
                }).find_all('li', attrs={
                    'class':'psw-cell'
                    })
    """

    #Selenium
    options =webdriver.ChromeOptions()
    options.add_argument('--incognito')
    
    driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
    driver.get(url)
    games = driver.find_elements_by_xpath('/html/body/div[3]/main/section/div/div/ul/li')
    
    time.sleep(2)
    cont = 1
    for item in games:
        print("\n==========================================================================================================")
        print(cont)
        cont += 1

        # url
        game_url = item.find_element_by_xpath('.//div[@class="ems-sdk-product-tile"]/a/div/div/span[2]/img').get_attribute('src')
        modify_url = game_url.split(sep="?")
        
        # name
        game_name = item.find_element_by_xpath('.//section[@class="ems-sdk-product-tile__details"]/span').text
        game_price = ""
        # price
        try:
            game_price = item.find_element_by_xpath('.//section[@class="ems-sdk-product-tile__details"]/div[2]/span').text
        except:
            game_price = item.find_element_by_xpath('.//section[@class="ems-sdk-product-tile__details"]/div[1]/span').text

        print(modify_url[0])
        print(game_name)
        print(game_price)
        

    driver.close()

def run():
    parse()


if __name__ == "__main__":
    run()
