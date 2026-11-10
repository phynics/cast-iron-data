+++
id = "ref/rule/attacks-that-deal-wound-point-damage"
kind = "rule"
title = "Attacks that Deal Wound Point Damage"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "attacks_that_deal_wound_point_damage", path = "json/rules_opt_combat01.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "207"

[fields]
kind = "none"
+++

Some attacks can be used to deal wound points damage directly.

**Critical Hits:** When a creature is subject to a critical hit, the critical hit deals the damage
normally, reducing vigor points first, and then reducing wound points when vigor points are gone. It
also deals an amount of wound point damage equal to its critical multiplier (for example, 3 wound
points for a weapon with a ×3 modifier), on top of any wound point damage the creature might take
from the critical hit.

**Negative Energy Damage:** When a creature deals negative energy damage to a creature with a spell
or effect, it can choose to deal wound point or vigor point damage (but not both) with the spell or
effect. If that creature chooses to deal vigor point damage, the spell or effect deals negative
energy damage normally, and that damage reduces vigor points only, even if it deals more damage than
the target has vigor points. If the spell or effect deals negative energy damage to wound points
directly, it deals an amount of wound point damage equal to the number of dice the creature would
roll for that effect; if the effect deals a number of points per caster level (such as the
[harm](ref/spell/harm) spell), it deals a number of wound points equal to the caster level of the
spell.
