from bs4 import BeautifulSoup
import requests
import sqlite3

#create/create a database
conn=sqlite3.connect('udemy_faq.db')
print('database created for udemy_faq.db')
sql=""" 
    CREATE TABLE IF NOT EXISTS faq_table(
        question uniTEXT NOT NULL,
        answer TEXT NOT NULL,
        get_url TEXT NOT NULL
    );
    """
cursor = conn.cursor()
# cursor.execute(sql)

print("Table connected")



udemy_page=requests.get('https://www.udemy.com/topic/python/')
# print(udemy_page)
soup = BeautifulSoup(udemy_page.text, 'lxml')
heading = soup.find_all('div', class_='panel--panel--3uDOH')
# print(heading)
for head in heading:
    question=head.find('span', class_='udlite-accordion-panel-title').text
    answer=head.find('div', class_='udlite-text-sm questions-and-answers--answer--2PMFk').text
    url = head.find(href=True)
    get_url=url['href']


    # print(question.text)
    # print(answer.text)
    # print(get_url)
    # print(url)

    sql = """INSERT INTO faq_table
                    (question, answer, get_url)
                    VALUES ("{}","{}","{}");""".format(question, answer, get_url)
    # print(sql)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit() 
print("Data is Inserted into faq_table...")
# cursor.close()
conn.close()
print("connection closed")