+++
id = "ref/arc-skald/urban-skald"
kind = "archetype"
title = "Urban Skald"
source_ids = ["heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "urban_skald", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]

[fields]
kind = "archetype"
replaces = ["Song of marching", "damage reduction", "Dirge of doom"]
alters = ["Weapon and armor proficiencies", "Inspired rage"]
+++

**Sources:** Heroes of the Streets pg 25\
The urban skald finds that challenging and mocking foes is sometimes more effective than inspiring
uncontrolled rage in a city.

**Weapon and Armor Proficiency**

**Alters:** Weapon and armor proficiencies

**Info:** An urban skald is not proficient with medium armor.

**Raging Song (Su)**

**Info:** An urban skald gains a different selection of _raging songs,_ as noted below. The save DC
for a _raging song_ that allows a save is equal to 10 + 1/2 the urban skald's skald level + his
Charisma modifier.

**Controlled Inspired Rage (Su)**

**Ability:** When the urban skald _inspires rage,_ he does not grant the normal benefits. Instead,
he can apply a +2 morale bonus to his allies' Strength, Dexterity, or Constitution.

**Alters:** Inspired rage

**Special:** The urban skald can apply the full bonus to one ability score or split the bonus
between several scores in increments of 2. The choice applies to all affected allies. The controlled
_inspired rage_ grants no bonus on Will saves, imposes no penalties to AC, and does not prevent
affected allies from using Intelligence-, Dexterity-, or Charisma-based skills.

At 8th level: The bonus +4.

At 16th level: The bonus +6.

**Infuriating Mockery (Su)**

**Ability:** The urban skald can inspire reckless fury in one foe within 30 feet. If the foe fails a
Will saving throw, it takes a -2 penalty to AC and on attack rolls, cannot use any Intelligence-,
Dexterity-, or Charisma-based skills, and must succeed at a [concentration](ref/rule/concentration)
check to cast spells (DC = 15 + spell level) for as long as it remains in range of the skald and the
performance is maintained.

**Gained:** At 3rd Level

**Repeat:** The urban skald can target an additional foe with this ability., 7, 4

**Replaces:** Song of marching, [damage reduction](ref/rule/damage-reduction)

**Humiliating Defamation (Su)**

**Ability:** The urban skald can ostracize a foe. The song has one primary target, who the skald
must see and name or describe. That target must attempt a Will save. On a failed save, the primary
target cannot benefit from any morale bonus or teamwork feats, cannot treat any creature as an ally,
and must attempt to save against any spell cast on it (including harmless spells, even if it casts
them on itself). These effects remain as long as the primary target can hear the skald and the skald
maintains the performance.

**Gained:** At 10th Level

**Passive:** All other foes within 60 feet of the skald are secondary targets. Secondary targets
must succeed at Will saves or they cannot treat the primary target as an ally, and cannot target it
with spells or abilities that are harmless. These effects remain as long as the secondary targets
are within 60 feet of the skald and the skald maintains the performance.

**Replaces:** Dirge of doom

**Special:** This is a sonic mind-affecting charm effect.

**Back of the Crowd (Ex)**

**Flavor:** An urban skald has learned to maximize the defensive benefit of being near allies.

**Gained:** At 3rd Level

**Passive:** He gains a +1 dodge bonus to AC when adjacent to 2 or more allies.

At 9th level: This bonus +2.

At 15th level: This bonus +3.
