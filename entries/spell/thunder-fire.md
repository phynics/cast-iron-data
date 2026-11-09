+++
id = "ref/spell/thunder-fire"
kind = "spell"
title = "Thunder Fire"
aon = "SpellDisplay.aspx?ItemName=Thunder%20Fire"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thunder_fire", path = "json/spells10.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "247"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of spent thunderstone)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "1 loaded firearm" },
]
duration = "instantaneous"
saving_throw = "Will negates (object), see text"
spell_resistance = "yes (object), see text"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Bard, Red Mantis Assassin, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of spent thunderstone)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates (object), see text
Spell resistance: yes (object), see text
Target: 1 loaded firearm
:::

The firearm targeted creates a thunderous report, even if the firearm is not loaded. Every creature
within 15 feet of the creature wielding or carrying the firearm must succeed at a Fortitude save or
be deafened for 1 minute. The creature wielding or carrying the firearm takes a -4 penalty on this
saving throw, and his misfire range increases by 1 for 1d4 rounds. If the firearm was loaded when it
was targeted by this spell, that ammunition is wasted.
