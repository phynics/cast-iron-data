+++
id = "ref/arc-gunslinger/wyrm-sniper"
kind = "archetype"
title = "Wyrm Sniper"
aon = "ArchetypeDisplay.aspx?FixedName=Gunslinger%20Wyrm%20Sniper"
source_ids = ["dragonslayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wyrm_sniper", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]
[[sources]]
publication = "dragonslayers-handbook"
page = "23"

[fields]
kind = "archetype"
features = [
  { anchor = "artillery-proficiency" },
  { anchor = "munitions-master", level = 7 },
  { anchor = "skeleton-crew", level = 11 },
  { anchor = "anti-air-targeting", level = 15 },
  { anchor = "siege-commander", level = 4 },
  { anchor = "heavy-gunner", level = 5 },
  { anchor = "master-siege-engineer", level = 12 },
]
trades = [
  { replaces = "Startling shot deed", feature = "deeds", power = "startling shot", by = ["munitions-master"] },
  { replaces = "Lightning reload deed", feature = "deeds", power = "lightning reload", by = ["skeleton-crew"] },
  { replaces = "Menacing shot deed", feature = "deeds", power = "menacing shot", by = ["anti-air-targeting"] },
  { alters = "Gun training", feature = "gun-training", by = ["heavy-gunner"] },
]
+++

These long-shot artists are masters at taking down dragons with sharp shooting and light siege
weaponry. The following are class features for wyrm snipers.

## Class Skills {#class-skills}

A wyrm sniper adds Knowledge (arcana) to her list of class skills, in addition to the normal
gunslinger class skills.

## Artillery Proficiency {#artillery-proficiency}

Wyrm snipers are proficient with light [siege engines](ref/rule/siege-engines), in addition to the
normal gunslinger weapon proficiencies. See page 26 of this book for new anti-dragon siege weaponry.

## Deeds {#deeds}

A wyrm sniper swaps a trio of deeds for the following deeds.

## Munitions Master {#munitions-master}

At 7th level, a wyrm sniper can spend 1 grit point to reduce the number of full-round actions (or
move actions, if the sniper has the Master Siege Engineer feat) required to load a light siege
engine by 1. This deed replaces the gunslinger's startling shot deed.

## Skeleton Crew {#skeleton-crew}

At 11th level, as long as a wyrm sniper has at least 1 grit point, she treats all light siege
engines as requiring a crew of one fewer than normal to operate (minimum 1). This deed replaces the
gunslinger's lightning reload deed.

## Anti-Air Targeting {#anti-air-targeting}

At 15th level, whenever a wyrm sniper targets a creature's wings with the targeting deed, the wyrm
sniper completely disables one of the creature's wings on a successful hit. If the wyrm sniper hits
her target, the creature falls to the ground, regardless of its altitude, taking the appropriate
amount of falling damage as a result. As long as the target has at least one functioning wing, it
may attempt a DC 20 Fly check to gain the benefits of _[feather fall](ref/spell/feather-fall)_
instead of plummeting to the ground. In either case, it must succeed at a Reflex save (DC 10 + 1/2
the wyrm sniper's level + the wyrm sniper's Wisdom modifier) or fall [prone](ref/rule/prone) when
reaching the ground. This ability replaces the gunslinger's menacing shot deed.

## Siege Commander (Ex) {#siege-commander}

At 4th level, a wyrm sniper may select the [Siege Commander](ref/feat/siege-commander) combat feat
as her bonus feat, even if she does not meet the prerequisites.

## Heavy Gunner (Ex) {#heavy-gunner}

Starting at 5th level, a wyrm sniper may select one specific type of light siege weapon (such as a
[ballista](ref/eq-siegeengine/ballista-light) or [light bombard](ref/eq-siegeengine/bombard-light))
in place of a specific type of firearm as part of her gun training class ability. Every 4 levels
thereafter (9th, 13th, and 17th), when she can pick a new type of firearm for the gun training class
ability, the gunslinger may again select another type of light siege engine.

## Master Siege Engineer (Ex) {#master-siege-engineer}

At 12th level, a wyrm sniper may select the [Master Siege Engineer](ref/feat/master-siege-engineer)
combat feat as her bonus feat, even if she does not meet the feat's prerequisites.
