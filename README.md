# Тестовое задание на траекторию "Ручное и автоматизированное тестирование"

Для решения задач использовались: Python, Selenium, Pytest

Также для запуска тестов необходим драйвер, в частности, я использую для Chrome, представлено в [папке](https://github.com/MarinaVasilevaIVT/nexign_test_exercise/edit/main/chromedriver) 

В файле conftest.py содержится конфигурация тестов с запуском вебдрайвера Chrome и его закрытием после того, как тест выполнился.

В файле test_1.py представлено решение для первого задания, в котором с помощью Selenium была проведена имитация кликов по необходимым вкладкам и проверка того, что мы перешли на нужную вкладку.

В файле test_2.py представлено решение для второго задания, в котором с помощью Selenium были собраны все слова с страницы и подсчитано общее количество упоминаний слова "Nexign". Ответ - 32. 

В файле test_3.py представлено решение для второго задания, в котором
