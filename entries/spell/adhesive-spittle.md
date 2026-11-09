+++
id = "ref/spell/adhesive-spittle"
kind = "spell"
title = "Adhesive Spittle"
aon = "SpellDisplay.aspx?ItemName=Adhesive%20Spittle"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "adhesive_spittle", path = "json/spells.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "172"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "15 ft."
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level or until discharged (see text)"
saving_throw = "Reflex partial"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Alchemist, Arcanist, Investigator, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: 15 ft.
Duration: 1 round/level or until discharged (see text)
Saving throw: Reflex partial
Spell resistance: no
Target: one creature
Subschool: Creation
:::

Once during this spell's duration, you can spit a viscous liquid as a standard action. This liquid
functions as a [tanglefoot bag](ref/eq-weapon/tanglefoot-bag), except you do not have to make a
successful attack roll to hit your target. The DCs to counteract this adhesive (to avoid being stuck
to the floor, to fly, to break the adhesive, or to cast a spell) use the spell's DC rather than a
tanglefoot bag's normal DCs. The adhesive persists for 2d4 rounds after you spit it.
