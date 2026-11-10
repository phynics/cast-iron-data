+++
id = "ref/spell/tattoo-potion"
kind = "spell"
title = "Tattoo Potion"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tattoo_potion", path = "json/spells10.json" },
]
[[sources]]
publication = "inner-sea-magic"
page = "62"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 minute"
components = "V, S, M (a potion to be tattooed, special inks worth 500 gp)"
range = "one potion"
effects = [
  { label = "Effect", value = "one spell tattoo" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Arcanist, Bard, Investigator, Red Mantis Assassin, Skald, Sorcerer, Witch, Wizard
Casting time: 1 minute
Components: V, S, M (a potion to be tattooed, special inks worth 500 gp)
Range: one potion
Duration: instantaneous
Saving throw: none
Spell resistance: no
Effect: one spell tattoo
:::

When you cast this spell, you mix special tattoo inks into a potion of your choice. Once you finish
casting tattoo potion, the potion begins bubbling and fizzing - if no one drinks the potion within 1
minute of the spell being cast, the potion bubbles away into vapor and is destroyed.

When a potion under the effects of tattoo potion is imbibed, the effects of the potion do not occur.
Instead, the potion transforms into a [spell tattoo](ref/magic-tattoo/spell-tattoo) on the drinker's
chest tattoo slot - if the drinker already has a magic tattoo in this location, the tattoo potion is
wasted. Once the potion transforms into a spell tattoo, it remains in place permanently until it is
used as a spell tattoo.
