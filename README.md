# Task_30.5.1_-HW-04-

Автоматизированное тестирование API Petfriends


В репозитории представлено решение двух заданий

В ходе выполнения заданий было составлено 4 теста:

1.test_show_my_pets - Этот тест проверяет, что на сайте присутствуют все питомцы пользователя

2.test_photo_pets - Этот тест проверяет, что у более половины питомцев есть фотографии

3.test_allpet_have_name_breed_age - Этот тест проверяет, что все питомцы содержат данные имя, возраст, породу, и нет двух питомцев с одинаковым именем

4.test_not_pet_same_name_breed_age - Этот тест проверяет, что  нет двух питомцев с одинаковым именем, возрастом и породой, то есть нет двойников:)

Для элементов поиска были применены методы явных и неявных ожиданий. 

Для фиксации проваленных тестов была применена функция записи скриншотов



Задание 30.5.1.

В написанном тесте (проверка карточек питомцев) добавьте неявные ожидания всех элементов (фото, имя питомца, его возраст).

В написанном тесте (проверка таблицы питомцев) добавьте явные ожидания элементов страницы.

 Задание 30.3.1
 
Написать тест, который проверяет, что на странице со списком питомцев пользователя:


Присутствуют все питомцы.

Хотя бы у половины питомцев есть фото.

У всех питомцев есть имя, возраст и порода.

У всех питомцев разные имена.

В списке нет повторяющихся питомцев. (Сложное задание).

Вопросы для самопроверки

Количество строк таблицы соответствует количеству питомцев в блоке статистики пользователя?

При изменении количества проверяемых строк таблицы тест из задания 1 падает?

Половина от чётного и нечётного количества фотографий выдаёт одинаковые результаты теста?

При добавлении питомца с повторяющимся именем все тесты проходят?

При добавлении питомца с повторяющимся именем, породой или возрастом все тесты проходят?
