import mysql.connector

def init_database():
    try:
        # Initial connection to create the database if it doesn't exist
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password"
        )
        cursor = db.cursor()
        
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS oral_ai")
        cursor.execute("USE oral_ai")
        
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create user_details table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_details (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_email VARCHAR(100) NOT NULL,
                full_name VARCHAR(100) NOT NULL,
                age INT NOT NULL,
                gender VARCHAR(20) NOT NULL,
                symptoms TEXT,
                mouth_opening VARCHAR(50),
                additional_notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Create reports table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reports (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_email VARCHAR(100) NOT NULL,
                user_details_id INT NOT NULL,
                result VARCHAR(50) NOT NULL,
                confidence FLOAT NOT NULL,
                risk_level VARCHAR(20) NOT NULL,
                img_path VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_details_id) REFERENCES user_details(id) ON DELETE CASCADE
            )
        """)
        
        print("Database 'oral_ai' and all tables initialized successfully!")
        db.commit()
    except Exception as e:
        print(f"Error: {e}")
        print("\nNOTE: Please make sure MySQL is running and update credentials in this script.")

if __name__ == "__main__":
    init_database()
