+++
id = "ref/misc/spell-resistance"
kind = "rule"
title = "Spell Resistance (SR)"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_resistance", path = "json/misc.json" },
]
[[sources]]
publication = "core-rulebook"
page = "13"

[fields]
kind = "none"
+++

Some [creatures](ref/misc/creature) are resistant to magic and gain
[spell resistance](ref/rule/spell-resistance). When a creature with spell resistance is targeted by
a spell, the caster of the spell must make a caster level check to see if the spell affects the
target. The DC of this check is equal to the target creature's SR (some spells do not allow SR
checks).
