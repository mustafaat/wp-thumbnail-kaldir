import os
import re

# --- AYARLAR ---
# uploads klasörünün tam yolunu buraya yazın
TARGET_DIR = "./wp-content/uploads"

# WordPress boyut desenini bulur: "-150x150.jpg", "-1024x768.png" vb.
size_pattern = re.compile(r'-\d+x\d+(\.(jpg|jpeg|png|gif|webp))$', re.IGNORECASE)

def clean_thumbnails():
    deleted_count = 0
    saved_space = 0
    
    print(f"--- Temizlik Başlıyor: {TARGET_DIR} ---")

    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if size_pattern.search(file):
                file_path = os.path.join(root, file)
                try:
                    # Dosya boyutunu hesapla (isteğe bağlı bilgi için)
                    file_size = os.path.getsize(file_path)
                    
                    # DOSYAYI SİL
                    os.remove(file_path)
                    
                    deleted_count += 1
                    saved_space += file_size
                    print(f"Silindi: {file}")
                except Exception as e:
                    print(f"Hata (Silinemedi): {file} -> {e}")

    print("\n--- İŞLEM TAMAMLANDI ---")
    print(f"Toplam Silinen Dosya: {deleted_count}")
    print(f"Kazanılan Alan: {saved_space / (1024*1024):.2f} MB")

if __name__ == "__main__":
    confirm = input("Bu işlem geri alınamaz. Devam etmek istediğine emin misin? (evet/hayır): ")
    if confirm.lower() == 'evet':
        clean_thumbnails()
    else:
        print("İşlem iptal edildi.")