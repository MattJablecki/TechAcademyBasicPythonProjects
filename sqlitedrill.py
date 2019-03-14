
import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

conn = sqlite3.connect("sqlitedrill.db")

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT)")
    def data_entry():
        for item in fileList:
            if item.endswith(".txt"):
                cur.execute("INSERT INTO tbl_files(col_filename) VALUES(?)", (item, ))
        conn.commit()
    data_entry()

    cur.execute("SELECT col_filename FROM tbl_files")
    print(cur.fetchall())

conn.close()






