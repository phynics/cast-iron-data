+++
id = "ref/spell/infernal-healing"
kind = "spell"
title = "Infernal Healing"
source_ids = ["hells-vengeance-players-guide", "pathfinder-29-mother-of-flies", "gods-and-magic", "inner-sea-world-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "infernal_healing", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 round"
components = "V, S, M (1 drop of devil blood or 1 dose of unholy water)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Arcanist, Bloodrager, Cleric, Magus, Oracle, Sorcerer, Summoner, Unchained Summoner, Warpriest, Witch, Wizard
Casting time: 1 round
Components: V, S, M (1 drop of devil blood or 1 dose of unholy water)
Range: touch
Duration: 1 minute
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Healing
Descriptors: evil
:::

**Sources:** Hell's Vengeance Player's Guide pg 11, Pathfinder \#29: Mother of Flies pg 67, Gods and
Magic pg 7, Inner Sea World Guide pg 295

You anoint a wounded creature with devil's blood or unholy water, giving it
[fast healing](ref/umr/fast-healing) 1. This ability cannot repair damage caused by silver weapons,
good-aligned weapons, or spells or effects with the good descriptor. The target detects as evil for
the duration of the spell and can sense the evil of the magic, though this has no long-term effect
on the target's alignment.

### Greater Infernal Healing

**Sources:** Hell's Vengeance Player's Guide pg 11

As per infernal healing, except the target gains [fast healing](ref/umr/fast-healing) 4 and the
target detects as an evil cleric.
