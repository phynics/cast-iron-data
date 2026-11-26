+++
id = "ref/arc-fighter/scrapper"
kind = "archetype"
title = "Scrapper"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Scrapper"
source_ids = ["construct-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scrapper", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "construct-handbook"
page = "14"

[fields]
kind = "archetype"
features = [
  { anchor = "scrap-armor", level = 3 },
  { anchor = "scrapper-training", level = 5 },
]
trades = [
  { replaces = "Armor training", feature = "armor-training", by = ["scrap-armor"] },
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["scrapper-training"] },
]
+++

Scrappers are adept at collecting the leftovers from their enemy's armor and using these scraps to
improve their own armor.

## Scrap Armor (Ex) {#scrap-armor}

At 3rd level, a scrapper learns to salvage scrap from constructs or other pieces of armor and attach
them to his own armor. Salvaging scrap from a destroyed construct or from another creature's armor
takes 1 minute. Scrap from a construct grants the scrapper a natural armor bonus to AC equal to
one-quarter the construct's Hit Dice (minimum +1). If the scrap is salvaged from a piece of armor,
it instead grants a natural armor bonus to AC equal to 1 + the armor's enhancement bonus (if any).
The salvaged armor piece is flimsy and prone to breaking. Scrap is immediately destroyed by any
[sunder](ref/rule/sunder) combat maneuver that targets the armor to which the scrap is attached.
Otherwise, scrap crumbles and falls away after a number of days equal to the natural armor bonus
that it grants. At 11th level, scrap salvaged from a construct also grants DR/adamantine equal to
one-quarter of the construct's Hit Dice.

This replaces armor training.

## Scrapper Training (Ex) {#scrapper-training}

At 5th level, a scrapper selects one fighter [weapon group](ref/ability/weapon-groups). He gains a
+1 bonus on attack and damage rolls when performing a sunder combat maneuver with a weapon from the
chosen group. He does not provoke attacks of opportunity when performing a sunder combat maneuver
with a weapon from the chosen group. If the scrapper has the
[Improved Sunder](ref/feat/improved-sunder) feat, the bonuses on attack and damage rolls from this
ability double. At 9th level and every 4 levels thereafter, a scrapper can either take the fighter's
weapon training class feature or improve his bonuses from the scrapper training class feature by 1.

This replaces weapon training 1.
