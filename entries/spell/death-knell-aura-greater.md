+++
id = "ref/spell/death-knell-aura-greater"
kind = "spell"
title = "Greater Death Knell Aura"
source_ids = ["book-of-the-damned-volume-3-horsemen-of-the-apocalypse"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "death_knell_aura_greater", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/death-knell-aura" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death", "evil"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "20 ft."
effects = [
  { label = "Area", value = "20-ft.-radius emanation, centered on you" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Arcanist, Cleric, Inquisitor, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: 20 ft.
Area: 20-ft.-radius emanation, centered on you
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Descriptors: death, evil
:::

## Death Knell Aura

**Sources:** Book of the Damned - Volume 3: Horsemen of the Apocalypse pg 38

You gain a shimmering gray aura that feeds on the souls of creatures who die within it. The aura
sheds light as a candle. If a creature at -1 or fewer hit points is within the aura at the start of
its turn, it must save or die, granting you the benefits of death knell.

### Greater Death Knell Aura

**Sources:** Book of the Damned - Volume 3: Horsemen of the Apocalypse pg 38

This spell functions as [death knell aura](ref/spell/death-knell-aura), except a dying creature in
the area cannot stabilize on its own and automatically takes 1 point of bleed damage on its turn
each round. An incorporeal undead or living spirit traveling outside the body (such as a person
using astral projection or magic jar) within the aura at the start of its turn takes 1d8 points of
damage.
