import psycopg2 as psy
#Membuat Tabel Baru
conn = psy.connect(database="kampus", user ="fazhri", password="123", host="localhost", port="5432")
print("Berhasil")

cur = conn.cursor()
cur.execute('''CREATE TABLE DATA_MAHASISWA
      (ID INT PRIMARY KEY NOT NULL,
      NAMA_MAHASISWA TEXT NOT NULL,
      NIM_MAHASISWA TEXT NOT NULL,
      PRODI VARCHAR NOT NULL);''')
print("tabel sukses dibuat")

conn.commit()
conn.close()