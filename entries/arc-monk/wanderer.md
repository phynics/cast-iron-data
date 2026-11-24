+++
id = "ref/arc-monk/wanderer"
kind = "archetype"
title = "Wanderer"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Wanderer"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wanderer", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "advanced-race-guide"
page = "76"

[fields]
kind = "archetype"
features = [
  { anchor = "class-skills" },
  { anchor = "far-traveler", level = 1 },
  { anchor = "long-walk", level = 3 },
  { anchor = "light-step", level = 5 },
  { anchor = "inscrutable", level = 5 },
  { anchor = "wanderer-s-wisdom", level = 7 },
  { anchor = "disappear-unnoticed", level = 12 },
  { anchor = "free-step", level = 13 },
]
trades = [
  { replaces = "Bonus feat gained at 1st level", feature = "bonus-feat", levels = [1], by = ["far-traveler"] },
  { replaces = "Still mind", feature = "still-mind", by = ["long-walk"] },
  { replaces = "Slow fall", feature = "slow-fall", by = ["light-step"] },
  { replaces = "High jump", feature = "high-jump", by = ["inscrutable"] },
  { replaces = "Wholeness of body", feature = "wholeness-of-body", by = ["wanderer-s-wisdom"] },
  { replaces = "Abundant step", feature = "abundant-step", by = ["disappear-unnoticed"] },
  { replaces = "Diamond soul", feature = "diamond-soul", by = ["free-step"] },
]
+++

Some monks wander the world in humility to learn and to share wisdom and philosophy from their
teachers with those they meet, often aiding those who are in need. A wanderer has the following
class features.

## Class Skills {#class-skills}

The wanderer adds Diplomacy, Knowledge (geography), Knowledge (local), Linguistics, and Survival to
his list of class skills.

## Far Traveler (Ex) {#far-traveler}

At 1st level, the wanderer gains either one additional language known or proficiency in one exotic
or martial weapon. At 4th level and every four levels thereafter, the wanderer may gain an
additional language known or may retrain her weapon proficiency from this ability to a different
exotic or martial weapon. This ability replaces the bonus feat gained at 1st level.

## Long Walk (Ex) {#long-walk}

At 3rd level, the wanderer gains [Endurance](ref/feat/endurance) as a bonus feat, and the feat bonus
doubles when he makes Constitution checks because of a forced march. In addition, a wanderer gains a
+2 bonus on saving throws against spells and effects that cause exhaustion and fatigue. This ability
replaces still mind.

## Light Step (Su) {#light-step}

At 5th level, a wanderer leaves no trail and cannot be tracked, though he can leave a trail if
desired. By spending 1 point from his ki pool, he can use _[ant haul](ref/spell/ant-haul)_,
_[feather step](ref/spell/feather-step)_, _[pass without trace](ref/spell/pass-without-trace)_, or
_[tireless pursuit](ref/spell/tireless-pursuit)_ as a
[spell-like ability](ref/umr/spell-like-abilities) (with a caster level equal to his monk level).
This ability replaces slow fall.

## Inscrutable (Su) {#inscrutable}

At 5th level, the wanderer gains a supernatural air of mystery. The DC to gain information or
insight into the wanderer with Diplomacy, Knowledge skills, or Sense Motive increases by 5. In
addition, by spending 1 point from his ki pool, the wanderer gains
_[nondetection](ref/spell/nondetection)_ for 24 hours with a caster level equal to his monk level.
This ability replaces high jump.

## Wanderer's Wisdom (Ex) {#wanderer-s-wisdom}

At 7th level, the wanderer can dispense excellent advice in the form of philosophical proverbs and
parables. As a swift action, the wanderer can [inspire courage](ref/performance/inspire-courage) or
[inspire competence](ref/performance/inspire-competence) as a [bard](ref/class/bard) of his monk
level by spending 2 points from his ki pool. This affects one creature within 30 feet and lasts a
number of rounds equal to the wanderer's Wisdom modifier (minimum 1 round). This ability is
language-dependent. This ability replaces wholeness of body.

## Disappear Unnoticed (Ex) {#disappear-unnoticed}

At 12th level, the wanderer may use Stealth to hide even while being directly observed or when no
cover or concealment is available, as long as he is adjacent to at least one creature of his size or
larger, by spending 1 point from his ki pool. This effect lasts until the beginning of the
wanderer's next turn and may be continued in consecutive rounds by spending 1 ki point each round.
This ability replaces abundant step.

## Free Step (Su) {#free-step}

At 13th level, the wanderer gains continuous _[freedom of movement](ref/spell/freedom-of-movement)_
as a continuous [spell-like ability](ref/umr/spell-like-abilities)_._ This ability replaces diamond
soul.
