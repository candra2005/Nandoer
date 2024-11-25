import os
import pandas as pd

FILE_BUYER = "data_buyer.csv"
FILE_SELLER = "data_seller.csv"
FILE_ADMIN = "data_admin.csv"

def cek_data():
    if not os.path.exists(FILE_BUYER):  
        user = pd.DataFrame(columns=["username", "password", "telepon"]) 
        user.to_csv(FILE_BUYER, index=False) 
    if not os.path.exists(FILE_SELLER):  
        user = pd.DataFrame(columns=["username", "password", "telepon"]) 
        user.to_csv(FILE_SELLER, index=False)
    if not os.path.exists(FILE_ADMIN):  
        user = pd.DataFrame(columns=["username", "password"]) 
        user.to_csv(FILE_ADMIN, index=False) 

def register():
    os.system("cls")
        
    print("╔" + "═"*38 + "╗")
    print("║" + "Registrasi Akun".center(38) + "║")
    print("╚" + "═"*38 + "╝")
        
    print("\n1. Penjual\n2. Pembeli\n3. Kembali\n")
    pilihan = input("Registrasi sebagai : ")
        
    if pilihan == "1":
        os.system("cls")
        
        seller = pd.read_csv(FILE_SELLER)
        
        kondisi = True
        kondisi2 = True
        kondisi3 = True
        
        print("╔" + "═"*38 + "╗")
        print("║" + "Registrasi Akun".center(38) + "║")
        print("║" + "Penjual".center(38) + "║")
        print("╚" + "═"*38 + "╝")
        print()
        
        while kondisi:
            username = input("Masukkan username : ")
            
            if username in seller["username"].values:
                print("Username sudah digunakan, silahkan gunakan username lain.")
            else:
                kondisi = False
        
        while kondisi2:
            password = input("Masukkan password : ")
            
            if len(password) < 8:
                print("Password harus berisi minimal 8 karakter!")
            else:
                kondisi2 = False
        
        while kondisi3:
            try:
                telepon = int(input("Masukkan nomor telepon : "))
                
                kondisi3 = False
            except:
                print("Masukan berupa angka!")
                
        data_baru = {"username": username, "password": password, "telepon": telepon}
        data_baru_df = pd.DataFrame([data_baru])
        seller = pd.concat([seller, data_baru_df], ignore_index=True)
        seller.to_csv(FILE_SELLER, index=False)    
        
        print(f"\nRegistrasi {username} sebagai penjual telah berhasil") 
        
    elif pilihan == "2":
        os.system("cls")
        
        seller = pd.read_csv(FILE_BUYER)
        
        kondisi = True
        kondisi2 = True
        kondisi3 = True
        
        print("╔" + "═"*38 + "╗")
        print("║" + "Registrasi Akun".center(38) + "║")
        print("║" + "Pembeli".center(38) + "║")
        print("╚" + "═"*38 + "╝")
        print()
        
        while kondisi:
            username = input("Masukkan username : ")
            
            if username in seller["username"].values:
                print("Username sudah digunakan, silahkan gunakan username lain.")
            else:
                kondisi = False
        
        while kondisi2:
            password = input("Masukkan password : ")
            
            if len(password) < 8:
                print("Password harus berisi minimal 8 karakter!")
            else:
                kondisi2 = False
        
        while kondisi3:
            try:
                telepon = int(input("Masukkan nomor telepon : "))
                
                kondisi3 = False
            except:
                print("Masukan berupa angka!")
                
        data_baru = {"username": username, "password": password, "telepon": telepon}
        data_baru_df = pd.DataFrame([data_baru])
        seller = pd.concat([seller, data_baru_df], ignore_index=True)
        seller.to_csv(FILE_BUYER, index=False)    
        
        print(f"\nRegistrasi {username} sebagai penjual telah berhasil") 
        
    elif pilihan == "3":
        pass
    else:
        print("Masukan anda salah, anda akan dikembalikan ke menu")
        

