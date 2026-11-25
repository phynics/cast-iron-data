+++
id = "ref/arc-familiar/ambassador"
kind = "archetype"
title = "Ambassador"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ambassador", path = "json/archetypes_FAMILIAR.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "210"

[fields]
kind = "archetype"
features = [
  { anchor = "persuasive" },
  { anchor = "enhanced-personality" },
]
trades = [
  { replaces = "Alertness", by = ["persuasive"] },
  { replaces = "The familiar's Intelligence score advancement", by = ["enhanced-personality"] },
]
+++

An ambassador speaks on its master's behalf and sometimes on behalf of its master's patron or other
extraplanar contacts.

## Special Requirement {#special-requirement}

An ambassador familiar must be able to speak at least one language, either as a special familiar
ability (as in the case of a raven or thrush) or by being an improved familiar. A familiar that
can't speak (or can speak only to its master or other animals) can't be an ambassador.

## Ambassador Skills {#ambassador-skills}

An ambassador treats Bluff, Diplomacy, and Intimidate as class skills.

## Persuasive (Ex) {#persuasive}

An ambassador gains [Persuasive](ref/feat/persuasive) as a bonus feat.

This replaces alertness.

## Enhanced Personality (Ex) {#enhanced-personality}

An ambassador gains a Charisma score equal to the typical Intelligence score of a familiar of its
level, if that would be higher than its normal Charisma score. The familiar's Intelligence score
remains 6 (or its normal starting Intelligence for an improved familiar) and doesn't increase by
level.

This replaces the familiar's Intelligence score advancement.
