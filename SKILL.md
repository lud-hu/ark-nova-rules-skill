---
name: arche-nova-regelfragen
description: "Use when answering Arche Nova rules questions."
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [arche-nova, brettspiel, regeln, deutsch]
    category: gaming
---

# Arche Nova – Regelhilfe

Bei jeder Frage zu Arche Nova diesen Skill laden. Deutsch, knapp und verständlich antworten. Regeln anhand der mitgelieferten Quellen nachschlagen, nicht aus dem Gedächtnis behaupten.

## When to Use

Für Regelfragen, Zugprüfungen, Aktionsstärke, Bau- und Gehegeregeln, Tiere, Verband, Sponsoren, Pause, Endwertung und Solo-Regeln des Grundspiels Arche Nova sowie Fragen zur mitgelieferten Beispielpartie.

## Quellen

- `assets/regelbuch-de-v2.pdf`: Original `AN_Rules_DE_V2_0_Web.pdf`, 20 PDF-Seiten.
- `assets/quickstart-de-v1.pdf`: Original `Arche_Nova_QuickStartGuide_V1_DE_Web_low.pdf`, 12 PDF-Seiten; illustrierte Beispielpartie.
- `references/regelbuch.md`, `references/quickstart.md`: vollständige seitenweise Textextraktionen.
- `references/themenindex.md`: kompakter Themenwegweiser.
- `references/seitenindex.md`: seitenweise Extraktionsübersicht und Prüfsummen.

Regelbuch vor Quickstart: Eine Beispielpartie begründet keine neue allgemeine Regel. Erweiterungen, separates Glossar, Symbolübersicht und spätere FAQ sind nicht mitgeliefert. Bei nicht geklärten Karten-/Sonderfällen Kartentext oder Foto erfragen. Zusätzliche offizielle Quellen bei Bedarf recherchieren und ausdrücklich kennzeichnen. Community-Auslegung nicht als offizielle Regel ausgeben.

## Regelfragen beantworten

1. Textreferenzen nach Begriffen und Synonymen durchsuchen. Passenden Abschnitt vollständig einschließlich Voraussetzungen, Ausnahmen und Nachbarseiten lesen.
2. Aktion I/II, Stärke, Kosten, Voraussetzungen, Boni und Zeitpunkt auseinanderhalten. Grundspiel und Erweiterungen nicht vermischen.
3. Symbole, Zahlen, Kartentexte und räumliche Beispiele bei Bedarf im gerenderten Original mit `vision_analyze` prüfen. Extraktion kann diese Inhalte beschädigen oder Textspalten vermischen; nicht raten. Bei abweichenden Kartensymbolen und Zahlen ist die Originalabbildung maßgeblich.
4. Zuerst konkrete Entscheidung, dann Begründung und ggf. kurzes Beispiel. Eigene Beispiele als solche kennzeichnen. Berechnungen mit Werkzeug prüfen.
5. Dokument und Seite angeben, z. B. „Regelbuch, S. 10 (PDF-Seite 10)“. Gedruckte Seitenzahl bei Abweichungen visuell prüfen. Unsicherheit offen benennen.
6. Bei hilfreichen Originalbeispielen einen passenden Bildausschnitt direkt im Chat mitschicken. Alle relevanten Symbole, Pfeile und Beschriftungen im Ausschnitt belassen; Kontext erklären.

## Bilder aus den Original-PDFs

`scripts/render_page.py` rendert ganze Seiten und Ausschnitte. Seiten **1-basiert**; `--crop x0 y0 x1 y1` als relative Koordinaten zwischen 0 und 1, Ursprung oben links. Zuerst ganze Seite ansehen, dann zuschneiden.

```sh
/home/hermes/.venvs/arche-nova/bin/python <SKILL_DIR>/scripts/render_page.py regelbuch 10 --output /home/hermes/.hermes/cache/scratch/arche-nova-s10.png
/home/hermes/.venvs/arche-nova/bin/python <SKILL_DIR>/scripts/render_page.py quickstart 5 --crop 0 0.2 1 0.8 --output /home/hermes/.hermes/cache/scratch/arche-nova-beispiel.png
```

Vor Versand mit `vision_analyze` prüfen. Telegram: eigene Antwortzeile `MEDIA:/absoluter/pfad/bild.png`, dazu Quelle, Seite und Kontext nennen. Nicht nur den Dateipfad als Text schicken. Originalbeispiele nicht durch erfundene Bilder ersetzen. Zweckgebundene Ausschnitte statt ungefragt vollständiger Bücher senden.

## Teilen und Installation

Teilbar als `SKILL.md` oder als vollständiges ZIP mit `SKILL.md`, `references/`, `assets/`, `scripts/`. Alle Pfade sind relativ zum Skillordner. **SKILL.md allein enthält den Workflow, nicht alle Regeln und Bilder**; für vollständige Offline-Nutzung das Paket mitgeben. Die Dateien stammen vom Nutzer; keine Lizenz zur öffentlichen Weiterverbreitung wird behauptet. Verlagsrechte beachten.

Renderer benötigt Python 3 und PyMuPDF, getestet mit 1.26.7. Portabel z. B. `uv run --with 'pymupdf==1.26.7' python scripts/render_page.py regelbuch 10 --output seite.png`. Lokal steht `/home/hermes/.venvs/arche-nova/bin/python` bereit. Titelblätter enthalten wenig oder keinen Text; das ist kein Verlust von Regeltext. Fehlende Originaldateien ausdrücklich melden.
