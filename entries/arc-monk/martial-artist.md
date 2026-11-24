+++
id = "ref/arc-monk/martial-artist"
kind = "archetype"
title = "Martial Artist"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Martial%20Artist"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "martial_artist", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "ultimate-combat"
page = "59"

[fields]
kind = "archetype"
features = [
  { anchor = "alignment" },
  { anchor = "pain-points", level = 3 },
  { anchor = "martial-arts-master", level = 4 },
  { anchor = "exploit-weakness", level = 4 },
  { anchor = "extreme-endurance", level = 5 },
  { anchor = "physical-resistance", level = 7 },
  { anchor = "bonus-feat", level = 12 },
  { anchor = "defensive-roll", level = 13 },
  { anchor = "quivering-palm" },
  { anchor = "greater-defensive-roll", level = 19 },
]
trades = [
  { replaces = "Still mind", feature = "still-mind", by = ["pain-points"] },
  { replaces = "Slow fall", feature = "slow-fall", by = ["martial-arts-master"] },
  { replaces = "Ki pool", feature = "ki-pool", by = ["exploit-weakness"] },
  { replaces = "Purity of body", feature = "purity-of-body", by = ["extreme-endurance"] },
  { replaces = "diamond body", feature = "diamond-body", by = ["extreme-endurance"] },
  { replaces = "perfect self", feature = "perfect-self", by = ["extreme-endurance"] },
  { replaces = "Wholeness of body", feature = "wholeness-of-body", by = ["physical-resistance"] },
  { replaces = "timeless body", feature = "timeless-body", by = ["physical-resistance"] },
  { replaces = "tongue of sun and moon", feature = "tongue-of-the-sun-and-moon", by = ["physical-resistance"] },
  { replaces = "Abundant step", feature = "abundant-step", by = ["bonus-feat"] },
  { replaces = "Diamond soul", feature = "diamond-soul", by = ["defensive-roll"] },
  { replaces = "Empty body", feature = "empty-body", by = ["greater-defensive-roll"] },
  { alters = "Quivering palm", feature = "quivering-palm", by = ["quivering-palm"] },
]
+++

The martial artist pursues a mastery of pure martial arts without the monastic traditions. He is a
master of form, but lacks the ability to harness his ki.

## Alignment {#alignment}

A martial artist may be of any alignment.

## Pain Points (Ex) {#pain-points}

At 3rd level, a martial artist's advanced knowledge of anatomy grants a +1 bonus on critical hit
confirmation rolls and increases the DC of his stunning fist and quivering palm by 1. This ability
replaces still mind.

## Martial Arts Master (Ex) {#martial-arts-master}

At 4th level, a martial artist may use his monk level to qualify for feats with a fighter level
prerequisite when those feats are applied to unarmed strikes or weapons with the monk special
quality. This ability replaces slow fall.

## Exploit Weakness (Ex) {#exploit-weakness}

At 4th level, as a swift action, a martial artist can observe a creature or object to find its weak
point by making a Wisdom check and adding his monk level against a DC of 10 + the object's
[hardness](ref/umr/hardness) or the target's CR. If the check succeeds, the martial artist gains a
+2 bonus on attack rolls until the end of his turn, and any attacks he makes until the end of his
turn ignore the creature or object's DR or hardness.

A martial artist may instead use this ability as a swift action to analyze the movements and
expressions of one creature within 30 feet, granting a bonus on Sense Motive checks and Reflex saves
and a dodge bonus to AC against that opponent equal to 1/2 his monk level until the start of his
next turn.

This ability replaces ki pool.

## Extreme Endurance (Ex) {#extreme-endurance}

At 5th level, a martial artist gains immunity to [fatigue](ref/misc/fatigued). At 10th level, he
also gains immunity to [exhaustion](ref/misc/exhausted). At 15th level, he gains immunity to
stunning. At 20th level, he gains immunity to death effects and
[energy drain](ref/rule/energy-drain-and-negative-levels). This ability replaces purity of body,
diamond body, and perfect self.

## Physical Resistance (Ex) {#physical-resistance}

At 7th level, if a martial artist suffers any effect that causes
[ability damage](ref/rule/ability-damage-drain), ability drain, or temporary ability score
penalties, the effect is reduced by 1 point. This reduction increases by 1 for every three levels
beyond 7th (to a maximum reduction of 5 at 19th level). This ability replaces wholeness of body,
timeless body, and tongue of the sun and moon.

## Bonus Feat {#bonus-feat}

At 12th level, a martial artist gains an additional bonus feat, selected from those available in the
monk class feature. This ability replaces abundant step.

## Defensive Roll (Ex) {#defensive-roll}

At 13th level, a martial artist may use the defensive roll advanced rogue talent once per day, plus
once per three levels beyond 13th (to a maximum of 3 times a day at 19th level). This ability
replaces diamond soul.

## Quivering Palm {#quivering-palm}

A martial artist may use this ability one additional time per day per level above 15th, but may not
have more than one in effect at a time.

## Greater Defensive Roll (Ex) {#greater-defensive-roll}

At 19th level, a martial artist suffers no damage on a successful defensive roll, and only half
damage if the Reflex saving throw fails. This ability replaces empty body.
