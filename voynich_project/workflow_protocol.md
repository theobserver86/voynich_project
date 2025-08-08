# Voynich Decoding Workflow – Codex Protocol Integration

## 1. Data Ingest
- Source: Yale/Beinecke scans (TIFF/JPEG)  
- Text: Zandbergen–Landini EVA ZL transcription
- Store: `/images`, `/transcription/eva_zl`

## 2. Segmentation
- Apply Currier A/B labels per voynich.nu dataset
- Tag each folio with section type

## 3. Baseline Analysis
- Zipf distribution
- Shannon entropy per line
- Long-range mutual information
- Compare with control corpora

## 4. Morphological Modeling
- Apply BPE/Morfessor for token segmentation
- Map affix behavior vs. position in line
- Identify statistical “gallows” symbol behavior

## 5. Cipher Diagnostics
- Test verbose cipher hypothesis
- Test homophonic cipher flattening
- Test null removal sharpening

## 6. Cross-Modal Clues
- Align labels with repeated visual motifs
- Build co-occurrence graphs of label reuse

## 7. Dialect Drift
- Train separate A/B language models
- Compute cross-perplexity
- Identify morphological shifts

## 8. Hypothesis Ledger
- Score claims (dataset openness, decoding rules, coverage %, reversibility, replication)
- Maintain a running public ledger
