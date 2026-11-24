+++
id = "ref/arc-monk/monk-of-the-healing-hand"
kind = "archetype"
title = "Monk of the Healing Hand"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Monk%20of%20the%20Healing%20Hand"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "monk_of_the_healing_hand", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "advanced-players-guide"
page = "113"

[fields]
kind = "archetype"
features = [
  { anchor = "ancient-healing-hand", level = 7 },
  { anchor = "ki-sacrifice", level = 11 },
  { anchor = "true-sacrifice", level = 20 },
]
trades = [
  { replaces = "Wholeness of body", feature = "wholeness-of-body", by = ["ancient-healing-hand"] },
  { replaces = "Diamond body", feature = "diamond-body", by = ["ki-sacrifice"] },
  { replaces = "quivering palm", feature = "quivering-palm", by = ["ki-sacrifice"] },
  { replaces = "Perfect self", feature = "perfect-self", by = ["true-sacrifice"] },
]
+++

Monks of the healing hand seek perfection through helping others. By focusing their meditations on
the flow of life within themselves and all creation they gain an understanding of how to share their
ki with others, healing wounds and even bringing the dead back to life. For such a monk, sacrificing
himself to save another is the surest way to achieve transcendence. A monk of the healing hand has
the following class features.

## Ancient Healing Hand (Su) {#ancient-healing-hand}

At 7th level, a monk of the healing hand can heal another creature's wounds with a touch. As a
full-round action, the monk can spend 2 _ki_ points to heal a number of hit points equal to the
monk's level. He needs at least one hand free to use this ability, and cannot heal himself. If the
action is interrupted, the subject heals no hit points, and the _ki_ points are lost. This ability
replaces wholeness of body.

## Ki Sacrifice (Su) {#ki-sacrifice}

At 11th level, a monk of the healing hand can use his entire _ki_ pool to bring a person back to
life. It takes 1 hour to perform this ritual. At the end of the ritual, the monk sacrifices all of
his _ki_ in order to cast _[raise dead](ref/spell/raise-dead)_ (as the spell) with a caster level
equal to his monk level. The ritual uses all of the _ki_ in the monk's _ki_ pool; the monk must have
at least 6 points of _ki_ in his _ki_ pool to use this ability. At 15th level, the monk may
sacrifice his _ki_ to cast _[resurrection](ref/spell/resurrection)_. The monk must have at least 8
points of _ki_ in his _ki_ pool to use this ability. These rituals do not require material
components. When this ability is used, the monk's _ki_ pool is not replenished until 24 hours have
passed. This ability replaces both diamond body and quivering palm.

## True Sacrifice (Su) {#true-sacrifice}

At 20th level, in a final selfless act, a monk of the healing hand can draw in his entire _ki_,
which then explodes outward in a 50-foot-radius [emanation](ref/misc/emanation). All dead allies
within the emanation are brought back to life, as if they were the subject of a
_[true resurrection](ref/spell/true-resurrection)_ spell with a caster level equal to the monk's
level. When the monk does this, he is truly and utterly destroyed. A monk destroyed in this way can
never come back to life, not even by way of a _[wish](ref/spell/wish)_ or
_[miracle](ref/spell/miracle)_ spell or by the power of a deity. Furthermore, the monk's name can
never be spoken or written down again. All written mentions of his name become nothing more than a
blank space. This ability replaces perfect self.
