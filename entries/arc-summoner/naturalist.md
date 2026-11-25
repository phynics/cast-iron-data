+++
id = "ref/arc-summoner/naturalist"
kind = "archetype"
title = "Naturalist"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20Naturalist"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "naturalist", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]
[[sources]]
publication = "advanced-class-guide"
page = "123"

[fields]
kind = "archetype"
features = [
  { anchor = "nature-s-call", level = 1 },
  { anchor = "animal-focus", level = 4 },
  { anchor = "second-animal-focus", level = 10 },
  { anchor = "shared-focus", level = 14 },
  { anchor = "third-animal-focus", level = 18 },
]
trades = [
  { replaces = "Summon monster I", feature = "summon-monster-i", by = ["nature-s-call"] },
  { replaces = "Shield ally", feature = "shield-ally", by = ["animal-focus"] },
  { replaces = "greater shield ally", feature = "greater-shield-ally", by = ["animal-focus"] },
  { replaces = "Aspect", feature = "aspect", by = ["second-animal-focus"] },
  { replaces = "Life bond", feature = "life-bond", by = ["shared-focus"] },
  { replaces = "Greater aspect", feature = "greater-aspect", by = ["third-animal-focus"] },
]
+++

A naturalist is a summoner who is in tune with the natural world, using his magic like a lens to
focus various animal aspects onto his eidolon. More akin to a hunter than to other arcane
spellcasters, a naturalist instinctively masters the power of such creatures as the bear, wolf,
mouse, or tiger to make his exotic eidolon the perfect living tool for battle or stealth, and he
eventually discovers how to apply these transformations to himself as well.

## Nature's Call (Sp) {#nature-s-call}

Starting at 1st level, the naturalist can cast
_[summon nature's ally I](ref/spell/summon-natures-ally-1)_ as a
[spell like ability](ref/umr/spell-like-abilities) a number of times per day equal to 3 + his
Charisma modifier. He can only use this ability to summon creatures of the animal, magical beast, or
vermin type. This ability otherwise functions as the
_[summon monster I](ref/spell/summon-monster-1)_ class feature (increasing in level as the
naturalist goes up in level and with the same restrictions). This ability replaces _summon monster
I_.

## Animal Focus (Su) {#animal-focus}

At 4th level, as a swift action a naturalist can enhance his eidolon with the aspect of an animal.
Each time he uses this ability, he can select a hunter's [animal aspect](ref/ability/animal-foci)
(see page 27) and apply it to his eidolon. His hunter level for this ability is equal to his
summoner level - 2. He does not gain the ability to add an animal aspect to himself (see Shared
Focus, below). This effect lasts until the eidolon is dismissed or sent back to its home plane.

When an animal aspect is applied to an eidolon, its form is altered by superficial physical changes
appropriate to that aspect. For example, using aspect of the [bat](ref/aspect/bat) might give the
eidolon larger ears and eyes and perhaps membranes of skin connecting its limbs to its body, while
using aspect of the [stag](ref/aspect/stag) might give the eidolon antlers and hoof like nails on
its feet. None of these changes interfere with any of the eidolon's natural or magical abilities.

This ability replaces shield ally and greater shield ally.

## Second Animal Focus (Su) {#second-animal-focus}

At 10th level, whenever a naturalist uses animal focus, he may apply two different animal aspects to
his eidolon. The eidolon's form gains superficial physical changes appropriate to the chosen aspect.
This replaces the aspect summoner class ability.

## Shared Focus (Su) {#shared-focus}

At 14th level, the naturalist begins to take on some of the feral nature of his eidolon. Whenever
the naturalist uses animal focus to grant an aspect to his eidolon, he also gains the effects of the
chosen aspect. The naturalist keeps this aspect until his eidolon is dismissed or sent back to its
home plane. The naturalist gains the effects of only one aspect, even if the eidolon gains more than
one (naturalist's choice). This ability replaces life bond.

## Third Animal Focus (Su) {#third-animal-focus}

At 18th level, whenever a naturalist uses his animal focus ability, he can apply three different
animal aspects to his eidolon (one of which lasts until he decides to change it). This ability
replaces greater aspect.
