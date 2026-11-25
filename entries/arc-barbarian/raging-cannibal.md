+++
id = "ref/arc-barbarian/raging-cannibal"
kind = "archetype"
title = "Raging Cannibal"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Raging%20Cannibal"
source_ids = ["ultimate-wilderness", "champions-of-corruption"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "raging_cannibal", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "38"
[[sources]]
publication = "champions-of-corruption"
page = "27"

[fields]
kind = "archetype"
features = [
  { anchor = "animal-fury", level = 2 },
  { anchor = "consume-vigor", level = 2 },
  { anchor = "intimidating-gouge", level = 3 },
  { anchor = "feed-from-fury", level = 5 },
  { anchor = "razor-toothed-fury", level = 6 },
]
trades = [
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["consume-vigor"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["intimidating-gouge"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["feed-from-fury"] },
  { replaces = "Damage reduction", feature = "damage-reduction", by = ["razor-toothed-fury"] },
  { alters = "The barbarian's 2nd-level rage power", feature = "rage-powers", levels = [2], by = ["animal-fury"] },
]
+++

While savagery is not inherently evil, some barbaric cultures thrive on depravity and welcome the
act of feeding on their own kind. The raging cannibal is a barbarian who feasts upon her fallen
opponents not out of hunger, or even a taste for flesh, but rather because she believes consuming
her foes and defiling their lost lives demonstrates her strength. This penchant for feasting on the
flesh of her kin makes the raging cannibal an awkward companion to travel with for many groups, with
rumors revolving around the raging cannibal's culinary exploits often causing tense situations that
other party members might be called upon to resolve via diplomacy before the raging cannibal grows
frustrated and decides to take matters into her own hands!

## Animal Fury {#animal-fury}

At 2nd level, a raging cannibal must select [animal fury](ref/ragepower/animal-fury) as her first
rage power.

This alters the barbarian's 2nd-level rage power.

## Consume Vigor (Ex) {#consume-vigor}

At 2nd level, when a raging cannibal reduces a creature of the same creature type as herself to 0 or
fewer hit points with her bite attack during combat while raging, she can consume a chunk of its
body to gain a portion of its power. If the creature's CR equals or exceeds her barbarian level, the
raging cannibal gains 1 additional round of rage. She can never consume the same creature's vigor
more than once. At 5th level and every 3 levels thereafter, the raging cannibal gains 1 additional
round of rage each time she uses this ability.

This replaces uncanny dodge.

## Intimidating Gouge (Ex) {#intimidating-gouge}

At 3rd level, when a raging cannibal confirms a critical hit against a creature of the same creature
type as herself with her bite attack while raging, she gains a bonus on Intimidate checks equal to
[half](ref/misc/fractions-and-rounding) her barbarian level for the duration of the rage.

This replaces trap sense.

## Feed from Fury (Ex) {#feed-from-fury}

At 5th level, a raging cannibal is empowered by eating her enemies during combat. When a raging
cannibal confirms a critical hit against a creature of the same creature type as herself with her
bite attack while raging, she gains a number of
[temporary hit points](ref/rule/temporary-hit-points) equal to her barbarian level. These temporary
hit points stack with other temporary hit points gained from this ability but not with those from
other sources. These temporary hit points fade after a period of time equal to 10 minutes per
barbarian level.

This replaces improved uncanny dodge.

## Razor-Toothed Fury (Ex) {#razor-toothed-fury}

At 6th level, a raging cannibal's bite becomes even more fearsome. When using her bite attack, the
raging cannibal can take a -1 penalty on her attack roll to add 2 points of [bleed](ref/rule/bleed)
damage to the damage dealt. At 10th level and every 4 levels thereafter, the attack penalty
increases by 1 and the bleed damage increases by 2 points.

This replaces [damage reduction](ref/rule/damage-reduction).

## Rage Powers {#rage-powers}

The following rage powers complement the raging cannibal archetype:
[internal fortitude](ref/ragepower/internal-fortitude),
[intimidating glare](ref/ragepower/intimidating-glare), [primal scent](ref/ragepower/primal-scent),
[scent](ref/ragepower/scent), and [terrifying howl](ref/ragepower/terrifying-howl).
