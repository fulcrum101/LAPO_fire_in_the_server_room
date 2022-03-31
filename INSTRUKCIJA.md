# Spēles uzstādināšanā

1. Lejupladējiet `Python` programmēšanas valodu. `Python` versija `3.10.` (kas tika izmantots) ir pieejams [šeit](https://www.python.org/downloads/release/python-3100/).
2. Bibliotēkas `Pygame` lejupladēšana. Atvērot terminālu, palaidiet komandu `pip install pygame`. Pygame versija, ko mēs izmantojam ir Pygame `2.1.2.`.
3. Bibliotēkas `firebase_admin` lejupladēšana. Atvērot terminālu, palaidiet komandu `pip install firebase_admin`. Pygame versija, ko mēs izmantojam ir Pygame `5.2.0.`.
4. Lejupladējiet kodu no GitHub Repository https://github.com/fulcrum101/LAPO_fire_in_the_server_room
    a. kā .zip failu un dearhivējott to
    b. Caur `git clone` komandu vai GitHub Desktop (klonējot)

# Spēles sākums

## 1. veids - caur IDE (PyCharm vai VsCode u.c.)

1. Atveriet lejupladētu projektu savā IDE.
2. Palaidiet `main.py` failu.

## 2. veids - caur terminālu.

1. Atveriet lejupladēta projekta mapītes adresi lietojot komandu `cd filepath\to\project\folder`.
2. Izmanotjot komandu `python main.py` palaidiet `main.py`.

### *Piebilde:* Lejuplādēto bobliotēku versijas var parbaudīt palaidot `Library_version.py`.

# Noteikumu lasīšana

- Noteikumus var palasīt spiežot jebkurā laika brīdī uz taustiņu `n`. Noteikumi parādas terminālā.

# Spēles kontrole - Menu

## Main menu

- Kursoru var kustīnat spiežot uz ↑ un ↓ taustītem.
- Lai izvēlēties kādu menu punktu, uzspiediet `Enter`.
- Lai atgriezties atpakaļ, uzspiediet uz `Backspace`.

## Iestatījumu menu

- Skaņas skaļuma palielināšana par 10% veic ↑ taustīte.
- Skaņas skaļuma palielināšana par 10% veic ↓ taustīte.

## Auto izvelēšanas menu

- Kursoru kustīna izmantojot ← un → taustītes.
- Lai izvelēties automašīnas dizainu, uzspiediet uz `Enter`.

# Auto trasē spēlīte

- Lai mainīt joslu, spiediet uz ← un → taustītēm.

# Jautājumu atbilžu izvēle (gan kontrolpunktiem, gan uzlādešanas stācijam)

- Kursoru var kustīnat spiežot uz ↑ un ↓ taustītem.
- Lai izvēlēties atbildi, uzspiediet `Enter`.
- Ziņas par atbildes korrektumu un punktu skaita izmaiņu tiek izvādītas terminālā.

# Statistika spēles beigās

- Visa statistika paradas pēc spēles aizveršanas termināla.
- Jāievada savu nickname/vārdu.
- Labākos rezultātus var skatīties real-time [šeit](https://share.streamlit.io/fulcrum101/lapo_fire_in_the_server_room/main/main_streamlit.py). 

# Obligātu prasību izpelde

Tiek izpildītas 11/25 obligātām prasībam.

# Papildus prasību izpelde

- Katram kontrolpunktam ir sagatavoti vairāki uzdevumi,katrā izspēles reizē programma nejauši izvēlas vienu no tiem, t.i., izspēlējot spēli atkārtoti spēlētājam būs jārisina citi uzdevumi.
- Spēles noslēgumā programma izvada reālo laiku minūtēs un sekundēs, cik ilgi spēlētājs pavadījis spēlē.
- Spēles noslēgumā spēlētājam tiek pajautāts ievadīt vārdu.
- Spēlētāja vārds un spēles rezultāti (laiks, bonusa punkti u.c.) tiek saglabāti teksta failā vai datu bāzē
- Programma nodrošina lietotājam iespēju apskatīties 10 labākos spēles rezultātus –spēlētāja vārds, spēles laiks (minūtēs un sekundes)un bonusa punkti–sakārtotus pēc spēles laika augošā secībā
- Spēlētājam tiek nodrošināta iespēja jebkurā spēles brīdī lasīt spēles noteikumus.

---
**Kommentāri no autoriem:**


- Īpaši smuka sanāca online-leaderboard lapa.
- Leaderboard'am izmantota datu bāze tiks deaktivitēta pec mēnēša.
- No sākuma bija doma uzrakstīt programmu, kas ģenerētu jauno audio pa daļiņam, tomēr, kad tas tika uzrakstīta, mēs sapratam, ka to nevar normāli klausīties, lai ausis nesapētu.
