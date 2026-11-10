+++
id = "ref/spell/magical-beast-shape"
kind = "spell"
title = "Magical Beast Shape"
aon = "SpellDisplay.aspx?ItemName=Magical%20Beast%20Shape"
source_ids = ["core-rulebook", "ultimate-wilderness", "animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magical_beast_shape", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/beast-shape-4" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "231"

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
Level: 3: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you plan to assume)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

### Magical Beast Shape

This spell functions as [beast shape IV](ref/spell/beast-shape-4) except you can assume the form of
only a magical beast of a size between Diminutive and Huge. If the form you assume has any of the
following abilities, you gain those abilities: burrow speed 60 feet, climb speed 90 feet, fly speed
120 feet (good maneuverability), swim speed 120 feet,
[blindsense](ref/rule/blindsight-and-blindsense) 60 feet, blindsight 30 feet,
[darkvision](ref/rule/darkvision) 90 feet, [low-light vision](ref/rule/low-light-vision), scent, see
in darkness, [tremorsense](ref/umr/tremorsense) 60 feet, blood drain, blood frenzy, breath weapon
(if damage, up to 12d6 points), constrict, [fast healing](ref/umr/fast-healing) 5, ferocity, grab,
hold breath, jet, no breath, poison, pounce, powerful charge, pull, rake, rend, roar, spikes,
trample, trip, and web. If the creature has immunity to poison, you gain a +8 resistance bonus on
saves against poison. If the creature has immunity or resistance to any energy types, you gain
resistance 20 to those energy types. If the creature has vulnerability to an energy type, you gain
that vulnerability.

_Diminutive Magical Beast:_ If you assume this form, you gain a +10 size bonus to your Dexterity
score and take a -4 penalty to your Strength score.

_Huge Magical Beast:_ If you assume this form, you gain a +8 size bonus to your Strength score, take
a -4 penalty on your Dexterity score, a +2 size bonus to your Constitution score, and gain a +7
natural armor bonus.
