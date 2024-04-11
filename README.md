Для получения скриншотов счетчиков выполните следующие действия.
1. Скачать с github проект: https://github.com/Aluona/Avito_answers.git
2. В Terminal перейти в папку с проектом.
В случае, если виртуальное окружение Playwright не установлено, переходите к п. 3 данной инструкции. В противном случае - переходите к п. 8 данной инструкции.
3. Внутри папки с проектом создайте виртуальное окружение:
    - $ python3 -m venv venv
4. Активируйте виртуальное окружение. Для macOS используйте команду:
    -  $ source venv/bin/activate
5. Установите Python packages:
    - $ pip3 install playwright
    - $ pip3 install pytest
    - $ pip3 install pytest-playwright
6. Проверить успешность установки Python packages можно используя команду: 
    - $ pip3 freeze
7. После успешной установки Python packages установите браузеры для Playwright, используя команду:
    - $ playwright install
    
Более детальная информация по установке приведена по ссылке https://github.com/AutomationPanda/playwright-python-tutorial/blob/main/tutorial/1-getting-started.md
8. Для запуска тестов выполните одну из следующих команд:
    - $ python3 -m pytest tests --headed (для визуального отображения запуска тестов);
    - $ python3 -m pytest tests  (headless режим запуска тестов, быстрее, чем headed, но без визуального сопровождения запуска тестов).
8. Тесты успешно пройдены, если:
    - в терминале появилось сообщение "3 passed";
    - в папке output появилось 3 скриншота счетчиков.
