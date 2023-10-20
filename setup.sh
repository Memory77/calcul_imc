# Créer une base de données SQLite
sqlite3 imc.db

# Exécuter la commande SQL pour créer la table "user"
sqlite3 imc.db "CREATE TABLE IF NOT EXISTS user (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    first_name TEXT,
    last_name TEXT
);"

# Exécuter la commande SQL pour créer la table "bmi" avec la clé étrangère
sqlite3 imc.db "CREATE TABLE IF NOT EXISTS bmi (
    bmi_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    weight REAL,
    height REAL,
    bmi_value REAL,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);"

echo "Base de données et tables créées avec succès."