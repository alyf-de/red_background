---
title: Seiteneinstellungen
order: 20
roles: [System Manager]
---

# Seiteneinstellungen

**Hintergrundfarbe Einstellungen** öffnen (System-Manager).

| Feld | fieldname | Zweck |
| --- | --- | --- |
| *Seitenfarbvoreinstellung* | `site_color_preset` | Seitenweite Farbe. **Standard** entfernt den Hintergrund. Standard bei Installation: **Hellrot** (bisheriges Test-System-Rot). |
| *Farbstärke* | `site_color_intensity` | **Sanft** oder **Kräftig**. Standard: **Sanft**. Ausgeblendet bei Preset **Standard**. |
| *Benutzern erlauben, eine eigene Farbe zu wählen* | `allow_user_color` | Wenn aktiv, kann jeder Nutzer *Schreibtisch-Farbe* und *Schreibtisch-Farbstärke* auf dem **Nutzer** setzen. Standard bei Installation: aus. |
| *Alle Benutzerauswahlen beim Zurücksetzen löschen* | `clear_user_choices_on_reset` | Mit *Auf Standard zurücksetzen* alle persönlichen Farben auf **Nutzer** löschen. |

## Voreinstellungen

Zwanzig kuratierte Farben plus **Standard**. Jede Farbe hat **Sanft** und **Kräftig**. Jede Fläche und Navbar erfüllt mindestens **4,5:1** Textkontrast (WCAG AA).

Kategorien nach Farbton: Neutraltöne (Off-White, Warmes Grau, Kühles Grau, Nebel), warmes Beige und Gelb (Sand, Weizen, Creme, Butter), Orange (Pfirsich, Aprikose), Rot / Rosa (Hellrot, Zartrosa, Rosenquarz), Grün (Minze, Salbei, Meerschaum), Blau (Himmel, Blaugrau), Violett (Lavendel, Flieder).

**Hellrot** + **Sanft** entspricht dem ursprünglichen weichen Rot früherer App-Versionen.

## Auf Standard zurücksetzen

*Auf Standard zurücksetzen* setzt die Seitenvoreinstellung auf **Standard** (Frappe-Standardfarben). Optional zuerst *Alle Benutzerauswahlen beim Zurücksetzen löschen* aktivieren.

Speichern von **Hintergrundfarbe Einstellungen** (oder *Auf Standard zurücksetzen*) leert den Cache und lädt den Schreibtisch neu, wie die Aktion *Cache leeren und neu laden*.

Siehe auch: [Persönliche Schreibtisch-Farbe](/app/docs/de/red-background/user-settings).
