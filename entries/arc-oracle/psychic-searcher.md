+++
id = "ref/arc-oracle/psychic-searcher"
kind = "archetype"
title = "Psychic Searcher"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Psychic%20Searcher"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychic_searcher", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "advanced-class-guide"
page = "106"

[fields]
kind = "archetype"
features = [
  { anchor = "inspiration", level = 2 },
  { anchor = "psychic-talent", level = 3 },
]
trades = [
  { replaces = "Mystery bonus spells at these levels", feature = "mystery", levels = [4, 6, 8, 12, 16, 18], power = "bonus spells" },
  { replaces = "Mystery spell gained at 2nd level", feature = "mystery", levels = [2], power = "bonus spells", by = ["inspiration"] },
  { replaces = "Revelation gained at 3rd level", feature = "revelation", levels = [3], by = ["psychic-talent"] },
  { alters = "Revelations gained after 3rd level", feature = "revelation", levels = [7, 11, 15, 19], by = ["psychic-talent"] },
]
+++

A psychic searcher is devoted to revealing the hidden within the world around her by sensing and
communing with residual mental energy, haunts, and fragments of living spirits that can dwell in
objects or rooms.

## Bonus Spells {#bonus-spells}

_Augury_ (4th), _locate object_ (6th), _divination_ (8th), _find the path_ (12th), _discern
location_ (16th), _foresight_ (18th). These bonus spells replace the oracle's normal mystery bonus
spells at these levels.

## Inspiration (Ex) {#inspiration}

At 2nd level, a psychic searcher gains an inspiration pool, as the
[investigator](ref/class/investigator) class ability. A psychic searcher uses her oracle level as
her investigator level to determine the effects of this ability. She gains free uses of inspiration
on Diplomacy, Knowledge (arcana, history, local, nobility, planes, religion), and Sense Motive skill
checks without spending a use of inspiration, provided she's trained in that skill. A psychic
searcher's inspiration pool refreshes each day, usually when she refreshes her spells. A psychic
searcher's inspiration pool is based on her Charisma modifier, not her Intelligence modifier. This
ability replaces the mystery spell gained at 2nd level.

## Psychic Talent (Su) {#psychic-talent}

At 3rd level, a psychic searcher's mastery of her supernatural insight grows, granting her a new
investigator talent from the following list:
[amazing inspiration](ref/invtalent/amazing-inspiration),
[eidetic recollection](ref/invtalent/eidetic-recollection), [empathy](ref/invtalent/empathy),
[inspired alertness](ref/invtalent/inspired-alertness), [item lore](ref/invtalent/item-lore),
[perceptive tracking](ref/invtalent/perceptive-tracking) (except using Sense Motive instead of
Perception or Survival), [rogue talent](ref/invtalent/rogue-talent) (only for
[hard to fool](ref/talent/hard-to-fool)), and
[tenacious inspiration](ref/invtalent/tenacious-inspiration). Whenever a psychic searcher can select
a new revelation, she can instead select an investigator or rogue talent from the above list. This
ability replaces the revelation gained at 3rd level.

## Recommended Mysteries {#recommended-mysteries}

[Ancestor](ref/mystery/ancestor), [lore](ref/mystery/lore), [nature](ref/mystery/nature).
