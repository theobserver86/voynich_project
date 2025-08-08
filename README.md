# voynich_project
# 📜 Voynich Project

**Research and decoding of the Voynich Manuscript using Codex-aligned ontology and recursive analysis protocols.**  
This project applies modern pattern-recognition methodologies, symbolic logic mapping, and ontology-based structuring to the enduring mystery of the Voynich Manuscript.

---

## 🔍 Project Overview

The **Voynich Project** is an open-source initiative to explore, decode, and document the Voynich Manuscript through:
- **Codex-aligned ontology** — mapping entities, relationships, and symbols into a structured semantic layer.
- **Recursive analysis protocols** — iterative passes over the text, illustrations, and patterns to refine hypotheses.
- **Interdisciplinary synthesis** — blending linguistics, cryptography, symbolic systems, and AI-driven analysis.

While the manuscript has resisted traditional translation efforts for over a century, this project treats it not as a puzzle to be "solved" in one step, but as a signal to be **decoded progressively through structured recursion**.

---

## 🗂 Repository Structure

```plaintext
voynich_project/
│
├── data/                  # High-resolution scans, transcriptions, symbol sets
├── analysis/              # Scripts, notebooks, and methodologies for pattern detection
├── ontology/              # Codex-aligned ontology definitions (YAML/JSON)
├── research/              # Historical context, linguistic studies, and references
├── output/                # Generated translations, symbolic mappings, and charts
└── docs/                  # Documentation, whitepapers, and progress reports

> Note: We’ll add `scripts/` and `outputs/` in a later commit once we publish runnable notebooks and code.

---

## 🚀 Getting Started

1) **Add data**
- Download high-res scans from the Beinecke Library and place them in `/images`.
- Put EVA ZL transcription files (TSV/CSV with `folio, region, line_no, eva_text`) in `/transcription/eva_zl/`.

2) **Follow the protocol**
- Read `workflow_protocol.md` for the analysis phases:
  - Data ingest → Segmentation (Currier A/B, section) → Baselines → Morphology → Cipher tests → Cross-modal clues → Dialect drift → Hypothesis ledger.

3) **Log claims**
- For any proposed decoding/partial mapping, copy `hypothesis_ledger_template.md` to `/research/` (or keep in root) and fill it out. Include data paths and exact rules so others can replicate.

---

## 📐 Principles

- **Authoritative Sources Only**: Beinecke scans, Zandbergen–Landini (EVA ZL) transcription.
- **Segment by Structure**: Currier A/B and section (botanical, astro, balneo, pharma, recipes).
- **Reproducibility First**: publish data paths, code, and exact parameters.
- **Falsifiability**: every claim must be testable and scoped (coverage %, rules, reversibility).
- **Open Collaboration**: invite replication and critique.

---

## 🤝 Contributing

- Open issues for data questions, methods, or results review.
- PRs welcome for:
  - Improved metadata (Currier/section maps)
  - Baseline calculations and visualizations
  - Morphology/cipher diagnostics
  - Cross-modal alignment (labels ↔ illustrations)
- Please explain datasets, steps, and assumptions clearly.

---

## 🏷️ Attribution

Created by **The Observer (Jacob Leander)** as part of ongoing research into Codex-aligned ontology and recursive analysis protocols.  
If you use or adapt this work, please **credit the original author** and link back to this repository.

---

## 📄 License

**MIT License** — free to use, modify, and distribute, with attribution.

---

## 🔗 Resources

- Yale Beinecke Voynich scans
- EVA ZL transcription (Zandbergen–Landini)
- `ontology_map.yaml` – tags & categories used in this project
- `workflow_protocol.md` – the analysis playbook
