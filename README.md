# ⚡ Smart Grid Stability Prediction

Logistik regressiya yordamida elektr tarmog'ining (smart grid) barqaror yoki
nobarqaror bo'lishini bashorat qiluvchi machine learning loyihasi.

## 🎯 Muammo

Aqlli elektr tarmog'ida (1 ta ishlab chiqaruvchi + 3 ta iste'molchi) turli
sozlamalar (reaksiya vaqti, quvvat, narx elastikligi) asosida, tizim
**barqaror (stable)** yoki **beqaror (unstable)** bo'lishini oldindan aytib
berish — bu real energetika sohasida blackout'larni oldini olishga yordam
beradi.

## 📊 Dataset

[Smart Grid Stability](https://www.kaggle.com/datasets/pcbreviglieri/smart-grid-stability)
— 60,000 ta simulyatsiya, 12 ta sonli feature.

## 🔧 Ishlatilgan usullar

- Logistic Regression (sklearn)
- StandardScaler bilan normalizatsiya
- Train/test split (80/20, stratified)
- Baholash: Accuracy, Precision, Recall, F1-score, Confusion Matrix
- Threshold tuning (0.1–0.9)

## 📈 Natijalar

| Metrika | Qiymat |
|---|---|
| Accuracy | 81.95% |
| Precision | 84.15% |
| Recall | 88.35% |
| F1-score | 86.20% |

Baseline (har doim "unstable" deb aytuvchi soxta model) — 63.8% accuracy,
demak modelimiz undan ~18 foiz yaxshiroq ishlaydi.

## 💡 Muhim topilma

Eng ko'p ta'sir qiluvchi feature'lar — **reaksiya vaqti (tau)** va
**narx elastikligi (g)**, quvvat miqdorining o'zi (**p**) deyarli
ahamiyatsiz.
