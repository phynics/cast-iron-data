+++
id = "ref/spell/undead-anatomy-2"
kind = "spell"
title = "Undead Anatomy II"
aon = "SpellDisplay.aspx?ItemName=Undead%20Anatomy%20II"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "undead_anatomy_2", path = "json/spells11.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/undead-anatomy-1" },
]
[[sources]]
publication = "ultimate-magic"
page = "244"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["polymorph"]
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Arcanist", level = 5 },
  { class = "Investigator", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Red Mantis Assassin", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of the creature whose form you plan to assume)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Alchemist, Arcanist, Investigator, Magus, Red Mantis Assassin, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you plan to assume)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: polymorph
:::

### Undead Anatomy II

This spell functions as [undead anatomy I](ref/spell/undead-anatomy-1), except it also allows you to
assume the form of a Tiny or Large corporeal creature of the undead type. If the form you assume has
any of the following abilities, you gain the listed ability: climb 60 feet, fly 60 feet (good
maneuverability), swim 60 feet, [darkvision](ref/rule/darkvision) 60 feet,
[low-light vision](ref/rule/low-light-vision), blood drain, DR 5/bludgeoning, scent, freeze, grab,
mimicry, pounce, shadowless, sound mimicry, and trip.

In this form, you gain a +4 bonus on saves against mind-affecting effects, disease, poison, sleep,
and stunning. If the form has a vulnerability to an attack (such as sunlight), you gain that
vulnerability.

_Tiny undead:_ If the form you take is that of a Tiny undead, you gain a +4 size bonus to your
Dexterity, a -2 penalty to your Strength, and a +1 natural armor bonus.

_Large undead:_ If the form you take is that of a Large undead, you gain a +4 size bonus to your
Strength, a -2 penalty to your Dexterity, and a +4 natural armor bonus.
