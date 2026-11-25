+++
id = "ref/arc-paladin/sacred-servant"
kind = "archetype"
title = "Sacred Servant"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Sacred%20Servant"
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
features = [
  { anchor = "smite-evil", level = 1 },
  { anchor = "spells", level = 4 },
  { anchor = "divine-bond", level = 5 },
  { anchor = "call-celestial-ally", level = 8 },
]
trades = [
  { replaces = "Smite evil", feature = "smite-evil", by = ["smite-evil"] },
  { replaces = "Aura of resolve", feature = "aura-of-resolve", by = ["call-celestial-ally"] },
  { alters = "Divine bond", feature = "divine-bond", by = ["divine-bond"] },
]
+++

Paladins as a general rule, venerate the gods of good and purity, but some take this a step further,
dedicating themselves to a specific deity and furthering the cause of the faith. These sacred
servants are rewarded for their devotion with additional spells and powerful allies. A sacred
servant must select one deity to worship. This deity's alignment must be lawful good, lawful
neutral, or neutral good. A sacred servant has the following class features.

## Smite Evil (Su) {#smite-evil}

This functions as the paladin ability, but the sacred servant can smite evil one additional time per
day at 7th level, and every six levels thereafter (instead of 4th level and every three levels
thereafter). This replaces smite evil.

## Spells {#spells}

At 4th level, when a sacred servant gains the ability to cast spells, she also chooses one
[domain](ref/ability/domains) associated with her deity. Her effective [cleric](ref/class/cleric)
level for this domain is equal to her paladin level -3. In addition, she also gains one domain spell
slot for each level of paladin spells she can cast. Every day she must prepare the domain spell from
her chosen domain in that spell slot.

## Divine Bond (Su) {#divine-bond}

At 5th level, instead of forming a divine bond with her weapon or a mount, a sacred servant forms a
bond with her holy symbol. As a standard action, a sacred servant can bind a celestial spirit to her
holy symbol for 1 minute per paladin level. When called, the spirit causes the sacred servant's holy
symbol to shed light like a [torch](ref/eq-misc/torch). At 5th level, the spirit grants one bonus.
For every three levels beyond 5th, the spirit grants one additional bonus. These bonuses can be
spent in a number of ways to grant the paladin enhanced abilities to channel positive energy and to
cast spells. Each bonus can be used to grant one of the following enhancements: +1 caster level to
any paladin spell cast, +1 to the DC to halve the damage of channel positive energy when used to
harm undead, +1d6 to channel positive energy, +1 use/ day of lay on hands. These enhancements stack
and can be selected multiple times. The enhancements granted by the spirit are determined when the
spirit is called and cannot be changed until the spirit is called again. If the sacred servant
increases her number of uses of lay on hands per day in this way, that choice is set for the rest of
the day, and once used, these additional uses are not restored (even if the spirit is called again
that day). The celestial spirit imparts no enhancements if the holy symbol is held by anyone other
than the sacred servant, but resumes giving enhancements if returned to the sacred servant. A sacred
servant can use this ability once per day at 5th level, and one additional time per day for every
four levels beyond 5th, to a total of four times per day at 17th level.

If a holy symbol with a celestial spirit is destroyed, the sacred servant loses the use of this
ability for 30 days, or until she gains a level, whichever comes first. During this 30-day period,
the sacred servant takes a -1 penalty on attack and weapon damage rolls.

## Call Celestial Ally (Sp) {#call-celestial-ally}

At 8th level, a sacred servant can call upon her deity for aid, in the form of a powerful servant.
This allows the sacred servant to cast _[lesser planar ally](ref/spell/planar-ally-lesser)_ once per
week as a [spell-like ability](ref/umr/spell-like-abilities) without having to pay the material
component cost or the servant (for reasonable tasks). At 12th level, this improves to
_[planar ally](ref/spell/planar-ally)_ and at 16th level, this improves to
_[greater planar ally](ref/spell/planar-ally-greater)_. The sacred servant's caster level for this
effect is equal to her paladin level. This ability replaces aura of resolve.
