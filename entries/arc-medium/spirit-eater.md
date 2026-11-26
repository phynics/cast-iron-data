+++
id = "ref/arc-medium/spirit-eater"
kind = "archetype"
title = "Spirit Eater"
aon = "ArchetypeDisplay.aspx?FixedName=Medium%20Spirit%20Eater"
source_ids = ["heroes-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spirit_eater", path = "json/archetypes_medium.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/medium" },
]
[[sources]]
publication = "heroes-of-golarion"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "ectoplasmic-strikes", level = 3 },
  { anchor = "consume-spirit", level = 7 },
]
trades = [
  { replaces = "Haunt channeler", feature = "haunt-channeler", by = ["ectoplasmic-strikes"] },
  { replaces = "Location channel", feature = "location-channel", by = ["consume-spirit"] },
  { replaces = "connection channel", feature = "connection-channel", by = ["consume-spirit"] },
]
+++

Shenmen is a ghost-haunted nation trapped in the shadow of the Gossamer Mountains and held beneath
the yoke of jorogumo witches. The mediums of Shenmen face brazen yokai that hunger for the living,
and these mediums have learned to devour them instead. Guardians of their communities, spirit eaters
absorb the dead to channel their power and serve as a line of defense against all manner of
incorporeal yokai.

## Ectoplasmic Strikes (Su) {#ectoplasmic-strikes}

At 3rd level, a spirit eater medium treats his attacks as if they had the
_[ghost touch](ref/magic-enh/ghost-touch-weapon)_ weapon property.

This replaces haunt channeler.

## Consume Spirit (Su) {#consume-spirit}

At 7th level, a spirit eater can attempt to consume an incorporeal creature and house it within his
body. If he reduces an incorporeal creature to 0 hit points or fewer, he can instead leave the
creature at 1 hit point and consume the creature as an immediate action. A consumed creature is
contained in the spirit eater's body and grants him a +1 bonus on either attack rolls, saving
throws, or skill checks, chosen by the spirit eater, and a number of
[temporary hit points](ref/rule/temporary-hit-points) equal to the consumed creature's Hit Dice.

A spirit eater's body can hold a number of creatures equal to his spirit bonus. If he attempts to
consume another creature after this point, he releases the creature that has been contained in his
body longest. He can release a consumed creature as a free action. A consumed creature attempts to
escape after 24 hours. The spirit eater can attempt to keep a consumed creature in his body by
attempting a Will save (DC = 10 + half the spirit eater's level + twice the number of the creatures
he has contained in his body). If he succeeds, the consumed creatures remain, but they grant the
spirit eater's channeled spirit 1 point of influence over him. A released creature is destroyed as
if it were reduced to 0 hit points and can reconstitute again later, if able.

This replaces location channel and connection channel.
