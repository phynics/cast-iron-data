+++
id = "ref/arc-sorcerer/umbral-scion"
kind = "archetype"
title = "Umbral Scion"
aon = "ArchetypeDisplay.aspx?FixedName=Sorcerer%20Umbral%20Scion"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "umbral_scion", path = "json/archetypes_sorcerer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/sorcerer" },
]
[[sources]]
publication = "blood-of-shadows"
page = "19"

[fields]
kind = "archetype"
features = [
  { anchor = "diminished-spellcasting", level = 1 },
  { anchor = "shrouded-spells" },
  { anchor = "encroaching-darkness", level = 1 },
  { anchor = "potent-shadows", level = 7 },
  { anchor = "crippling-darkness", level = 13 },
]
trades = [
  { replaces = "Shadowstrike bloodline power", feature = "bloodline", levels = [1], power = "bloodline power", by = ["encroaching-darkness"] },
  { replaces = "7th-level bloodline feat", feature = "bloodline", levels = [7], power = "bloodline feat", by = ["potent-shadows"] },
  { replaces = "13th-level bloodline feat", feature = "bloodline", levels = [13], power = "bloodline feat", by = ["crippling-darkness"] },
  { alters = "Spellcasting", feature = "spells", by = ["diminished-spellcasting"] },
]
+++

Umbral scions are sorcerers who are able to expertly control their especially potent
[shadow](ref/sorcbloodline/shadow) heritage. The majority of umbral sorcerers hail from the
Darklands.

## Bloodline {#bloodline}

An umbral scion must have the shadow bloodline.

## Diminished Spellcasting {#diminished-spellcasting}

An umbral scion can cast one fewer spell per day of each level than normal. If this reduces the
number to 0, she can cast spells of that level only if her Charisma score grants her
[bonus spells](ref/rule/determine-bonuses) of that level.

This ability alters the sorcerer's spellcasting.

## Shrouded Spells (Su) {#shrouded-spells}

An umbral scion is enveloped by wisps of shadow whenever she casts a spell. The DC to identify
spells cast by an umbral scion increases by 2. If the spell is being cast within an area of
[dim light](ref/rule/vision-and-light) or darkness, the DC increases by 5 instead.

## Encroaching Darkness (Su) {#encroaching-darkness}

An umbral scion is capable of influencing light around her. As a standard action, she can produce a
10-foot-radius veil centered on a creature or object within 30 feet. This veil decreases the
[light level](ref/rule/vision-and-light) by one step and remains for a number of rounds equal to the
sorcerer's Charisma modifier. At 7th level, the veil increases to a 30-foot radius. At 8th level,
the veil decreases the light level by two steps. If the light level is decreased past darkness, the
veil is treated as _[deeper darkness](ref/spell/deeper-darkness)_. At 14th level, the veil increases
to 60 feet and grants any creature within it [cover](ref/rule/cover) (even against senses normally
able to penetrate total darkness, such as the [see in darkness](ref/umr/see-in-darkness) ability).
An umbral scion can use this ability a number of times per day equal to 3 + her Charisma modifier.

This ability replaces the shadowstrike bloodline power.

## Potent Shadows (Su) {#potent-shadows}

At 7th level, when an umbral scion casts a spell of the
[shadow subschool](ref/spelldef/shadow-subschool) or a spell with the
[darkness](ref/spelldef/darkness) or [shadow descriptor](ref/spelldef/shadow-descriptor) within an
area of dim light or darkness, she treats her caster level as 1 higher. Only the sorcerer herself
needs to be in dim light or darkness. This bonus increases by 1 every 4 sorcerer levels beyond 7th
she has to a maximum of +4 at 19th level.

This ability replaces the 7th-level bloodline feat.

## Crippling Darkness (Su) {#crippling-darkness}

At 13th level, when an umbral scion targets a creature within an area of dim light or darkness with
a spell of the shadow subschool or a spell with the darkness or shadow descriptor, the DC for the
spell increases by 1. This bonus increases by 1 at 18th level.

This ability replaces the 13th-level bloodline feat.
