# Skill library maintenance

- Preserve existing skill purpose, source attribution and user-specific behavior unless the requested change intentionally alters it.
- Each top-level skill directory must have SKILL.md, README.md, skill.json, CHANGELOG.md and ORIGIN.md.
- skill.json is the sole local package version authority. Update it and CHANGELOG.md for behavioral changes.
- Keep runtime artifacts and machine-specific configuration outside this repository.
- Run scripts/validate.py, regenerate with scripts/catalog.py, then run validate.py --check-lock.
- Do not edit installed copies separately; this checkout is the maintained source.
- Never treat third-party imports as original work or infer a redistribution license from missing metadata.
