# RightsGuide

**Guide till LSS, assistansersättning och vårdstöd**

En enkel GTK4/Adwaita-app som hjälper dig förstå dina rättigheter till stöd och service i Sverige.

## Funktioner

- 🏠 **LSS** – Lagen om stöd och service till vissa funktionshindrade
- 🤝 **Personlig assistans** – Assistansersättning och personlig assistans
- 🏥 **Vård och omsorg** – Stöd från sjukvård och socialtjänst
- 💰 **Ekonomiskt stöd** – Bidrag och ersättningar

Alla texter är skrivna i lättläst svenska med piktogramstöd.

## Installation

### Beroenden

- Python 3.8+
- GTK 4
- libadwaita
- PyGObject

#### Fedora/RHEL

```bash
sudo dnf install python3-gobject gtk4 libadwaita
```

#### Ubuntu/Debian

```bash
sudo apt install python3-gi gir1.2-gtk-4.0 gir1.2-adw-1
```

#### Arch Linux

```bash
sudo pacman -S python-gobject gtk4 libadwaita
```

### Installera appen

```bash
pip install .
```

### Kör utan installation

```bash
python -m rightsguide.app
```

## Skärmdump

Appen visar kategorier med stora, lättlästa knappar. Tryck på en kategori för att se vanliga frågor, och tryck på en fråga för att läsa svaret.

## Licens

GPL-3.0
