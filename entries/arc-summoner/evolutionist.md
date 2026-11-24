+++
id = "ref/arc-summoner/evolutionist"
kind = "archetype"
title = "Evolutionist"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20Evolutionist"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "evolutionist", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]
[[sources]]
publication = "ultimate-magic"
page = "79"

[fields]
kind = "archetype"
features = [
  { anchor = "mutate-eidolon", level = 6 },
  { anchor = "evolve-base-form", level = 8 },
  { anchor = "transmogrify", level = 12 },
]
trades = [
  { replaces = "Maker's call", feature = "maker-s-call", by = ["mutate-eidolon"] },
  { replaces = "Transposition", feature = "transposition", by = ["evolve-base-form"] },
  { replaces = "Greater shield ally", feature = "greater-shield-ally", by = ["transmogrify"] },
]
+++

Changing an eidolon's evolutions is normally a slow process. As a summoner progresses in levels, his
control over his eidolon's abilities increases. But an evolutionist possesses greater power over his
eidolon's form, and is able to evolve his eidolon and its abilities to meet any challenge or face
any threat as it comes up, seemingly on a whim.

## Mutate Eidolon (Su) {#mutate-eidolon}

At 6th level, an evolutionist can change his eidolon's evolutions as if he had gained a level. To
mutate his eidolon, the evolutionist must perform an arcane ritual that requires 24 hours of
uninterrupted concentration and costs 200 gp per summoner level in material components. This ability
replaces maker's call.

## Evolve Base Form (Su) {#evolve-base-form}

Starting at 8th level, whenever he gains a level, the evolutionist can change his eidolon's base
form to a new base form. Once chosen, this base form is set until the evolutionist gains another
summoner level. This ability replaces transposition.

## Transmogrify (Sp) {#transmogrify}

At 12th level, the evolutionist can cast _[transmogrify](ref/spell/transmogrify)_ as a
[spell-like ability](ref/umr/spell-like-abilities) once per day without the need for a material
component. This ability has a casting time of 1 minute. This ability replaces greater shield ally.
