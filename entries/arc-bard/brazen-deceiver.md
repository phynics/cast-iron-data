+++
id = "ref/arc-bard/brazen-deceiver"
kind = "archetype"
title = "Brazen Deceiver"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Brazen%20Deceiver"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "brazen_deceiver", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "adventurers-guide"
page = "50"

[fields]
kind = "archetype"
features = [
  { anchor = "deceptive-tale", level = 1 },
  { anchor = "shameless-scoundrel", level = 1 },
  { anchor = "blatant-subtlety", level = 2 },
  { anchor = "invoke-vyriavaxus", level = 2 },
  { anchor = "devil-s-tongue", level = 5 },
]
trades = [
  { replaces = "Countersong", feature = "bardic-performance", power = "countersong", by = ["deceptive-tale"] },
  { replaces = "Distraction bardic performances", feature = "bardic-performance", power = "distraction", by = ["deceptive-tale"] },
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["shameless-scoundrel"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["blatant-subtlety"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["invoke-vyriavaxus"] },
  { replaces = "Lore master", feature = "lore-master", by = ["devil-s-tongue"] },
]
+++

Where other thieves use stealth or intimidation to achieve their goals, the brazen deceiver depends
on lies. The [Council of Thieves](ref/rule/aff-thieves) often sends brazen deceivers to acquire
blackmail materials, arrange the release of incarcerated agents, or otherwise manipulate events in
the Council's favor.

Brazen deceivers' techniques come from a dark source. During the reformation of the Council,
Sabriune and Aspexia acquired the shattered fragments of an ancient relic called the _Totemrix_,
which belonged to the long-deceased demon lord of shadows, Vyriavaxus. This particularly intrigued
Sabriune, for it was her demonic patron Nocticula who slew Vyriavaxus. Drawing upon Sabriune's
heretical faith, Aspexia's psychometric mastery, and Westcrown's lingering psychic trauma from an
oppressive shadow curse that plagued its nights for many years, the Council leaders were able to
coax remnants of power from the broken artifact. All brazen deceivers are imbued with a fragment of
that power during their initiation—not enough to damn a soul or shift alignment, but just enough to
give these bards access to the sinister energies they need to deceive.

## Deceptive Tale (Su) {#deceptive-tale}

A brazen deceiver learns the deceptive tale bardic performance, allowing him to weave magic into his
lies and imbue the most fantastic claims with the appearance of truth. While the brazen deceiver
maintains this performance, he takes half the normal penalty on Bluff checks for unlikely lies
(rounding down to -2). At 5th level, this effect also applies to Bluff checks for far-fetched lies,
and at 11th level, it applies to Bluff checks for impossible lies. Deceptive tale relies on audible
components.

This replaces the countersong and distraction bardic performances.

## Shameless Scoundrel (Ex) {#shameless-scoundrel}

A brazen deceiver adds [half](ref/misc/fractions-and-rounding) his level (minimum +1) on Bluff,
Disguise, and Stealth checks.

This ability replaces bardic knowledge.

## Blatant Subtlety (Ex) {#blatant-subtlety}

At 2nd level, a brazen deceiver has mastered the art of using magic without being detected. The
brazen deceiver gains [Spellsong](ref/feat/spellsong) as a bonus feat. Observers do not
automatically recognize his bardic performances as anything other than ordinary speech or
performance. Those specifically looking for abnormal effects must succeed at a Sense Motive check
(DC = 10 + half the brazen deceiver's bard level + the brazen deceiver's Charisma modifier) to
detect his performances.

This ability replaces well-versed.

## Invoke Vyriavaxus (Ex) {#invoke-vyriavaxus}

Westcrown suffered under the shadow curse for many years, and a brazen deceiver has a tiny piece of
that [darkness](ref/spell/darkness) lodged in his soul; as his skills increase, he learns to command
this shadowy power. A brazen deceiver adds the following spells to his bard spells known at the
listed class levels. At 2nd level, the brazen deceiver adds _[bleed](ref/spell/bleed)_ and
_[touch of fatigue](ref/spell/touch-of-fatigue)_ to his 0-level bard spells known. At 6th level, the
brazen deceiver adds _darkness_ and _[darkvision](ref/spell/darkvision)_ to his 2nd-level bard
spells known. At 10th level, he adds _[shadow conjuration](ref/spell/shadow-conjuration)_ and
_[shadow step](ref/spell/shadow-step)_ to his 4th-level bard spells known.

At 14th level, he adds _[shadow evocation](ref/spell/shadow-evocation)_ and
_[shadow walk](ref/spell/shadow-walk)_ to his 5th-level bard spells known. At 18th level, he adds
_greater shadow conjuration_ and _[greater shadow evocation](ref/spell/shadow-evocation-greater)_ to
his 6th-level bard spells known.

This ability replaces versatile performance.

## Devil's Tongue (Ex) {#devil-s-tongue}

At 5th level, a brazen deceiver beguiles others with astonishing skill.

This functions as the lore master ability, but its effects apply to Bluff checks instead of
Knowledge skill checks.

This ability replaces lore master.
