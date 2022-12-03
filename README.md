# alphabetize-keys-in-vs-code-settings-json

VS Code's default behavior for settings.json is to append new settings to the end, which leaves it too out-of-order for my liking. This small Python program does two things:
- sort settings.json (or any given json file) alphabetically by the 1st level of keys
- remove trailing commas that VS Code permits but that don't conform to strict JSON

