🎓 University Chatbot - LLM Tabanlı Akademik Asistan

Bu proje, üniversiteye dair temel bilgilere hızlı ve doğru şekilde yanıt verebilen bir yapay zekâ destekli sohbet botunun geliştirilmesini amaçlamaktadır. Chatbot, özellikle öğrencilerin akademik takvim, burs, yurt, kayıt işlemleri gibi sıkça sorulan sorularına cevap verebilecek şekilde tasarlanmıştır.

📌 Projenin Amacı

Bu projenin temel amacı, belirli "intent" türlerine göre etiketlenmiş veri setiyle eğitilen ve farklı büyük dil modelleri (LLM) ile karşılaştırmalı olarak test edilen bir chatbot geliştirmektir. Chatbot, önceden belirlenmiş intent (niyet) kategorilerine göre kullanıcıdan gelen ifadeleri sınıflandırmakta ve uygun yanıtları üretmektedir. 

Uygulama süreci aşağıdaki aşamaları kapsamaktadır:

1)	Intent tabanlı veri seti oluşturma

2)	LLM modelleri ile eğitme (BERT VE RoBERTa)

3)	Performans karşılaştırması (Precision, Recall, F1 Score)

4)	Uygulama arayüzü geliştirme (Streamlit)

📁 Veri Seti Oluşturma

Proje kapsamında Intent Classification için özel olarak 1000 satırlık bir veri seti oluşturulmuştur. Her satırda bir intent ve bu intent'e karşılık gelen örnek bir kullanıcı cümlesi yer almaktadır.

🎯 Intentler (Niyet Türleri)

Proje kapsamında aşağıdaki niyet türleri (intents) tanımlanmıştır:

•	Greeting – Selamlama

•	Goodbye – Vedalaşma

•	Reject – Reddetme

•	DepartmentInfo – Bölüm hakkında bilgi

•	ScholarshipInfo – Burs hakkında bilgi

•	DormitoryInfo – Yurt hakkında bilgi

•	Registration – Kayıt işlemleri

•	ContactInfo – İletişim bilgileri

•	EventInfo – Etkinlikler hakkında bilgi

•	AcademicCalendar – Akademik takvim

🔨 Veri Üretim Süreci

Veri seti, Python programlama dili kullanılarak otomatik bir şekilde oluşturulmuştur. Her intent türü için çeşitli örnek cümleler tanımlanmış, bu cümlelerden rastgele örnekler seçilerek toplamda 1000 satırlık bir etiketli veri seti üretilmiştir.
☁️ Kaggle Yüklemesi
Oluşturulan veri seti, analiz ve model eğitimlerinde kullanılmak üzere Kaggle platformuna yüklenmiştir.

🔗 Kaggle veri seti bağlantısı: https://www.kaggle.com/datasets/karun12345/intent-detection-for-university-q-and-a-chatbot

🧠 Kullanılan LLM Modelleri

Proje kapsamında iki farklı büyük dil modeli (LLM) ile chatbot eğitimi gerçekleştirilmiştir:

1)	BERT: Google tarafından geliştirilen ve doğal dil anlama görevlerinde yaygın olarak kullanılan bir dil modelidir. Projenin ilk sürümünde temel performansı test etmek amacıyla kullanılmıştır.

2)	RoBERTa: BERT’in daha büyük veriyle ve daha uzun süre eğitilmiş bir versiyonudur. Niyet sınıflandırma performansını artırmak amacıyla, BERT’ten sonra daha güçlü bir alternatif olarak projeye entegre edilmiştir.

Projenin ilk aşamasında T5 modeli denendi ancak düşük doğruluk oranları ve hatalı niyet tahminleri nedeniyle  T5 yerine daha başarılı sonuçlar veren BERT ve RoBERTa modelleri tercih edildi.





📌 Kullanılan Teknolojiler

	Python 
	OpenAI API
	Streamlit 
	Kaggle 
	Ngrok

🔑 Kullanılan API

OpenAI API (GPT-3.5 ile yanıt üretimi)

🔐 OpenAI API Anahtarı ve Entegrasyonu

	API Anahtarı Alma:

•	https://platform.openai.com adresinden hesap oluşturuldu.

•	API anahtarı, OpenAI dashboard üzerinden üretildi.

	API Entegrasyonu:

•	openai Python kütüphanesi kurularak projeye dahil edildi.

