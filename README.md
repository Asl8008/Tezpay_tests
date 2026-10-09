# Tezpay Mobile Automation Tests

Tezpay Android ilovasi uchun avtomatlashtirilgan testlar to'plami (Mobile QA Automation).

## Texnologiyalar
- **Python 3**
- **Appium** (Appium-Python-Client)
- **Pytest**
- **Selenium WebDriver**
- **Allure Report**
- **Page Object Model (POM)** pattern

## O'rnatish

1. Virtual muhit yaratish va faollashtirish:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Kerakli kutubxonalarni o'rnatish:
```bash
pip install -r requirements.txt
```

## Testlarni ishga tushirish

1. Appium serverni ishga tushiring:
```bash
appium
```

2. Testlarni bajarish:
```bash
pytest
```
yoki taqdim etilgan skript orqali:
```bash
./run_tests.sh
```

## Allure hisobotlarini ko'rish
```bash
allure serve allure-results
```
