+++
id = "ref/arc-monk/student-of-stone"
kind = "archetype"
title = "Student of Stone"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Student%20of%20Stone"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "student_of_stone", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "advanced-race-guide"
page = "146"

[fields]
kind = "archetype"
features = [
  { anchor = "hard-as-stone", level = 2 },
  { anchor = "strength-of-stone", level = 3 },
  { anchor = "bonus-feat", level = 6 },
  { anchor = "bones-of-stone", level = 7 },
  { anchor = "body-of-stone", level = 9 },
  { anchor = "soul-of-stone", level = 12 },
  { anchor = "stone-self", level = 20 },
]
trades = [
  { replaces = "Evasion", feature = "evasion", by = ["hard-as-stone"] },
  { replaces = "Fast movement", feature = "fast-movement", by = ["strength-of-stone"] },
  { replaces = "High jump", feature = "high-jump", by = ["bones-of-stone"] },
  { replaces = "Improved evasion", feature = "improved-evasion", by = ["body-of-stone"] },
  { replaces = "Abundant step", feature = "abundant-step", by = ["soul-of-stone"] },
  { alters = "Bonus feats", feature = "bonus-feat", by = ["bonus-feat"] },
]
+++

By following the path of the stone, students of stone give up much of monks' mobility in favor of
sheer resilience. A student of stone has the following class features.

## Hard as Stone (Ex) {#hard-as-stone}

At 2nd level, whenever an opponent rolls to confirm a critical hit against a student of stone, treat
the student of stone's AC as +4 higher than normal. This ability replaces evasion.

## Strength of Stone (Ex) {#strength-of-stone}

At 3rd level, a student of stone learns to draw strength from the earth. So long as both he and his
opponent are touching the ground, the student of stone gains a +1 bonus on attack rolls, damage
rolls, [bull rush](ref/rule/bull-rush) and [trip](ref/rule/trip) combat maneuver rolls, and to his
CMD when resisting a bull rush or trip attempt. This ability replaces fast movement.

## Bonus Feat {#bonus-feat}

At 6th level, a student of stone adds [Elemental Fist](ref/feat/elemental-fist) (_Advanced Player's
Guide_) to his list of available bonus feats. If the student of stone selects Elemental Fist as a
bonus feat, he may only deal acid damage when using the feat. At 10th level, the student of stone
adds [Shaitan Style](ref/feat/shaitan-style) (_Ultimate Combat_) to his list of bonus feats, at 14th
level, he adds [Shaitan Skin](ref/feat/shaitan-skin) (_Ultimate Combat_), and at 18th level, he adds
[Shaitan Earthblast](ref/feat/shaitan-earthblast) (_Ultimate Combat_). This otherwise functions as
and alters the bonus feat ability.

## Bones of Stone (Su) {#bones-of-stone}

At 7th level, as a swift action, a student of stone can spend 1 ki point to gain DR 2/magic until
the beginning of his next turn. At 10th level, he can spend 1 ki point to gain DR 2/chaotic until
his next turn. At 15th level, he can spend 1 ki point to gain DR 5/chaotic until his next turn. This
ability replaces high jump.

## Body of Stone (Ex) {#body-of-stone}

At 9th level, a student of stone gains the benefits of the
_[light fortification](ref/magic-enh/fortification-light)_ armor property (_Core Rulebook_ 463).
This ability replaces improved evasion.

## Soul of Stone (Su) {#soul-of-stone}

At 12th level, as a swift action, a student of stone can spend 1 ki point to gain
[tremorsense](ref/umr/tremorsense) 15 feet until his next turn. At 16th level, the range of this
[tremorsense](ref/umr/tremorsense) increases to 30 feet. This ability replaces abundant step.

## Stone Self {#stone-self}

At 20th level, a student of stone becomes an [earth](ref/subtype/earth)
[outsider](ref/type/outsider). He gains the earth subtype, as well as DR 5/chaotic, burrow speed 20
feet, and [tremorsense](ref/umr/tremorsense) 20 feet.
