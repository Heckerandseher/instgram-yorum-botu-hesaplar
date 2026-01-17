from instagrapi import Client
from instagrapi.exceptions import LoginRequired, ChallengeRequired
import random
import time
import os
import json
import glob


YORUM_SAYISI = 30
MEDIA_URL = "https://www.instagram.com/reels/DTfurNrjAzx/"
y = "@toskaorj"
YORUMLAR_DOSYA = "yorumlar.json"
PROXY_DOSYA = "proxy.txt"
IPHONE_17_PRO_MAX_SETTINGS = {
    "app_version": "361.0.0.0.0",
    "phone_manufacturer": "Apple",
    "phone_model": "iPhone17,2",
    "android_version": 0,
    "os_version": "19.2",
    "dpi": "460",
    "resolution": "1290x2796",
    "language": "tr_TR",
    "timezone_offset": "10800",
    "build": "23C71",
}

proxies = []

def proxyleri_yukle():
    global proxies
    if not os.path.exists(PROXY_DOSYA):
        with open(PROXY_DOSYA, "w", encoding="utf-8") as f:
            f.write(f"# {y} Proxy listesi (her satıra bir tane)\n")
            f.write(f"# Örnek: 45.67.89.123:8080\n")
        proxies = []
        return
    
    with open(PROXY_DOSYA, "r", encoding="utf-8") as f:
        proxy_list = [
            line.strip() 
            for line in f 
            if line.strip() and not line.strip().startswith('#')
        ]
    
    proxies = proxy_list
    print(f"{len(proxies)} adet proxy yüklendi {y}")

