+++
id = "ref/arc-investigator/psychic-detective"
kind = "archetype"
title = "Psychic Detective"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Psychic%20Detective"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychic_detective", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "occult-adventures"
page = "119"

[fields]
kind = "archetype"
features = [
  { anchor = "spells", level = 1 },
  { anchor = "psychic-meddler", level = 2 },
  { anchor = "phrenic-dabbler", level = 3 },
  { anchor = "investigator-talents", level = 3 },
]
trades = [
  { replaces = "Alchemy", feature = "alchemy", by = ["spells"] },
  { replaces = "Poison lore", feature = "poison-lore", by = ["psychic-meddler"] },
  { replaces = "poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["psychic-meddler"] },
  { replaces = "swift alchemy", feature = "swift-alchemy", by = ["psychic-meddler"] },
  { replaces = "poison immunity", feature = "poison-resistance", levels = [11], by = ["psychic-meddler"] },
  { replaces = "Investigator talent gained at 3rd level", feature = "investigator-talent", levels = [3], by = ["phrenic-dabbler"] },
  { alters = "Investigator talents", feature = "investigator-talent", by = ["investigator-talents"] },
  { alters = "Class skills" },
]
+++

A psychic detective supplements her keen insight with occult skill to unravel mysteries both
ordinary and supernatural.

## Class Skills {#class-skills}

The psychic detective does not receive Acrobatics, Climb, or Perform as class skills. This alters
the investigator's class skills.

## Spells {#spells}

A psychic detective casts psychic spells drawn from the psychic class spell list (see page 69) and
augmented by a select set of additional spells (see Psychic Detective Spells on page 120). Only
spells from the psychic class spell list of 6th level or lower and psychic detective spells are
considered to be part of the psychic detective's spell list. If a spell appears on both the psychic
detective and psychic class spell lists, the psychic detective uses the spell level from the psychic
detective spell list. She can cast any spell she knows without preparing it ahead of time. To learn
or cast a spell, a psychic detective must have an Intelligence score equal to at least 10 + the
spell's level. The saving throw DC against a psychic detective's spell is 10 + the spell's level +
the psychic detective's Intelligence modifier.

Like other spellcasters, a psychic detective can cast only a certain number of spells of each spell
level per day. She knows the same number of spells and receives the same number of spells slots per
day as a [bard](ref/class/bard) of her investigator level, and knows and uses 0-level knacks as a
bard uses cantrips. In addition, she receives [bonus spells per day](ref/rule/determine-bonuses) if
she has a high Intelligence score (see Table 1–3 on page 17 of the _Core Rulebook_).

At 5th level and every 3 levels thereafter, a psychic detective can choose to learn a new spell in
place of one she already knows, using the same rules as a bard. In effect, the psychic detective
loses the old spell in exchange for the new one. The new spell's level must be the same as that of
the spell being exchanged, and it must be at least 1 level lower than the highest-level spell the
psychic detective can cast.

A psychic detective need not prepare her spells in advance. She can cast any psychic detective spell
she knows at any time, assuming she has not yet used up her allotment of spells per day for the
spell's level.

### Psychic Detective Spells {#psychic-detective-spells}

A psychic detective has the following spells on her spell list, in addition to psychic spells of 6th
level or lower.

1st—_Detect chaos_, _detect evil_, _detect good_, _detect law_, _find traps_.

3rd—_Calm spirit_, _daylight_.

4th—_Modify memory_.

6th—_Banishment_, _moment of prescience_, _scrying (greater)_.

This ability replaces alchemy.

## Psychic Meddler (Su) {#psychic-meddler}

At 2nd level, a psychic detective receives a +1 bonus on saves against psychic spells and
[spell-like abilities](ref/umr/spell-like-abilities). This bonus increases by 1 at 5th level and
every 3 levels thereafter, to a maximum of +6 at 17th level. Starting at 5th level, the psychic
investigator adds [half](ref/misc/fractions-and-rounding) this bonus on caster level checks to
dispel psychic effects. This ability replaces poison lore, poison resistance, swift alchemy, and
poison immunity.

## Phrenic Dabbler (Su) {#phrenic-dabbler}

At 3rd level, a [psychic](ref/class/psychic) detective gains a small pool of phrenic points equal to
1/2 her psychic detective level, as well as one phrenic amplification, as the psychic class feature.
This does not allow the psychic detective to qualify for the
[Extra Amplification](ref/feat/extra-amplification) feat. This ability replaces the investigator
talent gained at 3rd level.

## Investigator Talents {#investigator-talents}

A psychic detective selects investigator talents as normal, except she cannot select the
[alchemist discovery](ref/invtalent/alchemist-discovery) investigator talent. She can select the
[Expanded Phrenic Pool](ref/feat/expanded-phrenic-pool) feat as a discovery even though she doesn't
meet that feat's prerequisites, and she can select an extra phrenic amplification once as a
discovery. The following investigator talents, which can be found on pages 32–34 of the _Pathfinder
RPG Advanced Class Guide_, complement the psychic detective archetype:
[confusing strike](ref/invtalent/confusing-strike), [device talent](ref/invtalent/device-talent),
[effortless aid](ref/invtalent/effortless-aid), [hidden agendas](ref/invtalent/hidden-agendas),
[inspired intelligence](ref/invtalent/inspired-intelligence), [item lore](ref/invtalent/item-lore),
and [unconventional inspiration](ref/invtalent/unconventional-inspiration). This ability alters
investigator talents.
