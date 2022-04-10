from ast import keyword
import psycopg2
#Connect Database
conn = psycopg2.connect(
         host="localhost",
         database="kampus",
         user="fazhri",
         password="123")

#Menyimpan Data Baru
def insert_data(conn):
   id = (input("Masukan ID Mahasiswa: "))
   nama = input("Masukan Nama Mahasiwa: ")
   nim = input("Masukan NIM Mahasiswa: ")
   prodi = (input("Masukan Prodi: "))
   val = (id,nama,nim,prodi)
   sql = "INSERT INTO DATA_MAHASISWA (ID, NAMA_MAHASISWA, NIM_MAHASISWA, PRODI) VALUES (%s, %s, %s, %s)"
   cur = conn.cursor()
   cur.execute(sql, val)
   conn.commit()
   print("{} Data Berhasil Disimpan".format(cur.rowcount))

#Menampilkan Data
def show_data(conn):
   cur = conn.cursor()
   sql = "SELECT * FROM DATA_MAHASISWA"
   cur.execute(sql)
   result = cur.fetchall()

   if cur.rowcount < 0:
      print("Tidak ada data")
   else:
      print("Data Berhasil Ditemukan")
      for data in result:
         print(data)

#Update Data
def update_data(conn):
   cur = conn.cursor()
   show_data(conn)
   id = input("Pilih ID Mahasiswa: ")
   nama = input("Masukan Nama Mahasiswa yang Baru: ")
   nim = input("Masukan NIM Mahasiswa yang Baru: ")
   prodi =input("Masukan Prodi Mahasiswa yang Baru: ")

   sql = "UPDATE DATA_MAHASISWA SET nama_mahasiswa=%s, nim_mahasiswa=%s, prodi=%s WHERE id=%s"
   val = (nama, nim, prodi, id)
   cur.execute(sql, val)
   conn.commit()
   print("{} Data Berhasil Diupdate".format(cur.rowcount))

#Menghapus Data
def delete_data(conn):
   cur = conn.cursor()
   show_data(conn)
   id = input("Pilih ID Mahasiswa: ")
   sql = "DELETE FROM DATA_MAHASISWA WHERE ID=%s"
   val = (id)
   cur.execute(sql, val)
   conn.commit()
   print("{} Data Berhasil Dihapus".format(cur.rowcount))

#Mencari Data
def search_data(conn):
   cur = conn.cursor()
   keyword = input("Masukan NIM atau nama Mahasiswa: ")
   sql = "SELECT * FROM DATA_MAHASISWA WHERE nim_mahasiswa LIKE %s OR nama_mahasiswa LIKE %s"
   val = ("%{}%".format(keyword), "%{}%".format(keyword))
   cur.execute(sql, val)
   result = cur.fetchall()

   if cur.rowcount <=0:
      print("Data tidak ditemukann")
   else:
      for data in result:
         print("Data ditemukan: ",data)

#Menampilkan Menu
def show_menu(conn):
   print("\n")
   print("==== TUGAS 1 PEMBUATAN CRUD MELALUI CLI ====")
   print("=== OLEH FAZHRI ARIF ALVINNES ===")
   print("==== TABEL DATA MAHASISWA ===")
   print("1. Insert Data")
   print("2. Show Data")
   print("3. Update Data")  
   print("4. Search Data")
   print("5. Delete Data")
   print("0. Keluar")
   print("------------------")
   menu = input("Pilih Menu: ")

   if menu == "1":
      insert_data(conn)
   elif menu == "2":
      show_data(conn)
   elif menu == "3":
      update_data(conn)
   elif menu == "4":
      search_data(conn)
   elif menu == "5":
      delete_data(conn)
   elif menu == "0":
      exit()
   else:
      print("Menu salah")

#Looping
if __name__ == "__main__":
   while(True):
      show_menu(conn)