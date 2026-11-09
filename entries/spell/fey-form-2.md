+++
id = "ref/spell/fey-form-2"
kind = "spell"
title = "Fey Form II"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fey_form_2", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/fey-form-1" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "229"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 4 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
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
Level: 3: Alchemist, Bloodrager, Druid, Hunter, Investigator, Shaman\
4: Arcanist, Magus, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you plan to assume)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

### Fey Form II

This spell functions as [fey form I](ref/spell/fey-form-1), except it also allows you to assume the
form of a Tiny or Large creature of the fey type. Your base speed can't increase above 90 feet this
way. If the form you assume has any of the following abilities, you gain those abilities: burrow
speed 30 feet, climb speed 90 feet, fly speed 60 feet (good maneuverability), swim speed 60 feet,
all-around vision, [blindsense](ref/rule/blindsight-and-blindsense) 30 feet,
[darkvision](ref/rule/darkvision) 60 feet, [low-light vision](ref/rule/low-light-vision), scent, see
in darkness, abduct, animated hair, bleed, blood rage, boot stomp, burn, compression, constrict,
crushing leap, DR 2/cold iron, grab, heavy weapons, icewalking, kneecapper, nasal spray, no shadow,
oversized weapons, poison, putrid vomit, rock throwing (50 feet, 1d6 damage), sound mimicry,
trackless step, trample, tree meld, undersized weapons, and woodland stride. If the creature has
immunity to mind-affecting effects or poison, you gain a +4 resistance bonus on saves against those
effects. If the creature has any weaknesses, you gain them.

_Tiny Fey:_ If you assume this form, you gain a +6 size bonus to your Dexterity score and take a -2
penalty to your Strength score.

_Large Fey:_ If you assume this form, you gain a +4 size bonus to your Strength and Constitution
scores and take a -2 penalty to your Dexterity score.
