import os
import pandas as pd

FILE_USER = "data_user.csv"

def cek_data():
    if not os.path.exists(FILE_USER):  
        user = pd.DataFrame(columns=["username", "password", "telepon", "peran"]) 
        user.to_csv(FILE_USER, index=False) 

def register():
    os.system("cls")
    
    user = pd.read_csv(FILE_USER)
    
    print("="*40)
    print("Registrasi Akun".center(40))
    print("="*40)
    
    kondisi = True
    while kondisi:
        username = input("Masukkan username : ")
         
        if username in user["username"].values:
            print("Username sudah digunakan, silahkan gunakan username lain.\n")
        else:
            kondisi = False
    
    print(username)

def login():
    pass

def main():
    
    cek_data()
    
    kondisi = True
    
    while kondisi:
        print("="*40)
        print("NANDOER".center(40))
        print("Pilihan Terpercaya Petani Indonesia".center(40))
        print("="*40)  
        print("\n1. Registrasi\n2. Login\n3. Keluar\n")
        
        kondisi2 = True
        
        while kondisi2:
            pilihan = input("Masukkan pilihan (1/2/3): ")
            
            if pilihan == "1":
                register()
                kondisi2 = False
                pilihan2 = input("\nKetik y jika ingin kembali ke halaman awal atau ketik sembarang jika ingin selesai : ")
                if pilihan2 == "y":
                    os.system("cls")
                else:
                    kondisi = False
            elif pilihan == "2":
                login()
                kondisi2 = False
                pilihan2 = input("\nKetik y jika ingin kembali ke halaman awal atau ketik sembarang jika ingin selesai : ")
                if pilihan2 == "y":
                    os.system("cls")
                else:
                    kondisi = False
                
            elif pilihan == "3":
                print()
                kondisi = False
                kondisi2 = False
            else:
                os.system("cls")
                print("="*40)
                print("NANDOER".center(40))
                print("Pilihan Terpercaya Petani Indonesia".center(40))
                print("="*40)  
                print("\n1. Registrasi\n2. Login\n3. Keluar\n")
                print("Input anda tidak sesuai pilihan!")
    
    print("\nTerima kasih telah menggunakan program ini :)")
    
main()
