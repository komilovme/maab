import sqlite3

# =====================================================
# TASK 1 — ROSTER DATABASE
# =====================================================

def task1_roster():
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()

    # 1. Create Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Roster (
            Name TEXT,
            Species TEXT,
            Age INTEGER
        )
    """)

    # Clear table if re-running
    cursor.execute("DELETE FROM Roster")

    # 2. Insert Data
    characters = [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ]

    cursor.executemany("INSERT INTO Roster VALUES (?, ?, ?)", characters)

    # 3. Update Data
    cursor.execute("""
        UPDATE Roster
        SET Name = 'Ezri Dax'
        WHERE Name = 'Jadzia Dax'
    """)

    # 4. Query Bajoran
    print("\n--- Bajoran Characters ---")
    cursor.execute("""
        SELECT Name, Age FROM Roster
        WHERE Species = 'Bajoran'
    """)
    for row in cursor.fetchall():
        print(row)

    # 5. Delete Age > 100
    cursor.execute("""
        DELETE FROM Roster
        WHERE Age > 100
    """)

    # 6. Add Rank Column
    try:
        cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
    except:
        pass  # Column may already exist

    cursor.execute("UPDATE Roster SET Rank='Captain' WHERE Name='Benjamin Sisko'")
    cursor.execute("UPDATE Roster SET Rank='Lieutenant' WHERE Name='Ezri Dax'")
    cursor.execute("UPDATE Roster SET Rank='Major' WHERE Name='Kira Nerys'")

    # 7. Advanced Query (Age DESC)
    print("\n--- All Characters (Age DESC) ---")
    cursor.execute("""
        SELECT Name, Species, Age, Rank
        FROM Roster
        ORDER BY Age DESC
    """)
    for row in cursor.fetchall():
        print(row)

    conn.commit()
    conn.close()


# =====================================================
# TASK 2 — LIBRARY DATABASE
# =====================================================

def task2_library():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # 1. Create Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            Title TEXT,
            Author TEXT,
            Year_Published INTEGER,
            Genre TEXT
        )
    """)

    # Clear table if re-running
    cursor.execute("DELETE FROM Books")

    # 2. Insert Data
    books = [
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
        ("1984", "George Orwell", 1949, "Dystopian"),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
    ]

    cursor.executemany("INSERT INTO Books VALUES (?, ?, ?, ?)", books)

    # 3. Update Year of 1984
    cursor.execute("""
        UPDATE Books
        SET Year_Published = 1950
        WHERE Title = '1984'
    """)

    # 4. Query Dystopian
    print("\n--- Dystopian Books ---")
    cursor.execute("""
        SELECT Title, Author
        FROM Books
        WHERE Genre = 'Dystopian'
    """)
    for row in cursor.fetchall():
        print(row)

    # 5. Delete Books Before 1950
    cursor.execute("""
        DELETE FROM Books
        WHERE Year_Published < 1950
    """)

    # 6. Add Rating Column
    try:
        cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
    except:
        pass

    cursor.execute("UPDATE Books SET Rating=4.8 WHERE Title='To Kill a Mockingbird'")
    cursor.execute("UPDATE Books SET Rating=4.7 WHERE Title='1984'")
    cursor.execute("UPDATE Books SET Rating=4.5 WHERE Title='The Great Gatsby'")

    # 7. Advanced Query (ASC)
    print("\n--- All Books (Year ASC) ---")
    cursor.execute("""
        SELECT Title, Author, Year_Published, Genre, Rating
        FROM Books
        ORDER BY Year_Published ASC
    """)
    for row in cursor.fetchall():
        print(row)

    conn.commit()
    conn.close()


# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":
    task1_roster()
    task2_library()