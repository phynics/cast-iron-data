+++
id = "ref/arc-familiar/arcane-amplifier"
kind = "archetype"
title = "Arcane Amplifier"
source_ids = ["wilderness-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcane_amplifier", path = "json/archetypes_FAMILIAR.json" },
]
[[sources]]
publication = "wilderness-origins"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "echo" },
  { anchor = "reverberate", level = 7 },
  { anchor = "resonate", level = 13 },
]
trades = [
  { replaces = "Alertness", by = ["echo"] },
  { replaces = "improved evasion", by = ["echo"] },
  { replaces = "Speak with animals of its kind", by = ["reverberate"] },
  { replaces = "spell resistance", by = ["reverberate"] },
  { replaces = "Scry on familiar", by = ["resonate"] },
]
+++

The secret of the arcane amplifier familiar was first discovered in Irrisen, where the winter
witches used white-furred foxes or hares to strengthen their spells. More recently, the practice has
spread to Nex and Cheliax, and to haunted Ustalav where necromancers use black-eyed ravens for their
spells.

## Echo (Su) {#echo}

Once per day when delivering a touch spell, an arcane amplifier can apply the
[Extend Spell](ref/feat/extend-spell) metamagic feat to the spell. An arcane amplifier can use this
ability twice per day at 8th level, and three times per day at 13th level.

This replaces Alertness and improved evasion.

## Reverberate (Su) {#reverberate}

At 7th level, once per day when delivering a touch spell, an arcane amplifier can apply either the
[Empower Spell](ref/feat/empower-spell) metamagic feat to the spell or use the
[Heighten Spell](ref/feat/heighten-spell) metamagic feat to increase its spell level by 2. An arcane
amplifier can use this ability twice per day at 11th level.

This replaces speak with animals of its kind and [spell resistance](ref/rule/spell-resistance).

## Resonate (Su) {#resonate}

At 13th level, once per day when delivering a touch spell, an arcane amplifier can apply the
[Maximize Spell](ref/feat/maximize-spell) metamagic feat to the spell.

This replaces scry on familiar.

An arcane amplifier can apply only one metamagic effect to a single casting of a spell using its
echo, reverberate, or resonate abilities.
