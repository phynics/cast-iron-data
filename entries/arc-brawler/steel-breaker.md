+++
id = "ref/arc-brawler/steel-breaker"
kind = "archetype"
title = "Steel-Breaker"
aon = "ArchetypeDisplay.aspx?FixedName=Brawler%20Steel-Breaker"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "steel_breaker", path = "json/archetypes_brawler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/brawler" },
]
[[sources]]
publication = "advanced-class-guide"
page = "88"

[fields]
kind = "archetype"
replaces = ["Brawler's strike"]
alters = ["Maneuver training"]
replaces_features = ["brawler-s-strike"]
alters_features = ["maneuver-training"]
+++

The steel-breaker studies destruction and practices it as an art form. She knows every defense has a
breaking point, and can shatter those defenses with carefully planned strikes.

**Gained class skills:** ke

**Lost class skills:** kd

**Exploit Weakness (Ex)**

**Ability:** As a **swift action**, a steel-breaker can observe a creature or object to find its
weak point by succeeding at a Wisdom check, adding her brawler level against a DC of 10 the object's
[hardness](ref/umr/hardness) or the target's CR. If it succeeds, the steel-breaker gains a +2 bonus
on attack rolls until the end of her turn, and any attacks she makes until the end of her turn
ignore the creature or object's DR or hardness.

**Info:** A steel-breaker can instead use this ability as a **swift action** to analyze the
movements and expressions of one creature within 30 feet, granting a bonus on Sense Motive checks
and Reflex saving throws, as well as a dodge bonus to AC against that opponent equal to
[half](ref/misc/fractions-and-rounding) her brawler level until the start of her next turn.

**Gained:** At 5th Level

**Replaces:** Brawler's strike

**Sunder Training (Ex)**

**Alters:** Maneuver training

**Flavor:** A steel-breaker receives additional training in sunder combat maneuvers.

**At 11th Level:** The sunder bonuses become +4 and the disarm bonuses become +3.

**At 15th Level:** These bonuses become +5 and +4, respectively.

**At 19th Level:** These bonuses become +6 and +5.

**At 3rd Level:** She gains a +2 bonus when attempting a [sunder](ref/rule/sunder) combat maneuver
checks and a +2 bonus to her CMD when defending against this maneuver.

**At 7th Level:** These bonuses increase to +3, and she gains a +2 bonus on
[disarm](ref/rule/disarm) combat maneuver checks and a +2 bonus to her CMD when defending against a
disarm maneuver.
