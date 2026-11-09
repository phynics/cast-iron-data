+++
id = "ref/arc-alchemist/wasteland-blightbreaker"
kind = "archetype"
title = "Wasteland Blightbreaker"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Wasteland%20Blightbreaker"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wasteland_blightbreaker", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "healers-handbook"
page = "10"

[fields]
kind = "archetype"
replaces = ["Poison resistance +2", "Swift poisoning", "Poison resistance +6", "the discovery gained at 8th level"]
+++

The deleterious effects of the weird hazards of the Mana Wastes require special skill to remedy.
Many wasteland blightbreakers are also [chirurgeons](ref/arc-alchemist/chirurgeon).

**Healing Infusion (Sp, Su)**

**Gained:** At 2nd Level

**Passive:** The blightbreaker can prepare extracts of the [healing](ref/spelldef/healing) subschool
as if he had the [infusion](ref/discovery/infusion) discovery and can choose to render any such
extracts inert and prepare other extracts to replace them (unlike infusions, which continue to
occupy the alchemist's daily extract slots until consumed or used).

**Replaces:** Poison resistance +2

**Standard:** If the blightbreaker has the infusion discovery, or if he is also a chirurgeon, he can
use [touch injection](ref/spell/touch-injection) as a
[spell-like ability](ref/umr/spell-like-abilities) once per day, but only to absorb an infusion of
the healing subschool.

**Swift Healing Infusions (Sp)**

**Gained:** At 6th Level

**Replaces:** Swift poisoning

**Standard:** The blightbreaker can absorb an infusion of the healing subschool as if with
_[touch injection](ref/spell/touch-injection)_ an unlimited number of times per day.

**Swift:** While he has a healing extract absorbed in this fashion, he can deliver it.

**Banish Blights (Su)**

**Ability:** A blightbreaker can end any effect affecting a creature that could be reversed by
[break enchantment](ref/spell/break-enchantment). To do so, the affected creature must imbibe one of
the blightbreaker's infused extracts of the healing subschool of at least 3rd level. The
blightbreaker must then attempt a caster level check as described in
_[break enchantment](ref/spell/break-enchantment)._ If the blightbreaker succeeds at the check, the
creature is free of the spell, curse, or effect. The blightbreaker can also use this ability to
attempt to dispel [primal magic](ref/rule/primal-magic) events affecting a creature or an area. To
do so, the affected creature must imbibe an infused extract as described above, and the
blightbreaker must attempt a caster level check against a DC equal to 11 + the primal magic event's
CR. If he succeeds at the check, the primal magic event ends as if the blightbreaker had
successfully used dispel magic.

**Gained:** At 8th Level

**Replaces:** Poison resistance +6, the discovery gained at 8th level

**Special:** If the blightbreaker attempts to dispel a primal magic event affecting an area, as a
**standard action**, he must dump an infused extract of the healing subschool of at least 3rd level
onto an affected square. He then must attempt a caster level check against a DC equal to 11 + the
primal magic event's CR. If he succeeds at the check, the primal magic event ends as if the
blightbreaker had successfully used [dispel magic](ref/spell/dispel-magic).

**Discoveries:** The following discoveries complement the wasteland blightbreaker archetype:
[dispelling bomb](ref/discovery/dispelling-bomb), [elixir of life](ref/discovery/elixir-of-life),
[healing bomb](ref/discovery/healing-bomb), [healing touch](ref/discovery/healing-touch),
[infusion](ref/discovery/infusion), [spontaneous healing](ref/discovery/spontaneous-healing).
