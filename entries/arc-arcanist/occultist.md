+++
id = "ref/arc-arcanist/occultist"
kind = "archetype"
title = "Occultist"
aon = "ArchetypeDisplay.aspx?FixedName=Arcanist%20Occultist"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "occultist", path = "json/archetypes_arcanist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/arcanist" },
]
[[sources]]
publication = "advanced-class-guide"
page = "78"

[fields]
kind = "archetype"
features = [
  { anchor = "planar-spells" },
  { anchor = "conjurer-s-focus", level = 1 },
  { anchor = "planar-contact", level = 7 },
  { anchor = "perfect-summoner", level = 20 },
]
trades = [
  { replaces = "The arcanist exploit gained at 1st level", feature = "arcanist-exploits", levels = [1], by = ["conjurer-s-focus"] },
  { replaces = "The arcanist exploit gained at 7th level", feature = "arcanist-exploits", levels = [7], by = ["planar-contact"] },
  { replaces = "Magical supremacy", feature = "magical-supremacy", by = ["perfect-summoner"] },
]
+++

Not all arcanists peer inward to discern the deepest secrets of magic. Some look outward, connecting
with extraplanar creatures and bartering for secrets, power, and favor.

## Planar Spells {#planar-spells}

An occultist adds all _[planar ally](ref/spell/planar-ally)_ spells to her spell list (using her
arcanist level as the cleric level), and treats _[plane shift](ref/spell/plane-shift)_ as a
5th-level arcanist spell.

## Conjurer's Focus (Sp) {#conjurer-s-focus}

An occultist can spend 1 point from her arcane reservoir to cast
_[summon monster I](ref/spell/summon-monster-1)_. She can cast this spell as a standard action and
the summoned creatures remain for 1 minute per level (instead of 1 round per level). At 3rd level
and every 2 levels thereafter, the power of this ability increases by one spell level, allowing her
to summon more powerful creatures (to a maximum of _[summon monster IX](ref/spell/summon-monster-9)_
at 17th level), at the cost of an additional point from her arcane spell reserve per spell level. An
occultist cannot have more than one _summon monster_ spell active in this way at one time. If this
ability is used again, any existing _summon monster_ immediately ends. This ability replaces the
arcanist exploit gained at 1st level.

## Planar Contact (Sp) {#planar-contact}

At 7th level, an occultist can cast _[augury](ref/spell/augury)_ once per day and
_[contact other plane](ref/spell/contact-other-plane)_ once per week, using her arcanist level as
her caster level. This ability replaces the arcanist exploit gained at 7th level.

## Perfect Summoner {#perfect-summoner}

At 20th level, an occultist can use her conjurer's focus without spending points from her arcane
reservoir, and the creatures summoned last until dismissed. This ability replaces magical supremacy.
