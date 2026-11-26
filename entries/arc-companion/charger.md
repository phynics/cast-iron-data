+++
id = "ref/arc-companion/charger"
kind = "archetype"
title = "Charger"
source_ids = ["animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "charger", path = "json/archetypes_COMPANION.json" },
]
[[sources]]
publication = "animal-archive"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "animal-feats" },
  { anchor = "animal-skills" },
  { anchor = "mounted-challenge" },
  { anchor = "barding-training", level = 3 },
  { anchor = "indefatigable", level = 6 },
  { anchor = "stalwart-steed", level = 15 },
]
trades = [
  { replaces = "Share Spells", by = ["mounted-challenge"] },
  { replaces = "Evasion", by = ["barding-training"] },
  { replaces = "Multiattack", by = ["barding-training"] },
  { replaces = "Devotion", by = ["indefatigable"] },
  { replaces = "Improved Evasion", by = ["stalwart-steed"] },
]
+++

The mighty charger is a boon to heavily armored and armed champions, bearing them and their
ironmongery into battle without hesitation.

## Animal Feats {#animal-feats}

In addition to the standard animal companion feats, a charger may select
[Charge Through](ref/feat/charge-through), [Greater Overrun](ref/feat/greater-overrun),
[Improved Great Fortitude](ref/feat/improved-great-fortitude), and
[Improved Iron Will](ref/feat/improved-iron-will).

## Animal Skills {#animal-skills}

Chargers treat Intimidate as a class skill.

## Mounted Challenge (Ex) {#mounted-challenge}

When ridden by a [cavalier](ref/class/cavalier), chargers gain
[half](ref/misc/fractions-and-rounding) of the bonuses and penalties granted by the cavalier's
challenge class feature. This ability replaces share spells.

## Barding Training (Ex) {#barding-training}

At 3rd level, a charger's armor check penalty for wearing barding or for
[carrying a medium load](ref/rule/carrying-capacity) is reduced by 1 and the maximum Dexterity bonus
for its armor and load increases by 1. Reduce the armor check and medium load penalties by an
additional 1 for every 6 levels after 3rd; increase the maximum Dexterity bonus for the charger's
armor by an additional 1 for every 6 levels after 3rd. In addition, the charger's speed does not
decrease when wearing medium armor or carrying a medium load. At 9th level, a charger can move at
normal speed in heavy armor or while carrying a heavy load. This ability replaces evasion and
Multiattack.

## Indefatigable (Ex) {#indefatigable}

At 6th level, a charger becomes immune to [fatigue](ref/misc/fatigued). This ability replaces
devotion.

## Stalwart Steed (Ex) {#stalwart-steed}

At 15th level, the charger gains the ability to withstand great punishment and stress. Whenever the
charger succeeds at a Fortitude or Will save that would normally result in a reduced or partial
effect, the charger is unaffected. This ability replaces improved evasion.
