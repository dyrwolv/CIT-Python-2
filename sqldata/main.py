import sqlite3
import csv

def read_csv_file(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader, None)
        return list(reader)

def main():
    conn = sqlite3.connect('retirement_eligibility.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employee (
        EmployeeID INTEGER PRIMARY KEY,
        Name TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pay (
        EmployeeID INTEGER,
        Year INTEGER,
        Earnings REAL,
        FOREIGN KEY(EmployeeID) REFERENCES Employee(EmployeeID)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SocialSecurityMin (
        Year INTEGER PRIMARY KEY,
        Minimum REAL
    )
    ''')

    employee_file_path = 'Employee.txt'
    pay_file_path = 'Pay.txt'
    social_security_min_file_path = 'SocialSecurityMinimum.txt'

    employee_data = read_csv_file(employee_file_path)
    pay_data = read_csv_file(pay_file_path)
    social_security_min_data = read_csv_file(social_security_min_file_path)

    # Insert data with ON CONFLICT IGNORE to avoid unique constraint errors
    cursor.executemany('INSERT OR IGNORE INTO Employee (EmployeeID, Name) VALUES (?, ?)', employee_data)
    cursor.executemany('INSERT INTO Pay (EmployeeID, Year, Earnings) VALUES (?, ?, ?)', pay_data)
    cursor.executemany('INSERT OR IGNORE INTO SocialSecurityMin (Year, Minimum) VALUES (?, ?)', social_security_min_data)

    conn.commit()

    query = '''
    SELECT
        E.Name,
        P.Year,
        P.Earnings,
        S.Minimum,
        CASE
            WHEN P.Earnings >= S.Minimum THEN 'Yes'
            ELSE 'No'
        END AS Eligible
    FROM Pay P
    JOIN Employee E ON P.EmployeeID = E.EmployeeID
    JOIN SocialSecurityMin S ON P.Year = S.Year
    ORDER BY E.EmployeeID, P.Year
    '''

    cursor.execute(query)
    results = cursor.fetchall()

    print(f'{"Employee Name":<15} {"Year":<5} {"Earnings":<10} {"Minimum":<10} {"Include":<7}')
    print('-' * 50)

    for row in results:
        print(f'{row[0]:<15} {row[1]:<5} {row[2]:<10.2f} {row[3]:<10.2f} {row[4]:<7}')

    conn.close()

if __name__ == "__main__":
    main()

