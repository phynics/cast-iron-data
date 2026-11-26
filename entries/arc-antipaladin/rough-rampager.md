+++
id = "ref/arc-antipaladin/rough-rampager"
kind = "archetype"
title = "Rough Rampager"
aon = "ArchetypeDisplay.aspx?FixedName=Antipaladin%20Rough%20Rampager"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rough_rampager", path = "json/archetypes_antipaladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/antipaladin" },
]
[[sources]]
publication = "inner-sea-combat"
page = "43"

[fields]
kind = "archetype"
features = [
  { anchor = "aura-of-blood", level = 3 },
  { anchor = "aura-of-putrefaction", level = 8 },
  { anchor = "aura-of-quietus", level = 14 },
]
trades = [
  { replaces = "Aura of cowardice", feature = "aura-of-cowardice", by = ["aura-of-blood"] },
  { replaces = "Aura of despair", feature = "aura-of-despair", by = ["aura-of-putrefaction"] },
  { replaces = "Aura of sin", feature = "aura-of-sin", by = ["aura-of-quietus"] },
]
+++

Rough rampagers venerate [Rovagug](ref/faith/rovagug), reveling in the destruction the dark god
represents. Where others seek power, wealth, or revenge, the rough rampager merely focuses on
slaughter and mayhem. Because of their sheer destructive nature, most rough rampagers live short,
brutal lives swathed in blood and carnage before someone puts them to the blade. Legends speak of
dozens of rough rampagers wreaking havoc when Rovagug's spawn escape, acting as heralds and
harbingers of the greater destruction created by the Rough Beast's terrifying children.

## Aura of Blood (Su) {#aura-of-blood}

At 3rd level, a rough rampager radiates a palpably daunting aura that causes all enemies within 10
feet to take a -4 penalty on Constitution or Heal checks to stop [bleed](ref/rule/bleed) damage and
checks to stabilize while [dying](ref/misc/dying). This ability functions only while the antipaladin
is conscious. This ability replaces aura of cowardice.

## Aura of Putrefaction (Su) {#aura-of-putrefaction}

At 8th level, a rough rampager radiates an aura that causes the wounds of enemies within 10 feet to
weep blood. Injured enemies in the area take 1 point of bleed damage per round. This ability
functions only while the antipaladin is conscious. This ability replaces aura of despair.

## Aura of Quietus (Su) {#aura-of-quietus}

At 14th level, a rough rampager radiates an aura that causes the failure of healing spells,
[spell-like abilities](ref/umr/spell-like-abilities), and supernatural abilities used to restore
enemies within 10 feet of him. This is not an antimagic field, however, and ongoing or passive
effects are not affected. Casters can overcome this ability with a successful caster level check
versus the rough rampager's class level + 11. This ability replaces aura of sin.
