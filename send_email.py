import smtplib
from os import getenv

from dotenv import load_dotenv

load_dotenv()
FROM_LOGIN_MAIL = getenv('FROM_LOGIN_MAIL')
PASSWORD_LOGIN_MAIL = getenv('PASSWORD_LOGIN_MAIL')
TO_LOGIN_MAIL = getenv('TO_LOGIN_MAIL')
site_name = 'https://dvmn.org/profession-ref-program/grachev.ro/ndYAO/'
friend_name = 'Friend'
sender_name = 'Mr.Grose'
letter_template = """
Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.

Как будет проходить ваше обучение на {website}?

→ Попрактикуешься на реальных кейсах.
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей.
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.

Регистрируйся → {website}
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""

new_letter_template = letter_template.format(website=site_name, friend_name=friend_name, my_name=sender_name)

letter = f"""\
From: {FROM_LOGIN_MAIL}
To: {TO_LOGIN_MAIL}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";
{new_letter_template}
"""

letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(FROM_LOGIN_MAIL, PASSWORD_LOGIN_MAIL)
server.sendmail(FROM_LOGIN_MAIL, TO_LOGIN_MAIL, letter)
server.quit()
