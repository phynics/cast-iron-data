+++
id = "ref/arc-skald/urban-skald"
kind = "archetype"
title = "Urban Skald"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Urban%20Skald"
source_ids = ["heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "urban_skald", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "heroes-of-the-streets"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "controlled-inspired-rage", level = 1 },
  { anchor = "infuriating-mockery", level = 3 },
  { anchor = "humiliating-defamation", level = 10 },
  { anchor = "back-of-the-crowd", level = 3 },
]
trades = [
  { replaces = "Song of marching", feature = "song-of-marching", by = ["infuriating-mockery"] },
  { replaces = "damage reduction", feature = "damage-reduction", by = ["infuriating-mockery"] },
  { replaces = "Dirge of doom", feature = "dirge-of-doom", by = ["humiliating-defamation"] },
  { alters = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { alters = "Inspired rage", feature = "inspired-rage", by = ["controlled-inspired-rage"] },
]
+++

The urban skald finds that challenging and mocking foes is sometimes more effective than inspiring
uncontrolled rage in a city.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

An urban skald is not proficient with medium armor. This ability modifies the skald's weapon and
armor proficiencies.

## Raging Song (Su) {#raging-song}

An urban skald gains a different selection of raging songs, as noted below. The save DC for a raging
song that allows a save is equal to 10 + 1/2 the urban skald's skald level + his Charisma modifier.

## Controlled Inspired Rage (Su) {#controlled-inspired-rage}

When the urban skald inspires rage, he does not grant the normal benefits. Instead, he can apply a
+2 morale bonus to his allies' Strength, Dexterity, or Constitution. This bonus increases to +4 at
8th level and to +6 at 16th level. The urban skald can apply the full bonus to one ability score or
split the bonus between several scores in increments of 2. The choice applies to all affected
allies. The controlled inspired rage grants no bonus on Will saves, imposes no penalties to AC, and
does not prevent affected allies from using Intelligence-, Dexterity-, or Charisma-based skills.
This alters inspired rage.

## Infuriating Mockery (Su) {#infuriating-mockery}

At 3rd level, the urban skald can inspire reckless fury in one foe within 30 feet. If the foe fails
a Will saving throw, it takes a -2 penalty to AC and on attack rolls, cannot use any Intelligence-,
Dexterity-, or Charisma-based skills, and must succeed at a [concentration](ref/rule/concentration)
check to cast spells (DC = 15 + spell level) for as long as it remains in range of the skald and the
performance is maintained. At 7th level and every 4 levels thereafter, the urban skald can target an
additional foe with this ability. This replaces song of marching and
[damage reduction](ref/rule/damage-reduction).

## Humiliating Defamation (Su) {#humiliating-defamation}

At 10th level, the urban skald can ostracize a foe. The song has one primary target, who the skald
must see and name or describe. That target must attempt a Will save. On a failed save, the primary
target cannot benefit from any morale bonus or teamwork feats, cannot treat any creature as an ally,
and must attempt to save against any spell cast on it (including harmless spells, even if it casts
them on itself). These effects remain as long as the primary target can hear the skald and the skald
maintains the performance.

All other foes within 60 feet of the skald are secondary targets. Secondary targets must succeed at
Will saves or they cannot treat the primary target as an ally, and cannot target it with spells or
abilities that are harmless. These effects remain as long as the secondary targets are within 60
feet of the skald and the skald maintains the performance. This is a sonic mind-affecting charm
effect.

This ability replaces dirge of doom.

## Back of the Crowd (Ex) {#back-of-the-crowd}

At 3rd level, an urban skald has learned to maximize the defensive benefit of being near allies. He
gains a +1 dodge bonus to AC when adjacent to 2 or more allies. This bonus increases to +2 at 9th
level and to +3 at 15th level.
