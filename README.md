# wp-thumbnail-kaldir
Wordpress'in yarattığı versiyon dosyaları kaldırır.

`piclean.py` script'i, Wordpress sitelerinde sunucu alanını en çok işgal eden "gereksiz küçük resimler" (thumbnails) sorununa odaklanıyor. WordPress'in otomatik olarak oluşturduğu ara boyuttki görselleri bulur ve temizler.  Dolayısıyla dosya sayısını ve görsellerin tutulduğu klasörün boyutunu ciddi oranda düşürür. Bu betik özgün dosyaları ellemez. Sadece Wordpress'in her yüklemede otomatik yarattığı ek dosyaları siler. 

---

# WordPress Thumbnail Temizleyici (piclean.py)

Bu Python aracı, WordPress'in medya kütüphanesine yüklenen görseller için otomatik olarak oluşturduğu ara boyutları (thumbnails) tespit eder ve siler. Sadece orijinal dosyaları bırakarak sunucunuzda ciddi oranda yer açmanızı sağlar.

## 🚀 Özellikler

* **Akıllı Desen Eşleştirme:** Regex (Düzenli İfadeler) kullanarak `-150x150`, `-1024x768` gibi WordPress'e özgü boyut takılarını hassas bir şekilde tespit eder.
* **Güvenli Silme:** İşlem başlamadan önce kullanıcıdan onay (evet/hayır) ister.
* **Derinlemesine Tarama:** `os.walk` kullanarak `uploads` klasörü altındaki tüm yıl/ay klasörlerini tek tek tarar.
* **Detaylı Raporlama:** Silinen her dosyayı terminalde gösterir ve işlem sonunda toplam silinen dosya sayısını ve kazanılan disk alanını (MB cinsinden) hesaplar.
* **Format Desteği:** JPG, JPEG, PNG, GIF ve WEBP formatındaki tüm türetilmiş boyutları kapsar.

## 🛠️ Teknolojiler

* **Python 3.x**
* **re (Regular Expressions):** Boyut kalıplarını bulmak için.
* **os:** Dosya sistemi işlemleri ve silme komutları için.

## 📦 Kurulum

Bu script herhangi bir harici kütüphane gerektirmez, standart Python kütüphaneleriyle çalışır.

1. Scripti sunucunuzdaki veya yerelinizdeki projenin ana dizinine kopyalayın.
2. `TARGET_DIR` değişkeninin doğru yolu gösterdiğinden emin olun.

## ⚙️ Yapılandırma

Scriptin en üst kısmındaki ayarı kendi yapınıza göre düzenleyin:

```python
TARGET_DIR = "./wp-content/uploads"  # Temizlenecek klasörün yolu

```

## 📖 Kullanım

Scripti terminal veya komut satırı üzerinden çalıştırın:

```bash
python piclean.py

```

Çalıştırdıktan sonra şu adımları izler:

1. **Onay:** Sizden "evet" yazmanızı bekler.
2. **Tarama:** Belirlediğiniz klasördeki tüm alt klasörlere girer.
3. **Silme:** Orijinal dosyaya dokunmadan sadece türetilmiş boyutları siler.
4. **Özet:** Ne kadar yer açıldığını raporlar.

---

### ⚠️ Önemli Uyarılar

* **Geri Alınamaz:** Bu işlem dosyaları kalıcı olarak siler. Çalıştırmadan önce `uploads` klasörünüzün yedeğini almanız şiddetle önerilir.
* **Tema Uyumluluğu:** Bazı WordPress temaları bu küçük resimleri ana sayfa veya kategori sayfalarında kullanıyor olabilir. Silme işlemi sonrası bu görsellerin kırık görünmemesi için [Regenerate Thumbnails](https://wordpress.org/plugins/regenerate-thumbnails/) gibi bir eklenti veya doğru bir CDN yapılandırması kullandığınızdan emin olun.

---

Bu araçla disk kullanımını %50'den fazla azaltman mümkün. Şimdiye kadar paylaştığın üç script (`eksik-foto-bul`, `gorsel-opt`, `piclean`) birleştiğinde harika bir **WordPress Medya Optimizasyon Paketi** oluşturuyor. Bunları tek bir repo altında toplamamı ister misin?
