+++
id = "ref/arc-paladin/martyr"
kind = "archetype"
title = "Martyr"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Martyr"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "martyr", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "horror-adventures"
page = "64"

[fields]
kind = "archetype"
features = [
  { anchor = "stigmata", level = 1 },
  { anchor = "see-no-evil-hear-no-evil", level = 2 },
  { anchor = "aura-mastery" },
  { anchor = "aura-of-health", level = 3 },
  { anchor = "martyr-s-mercy", level = 3 },
]
trades = [
  { replaces = "Smite evil", feature = "smite-evil", by = ["stigmata"] },
  { replaces = "Divine grace", feature = "divine-grace", by = ["see-no-evil-hear-no-evil"] },
  { replaces = "Divine health", feature = "divine-health", by = ["aura-of-health"] },
  { alters = "Aura of courage", feature = "aura-of-courage", by = ["aura-mastery"] },
  { alters = "aura of resolve", feature = "aura-of-resolve", by = ["aura-mastery"] },
  { alters = "aura of righteousness", feature = "aura-of-righteousness", by = ["aura-mastery"] },
  { alters = "Lay on hands", feature = "lay-on-hands", by = ["martyr-s-mercy"] },
  { alters = "mercy", feature = "mercy", by = ["martyr-s-mercy"] },
]
+++

Every paladin's code instructs him to put the welfare of others before his own, but some paladins
take this farther than most, shouldering the blackest suffering of the world onto themselves in
order to help others and inspiring their allies to achieve heights of valor rather than seeking the
glory for themselves.

## Stigmata {#stigmata}

As a standard action, the martyr can chant hymns of faith and cause bleeding stigmata to visibly
appear on his body; at 7th level, he can manifest stigmata as a move action, and at 13th level, he
can do so as a swift action. He can use this ability a number of rounds per day equal to 4 + his
Charisma modifier at 1st level, plus 1 additional round per day for each level beyond 1st. While his
stigmata are active, he takes 1 point of [bleed](ref/umr/bleed) damage, which automatically ceases
when he ends this ability but otherwise does not relent, even in the face of magical healing or Heal
checks. His stigmata assist his allies, duplicating the effect of the
[countersong](ref/performance/countersong), [distraction](ref/performance/distraction), or
[inspire courage](ref/performance/inspire-courage) bardic performance of a bard of his paladin
level, though both countersong and
[distraction](ref/carried/bestiary/rules/universal-monster-rules/distraction) use Heal skill checks
instead of Perform skill checks. At 10th level, he can choose to duplicate the effects of
[inspire greatness](ref/performance/inspire-greatness). At 16th level, he can choose to duplicate
the effects of [inspire heroics](ref/performance/inspire-heroics).

This ability replaces smite evil.

## See No Evil, Hear No Evil (Su) {#see-no-evil-hear-no-evil}

At 2nd level, the martyr and all allies within 20 feet of him gain a +4 morale bonus on saving
throws against bardic performance, sonic effects, language-dependent effects, and
[gaze](ref/umr/gaze) attacks. This ability functions only when the martyr is conscious.

This ability replaces divine grace.

## Aura Mastery (Su) {#aura-mastery}

The martyr's aura of courage, aura of resolve, and aura of righteousness have a radius of 20 feet
instead of 10 feet, but the martyr does not gain immunity to fear, charms, or compulsions from those
abilities.

This ability alters aura of courage, aura of resolve, and aura of righteousness.

## Aura of Health (Su) {#aura-of-health}

At 3rd level, the martyr and all allies within 20 feet of him gain a +4 morale bonus on saving
throws against diseases. This ability functions only when the martyr is conscious.

This ability replaces divine health.

## Martyr's Mercy (Su) {#martyr-s-mercy}

At 3rd level, a martyr can apply any of the mercies for which he qualifies based on his paladin
level to his lay on hands, even if he didn't select that mercy (or its prerequisites). However, when
he uses a mercy he didn't select, he transfers the condition to himself for the remaining duration
(ignoring any immunity he might have to the condition), and he can't use this ability if he already
has that condition. If he transfers a condition to himself in this way, he can't remove it from
himself with a personal-only ability. The martyr can use lay on hands on any ally within 30 feet,
rather than needing to touch the ally, but using lay on hands on himself is a standard action, not a
swift action.

This ability alters lay on hands and mercy.
