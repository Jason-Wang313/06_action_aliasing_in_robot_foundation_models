# Experiment Rigor Checklist

- [x] Detailed full-scale execution plan written before paper-specific edits.
- [x] Main alias-strength sweep regenerated with 10 seeds and 2,600/1,000 train/test rows.
- [x] Context-reliability suite regenerated with 10 seeds and 2,600/1,000 train/test rows.
- [x] Token granularity, chart count, data scale, shift, metric, threshold, and negative-control suites regenerated with 8 seeds.
- [x] Continuous regression upper retained as an outside-token comparator.
- [x] Oracle tokenization controls included.
- [x] Hidden-context and context-corruption failures included.
- [x] Random chart and raw-action chart controls included.
- [x] Effect-metric misspecification controls included.
- [x] Compact rows stored instead of raw datasets.
- [x] Final manuscript compiled to 25 pages before copying to the canonical PDF path.
- [x] Extracted final PDF text contains full-scale claims and no stale hardening/workshop markers.
- [ ] Real VLA/RFM action-token audit.
- [ ] Real robot or high-fidelity physics validation.
- [ ] Fully pinned package lockfile.
