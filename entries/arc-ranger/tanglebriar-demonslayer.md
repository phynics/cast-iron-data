+++
id = "ref/arc-ranger/tanglebriar-demonslayer"
kind = "archetype"
title = "Tanglebriar Demonslayer"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Tanglebriar%20Demonslayer"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tanglebriar_demonslayer", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "inner-sea-combat"
page = "46"

[fields]
kind = "archetype"
features = [
  { anchor = "favored-enemy", level = 1 },
  { anchor = "demonologist", level = 3 },
  { anchor = "expanded-spell-list" },
  { anchor = "fiendish-quarry", level = 11 },
  { anchor = "improved-fiendish-quarry", level = 19 },
]
trades = [
  { replaces = "Favored enemy", feature = "favored-enemy", by = ["favored-enemy"] },
  { replaces = "Endurance", feature = "endurance", by = ["demonologist"] },
  { replaces = "Quarry", feature = "quarry", by = ["fiendish-quarry"] },
  { replaces = "Improved quarry", feature = "improved-quarry", by = ["improved-fiendish-quarry"] },
]
+++

During the [elves](ref/race/elf)' long absence from Golarion, the nascent demon lord
[Treerazer](ref/monster/treerazer) took up residence in the Fierani Forest in what is now the Elven
kingdom of Kyonin. Eventually, the demon's presence in the forest drew the elves back to Golarion,
who sought to purge the fiendish blight from this once-sacred land. They defeated Treerazer but
could not destroy him, forcing him instead into the southern reaches of the Fierani, a corrupted
region of twisted plants and fiendish denizens called Tanglebriar. Even today, the elves constantly
battle to keep the corruption in the Tanglebriar from spreading to the rest of the Fierani Forest
and beyond. Though they are sworn foes of Treerazer and his kin, Tanglebriar demonslayers are known
to venture forth from Kyonin to broaden their expertise in the destruction of demons.

## Skills {#skills}

Tanglebriar demonslayers gain Knowledge (planes) as a class skill.

## Favored Enemy (Ex) {#favored-enemy}

At 1st level, a Tanglebriar demonslayer must choose favored enemy (evil outsider). At 5th level and
every time he advances his favored enemy bonus, the demonslayer must advance his bonus against evil
outsiders. In addition to the normal benefits of favored enemy, a Tanglebriar demonslayer gains a
bonus equal to 1/2 his favored enemy bonus on saving throws against spells,
[spell-like abilities](ref/umr/spell-like-abilities), and supernatural abilities of evil outsiders.
This ability is otherwise identical to and replaces the favored enemy ranger class ability.

## Demonologist (Ex) {#demonologist}

At 3rd level, a Tanglebriar demonslayer gains insight into his Abyssal enemies. The demonslayer
gains a bonus equal to 1/2 his class level on Knowledge (planes) checks that relate to demons,
Perception checks to pierce a demon's disguise, and Survival checks while tracking demons. This
bonus stacks with any bonuses from favored enemy. This ability replaces endurance.

## Expanded Spell List {#expanded-spell-list}

A Tanglebriar demonslayer adds the following spells to his spell list: 1st—_protection from evil_;
2nd—_align weapon, magic circle against evil_; 4th—_dimensional anchor, dismissal_.

## Fiendish Quarry (Su) {#fiendish-quarry}

At 11th level, when a Tanglebriar demonslayer chooses an evil outsider as his quarry, he can forgo
the normal +2 attack bonus and instead treat his weapon as if it were good-aligned versus his
quarry. This ability is otherwise identical to quarry and replaces that ability.

## Improved Fiendish Quarry (Su) {#improved-fiendish-quarry}

At 19th level, when a Tanglebriar demonslayer chooses an evil outsider as his quarry, he can forgo
the normal +4 attack bonus and instead treat his weapon as if it had the
_[holy](ref/magic-enh/holy)_ weapon special ability while attacking his quarry. This ability is
otherwise identical to improved quarry and replaces that ability.
