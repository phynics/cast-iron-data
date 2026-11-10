+++
id = "ref/spell/destabilize-powder"
kind = "spell"
title = "Destabilize Powder"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "destabilize_powder", path = "json/spells3.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "228"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a few drops of liquor)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "1 loaded firearm" },
]
duration = "instantaneous"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Red Mantis Assassin, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a few drops of liquor)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: 1 loaded firearm
:::

This spell makes the ammunition in the target firearm is prone to misfire. Increase the misfire
range by 1 + 1 per five caster levels (maximum +5) for the ammunition currently loaded into that
firearm. If aware of this spell's effect prior to firing the altered ammunition (a DC 17 Spellcraft
check to identify the spell being cast or similar effect), the firearm's user can spend a standard
action to clear the altered ammunition from the firearm. Doing so destroys that ammunition.
