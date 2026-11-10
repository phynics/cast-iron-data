+++
id = "ref/spell/haunting-mists"
kind = "spell"
title = "Haunting Mists"
aon = "SpellDisplay.aspx?ItemName=Haunting%20Mists"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "haunting_mists", path = "json/spells5.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "222"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
descriptors = ["fear", "shadow"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "20 ft."
effects = [
  { label = "Effect", value = "cloud spreads in 20-ft. radius, 20 ft. high" },
]
duration = "1 minute/level (D)"
saving_throw = "Will partial (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Arcanist, Bard, Mesmerist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: 20 ft.
Duration: 1 minute/level (D)
Saving throw: Will partial (see text)
Spell resistance: no
Effect: cloud spreads in 20-ft. radius, 20 ft. high
Subschool: Figment
Descriptors: fear, shadow
:::

An illusion of misty vapor inhabited by shadowy shapes arises around you. It is stationary. The
illusory mist obscures all sight, including [darkvision](ref/rule/darkvision), beyond 5 feet. A
creature 5 feet away has concealment (attacks have a 20% miss chance). Creatures farther away have
total concealment (50% miss chance, and the attacker cannot use sight to locate the target). All
creatures within the mist must save or take 1d2 points of Wisdom damage and gain the shaken
condition. The shaken condition lasts as long as the creature remains in the mist.
