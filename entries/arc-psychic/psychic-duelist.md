+++
id = "ref/arc-psychic/psychic-duelist"
kind = "archetype"
title = "Psychic Duelist"
aon = "ArchetypeDisplay.aspx?FixedName=Psychic%20Psychic%20Duelist"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychic_duelist", path = "json/archetypes_psychic.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/psychic" },
]
[[sources]]
publication = "occult-adventures"
page = "107"

[fields]
kind = "archetype"
features = [
  { anchor = "psychic-duel-acumen", level = 4 },
  { anchor = "manifestation-amplifications", level = 7 },
  { anchor = "extended-effect" },
  { anchor = "faithful-creature" },
  { anchor = "punishing-thought-form" },
  { anchor = "reciprocal-defense", level = 1 },
  { anchor = "thought-made-real", level = 9 },
  { anchor = "expert-manifester", level = 17 },
]
trades = [
  { replaces = "4th-level discipline spell", feature = "psychic-discipline", power = "discipline spell", by = ["psychic-duel-acumen"] },
  { replaces = "7th-level phrenic amplification", feature = "phrenic-amplifications", levels = [7], by = ["reciprocal-defense"] },
  { replaces = "Telepathic bond", feature = "telepathic-bond", by = ["thought-made-real"] },
  { replaces = "Telepathy", feature = "telepathy", by = ["expert-manifester"] },
  { alters = "Phrenic amplifications", feature = "phrenic-amplifications", by = ["reciprocal-defense"] },
]
+++

Psychic duelists hone their mental powers for combat, much as warriors do with their blades. They
specialize in [psychic duels](ref/rule/psychic-duels), perfecting their thought-form creatures into
mighty weapons.

## Psychic Duel Acumen (Ex) {#psychic-duel-acumen}

At 4th level, a psychic duelist adds _[instigate psychic duel](ref/spell/instigate-psychic-duel)_ to
her list of spells known, and the save DC of any
_[instigate psychic duel](ref/spell/instigate-psychic-duel)_ spell she casts increases by 1.
Beginning at 6th level, she can also expend any unused psychic spell slot of 3rd level or higher to
cast _[instigate psychic duel](ref/spell/instigate-psychic-duel)_. If she does so, she uses the
level of the spell slot expended to determine the Will save DC. In addition, when the psychic
duelist sacrifices points from her phrenic pool to generate manifestation points for an offensive
manifestation, she uses d8s for damage dice instead of d4s. This ability replaces the 4th-level
discipline spell.

## Manifestation Amplifications {#manifestation-amplifications}

At 7th level, a psychic duelist gains a manifestation amplification instead of a phrenic
amplification; thereafter, whenever the psychic duelist gains a phrenic amplification, she can
select either a phrenic amplification or a manifestation amplification. A manifestation
amplification functions for a manifestation as a phrenic amplification does for a spell, with the
same restrictions. The manifestation being amplified is called the linked manifestation. Phrenic
pool points spent toward manifestation amplifications are separate from points sacrificed to
generate manifestation points. For example, a psychic duelist capable of casting 4th-level spells
(with a maximum of 4 MP per manifestation) could turn 4 points from her phrenic pool into MP and
spend 2 points on a manifestation amplification, expending a total of 6 points from her phrenic
pool.

## Extended Effect (Ex) {#extended-effect}

The psychic duelist can spend points from her phrenic pool to increase the duration of a condition
by 1 round per point spent. She can spend a maximum of 1 phrenic pool point in this way; this
maximum increases to 2 points at 11th level, to 3 points at 15th level, and to 4 points at 19th
level. If the target succeeds at its saving throw, this amplification has no effect (though the
points are still lost). This amplification can be linked only to offensive manifestations that
impose conditions.

## Faithful Creature (Ex) {#faithful-creature}

When she manifests a thought-form creature, the psychic duelist can spend 1 point from her phrenic
pool to give that creature the ability to persist even if it doesn't attack. She can concentrate to
maintain the creature as a swift action instead of as a full-round action, but the creature can
attack only if the psychic duelist concentrates as a full-round action. In addition, the psychic
backlash damage from that thought-form creature is halved. This amplification can be linked only to
thought-form creature manifestations.

## Punishing Thought-form (Ex) {#punishing-thought-form}

The psychic duelist can spend 1 point from her phrenic pool to increase the damage die size of an
offensive manifestation by one step (d4 to d6, d6 to d8, or d8 to d10). This amplification can be
linked only to offensive manifestations.

## Reciprocal Defense (Su) {#reciprocal-defense}

The psychic duelist can spend 1 point from her phrenic pool when using a defensive manifestation to
improve her defenses in the real world as well. Her physical body gains a +2 insight bonus to AC for
the number of rounds the defensive manifestation lasts, or for 1 round if the manifestation doesn't
have a duration. This bonus increases to +3 at 11th level and to +4 at 15th level. This
amplification can be linked only to defensive manifestations.

This ability replaces the 7th-level phrenic amplification and alters phrenic amplifications.

## Thought Made Real (Su) {#thought-made-real}

At 9th level, a psychic duelist can bring offensive manifestations directly into her foes' minds,
attacking with them without entering a psychic duel. When doing so, she can generate manifestation
points only by sacrificing a spell, not through any other methods. Using an offensive manifestation
in this way functions as casting a spell with a full-round-action casting time. Conditions imposed
by these offensive manifestations last for their full duration, even though the target isn't in a
psychic duel. The psychic duelist can use manifestation amplifications on offensive manifestations
created this way. Such offensive manifestations can't affect thought-form creatures. This is a
mind-affecting illusion (phantasm) effect. A thought-form creature manifested in this way is visible
only to its target. This ability replaces _telepathic bond_.

## Expert Manifester (Ex) {#expert-manifester}

At 17th level, a psychic duelist doesn't have to expend as many resources to create manifestations.
She gains 1 additional MP each time she creates a psychic manifestation, in addition to the MP she
gains by sacrificing resources. This doesn't increase the maximum number of points she can spend per
manifestation, but does allow her to create a manifestation costing 1 MP without sacrificing any
resources. This ability replaces telepathy.
