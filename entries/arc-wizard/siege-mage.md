+++
id = "ref/arc-wizard/siege-mage"
kind = "archetype"
title = "Siege Mage"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "siege_mage", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]

[fields]
kind = "archetype"
replaces = ["Scribe scroll", "Arcane bond", "Cantrips", "Arcane school"]
+++

**Sources:** Ultimate Combat pg 75\
The siege mage combines his arcane mastery with a supernatural link to
[siege engines](ref/rule/siege-engines).

**Siege Engineer**

**Ability:** The siege mage gains [Siege Engineer](ref/feat/siege-engineer) as a bonus feat, even
though he does not meet the prerequisites for that feat.

**Gained:** At 1st Level

**Replaces:** Scribe scroll

**Siege Engine Bond (Su)**

**At 10th Level:** He can reload, aim, and fire the siege engine purely by the power of this link,
and no longer needs a crew to control the siege engine. It still takes the normal required amount of
time and actions to control a siege engine in this manner.

**Gained:** At 1st Level

**Replaces:** Arcane bond

**Special:** The siege mage can end this bond with a **free action**. A siege mage can only be
bonded with one siege engine at a time.

**Standard:** A siege mage can bond with a single siege engine within 30 feet and line of sight. He
can utilize the power of this link to aim and fire the siege engine remotely (as long as he's within
30 feet), though it still requires a crew to reload the siege engine.

**Usage:** Intelligence modifier times/day (minimum 1)

**Empower Siege Engine (Su)**

**Ability:** The siege mage gains the [detect magic](ref/spell/detect-magic) and
[read magic](ref/spell/read-magic) cantrips and places them in his spellbook. He can cast either of
these as 1st-level spells.

**Replaces:** Cantrips

**Swift:** A siege mage can sacrifice one of his spells to empower the next attack he makes before
the end of his turn with a siege engine he is bonded with. When he does, the siege engine attack
gains a bonus on its attack roll or targeting roll equal to the level of the spell he sacrificed,
and a bonus to damage equal to 3 &times& the level of the spell.

**Siege School**

**Flavor:** The strange rituals needed to empower all forms of siege engines takes a level of
dedication and perseverance that limits a wizard's time to unlock other arcane mysteries.

**At 1st Level:** The siege mage forsakes three schools of magic. Once chosen, these opposition
schools cannot be changed. A siege mage who prepares spells from his opposition school must use two
spell slots of that level to prepare the spell. In addition, the siege mage takes a -4 penalty on
any skill checks made when crafting a magic item that has a spell from one of his opposition
schools.

**Replaces:** Arcane school
