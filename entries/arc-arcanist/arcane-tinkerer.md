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
replaces = ["The arcanist exploit gained at 1st level", "The arcanist exploits gained at 5th and 11th level"]
+++

All constructs are animated by magic in some capacity. Arcane tinkerers use their knowledge and
understanding of magic to disrupt or even destroy constructs.

**Manipulate Construct (Su)**

**Flavor:** An arcane tinkerer can turn the animating magic of a construct against itself.

**At 13th Level:** If the arcane tinkerer has previously improved this ability, instead of gaining
an arcanist exploit, she can improve this ability again to instead cause a construct to become
[helpless](ref/misc/helpless) for 1 round.

**At 7th Level:** Instead of gaining an arcanist exploit, an arcane tinkerer can improve her
_manipulate construct_ ability to instead affect a construct with [slow](ref/spell/slow) for 1
round.

**Replaces:** The arcanist exploit gained at 1st level

**Standard:** She can expend 1 point from her arcane reservoir to impose a -1 penalty on a single
construct's attack and damage rolls for 1 round. The target can attempt a Will save to negate this
effect (DC = 10 + [half](ref/misc/fractions-and-rounding) the arcane tinkerer's level + the arcane
tinkerer's Charisma modifier).

**Break Magic Immunity (Su)**

**At 11th Level:** A construct is instead treated as if it has
[spell resistance](ref/rule/spell-resistance) equal to 11 + the construct's CR.

**At 5th Level:** An arcane tinkerer can overcome a construct's immunity to magic. When targeting a
construct with a spell, the construct is instead treated as if it has
[spell resistance](ref/rule/spell-resistance) equal to 15 + the construct's CR.

**Replaces:** The arcanist exploits gained at 5th and 11th level
