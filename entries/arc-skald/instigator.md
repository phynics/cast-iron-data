+++
id = "ref/arc-skald/instigator"
kind = "archetype"
title = "Instigator"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "instigator", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "49"

[fields]
kind = "archetype"
replaces = ["Spell kenning", "Dirge of doom", "Lore master"]
+++

The instigator influences the will of the people, turning them toward his own purposes. Regardless
of whether what the instigator says is true or not, he inflames emotions in others and suspends
their reason. Instigators are often revolutionaries, political or otherwise, but they might also be
warmongering firebrands or wicked souls who spread prejudice against others.

**Raging Song (Su)**

**Info:** An instigator gains the following _raging songs._

**Song of Rabble-Rousing (Sp)**

**Ability:** The instigator can perform for 1 full round and spend 4 rounds of _raging song._ This
affects those who hear the song for up to 1 hour as per [enthrall](ref/spell/enthrall).

**Gained:** At 5th Level

**Replaces:** Spell kenning

**Song of Riot (Sp, Su)**

**Ability:** He can use this performance on all targets with fewer than 4 Hit Dice and a Wisdom
score lower than 16 who are currently _enthralled,_ without disrupting the
_[enthrall](ref/spell/enthrall)_ effect (even if a creature succeeds at its saving throw). This
ability requires a **standard action** to activate and costs 4 additional rounds of _raging song._

**Flavor:** The instigator can fill the hearts of his listeners with hatred and rouse them into a
frenzy.

**Gained:** At 10th Level

**Replaces:** Dirge of doom

**Special:** Enthralled creatures must each attempt a new saving throw against an effect that
functions as the [foster hatred](ref/spell/foster-hatred) spell, except that, unlike with the spell,
the instigator is free to choose subgroups, organizations, religions, or the like regardless of the
targets' races. Creatures that fail the saving throw or choose to forego it also gain the effects of
the instigator's _raging song_ whenever they attack the target of their hatred, for as long as the
_[foster hatred](ref/spell/foster-hatred)_ effect lasts; however, they do not gain the effects of
the instigator's rage powers when they're under the effects of _raging song_ in this way.

**Revolutionary Heart (Su)**

**Ability:** Once per day, when he fails a saving throw against a compulsion effect, he can attempt
another saving throw after 1 time increment (1 round if the effect is measured in rounds, 1 minute
if the effect is measured in minutes, 10 minutes if the spell is measured in 10-minute increments,
and so on).

**Flavor:** An instigator's tumultuous mastery of demagoguery and revolution makes it difficult for
others' compulsions to sway him.

**Gained:** At 7th Level

**Replaces:** Lore master