def yorumlari_yukle():
    if os.path.exists(YORUMLAR_DOSYA):
        with open(YORUMLAR_DOSYA, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    return data
            except:
                pass
    
    return [
        f"{y} yapımcı.",
        f"{y} selamı var.",
        f"{y} abimdir.",
        f"destek {y}",
        f"{y} selamın aleyküm"
    ]

def yorumlari_kaydet(yorum_listesi):
    with open(YORUMLAR_DOSYA, "w", encoding="utf-8") as f:
        json.dump(yorum_listesi, f, ensure_ascii=False, indent=4)

yorumlar = yorumlari_yukle()

def yeni_yorum_ekle():
    print(f"\n--- Yeni Yorum Ekle --- {y}")
    print(f"{y} Mevcut yorum sayısı: {len(yorumlar)}")
    yeni = input(f"{y} Yeni yorum (iptal için boş): ").strip()
    if not yeni:
        print(f"{y} İşlem iptal edildi.")
        return
    yorumlar.append(yeni)
    yorumlari_kaydet(yorumlar)
    print(f"{y} ✅ Yorum eklendi: {yeni}")

def degistir_url():
    global MEDIA_URL
    print(f"\n{y} Mevcut URL: {MEDIA_URL}")
    yeni_url = input(f"{y} Yeni Reels/Post URL'si gir (değiştirmek istemiyorsan boş bırak): ").strip()
    if yeni_url:
        if "instagram.com" in yeni_url:
            MEDIA_URL = yeni_url
            print(f"{y} URL güncellendi: {MEDIA_URL}")
        else:
            print(f"{y} Geçersiz URL! instagram.com içermeli.")
    else:
        print(f"{y} URL değiştirilmedi.")

def degistir_yorum_sayisi():
    global YORUM_SAYISI
    print(f"\n{y} Mevcut yorum sayısı: {YORUM_SAYISI}")
    try:
        yeni_sayi = input(f"{y} Yeni yorum sayısı gir (1-100 arası önerilir): ").strip()
        if yeni_sayi:
            sayi = int(yeni_sayi)
            if 1 <= sayi <= 200:
                YORUM_SAYISI = sayi
                print(f"{y} Yorum sayısı güncellendi: {YORUM_SAYISI}")
            else:
                print(f"{y} Çok yüksek veya düşük! 1-200 arası olmalı.")
    except:
        print(f"{y} Geçersiz sayı girdin.")

def menu_goster():
    print("\n" + "="*70)
    print(f"{y} INSTAGRAM YORUM BOTU iOS 17 PRO MAX {y}")
    print("="*70)
    print(f"  1 → Mevcut session'dan devam et")
    print(f"  2 → Yeni giriş yap (şifre ile)")
    print(f"  3 → Yeni yorum ekle")
    print(f"  4 → Session dosyası sil")
    print(f"  5 → Proxy listesini yönet")
    print(f"  6 → Çıkış")
    print(f"  7 → Hedef URL değiştir ({MEDIA_URL[:40]}...)")
    print(f"  8 → Yorum sayısını değiştir ({YORUM_SAYISI} adet)")
    print("-"*70)
    print(f"Proxy sayısı {y} : {len(proxies)} adet")
    print(f"Yorum sayısı {y} : {YORUM_SAYISI} adet")
    print(f"Hedef URL {y} : {MEDIA_URL}")
    print(f"Cihaz: iPhone 17 Pro Max (iOS 19.2) {y}")
    print("="*70)
    return input(f"{y} Seçiminiz (1-8): ").strip()

def proxy_yonet():
    global proxies
    print(f"\n--- Proxy Yönetimi --- {y}")
    print(f"{y} Mevcut proxy sayısı: {len(proxies)}")
    print(f"1 → Yeni proxy ekle {y}")
    print(f"2 → Tüm proxy'leri göster {y}")
    print(f"3 → Proxy dosyasını sıfırla {y}")
    print(f"0 → Geri dön {y}")
    sec = input(f"{y} Seçiminiz: ").strip()
    
    if sec == "1":
        yeni = input(f"{y} Yeni proxy (ör: 45.67.89.123:8080): ").strip()
        if yeni:
            with open(PROXY_DOSYA, "a", encoding="utf-8") as f:
                f.write(yeni + "\n")
            proxyleri_yukle()
            print(f"{y} Proxy eklendi: {yeni}")
    
    elif sec == "2":
        if proxies:
            for i, p in enumerate(proxies, 1):
                print(f"{i}. {p} {y}")
        else:
            print(f"{y} Henüz proxy yok.")
    
    elif sec == "3":
        if input(f"{y} Dosyayı boşalt? (e/h): ").lower() == 'e':
            with open(PROXY_DOSYA, "w", encoding="utf-8") as f:
                f.write("")
            proxyleri_yukle()
            print(f"{y} Proxy listesi sıfırlandı.")
    
    input(f"\nEnter'a basın {y}...")

def mevcut_sessionlari_listele():
    return [
        {"username": f.replace("session_", "").replace(".json", ""), "dosya": f}
        for f in glob.glob("session_*.json")
    ]

def session_sec():
    sessionlar = mevcut_sessionlari_listele()
    if not sessionlar:
        print(f"\nSession dosyası yok. {y}")
        return None
    print(f"\nMevcut session'lar {y}:")
    for i, s in enumerate(sessionlar, 1):
        print(f"{i}) {s['username']} {y}")
    try:
        sec = int(input(f"{y} Numara: "))
        if 1 <= sec <= len(sessionlar):
            return sessionlar[sec-1]
    except:
        pass
    return None

def session_sil():
    sessionlar = mevcut_sessionlari_listele()
    if not sessionlar:
        return
    print("\nSession'lar:")
    for i, s in enumerate(sessionlar, 1):
        print(f"{i}) {s['username']}")
    try:
        sec = int(input(f"{y} Silmek istediğiniz numara (0=iptal): "))
        if sec == 0:
            return
        if 1 <= sec <= len(sessionlar):
            os.remove(sessionlar[sec-1]["dosya"])
            print(f"{y} Session silindi.")
    except:
        pass

def giris_yap(session_info=None, yeni_giris=False):
    kullan_proxy = False
    proxy = None
    
    if proxies and input(f"\n{y} Proxy kullan? (e/h): ").lower() == 'e':
        kullan_proxy = True
        proxy = random.choice(proxies)
        print(f"{y} → Proxy: {proxy}")
    else:
        print(f"{y} → Kendi IP (proxysiz)")

    cl = Client()
    cl.set_device(IPHONE_17_PRO_MAX_SETTINGS)
    
    cl.set_user_agent(
        "Instagram 361.0.0.0.0 (iPhone17,2; iPhone OS 19_2; tr_TR; scale=3.00; 1290x2796) "
        "AppleWebKit/605.1.15"
    )
    
    cl.delay_range = [10, 20]

    if kullan_proxy:
        try:
            cl.set_proxy(f"http://{proxy}")
        except Exception as e:
            print(f"{y} Proxy hatası: {e}")
            return None, None

    if session_info and not yeni_giris:
        print(f"\n{y} Session yükleniyor → {session_info['username']}")
        try:
            cl.load_settings(session_info["dosya"])
            cl.get_timeline_feed()
            print(f"{y} Session yüklendi ✓")
            return cl, session_info["username"]
        except Exception as e:
            print(f"{y} Session geçersiz: {e}")
            return giris_yap(session_info, True)
    
    else:
        username = input(f"\n{y} Kullanıcı adı: ").strip()
        password = input(f"{y} Şifre: ").strip()
        if not username or not password:
            return None, None
        
        print(f"\n{y} Giriş deneniyor → {username} (iPhone 17 Pro Max)")
        try:
            cl.login(username, password)
            session_file = f"session_{username}.json"
            cl.dump_settings(session_file)
            print(f"{y} Giriş başarılı! Session kaydedildi.")
            return cl, username
        except ChallengeRequired:
            print(f"{y} CHALLENGE gerekiyor! Tarayıcıdan doğrulayın.")
        except Exception as e:
            print(f"{y} Giriş hatası: {str(e)}")
        return None, None

def yorum_at(cl, username):
    if not cl:
        return
    
    try:
        media_pk = cl.media_pk_from_url(MEDIA_URL)
        print(f"\n{y} Hedef: {MEDIA_URL}")
        print(f"{y} {YORUM_SAYISI} yorum atılacak...\n")

        for i in range(YORUM_SAYISI):
            yorum = random.choice(yorumlar)
            cl.media_comment(media_pk, yorum)
            print(f"({i+1}/{YORUM_SAYISI}) → {yorum} {y}")
            
            sleep_min, sleep_max = (10, 20) if cl.proxy else (15, 40)
            sleep = random.uniform(sleep_min, sleep_max)
            print(f"   {y} Bekleniyor: {sleep:.0f} sn")
            time.sleep(sleep)
            
    except Exception as e:
        print(f"{y} Yorum hatası: {str(e)}")

# ================== BAŞLANGIÇ ==================
proxyleri_yukle()

while True:
    secim = menu_goster()

    if secim == "8":
        degistir_yorum_sayisi()
        continue

    elif secim == "7":
        degistir_url()
        continue

    elif secim == "6":
        print(f"{y} Bot kapatılıyor...")
        break

    elif secim == "5":
        proxy_yonet()
        continue

    elif secim == "4":
        session_sil()
        continue

    elif secim == "3":
        yeni_yorum_ekle()
        continue

    elif secim in ["1", "2"]:
        cl = None
        kullanici_adi = None
        
        if secim == "1":
            session_secimi = session_sec()
            if session_secimi:
                cl, kullanici_adi = giris_yap(session_secimi)
        else:
            cl, kullanici_adi = giris_yap(yeni_giris=True)
        
        if cl and kullanici_adi:
            yorum_at(cl, kullanici_adi)
            print(f"\n{y} [{kullanici_adi}] İşlem tamamlandı.")
        else:
            print(f"{y} Giriş yapılamadı.")
            
    else:
        print(f"{y} Geçersiz seçim.")