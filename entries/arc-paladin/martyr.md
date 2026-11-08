+++
id = "ref/arc-paladin/martyr"
kind = "archetype"
title = "Martyr"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "martyr", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]

[fields]
kind = "archetype"
replaces = ["Smite evil", "Divine grace", "Divine health"]
alters = ["Aura of courage", "aura of resolve", "aura of righteousness", "Lay on hands", "mercy"]
+++

**Sources:** Horror Adventures pg 64\
Every paladin's code instructs him to put the welfare of others before his own, but some paladins
take this farther than most, shouldering the blackest suffering of the world onto themselves in
order to help others and inspiring their allies to achieve heights of valor rather than seeking the
glory for themselves.

**Stigmata**

**At 10th Level:** He can choose to duplicate the effects of
[inspire greatness](ref/performance/inspire-greatness).

**At 13th Level:** He can manifest _stigmata_ as a **swift action**.

**At 16th Level:** He can choose to duplicate the effects of
[inspire heroics](ref/performance/inspire-heroics).

**At 7th Level:** He can manifest _stigmata_ as a **move action**.

**Gained:** At 1st Level

**Replaces:** Smite evil

**Standard:** The martyr can chant hymns of faith and cause bleeding stigmata to visibly appear on
his body. While his _stigmata_ are active, he takes 1 point of [bleed](ref/umr/bleed) damage, which
automatically ceases when he ends this ability but otherwise does not relent, even in the face of
magical healing or Heal checks. His _stigmata_ assist his allies, duplicating the effect of the
[countersong](ref/performance/countersong), [distraction](ref/performance/distraction), or
[inspire courage](ref/performance/inspire-courage) bardic performance of a bard of his paladin
level, though both _countersong_ and
_[distraction](ref/carried/bestiary/rules/universal-monster-rules/distraction)_ use Heal skill
checks instead of Perform skill checks.

**Usage:** paladin level + Charisma3 modifier rounds/day

**See No Evil, Hear No Evil (Su)**

**Gained:** At 2nd Level

**Passive:** The martyr and all allies within 20 feet of him gain a +4 morale bonus on saving throws
against bardic performance, sonic effects, language-dependent effects, and [gaze](ref/umr/gaze)
attacks.

**Replaces:** Divine grace

**Special:** This ability functions only when the martyr is conscious.

**Aura Mastery (Su)**

**Ability:** The martyr's _aura of courage, aura of resolve,_ and _aura of righteousness_ have a
radius of 20 feet instead of 10 feet, but the martyr does not gain immunity to fear, charms, or
compulsions from those abilities.

**Alters:** Aura of courage, aura of resolve, aura of righteousness

**Aura of Health (Su)**

**Gained:** At 3rd Level

**Passive:** The martyr and all allies within 20 feet of him gain a +4 morale bonus on saving throws
against diseases.

**Replaces:** Divine health

**Special:** This ability functions only when the martyr is conscious.

**Martyr's Mercy (Su)**

**Ability:** A martyr can apply any of the mercies for which he qualifies based on his paladin level
to his _lay on hands,_ even if he didn't select that mercy (or its prerequisites). However, when he
uses a mercy he didn't select, he transfers the condition to himself for the remaining duration
(ignoring any immunity he might have to the condition), and he can't use this ability if he already
has that condition. If he transfers a condition to himself in this way, he can't remove it from
himself with a personal-only ability.

**Alters:** Lay on hands, mercy

**Gained:** At 3rd Level

**Special:** The martyr can use _lay on hands_ on any ally within 30 feet, rather than needing to
touch the ally, but using _lay on hands_ on himself is a **standard action**, not a swift action.
