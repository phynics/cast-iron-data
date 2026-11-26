+++
id = "ref/arc-wizard/clocksmith"
kind = "archetype"
title = "Clocksmith"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Clocksmith"
source_ids = ["construct-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "clocksmith", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "construct-handbook"
page = "10"

[fields]
kind = "archetype"
features = [
  { anchor = "clockwork-bond", level = 1 },
  { anchor = "clockwork-expertise" },
  { anchor = "craft-construct", level = 1 },
  { anchor = "familiar-tinkering", level = 5 },
]
trades = [
  { replaces = "School powers granted by the wizard's arcane school", feature = "arcane-school", power = "school powers", by = ["clockwork-expertise"] },
  { replaces = "Scribe Scroll", feature = "scribe-scroll", by = ["craft-construct"] },
  { replaces = "Bonus feats gained at 5th, 10th, 15th, and 20th levels", feature = "bonus-feats", levels = [5, 10, 15, 20], by = ["familiar-tinkering"] },
  { alters = "Arcane bond", feature = "arcane-bond", by = ["clockwork-bond"] },
]
+++

Clocksmiths are oddities among wizard communities, pursuing the study and creation of clockwork
constructs to near obsession. These wizards favor mechanical experiments over other arcane pursuits.

## Clockwork Bond (Ex) {#clockwork-bond}

A clocksmith forms a bond with one of his [clockwork](ref/subtype/clockwork) creations and begins
play with a constructed familiar. He must select this familiar as his arcane bond. The constructed
familiar functions as a typical familiar of its type except as noted here. The construct familiar is
always a construct with the clockwork subtype. A construct familiar grants only half of its typical
bonus (minimum +1 bonus) from its special familiar ability to its master.

This alters arcane bond.

## Clockwork Expertise (Ex) {#clockwork-expertise}

A clocksmith is especially adept at dealing with clockworks. He gains a +2 bonus on saving throws
against effects created by creatures of the clockwork subtype. This bonus increases to +4 at 8th
level. Additionally, he treats his caster level as 1 higher when casting a spell that affects or
targets only creatures of the clockwork subtype. At 8th level, he treats his caster level as 2
higher when casting such a spell.

This replaces the school powers granted by the wizard's arcane school.

## Craft Construct {#craft-construct}

A clocksmith gains [Craft Construct](ref/feat/craft-construct) as a bonus feat, even if he does not
meet the prerequisites. He can create any construct, but he increases the cost required to create
constructs without the clockwork subtype by 50%.

This replaces Scribe Scroll.

## Familiar Tinkering (Ex) {#familiar-tinkering}

At 5th level, a clocksmith learns to improve upon his clockwork familiar. A clocksmith can grant his
familiar 1 evolution point worth of eidolon evolutions (_Pathfinder RPG Advanced Player's Guide_ 60)
for every 5 wizard levels he has, though he can't select any evolutions that require a specific base
form. Each time the clocksmith gains a level, he can change his familiar's evolutions. These
evolutions stack with those from the [Evolved Familiar](ref/feat/evolved-familiar) feat.

This replaces the bonus feats gained at 5th, 10th, 15th, and 20th levels.
