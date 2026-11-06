+++
id = "ref/spell/invisibility-sphere"
kind = "spell"
title = "Invisibility Sphere"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "invisibility_sphere", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M"
range = "personal or touch"
effects = [
  { label = "Area", value = "10-ft.-radius emanation around the creature" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Arcanist, Bard, Mesmerist, Occultist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M
Range: personal or touch
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Area: 10-ft.-radius emanation around the creature
Subschool: Glamer
Descriptors: glamer
:::

**Sources:** PRPG Core Rulebook pg 302

This spell functions like invisibility, except that this spell confers invisibility upon all
creatures within 10 feet of the recipient at the time the spell is cast. The center of the effect is
mobile with the recipient.

Those affected by this spell can see each other and themselves as if unaffected by the spell. Any
affected creature moving out of the area becomes visible, but creatures moving into the area after
the spell is cast do not become invisible. Affected creatures (other than the recipient) who attack
negate the invisibility only for themselves. If the spell recipient attacks, the invisibility sphere
ends.
