+++
id = "ref/spell/undead-anatomy-3"
kind = "spell"
title = "Undead Anatomy III"
aon = "SpellDisplay.aspx?ItemName=Undead%20Anatomy%20III"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "undead_anatomy_3", path = "json/spells11.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/undead-anatomy-2" },
]
[[sources]]
publication = "ultimate-magic"
page = "245"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Wizard", level = 3 },
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
Level: 3: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Red Mantis Assassin, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you plan to assume)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

### Undead Anatomy III

This spell functions as [undead anatomy II](ref/spell/undead-anatomy-2), except it also allows you
to assume the form of a Diminutive or Huge corporeal creature of the undead type. If the form you
assume has any of the following abilities, you gain the listed ability: burrow 30 feet, climb 90
feet, fly 90 feet (good maneuverability), swim 90 feet, all-around vision,
[blindsense](ref/rule/blindsight-and-blindsense) 30 feet, [darkvision](ref/rule/darkvision) 60 feet,
[low-light vision](ref/rule/low-light-vision), scent, constrict, disease, DR 5/-, fear aura, grab,
jet, natural cunning, overwhelming, poison, pounce, rake, trample, trip, unnatural aura, and web.

If the creature has immunity or resistance to any energy types, you gain resistance 20 to those
energy types. If the creature has vulnerability to an energy type, you gain that vulnerability. In
this form, you gain a +8 bonus on saves against mind-affecting effects, disease, poison, sleep, and
stunning. If the form has a vulnerability to an attack (such as sunlight), you gain that
vulnerability.

_Diminutive undead:_ If the form you take is that of a Diminutive undead, you gain a +6 size bonus
to your Dexterity, a -4 penalty to your Strength, and a +1 natural armor bonus.

_Huge undead:_ If the form you take is that of a Huge undead, you gain a +6 size bonus to your
Strength, a -4 penalty to your Dexterity, and a +6 natural armor bonus.
