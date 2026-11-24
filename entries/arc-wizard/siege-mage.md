+++
id = "ref/arc-wizard/siege-mage"
kind = "archetype"
title = "Siege Mage"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Siege%20Mage"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "siege_mage", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "ultimate-combat"
page = "75"

[fields]
kind = "archetype"
features = [
  { anchor = "siege-engineer", level = 1 },
  { anchor = "siege-engine-bond", level = 1 },
  { anchor = "empower-siege-engine", level = 1 },
  { anchor = "siege-school", level = 1 },
]
trades = [
  { replaces = "Scribe scroll", feature = "scribe-scroll", by = ["siege-engineer"] },
  { replaces = "Arcane bond", feature = "arcane-bond", by = ["siege-engine-bond"] },
  { replaces = "Cantrips", feature = "cantrips", by = ["empower-siege-engine"] },
  { replaces = "Arcane school", feature = "arcane-school", by = ["siege-school"] },
]
+++

The siege mage combines his arcane mastery with a supernatural link to
[siege engines](ref/rule/siege-engines).

## Siege Engineer {#siege-engineer}

At 1st level, the siege mage gains [Siege Engineer](ref/feat/siege-engineer) (see page 118) as a
bonus feat, even though he does not meet the prerequisites for that feat. This ability replaces
scribe scroll.

## Siege Engine Bond (Su) {#siege-engine-bond}

At 1st level, a siege mage can bond with a single siege engine within 30 feet and line of sight as a
standard action. He can utilize the power of this link to aim and fire the siege engine remotely (as
long as he's within 30 feet), though it still requires a crew to reload the siege engine. At 10th
level, he can reload, aim, and fire the siege engine purely by the power of this link, and no longer
needs a crew to control the siege engine. It still takes the normal required amount of time and
actions to control a siege engine in this manner. This ability replaces arcane bond. The siege mage
can end this bond with a free action. A siege mage can bond with a siege engine in this manner a
number of times per day equal to his Intelligence modifier (minimum 1) but can only be bonded with
one siege engine at a time.

## Empower Siege Engine (Su) {#empower-siege-engine}

As a swift action, a siege mage can sacrifice one of his spells to empower the next attack he makes
before the end of his turn with a siege engine he is bonded with. When he does, the siege engine
attack gains a bonus on its attack roll or targeting roll equal to the level of the spell he
sacrificed, and a bonus to damage equal to 3 × the level of the spell. This ability replaces
cantrips, but the siege mage gains the _[detect magic](ref/spell/detect-magic)_ and
_[read magic](ref/spell/read-magic)_ cantrips and places them in his spellbook. He can cast either
of these as 1st-level spells.

## Siege School {#siege-school}

The strange rituals needed to empower all forms of siege engines takes a level of dedication and
perseverance that limits a wizard's time to unlock other arcane mysteries. At 1st level, the siege
mage forsakes three schools of magic. Once chosen, these opposition schools cannot be changed. A
siege mage who prepares spells from his opposition school must use two spell slots of that level to
prepare the spell. In addition, the siege mage takes a -4 penalty on any skill checks made when
crafting a magic item that has a spell from one of his opposition schools. This ability replaces
arcane school.
