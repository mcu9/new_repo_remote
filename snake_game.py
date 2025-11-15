#!/usr/bin/env python3
"""
Yılan Oyunu (Snake Game)
Klavye ile yönlendirme yaparak yılanı kontrol edin ve yiyecekleri toplayın!
"""

import pygame
import random
import sys
from enum import Enum

# Renkler
SIYAH = (0, 0, 0)
BEYAZ = (255, 255, 255)
KIRMIZI = (255, 0, 0)
YESIL = (0, 255, 0)
MAVI = (0, 0, 255)
YILAN_RENK = (0, 200, 0)
YIYECEK_RENK = (255, 50, 50)
IZGARA_RENK = (40, 40, 40)

class Yon(Enum):
    """Yılanın hareket yönleri"""
    YUKARI = 1
    ASAGI = 2
    SOL = 3
    SAG = 4

class YilanOyunu:
    def __init__(self, genislik=800, yukseklik=600, blok_boyutu=20):
        """Oyun başlatıcı"""
        pygame.init()

        self.genislik = genislik
        self.yukseklik = yukseklik
        self.blok_boyutu = blok_boyutu

        # Ekran ayarları
        self.ekran = pygame.display.set_mode((genislik, yukseklik))
        pygame.display.set_caption('Yılan Oyunu')
        self.saat = pygame.time.Clock()

        # Font ayarları
        self.font = pygame.font.Font(None, 36)
        self.kucuk_font = pygame.font.Font(None, 24)

        # Oyun durumu
        self.yilan = []
        self.yon = Yon.SAG
        self.yiyecek_pozisyon = None
        self.skor = 0
        self.oyun_bitti = False

        # Oyunu başlat
        self.yeni_oyun()

    def yeni_oyun(self):
        """Yeni oyun başlat"""
        # Yılanın başlangıç pozisyonu (ekranın ortası)
        baslangic_x = self.genislik // 2
        baslangic_y = self.yukseklik // 2

        # Yılanı 3 parçalı olarak başlat
        self.yilan = [
            [baslangic_x, baslangic_y],
            [baslangic_x - self.blok_boyutu, baslangic_y],
            [baslangic_x - 2 * self.blok_boyutu, baslangic_y]
        ]

        self.yon = Yon.SAG
        self.skor = 0
        self.oyun_bitti = False
        self.yiyecek_olustur()

    def yiyecek_olustur(self):
        """Rastgele bir yerde yiyecek oluştur"""
        while True:
            x = random.randint(0, (self.genislik - self.blok_boyutu) // self.blok_boyutu) * self.blok_boyutu
            y = random.randint(0, (self.yukseklik - self.blok_boyutu) // self.blok_boyutu) * self.blok_boyutu

            # Yiyeceğin yılanın üzerinde olmamasını kontrol et
            if [x, y] not in self.yilan:
                self.yiyecek_pozisyon = [x, y]
                break

    def yon_degistir(self, yeni_yon):
        """Yılanın yönünü değiştir (ters yöne gidememeli)"""
        ters_yonler = {
            Yon.YUKARI: Yon.ASAGI,
            Yon.ASAGI: Yon.YUKARI,
            Yon.SOL: Yon.SAG,
            Yon.SAG: Yon.SOL
        }

        # Ters yöne gidemesin
        if yeni_yon != ters_yonler.get(self.yon):
            self.yon = yeni_yon

    def hareket_et(self):
        """Yılanı hareket ettir"""
        if self.oyun_bitti:
            return

        # Yılanın başını al
        bas = self.yilan[0].copy()

        # Yöne göre yeni baş pozisyonu
        if self.yon == Yon.YUKARI:
            bas[1] -= self.blok_boyutu
        elif self.yon == Yon.ASAGI:
            bas[1] += self.blok_boyutu
        elif self.yon == Yon.SOL:
            bas[0] -= self.blok_boyutu
        elif self.yon == Yon.SAG:
            bas[0] += self.blok_boyutu

        # Duvara çarpma kontrolü
        if (bas[0] < 0 or bas[0] >= self.genislik or
            bas[1] < 0 or bas[1] >= self.yukseklik):
            self.oyun_bitti = True
            return

        # Kendine çarpma kontrolü
        if bas in self.yilan:
            self.oyun_bitti = True
            return

        # Yeni başı ekle
        self.yilan.insert(0, bas)

        # Yiyecek yeme kontrolü
        if bas == self.yiyecek_pozisyon:
            self.skor += 10
            self.yiyecek_olustur()
        else:
            # Yiyecek yemediyse kuyruğu sil
            self.yilan.pop()

    def ciz(self):
        """Oyunu çiz"""
        # Arka plan
        self.ekran.fill(SIYAH)

        # Izgara çiz
        for x in range(0, self.genislik, self.blok_boyutu):
            pygame.draw.line(self.ekran, IZGARA_RENK, (x, 0), (x, self.yukseklik))
        for y in range(0, self.yukseklik, self.blok_boyutu):
            pygame.draw.line(self.ekran, IZGARA_RENK, (0, y), (self.genislik, y))

        # Yiyecek çiz
        if self.yiyecek_pozisyon:
            pygame.draw.rect(
                self.ekran,
                YIYECEK_RENK,
                (self.yiyecek_pozisyon[0], self.yiyecek_pozisyon[1],
                 self.blok_boyutu, self.blok_boyutu)
            )
            # Yiyeceğin ortasına küçük bir daire
            pygame.draw.circle(
                self.ekran,
                BEYAZ,
                (self.yiyecek_pozisyon[0] + self.blok_boyutu // 2,
                 self.yiyecek_pozisyon[1] + self.blok_boyutu // 2),
                self.blok_boyutu // 4
            )

        # Yılan çiz
        for i, segment in enumerate(self.yilan):
            # Baş biraz daha parlak
            renk = YESIL if i == 0 else YILAN_RENK
            pygame.draw.rect(
                self.ekran,
                renk,
                (segment[0], segment[1], self.blok_boyutu, self.blok_boyutu)
            )
            # Segment kenarları
            pygame.draw.rect(
                self.ekran,
                SIYAH,
                (segment[0], segment[1], self.blok_boyutu, self.blok_boyutu),
                1
            )

        # Skor göster
        skor_text = self.kucuk_font.render(f'Skor: {self.skor}', True, BEYAZ)
        self.ekran.blit(skor_text, (10, 10))

        # Oyun bittiyse
        if self.oyun_bitti:
            # Yarı saydam arka plan
            overlay = pygame.Surface((self.genislik, self.yukseklik))
            overlay.set_alpha(200)
            overlay.fill(SIYAH)
            self.ekran.blit(overlay, (0, 0))

            # Oyun bitti mesajı
            oyun_bitti_text = self.font.render('OYUN BİTTİ!', True, KIRMIZI)
            skor_text = self.font.render(f'Skorunuz: {self.skor}', True, BEYAZ)
            yeniden_text = self.kucuk_font.render('Yeniden başlamak için SPACE tuşuna basın', True, BEYAZ)
            cikis_text = self.kucuk_font.render('Çıkmak için ESC tuşuna basın', True, BEYAZ)

            # Metinleri merkeze yerleştir
            self.ekran.blit(oyun_bitti_text,
                          (self.genislik // 2 - oyun_bitti_text.get_width() // 2,
                           self.yukseklik // 2 - 80))
            self.ekran.blit(skor_text,
                          (self.genislik // 2 - skor_text.get_width() // 2,
                           self.yukseklik // 2 - 20))
            self.ekran.blit(yeniden_text,
                          (self.genislik // 2 - yeniden_text.get_width() // 2,
                           self.yukseklik // 2 + 40))
            self.ekran.blit(cikis_text,
                          (self.genislik // 2 - cikis_text.get_width() // 2,
                           self.yukseklik // 2 + 70))

        pygame.display.flip()

    def calistir(self):
        """Ana oyun döngüsü"""
        # Başlangıç ekranı
        baslangic = True

        while True:
            # Başlangıç ekranı
            if baslangic:
                self.ekran.fill(SIYAH)
                baslik = self.font.render('YILAN OYUNU', True, YESIL)
                alt_baslik = self.kucuk_font.render('Başlamak için SPACE tuşuna basın', True, BEYAZ)
                kontroller1 = self.kucuk_font.render('Ok tuşları ile yön verin', True, BEYAZ)
                kontroller2 = self.kucuk_font.render('ESC ile çıkış yapın', True, BEYAZ)

                self.ekran.blit(baslik,
                              (self.genislik // 2 - baslik.get_width() // 2,
                               self.yukseklik // 2 - 100))
                self.ekran.blit(alt_baslik,
                              (self.genislik // 2 - alt_baslik.get_width() // 2,
                               self.yukseklik // 2 - 20))
                self.ekran.blit(kontroller1,
                              (self.genislik // 2 - kontroller1.get_width() // 2,
                               self.yukseklik // 2 + 40))
                self.ekran.blit(kontroller2,
                              (self.genislik // 2 - kontroller2.get_width() // 2,
                               self.yukseklik // 2 + 70))

                pygame.display.flip()

                # Başlangıç için bekleme
                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                baslangic = False
                                waiting = False
                            elif event.key == pygame.K_ESCAPE:
                                pygame.quit()
                                sys.exit()

            # Olayları işle
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.yon_degistir(Yon.YUKARI)
                    elif event.key == pygame.K_DOWN:
                        self.yon_degistir(Yon.ASAGI)
                    elif event.key == pygame.K_LEFT:
                        self.yon_degistir(Yon.SOL)
                    elif event.key == pygame.K_RIGHT:
                        self.yon_degistir(Yon.SAG)
                    elif event.key == pygame.K_SPACE and self.oyun_bitti:
                        self.yeni_oyun()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            # Oyun devam ediyorsa hareket et
            if not self.oyun_bitti:
                self.hareket_et()

            # Ekranı çiz
            self.ciz()

            # FPS ayarla (oyun hızı)
            self.saat.tick(10)

def main():
    """Ana fonksiyon"""
    oyun = YilanOyunu(genislik=800, yukseklik=600, blok_boyutu=20)
    oyun.calistir()

if __name__ == '__main__':
    main()
