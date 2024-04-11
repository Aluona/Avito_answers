Bug-report
1. Summary:
На странице экосчетчиков в циклически воспроизводимом видео для подсчета сохраненной воды дублируется слово "воды".

2. Precondition: 
Перейти на страницу экосчетчиков Avito: https://www.avito.ru/avito-care/eco-impact?from=avito-care-navigation

3. Steps to reproduce:
    1. Найти раздел со счетчиками, отображающими информацию об общем эковкладе пользователей Avito.
    2. Найти циклически воспроизводимое видео для подсчета сохраненной воды. 

4. Expected result: 
В счетчике содержится 2 строки: 
- первая строка - числовое значение сохраненного объема воды и единица измерения;
- вторая строка - текст "воды было сохранено".

5. Actual result:
Слово "воды"  присутствует как в первой, так и во второй строке.

6. Environment: 
Prod, macOS Sonoma Version 14.4.1, Google Chrome, Version 123.0.6312.106

7. Severity: Trivial

8. Attachments: 
https://drive.google.com/file/d/1mk2JX9Spr7DwTf6w7wh_XnSHSMFPowsb/view?usp=sharing
