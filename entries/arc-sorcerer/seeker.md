+++
id = "ref/arc-sorcerer/seeker"
kind = "archetype"
title = "Seeker"
aon = "ArchetypeDisplay.aspx?FixedName=Sorcerer%20Seeker"
source_ids = ["pathfinder-society-field-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "seeker", path = "json/archetypes_sorcerer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/sorcerer" },
]
[[sources]]
publication = "pathfinder-society-field-guide"
page = "29"

[fields]
kind = "archetype"
replaces = ["Eschew Materials", "3rd-level bloodline power", "15th-level bloodline power"]
+++

Oracles and sorcerers gain their magical powers through strange and mysterious ways, be they chosen
by fate or blood. While most might be content with their strange powers, some oracles and sorcerers
join the [Pathfinders](ref/rule/aff-scholars) specifically to find out more about their mysteries
and bloodlines and determine the genesis and history of their eldritch talents. These spellcasters
are known among the Spells as seekers, after their obsession with researching ancient texts and
obscure ruins for any clues they can find about their heritage and histories. A seeker has the
following class features.

**Gained class skills:** dd

**Tinkering (Ex)**

**Ability:** A seeker can use Disable Device to disarm magical traps.

**Passive:** A seeker adds [half](ref/misc/fractions-and-rounding) his sorcerer level on Perception
checks made to locate traps and on all Disable Device skill checks (minimum +1).

**Replaces:** Eschew Materials

**Special:** If the seeker also possesses levels in [rogue](ref/class/rogue) or another class that
provides the [trapfinding](ref/ability/trapfinding) ability, those levels stack with his sorcerer
levels for determining his overall bonus on these skill checks.

**Seeker Lore (Ex)**

**Flavor:** A seeker has already learned much about his bloodline, and is more comfortable using the
bonus spells gained by that bloodline.

**Gained:** At 3rd Level

**Passive:** He gains a +4 bonus on all [concentration](ref/rule/concentration) checks, on caster
level checks made to overcome [spell resistance](ref/rule/spell-resistance), and on all Knowledge
(arcana) and Spellcraft checks made on topics associated with his bonus spells.

**Replaces:** 3rd-level bloodline power

**Seeker Magic (Su)**

**Ability:** When a seeker applies a metamagic feat to any bonus spells granted by his bloodline, he
reduces the metamagic feat's spell level adjustment by 1. Thus, applying a Metamagic feat like
[Still Spell](ref/feat/still-spell) to a spell does not change its effective spell level at all,
while applying [Quicken Spell](ref/feat/quicken-spell) only increases the spell's effective spell
level by 3 instead of by 4.

**Flavor:** A seeker becomes skilled at modifying his bloodline spells with metamagic.

**Gained:** At 15th Level

**Replaces:** 15th-level bloodline power

**Special:** This reduction to the spell level adjustment for Metamagic feats does not stack with
similar reductions from other abilities.
