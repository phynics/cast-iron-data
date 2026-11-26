+++
id = "ref/arc-oracle/shigenjo"
kind = "archetype"
title = "Shigenjo"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Shigenjo"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shigenjo", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "advanced-race-guide"
page = "164"

[fields]
kind = "archetype"
features = [
  { anchor = "ki-pool", level = 7 },
  { anchor = "quivering-palm", level = 15 },
  { anchor = "final-revelation", level = 20 },
]
trades = [
  { replaces = "Mystery bonus spells at these levels", feature = "mystery", levels = [2, 4, 8, 12, 14, 16], power = "bonus spells" },
  { replaces = "7th-level revelation", feature = "revelation", levels = [7], by = ["ki-pool"] },
  { replaces = "Final revelation of the shigenjo's mystery", feature = "final-revelation", by = ["final-revelation"] },
]
+++

The shigenjo walks the path of enlightenment and transcendence by seeking oneness with the celestial
spirits. In doing so, she unlocks the martial potential of her own spiritual power. A shigenjo has
the following class features.

## Class Skills {#class-skills}

A shigenjo adds Survival to her list of class skills in place of Diplomacy.

## Alignment {#alignment}

Any neutral.

## Recommended Mysteries {#recommended-mysteries}

ancestor, battle, fire, heavens, lore, metal, nature, stone, time, waves, wood.

## Bonus Spells {#bonus-spells}

_true strike_ (2nd), _alter self_ (4th), _divine power_ (8th), _magic jar_ (12th), _ki shout_
(14th), _moment of prescience_ (16th). These bonus spells replace the shigenjo's mystery bonus
spells at these levels.

## Ki Pool (Su) {#ki-pool}

At 7th level, a shigenjo gains a pool of ki points, supernatural energy she can use to accomplish
amazing feats. The number of points in the shigenjo's ki pool is equal to 1/3 her oracle level + her
Charisma modifier. The ki pool is replenished each morning after 8 hours of rest or meditation;
these hours do not need to be consecutive. If the shigenjo possesses levels in another class that
grants points to a ki pool, ki points gained from the shigenjo class stack with those gained from
the other class to determine the total number of ki points in the combined pool, but only one
ability score modifier is added to the total. The choice of which score to use is made when the
second class ability is gained, and once made, the choice is permanent. The shigenjo can use ki
points from this pool to power the abilities of every class she possesses that grants a ki pool.

As long as she has at least 1 point in her ki pool, a shigenjo can make a ki strike as a monk whose
level is equal to her oracle level - 3. As a swift action, she may spend 1 point from her ki pool to
gain one of the following three benefits.

### Ki Magic {#ki-magic}

Add +1 to the DC of the next spell she casts on her turn.

### Ki Curse {#ki-curse}

Treat her oracle level as 5 higher for the purpose of determining the effects of her
[curse](ref/carried/bestiary/rules/universal-monster-rules/curse) for the next round.

### Ki Insight {#ki-insight}

Gain a +4 insight bonus on Spellcraft checks for 1 round.

This ability replaces the shigenjo's 7th-level revelation.

## Quivering Palm (Su) {#quivering-palm}

At 15th level, a shigenjo may learn quivering palm as the [monk](ref/class/monk) ability of the same
name in place of a revelation. She treats her oracle level as her monk level for this ability, and
the DC is based on her Charisma bonus instead of her Wisdom bonus.

## Final Revelation {#final-revelation}

Upon reaching 20th level, you achieve true enlightenment and become one with the celestial spirits.
You gain the ability to speak with any creature that uses a language. For a number of days equal to
your Wisdom score, you can ignore the negative effects of extreme weather, starvation, thirst, and
exhaustion. If you die, your powerful connection to the celestial realm allows you to be reborn 3
days later (as _[reincarnate](ref/spell/reincarnate)_). This replaces the final revelation of the
shigenjo's mystery.
