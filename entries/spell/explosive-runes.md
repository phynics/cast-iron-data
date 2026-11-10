+++
id = "ref/spell/explosive-runes"
kind = "spell"
title = "Explosive Runes"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "explosive_runes", path = "json/spells4.json" },
]
[[sources]]
publication = "core-rulebook"
page = "279"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one touched object weighing no more than 10 lbs." },
]
duration = "permanent until discharged (D)"
saving_throw = "see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Arcanist, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: permanent until discharged (D)
Saving throw: see text
Spell resistance: yes
Target: one touched object weighing no more than 10 lbs.
Descriptors: force
:::

You trace mystic runes upon a book, map, scroll, or similar object bearing written information. The
explosive runes detonate when read, dealing 6d6 points of force damage. Anyone next to the explosive
runes (close enough to read them) takes the full damage with no saving throw; any other creature
within 10 feet of the explosive runes is entitled to a Reflex save for half damage. The object on
which the explosive runes were written also takes full damage (no saving throw).

You and any characters you specifically instruct can read the protected writing without triggering
the explosive runes. Likewise, you can remove the explosive runes whenever desired. Another creature
can remove them with a successful [dispel magic](ref/spell/dispel-magic) or [erase](ref/spell/erase)
spell, but attempting to dispel or erase the explosive runes and failing to do so triggers the
explosion.

Magic traps such as explosive runes are hard to detect and disable. A character with the trapfinding
class feature (only) can use Disable Device to thwart explosive runes. The DC to find magic traps
using Perception and to disable them is 25 + spell level, or 28 for explosive runes.
