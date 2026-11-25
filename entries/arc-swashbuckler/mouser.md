+++
id = "ref/arc-swashbuckler/mouser"
kind = "archetype"
title = "Mouser"
aon = "ArchetypeDisplay.aspx?FixedName=Swashbuckler%20Mouser"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mouser", path = "json/archetypes_swashbuckler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/swashbuckler" },
]
[[sources]]
publication = "advanced-class-guide"
page = "125"

[fields]
kind = "archetype"
features = [
  { anchor = "deeds" },
  { anchor = "underfoot-assault", level = 1 },
  { anchor = "quick-steal", level = 3 },
  { anchor = "hamstring", level = 7 },
  { anchor = "cat-s-charge", level = 11 },
]
trades = [
  { replaces = "Opportune parry and riposte", feature = "deeds", power = "opportune parry and riposte", by = ["underfoot-assault"] },
  { replaces = "Menacing swordplay", feature = "deeds", power = "menacing swordplay", by = ["quick-steal"] },
  { replaces = "Targeted strike", feature = "deeds", power = "targeted strike", by = ["hamstring"] },
  { replaces = "Bleeding wound", feature = "deeds", power = "bleeding wound", by = ["cat-s-charge"] },
]
+++

In the hands of a trained warrior, a well-sharpened blade is deadly regardless of size. A mouser
moves in close, using her size and skill as an advantage.

## Deeds {#deeds}

The mouser gains the following deeds, each of which replaces an existing deed.

## Underfoot Assault (Ex) {#underfoot-assault}

At 1st level, if a foe whose size is larger than the mouser's is adjacent to her and misses her with
a melee attack, the mouser can as an immediate action spend 1 panache point to move 5 feet into an
area of the attacker's space. This movement does not count against the mouser's movement the next
round, and it doesn't provoke attacks of opportunity. While the mouser is within a foe's space, she
is considered to occupy her square within that foe's space.

While the mouser is within her foe's space, the foe takes a -4 penalty on all attack rolls and
combat maneuver checks not made against the mouser, and all of the mouser's allies that are adjacent
to both the foe and the mouser are considered to be [flanking](ref/rule/flanking) the foe. The
mouser is considered to be flanking the foe whose space she is within if she is adjacent to an ally
who is also adjacent to the foe. The mouser can move within her foe's space and leave the foe's
space unhindered and without provoking attacks of opportunity, but if the foe attempts to move to a
position where the mouser is no longer in its space, the movement provokes an attack of opportunity
from the mouser. This deed replaces opportune parry and riposte.

## Quick Steal (Ex) {#quick-steal}

At 3rd level, as a swift action the mouser can spend 1 panache point when she hits a foe larger than
her size with a light or one-handed piercing melee weapon to attempt a [steal](ref/rule/steal)
combat maneuver check against the creature she hit. Using this deed does not provoke an attack of
opportunity. This deed replaces menacing swordplay.

## Hamstring (Ex) {#hamstring}

At 7th level, as long as a mouser has at least 1 panache point when she hits a foe whose size is
larger than her own with a light or one-handed piercing melee weapon, she can as a swift action
attempt a [dirty trick](ref/rule/dirty-trick) combat maneuver check. Instead of the normal
conditions that can be applied with dirty trick, this deed can only [stagger](ref/misc/staggered)
the target if the check is successful. This deed replaces targeted strike.

## Cat's Charge (Ex) {#cat-s-charge}

At 11th level, as long as a mouser has at least 1 panache point, when she [charges](ref/rule/charge)
a foe whose size is larger than her own, the mouser can end her charge in any space she can reach,
not just the closest space. All other requirements of the charge must still be satisfied. This deed
replaces bleeding wound.
