---
title: Install the app
order: 10
roles: [System Manager]
---

# Install the app

## Bench

```bash
bench get-app https://github.com/alyf-de/red_background.git
bench --site SITE install-app red_background
```

## Upgrade

Sites that already use the CSS-only app keep the **Light Red** tint after upgrade:

```bash
bench --site SITE migrate
```

Next: [Site settings](/app/docs/en/red-background/site-settings).
