
import sqlite3

conn = sqlite3.connect("sqlitedrill.db")

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT)")
    conn.commit()
conn.close()

def get_file():
    fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
    for file in fileList:
        if file.endswith(".txt"):
            return (file)

if __name__ == "__main__":
    get_file()


conn = sqlite3.connect("sqlitedrill.db")
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(col_filename) VALUES (file)")
    conn.commit()        
conn.close()

