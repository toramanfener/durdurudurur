import random
kelimeler = ['yazılmak', 'yatmak', 'uyumak', 'borsa', 'ülke', 'dolap', 'ünlü', 'dolaşmak', 'içmek', 'içki',
             'susmam', 'giymek', 'gitmek', 'porselen', 'ayakkabı', 'bilgisayar', 'pencere', 'düzenbaz', 'yalancı', 
             'peçete', 'selpak', 'salıncak', 'baba', 'vurgun', 'durgun', 'sinek', 'yaz', 'kış', 'cumhuriyet', 'atatürk',
             'oyuncak', 'salıncak', 'çocuk', 'naz', 'kur', 'sinek', 'böcek', 'kapı', 'şarj', 'kulaklık', 'oyun',
             'ressam', 'film', 'dizi', 'müzik', 'ayna', 'firma', 'sevgi', 'ask', 'duygusal', 'feminist', 'aldatmak', 
             'kelime', 'süzmek', 'sürgün', 'kitap', 'öğretmen', 'polis', 'öğrenmek', 'savcı', 'hakim', 'tepki', 
             'asker', 'baba', 'din', 'anne', 'ruh', 'bal', 'arı', 'güzel', 'çirkin', 'define', 'hazine', 'suçlu', 'mahkeme',
             'sanık', 'yazılım', 'korumak', 'dümen', 'gülmek', 'at', 'spor', 'dil', 'müşteki', 'müşteri', 'hak', 'hukuk',
             'mahkeme', 'yasal', 'yol', 'ölüm', 'yalan', 'gezegen', 'rütbe', 'evren', 'mars', 'dünya', 'insan', 'evlat',
             'karakter', 'kötu', 'birlik', 'birim', 'sevgi', 'etki', 'tepki', 'coşmak', 'satmak', 'bahçe', 'vergi', 'zam',
             'dar', 'geniş', 'bolluk', 'sol', 'sağ', 'müzisyen', 'sanatçı', 'karınca', 'hayvan', 'korumak', 'yük', 'yükümlülük',
             'sülük', 'makyaj', 'taraf', 'futbol', 'petek', 'doğal', 'gaz', 'elektrik', 'fatura', 'kod', 'oyun', 'telegram', 
             'yastık', 'baza', 'taraf', 'taraftar', 'dolar', 'vadi', 'havlu', 'motivasyon', 'aksiyon', 'şirket', 'sahip', 
             'tarih', 'bozgun', 'tok', 'aç', 'kahvaktı', 'lamba', 'irdelemek', 'almak', 'satmak', 'çiftçi', 'horlamak', 
             'kulaklık', 'ses', 'göz', 'kulak', 'ayak', 'bacak', 'hayat', 'doğal', 'doğa', 'hava', 'oksijen', 'temiz', 
             'pis', 'ter', 'koku', 'terlik', 'yorgan', 'kılıf', 'tabanca', 'kın', 'kılıç', 'özgüven', 'tavan', 'taban', 
             'avukat', 'avutmak', 'hakime', 'radyo', 'popüler', 'resmi', 'dilekçe', 'şikayet', 'vilayet', 'tohum', 'torun',
             'osmanlı', 'boğulmak', 'soyulmak', 'devir', 'teslim', 'kesin', 'villa', 'konut', 'proje', 'onay', 'tümen', 'tüzük',
             'üniversite', 'soba', 'boru', 'kullanmak', 'araba', 'marka', 'makyaj', 'trip', 'sirk', 'red', 'kalıp', 'kalp', 
             'cerrah', 'selamet', 'hoşlanmak', 'küsmek', 'gece', 'gündüz', 'düz', 'yokuş', 'tırmanmak', 'alınmak', 'kurulmak', 
             'sevilmek', 'pantalon', 'elbise', 'polar', 'sofra', 'aile', 'keyif', 'komutan', 'kumandan', 'burjuva', 'balıklama', 
             'sayıklamak', 'hayıflanmak', 'telefon', 'zayıflamak'
             ]


def kelime_sec():
    return random.choice(kelimeler)
