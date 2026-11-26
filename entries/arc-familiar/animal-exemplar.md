+++
id = "ref/arc-familiar/animal-exemplar"
kind = "archetype"
title = "Animal Exemplar"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "animal_exemplar", path = "json/archetypes_FAMILIAR.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "210"

[fields]
kind = "archetype"
features = [
  { anchor = "influence-animals", level = 3 },
]
trades = [
  { replaces = "Deliver touch spells", by = ["influence-animals"] },
  { replaces = "spell resistance", by = ["influence-animals"] },
  { replaces = "scry on familiar", by = ["influence-animals"] },
  { alters = "Speak with animals of its kind", by = ["influence-animals"] },
]
+++

An animal exemplar is a paragon of its species, able to command the loyalty of others of its kind.

## Special Requirement {#special-requirement}

An animal exemplar familiar cannot be an improved familiar, plant, vermin, or other nonanimal themed
familiar.

## Animal Exemplar Skills {#animal-exemplar-skills}

An animal exemplar treats Handle Animal as a class skill.

## Influence Animals (Ex, Sp) {#influence-animals}

An animal exemplar gains _speak with animals_ with respect to others of its kind at 3rd level
instead of 7th level. At 7th level, it gains the ability to influence animals of its kind, as per
the [wild empathy](ref/ability/wild-empathy) ability of a [druid](ref/class/druid) of its master's
level with a +4 racial bonus on the check, but only for animals of its kind. At 11th level, it can
cast _[charm animal](ref/spell/charm-animal)_ three times per day as a
[spell-like ability](ref/umr/spell-like-abilities) against animals of its kind, and at 13th level,
it can cast _[dominate animal](ref/spell/dominate-animal)_ once per day as a
[spell-like ability](ref/umr/spell-like-abilities) against animals of its kind.

This alters speak with animals of its kind and replaces deliver touch spells,
[spell resistance](ref/rule/spell-resistance), and scry on familiar.
