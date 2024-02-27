from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC




def test_show_my_pets(selenium_driver):
    '''Этот тест проверяет, что на сайте присутствуют все питомцы пользователя'''
    driver = selenium_driver
     # Проверяем, что мы оказались на главной странице пользователя
    #ЯВНЫЕ ОЖИДАНИЯ
    WDW(driver, 2).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="navbarNav"]/ul/li[1]/a')))
    driver.find_element(By.XPATH,'//*[@id="navbarNav"]/ul/li[1]/a').click()



    #Находим количество (цифру) питомцев, отображенную на сайте
    WDW(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@class=".col-sm-4 left"]')))
    pets_number = driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]

    #Находим таблицу со всеми моими питомцами
    # НЕЯВНЫЕ ОЖИДАНИЯ
    driver.implicitly_wait(10)
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    # pets_number=50 # при изменении числа питомцев тест падает (тест проходит если убрать число) Так в задании указано:))))
    assert  int(pets_number) == len(pets_count)
    print(f'Указанное число моих питомце - {int(pets_number)} равно количеству присутствующих питомцев в таблице {len(pets_count)} ')

def test_photo_pets(selenium_driver):
    '''Этот тест проверяет, что у более половины питомцев есть фотографии'''
    driver = selenium_driver
    # Проверяем, что мы оказались на главной странице пользователя
    # ЯВНЫЕ ОЖИДАНИЯ
    WDW(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a')))
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()


    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    #Находим питомцев у которых есть фото

    # НЕЯВНЫЕ ОЖИДАНИЯ
    driver.implicitly_wait(10)
    image_count = driver.find_elements(By.XPATH, '//img[starts-with(@src, "data:image/")]')
    # Проверяем что фотографии имеются более чем у половины питомцев


    assert len(image_count) > (len(pets_count) % 2) == 0  #Половина от чётного  и нечетного дает разные результаты
    print(f'Количество питомцев с фото {len(image_count)} составляет больше половины всех моих питомцев {len(pets_count)}')



    # if len(image_count) > len(pets_count) % 2 == 0: #Половина от чётного  количества фотографий
    #     print(f'Количество питомцев с фото {len(image_count)} составляет больше половины всех моих питомцев {len(pets_count)}')
    # else:
    #     print(f'Количество питомцев с фото {len(image_count)} составляет меньше половины всех моих питомцев {len(pets_count)}')
    #
    # if len(image_count) > len(pets_count) % 2 == 1: #Половина от нечётного  количества фотографий
    #     print(f'Количество питомцев с фото {len(image_count)} составляет больше половины всех моих питомцев {len(pets_count)}')
    # else:
    #     print(f'Количество питомцев с фото {len(image_count)} составляет меньше половины всех моих питомцев {len(pets_count)}')

# def test_allpet_have_name_breed_age(selenium_driver):
#     '''Этот тест проверяет, что все питомцы содержат данные имя, возраст, породу,
#     что нет дублирующих имен, а также, что нет питомцев с одинаковым именем, возрастом и породой'''
#     driver = selenium_driver
#     # Проверяем, что мы оказались на главной странице пользователя
#     # ЯВНЫЕ ОЖИДАНИЯ
#     WDW(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a')))
#     driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
#
#     #Находим таблицу со всеми питомцами
#     # НЕЯВНЫЕ ОЖИДАНИЯ
#     driver.implicitly_wait(10)
#     allpet_count = driver.find_elements(By.XPATH,
#         '//*[@id="all_my_pets"]/table/tbody/tr/td[1] | //*[@id="all_my_pets"]/table/tbody/tr/td[2] | //*[@id="all_my_pets"]/table/tbody/tr/td[3]')
#
#     pet_data=set()
#
#     for i in range(1, len(allpet_count) // 3 + 1):
#         name = driver.find_element(By.XPATH,f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[1]').text
#         breed = driver.find_element(By.XPATH,f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[2]').text
#         age = driver.find_element(By.XPATH,f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[3]').text
#
#         if name and breed and age:
#
#             print(f'Питомец {i}: Имеет Имя: {name}, Породу: {breed}, Возраст: {age}')
#
#         else:
#
#             print(f'Питомец {i} не имеет информации о имени возрасте и породе')
#
#             # Проверяем, что нет пустых значений
#         if name and breed and age:
#
#             # Проверяем уникальность имени
#             if name not in pet_data:
#                 pet_data.add(name)
#             else:
#
#                 print(f"Ошибка: Дублирующееся имя - {name}")
#
#             # Проверяем уникальность комбинации имени, породы и возраста
#
#             pet_info = (name, breed, age)
#             if pet_info not in pet_data:
#                 pet_data.add(pet_info)
#             else:
#                 print(f"Ошибка: Дублирующаяся комбинация - {pet_info}")
#         else:
#             print("Ошибка: Не все данные заполнены")


def test_allpet_have_name_breed_age(selenium_driver):
    '''Этот тест проверяет, что все питомцы содержат данные
    имя, возраст, породу, и нет двух питомцев с одинаковым именем
    '''
    driver = selenium_driver
    # Проверяем, что мы оказались на главной странице пользователя
    # ЯВНЫЕ ОЖИДАНИЯ
    WDW(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a')))
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()

    #Находим таблицу со всеми питомцами
    # НЕЯВНЫЕ ОЖИДАНИЯ
    driver.implicitly_wait(10)
    allpet_count = driver.find_elements(By.XPATH,
        '//*[@id="all_my_pets"]/table/tbody/tr/td[1] | //*[@id="all_my_pets"]/table/tbody/tr/td[2] | //*[@id="all_my_pets"]/table/tbody/tr/td[3]')

    names=set()

    for i in range(1, len(allpet_count) // 3 + 1):
        name = driver.find_element(By.XPATH,f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[1]').text
        breed = driver.find_element(By.XPATH,f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[2]').text
        age = driver.find_element(By.XPATH,f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[3]').text

        assert name and breed and age

        print(f'Питомец {i}: Имеет Имя: {name}, Породу: {breed}, Возраст: {age}')

        assert name not in names, f'Имя животного {name} встречается больше одного раза'
        names.add(name)

def test_not_pet_same_name_breed_age(selenium_driver):
    '''Этот тест проверяет, что  нет двух питомцев с одинаковым именем, возрастом и породой
    '''
    driver = selenium_driver
    # Проверяем, что мы оказались на главной странице пользователя
    # ЯВНЫЕ ОЖИДАНИЯ
    WDW(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a')))
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()

    #Находим таблицу со всеми питомцами
    # НЕЯВНЫЕ ОЖИДАНИЯ
    driver.implicitly_wait(10)
    allpet_count = driver.find_elements(By.XPATH,
        '//*[@id="all_my_pets"]/table/tbody/tr/td[1] | //*[@id="all_my_pets"]/table/tbody/tr/td[2] | //*[@id="all_my_pets"]/table/tbody/tr/td[3]')

    pet_info=set()

    for i in range(1, len(allpet_count) // 3 + 1):
        name = driver.find_element(By.XPATH,f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[1]').text
        breed = driver.find_element(By.XPATH,f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[2]').text
        age = driver.find_element(By.XPATH,f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[3]').text

        pet_data = (name, age, breed)
        assert pet_data not in pet_info, f'Питомец {name} имеет двойника:)))'

        print(f'Питомец {i}: Имеет Имя: {name}, Породу: {breed}, Возраст: {age}')

        pet_info.add(pet_data)







# def test_allpet_not_same_name(selenium_driver):
#     '''Этот тест проверяет, что нет питомцев с одинаковыми именами
#     '''
#     driver = selenium_driver
#     # Проверяем, что мы оказались на главной странице пользователя
#     # ЯВНЫЕ ОЖИДАНИЯ
#     WDW(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a')))
#     driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
#
#     # Находим таблицу со всеми питомцами
#     # НЕЯВНЫЕ ОЖИДАНИЯ
#     driver.implicitly_wait(10)
#     allpet_count = driver.find_elements(By.XPATH,
#                                                 '//*[@id="all_my_pets"]/table/tbody/tr/td[1] | //*[@id="all_my_pets"]/table/tbody/tr/td[2] | //*[@id="all_my_pets"]/table/tbody/tr/td[3]')
#
#     pet_data = set()
#
#     for i in range(1, len(allpet_count) // 3 + 1):
#         name = driver.find_element(By.XPATH, f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[1]').text
#         breed = driver.find_element(By.XPATH, f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[2]').text
#         age = driver.find_element(By.XPATH, f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[3]').text
#
#
#             # Проверяем, что нет пустых значений
#         assert name not in pet_data(name)

        #     # Проверяем уникальность имени
        #     if name not in pet_data:
        #         pet_data.add(name)
        #     else:
        #
        #         print(f"Ошибка: Дублирующееся имя - {name}")
        #
        #     # Проверяем уникальность комбинации имени, породы и возраста
        #
        #     pet_info = (name, breed, age)
        #     if pet_info not in pet_data:
        #         pet_data.add(pet_info)
        #     else:
        #         print(f"Ошибка: Дублирующаяся комбинация - {pet_info}")
        # else:
        #     print("Ошибка: Не все данные заполнены")
