import sqlite3
import subprocess
import sys

def unsafe_sql_query(user_input):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    
    # Уязвимость: SQL-инъекция (Bandit обнаружит)
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    cursor.execute(query)
    
    result = cursor.fetchall()
    conn.close()
    return result

def unsafe_system_call(command):
    # Уязвимость: выполнение произвольных команд (Bandit обнаружит)
    subprocess.run(command, shell=True)

def hardcoded_password():
    # Уязвимость: хардкод пароля (Bandit обнаружит)
    password = "admin123"
    return password

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python app.py <имя пользователя>")
    else:
        user_input = sys.argv[1]
        print("Результат запроса:", unsafe_sql_query(user_input))
        
        # Опасный вызов
        print("Запускаем команду...")
        unsafe_system_call(user_input)
        
        # Хардкод пароля
        print("Хардкод пароля:", hardcoded_password())