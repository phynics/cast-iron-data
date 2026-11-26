+++
id = "ref/arc-psychic/magaambyan-telepath"
kind = "archetype"
title = "Magaambyan Telepath"
aon = "ArchetypeDisplay.aspx?FixedName=Psychic%20Magaambyan%20Telepath"
source_ids = ["wilderness-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magaambyan_telepath", path = "json/archetypes_psychic.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/psychic" },
]
[[sources]]
publication = "wilderness-origins"
page = "27"

[fields]
kind = "archetype"
features = [
  { anchor = "primal-spells", level = 1 },
  { anchor = "nature-s-command", level = 1 },
  { anchor = "know-the-land", level = 9 },
  { anchor = "wild-mind", level = 17 },
]
trades = [
  { replaces = "Discipline spells", feature = "psychic-discipline", power = "discipline spell", by = ["primal-spells"] },
  { replaces = "The phrenic amplifications gained at 1st and 11th levels", feature = "phrenic-amplifications", levels = [1, 11], by = ["nature-s-command"] },
  { replaces = "Telepathic bond", feature = "telepathic-bond", by = ["know-the-land"] },
  { alters = "Telepathy", feature = "telepathy", by = ["wild-mind"] },
]
+++

While most students of the [Magaambya](ref/rule/aff-i-school) in the Mwangi Expanse focus on the
blending of arcane and divine magic, followers of Old-Mage Jatembe's more esoteric wisdom instead
focus on the occult connection between all living creatures and the resonance between the natural
and supernatural world. These Magaambyan telepaths hone their mental abilities to detect such
spiritual and eldritch bonds, and attempt to commune with the mind of the jungle or the hearts of
its wild inhabitants. Whether seeking information that only nature knows or attempting to impose
their will upon the natural world, these psychics employ techniques that few outside of the
Magaambya understand.

## Primal Spells {#primal-spells}

A Magaambyan telepath adds one 1st-level spell from the druid spell list to the psychic spell list
and her spells known. Each time a Magaambyan telepath gains the ability to cast a new level of
spell, she can add one spell of that level from the druid spell list to both the psychic spell list
and her spells known. She casts these spells as psychic spells, and once the spells are selected
these choices cannot be changed.

This replaces discipline spells.

## Nature's Command (Ex) {#nature-s-command}

The Magaambyan telepath's mind-affecting spells can affect even plant creatures. When she casts a
mind-affecting spell, the Magaambyan telepath can spend 2 points from her phrenic pool to overcome a
plant creature's immunity to mind-affecting effects for the purposes of that spell. This ability
functions even on mindless plant creatures, but it has no effect on creatures that aren't plants.

At 11th level, when the Magaambyan telepath casts a mind-affecting or language-dependent spell, the
psychic can spend 2 points from her phrenic pool to cause the spell to affect creatures of the plant
and animal types as if they were humanoids that understood her language.

This replaces the phrenic amplifications gained at 1st and 11th levels.

## Know the Land (Sp) {#know-the-land}

At 9th level, the Magaambyan telepath can cast
_[commune with nature](ref/spell/commune-with-nature)_ as a
[spell-like ability](ref/umr/spell-like-abilities) once per day, using her psychic level as her
caster level. She can also expend any unused spell slot of 5th level or higher to cast
_[commune with nature](ref/spell/commune-with-nature)_.

This replaces _telepathic bond_.

## Wild Mind (Su) {#wild-mind}

At 17th level, when the Magaambyan telepath gains the [telepathy](ref/spell/telepathy) ability, she
can also mentally communicate with any animal or plant creature as if it had a language.

This alters telepathy.
