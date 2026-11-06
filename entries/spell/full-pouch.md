+++
id = "ref/spell/full-pouch"
kind = "spell"
title = "Full Pouch"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "full_pouch", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 3 },
  { class = "Investigator", level = 2 },
  { class = "Occultist", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 swift action"
components = "V, S, M (alchemical reagents or herbs worth 1 gp)"
range = "touch"
effects = [
  { label = "Target", value = "1 object touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates (object)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Arcanist, Bard, Druid, Hunter, Investigator, Skald, Sorcerer, Wizard\
3: Inquisitor, Occultist, Ranger
Casting time: 1 swift action
Components: V, S, M (alchemical reagents or herbs worth 1 gp)
Range: touch
Duration: instantaneous
Saving throw: Fortitude negates (object)
Spell resistance: no
Target: 1 object touched
:::

**Sources:** Arcane Anthology pg 20

You cast this spell as you draw out a consumable alchemical item to use. The object must be an
alchemical item, but not a dose of disease, a poison, a magic potion, or another type of consumable
item. The item divides itself into two nearly identical copies and the newly separated one is
delivered into your hand. The new item functions as the original in all ways except the copied item
suffers a slight reduction in quality. Saves against the new alchemical item's effects use the
original item's save DC or the save DC of this spell, whichever is
higher.^[1](ref/spell/full-pouch#footnote-n)^

###### ^1^ {#footnote-n}

The final two sentences make no sense, as choosing the higher DC would **not** be a reduction in
quality. Consult your GM.
