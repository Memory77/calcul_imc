import sqlite3

# Établir une connexion à la base de données
conn = sqlite3.connect("imc.db")
cursor = conn.cursor()


# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS user (
#         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT UNIQUE,
#         first_name TEXT,
#         last_name TEXT
#     )
# ''')

# Créer la table "bmi" avec une clé étrangère "user_id"
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS bmi (
#         bmi_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER,
#         weight REAL,
#         height REAL,
#         bmi_value REAL,
#         FOREIGN KEY (user_id) REFERENCES user(user_id)
#     )
# ''')

# Valider la transaction et fermer la connexion
conn.commit()
conn.close()