•	Anahtar, os.environ["OPENAI_API_KEY"] komutu ile güvenli şekilde çevresel değişken olarak tanımlandı.

•	GPT-3.5, client.chat.completions.create() fonksiyonu ile yanıt üretmek üzere çağrıldı.


🛠️ Model Eğitimi

Model, transformers kütüphanesi kullanılarak aşağıdaki adımlarla eğitilmiştir:

•	Veriler etiketlenip LabelEncoder ile sayısallaştırıldı.

•	train_test_split ile %80 eğitim, %20 doğrulama olacak şekilde ayrıldı.

•	AutoTokenizer ile veriler token’lara ayrıldı.

•	AutoModelForSequenceClassification ile RoBERTa ve BERT modeli, niyet sınıflandırması için fine-tune edildi.

•	Trainer ve TrainingArguments ile model eğitildi.

•	F1, accuracy, precision, recall gibi metrikler kullanılarak değerlendirme yapıldı.

🔓 Kullanım

Gereksinimleri yükle

	pip install -r requirements.txt

 Modeli eğit

Kodun ilgili kısmında model eğitimi yapılır. (Eğitilmiş model klasörü   models/roberta_intent_model  veya  models/bert_intent_model olarak kaydedilmiştir.)

Chatbot'u başlat

	streamlit run app.py

        Ngrok ile internete aç

	ngrok authtoken <tokenınız>

	public_url = ngrok.connect(8501)
	print("Public URL:", public_url)


📊 Sonuçlar

Modelin doğruluk ve F1 skoru gibi performans metrikleri Trainer.evaluate() ile hesaplanmış ve bir Confusion Matrix oluşturulmuştur.

BERT Modeli Değerlendirme Sonuçları:

![image](https://github.com/user-attachments/assets/3db1e3c9-a43b-45c8-8e00-bf28572d2f96)
![image](https://github.com/user-attachments/assets/537a551c-503b-401b-a2c0-2f9172e13818)

RoBERTa  Modeli Değerlendirme Sonuçları:

 ![image](https://github.com/user-attachments/assets/652adb36-d1e1-48ae-b753-9532b71c608b)
![image](https://github.com/user-attachments/assets/b2bdb6b4-d63a-4705-9d4b-20f988d45a91)


📊 Model Performansı Karşılaştırma Tablosu

![image](https://github.com/user-attachments/assets/934a9925-f711-45f5-9cbe-6fc23ac30cfc)


🖥️ Chatbot Arayüzü

Streamlit ile geliştirilen arayüz sayesinde kullanıcılar metin giriş alanına üniversiteyle ilgili sorularını yazabilirler. Sistem, soru metnini RoBERTa veya BERT modeline gönderir ve niyeti tahmin eder. Bu niyeti GPT-3.5'e ileterek uygun yanıt üretilmesini sağlar. Kullanıcıya tahmin edilen niyet ve yanıtı gösterir.

Streamlit Ekran Görüntüleri

RoBERTa + GPT3.5 Destekli Chatbot Tasarımı

Greeting Intent

![image](https://github.com/user-attachments/assets/3219459d-9eed-45c1-a16f-4286d769ec5b)

DormitoryInfo Intent

![image](https://github.com/user-attachments/assets/fe00b106-601e-40d4-9784-810d0dd4b5ae)

Registration Intent

![image](https://github.com/user-attachments/assets/9e299201-280e-4ba3-8ccc-96b213888fc5)

EventInfo Intent

![image](https://github.com/user-attachments/assets/26880d82-a721-4fc2-8443-591ff53773f9)

ContactInfo Intent

![image](https://github.com/user-attachments/assets/19909f81-be25-4d62-8a78-bdfcc972f7a5)

Goodbye Intent

![image](https://github.com/user-attachments/assets/40841783-e792-4d99-91bd-727eb915d942)

ScholarshipInfo Intent

![image](https://github.com/user-attachments/assets/6df01d6a-af31-4eab-9fc5-4fe340de8650)

DepartmentInfo Intent

![image](https://github.com/user-attachments/assets/84c69c3d-af4e-4ed4-a2cc-6da27ba1146d)

Reject Intent

![image](https://github.com/user-attachments/assets/f102989b-d8e0-4884-8519-ed0026c1dfc9)

 
 BERT + GPT3.5 Destekli Chatbot Tasarımı
 
![image](https://github.com/user-attachments/assets/6f04ac0c-cf4a-4576-81df-782ae1557b7d)

 



