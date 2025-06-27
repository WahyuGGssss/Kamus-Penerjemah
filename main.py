print("Selamat datang di Aplikasi Kamus Meme!")
print("Ketik kata yang tidak Kamu mengerti (gunakan HURUF KAPITAL semua!)")
print("Kami akan mencoba menjelaskan artinya...\n")

# Kamus
meme_dict = {
    "LOL": "Tanggapan terhadap sesuatu yang lucu",
    "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
    "ROFL": "Tanggapan terhadap lelucon",
    "SHEESH": "Sedikit ketidaksetujuan",
    "CREEPY": "Menakutkan, tidak menyenangkan",
    "AGGRO": "Untuk menjadi agresif/marah"
}

# Tanya pengguna 5 kali
for i in range(5):
    word = input(str(i + 1) + ". Ketik kata: ")
    if word in meme_dict:
        print("Arti '" + word + "': " + meme_dict[word] + "\n")
    else:
        print("Maaf, kami tidak tahu arti dari '" + word + "'.\n")

print("Terima kasih telah menggunakan Kamus Meme!")
