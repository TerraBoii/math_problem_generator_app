___
- [Установка](#установка)
    - [Windows](#windows)
    - [Linux](#linux)
- [Генератор задач по математике](#генератор-задач-по-математике)
    - [Описание:](#описание)
  - [В данные момент работаю над:](#в-данные-момент-работаю-над)
- [Основные проблемы](#основные-проблемы)

___


# Установка
### Windows

1. Перейти в папку `app_installer` на главной странице проекта
2. Нажать на `mathproblemgenerator_setup.exe`
3. Нажать на кнопку `Download` или `Скачать`
4. После скачивания запустить установленный файл
5. Продолжить установку выбирая необходимые опции
6. После окончания установки приложение само запустится или придется найти его на рабочем столе, меню пуск или папке, куда оно было утановлено и запустить его (Требуемый файл `Math problem generator app.exe` or `Math problem generator launcher.exe`)

### Linux
На данный момент работаю над этим. Но пока можно сделать так в консоле: \
SSH:
```sh
git clone git@github.com:TerraBoii/math_problem_generator_app.git
cd math_problem_generator_app
python main_app.py
```
HTTPS
```sh
git clone https://github.com/TerraBoii/math_problem_generator_app.git
cd math_problem_generator_app
python main_app.py
```

<p align="right">(<a href="#top" title="to the top of the page">back to top</a>)</p>


# Генератор задач по математике
### Описание:
Данное приложение генерирует определённые задачи по математике. Задачки имеют уникальный номер, при помощи которого можно будет получить к ним доступ в любое время и прорешать их сколько угодно раз.

## В данные момент работаю над:
- Квадратными уравнениями
- Возвращением к задачи, используя её номер
- Авто обновлениями
- Поддержкой на линуксе
- Улучшением дизайна
  - Увеличением количества условий для задач


<p align="right">(<a href="#top" title="to the top of the page">back to top</a>)</p>


# Основные проблемы
+ Текст условий задач мал по сравнению с полноэкранным окном приложения
+ версии до `0.6.1` могут иметь трудности в обновлении, особенно до `0.5` (Не может быть исправлено)


<p align="right">(<a href="#top" title="to the top of the page">back to top</a>)</p>