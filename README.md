# Arche Nova – Regelhilfe als Agent-Skill

Deutschsprachiger Skill für Detailfragen zu den Regeln des Brettspiels **Arche Nova**. Er verbindet belegte Regelerklärungen mit den Originalabbildungen aus Regelbuch und Quickstart.

## Inhalt

- [`SKILL.md`](SKILL.md): Anweisungen für den Agenten.
- [`assets/regelbuch-de-v2.pdf`](assets/regelbuch-de-v2.pdf): bereitgestelltes deutsches Regelbuch V2, 20 Seiten.
- [`assets/quickstart-de-v1.pdf`](assets/quickstart-de-v1.pdf): bereitgestellter deutscher Quickstart V1, 12 Seiten.
- [`references/`](references/): seitenweise Textextraktionen, Themenindex und Quellenprüfsummen.
- [`scripts/render_page.py`](scripts/render_page.py): Originalseiten und Bildausschnitte als PNG rendern.

## Als Skill verwenden

Das **vollständige Repository** herunterladen oder klonen, nicht nur `SKILL.md`. Den Ordner unter dem Namen `arche-nova-regelfragen` in das Skillverzeichnis des verwendeten Agenten legen; `SKILL.md` liegt dabei direkt im Skillordner. Bei Hermes ist das standardmäßig `~/.hermes/skills/arche-nova-regelfragen/`. Bei abweichenden Profilen den passenden Profilordner verwenden.

`SKILL.md` allein ist ebenfalls teilbar, enthält aber nur den Arbeitsablauf und Verweise – nicht die Regeltexte oder Originalbilder. Für vollständige Offline-Nutzung gehören die Assets und Referenzen dazu.

Der Agent soll den Skill bei Arche-Nova-Fragen laden, passende Quellen nachschlagen und Dokument sowie Seite nennen. Bei Symbolen, Kartentexten und räumlichen Beispielen soll er die Originalabbildung prüfen. Das setzt Werkzeuge zum Lesen lokaler Dateien und zur Bildbetrachtung voraus; der Skill ist keine eigenständig laufende Chat-Anwendung.

## Originalbeispiele rendern

Python 3 und PyMuPDF werden benötigt. Mit [uv](https://docs.astral.sh/uv/), aus dem Repositoryordner:

```sh
uv run --with 'pymupdf==1.26.7' python scripts/render_page.py regelbuch 10 --output seite-10.png
uv run --with 'pymupdf==1.26.7' python scripts/render_page.py quickstart 5 --crop 0 0.2 1 0.8 --output ausschnitt.png
```

Alternativ in einer eigenen Python-Umgebung `pip install -r requirements.txt` und `python scripts/render_page.py ...` verwenden.

- Seitenzahlen sind **1-basiert**.
- Ausschnitte: `--crop x0 y0 x1 y1`, jeweils zwischen 0 und 1, Ursprung oben links.
- Erst die ganze Seite ansehen, dann einen sinnvollen Ausschnitt wählen. Nicht versehentlich zugehörige Pfeile, Beschriftungen oder Voraussetzungen abschneiden.
- Auf Telegram kann ein entsprechend ausgestatteter Agent die PNG-Datei als Bild senden. Andere Plattformen benötigen deren jeweilige Anhangsfunktion.
- Die absoluten `/home/hermes/...`-Pfade in `SKILL.md` beschreiben die ursprüngliche Installation. Auf anderen Systemen den portablen Befehl oben und eigene Ausgabepfade verwenden.

## Quellen und Grenzen

Die Original-PDFs wurden vom Nutzer bereitgestellt. Die seitenweisen Textreferenzen sind maschinelle Extraktionen, keine redigierte Regelübersetzung. Spalten, Symbole und Zahlen können fehlerhaft extrahiert sein; im Zweifelsfall ist die Originalseite maßgeblich.

Das Regelbuch hat Vorrang vor der Beispielpartie. Separates Glossar, Symbolübersicht, spätere FAQ und Erweiterungen sind nicht enthalten. Für dort nicht geklärte Karten-/Sonderfälle soll der Agent nach Kartentext oder Foto fragen, statt eine Regel zu erfinden.

## Rechte

Inoffizielles Hilfsprojekt, keine Verbindung zum Verlag behauptet. Rechte an Spiel, Regeltexten und Abbildungen verbleiben bei den jeweiligen Rechteinhabern. Die Aufnahme in dieses Repository begründet **keine freie Lizenz** für diese Inhalte. Auch extrahierte Regeltexte sind von diesem Hinweis umfasst; vor Weiterverwendung oder Weiterverbreitung die entsprechenden Rechte prüfen.
