############1.1
import sqlite3

conn = sqlite3.connect('autosalon.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS avtomobillar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nomi VARCHAR(100) NOT NULL,
    model TEXT,
    yil INTEGER,
    narx NUMERIC(12, 2),
    mavjudmi BOOL DEFAULT 1
)
''')

conn.commit()

###########1.2
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientlar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ism VARCHAR(50) NOT NULL,
    familiya VARCHAR(50),
    telefon CHAR(13),
    manzil TEXT
)
''')

conn.commit()


#################1.3
cursor.execute('''
CREATE TABLE IF NOT EXISTS buyurtmalar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    avtomobil_id INTEGER,
    client_id INTEGER,
    sana DATE NOT NULL,
    umumiy_narx NUMERIC(12, 2),
    FOREIGN KEY (avtomobil_id) REFERENCES avtomobillar(id),
    FOREIGN KEY (client_id) REFERENCES clientlar(id)
)
''')

conn.commit()

################1.4
cursor.execute('''
CREATE TABLE IF NOT EXISTS xodimlar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ism VARCHAR(50) NOT NULL,
    lavozim VARCHAR(50),
    maosh NUMERIC(10, 2)
)
''')

conn.commit()

###################2.1
cursor.execute('''
ALTER TABLE clientlar ADD COLUMN email VARCHAR(100)
''')

conn.commit()

####################2.2
cursor.execute('''
PRAGMA foreign_keys=off;

CREATE TABLE clientlar_new AS
SELECT id, ism AS yangi_ism, familiya, telefon, manzil, email FROM clientlar;

DROP TABLE clientlar;

ALTER TABLE clientlar_new RENAME TO clientlar;

PRAGMA foreign_keys=on;
''')

conn.commit()

##################2.3
cursor.execute('''
ALTER TABLE clientlar RENAME TO mijozlar
''')

conn.commit()

################3
cursor.execute('''
INSERT INTO avtomobillar (nomi, model, yil, narx, mavjudmi)
VALUES ('Tesla Model S', 'Electric', 2022, 799.99, 1),
       ('Mersedes', 'Cls 63', 2024, $197.600, 1),
       ('Audi A4', 'Sedan', 2023, 450.00, 1)
''')

cursor.execute('''
INSERT INTO mijozlar (ism, familiya, telefon, manzil, email)
VALUES ('Toxir', 'Toxirov', '+998901234567', 'Toshkent', 'toxir@example.com'),
       ('Vali', 'Valiyev', '+998905678910', 'Samarkand', 'vali@example.com')
''')

cursor.execute('''
INSERT INTO buyurtmalar (avtomobil_id, client_id, sana, umumiy_narx)
VALUES (1, 1, '2024-11-13', 79999.99),
       (2, 2, '2024-11-14', 55000.00)
''')

cursor.execute('''
INSERT INTO xodimlar (ism, lavozim, maosh)
VALUES ('Ali', 'Sotuvchi', 1500.50),
       ('Svetlana', 'Direktor', 3500.75)
''')

conn.commit()

####################4
cursor.execute('''
UPDATE xodimlar
SET ism = 'Jasur'
WHERE ism = 'Ali'
''')

cursor.execute('''
UPDATE xodimlar
SET ism = 'Olga'
WHERE ism = 'Svetlana'
''')

conn.commit()

#####################5
cursor.execute('''
DELETE FROM xodimlar WHERE ism = 'Jasur'
''')

conn.commit()

######################6
cursor.execute('SELECT * FROM avtomobillar')
avtomobillar = cursor.fetchall()
print("Avtomobillar:")
for avtomobil in avtomobillar:
    print(avtomobil)

cursor.execute('SELECT * FROM mijozlar')
mijozlar = cursor.fetchall()
print("\nMijozlar:")
for mijoz in mijozlar:
    print(mijoz)

cursor.execute('SELECT * FROM buyurtmalar')
buyurtmalar = cursor.fetchall()
print("\nBuyurtmalar:")
for buyurtma in buyurtmalar:
    print(buyurtma)

cursor.execute('SELECT * FROM xodimlar')
xodimlar = cursor.fetchall()
print("\nXodimlar:")
for xodim in xodimlar:
    print(xodim)

conn.commit()
