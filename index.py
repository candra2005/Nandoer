import os
import csv
import pandas as pd

FILE_ADMIN = "data_admin.csv"
FILE_USER = "data_user.csv"
folder_toko = "data_toko"

#UNTUK PROGRAM UTAMA
def cek_data():
    if not os.path.exists(FILE_USER):  
        user = pd.DataFrame(columns=["username", "password", "email", "role"]) 
        user.to_csv(FILE_USER, index=False) 
    if not os.path.exists(FILE_ADMIN):  
        user = pd.DataFrame(columns=["username", "password"]) 
        user.to_csv(FILE_ADMIN, index=False) 
    if not os.path.exists(folder_toko):
        os.makedirs(folder_toko)

#UNTUK REGISTRASI
def cek_email(email):
    if "@" not in email or "." not in email:
        return False

    local, _, domain = email.partition("@")

    if not local or not domain:
        return False

    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False

    char_email = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_"
    for char in email:
        if char not in char_email and char != "@":
            return False

    return True

#MENU AWAL
def register():
    os.system("cls")
        
    print("╔" + "═"*48 + "╗")
    print("║" + "Registrasi Akun".center(48) + "║")
    print("╚" + "═"*48 + "╝")
        
    print("\n1. Penjual\n2. Pembeli\n3. Kembali\n")
    pilihan = input("Registrasi sebagai : ")
        
    if pilihan == "1":
        os.system("cls")
        
        seller = pd.read_csv(FILE_USER)
        
        kondisi = True
        kondisi2 = True
        
        print("╔" + "═"*48 + "╗")
        print("║" + "Registrasi Akun".center(48) + "║")
        print("║" + "Penjual".center(48) + "║")
        print("╚" + "═"*48 + "╝")
        print()
        
        username = input("Masukkan username : ")
        
        while kondisi:
            password = input("Masukkan password : ")
            
            if len(password) < 8:
                print("Password harus berisi minimal 8 karakter!")
            else:
                kondisi = False
        
        while kondisi2:
            email = input("Masukkan email : ")
        
            if email in seller["email"].values:
                print("Username sudah digunakan, silahkan gunakan username lain.")
            if cek_email(email):
                kondisi2 = False
            else:
                print("Masukkan email yang valid!")
                
        data_baru = {"username": username, "password": password, "email": email, "role": "seller"}
        data_baru_df = pd.DataFrame([data_baru])
        seller = pd.concat([seller, data_baru_df], ignore_index=True)
        seller.to_csv(FILE_USER, index=False)     
        
        print(f"\nRegistrasi {username} sebagai penjual telah berhasil") 
        
    elif pilihan == "2":
        os.system("cls")
        
        buyer = pd.read_csv(FILE_USER)
        
        kondisi = True
        kondisi2 = True
        
        print("╔" + "═"*48 + "╗")
        print("║" + "Registrasi Akun".center(48) + "║")
        print("║" + "Pembeli".center(48) + "║")
        print("╚" + "═"*48 + "╝")
        print()
        
        username = input("Masukkan username : ")
        
        while kondisi:
            password = input("Masukkan password : ")
            
            if len(password) < 8:
                print("Password harus berisi minimal 8 karakter!")
            else:
                kondisi = False
        
        while kondisi2:
            email = input("Masukkan email : ")
        
            if email in buyer["email"].values:
                print("Username sudah digunakan, silahkan gunakan username lain.")
            if cek_email(email):
                kondisi2 = False
            else:
                print("Masukkan email yang valid!")
                
        data_baru = {"username": username, "password": password, "email": email, "role": "buyer"}
        data_baru_df = pd.DataFrame([data_baru])
        seller = pd.concat([buyer, data_baru_df], ignore_index=True)
        seller.to_csv(FILE_USER, index=False)    
        
        print(f"\nRegistrasi {username} sebagai penjual telah berhasil") 
        
    elif pilihan == "3":
        pass
    else:
        print("Masukan anda salah, anda akan dikembalikan ke menu awal")
        

