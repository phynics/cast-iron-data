+++
id = "ref/arc-rogue/swamp-poisoner"
kind = "archetype"
title = "Swamp Poisoner"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Swamp%20Poisoner"
source_ids = ["potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "swamp_poisoner", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "potions-and-poisons"
page = "4"

[fields]
kind = "archetype"
replaces = ["Trapfinding", "Rogue talent gained at 2nd level", "Trap sense (core rogue)", "danger sense (unchained rogue)"]
+++

Swamp poisoners use their own toxins to defend their homes and level the playing field. The swamp
poisoner is an archetype available to grippli characters, and it is appropriate for rogues built
using the rules from the Pathfinder RPG Core Rulebook as well as for unchained rogues.

**Prerequisites:** Grippli; _Toxic skin_ alternate racial trait

**Mucous Membrane (Ex)**

**Passive:** A swamp poisoner gains a bonus equal to half his class level on Escape Artist checks
and to his CMD when resisting grapple attempts (minimum 1).

**Replaces:** Trapfinding

**Mark the Vein (Ex)**

**Ability:** When the swamp poisoner attacks a target that is currently affected by his grippli
racial poison, that target is denied its Dexterity bonus to AC. The target must be actively
poisoned, not just suffering the effects of poison, such as lingering ability damage.

**Gained:** At 2nd Level

**Replaces:** Rogue talent gained at 2nd level

**Poison the Well (Ex)**

**Ability:** The swamp poisoner also gains extra uses per day of his toxic skin alternate racial
trait equal to [one-third](ref/misc/fractions-and-rounding) of his rogue level.

**Gained:** At 3rd Level

**Replaces:** Trap sense (core rogue), danger sense (unchained rogue)

**Standard:** A swamp poisoner can smear the poison generated through the use of his toxic skin
alternate racial trait onto the ground in a 5-foot area, instead of onto a weapon or his own body.
The first creature other than the swamp poisoner to enter the area is exposed to the poison. The
poison loses its potency after 1 hour. This area is considered a [trap](ref/rule/traps), and the DCs
of Perception checks to notice it and Disable Device checks to disable it are equal to 10 + half the
swamp poisoner's level + the swamp poisoner's Constitution modifier.
