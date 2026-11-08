+++
id = "ref/spell/vermin-shape-2"
kind = "spell"
title = "Vermin Shape II"
source_ids = ["ultimate-magic", "book-of-the-damned-volume-2-lords-of-chaos", "inner-sea-world-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vermin_shape_2", path = "json/spells11.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/vermin-shape-1" },
]

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Investigator", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of the creature whose form you plan to assume)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Druid, Hunter, Witch\
4: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you plan to assume)
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

### Vermin Shape II

**Sources:** Ultimate Magic pg 246, Inner Sea World Guide pg 297, Book of the Damned - Volume 2:
Lords of Chaos pg 49

This spell functions as [vermin shape I](ref/spell/vermin-shape-1), except it also allows you to
assume the form of a Tiny or Large creature of the vermin type. If the form you assume has any of
the following abilities, you gain the listed ability: burrow 30 feet, climb 60 feet, fly 60 feet
(good maneuverability), swim 60 feet, [darkvision](ref/rule/darkvision) 60 feet,
[low-light vision](ref/rule/low-light-vision), [tremorsense](ref/umr/tremorsense) 30 feet, scent,
blood drain, constrict, grab, lunge, poison, pull, trample, and web. You don't gain full immunity to
mind-affecting effects, but you do gain a +4 bonus on all saving throws against such effects.

_Tiny vermin:_ If you take the form of a Tiny vermin, you gain a +4 size bonus to your Dexterity, a
-2 penalty to your Strength, and a +1 natural armor bonus.

_Large vermin:_ If you take the form of a Large vermin, you gain a +4 size bonus to your Strength, a
-2 penalty to your Dexterity, and a +5 natural armor bonus.
