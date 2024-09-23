def hapus_baris_baru(nama_file_input, nama_file_output):
    try:
        with open(nama_file_input, 'r') as file_input:
            teks = file_input.read().replace('\n', '')

        with open(nama_file_output, 'w') as file_output:
            file_output.write(teks)
        
        print(f"Berkas '{nama_file_input}' berhasil dikonversi menjadi tanpa baris baru dan disimpan di '{nama_file_output}'")
    
    except FileNotFoundError:
        print(f"Berkas '{nama_file_input}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

nama_file_input = "input.txt"
nama_file_output = "output.txt"

hapus_baris_baru(nama_file_input, nama_file_output)