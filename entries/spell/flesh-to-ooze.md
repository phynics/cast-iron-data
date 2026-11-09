+++
id = "ref/spell/flesh-to-ooze"
kind = "spell"
title = "Flesh to Ooze"
aon = "SpellDisplay.aspx?ItemName=Flesh%20to%20Ooze"
source_ids = ["dungeon-denizens-revisited"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flesh_to_ooze", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/baleful-polymorph" },
]
[[sources]]
publication = "dungeon-denizens-revisited"
page = "19"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (alchemical reagents worth 100 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "1 creature or see text" },
]
duration = "permanent"
saving_throw = "Fortitude negates, Will partial, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (alchemical reagents worth 100 gp)
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent
Saving throw: Fortitude negates, Will partial, see text
Spell resistance: no
Target: 1 creature or see text
Subschool: Polymorph
:::

This functions like [baleful polymorph](ref/spell/baleful-polymorph), except the target becomes an
ooze. A creature of 3 HD or less becomes a gray ooze, 4-9 HD becomes a gelatinous cube or ochre
jelly, and 10+ HD becomes a black pudding. Alternatively, instead of a creature you may target a
quantity of inert flesh (such as that created by the stone to flesh spell) of sufficient mass, which
becomes an ooze of your choice.

Because a target's gear does not transform with it, any items fall under or within the ooze's body,
which may mean the items are destroyed. If the ooze has the split ability, splitting the ooze
creates one ooze that retains the creature's original identity (for the purpose of memories or
restoring the creature) and one normal mindless ooze of that type.
