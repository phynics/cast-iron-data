+++
id = "ref/arc-summoner/story-summoner"
kind = "archetype"
title = "Story Summoner"
source_ids = ["the-harrow-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "story_summoner", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]
[[sources]]
publication = "the-harrow-handbook"
page = "25"

[fields]
kind = "archetype"
replaces = ["Bond senses", "Transposition"]
replaces_features = ["bond-senses", "transposition"]
+++

Story summoners rely on the harrow to weave the paths they walk, turning their tales into reality.
They channel magic through their harrow decks to influence the strange extraplanar beings they
summon, bringing familiar and fateful characters to life. Some focus on the more whimsical figures
of the harrow, while others bring its darkest icons into the real world.

**Storykin Eidolon**

**Info:** Unlike most eidolons, a story summoner's eidolon cannot touch or attack creatures warded
by [protection from evil](ref/spell/protection-from-evil) and similar effects that prevent contact
with summoned creatures.

**Standard:** While his eidolon is summoned, the story summoner can draw a random card from a
complete [harrow deck](ref/eq-misc/harrow-deck) he owns. For a number of rounds equal to 1/2 the
summoner's class level (minimum 1), the eidolon's alignment changes to match that of the harrow card
drawn, and the eidolon gains a +4 enhancement bonus on the ability score linked to the drawn card's
suit. The eidolon continues to follow its summoner's orders regardless of its alignment.

**Usage:** Charisma3 modifier times/day

**Summon Arcana**

**Ability:** A story summoner can use a complete harrow deck he owns as an additional focus
component for his _[summon monster](ref/spell/summon-monster)_
[spell-like ability](ref/umr/spell-like-abilities). When he does so, the summoner draws a random
card from the deck and applies a simple template to the summoned monster based on the card's
alignment: [celestial](ref/template/celestial) (any good), [fiendish](ref/template/fiendish) (any
evil), [resolute](ref/template/resolute) (any lawful), or [entropic](ref/template/entropic) (any
chaotic). If a card has more than one alignment - such as a lawful evil or chaotic good card - the
summoner can choose which template to apply to the summoned creature.

**Gained:** At 2nd Level

**Replaces:** Bond senses

**Special:** This ability allows a story summoner to summon and command creatures normally
prohibited by their alignment.

**Evolve Base Form (Su)**

**Ability:** Whenever he gains a level, the story summoner can change his eidolon's base form to a
new base form. Once chosen, this base form is set until the story summoner gains another summoner
level.

**Gained:** At 8th Level

**Replaces:** Transposition
