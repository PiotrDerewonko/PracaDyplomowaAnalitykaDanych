# PracaDyplomowaAnalitykaDanych

## Wymagania
- Python `>=3.13`
- `uv`

## 1. Instalacja `uv`

### Windows (PowerShell)
```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

### macOS / Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Sprawdzenie instalacji:
```bash
uv --version
```

## 2. Srodowisko i zaleznosci

W katalogu projektu:
```bash
uv venv
```

Aktywacja srodowiska:

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

Instalacja zaleznosci:
```bash
uv sync
```

## 3. Dane wejsciowe

W katalogu `data/` musi byc plik:

- `data/dane_projektowe_ny_collisions.csv`

## 4. Czyszczenie danych (`czyszczenie_danych_2.ipynb`)

Uruchom notebook:
```bash
uv run jupyter notebook czyszczenie_danych_2.ipynb
```

Nastepnie wykonaj wszystkie komorki (`Run All`). Notebook tworzy:

- `data/dane_przetworzone_2.csv`
- `data/dane_pojazdy_przyczyny_2.csv`
- `data/raport_czyszczenia_2.csv`

## 5. Analiza danych (`analiza_danych.ipynb`)

Po czyszczeniu danych uruchom:

```bash
uv run jupyter notebook analiza_danych.ipynb
```

Notebook zawiera analize zgodna z wymaganiami w `docs/informacje_o_projekcie_zaliczeniowym`.

## 6. Aktualny sposob pracy

Projekt jest obecnie realizowany w notebookach:

- `czyszczenie_danych_2.ipynb`
- `analiza_danych.ipynb`
