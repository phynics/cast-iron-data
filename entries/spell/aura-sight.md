+++
id = "ref/spell/aura-sight"
kind = "spell"
title = "Aura Sight"
aon = "SpellDisplay.aspx?ItemName=Aura%20Sight"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aura_sight", path = "json/spells.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "174"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 4 },
  { class = "Investigator", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Alchemist, Arcanist, Cleric, Investigator, Mesmerist, Oracle, Psychic, Shaman, Sorcerer, Spiritualist, Warpriest, Witch, Wizard\
4: Inquisitor
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

This spell makes your eyes glow and allows you to see alignment auras within 120 feet of you. The
effect is similar to that of a [detect chaos/evil/good/law](ref/spell/detect-chaos-evil-good-law)
spell, but aura sight does not require concentration, and it discerns an aura's location and power
more quickly.

You know the location and power of all chaotic, evil, good, and lawful auras within your sight. An
aura's power depends on a creature's Hit Dice or an item's caster level, as noted in the description
of the detect evil spell. If an item or a creature bearing an aura is in line of sight, you can
attempt a Knowledge (religion) check to determine the aura's strength (one check per aura; DC 15 +
spell level, or 15 + 1/2 caster level for a non-spell effect).

Aura sight can be made permanent with a [permanency](ref/spell/permanency) spell by a caster of 11th
level or higher at a cost of 7,500 gp.
