# Настройка окружения для запуска тестов

Для работы тестов нам понадобится несколько пакетов:
* git - для работы с репозиторием
* curl - для скачивания скрипта установки pyenv
* [pyenv](https://github.com/pyenv/pyenv) - для управления версиями Python
* Python версии 3.11 - язык программирования, на котором написаны тесты
* [Playwright for Python](https://playwright.dev/python/) - тестовый фреймворк

## Linux

Приведенные команды работают для Ubuntu 20.04. 

1. Установи необходимые зависимости, выполнив команды в терминале
```
sudo apt update
sudo apt install curl -y
sudo apt install git -y
```
2. Установи pyenv. [Подробнее](https://itslinuxfoss.com/install-use-pyenv-ubuntu/) о процессе установки
```
curl https://pyenv.run | bash
export PATH="$HOME/.pyenv/bin:$PATH" && eval "$(pyenv init --path)" && echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
exec $SHELL
```
Убедись, что pyenv установлен, выполнив:
```
pyenv --version
```

3. Установи Python версии 3.11 и переключись на нее, чтобы использовать по умолчанию для всех проектов. [Подробнее о работе pyenv](https://github.com/pyenv/pyenv)
```
pyenv install 3.11.0
pyenv global 3.11.0
```

4. Установи тестовый фреймворк:
```
pip install pytest-playwright
```

5. Установи браузеры
```
playwright install
```

6. Скачай репозиторий с тестами в нужную тебе директорию (в нашем случае это будет папка Home)
```
cd ~
git clone <репозиторий с тестами>
cd <директория с тестами>
```

7. Запусти тест
```
pytest <путь к файлу с тестом>
```
Для запуска теста с графическим интерфейсом браузера выполни команду с --headed аргументом.
```
pytest --headed <путь к файлу с тестом> 
```
