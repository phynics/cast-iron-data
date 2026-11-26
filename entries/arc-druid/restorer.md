+++
id = "ref/arc-druid/restorer"
kind = "archetype"
title = "Restorer"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Restorer"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "restorer", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "healers-handbook"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "healing-touch", level = 1 },
  { anchor = "natural-medic" },
  { anchor = "enemy-of-blight", level = 4 },
  { anchor = "guide-across-lifetimes", level = 13 },
]
trades = [
  { replaces = "Nature sense", feature = "nature-sense", by = ["healing-touch"] },
  { replaces = "Spontaneous casting", feature = "spontaneous-casting", by = ["natural-medic"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["enemy-of-blight"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["guide-across-lifetimes"] },
]
+++

Restorers carefully tend to the health of both the environment and creatures in it. Restorers in the
most remote places often choose druidic herbalism as their nature bond option (see below).

## Healing Touch (Ex) {#healing-touch}

A restorer gains a +2 bonus on Heal checks. When a restorer uses Heal to provide first aid, the
bonus increases to +3.

This ability replaces nature sense.

## Natural Medic {#natural-medic}

A restorer can channel stored spell energy into healing spells that she did not prepare ahead of
time. The restorer can "lose" any prepared spell in order to cast any cure spell she can cast of the
same spell level or lower (a cure spell is any spell with "cure" in its name).

This ability replaces spontaneous casting.

## Enemy of Blight (Ex) {#enemy-of-blight}

At 4th level, a restorer can ignore the effects of an overgrown area that has been magically
manipulated to impede motion. She can ignore these effects for a number of rounds per day equal to
double her Wisdom bonus. These rounds don't have to be used consecutively.

This ability replaces resist nature's lure.

## Guide across Lifetimes (Sp) {#guide-across-lifetimes}

At 13th level, once per day as a full-round action, a restorer can cast
_[reincarnate](ref/spell/reincarnate)_ without a material component.

This ability replaces a thousand faces.
