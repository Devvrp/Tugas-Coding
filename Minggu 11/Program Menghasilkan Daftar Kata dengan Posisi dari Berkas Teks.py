def daftar_kata_dengan_posisi(nama_file_input, nama_file_output):
    try:
        with open(nama_file_input, 'r') as file_input:
            teks = file_input.read()
            kata_list = teks.split()
        
        with open(nama_file_output, 'w') as file_output:
            for posisi, kata in enumerate(kata_list, start=1):
                file_output.write(f"{posisi}: {kata}\n")
        
        print(f"Daftar kata beserta posisinya berhasil disimpan di '{nama_file_output}'")
    
    except FileNotFoundError:
        print(f"Berkas '{nama_file_input}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

nama_file_input = "input.txt"
nama_file_output = "output_kata_dan_posisi.txt"

daftar_kata_dengan_posisi(nama_file_input, nama_file_output)
