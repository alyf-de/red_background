# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Frappe/ERPNext system administrators, implementation consultants, and developers who
work across several sites of the same system — production, staging, UAT, a local dev
bench — often with more than one open in adjacent browser tabs. Their job is ordinary
desk work (editing records, running reports, testing a change). The app serves them at
the moment before an action: it answers "which site am I in?" without them having to
read the URL bar.

## Product Purpose

Red Background tints the Frappe desk a light red so a non-production site is visually
unmistakable. It exists to prevent the class of mistake where real data is edited, or a
real document submitted, because the operator believed they were on a test system (or
the reverse). Success is that the wrong-site mistake stops happening, and that nobody
has to think about the app after installing it.

## Positioning

The signal is carried by the *whole background*, not a badge, banner, or ribbon. It is
unmissable in peripheral vision and in a browser tab preview, and it cannot be
mentally filtered out the way a corner label can. It works by installation rather than
configuration: an app present on a bench site is the statement that the site is not
production, so there is no setting to be left wrong.

## Operating Context

- Installed per site via `bench --site $SITE install-app red_background`, or from the
  Frappe Cloud marketplace.
- Delivered as `app_include_css` in `hooks.py` — a stylesheet loaded into every desk
  page. There is no Python logic, no DocType, and no runtime code path.
- Frappe ships both a light and a dark desk theme, switched by `data-theme` on the
  document root. Both must carry the signal; the app must never look broken in either.

## Capabilities and Constraints

- **Scope is the desk only.** The logged-in desk UI is the surface. Website/portal
  pages, the login screen, and print formats/PDFs are deliberately out of scope.
- **CSS custom properties only.** The app overrides Frappe's own theme variables
  (`--bg-color`, `--card-bg`, `--navbar-bg`, `--surface-menu-bar`, and peers). It does
  not add element selectors and does not use `!important`. This is the durable
  constraint: it keeps the app a few lines long, upgrade-safe across Frappe versions,
  and unable to fight the desk stylesheet. A surface that Frappe does not expose as a
  variable stays untinted rather than being forced.
- **Unconditional.** No settings DocType, no color option, no environment
  auto-detection. Installed means tinted.
- Versioned in step with Frappe major versions (current branch: `version-15`; a
  `version-16` line follows the same pattern).

## Brand Commitments

Published by ALYF GmbH (hallo@alyf.de) under MIT. App title "Red Background".
The color is red because red is the shared convention for "not the real thing" —
it is the product's identity, not a decorative choice, and must not drift to another hue.

## Evidence on Hand

- `img/red_background.png` — screenshot of the tinted desk, used in the README.
- Public repository: `github.com/alyf-de/red_background`; Frappe Cloud marketplace listing.
- No usage numbers, testimonials, or customer references exist. Future work must not
  invent them.

## Product Principles

1. **The signal must be impossible to miss and impossible to ignore.** Ambient, not a
   badge; peripheral vision and tab previews count as viewing conditions.
2. **Tint, never obstruct.** Desk work must stay fully legible and comfortable for a
   full working day. The red is a wash, not a warning screen.
3. **Stay a stylesheet.** Every addition is weighed against upgrade-safety; if it needs
   selectors, logic, or configuration, the default answer is no.
4. **Both themes are first-class.** Light and dark each get a considered treatment;
   neither is a fallback from the other.
5. **Install is the only decision.** Anything that could be configured wrong is a way
   for the signal to be silently absent on the day it matters.

## Accessibility & Inclusion

The tint must not be the *only* thing that has changed for a user who cannot perceive
it, and it must not reduce text contrast on any desk surface below what stock Frappe
provides. Red-green color vision deficiency does not affect the light-vs-tinted
distinction here (the change is in lightness and saturation as well as hue), but any
future color work must preserve that.
