# PracaDyplomowaAnalitykaDanych

## Wymagania
- Python `>=3.13`
- `uv`

## 1. Instalacja `uv` (zależnie od platformy)

### Windows (PowerShell)
```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

### macOS / Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Po instalacji sprawdź:
```bash
uv --version
```

## 2. Utworzenie i aktywacja środowiska

W katalogu projektu:
```bash
uv venv
```

Aktywacja środowiska:

### Windows (PowerShell)
```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows (CMD)
```cmd
.venv\Scripts\activate.bat
```

### macOS / Linux
```bash
source .venv/bin/activate
```

Instalacja zależności:
```bash
uv sync
```

## 3. Dane wejściowe

Dane muszą znajdować się w katalogu `data/` pod poprawną nazwą:

- `data/dane_projektowe_ny_collisions.csv` (plik wejściowy)

Po przygotowaniu danych powstaje:

- `data/dane_przetworzone.csv`

## 4. Przygotowanie danych

Przed uruchomieniem aplikacji uruchom plik:

- `przygotowanie_danych.ipynb`

Najprościej:
```bash
uv run jupyter notebook przygotowanie_danych.ipynb
```

Następnie wykonaj wszystkie komórki notebooka (`Run All`), aby uporządkować dane.

## 5. Uruchomienie aplikacji Streamlit

```bash
uv run streamlit run report_app.py
```
