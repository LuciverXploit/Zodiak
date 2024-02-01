#LuciverXploit Code
#@arimarshello_reall
#ZODIAK
def zodiak(tanggal, bulan):
    if (bulan == 3 and tanggal >= 21) or (bulan == 4 and tanggal <= 19):
        sign = "Aries"
    elif (bulan == 4 and tanggal >= 20) or (bulan == 5 and tanggal <= 20):
        sign = "Taurus"
    elif (bulan == 5 and tanggal >= 21) or (bulan == 6 and tanggal <= 20):
        sign = "Gemini"
    elif (bulan == 6 and tanggal >= 21) or (bulan == 7 and tanggal <= 22):
        sign = "Cancer"
    elif (bulan == 7 and tanggal >= 23) or (bulan == 8 and tanggal <= 22):
        sign = "Leo"
    elif (bulan == 8 and tanggal >= 23) or (bulan == 9 and tanggal <= 22):
        sign = "Virgo"
    elif (bulan == 9 and tanggal >= 23) or (bulan == 10 and tanggal <= 22):
        sign = "Libra"
    elif (bulan == 10 and tanggal >= 23) or (bulan == 11 and tanggal <= 21):
        sign = "Scorpio"
    elif (bulan == 11 and tanggal >= 22) or (bulan == 12 and tanggal <= 21):
        sign = "Sagittarius"
    elif (bulan == 12 and tanggal >= 22) or (bulan == 1 and tanggal <= 19):
        sign = "Capricorn"
    elif (bulan == 1 and tanggal >= 20) or (bulan == 2 and tanggal <= 18):
        sign = "Aquarius"
    elif (bulan == 2 and tanggal >= 19) or (bulan == 3 and tanggal <= 20):
        sign = "Pisces"
    else:
        return "Tanggal atau bulan tidak valid"

    # Informasi tambahan berdasarkan zodiak
    zodiak_info = {
        "Aries": {
            "jodoh": "Leo dan Sagitarius",
            "nasib": "Keberuntungan akan menyertai Anda.",
            "arti": "Penuh semangat, berani, dan petualang."
        },
        "Taurus": {
            "jodoh": "Virgo dan Capricorn",
            "nasib": "Waktu yang baik untuk kesuksesan finansial.",
            "arti": "Stabil, praktis, dan berkemauan keras."
        },
        "Gemini": {
            "jodoh": "Libra dan Aquarius",
            "nasib": "Jangan ragu untuk mengejar impian Anda.",
            "arti": "Cerdas, komunikatif, dan fleksibel."
        },
        "Cancer": {
            "jodoh": "Scorpio dan Pisces",
            "nasib": "Waktu yang baik untuk mendekatkan hubungan dengan keluarga.",
            "arti": "Penuh perhatian, emosional, dan pelindung."
        },
        "Leo": {
            "jodoh": "Aries dan Sagitarius",
            "nasib": "Waktu yang baik untuk prestasi dan pengakuan.",
            "arti": "Berani, suka menjadi pusat perhatian, dan kreatif."
        },
        "Virgo": {
            "jodoh": "Taurus dan Capricorn",
            "nasib": "Fokus pada pekerjaan akan membawa kesuksesan.",
            "arti": "Detail-oriented, praktis, dan analitis."
        },
        "Libra": {
            "jodoh": "Gemini dan Aquarius",
            "nasib": "Hubungan sosial akan berkembang dengan baik.",
            "arti": "Harmonis, adil, dan senang berkomunikasi."
        },
        "Scorpio": {
            "jodoh": "Cancer dan Pisces",
            "nasib": "Waktu yang baik untuk mengatasi rintangan.",
            "arti": "Intens, penuh gairah, dan misterius."
        },
        "Sagittarius": {
            "jodoh": "Aries dan Leo",
            "nasib": "Waktu yang baik untuk perjalanan dan pengetahuan baru.",
            "arti": "Optimis, petualang, dan suka kebebasan."
        },
        "Capricorn": {
            "jodoh": "Taurus dan Virgo",
            "nasib": "Ketekunan akan membawa kesuksesan jangka panjang.",
            "arti": "Bertanggung jawab, ambisius, dan tahan uji."
        },
        "Aquarius": {
            "jodoh": "Gemini dan Libra",
            "nasib": "Waktu yang baik untuk menciptakan perubahan positif.",
            "arti": "Inovatif, humanis, dan suka berkolaborasi."
        },
        "Pisces": {
            "jodoh": "Cancer dan Scorpio",
            "nasib": "Waktu yang baik untuk pengembangan pribadi.",
            "arti": "Sensitif, imajinatif, dan penuh empati."
        }
    }

    return sign, zodiak_info[sign]

# Input tanggal lahir
tanggal_lahir = int(input("Masukkan tanggal lahir (1-31): "))
bulan_lahir = int(input("Masukkan bulan lahir (1-12): "))

# Memanggil fungsi zodiak
sign, info = zodiak(tanggal_lahir, bulan_lahir)

# Menampilkan hasil
print(f"Zodiak Anda adalah: {sign}")
print(f"Jodoh yang cocok: {info['jodoh']}")
print(f"Nasib Anda: {info['nasib']}")
print(f"Arti zodiak Anda: {info['arti']}")

