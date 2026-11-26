+++
id = "ref/arc-spiritualist/exciter"
kind = "archetype"
title = "Exciter"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Exciter"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "exciter", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "horror-adventures"
page = "68"

[fields]
kind = "archetype"
features = [
  { anchor = "merged-phantom", level = 1 },
  { anchor = "rapture" },
  { anchor = "fast-movement", level = 1 },
  { anchor = "excitation", level = 2 },
  { anchor = "rapturous-rage", level = 10 },
  { anchor = "perfect-passion", level = 4 },
  { anchor = "overwhelming-excitement", level = 10 },
  { anchor = "greater-rapture", level = 12 },
]
trades = [
  { replaces = "6th-level phantom recall", feature = "phantom-recall", levels = [6], by = ["merged-phantom"] },
  { replaces = "Ability to manifest his phantom", by = ["rapture"] },
  { replaces = "Use emotional focus abilities that require a manifested phantom", by = ["rapture"] },
  { replaces = "Etheric tether", feature = "etheric-tether", by = ["fast-movement"] },
  { replaces = "Bonded senses", feature = "bonded-senses", by = ["excitation"] },
  { replaces = "10th-, 14th-, and 18th-level phantom recall", feature = "phantom-recall", levels = [10, 14, 18], by = ["rapturous-rage"] },
  { replaces = "spiritual bond", feature = "spiritual-bond", by = ["rapturous-rage"] },
  { replaces = "Spiritual interference", feature = "spiritual-interference", by = ["perfect-passion"] },
  { replaces = "Fused consciousness", feature = "fused-consciousness", by = ["overwhelming-excitement"] },
  { replaces = "Greater spiritual interference", feature = "greater-spiritual-interference", by = ["greater-rapture"] },
  { alters = "Phantom", feature = "phantom", by = ["merged-phantom"] },
  { alters = "emotional focus", feature = "phantom", power = "emotional focus", by = ["merged-phantom"] },
]
+++

Psychic magic draws upon the twin and sometimes opposed powers of thought and emotion, but an
exciter cares little for rationality. The phantom that accompanies him fills him with unbridled
exultation, as he lets feeling and passion rule and sharpen his mind and body into a glorious
fusion.

## Merged Phantom {#merged-phantom}

An exciter internalizes his phantom and merges it completely within his mind. He cannot fully
manifest his phantom outside of his own body in incorporeal or ectoplasmic form. Emotional focus
abilities that affect or require a manifested phantom are lost, except for any aura gained by the
phantom at 7th level; if the phantom gains an aura at 7th level, this aura functions despite the
phantom not being manifested, and is centered on the exciter.

This ability alters phantom and emotional focus and replaces the 6th-level phantom recall.

## Rapture (Su) {#rapture}

An exciter gains the ability to enter an ecstatic state in which he's consumed and overwhelmed by
his passions and driven into a fighting fury. This functions similarly to a
[bloodrager's](ref/class/bloodrager) bloodrage (_Pathfinder RPG_ _Advanced Class Guide_ 15),
treating his spiritualist level as his bloodrager level, though he doesn't qualify for feats or
other elements that require rage or bloodrage. When entering a rapture, the exciter loses all other
benefits from having his phantom confined in his consciousness (such as the
[Skill Focus](ref/feat/skill-focus) feats and bonus against mind-affecting effects), but he can
choose to exchange the normal +4 morale bonus to his Strength and Constitution scores normally
gained from bloodrage for a +4 morale bonus to his Dexterity and Charisma scores or a +2 morale
bonus to his Strength, Dexterity, Constitution, and Charisma scores. In addition to the fatigue for
ending a bloodrage, an exciter can't enter a rapture again for 1 minute after ending his last
rapture.

This ability replaces a spiritualist's ability to manifest his phantom and use emotional focus
abilities that require a manifested phantom.

## Fast Movement (Ex) {#fast-movement}

An exciter's land speed is faster than normal for his race by 10 feet. This benefit applies only
when he is wearing light armor, medium armor, or no armor and is not carrying a heavy load. This
doesn't stack with the [barbarian](ref/class/barbarian) ability of the same name.

This ability replaces etheric tether.

## Excitation (Su) {#excitation}

At 2nd level, when an exciter is in a rapture, each round he can choose to intensify his emotional
fury, expending 2 rounds of rapture instead of 1. When he uses excitation, he chooses one of the two
abilities that his emotional focus would normally grant to a manifested phantom, such as strength
focus and powerful strike for an [anger](ref/emotionalfocus/anger) phantom, or power from
[despair](ref/emotionalfocus/despair) and miserable strike for a despair phantom. He gains these
abilities until the beginning of his next turn. If the ability normally augments only a phantom's
slam attacks, it instead applies to the ectoplasmic tendrils that the spiritualist can sprout using
his ectoplasmic bonded manifestation.

This ability replaces bonded senses.

## Rapturous Rage {#rapturous-rage}

At 10th level and every 4 spiritualist levels thereafter, an exciter can select one rage power for
which he qualifies, treating his spiritualist level as his barbarian level for all purposes relating
to that particular rage power (he still doesn't qualify for the
[Extra Rage Power](ref/feat/extra-rage-power) feat or any similar abilities).

This ability replaces the 10th-, 14th-, and 18th-level phantom recall and spiritual bond.

## Perfect Passion (Su) {#perfect-passion}

At 4th level, an exciter can cast psychic spells with an emotion component (_Pathfinder RPG Occult
Adventures_ 144) even while in his rapture. He can cast these spells defensively and attempt
[concentration](ref/rule/concentration) checks for these spells without impairment, despite being in
a rapture. He also can attempt Charisma- and Intelligence-based skill checks related to psychic
spells with an emotion component while in his rapture. He cannot cast arcane or divine spells or
psychic spells that have a thought component while in a rapture.

This ability replaces spiritual interference.

## Overwhelming Excitement (Su) {#overwhelming-excitement}

At 10th level, an exciter can share the effects of his rapture with willing allies within 10 feet.
He must expend 2 additional rounds of his rapture each round for each ally sharing its effects. The
exciter's allies share all effects of the rapture except the rage powers; each ally must end its
turn within 10 feet of the exciter, or the effects of the rapture end for that ally and it becomes
[fatigued](ref/misc/fatigued).

Whenever he is not sharing the effects of his rapture with an ally, the exciter now retains the
benefits of his phantom in his consciousness even during rapture.

This ability replaces fused consciousness.

## Greater Rapture (Su) {#greater-rapture}

At 12th level, an exciter increases the morale bonus his rapture grants to each applicable ability
score by 2 and the morale bonus he gains on Will saves by 1. In addition, upon entering a rapture,
he can apply the effects of a single spiritualist spell he knows with an emotion component to
himself. The spell must have a range of touch or personal, and it must be a 1st- or 2nd-level spell.
For every 3 spiritualist levels he has beyond 12th, the maximum spell level of this spell increases
by 1. If he uses this ability to apply the effects of a spell again before the duration of the
previous spell expires, the previous spell ends immediately.

This replaces greater spiritual interference.
