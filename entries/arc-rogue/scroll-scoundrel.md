+++
id = "ref/arc-rogue/scroll-scoundrel"
kind = "archetype"
title = "Scroll Scoundrel"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Scroll%20Scoundrel"
source_ids = ["pathfinder-society-field-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scroll_scoundrel", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "pathfinder-society-field-guide"
page = "27"

[fields]
kind = "archetype"
features = [
  { anchor = "fast-talker", level = 2 },
  { anchor = "adaptive-learning", level = 3 },
  { anchor = "pay-it-back", level = 4 },
  { anchor = "elusive-gambit", level = 6 },
  { anchor = "spot-weakness", level = 10 },
]
trades = [
  { replaces = "2nd-level rogue talent", feature = "rogue-talents", levels = [2], by = ["fast-talker"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["adaptive-learning"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["pay-it-back"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["elusive-gambit"] },
  { replaces = "The scroll scoundrel's 10th-level rogue talent", feature = "rogue-talents", levels = [10], by = ["spot-weakness"] },
]
+++

The scroll scoundrel is a rogue archetype that relies on cunning and quick wits to stay alive. He
excels in exploiting overconfidence and predictability, using knowledge he's gained from his
extensive research and field experience combined with hearsay and recent observations to react to
problems as soon as they arise with swift but unnaturally accurate guesswork. A scroll scoundrel is
often called upon by the Pathfinders to undertake missions where killing a foe isn't nearly as
important as humiliating them in public duels or similar conflicts. A scroll scoundrel has the
following class features.

## Fast Talker (Ex) {#fast-talker}

At 2nd level, a scroll scoundrel's penalty on [Bluff](ref/skill/bluff) checks that are unlikely,
farfetched, or impossible to achieve is reduced by 5. When he makes a
[Diplomacy](ref/skill/diplomacy) check to adjust a creature's starting attitude, he gains a +3
competence bonus on the skill check. This ability replaces the rogue's 2nd-level rogue talent.

## Adaptive Learning (Ex) {#adaptive-learning}

At 3rd level, a scroll scoundrel gains a +1 bonus on saving throws against abilities and spells he
has already successfully saved against within the past minute (even if the spells or abilities in
question were used by different creatures). This bonus increases by +1 when the scroll scoundrel
reaches 6th level, and by an additional +1 for every three levels thereafter, to a maximum of +6 at
18th level. This ability replaces trap sense.

## Pay It Back (Ex) {#pay-it-back}

At 4th level, a scroll scoundrel receives a +1 bonus on attack rolls and weapon damage rolls against
foes who made melee attacks against him in the previous round. This bonus increases to +2 at 10th
level. This ability replaces uncanny dodge.

## Elusive Gambit (Ex) {#elusive-gambit}

At 6th level, a scroll scoundrel's movement can leave a foe off-balance. If a scroll scoundrel
provokes an attack of opportunity by moving past an opponent and that opponent then misses with the
attack, that foe is considered to be [flat-footed](ref/rule/flat-footed) against the scroll
scoundrel's next melee attack, provided that melee attack comes within 1 round of the missed attack
of opportunity. This ability replaces improved uncanny dodge.

## Spot Weakness (Ex) {#spot-weakness}

At 10th level, a scroll scoundrel can discover a weakness in his enemy's defenses as a swift action.
His next successful hit in the same round ignores 5 points of the foe's
[damage reduction](ref/rule/damage-reduction) or [hardness](ref/umr/hardness). At 15th level, he
ignores the first 10 points, and at 20th level, the first 15 points. If the attack deals any sneak
attack damage, he ignores all of the foe's [damage reduction](ref/rule/damage-reduction) or
[hardness](ref/umr/hardness) for that attack. He cannot use this ability on foes that are immune to
critical hits. This ability replaces the scroll scoundrel's 10th-level rogue talent.
