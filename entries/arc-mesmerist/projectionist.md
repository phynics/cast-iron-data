+++
id = "ref/arc-mesmerist/projectionist"
kind = "archetype"
title = "Projectionist"
aon = "ArchetypeDisplay.aspx?FixedName=Mesmerist%20Projectionist"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "projectionist", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]
[[sources]]
publication = "psychic-anthology"
page = "18"

[fields]
kind = "archetype"
features = [
  { anchor = "spells" },
  { anchor = "implant-consciousness", level = 4 },
  { anchor = "hidden-presence", level = 5 },
]
trades = [
  { replaces = "Mesmerist tricks gained at 4th and 8th levels", feature = "mesmerist-tricks", levels = [4, 8], by = ["implant-consciousness"] },
  { replaces = "Mental potency", feature = "mental-potency", by = ["hidden-presence"] },
  { alters = "Spellcasting", feature = "spells", by = ["spells"] },
]
+++

Not content to simply command others from afar, a projectionist is able to use his mesmerizing
powers to utterly dominate other creatures and objects by projecting his spirit from his body.

## Spells {#spells}

A projectionist's psychic powers manifest in an almost predictable manner, making them less
versatile than other spellcasters. At each of the indicated levels, a projectionist must choose the
indicated spell to learn—he cannot choose other spells. The spells that a projectionist must learn
(and the level at which he must choose them) are _enter image_ (4th), _lesser object possession_
(7th), _riding possession_ (10th), _object possession_ (13th), and _greater object possession_
(16th). The projectionist adds _greater object possession_ to his spell list as a 6th-level spell.

This ability alters the mesmerist's spellcasting.

## Implant Consciousness (Su) {#implant-consciousness}

At 4th level, a projectionist can spend one use of his mesmerist trick ability to create a psychic
link between himself and one object that bears his likeness, such as a painting or a statue. This
functions in all ways like implanting a mesmerist trick in a creature, except the target is an
object. The projectionist can trigger the trick as a standard action at any time—upon doing so, his
consciousness leaves his body and fills the target object, functioning as described by the "filling
an image with your consciousness" use of the _[enter image](ref/spell/enter-image)_ spell. Use the
projectionist's mesmerist level as the spell's caster level. While filling an image with his
consciousness, the projectionist can use and maintain his hypnotic stare on opponents, and can also
trigger his painful stare. At 8th level, he can also use any purely mental action (including casting
psychic spells) while filling an object with his consciousness.

Once he implants this trick in an object, the projectionist can fill the target with his
consciousness whenever he pleases, regardless of distance or whether he is on the same plane as his
target. Once he stops concentrating on maintaining the _[enter image](ref/spell/enter-image)_
effect, his consciousness returns to his body and he cannot fill the target with his consciousness
again until he implants another mesmerist trick in that object.

This ability replaces the mesmerist tricks gained at 4th and 8th levels.

## Hidden Presence {#hidden-presence}

At 5th level, a projectionist gains [Hidden Presence](ref/feat/hidden-presence) as a bonus feat. He
doesn't need to meet the feat's prerequisites. He benefits from Hidden Presence and feats that list
Hidden Presence as a prerequisite while possessing objects (as with
_[object possession](ref/spell/object-possession)_) or while filling an object with his
consciousness (as described in the _[enter image](ref/spell/enter-image)_ spell), as well as when he
possesses creatures, provided the feat is applicable. For instance,
[Intrusive Presence](ref/feat/intrusive-presence) cannot be used to read the mind of an inanimate
object possessed via _[enter image](ref/spell/enter-image)_ or
_[object possession](ref/spell/object-possession)_, as objects possess no minds to be read.

This ability replaces the mesmerist's mental potency.
