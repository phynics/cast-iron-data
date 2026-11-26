+++
id = "ref/arc-monk/hellcat"
kind = "archetype"
title = "Hellcat"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Hellcat"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hellcat", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "villain-codex"
page = "92"

[fields]
kind = "archetype"
features = [
  { anchor = "bonus-feat", level = 1 },
  { anchor = "hellcat-fury", level = 1 },
  { anchor = "torture-training", level = 2 },
  { anchor = "crucible-of-pain", level = 3 },
  { anchor = "hellcat-ki", level = 4 },
]
trades = [
  { replaces = "Weapon proficiencies", feature = "weapon-and-armor-proficiencies", power = "weapons" },
  { replaces = "Stunning fist", feature = "stunning-fist", by = ["hellcat-fury"] },
  { replaces = "fast movement", feature = "fast-movement", by = ["hellcat-fury"] },
  { replaces = "Evasion", feature = "evasion", by = ["torture-training"] },
  { replaces = "purity of body", feature = "purity-of-body", by = ["torture-training"] },
  { replaces = "improved evasion", feature = "improved-evasion", by = ["torture-training"] },
  { replaces = "Slow fall", feature = "slow-fall", by = ["crucible-of-pain"] },
  { replaces = "still mind", feature = "still-mind", by = ["crucible-of-pain"] },
  { replaces = "Wholeness of body", feature = "wholeness-of-body", by = ["hellcat-ki"] },
  { replaces = "diamond body", feature = "diamond-body", by = ["hellcat-ki"] },
  { alters = "Alignment requirements" },
  { alters = "Bonus feat", feature = "bonus-feat", by = ["bonus-feat"] },
  { alters = "Ki pool", feature = "ki-pool", by = ["hellcat-ki"] },
  { alters = "Class skills" },
]
+++

Monks of the hellcat sect follow the teachings of Asmodeus or another infernal power. Their brutal
training strips away their physical weaknesses, and their vicious fighting style is inspired by the
predatory techniques of the hellcat.

## Alignment {#alignment}

A hellcat must be lawful evil or lawful neutral. A hellcat who becomes lawful good or nonlawful
cannot gain new levels as a monk but retains all monk abilities.

This alters the monk's alignment requirements.

## Class Skills {#class-skills}

A hellcat gains Knowledge (planes) and Survival as class skills, instead of Craft, Knowledge
(history), Perform, and Profession.

This alters the monk's class skills.

## Weapon Proficiency {#weapon-proficiency}

A hellcat is proficient with the [club](ref/eq-weapon/club), crossbow (light or heavy),
[dagger](ref/eq-weapon/dagger), [kama](ref/eq-weapon/kama), [light mace](ref/eq-weapon/light-mace),
[nunchaku](ref/eq-weapon/nunchaku), [quarterstaff](ref/eq-weapon/quarterstaff), repeating crossbow
(light or heavy), [sai](ref/eq-weapon/sai), [shuriken](ref/eq-weapon/shuriken), and
[siangham](ref/eq-weapon/siangham). In addition to monk weapons and unarmed strikes, a hellcat can
use a [light mace](ref/eq-weapon/light-mace) to perform a flurry of blows.

This replaces the monk's weapon proficiencies.

## Bonus Feat {#bonus-feat}

A hellcat selects bonus feats from the following list:
[Aspect of the Beast](ref/feat/aspect-of-the-beast), [Blind-Fight](ref/feat/blind-fight),
[Combat Reflexes](ref/feat/combat-reflexes), [Dodge](ref/feat/dodge), [Diehard](ref/feat/diehard),
[Improved Grapple](ref/feat/improved-grapple), and [Power Attack](ref/feat/power-attack). At 6th
level, the following feats are added to the list: [Critical Focus](ref/feat/critical-focus),
[Greater Grapple](ref/feat/greater-grapple), [Improved Blind-Fight](ref/feat/improved-blind-fight),
[Mobility](ref/feat/mobility), and [Stalwart](ref/feat/stalwart). At 10th level, the following feats
are added to the list: [Bleeding Critical](ref/feat/bleeding-critical),
[Greater Blind-Fight](ref/feat/greater-blind-fight),
[Improved Critical](ref/feat/improved-critical), [Improved Stalwart](ref/feat/improved-stalwart),
and [Spring Attack](ref/feat/spring-attack).

This ability alters the monk's bonus feat ability.

## Hellcat Fury (Ex) {#hellcat-fury}

At 1st level, a hellcat can deal slashing damage with his unarmed strikes. At 4th level, whenever a
hellcat confirms a critical hit with his slashing unarmed strike, the target of that attack also
takes 1d4 points of [bleed](ref/umr/bleed) damage. At 8th level, the bleed damage increases to 1d6
points; at 12th level, the bleed damage increases to 1d8 points; at 16th level, the bleed damage
increases to 1d10 points; and at 20th level, the bleed damage increases to 1d12 points.

This ability replaces stunning fist and fast movement.

## Torture Training (Ex) {#torture-training}

At 2nd level, a hellcat who fails a save against an effect that causes him to become fatigued,
sickened, or staggered can attempt a second save against the effect at the end of his next turn.
Only one additional save is allowed. At 5th level, he can also attempt this second save against
effects that would cause him to become frightened or shaken. At 9th level, he can also attempt this
second save against effects that would cause him to become exhausted, nauseated, or dazed.

This ability replaces evasion, purity of body, and improved evasion.

## Crucible of Pain (Ex) {#crucible-of-pain}

At 3rd level, a hellcat gains an amount of [DR](ref/rule/damage-reduction)/— equal to half his monk
level against nonlethal damage. In addition, a hellcat is inured to hot climate effects as if using
_[endure elements](ref/spell/endure-elements)_.

This ability replaces slow fall and still mind.

## Hellcat Ki (Su) {#hellcat-ki}

At 4th level, a hellcat gains a pool of ki points that he can use as per the monk class feature but
with the following changes. In addition to spending ki to gain an additional attack, increased
speed, or improved AC, a hellcat can spend 1 ki point as a swift action to enhance his sight
(gaining 60-foot [darkvision](ref/rule/darkvision)) or his sense of smell (gaining the
[scent](ref/umr/scent) ability) for 1 minute per level.

At 7th level, a hellcat can spend 1 point of ki as a swift action to gain fire resistance 5 for 1
round per level. At 10th level, this fire resistance increases to 10, and at 14th level, it
increases to 15.

At 11th level, a hellcat can spend 1 point of ki as a swift action to become silhouetted with a
ghostly flame, which makes him harder to see in light but easier to see in darkness for 1 round per
level. He becomes invisible in bright light, gains [concealment](ref/rule/concealment) (20% miss
chance) in normal light, gains no benefit in dim light, and gives off light like a
[candle](ref/eq-misc/candle) in darkness, allowing other creatures to see him even without
[darkvision](ref/rule/darkvision). If he takes any action that would break
_[invisibility](ref/spell/invisibility)_ while in bright light, his invisibility is reduced to
concealment until the end of his next turn.

This ability alters ki pool and replaces wholeness of body and diamond body.