def login():
    os.system("cls")
        
    print("╔" + "═"*48 + "╗")
    print("║" + "Login Akun".center(48) + "║")
    print("╚" + "═"*48 + "╝")
        
    print("\n1. Admin\n2. Penjual\n3. Pembeli\n4. Kembali\n")
    pilihan = input("Login sebagai : ")
    
    if pilihan == "1":
        os.system("cls")
        
        admin = pd.read_csv(FILE_ADMIN)
        
        i = 0
        
        print("╔" + "═"*48 + "╗")
        print("║" + "Login Akun".center(48) + "║")
        print("║" + "Admin".center(48) + "║")
        print("╚" + "═"*48 + "╝")
        
        while i < 3:
            admin["username"] = admin["username"].astype(str)
            admin["password"] = admin["password"].astype(str)

            username = input("\nMasukkan username : ")
            password = input("Masukkan password : ")

            user = admin[(admin["username"] == username) & (admin["password"] == password)]
            if not user.empty:
                menu_admin(username)
                i+=3
            else:
                print("\nLogin gagal! Username atau password salah.")
                i+=1
    
    elif pilihan == "2":
        os.system("cls")
        
        seller = pd.read_csv(FILE_USER)
        
        i = 0
        
        print("╔" + "═"*48 + "╗")
        print("║" + "Login Akun".center(48) + "║")
        print("║" + "Penjual".center(48) + "║")
        print("╚" + "═"*48 + "╝")
        
        while i < 3:
            seller["email"] = seller["email"].astype(str)
            seller["password"] = seller["password"].astype(str)

            email = input("\nMasukkan email : ")
            password = input("Masukkan password : ")

            user = seller[(seller["email"] == email) & (seller["password"] == password) & (seller["role"] == "seller")]
            if not user.empty:
                menu_penjual(email)
                i+=3
            else:
                print("\nLogin gagal! email atau password salah.")
                i+=1
    
    elif pilihan == "3":
        os.system("cls")
        
        buyer = pd.read_csv(FILE_USER)
        
        i = 0
        
        print("╔" + "═"*48 + "╗")
        print("║" + "Login Akun".center(48) + "║")
        print("║" + "Pembeli".center(48) + "║")
        print("╚" + "═"*48 + "╝")
        
        while i < 3:
            buyer["email"] = buyer["email"].astype(str)
            buyer["password"] = buyer["password"].astype(str)
            
            email = input("\nMasukkan email : ")
            password = input("Masukkan password : ")

            user = buyer[(buyer["email"] == email) & (buyer["password"] == password) & (buyer["role"] == "buyer")]
            if not user.empty:
                menu_pembeli(email)
                i+=3
            else:
                print("\nLogin gagal! Username atau password salah.")
                i+=1
                
    elif pilihan == "4":
        pass
    else:
        print("Masukan anda salah, anda akan dikembalikan ke menu awal")

