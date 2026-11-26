+++
id = "ref/arc-samurai/sovereign-blade"
kind = "archetype"
title = "Sovereign Blade"
aon = "ArchetypeDisplay.aspx?FixedName=Samurai%20Sovereign%20Blade"
source_ids = ["legacy-of-dragons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sovereign_blade", path = "json/archetypes_samurai.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/samurai" },
]
[[sources]]
publication = "legacy-of-dragons"
page = "14"

[fields]
kind = "archetype"
features = [
  { anchor = "dogmatic-denial", level = 1 },
  { anchor = "golden-armor", level = 4 },
  { anchor = "sovereign-breath", level = 6 },
]
trades = [
  { replaces = "Mount", feature = "mount", by = ["dogmatic-denial"] },
  { replaces = "Mounted archer", feature = "mounted-archer", by = ["golden-armor"] },
  { replaces = "Bonus feats a samurai gained at 6th, 12th, and 18th level", feature = "bonus-feat", levels = [6, 12, 18], by = ["sovereign-breath"] },
]
+++

In Tian Xia, many samurai are tutored in the ways of honor using lessons that originate from
sovereign dragons and their dedication to safeguarding harmony.

## Alignment {#alignment}

A sovereign blade's alignment must be at least partially neutral. If the sovereign blade's alignment
is not partially neutral, she is treated as if she had violated her order's edicts each day until
her alignment is again partially neutral.

## Dogmatic Denial (Ex) {#dogmatic-denial}

A sovereign blade gains a +2 bonus on saving throws against spells with any of the following
descriptors that don't match part of the character's own alignment: chaotic, evil, good, or lawful.

This ability replaces mount.

## Golden Armor (Su) {#golden-armor}

At 4th level, a sovereign blade can spend one use of her resolve to cause her armor to become golden
for 1 round per class level, gaining energy resistance equal to 1/2 her samurai level against one
energy type of her choice.

This ability replaces mounted archer.

## Sovereign Breath (Sp) {#sovereign-breath}

At 6th level, the sovereign blade can issue forth an immense roar similar to the breath weapon of a
[sovereign dragon](ref/family/dragon-imperial-sovereign). This functions as
_[dragon's breath](ref/spell/dragons-breath)_, except it deals sonic damage in a 30-foot cone and
has a caster level equal to half the sovereign blade's samurai level. The sovereign blade can use
this ability once per day, plus one additional time per day at 12th and 18th levels.

This replaces the bonus feats a samurai gained at 6th, 12th, and 18th level.
