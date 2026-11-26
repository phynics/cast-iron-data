+++
id = "ref/arc-arcanist/arcane-tinkerer"
kind = "archetype"
title = "Arcane Tinkerer"
aon = "ArchetypeDisplay.aspx?FixedName=Arcanist%20Arcane%20Tinkerer"
source_ids = ["construct-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcane_tinkerer", path = "json/archetypes_arcanist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/arcanist" },
]
[[sources]]
publication = "construct-handbook"
page = "10"

[fields]
kind = "archetype"
features = [
  { anchor = "manipulate-construct", level = 1 },
  { anchor = "break-magic-immunity", level = 5 },
]
trades = [
  { replaces = "The arcanist exploit gained at 1st level", feature = "arcanist-exploits", levels = [1], by = ["manipulate-construct"] },
  { replaces = "The arcanist exploits gained at 5th and 11th level", feature = "arcanist-exploits", levels = [5, 11], by = ["break-magic-immunity"] },
]
+++

All constructs are animated by magic in some capacity. Arcane tinkerers use their knowledge and
understanding of magic to disrupt or even destroy constructs.

## Manipulate Construct (Su) {#manipulate-construct}

An arcane tinkerer can turn the animating magic of a construct against itself. As a standard action,
she can expend 1 point from her arcane reservoir to impose a -1 penalty on a single construct's
attack and damage rolls for 1 round. The target can attempt a Will save to negate this effect (DC =
10 + [half](ref/misc/fractions-and-rounding) the arcane tinkerer's level + the arcane tinkerer's
Charisma modifier). At 7th level, instead of gaining an arcanist exploit, an arcane tinkerer can
improve her manipulate construct ability to instead affect a construct with _[slow](ref/spell/slow)_
for 1 round. At 13th level, if the arcane tinkerer has previously improved this ability, instead of
gaining an arcanist exploit, she can improve this ability again to instead cause a construct to
become [helpless](ref/misc/helpless) for 1 round.

This replaces the arcanist exploit gained at 1st level.

## Break Magic Immunity (Su) {#break-magic-immunity}

At 5th level, an arcane tinkerer can overcome a construct's immunity to magic. When targeting a
construct with a spell, the construct is instead treated as if it has
[spell resistance](ref/rule/spell-resistance) equal to 15 + the construct's CR. At 11th level, a
construct is instead treated as if it has [spell resistance](ref/rule/spell-resistance) equal to
11 + the construct's CR.

This replaces the arcanist exploits gained at 5th and 11th level.
