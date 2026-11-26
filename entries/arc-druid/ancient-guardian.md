+++
id = "ref/arc-druid/ancient-guardian"
kind = "archetype"
title = "Ancient Guardian"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Ancient%20Guardian"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ancient_guardian", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "monster-codex"
page = "140"

[fields]
kind = "archetype"
features = [
  { anchor = "ancient-arms" },
  { anchor = "community-bond", level = 1 },
  { anchor = "patience-of-nature", level = 2 },
  { anchor = "ancient-ways", level = 3 },
  { anchor = "dispel-hostility", level = 3 },
  { anchor = "unimpeachable", level = 4 },
  { anchor = "undo-artifice", level = 13 },
]
trades = [
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["patience-of-nature"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["ancient-ways"] },
  { replaces = "woodland stride", feature = "woodland-stride", by = ["ancient-ways"] },
  { replaces = "Spontaneous casting", feature = "spontaneous-casting", by = ["dispel-hostility"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["unimpeachable"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["undo-artifice"] },
  { alters = "Weapon proficiencies", feature = "weapon-and-armor-proficiencies", power = "weapons", by = ["ancient-arms"] },
  { alters = "Nature bond", feature = "nature-bond", by = ["community-bond"] },
]
+++

Ancient guardians revere nature and draw power from its divine energies, but also protect the
customs, histories, and lore of their tribe and race. They act as ambassadors and protectors of the
old ways, nurturing their tribe's growth and holding back civilization's corruptive influence.

## Ancient Arms {#ancient-arms}

An ancient guardian can't wield weapons made primarily of metal. She is proficient with only the
[club](ref/eq-weapon/club), [dart](ref/eq-weapon/dart), [quarterstaff](ref/eq-weapon/quarterstaff),
[shortspear](ref/eq-weapon/shortspear), [sling](ref/eq-weapon/sling), and
[spear](ref/eq-weapon/spear). She is also proficient with all natural attacks (claw, bite, and so
forth) of any form she assumes with wild shape. Using a prohibited weapon renders her unable to cast
druid spells or use any of her druid supernatural or spell-like class abilities while wielding the
weapon and for 24 hours after ceasing to wield it. This alters the druid's normal weapon
proficiencies.

## Community Bond (Ex) {#community-bond}

At 1st level, an ancient guardian must choose the domain nature bond ability and select from the
following domains: Community, [Healing](ref/domain/healing), Knowledge,
[Protection](ref/domain/protection), or Repose. This ability alters nature bond.

## Patience of Nature (Ex) {#patience-of-nature}

An ancient guardian does not gain wild empathy at 1st level. Instead, at 2nd level, an ancient
guardian adds [Diplomacy](ref/skill/diplomacy), [Perform (oratory)](ref/skill/perform-any), and
[Sense Motive](ref/skill/sense-motive) to her list of class skills and gains an insight bonus equal
to [half](ref/misc/fractions-and-rounding) her druid level on such checks. This ability replaces
wild empathy.

## Ancient Ways (Ex) {#ancient-ways}

At 3rd level, an ancient guardian increases any climb, fly, or swim speeds she has or gains via her
wild shape ability by 10 feet. This ability replaces trackless step and woodland stride.

## Dispel Hostility (Su) {#dispel-hostility}

An ancient guardian doesn't gain spontaneous casting at 1st level. Instead, at 3rd level, she can
channel stored spell energy into a spell capable of dispelling hostile thoughts and strong emotions.
She can "lose" a prepared spell in order to cast _[calm emotions](ref/spell/calm-emotions)_. Instead
of the normal Will saving throw for that spell, the DC of a
_[calm emotions](ref/spell/calm-emotions)_ spell cast with this ability is 10 + 1/2 the ancient
guardian's druid level + her Wisdom modifier. This ability replaces spontaneous casting.

## Unimpeachable (Ex) {#unimpeachable}

At 4th level, an ancient guardian gains a +4 bonus on saves against enchantments. This ability
replaces resist nature's lure.

## Undo Artifice (Sp) {#undo-artifice}

At 13th level, an ancient guardian gains the ability to reduce a nonliving item to its component raw
materials. This acts as the spell _[polymorph any object](ref/spell/polymorph-any-object)_, but
works on magical or nonmagical nonliving objects. The duration is always permanent. Unlike
_[polymorph any object](ref/spell/polymorph-any-object)_, this ability can't be used to mimic the
effects of other spells. Items subject to this effect receive a Fortitude saving throw to negate the
effect (DC = 10 + 1/2 the ancient guardian's druid level + her Wisdom modifier). Magic items receive
a circumstance bonus on this save equal to +1 for every 5,000 gp of the item's value. An ancient
guardian can use undo artifice a number of times per day equal to her Wisdom modifier. This ability
replaces a thousand faces.
