# Contributing

Suggestions via issues; PRs may be closed and applied manually to keep a single-author history.

## Scope

- Keep entries focused on efficient, edge, and wearable HAR.
- Prefer primary sources: official docs, paper pages, and canonical repositories.
- Keep descriptions concise and verifiable.

## Style

- Use deterministic ordering for generated content.
- Keep markdown clean and lightweight.
- Avoid large assets and binaries.

## Contributing workflow

1. Edit `data/entries.yaml`.
2. Run validation: `python scripts/validate_entries.py` or `make validate`.
3. Regenerate README: `python scripts/generate_readme.py` or `make generate`.
4. Check README consistency: `python scripts/check_generated_readme.py` or `make check`.
