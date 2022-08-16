import random
kelimeler = ["güzel ","bilgi ","sorun","sağlamak ","bırakmak","zaman","su","yapmak","kullanılmak","değil","görmek",
             "teniden", "çoğu", "fakat", "lira", "oynamak", "çiçek", "şehir", "yükselmek", "mücadele", "varlık", "yapmak",
             "güven", "gerek", "tedavi", "birim", "rahat", "soğuk", "orası", "kitap", "paylaşmak", "hesap", "vücut",
             "toprak", "üzeri", "sistem", "hoş", "çekilmek", "teknik", "yaklaşmak", "yıl", "tarih", "kesin", "abla",
             "ince", "eğer", "oysa", "karşılık","vermek", "sahip", "artık", "kişi", "diğer", "dönem", "yine", "bunlar",
             "kitap", "olay", "bulunmak", "siz", "devlet", "ön", "en", "bakmak", "üzerine", "böyle", "bazı", "başlamak",
             "tutmak", "birbiri", "hiçbir", "yapmak", "su", "gibi", "hal", "doğru", "orta", "başka", "büyük", "etmek",
             "yeni", "fazla", "sormak", "onlar", "açmak", "hem", "hep", "ses", "anlamak", "değil", "saat", "nasıl",
             'bir', 've', 'olmak', 'bu', 'için', 'o', 'ben', 'demek', 'çok', 'yapmak', 'ne', 'gibi', 'daha', 'almak',
             'var', 'kendi', 'gelmek', 'ile', 'vermek', 'ama', 'sonra', 'kadar', 'yer', 'en', 'insan', 'değil', 'her',
             'istemek', 'yıl', 'çıkmak', 'görmek', 'gün', 'biz', 'gitmek', 'iş', 'şey', 'ara', 'ki', 'bilmek', 'el', 'zaman',
             'ya', 'çocuk', 'iki', 'bakmak', 'çalışmak', 'içinde', 'büyük', 'yok', 'başlamak', 'yol', 'kalmak', 'neden', 'siz',
             'konu', 'yapılmak', 'iyi', 'kadın', 'ev', 'diye', 'bulunmak', 'söylemek', 'göz', 'gerekmek', 'dünya',
             'baş', 'durum', 'yan', 'geçmek', 'sen', 'onlar', 'yeni', 'önce', 'başka', 'hâl', 'orta', 'su', 'girmek', 'ülke',
             'yemek', 'hiç', 'bile', 'nasıl', 'bütün', 'karşı', 'bulmak', 'böyle', 'yaşamak', 'düşünmek', 'aynı', 'iç', 'ancak',
             'kişi', 'bunlar', 'veya', 'ilk', 'göre', 'ön', 'son', 'biri', 'şekil', 'önemli', 'yüz', 'hem', 'göstermek', 'etmek',
             'alt', 'getirmek', 'kullanmak', 'çünkü', 'taraf', 'şimdi', 'adam', 'onun', 'diğer', 'artık', 'üzerinde', 'ses', 'hep',
             'doğru', 'durmak', 'kız', 'tüm', 'çekmek', 'konuşmak', 'para', 'anlamak', 'anne', 'az', 'bazı', 'baba', 'hayat',
             'sadece', 'küçük', 'fazla', 'bilgi', 'an', 'sormak', 'bunun', 'öyle', 'yine', 'sağlamak', 'sonuç', 'kullanılmak', 'dış',
             'ad', 'yani', 'süre', 'dönmek', 'açmak', 'oturmak', 'anlatmak', 'bırakmak', 'hemen', 'saat', 'yaş', 'sorun', 'devlet',
             'sahip', 'sıra', 'yazmak', 'yüzde', 'ay', 'atmak', 'tutmak', 'bunu', 'olay', 'düşmek', 'duymak', 'söz', 'güzel',
             'sevmek', 'biraz', 'zor', 'çıkarmak', 'şu', 'koymak', 'tek', 'sistem', 'birlikte', 'verilmek', 'kim', 'alınmak', 'genç',
             'kapı', 'kitap', 'üzerine', 'burada', 'gece', 'alan', 'birbiri', 'işte', 'beklemek', 'uzun', 'hiçbir', 'bugün', 'dönem',
             'arkadaş', 'ürün', 'aile', 'üç', 'okumak', 'erkek', 'herkes', 'güç', 'belki', 'gerçek', 'tam', 'ilgili', 'ilişki',
             'çevre', 'eski', 'aramak', 'yaşam', 'halk', 'yakın', 'sokak', 'bey', 'tarih', 'özellik', 'bölüm', 'özel', 'akıl',
             'kimse', 'pek', 'eğer', 'gerek', 'özellikle', 'anlam', 'yüksek', 'banka', 'kez', 'ayak', 'taşımak', 'geri', 'toplum',
             'araç', 'madde', 'tür', 'karar', 'görülmek', 'hava', 'sayı', 'farklı', 'grup', 'oda', 'biçim', 'oluşmak', 'haber',
             'allah', 'ayrıca', 'gelen', 'birkaç', 'soru', 'arka', 'kazanmak', 'yazı', 'okul', 'açık', 'öğrenmek', 'sürmek',
             'dil', 'şirket', 'kaynak', 'bitmek', 'program', 'devametmek', 'hareket', 'renk', 'açılmak', 'hak', 'inanmak',
             'çalışma', 'açı', 'parça', 'gazete', 'oluşturmak', 'tabi', 'değer', 'tanımak', 'yapı', 'doktor', 'gelir',
             'görev', 'amaç', 'bölge', 'film', 'üzere', 'müşteri', 'zaten', 'telefon', 'eğitim', 'deniz', 'ikinci',
             'kalkmak', 'hatta', 'etki', 'gelişmek', 'geçen', 'vücut', 'düşünce', 'milyon', 'oynamak', 'değişmek', 'temel',
             'yaratmak', 'ulaşmak', 'sanmak', 'geçirmek', 'kültür', 'kurmak', 'fakat', 'buna', 'resim', 'işık', 'içmek',
             'hanım', 'hizmet', 'ihtiyaç', 'nokta', 'yön', 'evet', 'oyun', 'artmak', 'yeniden', 'işlem', 'kısa', 'kolay',
             'hangi', 'oran', 'aslında', 'kabuletmek', 'orada', 'dikkat', 'uzak', 'bilgisayar', 'gelecek', 'görünmek',
             'örneğin', 'oğul', 'dinlemek', 'uygun', 'lira', 'üretim', 'dakika', 'unutmak', 'yürümek', 'böylece', 'kötü',
             'araba', 'ağız', 'duygu', 'uygulamak', 'hâlâ', 'örnek', 'birçok', 'izlemek', 'derece', 'mümkün', 'şöyle',
             'duvar', 'on', 'sanat', 'ana', 'hastalık', 'öğrenci', 'televizyon', 'yöntem', 'masa', 'ölmek', 'takım', 'üst',
             'kafa', 'müzik', 'ayrılmak', 'enerji', 'üniversite', 'spor', 'türlü', 'can', 'rağmen', 'kısım', 'ölüm',
             'sürekli', 'sağlık', 'çeşitli', 'bundan', 'hissetmek', 'oysa', 'sabah', 'internet', 'teknik', 'dışarı',
             'merkez', 'ortam', 'yerine', 'düzey', 'köy', 'yönetim', 'aşağı', 'cevap', 'yatmak', 'toprak', '', 'akşam',
             'araştırma', 'götürmek', 'katılmak', 'yoksa', 'kurulmak', 'ödemek', 'sanki', 'kan', 'hasta', 'şehir', 'inmek',
             'sunmak', 'bilinmek', 'hafta', 'trafik', 'hesap', 'otomobil', 'yabancı', 'davranış', 'mutfak', 'kent', 'bazen',
             'belli', 'ayrı', 'fiyat', 'hakkında', 'kaldırmak', 'kol', 'yalnız', 'hazırlamak', 'cam', 'sonunda', 'yavaş',
             'gerekli', 'önem', 'koca', 'yanlış', 'varlık', 'art', 'ilgi', 'sana', 'satış', 'içeri', 'doğal', 'sahipolmak',
             'ekonomik', 'acı', 'hayır', 'korumak', 'kat', 'ekonomi', 'genel', 'belirtmek', 'fotoğraf', 'hayvan', 'savaş',
             'mal', 'saç', 'kaybetmek', 'kalan', 'değiştirmek', 'dört', 'gerçekten', 'sayfa', 'teknoloji', 'kurum', 'beş',
             'sektör', 'geniş', 'kağıt', 'koku', 'sağ', 'sıcak', 'yüzyıl', 'cadde', 'pazar', 'sürdürmek', 'kullanım', 'sınıf',
             'aşk', 'doğmak', 'ağır', 'tekrar', 'güneş', 'sigara', 'ağaç', 'kelime', 'bina', 'eş', 'kaçmak', 'parti', 'yatak',
             'yazar', 'kulak', 'öğretmen', 'sebep', 'sol', 'peki', 'yağ', 'yüzden', 'anlaşılmak', 'varmak', 'gülmek', 'kural',
             'satmak', 'şiir', 'göndermek', 'başarı', 'firma', 'hükümet', 'kalp', 'kesmek', 'proje', 'şart', 'hız', 'köşe',
             'vurmak', 'model', 'balık', 'piyasa', 'görüş', 'bura', 'hazırlanmak', 'miktar', 'birinci', 'meydan', 'ölçü',
             'seçmek', 'uygulanmak', 'bahçe', 'sevgi', 'ekmek', 'boyunca', 'koşmak', 'dolu', 'kuruluş', 'saye', 'korkmak',
             'yardım', 'karşılaşmak', 'malzeme', 'hoş', 'köpek', 'ünlü', 'büyümek', 'dolaşmak', 'oldukça', 'üstelik',
             'yaşanmak', 'beyaz', 'istek', 'öte', 'denmek', 'kardeş', 'çekilmek', 'nerede', 'çalmak', 'izin', 'korku',
             'meslek', 'polis', 'yalnızca', 'açıklamak', 'fikir', 'hızlı', 'pencere', 'uğraşmak', 'taş', 'ateş', 'fark',
             'yetmek', 'çoğu', 'kimi', 'koşul', 'mahalle', 'mutlaka', 'tane', 'üretmek', 'üstüne', 'dayanmak', 'ince',
             'kaç', 'ortak', 'tip', 'görüntü', 'beri', 'ders', 'başkan', 'karşılık', 'kurtulmak', 'numara', 'defa',
             'edilmek', 'batı', 'farketmek', 'herhangibir', 'sinema', 'değişik', 'hedef', 'uyumak', 'dost', 'yanmak',
             'anlayış', 'asıl', 'basmak', 'kenar', 'kontrol', 'çevirmek', 'din', 'güçlü', 'henüz', 'plan', 'beyin',
             'elektrik', 'karı', 'üstünde', 'et', 'sağlanmak', 'söylenmek', 'çizgi', 'uç', 'üye', 'cilt', 'ruh',
             'sevgili', 'yaklaşmak', 'süreç', 'bakış', 'bilim', 'ileri', 'ifade', 'beden', 'hatırlamak', 'kaza',
             'iyice', 'dağ', 'kapatmak', 'adım', 'ciddi', 'çözüm', 'etkilemek', 'belediye', 'gelişme', 'seçim',
             'ağlamak', 'bağlı', 'kavram', 'artırmak', 'faaliyet', 'zarar', 'derin', 'salon', 'çeşit', 'kesilmek',
             'seyretmek', 'birden', 'içermek', 'sayılmak', 'toplamak', 'aşmak', 'bağırmak', 'sorumluluk', 'davranmak',
             'mektup', 'soğuk', 'canlı', 'idiekeylem', 'makine', 'yararlanmak', 'yaşlı', 'boş', 'acaba', 'maç', 'yönetici',
             'getirilmek', 'metre', 'tutulmak', 'kalite', 'bitki', 'değişiklik', 'ilaç', 'kredi', 'yasa', 'başarılı',
             'birer', 'imkan', 'ceza', 'herşey', 'incelemek', 'top', 'uzman', 'doldurmak', 'kanal', 'mekân', 'uymak',
             'yıllık', 'dolayısıyla', 'yazılmak', 'ait', 'parmak', 'saymak', 'atılmak', 'belirlemek', 'normal', 'hele',
             'ilke', 'kırmızı', 'rol', 'şarkı', 'eleman', 'hazır', 'benzemek', 'birşey', 'hoca', 'boy', 'günlük', 'politika',
             'suç', 'niye', 'sahne', 'sokmak', 'adet', 'koltuk', 'kurtarmak', 'sanatçı', 'tercihetmek', 'uzanmak', 'aşama',
             'eklemek', 'orman', 'ayırmak', 'düzen', 'faiz', 'genellikle', 'herzaman', 'hikaye', 'hücre', 'ora', 'roman',
             'vergi', 'yakmak', 'ağabey', 'basın', 'destek', 'giymek', 'hata', 'sınır', 'birlik', 'eser', 'karşılamak',
             'yarı', 'yeterli', 'birey', 'karanlık', 'otobüs', 'sanayi', 'bebek', 'vatandaş', 'bakan', 'kere', 'millet',
             'reklam', 'yükselmek', 'boyut', 'dergi', 'enflasyon', 'sosyal', 'birisi', 'geçmiş', 'hastahane', 'olma',
             'toplantı', 'gazeteci', 'içerisi', 'inanç', 'nitelik', 'üzeri', 'bitirmek', 'gerçekleşmek', 'giriş', 'rahat',
             'toplam', 'beraber', 'dükkan', 'gizli', 'benzer', 'deri', 'dönüşmek', 'mücadele', 'problem', 'servis', 'tedavi',
             'yeşil', 'bakanlık', 'baskı', 'tepki', 'cümle', 'dilemek', 'özgürlük', 'gene', 'kimlik', 'mesele', 'üçüncü',
             'belirlenmek', 'değerlendirmek', 'ilginç', 'sürücü', 'süt', 'yakalamak', 'eşya', 'uluslararası', 'aday',
             'ağırlık', 'milyar', 'sağlılklı', 'sıkıntı', 'tanrı', 'tavır', 'toplumsal', 'yayın', 'dikkatetmek', 'sonderece',
             'toplanmak', 'yatırım', 'hafif', 'karışmak', 'tehlike', 'vakit', 'daire', 'fırsat', 'işlemek', 'karıştırmak',
             'katkı', 'öykü', 'tamamen', 'uçak', 'yanıt', 'doğa', 'evlenmek', 'burun', 'çıkar', 'elbette', 'işçi', 'işletme',
             'kısaca', 'mağaza', 'medya', 'yüzünden', 'artış', 'çıkarılmak', 'kamu', 'sigorta', 'yaz', 'yürek', 'belge',
             'çaba', 'hergün', 'ifadeetmek', 'risk', 'sözetmek', 'sözcük', 'demokrasi', 'tuz', 'cami', 'çağ', 'düşük',
             'etraf', 'hızla', 'olanak', 'organ', 'öldürmek', 'öteki', 'sene', 'bozulmak', 'ilgilenmek', 'meyve', 'takılmak',
             'tatlı', 'bacak', 'değişim', 'kanun', 'rüzgar', 'cumhuriyet', 'geliştirmek', 'tarz', 'yedi', 'azalmak',
             'bağlamak', 'ceptelefonu', 'iletişim', 'müdür', 'otel', 'yayımlanmak', 'zevk', 'binmek', 'güvenlik', 'hukuk',
             'kılmak', 'modern', 'okur', 'silah', 'talep', 'yıldız', 'yoğun', 'asker', 'basit', 'denilmek', 'gaz',
             'uygulama', 'üretilmek', 'beyan', 'besin', 'dün', 'görüşmek', 'yaklaşık', 'alışveriş', 'bilinç', 'çerçeve',
             'lazım', 'mevcut', 'tüketici', 'uzatmak', 'yönelik', 'at', 'bağlanmak', 'mesela', 'neredeyse', 'site',
             'yardımcıolmak', 'abla', 'çiçek', 'hepsi', 'saygı', 'ücret', 'yetenek', 'kilo', 'paylaşmak', 'sert', 'yanısıra',
             'çay', 'gider', 'kesin', 'zengin', 'asla', 'laf', 'örgüt', 'ticaret', 'yaptırmak', 'boyun', 'cihaz',
             'denge', 'giderek', 'sırt', 'dolayı', 'kahve', 'kas', 'meclis', 'öteki', 'uğraşmak', 'adres', 'belirtilmek',
             'paşa', 'sıcaklık', 'tamam', 'güven', 'marka', 'yaprak', 'yarar', 'yayılmak', 'akmak', 'çizmek', 'düşünülmek',
             'gönül', 'hayal', 'ilerlemek', 'şarap', 'yukarıda', 'altın', 'düzenlemek', 'satınalmak', 'sunulmak', 'temiz',
             'vitamin', 'ek', 'geç', 'hareketetmek', 'yumurta', 'aşırı', 'eylem', 'istenmek', 'kesim', 'kriz', 'birim',
             'kapanmak', 'saklamak', 'saklamak', 'sehpa', 'vazo', 'vezir', 'bardak', 'içki', 'halı', 'kilim', 'koltuk', 
             'dikiş', 'dikim', 'perde', 'kişi', 'ev', 'boru', 'köpek', 'cam', 'pense', 'yatak', 'televizyon', 'sinema', 
             'işlek', 'tablo', 'fantastik', 'kadın', 'bebek', 'ezan', 'şehit', 'mikrop', 'bakteri', 'yazlık', 'isyan',
             'mezar', 'seslenmek', 'bagırmak', 'ağlamak', 'kitap', 'turuncu', 'müzik', 'yemek', 'havlu', 'bornoz', 'cam', 
             'ense', 'pense', 'sinsi', 'medusa', 'tanrı', 'yapım', 'şarap', 'yurt', 'para', 'borç', 'vergi', 'sezgi', 'sinsi',
             ,dede', 'bere', 'komedi', 'şaka', 'eski', 'türk', 'süt', 'ütü', 'baba', 'anne', 'ajan', 'oyun', 'doymak', 'dolgu',
             ]


def kelime_sec():
    return random.choice(kelimeler)
