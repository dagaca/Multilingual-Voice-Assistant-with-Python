import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
from deep_translator import GoogleTranslator
import inflect

def dinle():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinleniyor...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Anlasiliyor...")
        sorgu = recognizer.recognize_google(audio, language="tr-TR")
        print(f"Soylediginiz: {sorgu}")
        return sorgu.lower()
    except sr.UnknownValueError:
        print("Uzgunum, ne dediginizi anlayamadim.")
        return ""
    except sr.RequestError as e:
        print(f"Google Konusma Tanima servisinden sonuc alinamadi; {e}")
        return ""

def konus(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def zaman_al():    
    p = inflect.engine()
    sayisal_saat = datetime.datetime.now().strftime("%H")
    sayisal_dakika = datetime.datetime.now().strftime("%M")

    ingilizce_saat_metin = p.number_to_words(sayisal_saat)
    ingilizce_dakika_metin = p.number_to_words(sayisal_dakika)

    ingilizce_metin = f"{ingilizce_saat_metin} hour {ingilizce_dakika_metin} minute"

    try:
        tercume = GoogleTranslator(source='en', target='tr').translate(ingilizce_metin)
        return tercume
    
    except Exception as e:
        return f"Hata oluştu: {e}"

def tarih_al():
    p = inflect.engine()
    sayisal_yil = datetime.datetime.now().strftime("%Y")
    sayisal_ay = datetime.datetime.now().strftime("%B")
    sayisal_day = datetime.datetime.now().strftime("%d")

    ingilizce_yil_metin = p.number_to_words(sayisal_yil)
    ingilizce_ay_metin = p.number_to_words(sayisal_ay)
    ingilizce_day_metin = p.number_to_words(sayisal_day)


    # İngilizce tarih açıklamasını ve tarihi birleştir
    ingilizce_metin = f"{ingilizce_yil_metin} Year {ingilizce_ay_metin} Moon {ingilizce_day_metin} Day"

    try:
        tercume = GoogleTranslator(source='en', target="tr").translate(ingilizce_metin)

        # Çevrilen metni sesli olarak söyle
        return tercume
    
    except Exception as e:
        return f"Hata oluştu: {e}"
    
def cevir():
    konus("Hangi metni çevirmemi istersiniz?")
    metin_sorgusu = dinle()

    try:
        # İngilizce metni çevir
        cevirisi = GoogleTranslator(source='en', target='tr').translate(metin_sorgusu)

        # Çevrilen metni terminale yaz ve sesli olarak oku
        print(f"Çevrilen Metin: {cevirisi}")
        konus(f"Çevrilen Metin: {cevirisi}")

    except Exception as e:
        print(f"Çeviri sırasında bir hata oluştu: {e}")
        konus("Çeviri sırasında bir hata oluştu. Lütfen tekrar deneyin.")

def wikipedia_bilgi(sorgu):
    hedef_dil = "tr"
    try:
        ingilizce_bilgi = wikipedia.summary(sorgu, sentences=2)
        tercume = GoogleTranslator(source='en', target=hedef_dil).translate(ingilizce_bilgi)
        return tercume
    except wikipedia.exceptions.DisambiguationError as e:
        secenekler = e.options[:5]
        return f"Coklu sonuc bulundu. Lutfen sorgunuzu belirtin. Secenekler: {', '.join(secenekler)}"
    except wikipedia.exceptions.PageError:
        return f"Uzgunum, '{sorgu}' hakkinda hicbir bilgi bulamadim."
    except wikipedia.exceptions.WikipediaException as e:
        return f"Bir hata olustu: {e}"

def web_sitesi_ac(sorgu):
    base_url = "https://www."  # Temel URL
    end_url = ".com/"  # URL'nin sonu

    # Girilen sorguyu küçük harfe çevirip boşlukları '-' ile değiştir
    formatli_sorgu = sorgu.lower().replace(' ', '-')

    # Tam URL'yi oluştur
    tam_url = f"{base_url}{formatli_sorgu}{end_url}"

    konus(f"{tam_url} adresini varsayilan web tarayicinizda aciyorum.")
    webbrowser.open(tam_url)

def muzik_cal():
    konus("Tabii, hangi muzigi dinlemek istersiniz?")
    muzik_sorgu = dinle()

    # YouTube arama URL'sini oluştur
    arama_url = f"https://www.youtube.com/results?search_query={muzik_sorgu.replace(' ', '+')}"

    # YouTube arama sonuçlarını varsayılan web tarayıcısında aç
    webbrowser.open(arama_url)

    return f"YouTube'da {muzik_sorgu} aranıyor. Lütfen oynatılacak videoyu seçin."

def not_yaz():
    konus("Ne yazmaliyim, efendim?")
    not_al = ""

    while True:
        kullanici_girisi = dinle()
        not_al += kullanici_girisi + " "
        print(f"Mevcut Not: {not_al}")

        if "çıkış" in not_al.lower():
            break

    # "not kaydet" içermeyen kısmını al, "not kaydet" ve sonrasını at
    not_al = not_al.lower().replace("not kaydet", "").strip()

    dosya = open('notlar.txt', 'a')  # Notları eklemek için 'a' modunu kullanıyoruz (append)
    dosya.write(f"{not_al}\n")
    konus("Not kaydedildi.")

    dosya.close()