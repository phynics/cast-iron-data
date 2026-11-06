+++
id = "ref/spell/gift-of-the-deep"
kind = "spell"
title = "Gift of the Deep"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gift_of_the_deep", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one non-mutated sahuagin/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level (D)"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Cleric, Oracle, Warpriest\
5: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: one non-mutated sahuagin/level, no two of which can be more than 30 ft. apart
Subschool: Polymorph
:::

**Sources:** Monster Codex pg 189

You give the targets the appearance and many of the abilities of sahuagin mutants, with effects as
described below. Choose one benefit for all targets of this spell. This spell has no effect on
sahuagin that are already mutants or already under the effects of gift of the deep.

_Four-Armed:_ The sahuagin sprouts an extra pair of arms - which can be used to make claw attacks
(dealing 1d4 points of damage), or to wield weapons or hold items. It gains the benefits of the
[Multiattack](ref/feat/multiattack) and [Multiweapon Fighting](ref/feat/multiweapon-fighting) feats.

_Malenti:_ The sahuagin's features shift to resemble those of an aquatic elf. It loses its light
blindness as well as its claw and bite attacks. The sahuagin gains a +4 enhancement bonus to
Dexterity and Charisma, and a +10 circumstance bonus on Disguise checks to appear to be an aquatic
elf.

_Prehistoric:_ The sahuagin grows in size, as enlarge person. It also gains a +2 enhancement bonus
to its natural armor.

_Shark-Blooded:_ The sahuagin's tail elongates and melds with its legs. Its mouth enlarges,
increasing its bite damage by one size category (to 1d6 for a typical sahuagin). Its swim speed
increases by 20 feet, but its land speed is reduced to 5 feet. The sahuagin can't be tripped.

_Sightless:_ The sahuagin is blinded, but gains the benefits of the Blind Fight feat and
[blindsense](ref/rule/blindsight-and-blindsense) with a range of 90 feet.

_Spined:_ Spines grow on the sahuagin's scales. Any creature that successfully grapples with it, is
grappled by it, or hits it with an unarmed strike or natural weapon takes 1d4 points of piercing
damage. The sahuagin also gains the benefits of the [Improved Grapple](ref/feat/improved-grapple)
feat.
