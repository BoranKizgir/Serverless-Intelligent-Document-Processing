# Serverless-Intelligent-Document-Processing
Bu proje, AWS üzerinde tamamen sunucusuz (serverless) bir mimari kullanarak dökümanlardan (fatura, kimlik, kart vb.) otomatik veri ayıklayan bir boru hattı (pipeline) çözümüdür.
## Mimari (Architecture)

1. **Amazon S3**: Ham belgelerin yüklendiği veri gölü (Data Lake).
2. **AWS Lambda**: S3 tetikleyicisiyle çalışan ve iş mantığını yürüten işlem birimi.
3. **Amazon Textract**: Bilgisayarlı görü (OCR) ile metin ve form verisi analizi.
4. **Amazon DynamoDB**: İşlenen verilerin saklandığı NoSQL veritabanı.
5. **Amazon CloudWatch**: Sistem izleme ve hata günlükleme.

## Öne Çıkan Özellikler

- **Maliyet Optimizasyonu**: AWS Free Tier uyumlu, sadece işlem yapıldığında ücretlendirilen mimari.
- **Ölçeklenebilirlik**: S3 Event-Driven yapısı sayesinde binlerce belgeyi eşzamanlı işleyebilir.
- **Veri Bilimi**: Ham OCR çıktısını Regex ile temizleyerek yapılandırılmış veriye dönüştürme.

## Kurulum ve Kullanım

1. `src/lambda_function.py` dosyasını bir AWS Lambda fonksiyonuna yükleyin.
2. Lambda için gerekli IAM izinlerini (S3, Textract, DynamoDB) yapılandırın.
3. Bir S3 Bucket oluşturun ve Lambda'yı tetikleyici olarak ekleyin.
4. Herhangi bir görseli (JPG/PNG) bucket'a yükleyin ve sonuçları DynamoDB'den izleyin.
