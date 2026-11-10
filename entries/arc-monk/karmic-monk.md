+++
id = "ref/arc-monk/karmic-monk"
kind = "archetype"
title = "Karmic Monk"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "karmic_monk", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "occult-adventures"
page = "122"

[fields]
kind = "archetype"
replaces = ["Stunning fist", "Still mind", "7th- and 10th-level ki pool abilities", "Improved evasion", "The slow fall improvement; it remains at 70 feet"]
alters = ["Alignment requirement", "Slow fall", "Perfect self"]
replaces_features = ["stunning-fist", "still-mind", "improved-evasion"]
alters_features = ["slow-fall", "perfect-self"]
+++

A karmic monk contemplates the myriad harmonies that guide existence. He learns to use the
disharmony in others against them, and to alter his own inner harmonies to exploit weaknesses in his
opponents' defenses.

**Alignment**

**Alters:** Alignment requirement

**Info:** A karmic monk must be true neutral or of any lawful alignment.

**Gained class skills:** diplo

**Lost class skills:** intm

**Karmic Strike (Su)**

**Gained:** At 1st Level

**Passive:** A karmic monk gains bonuses against creatures that attack him first. If a creature the
karmic monk has not attacked within the past 24 hours makes an attack roll against the karmic monk
or casts an offensive spell that affects the karmic monk, the karmic monk receives a +2 bonus on
attack rolls and damage rolls against that creature. If the karmic monk hits such a target, this
bonus lasts until the end of the karmic monk's turn (or until the beginning of the karmic monk's
next turn, if it isn't his turn). Otherwise, the bonus against a particular creature lasts for 1
minute after the creature's last attack against the karmic monk.

**Replaces:** Stunning fist

**Balanced Mind (Su)**

**Gained:** At 3rd Level

**Passive:** A karmic monk receives a +2 bonus on saving throws against effects with the chaos,
evil, good, or law subtype. He also receives this bonus against the abilities and effects of
creatures of the listed subtypes.

**Replaces:** Still mind

**Ki Pool (Su)**

**Gained:** At 7th Level

**Passive:** When a karmic monk makes unarmed strikes, they're treated as chaotic, evil, good, and
lawful.

**Replaces:** 7th- and 10th-level _ki pool_ abilities

**Harmony (Su)**

**Immediate:** A karmic monk can shift his alignment by one step for the purpose of all effects
dependent on alignment until the beginning of his next turn. This does not actually alter the karmic
monk's alignment.

**Gained:** At 9th Level

**Replaces:** Improved evasion

**Karmic Disruption (Su)**

**Gained:** At 16th Level

**Replaces:** The _slow fall_ improvement; it remains at 70 feet

**Special:** This attack disrupts only alignment components of
[damage reduction](ref/rule/damage-reduction), not any other components; for example, DR/cold iron
and good becomes DR/cold iron.

**Swift:** A karmic monk can spend 1 point from his _ki pool_ to add 1d6 points of damage to his
unarmed strikes against creatures of either chaotic, evil, good, or lawful alignment for 1 round.
This stacks with other abilities that deal damage based on alignment. He cannot alter his alignment
choice until the next time he uses this ability. Creatures that are of the appropriate alignment and
are struck by this attack must succeed at a Will save (DC = 10 + 1/2 the karmic monk's class level +
the karmic monk's Wisdom modifier) or lose any [damage reduction](ref/rule/damage-reduction) based
on alignment for a number of rounds equal to the karmic monk's Wisdom modifier (minimum 1 round). A
creature that succeeds at this save is immune to having its damage reduction disrupted by that
karmic monk for 24 hours.

**Slow Fall**

**Ability:** _Slow fall_ now reduces your fall damage by 80 feet.^1^

**Alters:** Slow fall

**Gained:** At 18th Level

**Harmonic Self**

**Ability:** A karmic monk is truly in tune with the harmonic balance of the universe. He gains the
abilities of _perfect self,_ except that instead of DR 10/chaotic, he gains DR 10 that is overcome
only by attacks that do not count as chaotic, evil, good, or lawful.

**Alters:** Perfect self

**Gained:** At 20th Level

^1^ The original source book presents this as replacing the \*slow fall\* increase at 19th level,
but the ability actually increases at 18th level. This would mean that the ability would increase to
90 feet at 18th level, then revert down to 80 feet at 19th level, which would be strange. There is
no official errata confirming this, but the ability is presented above as if it was adjusted at 18th
level.
