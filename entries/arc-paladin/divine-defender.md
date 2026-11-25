+++
id = "ref/arc-paladin/divine-defender"
kind = "archetype"
title = "Divine Defender"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Divine%20Defender"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "divine_defender", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "advanced-players-guide"
page = "116"

[fields]
kind = "archetype"
features = [
  { anchor = "shared-defense", level = 3 },
  { anchor = "divine-bond", level = 5 },
]
trades = [
  { replaces = "Mercy", feature = "mercy", by = ["shared-defense"] },
]
+++

Some paladins see themselves as the last line of defense between the teeming hordes of evil and the
innocent folk trying to make a living in a harsh, unforgiving world. These defenders spend their
lives protecting others and taking on foes that the common man should not even know exist. To aid
them in their holy mission, they have special powers to protect themselves and those around them.
The divine defender has the following class features.

## Shared Defense (Su) {#shared-defense}

At 3rd level, a divine defender can spend one use of her lay on hands ability as a standard action
to grant all adjacent allies (including paladins) a bonus. At 3rd level, adjacent allies receive a
+1 sacred bonus to their AC and CMD and on their saving throws. These bonuses last for a number of
rounds equal to the divine defender's Charisma modifier. At 9th level and 15th level, this bonus
increases by +1. At 6th level, these bonuses are granted to all allies within 10 feet, and allies
that are at fewer than 0 hit points within this area are automatically stabilized. At 12th level,
these bonuses are granted to all allies within 15 feet, and allies within this area are immune to
[bleed](ref/umr/bleed) damage. At 18th level, these bonuses are granted to all allies within 20
feet, and allies within this area gain a 25% chance to negate any sneak attack or critical hit
scored against them. This ability does not stack with the chance provided from the light, medium, or
heavy _fortification_ armor special abilities. These bonuses are cumulative with each other. Allies
only benefit from these bonuses while in the listed area. This ability replaces mercy.

## Divine Bond (Su) {#divine-bond}

At 5th level, instead of forming a divine bond with her weapon or a mount, a divine defender can
form a bond with her armor. As a standard action, a divine defender can enhance her armor by calling
upon the aid of a celestial spirit. This bond lasts for 1 minute per paladin level. When called, the
spirit causes the armor to shed light like a [torch](ref/eq-misc/torch). At 5th level, the spirit
grants the armor a +1 enhancement bonus. For every three levels beyond 5th, the armor gains another
+1 enhancement bonus, to a maximum of +6 at 20th level. These bonuses can be added to the armor,
stacking with existing armor bonuses to a maximum of +3, or they can be used to add any of the
following armor properties (asterisks note new armor properties found in Chapter 7):
_[champion](ref/magic-enh/champion)_, _[ghost touch](ref/magic-enh/ghost-touch-armor),
[heavy fortification](ref/magic-enh/fortification-heavy),
[invulnerability](ref/magic-enh/invulnerability),
[light fortification](ref/magic-enh/fortification-light),
[moderate fortification](ref/magic-enh/fortification-moderate),
[spell resistance](ref/magic-enh/spell-resistance)_ (13, 15, 17, or 19). Adding these properties
consumes an amount of bonus equal to the property's cost (see Table 15–4 of the _Core Rulebook_). In
addition, the bonuses can be consumed at the listed amount to add any of the following armor
properties: _[energy resistance](ref/magic-enh/energy-resistance)_ for +3 bonus,
_[improved energy resistance](ref/magic-enh/energy-resistance-improved)_ for +5 bonus, or
_[righteous](ref/magic-enh/righteous)_ for +4 bonus. These bonuses are added to any properties the
armor already has, but duplicate abilities do not stack. If the armor is not magical, at least a +1
enhancement bonus must be added before any other properties can be added. The bonus and properties
granted by the spirit are determined when the spirit is called and cannot be changed until the
spirit is called again. The celestial spirit imparts no bonuses if the armor is worn by anyone other
than the divine defender, but it resumes giving bonuses if the divine defender dons the armor again.
A divine defender can use this ability once per day at 5th level, and one additional time per day
for every four levels beyond 5th, to a total of four times per day at 17th level.

If a suit of armor with a celestial spirit is destroyed, the divine defender loses the use of this
ability for 30 days, or until she gains a level, whichever comes first. During this 30-day period,
the divine defender takes a -1 penalty on attack and weapon damage rolls.
