+++
id = "ref/arc-inquisitor/sacred-huntsmaster"
kind = "archetype"
title = "Sacred Huntsmaster"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Sacred%20Huntsmaster"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sacred_huntsmaster", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "advanced-class-guide"
page = "99"

[fields]
kind = "archetype"
features = [
  { anchor = "animal-companion", level = 1 },
  { anchor = "hunter-tactics", level = 3 },
  { anchor = "animal-focus", level = 4 },
  { anchor = "improved-empathic-link", level = 8 },
  { anchor = "raise-animal-companion", level = 16 },
  { anchor = "second-animal-focus", level = 17 },
  { anchor = "greater-empathic-link", level = 20 },
]
trades = [
  { replaces = "Judgment 1/day", feature = "judgment", levels = [1], by = ["animal-companion"] },
  { replaces = "Solo tactics", feature = "solo-tactics", by = ["hunter-tactics"] },
  { replaces = "Later iterations of the judgment ability", by = ["animal-focus"] },
  { replaces = "Second judgment", feature = "second-judgment", by = ["improved-empathic-link"] },
  { replaces = "Third judgment", feature = "third-judgment", by = ["raise-animal-companion"] },
  { replaces = "Slayer", feature = "slayer", by = ["second-animal-focus"] },
  { replaces = "True judgment", feature = "true-judgment", by = ["greater-empathic-link"] },
]
+++

Some inquisitors create a strong bond with an animal companion, and they hunt and punish threats to
the faith as an awe-inspiring duo. When they work together as one, there are few that dare to stand
in their way.

## Animal Companion (Ex) {#animal-companion}

At 1st level, a sacred huntsmaster forms a bond with an
[animal companion](ref/sidekick/animal-companion). This ability works as the
[hunter](ref/class/hunter) class feature of the same name, using her inquisitor level as her hunter
level. This ability replaces judgment 1/day.

## Hunter Tactics (Ex) {#hunter-tactics}

At 3rd level, a sacred huntsmaster automatically grants her teamwork feats to her animal companion.
The companion doesn't need to meet the prerequisites of these teamwork feats. This ability replaces
solo tactics.

## Animal Focus (Su) {#animal-focus}

At 4th level, a sacred huntsmaster can take on the aspects of an animal as a swift action. This
ability works as the hunter's [animal focus](ref/ability/animal-foci) class feature, with her
inquisitor level serving as her hunter level. This ability replaces later iterations of the judgment
ability.

## Improved Empathic Link (Su) {#improved-empathic-link}

At 8th level, the sacred huntsmaster gains an empathic link with her animal companion. This
functions like an empathic link with a [familiar](ref/sidekick/familiar), except the sacred
huntsmaster can also see through a companion's eyes as a swift action, maintaining this connection
as long as she likes (as long as the companion is within 1 mile) and ending it as a free action. The
sacred huntsmaster is [blinded](ref/misc/blinded) while maintaining this connection. This ability
replaces second judgment.

## Raise Animal Companion (Sp) {#raise-animal-companion}

At 16th level, a sacred huntsmaster gains
_[raise animal companion](ref/spell/raise-animal-companion)_ as a
[spell-like ability](ref/umr/spell-like-abilities) (not restricted to her own animal companion).
Using this ability gives the sacred huntsmaster a
[negative level](ref/rule/energy-drain-and-negative-levels) that cannot be overcome in any way
(including by _[restoration](ref/spell/restoration)_), but automatically ends after 24 hours. At
16th level, this functions as _[resurrection](ref/spell/resurrection)_ instead of
_[raise dead](ref/spell/raise-dead)_, but otherwise operates as normal. This ability replaces third
judgment.

## Second Animal Focus (Ex) {#second-animal-focus}

At 17th level, whenever a sacred huntsmaster uses her animal focus ability, she selects two
different animal aspects for herself instead of one, and can assign two aspects to her companion
instead of one. As with the companion's previous aspect, the second one does not count against the
minutes per day a sacred huntsmaster can take on an aspect. If her animal companion is dead and the
sacred huntsmaster has applied that aspect to herself, that aspect counts toward her maximum of two
aspects at once. The sacred huntsmaster can still only apply one of her dead companion's to herself,
not both. This ability replaces slayer.

## Greater Empathic Link (Su) {#greater-empathic-link}

At 20th level, the range of a sacred huntsmaster's empathic link with her animal companion increases
to 10 miles. If the animal companion is within 1 mile, it and the sacred huntsmaster can communicate
telepathically. This ability replaces true judgment.
