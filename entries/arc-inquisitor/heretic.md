+++
id = "ref/arc-inquisitor/heretic"
kind = "archetype"
title = "Heretic"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Heretic"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "heretic", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "ultimate-magic"
page = "45"

[fields]
kind = "archetype"
features = [
  { anchor = "judgment" },
  { anchor = "escape" },
  { anchor = "lore-of-escape", level = 1 },
  { anchor = "hide-tracks", level = 1 },
  { anchor = "ex-inquisitors" },
]
trades = [
  { replaces = "Monster lore", feature = "monster-lore", by = ["lore-of-escape"] },
]
+++

While all inquisitors hunt the enemies of the faith, sometimes, either through political maneuvering
by her enemies or an unyielding tenacity that breaks her faith's basic tenets, an inquisitor can
find herself a heretic. Still unyielding in her cause, these heretics are accustomed to using guile
and deception to hide themselves and their activities while they continue to hunt their enemies.

## Judgment (Su) {#judgment}

A heretic gains the following judgment in addition to the normal list of inquisitor judgments.

## Escape (Su) {#escape}

Each time the inquisitor using this judgment hits an opponent with a melee or ranged attack, she can
use a move action attempt to create a diversion to hide.

## Lore of Escape (Ex) {#lore-of-escape}

At 1st level, the heretic uses every trick she knows to escape those now pursuing her. She adds her
Wisdom modifier on Bluff and Stealth skill checks in addition to the normal ability score modifiers.
This ability replaces monster lore.

## Hide Tracks (Ex) {#hide-tracks}

At 1st level, a heretical inquisitor is adept at hiding her tracks. Creatures attempting to track
her take a -5 penalty on rolls to find or follow her tracks.

## Ex-Inquisitors {#ex-inquisitors}

An inquisitor who becomes an ex-inquisitor can, with the GM's permission, take the heretic
archetype, replacing her class abilities with the appropriate archetype abilities. If the character
atones or joins a different faith, she loses her heretic abilities and regains her previous
inquisitor class abilities.
