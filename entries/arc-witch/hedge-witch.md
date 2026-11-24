+++
id = "ref/arc-witch/hedge-witch"
kind = "archetype"
title = "Hedge Witch"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Hedge%20Witch"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hedge_witch", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "ultimate-magic"
page = "84"

[fields]
kind = "archetype"
features = [
  { anchor = "patron" },
  { anchor = "spontaneous-healing", level = 4 },
  { anchor = "empathic-healing", level = 8 },
  { anchor = "hexes" },
  { anchor = "major-hexes" },
]
trades = [
  { replaces = "4th-level hex", feature = "hex", levels = [4], by = ["spontaneous-healing"] },
  { replaces = "8th-level hex", feature = "hex", levels = [8], by = ["empathic-healing"] },
]
+++

Among witches, there are those who devote themselves to the care of others and restrict their
practices to the healing arts. They often take the place of clerics in rural communities and may
wander the countryside servicing the needs of several small communities.

## Patron {#patron}

A hedge witch's patron is normally one with a [healing](ref/patron/healing) theme.

## Spontaneous Healing (Su) {#spontaneous-healing}

A hedge witch can channel stored spell energy into healing spells that she did not prepare ahead of
time. The witch can "lose" any prepared spell that is not a cantrip in order to cast any _cure_
spell of the same spell level or lower, even if she doesn't know that cure spell. This replaces the
witch's hex gained at 4th level.

## Empathic Healing (Su) {#empathic-healing}

A hedge witch can minister to a diseased or poisoned target, redirecting the affliction into
herself. For a poisoned target, the witch must tend to him as a standard action; he makes his next
saving throw against the poison as normal, but the witch suffers the effects of the failed save
instead of the poisoned creature. For a diseased target, the witch must tend to the sick person for
an hour; he makes his next saving throw against the disease as normal, but the witch suffers the
effects of the failed save instead of the diseased creature. The witch does not actually become
poisoned or diseased (and is not contagious and does not need to be cured), but suffers the effects
of the affliction as if she had been. The witch normally uses this ability to extend the life of
someone near death, giving him time to recover. This ability has no effect if the witch is immune to
disease or poison. This replaces the witch's hex gained at 8th level.

## Hexes {#hexes}

The following witch hexes complement the hedge witch archetype: cauldron, feral speech, healing,
tongues.

## Major Hexes {#major-hexes}

The following major hexes complement the hedge witch archetype: major healing, weather control,
witch's brew. Grand Hexes: The following grand hex complements the hedge witch archetype: life
giver.
