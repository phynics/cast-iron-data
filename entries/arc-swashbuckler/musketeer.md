+++
id = "ref/arc-swashbuckler/musketeer"
kind = "archetype"
title = "Musketeer"
aon = "ArchetypeDisplay.aspx?FixedName=Swashbuckler%20Musketeer"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "musketeer", path = "json/archetypes_swashbuckler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/swashbuckler" },
]
[[sources]]
publication = "advanced-class-guide"
page = "126"

[fields]
kind = "archetype"
features = [
  { anchor = "musketeer-instruction", level = 1 },
  { anchor = "quick-clear", level = 1 },
]
trades = [
  { replaces = "Weapon proficiencies", feature = "weapon-and-armor-proficiencies", power = "weapons" },
  { replaces = "Swashbuckler finesse", feature = "swashbuckler-finesse", by = ["musketeer-instruction"] },
  { replaces = "Dodging panache", feature = "deeds", power = "dodging panache", by = ["quick-clear"] },
]
+++

A number of organizations and kingdoms search for warriors who are brave (or foolish) enough to
wield firearms on the battlefield. The daring nature of swashbucklers often makes them ideal
candidates for such service.

## Weapon Proficiency {#weapon-proficiency}

A musketeer gains proficiency with all simple weapons and martial weapons, as well as one-handed and
two-handed firearms. This ability replaces the swashbuckler's weapon proficiencies.

## Musketeer Instruction (Ex) {#musketeer-instruction}

At 1st level, a musketeer gains the benefits of the [Weapon Finesse](ref/feat/weapon-finesse)
feature with the [rapier](ref/eq-weapon/rapier) (this counts as having the Weapon Finesse feat for
purposes of meeting feat prerequisites), as well as both [Rapid Reload](ref/feat/rapid-reload)
(musket) and [Gunsmithing](ref/feat/gunsmithing) feats as bonus feats. This ability replaces
swashbuckler finesse.

## Deed {#deed}

The musketeer gains the following deed, which replaces an existing deed.

## Quick Clear (Ex) {#quick-clear}

At 1st level, as a standard action the musketeer can spend 1 panache point to remove the
[broken](ref/misc/broken) condition from a single firearm he is currently wielding, as long as the
firearm gained that condition through a misfire. This deed replaces dodging panache.
