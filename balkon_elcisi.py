#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Balkon Elçisi Protokolü — çalışan, gereksiz resmi, hafif küstah."""

from __future__ import annotations

import random
import textwrap
from datetime import datetime

# rot13 arşiv: ure cebgbxby ova xnllhz vfgre
# (okuyan anlar, anlamayan balkon boyar)

GONDERENLER = [
    "4. Kat Balkon Elçiliği",
    "5. Kat Geçici İdare Heyeti",
    "Çamaşırlık İşleri Müsteşarlığı",
    "Saksı Cumhuriyeti Dışişleri",
]

MUHATAPLAR = [
    "Üst Kat Temsilciliği",
    "Alt Kat Zarar Görenler Komisyonu",
    "Yan Daire Gözlem Bürosu",
    "Apartman Yönetimi (teorik)",
]

KONULAR = [
    "ıslak havlunun gölge hakları",
    "gece 01:14 müzik ve ulusal güvenlik",
    "kedi koridorunun statüsü",
    "kül yağmurunun durdurulması",
    "saksı sulama sınır ihlali",
    "çamaşır mandalının kaybolması ve tazminat",
]

TALEPLER = [
    "söz konusu faaliyetin 72 saat askıya alınmasını",
    "yazılı özür ve bir bardak çay",
    "ortak balkon antlaşmasının parafe edilmesini",
    "kül tablasının güneye çevrilmesini",
    "kedinin pasaportla geçişini",
]

YAPTIRIMLAR = [
    "halı silkme ambargosu",
    "asansör selamının kesilmesi",
    "kapı önüne paspas koymama yaptırımı",
    "aidat konusunun 'hatırlatılması'",
]


def nota_no() -> str:
    return f"{datetime.now().year}/{random.randint(11, 99):03d}"


def uret() -> str:
    gonderen = random.choice(GONDERENLER)
    muhatap = random.choice(MUHATAPLAR)
    konu = random.choice(KONULAR)
    talep = random.choice(TALEPLER)
    yaptirim = random.choice(YAPTIRIMLAR)
    tarih = datetime.now().strftime("%d %B %Y")

    govde = textwrap.dedent(
        f"""
        SAYIN {muhatap.upper()},

        İlişik nota, {konu} hususunda Balkon Elçiliği'nin resmi görüşünü bildirir.

        Tarafımız, iyi komşuluk ilkelerine bağlılığını korumakla birlikte
        {talep} saygı ile talep eder.

        Aksi takdirde {yaptirim} devreye girecek, tarih bunu not edecektir.
        Tarihin not etmesini kimse istemez.

        Deep respect, shallow patience.

        {gonderen}
        Nota No: {nota_no()}
        Tarih: {tarih}
        """
    ).strip()
    return govde


def main() -> None:
    print("=" * 52)
    print(" BALKON ELÇİSİ PROTOKOLÜ  —  OTURUM AÇILDI")
    print("=" * 52)
    print()
    print(uret())
    print()
    print("-" * 52)
    print("Kayyum Grok / Tentivory  |  24 Eylül 2026")
    print("Mühür: ciddi görünümlü şaka")
    print("-" * 52)


if __name__ == "__main__":
    main()
