import pandas as pd
import random

# Her intent için zenginleştirilmiş örnek ifadeler
intent_examples = {
    "Greeting": [
        "Merhaba", "Selam", "İyi günler", "Günaydın", "İyi akşamlar", "Nasılsınız?",
        "Size nasıl yardımcı olabilirim?", "Sorularınızı yanıtlamaya hazırım", "Selamlar!",
        "Destek için buradayım", "Yardımcı olabilir miyim?"
    ],
    "Goodbye": [
        "Hoşçakal", "Görüşmek üzere", "İyi günler", "Kendinize iyi bakın", "Tekrar görüşürüz",
        "İyi akşamlar", "Görüşürüz", "Hoşça kal", "Şimdilik hoşça kalın", "Güle güle"
    ],
    "Reject": [
        "Hayır", "İlgilenmiyorum", "Teşekkürler, hayır", "Şimdilik gerek yok",
        "Hayır teşekkür ederim", "Şu an istemiyorum", "Gerek yok", "İstemiyorum"
    ],
    "DepartmentInfo": [
        "Bilgisayar mühendisliği hakkında bilgi verir misiniz?",
        "Bilgisayar mühendisliği nedir?", "Bilgisayar bölümü nasıl bir bölüm?",
        "Ders içerikleri hakkında bilgi alabilir miyim?", "Bölümde hangi dersler var?",
        "Bilgisayar bölümü ders programı nasıldır?"
    ],
    "ScholarshipInfo": [
        "Burs başvurusu nasıl yapılır?", "Burs olanakları nelerdir?", "Üniversitede burs veriliyor mu?",
        "Burs almak için ne yapmalıyım?", "Burs imkanlarınız nedir?", "Maddi destek sağlıyor musunuz?"
    ],
    "DormitoryInfo": [
        "Yurt hakkında bilgi verir misiniz?", "Yurtlar nasıl?", "Yurt başvurusu ne zaman?",
        "Yurt imkanları nelerdir?", "Yurt ücretleri ne kadar?", "Kampüste yurt var mı?"
    ],
    "Registration": [
        "Üniversite kayıtları ne zaman başlıyor?", "Kayıt işlemleri nasıl yapılır?",
        "Online kayıt mümkün mü?", "Kayıt için gerekli belgeler nelerdir?",
        "Kayıt tarihi nedir?", "Kayıtla ilgili bilgi verir misiniz?"
    ],
    "ContactInfo": [
        "İletişim bilgileriniz nedir?", "Telefon numaranız nedir?",
        "Size nasıl ulaşabilirim?", "E-posta adresiniz nedir?", "Ofisiniz nerede?",
        "İletişim kurmak istiyorum"
    ],
    "EventInfo": [
        "Etkinlikler hakkında bilgi verir misiniz?", "Kampüste etkinlik oluyor mu?",
        "Etkinlik takvimi nedir?", "Üniversitede hangi etkinlikler var?",
        "Bir etkinlik düzenleniyor mu?", "Etkinlikleri nereden takip edebilirim?"
    ],
    "AcademicCalendar": [
        "Akademik takvim açıklandı mı?", "Dersler ne zaman başlıyor?",
        "Sınav haftası ne zaman?", "Tatiller hangi tarihlerde?",
        "Akademik yıl başlangıcı nedir?", "Akademik program ne zaman başlıyor?"
    ]
}

# Hedef satır sayısı
target_size = 1000
data = []

# Verileri oluştur
while len(data) < target_size:
    for intent, examples in intent_examples.items():
        example = random.choice(examples)
        data.append({"Intent": intent, "Example": example})
        if len(data) >= target_size:
            break

# DataFrame oluştur ve dışa aktar
df = pd.DataFrame(data)
df.to_excel("university_intents_1000.xlsx", index=False)

print("Veri seti başarıyla oluşturuldu ve kaydedildi.")
