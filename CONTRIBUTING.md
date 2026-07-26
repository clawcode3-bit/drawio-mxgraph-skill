# Contributing

Thanks for helping improve Draw.io mxGraph Skill.

## Good contributions

- reproducible layout or connector-routing bugs;
- new icon mappings with clear license information;
- valid architecture and process examples;
- XML validation improvements;
- documentation corrections.

## Development workflow

1. Fork the repository and create a focused branch.
2. Keep changes small and explain the user-visible outcome.
3. Run the Skill validator.
4. Build at least one example diagram.
5. Validate every changed `.drawio` file.
6. Open a pull request with before/after details.

## Validation

```bash
python3 scripts/validate_examples.py
```

For a layout bug, attach the smallest JSON specification that reproduces the issue. Do not commit downloaded icon caches, credentials, or personal files.

## Commit style

Use short imperative messages, for example:

```text
Fix edge routing around grouped nodes
Add Azure database icon mapping
Clarify offline icon behavior
```
