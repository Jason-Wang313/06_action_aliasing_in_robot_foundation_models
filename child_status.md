# Child Status

- Stage: complete
- Current task: none
- Last updated: 2026-06-11
- Commands run:
  - `apply_patch` added `plan.md`
  - `apply_patch` added `child_status.md`
  - repository/tool probes for files, git state, and tool availability
  - `apply_patch` added `scripts/build_literature.py`
  - `python scripts/build_literature.py; exit 0`
  - literature matrix/count/sample/progress inspection commands
  - `python -c "import importlib.util; ..."; exit 0`
  - `apply_patch` added `scripts/synthesize_literature.py`
  - `python scripts/synthesize_literature.py; exit 0`
  - artifact check commands for `docs/`
  - `apply_patch` added `scripts/run_experiments.py`
  - `python scripts/run_experiments.py; exit 0`
  - experiment result inspection commands
  - `apply_patch` updated simulator to add redundant motor nullspace variation
  - `python scripts/run_experiments.py; exit 0`
  - web search identified latest official ICLR template source: ICLR 2026 Author Guide -> `https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip`
  - `Invoke-WebRequest` downloaded `paper/iclr2026.zip`; `Expand-Archive` expanded it
  - template path probe initially missed root-level `.tex`; recovered by listing inner `paper/iclr2026_template/iclr2026/`
  - copied `iclr2026_conference.sty`, `iclr2026_conference.bst`, `natbib.sty`, and `fancyhdr.sty` to `paper/`
  - `apply_patch` added `paper/main.tex`
  - `apply_patch` added `paper/references.bib`
  - first LaTeX build failed on unescaped underscores in appendix path text
  - `apply_patch` fixed appendix path text
  - `pdflatex; bibtex; pdflatex; pdflatex; exit 0` built `paper/main.pdf`
  - log checks found no unresolved citations/references/fatal errors; only underfull appendix path warnings
  - copied `paper/main.pdf` to `C:/Users/wangz/Downloads/06.pdf`
  - read GitHub plugin publish guidance; this run needs repo create/push rather than PR
  - updated `.gitignore` to ignore downloaded/extracted template archive
  - added `README.md` and `requirements.txt`
  - `gh auth status; exit 0`
  - `git add -A; git commit -m "Create action aliasing paper artifacts"; exit 0`
  - `gh repo create 06_action_aliasing_in_robot_foundation_models --public --source=. --remote=origin --push --description "..."; exit 0`
  - `gh repo view Jason-Wang313/06_action_aliasing_in_robot_foundation_models --json nameWithOwner,url,visibility,defaultBranchRef; exit 0`
  - checked `C:/Users/wangz/OneDrive/Desktop/06.pdf`; file was missing
  - `apply_patch` added `docs/final_audit.md`
  - `git status --short; git add docs/final_audit.md child_status.md README.md .gitignore; git commit -m "Add final audit"; git push; exit 0`
- Findings:
  - `docs/related_work_matrix.csv` has 3106 entries.
  - `docs/deep_read_extractions.csv` has 250 entries.
  - Required literature docs generated.
  - At alias strength 1.25: coarse token success 0.148; raw action charts 0.631; ESAC full context 0.743; ESAC hidden-context ablation 0.374; continuous upper 1.000.
  - `paper/main.pdf` built successfully, 223625 bytes.
  - Exact final PDF exists at `C:/Users/wangz/Downloads/06.pdf`, 223625 bytes.
  - Public GitHub repo exists: `https://github.com/Jason-Wang313/06_action_aliasing_in_robot_foundation_models`
  - Final audit commit `aaf9c80` pushed to `master`.
  - Desktop PDF status: pending orchestrator copy.
- Failures:
  - Initial `Get-Content paper/iclr2026_template/iclr2026_conference.tex` path was wrong because zip contains inner `iclr2026/`; recovered by recursive listing.
  - First LaTeX pass failed on Markdown-style appendix path text with underscores; patched to `\texttt{...}`.
- Recovery steps:
  - Used recursive file listing to locate template files.
  - Patched appendix path text and reran direct `pdflatex`/`bibtex` sequence.
- Notes:
  - Current limitation: literature extraction is metadata/abstract-based, not full-PDF reading for every row.
  - Final PDF target: `C:/Users/wangz/Downloads/06.pdf`
  - GitHub repo target: `06_action_aliasing_in_robot_foundation_models`

Exit code: 0
End time: 2026-06-11 02:05:37 +01:00
PDF exists: True

## Submission Hardening v2

- Completed: 2026-06-12 21:10:52 +01:00
- Terminal decision: workshop-only
- Canonical PDF target: `C:/Users/wangz/Downloads/06.pdf` (225620 bytes)
- Key experiment change: added ESAC context-corruption stress at alias strength 1.25.
- Key result: ESAC success is 74.2% with clean alias context, 60.5% with 20% corrupted context, 44.3% with 40% corrupted context, and 37.7% when alias context is hidden.
- Claim narrowed: ESAC requires reliable alias-resolving observations at test time and is not a real-robot or real-VLA result.
