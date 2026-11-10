+++
id = "ref/arc-paladin/sacred-servant"
kind = "archetype"
title = "Sacred Servant"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sacred_servant", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "advanced-players-guide"
page = "117"

[fields]
kind = "archetype"
replaces = ["Smite evil", "Aura of resolve"]
alters = ["Divine bond"]
+++

Paladins as a general rule, venerate the gods of good and purity, but some take this a step further,
dedicating themselves to a specific deity and furthering the cause of the faith. These sacred
servants are rewarded for their devotion with additional spells and powerful allies. A sacred
servant must select one deity to worship. This deity's alignment must be lawful good, lawful
neutral, or neutral good. A sacred servant has the following class features.

**Smite Evil (Su)**

**Info:** This functions as the paladin ability, but the sacred servant has fewer uses of _smite
evil_ per day.

**Replaces:** Smite evil

**Usage:** 1 time/day + 1 per 6 paladin levels beyond 1st

**Spells**

**Ability:** When a sacred servant gains the ability to cast spells, she also chooses one
[domain](ref/ability/domains) associated with her deity. Her effective [cleric](ref/class/cleric)
level for this domain is equal to her paladin level - 3. In addition, she also gains one domain
spell slot for each level of paladin spells she can cast. Every day she must prepare the domain
spell from her chosen domain in that spell slot.

**Gained:** At 4th Level

**Divine Bond (Su)**

**Action:** Standard Action

**Alters:** Divine bond

**Flavor:** Instead of forming a _divine bond_ with her weapon or a mount, a sacred servant forms a
bond with her holy symbol.

**Gained:** At 5th Level

**Special:** The celestial spirit imparts no enhancements if the holy symbol is held by anyone other
than the sacred servant, but resumes giving enhancements if returned to the sacred servant.

If a holy symbol with a celestial spirit is destroyed, the sacred servant loses the use of this
ability for 30 days, or until she gains a level, whichever comes first. During this 30-day period,
the sacred servant takes a -1 penalty on attack and weapon damage rolls.

Once a day, a sacred servant can bind a celestial spirit to her holy symbol for 1 minute per paladin
level. When called, the spirit causes the sacred servant's holy symbol to shed light like a
[torch](ref/eq-misc/torch).

Starting out, the spirit grants one bonus. As the sacred servant gains levels, the spirit grants
more bonuses. These bonuses can be spent in a number of ways to grant the paladin enhanced abilities
to channel positive energy and to cast spells.

Each bonus can be used to grant one of the following enhancements:

- +1 caster level to any paladin spell cast
- +1 to the DC to halve the damage of channel positive energy when used to harm undead
- +1d6 to channel positive energy
- +1 use/day of _lay on hands_

These enhancements stack and can be selected multiple times. The enhancements granted by the spirit
are determined when the spirit is called and cannot be changed until the spirit is called again.

If the sacred servant increases her number of uses of _lay on hands_ per day in this way, that
choice is set for the rest of the day, and once used, these additional uses are not restored (even
if the spirit is called again that day).

**Call Celestial Ally (Sp)**

**At 12th Level:** This improves to [planar ally](ref/spell/planar-ally).

**At 16th Level:** This improves to [greater planar ally](ref/spell/planar-ally-greater).

**At 8th Level:** A sacred servant can call upon her deity for aid, in the form of a powerful
servant. This allows the sacred servant to cast [lesser planar ally](ref/spell/planar-ally-lesser)
once per week as a [spell-like ability](ref/umr/spell-like-abilities) without having to pay the
material component cost or the servant (for reasonable tasks).

**Replaces:** Aura of resolve

**Special:** The sacred servant's caster level for this effect is equal to her paladin level.
