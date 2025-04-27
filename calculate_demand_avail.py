import sqlite3

MAX_ORDERS = 10   
MAX_PROVIDERS = 5 

def connect_db(db_name='services.db'):
    conn = sqlite3.connect(db_name)
    return conn, conn.cursor()

def fetch_providers(cursor):
    cursor.execute('SELECT id, type FROM service_providers')
    providers = cursor.fetchall()
    
    type_to_providers = {}
    for provider_id, provider_type in providers:
        type_to_providers.setdefault(provider_type, []).append(provider_id)
        
    return type_to_providers

def fetch_orders(cursor):
    cursor.execute('SELECT service_provider_id FROM orders')
    orders = cursor.fetchall()
    
    provider_order_count = {}
    for (provider_id,) in orders:
        provider_order_count[provider_id] = provider_order_count.get(provider_id, 0) + 1
        
    return provider_order_count

def calculate_service_metrics(service_type, db_name='services.db'):
    conn, cursor = connect_db(db_name)
    
    type_to_providers = fetch_providers(cursor)
    provider_order_count = fetch_orders(cursor)
    
    conn.close()
    
    provider_ids = type_to_providers.get(service_type, [])
    total_providers = len(provider_ids)
    
    total_orders = sum(provider_order_count.get(pid, 0) for pid in provider_ids)
    
    if total_providers == 0:
        availability_score = 0
    else:
        availability_score = min((total_providers / MAX_PROVIDERS) * 100, 100)
    
    if total_orders == 0:
        demand_score = 0
    else:
        demand_score = min((total_orders / MAX_ORDERS) * 100, 100)
    
    return {
        'service_type': service_type,
        'demand_score': round(demand_score, 2),
        'availability_score': round(availability_score, 2)
    }