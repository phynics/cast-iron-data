+++
id = "ref/arc-alchemist/mnemostiller"
kind = "archetype"
title = "Mnemostiller"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Mnemostiller"
source_ids = ["distant-realms"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mnemostiller", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "distant-realms"
page = "52"

[fields]
kind = "archetype"
features = [
  { anchor = "mental-ambix", level = 1 },
  { anchor = "rasugen", level = 1 },
  { anchor = "anguish-bomb", level = 1 },
  { anchor = "brewed-memories", level = 2 },
  { anchor = "natural-empath", level = 2 },
  { anchor = "mind-delver", level = 10 },
]
trades = [
  { replaces = "Throw anything", feature = "throw-anything", by = ["mental-ambix"] },
  { replaces = "Mutagen", feature = "mutagen", by = ["rasugen"] },
  { replaces = "Bombs", feature = "bomb", by = ["anguish-bomb"] },
  { replaces = "Poison resistance", feature = "poison-resistance", by = ["brewed-memories"] },
  { replaces = "Poison use", feature = "poison-use", by = ["natural-empath"] },
  { alters = "Alchemy", feature = "alchemy", by = ["mental-ambix"] },
]
+++

Mnemostillers extract memories, storing them as a thick vapor called mnemos. They can return
memories as easily as administering a potion, and experienced mnemostillers create a variety of
effects through the careful administration of past traumas or victories.

## Mental Ambix {#mental-ambix}

A mnemostiller's alchemy relies on force of personality, using his own mind as an alchemy lab to
draw and purify the mnemos collected from others. A mnemostiller uses his Charisma score in place of
his Intelligence score for the purpose of extracts and bonus extracts. A mnemostiller still uses his
Intelligence score to learn new formulae.

The mnemostiller can cast _[detect thoughts](ref/spell/detect-thoughts)_ as a
[spell-like ability](ref/umr/spell-like-abilities) a number of times per day equal to his Charisma
modifier (minimum 1).

This alters alchemy and replaces throw anything.

## Rasugen (Su) {#rasugen}

A mnemostiller learns to brew a unique type of mutagen, called a rasugen, that suppresses his mind
to enter a state of sublime purity. In this state, a mnemostiller becomes incredibly resilient, but
cannot perform complex skills. Once imbibed, a rasugen grants a +2 alchemical bonus on all saving
throws and 2 [temporary hit points](ref/rule/temporary-hit-points) per alchemist level for 10
minutes per alchemist level. In addition, while the rasugen is in effect, a mnemostiller takes a -2
penalty to his Intelligence score and can't attempt checks using Appraise, Craft, Disable Device,
Heal, Knowledge (any), Profession, Sleight of Hand, or Spellcraft. This acts in all other ways like
a mutagen.

This replaces mutagen. A mnemostiller can never gain the mutagen, cognatogen, or inspiring
cognatogen ability, even from a discovery or another class.

## Anguish Bomb (Su) {#anguish-bomb}

A mnemostiller crafts his bombs from mnemos of pain and discomfort, inflicting psychic damage. An
anguish bomb is identical to a bomb except that it deals nonlethal damage, it deals no damage to
inanimate objects and creatures immune to mental effects, and creatures caught in the anguish bomb's
splash can attempt a Will save for [half](ref/misc/fractions-and-rounding) damage. A mnemostiller
uses his Charisma score in place of his Intelligence score to determine the bonus damage of his
anguish bomb and the save DC of the anguish bomb's splash damage. He still uses his Intelligence
score to determine his number of bombs per day. If the mnemostiller has taken any hit point damage
in the past 24 hours, his anguish bombs inflict 1 additional point of nonlethal damage for every 2
alchemist levels he has.

This replaces bombs.

## Brewed Memories {#brewed-memories}

A mnemostiller can create several unique extracts from the mnemos he pulls from the minds of others.
At 2nd level, he adds _[mindlink](ref/spell/mindlink)_,
_[placebo effect](ref/spell/placebo-effect)_, and _[thought echo](ref/spell/thought-echo)_ to his
formula book as 1st-level extracts. At 5th level, he adds
_[aura alteration](ref/spell/aura-alteration)_, _[detect mindscape](ref/spell/detect-mindscape)_,
and _[mindscape door](ref/spell/mindscape-door)_ to his formula book as 2nd-level extracts. At 8th
level, he adds _[mindwipe](ref/spell/mindwipe)_ and _[thoughtsense](ref/spell/thoughtsense)_ to his
formula book as 3rd-level extracts; the range for a _[mindwipe](ref/spell/mindwipe)_ extract becomes
creature touched, and it can be applied only to a helpless or willing creature.

This replaces poison resistance.

## Natural Empath (Ex) {#natural-empath}

A mnemostiller's studies naturally focus on others. He gains [infusion](ref/discovery/infusion) as a
bonus discovery at 2nd level.

This replaces poison use.

## Mind-Delver (Su) {#mind-delver}

At 10th level, a mnemostiller can use _[mind probe](ref/spell/mind-probe)_ as a
[spell-like ability](ref/umr/spell-like-abilities) a number of times per day equal to his Charisma
modifier (minimum 1).
