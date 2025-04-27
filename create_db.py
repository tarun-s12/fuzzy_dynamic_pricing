import sqlite3

conn = sqlite3.connect('services.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS service_providers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    address TEXT,
    type TEXT,
    latitude REAL,
    longitude REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    service_provider_id INTEGER,
    FOREIGN KEY (service_provider_id) REFERENCES service_providers(id)
)
''')

service_providers = [
    (1, 'John Smith', '123 Main St', 'plumber', 37.7749, -122.4194),
    (2, 'Alice Lee', '45 Market Ave', 'electrician', 37.8044, -122.2712),
    (3, 'Mike Johnson', '78 Central Blvd', 'plumber', 37.8715, -122.2730)
]

cursor.executemany('''
INSERT INTO service_providers (id, name, address, type, latitude, longitude)
VALUES (?, ?, ?, ?, ?, ?)
''', service_providers)

orders = [
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 3),
    (6, 3)
]

cursor.executemany('''
INSERT INTO orders (id, service_provider_id)
VALUES (?, ?)
''', orders)

conn.commit()
conn.close()

print("Database and tables created, sample data inserted successfully!")
