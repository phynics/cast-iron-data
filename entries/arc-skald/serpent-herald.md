+++
id = "ref/arc-skald/serpent-herald"
kind = "archetype"
title = "Serpent Herald"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Serpent%20Herald"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "serpent_herald", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "28"

[fields]
kind = "archetype"
features = [
  { anchor = "serpentine-rage", level = 3 },
  { anchor = "serpent-shape", level = 5 },
]
trades = [
  { replaces = "Rage power gained at 3rd level", feature = "rage-powers", levels = [3], by = ["serpentine-rage"] },
  { replaces = "Spell kenning", feature = "spell-kenning", by = ["serpent-shape"] },
]
+++

Warrior bands devoted to [Ragadahn](ref/faith/ragadahn) are often led by a serpent herald, whose
deep roars shake the earth itself. Rumors tell of waves of snakes slithering forth from their nests
in awe as these bellowing commanders take on serpentine features.

## Serpentine Rage (Su) {#serpentine-rage}

At 3rd level, a serpent herald can call down Ragadahn's features onto his allies. Allies affected by
the serpent herald's inspired rage ability gain a serpentine aspect of the serpent herald's choice
(all affected allies gain the same aspect). The serpent herald may choose from the following
aspects: movement (+8 competence bonus on Climb and Swim checks, and targets can take 10 on these
checks even when rushed or threatened), scales (+2 natural armor bonus), senses
([low-light vision](ref/rule/low-light-vision) and [scent](ref/umr/scent)), or a natural bite attack
(1d4 damage [for a Medium creature](ref/umr/natural-attacks) plus poison \[bite—injury; _save_
Fortitude DC 10 + half the serpent herald's class level + his Constitution modifier; _frequency_
1/round for 6 rounds; _effect_ 1 Constitution damage, _cure_ 1 save\]). This is a polymorph effect;
a creature under another polymorph effect, such as wild shape, does not gain the aspect. If the
serpent herald grants one of these aspects to himself, he also gains the ability to
_[speak with animals](ref/spell/speak-with-animals)_ (reptiles and creatures with the aquatic
subtype only) for as long as he has the aspect. The serpent herald must have the inspired rage
raging song to use this ability.

This ability replaces the rage power gained at 3rd level.

## Serpent Shape (Su) {#serpent-shape}

At 5th level, a serpent herald gains the ability to use wild shape to take the form of a reptile or
an aquatic animal once per day, as the [druid](ref/class/druid) class feature. His effective druid
level for this ability is equal to his serpent herald level - 1. This doesn't allow him to assume
other forms, such as elementals or other kinds of animals. When in animal form, the serpent herald
is treated as able to speak normally for the purpose of using raging song, but not for using other
abilities that require speech (such as spellcasting).

At 11th level, a serpent herald can use this ability twice per day and gains the benefits of the
[Wild Speech](ref/feat/wild-speech) feat while using this ability, treating his druid level as his
serpent herald level - 1.

At 17th level, a serpent herald can use this ability three times per day. In addition, he gains the
supernatural resiliency of a [linnorm](ref/family/linnorm), gaining the effects of
_[freedom of movement](ref/spell/freedom-of-movement)_ while using this ability.

This ability replaces spell kenning.

## Rage Powers {#rage-powers}

The following rage powers complement the serpent herald archetype: animal fury, battle roar,
knockback, knockdown, linnorm death curse (any), low-light vision, sprint, and swift foot.
