---
title: Site settings
order: 20
roles: [System Manager]
---

# Site settings

Open **Desk Background Settings** (System Manager).

| Field | fieldname | Purpose |
| --- | --- | --- |
| *Site Colour Preset* | `site_color_preset` | Site-wide colour. **Standard** removes the tint. Default on install: **Light Red** (legacy red test-system look). |
| *Colour Strength* | `site_color_intensity` | **Tint** (softer) or **Strong** (more vivid). Default: **Tint**. Hidden when preset is **Standard**. |
| *Allow users to choose their own colour* | `allow_user_color` | When enabled, each user may set *Desk Colour* and *Desk Colour Strength* on their **User** record. Default on install: off. |
| *Clear all user choices on reset* | `clear_user_choices_on_reset` | Used with *Reset to Standard* to clear personal choices on all **User** records. |

## Presets

Twenty curated colours plus **Standard**. Each colour has **Tint** and **Strong** variants. Every surface and navbar meets at least **4.5:1** text contrast (WCAG AA).

Categories by hue: neutrals (Off White, Warm Gray, Cool Gray, Fog), warm beige and yellow (Sand, Wheat, Cream, Butter), orange (Peach, Apricot), red / pink (Light Red, Blush, Rose Quartz), green (Mint, Sage, Sea Foam), blue (Sky, Blue Gray), purple (Lavender, Lilac).

**Light Red** + **Tint** keeps the original soft red look from earlier app versions.

## Reset to Standard

Use *Reset to Standard* to set the site preset to **Standard** (stock Frappe colours). Optionally enable *Clear all user choices on reset* first.

Saving **Desk Background Settings** (or using *Reset to Standard*) clears cache and reloads Desk, same as the Desk "Clear Cache" action.

See also: [Personal desk colour](/app/docs/en/red-background/user-settings).