#MENU SETELAH LOGIN
def menu_admin(user):
    kondisi = True
    
    while kondisi:
        os.system('cls')
        
        print("╔" + "═"*48 + "╗")
        print("║" + "Menu Admin".center(48) + "║")
        print("╠" + "═"*48 + "╣")
        print("║" + user.center(48) + "║")
        print("╚" + "═"*48 + "╝")
        
        print("\n1. Edit akun seller\n2. Edit akun buyer\n3. Histori penjualan\n4. Total Penjualan\n5. Keluar akun")
        
        kondisi2 = True
        
        while kondisi2:
            pilihan = input("\nGunakan menu nomor : ")
            
            if pilihan == "1":
                edit_akun_seller()
                kondisi2 = False
            elif pilihan == "2":
                edit_akun_buyer()
                kondisi2 = False
            elif pilihan == "3":
                kondisi2 = False
            elif pilihan == "4":
                kondisi2 = False
            elif pilihan == "5":
                kondisi2 = False
                kondisi = False
            else:
                print("Masukkan input yang benar!")

    def id_users(tipe):
        try:
            with open(FILE_USER, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                data = list(reader)

                tipe_data = [row for row in data if len(row) > 2 and row[2] == tipe]

                return len(tipe_data) + 1
        except FileNotFoundError:
            return 1   

    # Fungsi untuk menambahkan data pembeli atau penjual
    def edit_akun_seller():
        pilih = True
    
        while pilih:
            os.system('cls')
            
            print("╔" + "═"*48 + "╗")
            print("║" + "Menu Edit Akun Seller".center(48) + "║")
            print("╠" + "═"*48 + "╣")
            print("║" + user.center(48) + "║")
            print("╚" + "═"*48 + "╝")
            
            print("\n1. Tambah akun seller\n2. Edit akun seller\n3. Lihat akun seller\n4. Hapus akun seller\n5. Keluar menu akun seller")
            
            pilih2 = True
            
            while pilih2:
                pilihan = input("\nGunakan menu nomor : ")
                
                if pilihan == "1":
                    tambah_akun_seller()
                    pilih2 = False
                elif pilihan == "2":
                    ubah_akun_seller()
                    pilih2 = False
                elif pilihan == "3":
                    lihat_data_seller()
                    pilih2 = False
                elif pilihan == "4":
                    hapus_data_seller()
                    pilih2 = False
                elif pilihan == "5":
                    pilih2 = False
                    pilih = False
                else:
                    print("Masukkan input yang benar!")

        def tambah_akun_seller():
            nama = input("Masukkan Nama: ")
            tipe = input("Masukkan Tipe (Pembeli/Penjual): ").capitalize()
            if tipe not in ["Penjual"]:
                print("Tipe yang dipilih tidak sesuai.")
                return
            id = id_users(tipe)
            email = input("Masukkan email: ")

            with open(FILE_USER, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([id, nama, tipe, email])

            print(f"Data {tipe} dengan ID {id} berhasil ditambahkan.")

        def ubah_akun_seller():
            try:
                with open(FILE_USER, mode='r', newline='', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    data = list(reader)

                if len(data) <= 1:
                    print("Belum ada data yang tersimpan.")
                    return

                tipe = "Penjual".capitalize()
                if tipe not in ["Penjual"]:
                    print("Tipe yang dipilih tidak sesuai.")
                    return
                id_edit = input("Masukkan ID data yang ingin diedit: ")

                # Cari data yang sesuai
                for i, row in enumerate(data[1:], start=1):
                    if row[2] == tipe and row[0] == id_edit:
                        print(f"Data saat ini: Nama: {row[1]}, Kontak: {row[3]}")
                        nama_baru = input("Masukkan Nama baru (tekan Enter untuk tidak mengubah): ")
                        kontak_baru = input("Masukkan Kontak baru (tekan Enter untuk tidak mengubah): ")

                        # Perbarui data
                        if nama_baru.strip():
                            row[1] = nama_baru
                        if kontak_baru.strip():
                            row[3] = kontak_baru

                        # Tulis ulang data ke file CSV
                        with open(FILE_USER, mode='w', newline='', encoding='utf-8') as file:
                            writer = csv.writer(file)
                            writer.writerows(data)

                        print(f"Data dengan ID {id_edit} berhasil diperbarui.")
                        return

                print(f"Data dengan ID {id_edit} dan tipe {tipe} tidak ditemukan.")
            except FileNotFoundError:
                print("Belum ada file data. Tambahkan data terlebih dahulu.")

        
        def lihat_data_seller():
            tipe = "Penjual".capitalize()
            if tipe not in ["Penjual"]:
                print("Tipe yang dipilih tidak sesuai.")
                return

            try:
                with open(FILE_USER, mode='r', newline='', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    data = list(reader)
                    if len(data) <= 1:
                        print("Belum ada data yang tersimpan.")
                        return

                    print(f"\nData {tipe}:")
                    print(f"{'ID':<10}{'Nama':<20}{'Kontak':<20}")
                    print("-" * 50)
                    for row in data[1:]:
                        if row[2] == tipe:
                            print(f"{row[0]:<10}{row[1]:<20}{row[3]:<20}")
            except FileNotFoundError:
                print("Belum ada file data. Tambahkan data terlebih dahulu.")
        
        def hapus_data_seller():
            tipe = "Penjual".capitalize()
            if tipe not in ["Penjual"]:
                print("Tipe yang dipilih tidak sesuai.")
                return
            
            try:
                with open(FILE_USER, mode='r', newline='', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    data = list(reader)

                if len(data) <= 1:
                    print("Belum ada data yang tersimpan.")
                    return

                print(f"\nData {tipe}:")
                print(f"{'ID':<10}{'Nama':<20}{'Tipe':<10}{'Kontak':<20}")
                print("-" * 60)
                for row in data[1:]:
                    if row[2] == tipe:
                            print(f"{row[0]:<10}{row[1]:<20}{row[3]:<20}")

                id_hapus = input("\nMasukkan ID data yang ingin dihapus: ")

                # Filter data, menyimpan hanya data yang ID-nya tidak cocok
                new_data = [row for row in data if row[0] != id_hapus]

                if len(new_data) == len(data):
                    print(f"Data dengan ID {id_hapus} tidak ditemukan.")
                    return

                with open(FILE_USER, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerows(new_data)

                print(f"Data dengan ID {id_hapus} berhasil dihapus.")

            except FileNotFoundError:
                print("Belum ada file data. Tambahkan data terlebih dahulu.")
        
    def edit_akun_buyer():
        pilih = True
    
        while pilih:
            os.system('cls')
            
            print("╔" + "═"*48 + "╗")
            print("║" + "Menu Edit Akun Buyer".center(48) + "║")
            print("╠" + "═"*48 + "╣")
            print("║" + user.center(48) + "║")
            print("╚" + "═"*48 + "╝")
            
            print("\n1. Tambah akun buyer\n2. Edit akun buyer\n3. Lihat akun buyer\n4. Hapus akun buyer\n5. Keluar menu akun buyer")
            
            pilih2 = True
            
            while pilih2:
                pilihan = input("\nGunakan menu nomor : ")
                
                if pilihan == "1":
                    tambah_akun_buyer()
                    pilih2 = False
                elif pilihan == "2":
                    ubah_akun_buyer()
                    pilih2 = False
                elif pilihan == "3":
                    lihat_data_buyer()
                    pilih2 = False
                elif pilihan == "4":
                    hapus_data_buyer()
                    pilih2 = False
                elif pilihan == "5":
                    pilih2 = False
                    pilih = False
                else:
                    print("Masukkan input yang benar!")

        def tambah_akun_buyer():
            nama = input("Masukkan Nama: ")
            tipe = "Pembeli".capitalize()
            if tipe not in ["Pembeli"]:
                print("Tipe yang dipilih tidak sesuai.")
                return
            id = id_users(tipe)
            email = input("Masukkan email: ")

            with open(FILE_USER, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([id, nama, tipe, email])

            print(f"Data {tipe} dengan ID {id} berhasil ditambahkan.")

        def ubah_akun_buyer():
            try:
                with open(FILE_USER, mode='r', newline='', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    data = list(reader)

                if len(data) <= 1:
                    print("Belum ada data yang tersimpan.")
                    return

                tipe = "Pembeli".capitalize()
                if tipe not in ["Pembeli"]:
                    print("Tipe yang dipilih tidak sesuai.")
                    return
                id_edit = input("Masukkan ID data yang ingin diedit: ")

                # Cari data yang sesuai
                for i, row in enumerate(data[1:], start=1):
                    if row[2] == tipe and row[0] == id_edit:
                        print(f"Data saat ini: Nama: {row[1]}, Kontak: {row[3]}")
                        nama_baru = input("Masukkan Nama baru (tekan Enter untuk tidak mengubah): ")
                        kontak_baru = input("Masukkan Kontak baru (tekan Enter untuk tidak mengubah): ")

                        # Perbarui data
                        if nama_baru.strip():
                            row[1] = nama_baru
                        if kontak_baru.strip():
                            row[3] = kontak_baru

                        # Tulis ulang data ke file CSV
                        with open(FILE_USER, mode='w', newline='', encoding='utf-8') as file:
                            writer = csv.writer(file)
                            writer.writerows(data)

                        print(f"Data dengan ID {id_edit} berhasil diperbarui.")
                        return

                print(f"Data dengan ID {id_edit} dan tipe {tipe} tidak ditemukan.")
            except FileNotFoundError:
                print("Belum ada file data. Tambahkan data terlebih dahulu.")

        
        def lihat_data_buyer():
            tipe = "Pembeli".capitalize()
            if tipe not in ["Pembeli"]:
                print("Tipe yang dipilih tidak sesuai.")
                return

            try:
                with open(FILE_USER, mode='r', newline='', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    data = list(reader)
                    if len(data) <= 1:
                        print("Belum ada data yang tersimpan.")
                        return

                    print(f"\nData {tipe}:")
                    print(f"{'ID':<10}{'Nama':<20}{'Kontak':<20}")
                    print("-" * 50)
                    for row in data[1:]:
                        if row[2] == tipe:
                            print(f"{row[0]:<10}{row[1]:<20}{row[3]:<20}")
            except FileNotFoundError:
                print("Belum ada file data. Tambahkan data terlebih dahulu.")
        
        def hapus_data_buyer():
            tipe = "Pembeli".capitalize()
            if tipe not in ["Pembeli"]:
                print("Tipe yang dipilih tidak sesuai.")
                return
            
            try:
                with open(FILE_USER, mode='r', newline='', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    data = list(reader)

                if len(data) <= 1:
                    print("Belum ada data yang tersimpan.")
                    return

                print(f"\nData {tipe}:")
                print(f"{'ID':<10}{'Nama':<20}{'Tipe':<10}{'Kontak':<20}")
                print("-" * 60)
                for row in data[1:]:
                    if row[2] == tipe:
                            print(f"{row[0]:<10}{row[1]:<20}{row[3]:<20}")

                id_hapus = input("\nMasukkan ID data yang ingin dihapus: ")

                # Filter data, menyimpan hanya data yang ID-nya tidak cocok
                new_data = [row for row in data if row[0] != id_hapus]

                if len(new_data) == len(data):
                    print(f"Data dengan ID {id_hapus} tidak ditemukan.")
                    return

                with open(FILE_USER, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerows(new_data)

                print(f"Data dengan ID {id_hapus} berhasil dihapus.")

            except FileNotFoundError:
                print("Belum ada file data. Tambahkan data terlebih dahulu.")


    
def menu_penjual(email):
    baca = pd.read_csv(FILE_USER)
    
    kondisi = True
    
    index = baca[baca['email'] == email].index[0]
    user = baca.at[index, 'username']
    
    while kondisi:
        os.system('cls')
        
        print("╔" + "═"*48 + "╗")
        print("║" + "Menu Penjual".center(48) + "║")
        print("╠" + "═"*48 + "╣")
        print("║" + user.center(48) + "║")
        print("╚" + "═"*48 + "╝")
        
        print("\n1. Profil akun\n2. Edit barang\n3. Total penjualan\n4. Keluar akun")
        
        kondisi2 = True
        
        while kondisi2:
                pilihan = input("\nGunakan menu nomor : ")
                
                if pilihan == "1":
                    profil(index)
                    kondisi2 = False
                elif pilihan == "2":
                    edit_barang_penjual(user)
                    kondisi2 = False
                elif pilihan == "3":
                    kondisi2 = False
                elif pilihan == "4":
                    kondisi2 = False
                    kondisi = False
                else:
                    print("\nMasukkan input yang benar!")
    
def menu_pembeli(email):
    baca = pd.read_csv(FILE_USER)
    
    kondisi = True
    
    index = baca[baca['email'] == email].index[0]
    user = baca.at[index, 'username']
    
    while kondisi:
        os.system('cls')
        
        print("╔" + "═"*48 + "╗")
        print("║" + "Menu Pembeli".center(48) + "║")
        print("╠" + "═"*48 + "╣")
        print("║" + user.center(48) + "║")
        print("╚" + "═"*48 + "╝")
        
        print("\n1. Profil akun\n2. Beli barang\n3. Histori pembelian\n4. Keluar akun")
        
        kondisi2 = True
            
        while kondisi2:
                pilihan = input("\nGunakan menu nomor : ")
                
                if pilihan == "1":
                    profil(index)
                    kondisi2 = False
                elif pilihan == "2":
                    kondisi2 = False
                elif pilihan == "3":
                    kondisi2 = False
                elif pilihan == "4":
                    kondisi2 = False
                    kondisi = False
                else:
                    print("Masukkan input yang benar!")
            
#FITUR PROFIL        
def profil(index):
    os.system('cls')
    
    baca = pd.read_csv(FILE_USER)
    
    user = baca.at[index, 'username']
    email = baca.at[index, 'email']
    role = baca.at[index, 'role']
    
    print("╔" + "═"*48 + "╗")
    print("║" + "Profil Akun".center(48) + "║")
    print("╚" + "═"*48 + "╝")
    
    print(f"\nUsername : {user}\nEmail : {email}\nPeran : {role}")
    
    i = input("\nKetik apa saja untuk kembali")

#FITUR PENJUAL
def edit_barang_penjual(user):    
    sub_folder = os.path.join(folder_toko, f"toko_{user}")
    
    if not os.path.exists(sub_folder):
        os.makedirs(sub_folder)
    
    barang = os.path.join(sub_folder, f"toko_{user}.csv")
    histori = os.path.join(sub_folder, f"histori_{user}.csv")
    
    if not os.path.exists(barang):  
        user_df = pd.DataFrame(columns=["barang", "harga", "stok"]) 
        user_df.to_csv(barang, index=False)
    if not os.path.exists(histori):  
        user_df = pd.DataFrame(columns=["barang", "terjual"]) 
        user_df.to_csv(histori, index=False) 
        
    kondisi = True

    while kondisi:
        os.system('cls')
        
        print("╔" + "═"*48 + "╗")
        print("║" + "Edit Barang".center(48) + "║")
        print("╚" + "═"*48 + "╝")
        
        print("\n1. List barang\n2. Tambah jenis barang\n3. Hapus jenis barang\n4. Edit harga\n5. Edit stok barang\n6. Kembali")
        
        kondisi2 = True
            
        while kondisi2:
                pilihan = input("\nGunakan menu nomor : ")
                
                if pilihan == "1":
                    list_barang(user)
                    kondisi2 = False
                elif pilihan == "2":
                    tambah(user)
                    kondisi2 = False
                elif pilihan == "3":
                    hapus(user)
                    kondisi2 = False
                elif pilihan == "4":
                    edit_harga(user)
                    kondisi2 = False
                elif pilihan == "5":
                    edit_stok(user)
                    kondisi2 = False
                elif pilihan == "6":
                    kondisi2 = False
                    kondisi = False
                else:
                    print("Masukkan input yang benar!")

#FITUR EDIT BARANG
def list_barang(user):
    sub_folder = os.path.join(folder_toko, f"toko_{user}")
    file_barang = os.path.join(sub_folder, f"toko_{user}.csv")
    
    baca = pd.read_csv(file_barang)
    os.system('cls')

    print("╔" + "═"*48 + "╗")
    print("║" + "List Barang".center(48) + "║")
    print("╚" + "═"*48 + "╝")
    print()
    
    if baca.empty:
        print("Tidak ada barang dalam toko ini!")
        
        i = input("\nTekan enter untuk kembali")
        return
    
    print("List barang:")
    for index, row in baca.iterrows():
        barang = row["barang"]
        harga = row["harga"]
        stok = row["stok"]
        print(f"{index + 1}. {barang} | harga = {harga} | stok = {stok}")
    
    i = input("\nTekan enter untuk kembali")

def tambah(user):
    sub_folder = os.path.join(folder_toko, f"toko_{user}")
    file_barang = os.path.join(sub_folder, f"toko_{user}.csv")
    
    baca = pd.read_csv(file_barang)
    os.system('cls')
    
    print("╔" + "═"*48 + "╗")
    print("║" + "Tambah Jenis Barang".center(48) + "║")
    print("╚" + "═"*48 + "╝")
    print()
    
    kondisi2 = True
    
    while kondisi2:
        barang = input("Masukkan nama barang : ")
        
        if barang in baca["barang"].values:
            print("Barang sudah ada dalam data!")
        else:
            kondisi2 = False
    
    kondisi3 = True
    
    while kondisi3:
        try:
            harga = int(input("Masukkan harga barang : "))
            
            kondisi3 = False
        except:
            print("Masukkan input berupa angka!")
            
    kondisi4 = True
    
    while kondisi4:
        try:
            stok = int(input("Masukkan stok barang : "))
            
            kondisi4 = False
        except:
            print("Masukkan input berupa angka!")
            
    data_baru = {"barang": barang, "harga": harga, "stok": stok}
    df_barang = pd.concat([baca, pd.DataFrame([data_baru])], ignore_index=True)
    df_barang.to_csv(file_barang, index=False)
    
    print(f"\n{barang} telah ditambahkan dengan harga : {harga} dan stok : {stok}")
    
    i = input("\nTekan enter untuk kembali")
    
def hapus(user):
    sub_folder = os.path.join(folder_toko, f"toko_{user}")
    file_barang = os.path.join(sub_folder, f"toko_{user}.csv")
    
    baca = pd.read_csv(file_barang)
    
    os.system('cls')
    
    print("╔" + "═"*48 + "╗")
    print("║" + "Hapus Barang".center(48) + "║")
    print("╚" + "═"*48 + "╝")
    print()
    
    if baca.empty:
        print("Tidak ada barang dalam toko ini!")
        
        i = input("\nTekan enter untuk kembali")
        return
    
    print("List barang:")
    for index, row in baca.iterrows():
        barang = row["barang"]
        harga = row["harga"]
        stok = row["stok"]
        print(f"{index + 1}. {barang} | harga = {harga} | stok = {stok}")
        
    kondisi = True
    
    print()
    
    while kondisi:
        try:
            hapus_item = int(input("Hapus item nomor : "))
            
            if 1 <= hapus_item <= len(baca):
                kondisi = False
            else:
                print("Masukkan nomor barang yang sudah ada di atas!")
        except:
            print("Masukkan input yang benar!")
    
    baca.drop(baca.index[hapus_item - 1], inplace=True)
    baca.to_csv(file_barang, index=False)
    
    print(f"\nBarang urutan {hapus_item} telah dihapus")

    i = input("\nTekan enter untuk kembali")
    
def edit_harga(user):
    sub_folder = os.path.join(folder_toko, f"toko_{user}")
    file_barang = os.path.join(sub_folder, f"toko_{user}.csv")
    
    baca = pd.read_csv(file_barang)
    
    os.system('cls')
    
    print("╔" + "═"*48 + "╗")
    print("║" + "Edit Harga".center(48) + "║")
    print("╚" + "═"*48 + "╝")
    print()
    
    if baca.empty:
        print("Tidak ada barang dalam toko ini!")
        
        i = input("\nTekan enter untuk kembali")
        return
    
    print("List barang:")
    for index, row in baca.iterrows():
        barang = row["barang"]
        harga = row["harga"]
        stok = row["stok"]
        print(f"{index + 1}. {barang} | harga = {harga} | stok = {stok}")
        
    kondisi = True
    
    print()
    
    while kondisi:
        try:
            index_ubah = int(input("Ubah item nomor : "))
            
            if 1 <= index_ubah <= len(baca):
                kondisi = False
            else:
                print("Masukkan nomor barang yang sudah ada di atas!")
        except:
            print("Masukkan input yang benar!")
    
    barang_dipilih = baca.iloc[index_ubah-1]
    print(f"\nBarang yang dipilih: {barang_dipilih['barang']} | harga saat ini = {barang_dipilih['harga']}\n")
    
    kondisi2 = True
    
    while kondisi2:
        try:
            harga_baru = int(input("Masukkan harga baru : "))
            
            kondisi2 = False
        except:
            print("Masukkan input berupa angka!")
            
    baca.at[index_ubah-1, "harga"] = harga_baru
    baca.to_csv(file_barang, index=False)
    
    print(f"\nHarga barang '{barang_dipilih['barang']}' berhasil diubah menjadi {harga_baru}.")
    
    i = input("\nTekan enter untuk kembali")
    
def edit_stok(user):
    sub_folder = os.path.join(folder_toko, f"toko_{user}")
    file_barang = os.path.join(sub_folder, f"toko_{user}.csv")
    
    baca = pd.read_csv(file_barang)
    
    os.system('cls')
    
    print("╔" + "═"*48 + "╗")
    print("║" + "Edit Stok".center(48) + "║")
    print("╚" + "═"*48 + "╝")
    print()
    
    if baca.empty:
        print("Tidak ada barang dalam toko ini!")
        
        i = input("\nTekan enter untuk kembali")
        return
    
    print("List barang:")
    for index, row in baca.iterrows():
        barang = row["barang"]
        harga = row["harga"]
        stok = row["stok"]
        print(f"{index + 1}. {barang} | harga = {harga} | stok = {stok}")
        
    kondisi = True
    
    print()
    
    while kondisi:
        try:
            index_ubah = int(input("Ubah item nomor : "))
            
            if 1 <= index_ubah <= len(baca):
                kondisi = False
            else:
                print("Masukkan nomor barang yang sudah ada di atas!")
        except:
            print("Masukkan input yang benar!")
    
    barang_dipilih = baca.iloc[index_ubah-1]
    print(f"\nBarang yang dipilih: {barang_dipilih['barang']} | stok saat ini = {barang_dipilih['stok']}\n")
    
    kondisi2 = True
    
    while kondisi2:
        try:
            stok_baru = int(input("Masukkan stok baru : "))
            
            kondisi2 = False
        except:
            print("Masukkan input berupa angka!")
            
    baca.at[index_ubah-1, "stok"] = stok_baru
    baca.to_csv(file_barang, index=False)
    
    print(f"\nStok barang '{barang_dipilih['barang']}' berhasil diubah menjadi {stok_baru}.")
    
    i = input("\nTekan enter untuk kembali")
      
#PROGRAM UTAMA
def main():
    os.system('cls')
    
    cek_data()
    
    kondisi = True
    
    while kondisi:
        print("╔" + "═"*48 + "╗")
        print("║" + "NANDOER".center(48) + "║")
        print("╠" + "═"*48 + "╣")
        print("║" + "Pilihan Terpercaya Petani Indonesia".center(48) + "║")
        print("╚" + "═"*48 + "╝") 
        print("\n1. Registrasi\n2. Login\n3. Keluar\n")
        
        kondisi2 = True
        
        while kondisi2:
            pilihan = input("Masukkan pilihan (1/2/3): ")
            
            if pilihan == "1":
                register()
                kondisi2 = False
                os.system('cls')
                '''pilihan2 = input("\n(Y) untuk kembali | (enter) untuk keluar : ").lower()
                if pilihan2 == "y":
                    os.system("cls")
                else:
                    kondisi = False'''
            elif pilihan == "2":
                login()
                kondisi2 = False
                os.system('cls')
                '''pilihan2 = input("\n(Y) untuk kembali | (enter) untuk keluar : ").lower()
                if pilihan2 == "y":
                    os.system("cls")
                else:
                    kondisi = False'''
            elif pilihan == "3":
                kondisi = False
                kondisi2 = False
            else:
                os.system("cls")
                print("╔" + "═"*48 + "╗")
                print("║" + "NANDOER".center(48) + "║")
                print("╠" + "═"*48 + "╣")
                print("║" + "Pilihan Terpercaya Petani Indonesia".center(48) + "║")
                print("╚" + "═"*48 + "╝") 
                print("\n1. Registrasi\n2. Login\n3. Keluar\n")
                print("Input anda tidak sesuai pilihan!")
    
    print("\nTerima kasih telah menggunakan program ini :)")
    
main()
