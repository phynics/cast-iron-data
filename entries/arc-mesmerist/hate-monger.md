+++
id = "ref/arc-mesmerist/hate-monger"
kind = "archetype"
title = "Hate-Monger"
aon = "ArchetypeDisplay.aspx?FixedName=Mesmerist%20Hate-Monger"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hate_monger", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]
[[sources]]
publication = "horror-adventures"
page = "61"

[fields]
kind = "archetype"
features = [
  { anchor = "mental-manipulator", level = 1 },
  { anchor = "insidious-hatred", level = 3 },
  { anchor = "xenophobe", level = 5 },
  { anchor = "out-for-blood", level = 7 },
  { anchor = "insidious-emotions", level = 11 },
]
trades = [
  { replaces = "Consummate liar", feature = "consummate-liar", by = ["mental-manipulator"] },
  { replaces = "Mental potency", feature = "mental-potency", by = ["xenophobe"] },
  { replaces = "manifold tricks", feature = "manifold-tricks", by = ["xenophobe"] },
  { replaces = "7th-level bold stare", feature = "bold-stare", levels = [7], by = ["out-for-blood"] },
  { replaces = "Glib lie", feature = "glib-lie", by = ["insidious-emotions"] },
  { alters = "Mesmerist tricks", feature = "mesmerist-tricks", by = ["mental-manipulator"] },
  { alters = "Touch treatment", feature = "touch-treatment", by = ["insidious-hatred"] },
]
+++

Hate-mongers are xenophobic and judgmental rabblerousers who whip up mobs against enemies real or
imagined.

## Alignment {#alignment}

A hate-monger must be of a nongood alignment. A hate-monger who becomes good cannot gain new levels
as a mesmerist but retains all his class abilities.

## Mental Manipulator (Ex) {#mental-manipulator}

A hate-monger masters a broad repertoire of emotional corruption. At 1st level, he adds one spell
from the 1st-level spells below to his spells known. When he would gain a new mesmerist trick, he
can learn additional spells instead, adding two of the following spells of a level he can currently
cast to his spells known: 1st—_cause fear, compel hostility_, _delusional pride_, _demand offering_,
_forbid action_, _lesser confusion_, _murderous command_, _scare, sow thought_; 2nd—_aversion_,
_paranoia_, _rage_, _unadulterated loathing_; 3rd—_confusion, crushing despair, curse of disgust_,
_fear, instant enemy_, _malicious spite_, _smug narcissism_, _spite_; 4th—_envious urge_, _feast on
fear_, _greater forbid action_, _modify memory_, _utter contempt_; 5th—_foe to friend_, _foster
hatred_, _song of discord, repress memory_, _unwilling shield_, _vengeful outrage_; 6th—_eyebite_,
_insanity_, _overwhelming presence_, _symbol of persuasion_.

When he casts a spell he learns in this way, he increases the duration as if his caster level were 1
higher. Starting at 5th level, the save DC is increased by 1 for creatures of his favored enemy
type.

This ability replaces consummate liar and alters mesmerist tricks.

## Insidious Hatred (Su) {#insidious-hatred}

At 3rd level, a hate-monger can sow hatred and strife under the pretense of assisting others. He can
use his touch treatment only on others, but as part of the action of using touch treatment, he can
cast any targeted spell from the mental manipulator list that does not have a range of "personal"
and has a casting time of 1 standard action or less, targeting only the creature that receives his
touch treatment. That creature doesn't realize the hate-monger has cast a spell, and considers any
manifestations to be part of the touch treatment. Other creatures notice as normal. The target
creature takes a -2 penalty on its saving throw and to its
[spell resistance](ref/rule/spell-resistance) against the spell.

This ability alters touch treatment.

## Xenophobe (Ex) {#xenophobe}

At 5th level, a hate-monger can choose one [favored enemy](ref/ability/favored-enemy), as per the
[ranger](ref/class/ranger) class feature. His favored enemy bonus begins at +2 and increases by 2
for every 4 mesmerist levels after 5th, but he does not gain additional favored enemies. His favored
enemy bonus also applies on Intimidate checks against his favored enemy.

This ability replaces mental potency and manifold tricks.

## Out for Blood (Ex) {#out-for-blood}

At 7th level, when a creature takes extra damage from the hate-monger's painful stare, it also takes
1 point of [bleed](ref/rule/bleed) damage (or 1 point of bleed damage per 1d6 points of damage dealt
by the painful stare if the hate-monger damages the target himself). This bleed damage does not
stack with itself or other sources of bleed damage.

This ability replaces the 7th-level bold stare.

## Insidious Emotions (Su) {#insidious-emotions}

At 11th level, the power of a hate-monger's psychic hold becomes more difficult to detect or to
break. The DC of Sense Motive checks to notice if a creature is under the effects of his
enchantments with the emotion descriptor increases by 5 (if he also has the Subtle Enchantment feat,
the effects stack), as does the DC to identify his emotion spells. Magical divinations can detect
his emotion effects only if the caster succeeds at a caster level check (DC = 11 + the hate-monger's
mesmerist level) as if the affected creatures were the subject of
_[nondetection](ref/spell/nondetection)._

This ability replaces glib lie.
