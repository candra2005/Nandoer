import os
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
        seller = pd.concat([seller, data_baru_df])
        seller.to_csv(FILE_USER)     
        
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
        seller = pd.concat([buyer, data_baru_df])
        seller.to_csv(FILE_USER)    
        
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
                kondisi2 = False
            elif pilihan == "2":
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
        
        print("\n1. Profil akun\n2. Edit barang\n3. Histori penjualan\n4. Total penjualan\n5. Keluar akun")
        
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
                elif pilihan == "5":
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
    folder_data = os.path.join(folder_toko, f"toko_{user}.csv")
    
    if not os.path.exists(f"toko_{user}.csv"):  
        user_df = pd.DataFrame(columns=["barang", "harga", "stok"]) 
        user_df.to_csv(folder_data) 
        
    kondisi = True

    while kondisi:
        os.system('cls')
        
        print("╔" + "═"*48 + "╗")
        print("║" + "Edit Barang".center(48) + "║")
        print("╚" + "═"*48 + "╝")
        
        print("\n1. Tambah jenis barang\n2. Hapus jenis barang\n3. Edit harga\n4. Edit stok barang\n5. Kembali")
        
        kondisi2 = True
            
        while kondisi2:
                pilihan = input("\nGunakan menu nomor : ")
                
                if pilihan == "1":
                    kondisi2 = False
                elif pilihan == "2":
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

#PROGRAM UTAMA
def main():
    
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
                pilihan2 = input("\n(Y) untuk kembali | (enter) untuk keluar : ").lower()
                if pilihan2 == "y":
                    os.system("cls")
                else:
                    kondisi = False
            elif pilihan == "2":
                login()
                kondisi2 = False
                pilihan2 = input("\n(Y) untuk kembali | (enter) untuk keluar : ").lower()
                if pilihan2 == "y":
                    os.system("cls")
                else:
                    kondisi = False
                
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
