+++
id = "ref/spell/phantom-trap"
kind = "spell"
title = "Phantom Trap"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phantom_trap", path = "json/spells7.json" },
]
[[sources]]
publication = "core-rulebook"
page = "320"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (special dust worth 50 gp)"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "permanent (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Arcanist, Mesmerist, Occultist, Psychic, Red Mantis Assassin, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S, M (special dust worth 50 gp)
Range: touch
Duration: permanent (D)
Saving throw: none
Spell resistance: no
Target: object touched
Subschool: Glamer
Descriptors: glamer
:::

This spell makes a lock or other small mechanism seem to be trapped to anyone who can detect traps.
You place the spell upon any small mechanism or device, such as a lock, hinge, hasp, cork, cap, or
ratchet. Any character able to detect traps, or who uses any spell or device enabling trap
detection, is certain a real trap exists. Of course, the effect is illusory and nothing happens if
the trap is "sprung"; its primary purpose is to frighten away thieves or make them waste precious
time.

If another phantom trap is active within 50 feet when the spell is cast, the casting fails.
