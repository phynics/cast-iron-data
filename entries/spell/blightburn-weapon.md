+++
id = "ref/spell/blightburn-weapon"
kind = "spell"
title = "Blightburn Weapon"
aon = "SpellDisplay.aspx?ItemName=Blightburn%20Weapon"
source_ids = ["kobolds-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blightburn_weapon", path = "json/spells2.json" },
]
[[sources]]
publication = "kobolds-of-golarion"
page = "26"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 5 },
  { class = "Inquisitor", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one weapon" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Alchemist, Inquisitor, Investigator, Magus\
5: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: one weapon
:::

You transform the target weapon into pure blightburn. The weapon functions as normal, but any
creature that touches it, or that it strikes, takes 2d6 points of fire damage each round it remains
in contact. In addition, the weapon emanates an aura of radiation that causes
[blightburn sickness](ref/disease/blightburn-sickness). This is as the disease, but with a 10-foot
radius and a save DC equal to this spell's save DC.
