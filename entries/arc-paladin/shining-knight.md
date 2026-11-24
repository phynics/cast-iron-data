+++
id = "ref/arc-paladin/shining-knight"
kind = "archetype"
title = "Shining Knight"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Shining%20Knight"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shining_knight", path = "json/archetypes_paladin.json" },
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
  { anchor = "skilled-rider", level = 3 },
  { anchor = "divine-bond" },
  { anchor = "knight-s-charge", level = 11 },
]
trades = [
  { replaces = "Divine health", feature = "divine-health", by = ["skilled-rider"] },
  { replaces = "Aura of justice", feature = "aura-of-justice", by = ["knight-s-charge"] },
  { alters = "Divine bond", feature = "divine-bond", by = ["divine-bond"] },
]
+++

While paladins often are seen mounted atop a loyal steed, the shining knight is the true symbol of
mounted bravery. They are never far from their steeds and are always clad in brightly polished
armor. The shining knight has the following class features.

## Skilled Rider (Ex and Su) {#skilled-rider}

At 3rd level, a shining knight does not take any penalty to her Ride skill due to her armor check
penalty. In addition, any mount she is riding gains the benefit of her divine grace class feature,
adding her Charisma bonus (if any) to its saving throws. This ability replaces divine health.

## Divine Bond (Su) {#divine-bond}

Upon reaching 5th level, a shining knight must form a bond with a mount. This ability otherwise
functions as the paladin ability.

## Knight's Charge (Su) {#knight-s-charge}

At 11th level, whenever a mounted shining knight charges a foe, her movement does not provoke
attacks of opportunity, for either her or her mount. In addition, if her target is also the target
of her smite evil ability and the charge attack hits, the target must make a Will save or be
[panicked](ref/misc/panicked) for a number of rounds equal to 1/2 the shining knight's level. The DC
of this save is equal to 10 + 1/2 the shining knight's level + the shining knight's Charisma
modifier. This ability replaces aura of justice.
