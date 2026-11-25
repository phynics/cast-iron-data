+++
id = "ref/arc-mesmerist/enigma"
kind = "archetype"
title = "Enigma"
aon = "ArchetypeDisplay.aspx?FixedName=Mesmerist%20Enigma"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "enigma", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "36"

[fields]
kind = "archetype"
features = [
  { anchor = "solipsism", level = 1 },
  { anchor = "veiled-steps", level = 1 },
  { anchor = "enigmatic-stare", level = 1 },
  { anchor = "transfer-affliction", level = 3 },
  { anchor = "sneak-attack", level = 5 },
  { anchor = "detection-void", level = 11 },
  { anchor = "absentia", level = 20 },
]
trades = [
  { replaces = "Consummate liar", feature = "consummate-liar", by = ["veiled-steps"] },
  { replaces = "Painful stare", feature = "painful-stare", by = ["enigmatic-stare"] },
  { replaces = "Manifold tricks", feature = "manifold-tricks", by = ["sneak-attack"] },
  { replaces = "Glib lie", feature = "glib-lie", by = ["detection-void"] },
  { replaces = "Rule minds", feature = "rule-minds", by = ["absentia"] },
  { alters = "Hypnotic stare", feature = "hypnotic-stare", by = ["solipsism"] },
  { alters = "Touch treatment", feature = "touch-treatment", by = ["transfer-affliction"] },
]
+++

An enigma spends his life dedicated to developing psychic abilities that allow him to operate
unnoticed. While the target of a mesmerist's _hypnotic stare_ might not realize that the mesmerist
is the source of the strange thoughts invading his mind, an enigma takes that mental obfuscation to
a more extreme level. Enigmas often end up serving as master spies and infiltration experts.

## Solipsism (Su) {#solipsism}

At 1st level, whenever the enigma uses hypnotic stare on a creature, instead of applying a penalty
on the creature's saving throws, the enigma begins to fade from the creature's view. Until the
enigma's next turn, the enigma gains the effects of [concealment](ref/rule/concealment) against that
creature (unless it can see invisible creatures). Starting on the enigma's next turn, he gains the
effect of _[invisibility](ref/spell/invisibility)_ against that creature. These effects last as long
as the enigma continues to use his hypnotic stare, but if he takes an action that would end
_invisibility_, it ends his hypnotic stare immediately. The enigma can reinstate this effect
whenever he wishes, but each time it begins with 1 round of concealment. At 8th level, attacks that
would end _invisibility_ do not end the enigma's hypnotic stare, and after 1 round of concealment,
he gains the benefits of _[greater invisibility](ref/spell/invisibility-greater)_ against the target
of his stare.

For the purpose of bold stare improvements, the enigma's hypnotic stare always has a penalty of -1.

This ability alters hypnotic stare.

## Veiled Steps {#veiled-steps}

An enigma gains a bonus to his Stealth checks equal to 1/4 his mesmerist level (minimum +1).

This ability replaces consummate liar.

## Enigmatic Stare (Su) {#enigmatic-stare}

The target of an enigma's hypnotic stare takes a -4 penalty on Perception checks to notice the
enigma. At 8th level, this penalty increases to -6.

This ability replaces painful stare.

## Transfer Affliction (Su) {#transfer-affliction}

At 3rd level, the enigma can afflict others with the harmful conditions that he endures. This
ability functions as the touch treatment ability, but can only be used to remove harmful conditions
from the enigma, not other creatures. In order to remove these harmful effects, the enigma must
succeed at a touch attack against another creature. The creature touched gains the chosen harmful
effect for whatever duration it would have afflicted the enigma and the effect is removed from the
enigma, unless the creature succeeds at a Will save (DC = 10 + 1/2 the enigma's mesmerist level +
his Charisma modifier). Using this ability is always a standard action. At 14th level, the enigma
can instead expend one use of touch treatment to replicate the effects of
_[bestow curse](ref/spell/bestow-curse)_, delivered as a touch attack as part of using this ability.
Transfer affliction is a mind-affecting effect.

This ability alters touch treatment.

## Sneak Attack (Ex) {#sneak-attack}

At 5th level, an enigma gains the [sneak attack](ref/ability/sneak-attack) ability of a rogue. This
sneak attack damage is +1d6 at 5th level, and increases by +1d6 every 4 mesmerist levels thereafter.

This ability replaces manifold tricks.

## Detection Void (Su) {#detection-void}

At 11th level, an enigma can elude detection spells (spells with "detect" in their name). A creature
using this sort of magic against the enigma must succeed at a caster level check against a DC equal
to 15 + the enigma's class level to succeed (as if the enigma was under the effect of a
_[nondetection](ref/spell/nondetection)_ spell); failure means the magic fails to detect the enigma,
as if he did not exist.

This ability replaces glib lie.

## Absentia (Su) {#absentia}

At 20th level, all creatures adjacent to the enigma subconsciously ignore him. Adjacent creatures
are always treated as [flat-footed](ref/rule/flat-footed) to the enigma and are not considered to be
directly observing the enigma for the purpose of the Stealth skill. This effect ends immediately if
the enigma makes a successful attack against any creature, but automatically resumes at the
beginning of his next turn.

This ability replaces rule minds.
