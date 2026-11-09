+++
id = "ref/arc-fighter/scrapper"
kind = "archetype"
title = "Scrapper"
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
replaces = ["Armor training", "Weapon training 1"]
+++

Scrappers are adept at collecting the leftovers from their enemy's armor and using these scraps to
improve their own armor.

**Scrap Armor (Ex)**

**Ability:** Salvaging scrap from a destroyed construct or from another creature's armor takes 1
minute. Scrap from a construct grants the scrapper a natural armor bonus to AC equal to one-quarter
the construct's Hit Dice (minimum +1). If the scrap is salvaged from a piece of armor, it instead
grants a natural armor bonus to AC equal to 1 + the armor's enhancement bonus (if any). The salvaged
armor piece is flimsy and prone to breaking. Scrap is immediately destroyed by any
[sunder](ref/rule/sunder) combat maneuver that targets the armor to which the scrap is attached.
Otherwise, scrap crumbles and falls away after a number of days equal to the natural armor bonus
that it grants.

**Flavor:** A scrapper learns to salvage scrap from constructs or other pieces of armor and attach
them to his own armor.

**At 11th Level:** Scrap salvaged from a construct also grants DR/adamantine equal to one-quarter of
the construct's Hit Dice.

**Gained:** At 3rd Level

**Replaces:** Armor training

**Scrapper Training (Ex)**

**Ability:** A scrapper selects one fighter [weapon group](ref/ability/weapon-groups). He gains a +1
bonus on attack and damage rolls when performing a sunder combat maneuver with a weapon from the
chosen group. He does not provoke attacks of opportunity when performing a sunder combat maneuver
with a weapon from the chosen group. If the scrapper has the
[Improved Sunder](ref/feat/improved-sunder) feat, the bonuses on attack and damage rolls from this
ability double.

**Gained:** At 5th Level

**Repeat:** A scrapper can either take the fighter's _weapon training_ class feature or improve his
bonuses from the _scrapper training_ class feature by 1., 13, 4

**Replaces:** Weapon training 1
