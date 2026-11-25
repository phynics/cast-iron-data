+++
id = "ref/spell/fey-form-3"
kind = "spell"
title = "Fey Form III"
aon = "SpellDisplay.aspx?ItemName=Fey%20Form%20III"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fey_form_3", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/fey-form-2" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "230"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["polymorph"]
levels = [
  { class = "Alchemist", level = 6 },
  { class = "Arcanist", level = 7 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Investigator", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
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
Level: 6: Alchemist, Druid, Hunter, Investigator, Shaman\
7: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you plan to assume)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: polymorph
:::

### Fey Form III

This spell functions as [fey form II](ref/spell/fey-form-2) except it allows you to assume the form
of a Diminutive or Huge creature of the fey type. If the form you assume has any of the following
abilities, you gain those abilities: burrow speed 60 feet, climb speed 90 feet, fly speed 90 feet
(good maneuverability), swim speed 90 feet, all-around vision,
[blindsense](ref/rule/blindsight-and-blindsense) 60 feet, blindsight 30 feet,
[darkvision](ref/rule/darkvision) 90 feet, [low-light vision](ref/rule/low-light-vision), scent, see
in darkness, [tremorsense](ref/umr/tremorsense) 60 feet, abduct, animated hair, bleed, blood rage,
boot stomp, burn, compression, constrict, crushing leap, DR 5/cold iron, fear aura, frightful
presence, grab, heavy weapons, icewalking, kneecapper, luminous, nasal spray, no shadow, oversized
weapons, poison, putrid vomit, rend, rock throwing (100 feet, 2d6 damage), sound mimicry,
supernatural speed, tear shadow, trackless step, trample, tree meld, undersized weapons, and
woodland stride. If the creature has immunity or resistance to any energy types, you gain resistance
20 to those energy types. If the creature has immunity to mind-affecting effects or poison, you gain
a +8 resistance bonus on saves against those effects. If the creature has any weaknesses, you gain
those weaknesses.

_Diminutive Fey:_ If you assume this form, you gain a +8 size bonus to your Dexterity score and take
a -4 penalty to your Strength score.

_Huge Fey:_ If you assume this form, you gain a +6 size bonus to your Strength and Constitution
scores and take a -4 penalty to your Dexterity score.
