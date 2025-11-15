# Yılan Oyunu (Snake Game)

Klasik yılan oyununun Python ve Pygame kullanılarak yapılmış implementasyonu.

## Özellikler

- 🐍 Klasik yılan oyunu mekaniği
- 🎮 Ok tuşları ile kontrol
- 🍎 Rastgele yiyecek oluşturma
- 📊 Skor sistemi
- 🎨 Renkli ve temiz arayüz
- 🔄 Yeniden oynanabilirlik

## Kurulum

### Gereksinimler

- Python 3.6 veya üzeri
- Pygame kütüphanesi

### Bağımlılıkları Yükleme

```bash
pip install -r requirements.txt
```

veya doğrudan:

```bash
pip install pygame
```

## Oyunu Çalıştırma

```bash
python snake_game.py
```

veya:

```bash
python3 snake_game.py
```

## Nasıl Oynanır

### Kontroller

- **↑ (Yukarı Ok)**: Yılanı yukarı hareket ettir
- **↓ (Aşağı Ok)**: Yılanı aşağı hareket ettir
- **← (Sol Ok)**: Yılanı sola hareket ettir
- **→ (Sağ Ok)**: Yılanı sağa hareket ettir
- **SPACE**: Oyun bittikten sonra yeniden başlat
- **ESC**: Oyundan çık

### Kurallar

1. Yılanı yönlendirerek kırmızı yiyecekleri toplayın
2. Her yiyecek topladığınızda yılan uzar ve 10 puan kazanırsınız
3. Duvarlara veya kendi gövdenize çarpmayın
4. Yılan kendi tersine dönemez (örneğin sağa giderken sola dönemez)

### Amaç

Mümkün olduğunca çok yiyecek toplayarak yüksek skor elde edin!

## Oyun Özellikleri

- **Ekran Boyutu**: 800x600 piksel
- **Blok Boyutu**: 20x20 piksel
- **Oyun Hızı**: 10 FPS
- **Başlangıç Uzunluğu**: 3 segment
- **Puan**: Her yiyecek için 10 puan

## Geliştirme

Oyunu özelleştirmek isterseniz, `YilanOyunu` sınıfını başlatırken parametreleri değiştirebilirsiniz:

```python
oyun = YilanOyunu(
    genislik=800,      # Ekran genişliği
    yukseklik=600,     # Ekran yüksekliği
    blok_boyutu=20     # Her bloğun boyutu
)
```

Oyun hızını değiştirmek için `calistir()` metodundaki `self.saat.tick(10)` satırındaki değeri artırın veya azaltın.

## Lisans

Bu proje eğitim amaçlı hazırlanmıştır.

## İyi Oyunlar! 🎮🐍
