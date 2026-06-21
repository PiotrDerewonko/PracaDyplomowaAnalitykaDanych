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

## 4. Przygotowanie danych w Jupyter

Nowa wersja projektu do oddania w Jupyterze korzysta z notebooka:

- `czyszczenie_danych_2.ipynb`

Najprościej:
```bash
uv run jupyter notebook czyszczenie_danych_2.ipynb
```

Następnie wykonaj wszystkie komórki notebooka (`Run All`), aby utworzyć:

- `data/dane_przetworzone_2.csv`
- `data/dane_pojazdy_przyczyny_2.csv`
- `data/raport_czyszczenia_2.csv`

## 5. Analiza danych w Jupyter

Po przygotowaniu danych uruchom:

```bash
uv run jupyter notebook analiza_danych.ipynb
```

Notebook `analiza_danych.ipynb` zawiera analizę według punktów z `docs/informacje_o_projekcie_zaliczeniowym`.

## 6. Uruchomienie aplikacji Streamlit

```bash
uv run streamlit run report_app.py
```
