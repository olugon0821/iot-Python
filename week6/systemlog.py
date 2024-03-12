import matplotlib.pyplot as plt
import psutil
import time
from datetime import datetime
import sqlite3

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
return conn
except sqlite3.Error as e:
print(f"연결 오류: {e}")
return conn

def create_table(conn):

try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS system_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME NOT NULL,
                cpu_usage REAL NOT NULL,
                memory_usage REAL NOT NULL
            )
        ''')
        conn.commit()
except sqlite3.Error as e:
print(f"테이블 생성 오류: {e}")

def insert_data(conn, date, cpu_percent, memory_percent):

try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO system_info (timestamp, cpu_usage, memory_usage) VALUES (?, ?, ?)",
                       (date, cpu_percent, memory_percent))
        conn.commit()
except sqlite3.Error as e:
print(f"데이터 삽입 오류: {e}")

def dataPlot(conn):
try:
        cursor = conn.cursor()
        cursor.execute("SELECT timestamp, cpu_usage, memory_usage FROM system_info")
        rows = cursor.fetchall()

        timestamps = []
        cpu_use = []
        memory_use = []

for row in rows:
            timestamps.append(row[0])
            cpu_use.append(row[1])
            memory_use.append(row[2])

if len(timestamps) > 60:
            timestamps = timestamps[-60:]
            cpu_use = cpu_use[-60:]
            memory_use = memory_use[-60:]

        plt.plot(timestamps,cpu_use,memory_use)

except sqlite3.Error as e:
print(f"오류: {e}")


def main():
    db_file = 'SystemLog.db'
    conn = create_connection(db_file)

if conn is not None:
        create_table(conn)

while True:
            cpu_percent = psutil.cpu_percent()
            memory_percent = psutil.virtual_memory().percent
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            insert_data(conn, date, cpu_percent, memory_percent)

            dataPlot(conn)

            time.sleep(3)
else:
print("데이터베이스 연결 실패")

if __name__ == '__main__':
    main()
