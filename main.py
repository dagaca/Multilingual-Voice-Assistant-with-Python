from voice_assistant_english import listen, speak, get_time, get_date, translate, get_wikipedia, open_website, play_music, write_note
from voice_assistant_turkish import dinle, konus, zaman_al, tarih_al, cevir, wikipedia_bilgi, web_sitesi_ac, muzik_cal, not_yaz


def main():
    speak("Hello select language. Just say English or Turkish.")
    
    select = listen()
    if "turkish" in select.lower():
        konus("Merhaba! Size nasil yardimci olabilirim?")
        while True:
            komut = dinle()

            if "çıkış" in komut:
                konus("Gorusmek uzere!")
                break

            if "adın ne" in komut:
                konus("Ben Python ile olusturulmus basit bir sesli asistanim.")

            elif "zaman" in komut:
                konus(zaman_al())

            elif "tarih" in komut:
                konus(tarih_al())

            elif "arama" in komut:
                konus("Ne icin arama yapmami istersiniz?")
                arama_sorgusu = dinle()
                konus(wikipedia_bilgi(arama_sorgusu))
            
            elif "çevir" in komut:
                cevir()
            
            elif "web sitesi aç" in komut:
                konus("Tabii, hangi web sitesini acmami istersiniz?")
                web_sitesi_sorgusu = dinle()
                web_sitesi_ac(web_sitesi_sorgusu)

            elif "müzik çal" in komut:
                konus(muzik_cal())

            elif "not yaz" in komut:
                not_yaz()
                
                
    elif "english" in select.lower():
        speak("Hello! How can I assist you today?")
        while True:
            command = listen()

            if "exit" in command:
                speak("Goodbye!")
                break

            if "your name" in command:
                speak("I am a simple voice assistant created with Python.")

            elif "time" in command:
                speak(get_time())

            elif "date" in command:
                speak(get_date())

            elif "search" in command:
                speak("What would you like me to search for?")
                search_query = listen()
                speak(get_wikipedia(search_query))
                
            elif "translate" in command:
                translate()
            
            elif "open website" in command:
                speak("Sure, what website would you like to open?")
                website = listen()
                open_website(website)

            elif "play music" in command:
                speak(play_music())

            elif "write a note" in command:
                write_note() 


if __name__ == "__main__":
    main()