def login():
    os.system("cls")
        
    print("╔" + "═"*38 + "╗")
    print("║" + "Login Akun".center(38) + "║")
    print("╚" + "═"*38 + "╝")
        
    print("\n1. Admin\n2. Penjual\n3. Pembeli\n4. Kembali\n")
    pilihan = input("Login sebagai : ")
    
    if pilihan == "1":
        os.system("cls")
        
        admin = pd.read_csv(FILE_ADMIN)
        
        i = 0
        
        print("╔" + "═"*38 + "╗")
        print("║" + "Login Akun".center(38) + "║")
        print("║" + "Admin".center(38) + "║")
        print("╚" + "═"*38 + "╝")
        
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
    
    if pilihan == "2":
        os.system("cls")
        
        seller = pd.read_csv(FILE_SELLER)
        
        i = 0
        
        print("╔" + "═"*38 + "╗")
        print("║" + "Login Akun".center(38) + "║")
        print("║" + "Penjual".center(38) + "║")
        print("╚" + "═"*38 + "╝")
        
        while i < 3:
            seller["username"] = seller["username"].astype(str)
            seller["password"] = seller["password"].astype(str)

            username = input("\nMasukkan username : ")
            password = input("Masukkan password : ")

            user = seller[(seller["username"] == username) & (seller["password"] == password)]
            if not user.empty:
                menu_penjual(username)
                i+=3
            else:
                print("\nLogin gagal! Username atau password salah.")
                i+=1
    
    elif pilihan == "3":
        os.system("cls")
        
        buyer = pd.read_csv(FILE_BUYER)
        
        i = 0
        
        print("╔" + "═"*38 + "╗")
        print("║" + "Login Akun".center(38) + "║")
        print("║" + "Pembeli".center(38) + "║")
        print("╚" + "═"*38 + "╝")
        
        while i < 3:
            buyer["username"] = buyer["username"].astype(str)
            buyer["password"] = buyer["password"].astype(str)

            username = input("\nMasukkan username : ")
            password = input("Masukkan password : ")

            user = buyer[(buyer["username"] == username) & (buyer["password"] == password)]
            if not user.empty:
                menu_pembeli(username)
                i+=3
            else:
                print("\nLogin gagal! Username atau password salah.")
                i+=1
    
def menu_admin(user):
    os.system('cls')
    
    print("=" * 40)
    print("Menu Admin".center(40))
    print(user.center(40))
    print("=" * 40)
    
    print("\n1. List akun seller\n2. List akun buyer\n3. Total Penjualan\n4. Keluar akun")
    i = input()
    
def menu_penjual(user):
    os.system('cls')
    
    print("=" * 40)
    print("Menu Penjual".center(40))
    print(user.center(40))
    print("=" * 40)
    
    print("\n1. Tambah barang\n2. Hasil penjualan\n3. Keluar akun")
    i = input()
    
def menu_pembeli(user):
    os.system('cls')
    
    print("=" * 40)
    print("Menu Pembeli".center(40))
    print(user.center(40))
    print("=" * 40)
    
    print("\n1. Beli barang\n2. Keluar akun")
    i = input()

def main():
    
    cek_data()
    
    kondisi = True
    
    while kondisi:
        print("╔" + "═"*38 + "╗")
        print("║" + "NANDOER".center(38) + "║")
        print("╠" + "═"*38 + "╣")
        print("║" + "Pilihan Terpercaya Petani Indonesia".center(38) + "║")
        print("╚" + "═"*38 + "╝") 
        print("\n1. Registrasi\n2. Login\n3. Keluar\n")
        
        kondisi2 = True
        
        while kondisi2:
            pilihan = input("Masukkan pilihan (1/2/3): ")
            
            if pilihan == "1":
                register()
                kondisi2 = False
                pilihan2 = input("\nKetik y jika ingin kembali ke halaman awal atau ketik sembarang jika ingin keluar : ")
                if pilihan2 == "y":
                    os.system("cls")
                else:
                    kondisi = False
            elif pilihan == "2":
                login()
                kondisi2 = False
                pilihan2 = input("\nKetik y jika ingin kembali ke halaman awal atau ketik sembarang jika ingin keluar : ")
                if pilihan2 == "y":
                    os.system("cls")
                else:
                    kondisi = False
                
            elif pilihan == "3":
                kondisi = False
                kondisi2 = False
            else:
                os.system("cls")
                print("╔" + "═"*38 + "╗")
                print("║" + "NANDOER".center(38) + "║")
                print("╠" + "═"*38 + "╣")
                print("║" + "Pilihan Terpercaya Petani Indonesia".center(38) + "║")
                print("╚" + "═"*38 + "╝") 
                print("\n1. Registrasi\n2. Login\n3. Keluar\n")
                print("Input anda tidak sesuai pilihan!")
    
    print("\nTerima kasih telah menggunakan program ini :)")
    
main()
