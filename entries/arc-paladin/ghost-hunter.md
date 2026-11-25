+++
id = "ref/arc-paladin/ghost-hunter"
kind = "archetype"
title = "Ghost Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Ghost%20Hunter"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ghost_hunter", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "occult-adventures"
page = "123"

[fields]
kind = "archetype"
features = [
  { anchor = "ghostly-smite" },
  { anchor = "exorcise-possession", level = 6 },
  { anchor = "speak-to-the-restless", level = 9 },
]
trades = [
  { replaces = "6th-level mercy", feature = "mercy", levels = [6], by = ["exorcise-possession"] },
  { replaces = "9th-level mercy", feature = "mercy", levels = [9], by = ["speak-to-the-restless"] },
  { alters = "Smite evil", feature = "smite-evil", by = ["ghostly-smite"] },
]
+++

Ghost hunters devote their lives to eliminating malevolent spirits and putting them to rest.

## Ghostly Smite (Su) {#ghostly-smite}

A ghost hunter's smite evil ability does not automatically bypass DR (other than DR/good). However,
she treats her weapon as a _[ghost touch](ref/magic-enh/ghost-touch-weapon)_ weapon against the
target of her smite. She does not deal extra damage on the first attack against evil outsiders and
evil dragons, but she deals 3 points of damage per paladin level she possesses to undead creatures
on the first attack (instead of 2 points). This ability alters smite evil.

## Exorcise Possession (Su) {#exorcise-possession}

At 6th level, a ghost hunter can try to end any possession spells or effects, or effects that
directly exercise mental control over a creature. She must touch the affected creature (this
requires a melee touch attack if the target is neither willing nor helpless) and expend a use of her
lay on hands ability. The target can immediately attempt a Will save against the original save DC of
the controlling effect. If the save is successful, the effect immediately ends, as if the target had
succeeded at its original saving throw. This ability replaces the 6th-level mercy.

## Speak to the Restless (Sp) {#speak-to-the-restless}

At 9th level, a ghost hunter can commune with the spirits of the restless dead once per day. By
holding a seance for 10 minutes, she can ask questions of a destroyed undead or a neutralized or
destroyed [haunt](ref/rule/haunts). To use this ability on a corporeal undead, the ghost hunter must
have the creature's head in her possession. For a haunt or incorporeal undead, this seance must be
held in the haunt's location or where the incorporeal undead was destroyed. Treat this ability as
_[speak with haunt](ref/spell/speak-with-haunt)_ or as
_[speak with dead](ref/spell/speak-with-dead)_ (but affecting only undead rather than only corpses),
using the ghost hunter's class level as the caster level. This ability replaces the 9th-level mercy.
