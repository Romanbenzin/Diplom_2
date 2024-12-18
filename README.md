# Diplom_2
Проект по api тестам

# Документация проекта
https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89

# Запуск тестов:
pytest tests/ --alluredir=allure-results

# Посмотреть результат в allure
allure serve allure_results

# Если тесты не запускаются на Windows через консоль:
$env:PYTHONPATH="."; pytest tests/ --alluredir=allure-results -v

# Посмотреть allure отчет на windows
allure generate allure-results -o allure-report --clean
allure open allure-report

# urls.py
url'ы для запросов к API

# data.py
Статические данные

# helpers.py
Небольшие функции, которые помогают в тестах

# requirements
Внешние зависимости