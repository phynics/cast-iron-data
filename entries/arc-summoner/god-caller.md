+++
id = "ref/arc-summoner/god-caller"
kind = "archetype"
title = "God Caller"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20God%20Caller"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "god_caller", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "40"

[fields]
kind = "archetype"
replaces = ["Transposition", "Aspect", "Greater aspect", "Twin eidolon"]
alters = ["Life link"]
replaces_features = ["transposition", "aspect", "greater-aspect", "twin-eidolon"]
alters_features = ["life-link"]
+++

God callers follow a fractured tradition that originated in the now-lost nation of Sarkoris. They
speak to an assortment of ancient divine powers to lead their communities and sometimes stir up
reformations in faiths with ideals similar to their personal convictions.

**Gained class skills:** diplo, intm

**Lost class skills:** kd, ke, kg, kna, umd

**Guidance (Sp)**

**Ability:** The eidolon can use [guidance](ref/spell/guidance) as a
[spell-like ability](ref/umr/spell-like-abilities) at will. However, the eidolon and the god caller
must remain within 50 feet of one another for the eidolon to remain at full strength. If the eidolon
is beyond 50 feet but closer than 1,000 feet, its current and maximum hit point totals are reduced
by half.

**Alters:** Life link

**Flavor:** A god caller's eidolon has a tiny spark of divinity.

**Divine Word (Ex)**

**Ability:** Once per day while his eidolon uses the aid another action to assist him in such a
check, if the god caller would improve a target's attitude toward him, or gain a success if using
the individual [influence rules](ref/rule/influence), he instead improves that target's attitude by
2 steps or it counts as 2 successes.

**Gained:** At 8th Level

**Passive:** If a god caller's eidolon would grant him a bonus with the
[aid another](ref/rule/aid-another) action on a Diplomacy or Intimidate check, the god caller can
instead choose to roll twice and take the better result. He makes the choice before rolling.

**Replaces:** Transposition

**Divine Awareness (Sp)**

**Ability:** After 10 minutes of concentration, a god caller's eidolon can see from afar as per
[clairaudience/clairvoyance](ref/spell/clairaudience-clairvoyance).

**Gained:** At 10th Level

**Replaces:** Aspect

**Usage:** 1 time/day + 1 per 4 summoner levels beyond 10th

**Divine Might (Ex)**

**Gained:** At 18th Level

**Passive:** A god caller's eidolon's attacks are treated as epic for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction) and harming mythic creatures.

**Replaces:** Greater aspect

**Overwhelming Presence (Sp)**

**Ability:** A god caller's eidolon can use [overwhelming presence](ref/spell/overwhelming-presence)
three times per day. The save DC is equal to 19 + the eidolon's Charisma modifier.

**Gained:** At 20th Level

**Replaces:** Twin eidolon
