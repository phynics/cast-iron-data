+++
id = "ref/spell/shield-of-the-dawnflower-greater"
kind = "spell"
title = "Greater Shield of the Dawnflower"
aon = "SpellDisplay.aspx?ItemName=Shield%20of%20the%20Dawnflower%2C%20Greater"
source_ids = ["inner-sea-world-guide", "gods-and-magic", "inner-sea-gods"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shield_of_the_dawnflower_greater", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/shield-of-the-dawnflower" },
]
[[sources]]
publication = "inner-sea-gods"
page = "240"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire", "good", "light"]
levels = [
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Skald", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Bard, Cleric, Magus, Oracle, Skald
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Target: you
Duration: 1 round/level
Saving throw: see text
Spell resistance: no
Descriptors: fire, good, light
:::

### Greater Shield of the Dawnflower

You create a disk of sunlight on one arm. Any creature that strikes you with a melee attack deals
normal damage, but also takes 1d6 points of damage + 1 point per caster level. Half of this damage
is fire damage and half is holy damage (as the spell [flame strike](ref/spell/flame-strike)). An
undead creature or a creature particularly vulnerable to light that hits you instead takes 2d6
points of damage +1 point per caster level. Creatures with reach weapons are not subject to this
damage if they attack you. The shield provides illumination equivalent to a
[daylight](ref/spell/daylight) spell. You can have only one instance of this spell in effect at a
time. It does not stack with similar damaging aura spells such as fire shield or shield of the
Dawnflower.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
