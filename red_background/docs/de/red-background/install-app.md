---
title: App installieren
order: 10
roles: [System Manager]
---

# App installieren

## Bench

```bash
bench get-app https://github.com/alyf-de/red_background.git --branch version-15
bench --site SITE install-app red_background
```

## Upgrade

Sites mit der bisherigen CSS-only-App behalten nach dem Upgrade den **Light Red**-Tint:

```bash
bench --site SITE migrate
```

Weiter: [Site-Einstellungen](/app/docs/de/red-background/site-settings).
