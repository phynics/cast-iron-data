+++
id = "ref/spell/versatile-weapon"
kind = "spell"
title = "Versatile Weapon"
aon = "SpellDisplay.aspx?ItemName=Versatile%20Weapon"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "versatile_weapon", path = "json/spells11.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/magic-weapon-greater" },
]
[[sources]]
publication = "advanced-players-guide"
page = "254"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Magus", level = 3 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 3 },
  { class = "Ranger", level = 2 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (iron filings)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one weapon or 50 projectiles, all of which must be together at the time of casting" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Bard, Hunter, Occultist, Ranger, Skald\
3: Arcanist, Bloodrager, Magus, Psychic, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (iron filings)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: one weapon or 50 projectiles, all of which must be together at the time of casting
:::

You transform the physical makeup of a weapon as you desire. This spell functions like
[greater magic weapon](ref/spell/magic-weapon-greater), except that it subtly alters the physical
properties of a weapon, enabling it to bypass [damage reduction](ref/rule/damage-reduction) of one
the following types: bludgeoning, cold iron, piercing, silver, or slashing. The affected weapon
still inflicts damage of its normal type and its [hardness](ref/umr/hardness) and hit points are
unchanged. This spell can be cast on a natural weapon or unarmed strike.
