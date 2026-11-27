+++
id = "ref/arc-cleric/foundation-of-faith"
kind = "archetype"
title = "Foundation of Faith"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Foundation%20of%20Faith"
source_ids = ["elemental-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "foundation_of_faith", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "elemental-masters-handbook"
page = "8"

[fields]
kind = "archetype"
features = [
  { anchor = "channel-energy", level = 1 },
  { anchor = "bastion", level = 1 },
  { anchor = "granite-focus", level = 3 },
  { anchor = "rooted-vitality", level = 5 },
]
trades = [
  { replaces = "Channel energy", feature = "channel-energy", by = ["channel-energy"] },
]
+++

Whether aiding the faithful or defending against the depredations of unbelievers, a foundation of
faith is unshakable in her convictions. These clerics are most common among worshipers of deities of
earth or protection, such as [Abadar](ref/faith/abadar) or [Torag](ref/faith/torag), but any
religion might count foundations of faith among its priests.

## Channel Energy {#channel-energy}

A foundation of faith does not gain the channel energy ability.

## Bastion (Ex) {#bastion}

A foundation of faith is an unbreakable obstacle, unmoved by threats and violence alike. At 1st
level, the foundation of faith adds her Constitution bonus to her CMD and to the DC of attempts to
use the Intimidate skill against her.

## Granite Focus (Ex) {#granite-focus}

A foundation of faith's focus is truly impressive. At 3rd level, the foundation of faith can take a
move action to center herself. If she does, she adds her Constitution modifier to any
[concentration](ref/rule/concentration) checks attempted as part of casting cleric spells until the
end of her turn.

## Rooted Vitality (Su) {#rooted-vitality}

At 5th level, a foundation of faith draws healing from the earth. As a swift action while standing
on natural or worked stone, the foundation of faith can gain [fast healing](ref/umr/fast-healing) 1.
This effect lasts for a number of rounds equal to the foundation of faith's Constitution modifier or
until the foundation of faith loses contact with the natural or worked stone. At 7th level, this
ability increases to [fast healing](ref/umr/fast-healing) 2, and it increases by an additional point
every 2 levels thereafter (to a maximum of [fast healing](ref/umr/fast-healing) 8 at 19th level).

Instead of gaining this [fast healing](ref/umr/fast-healing) herself, a foundation of faith can
expend a use of this ability to instead touch up to six other creatures as a standard action to
grant each creature [half](ref/misc/fractions-and-rounding) of the
[fast healing](ref/umr/fast-healing) that the foundation of faith would receive (minimum
[fast healing](ref/umr/fast-healing) 1). A recipient must be standing on natural or worked stone to
receive this [fast healing](ref/umr/fast-healing), and the [fast healing](ref/umr/fast-healing)
lasts for a number of rounds equal to the foundation of faith's Constitution modifier or until the
recipient leaves contact with natural or worked stone. If one recipient loses this
[fast healing](ref/umr/fast-healing) early, it does not affect the duration for the other targets.

This ability is usable once per day at 5th level, plus an additional time per day for every 5 levels
beyond 5th.
