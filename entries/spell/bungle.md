+++
id = "ref/spell/bungle"
kind = "spell"
title = "Bungle"
aon = "SpellDisplay.aspx?ItemName=Bungle"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bungle", path = "json/spells2.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "209"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one humanoid" },
]
duration = "concentration+ 2 rounds or until triggered"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Arcanist, Mesmerist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: concentration+ 2 rounds or until triggered
Saving throw: Will negates
Spell resistance: yes
Target: one humanoid
Subschool: Compulsion
:::

The target takes a -20 penalty on its next attack roll or check that requires a d20 roll. The action
must be one deliberately taken by the target on its turn. Creatures with more than 10 HD are
unaffected by this spell.
