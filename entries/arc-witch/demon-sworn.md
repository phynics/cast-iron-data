+++
id = "ref/arc-witch/demon-sworn"
kind = "archetype"
title = "Demon-Sworn"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Demon-Sworn"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "demon_sworn", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "heroes-of-the-darklands"
page = "16"

[fields]
kind = "archetype"
features = [
  { anchor = "demonic-pact" },
  { anchor = "cruel-hex", level = 1 },
  { anchor = "manifest-pact", level = 6 },
]
trades = [
  { replaces = "Hex gained at 6th level", feature = "hex", levels = [6], by = ["manifest-pact"] },
  { alters = "Patron spells", feature = "patron-spells", by = ["demonic-pact"] },
  { alters = "Hex", feature = "hex", by = ["cruel-hex"] },
  { alters = "major hex", feature = "major-hex", by = ["cruel-hex"] },
  { alters = "grand hex", feature = "grand-hex", by = ["cruel-hex"] },
]
+++

The drow are among the best known creatures on Golarion who were "saved" by demonic intervention,
but they're far from the only ones. In the depths of the Darklands, as well as similarly
inhospitable locales on Golarion, many seek the succor of demons as a means of survival. Such pacts
are often made in haste, without a true understanding of the lifelong effects they'll have on those
who make them.

## Demonic Pact {#demonic-pact}

A demon-sworn makes a pact with a demonic entity, forever binding her to the forces of the Abyss and
corrupting her connection with her patron. At the indicated levels, she gains the spells below in
place of her normal patron spells: 2nd—_protection from_ _good_, 6th—_unholy blight_, 10th—_dispel
good_, 14th—_blasphemy_, 18th—_unholy aura_. Casting spells with the evil descriptor from this
replacement list has no effect on the demon-sworn's alignment.

This ability modifies patron spells.

## Cruel Hex {#cruel-hex}

A demon-sworn always inflicts some pain, whether she wants to or not. Each hex deals 1d4 points of
nonlethal damage to creatures affected by it, in addition to any damage the hex normally deals. For
major hexes, the damage increases to 2d4. For grand hexes, the damage increases to 4d4. Each die
result of a natural 4 deals 1 point of lethal damage to the demon-sworn.

This ability alters the witch's hex, major hex, and grand hex.

## Manifest Pact (Ex) {#manifest-pact}

At 6th level, the demon-sworn gains [Improved Familiar](ref/feat/improved-familiar) as a bonus feat.
The associated familiar is made up of the tiny amount of soul matter lost when the demon-sworn made
her pact with demonic powers. The familiar must be a [quasit](ref/monster/demon-quasit), regardless
of the demon-sworn's actual alignment, and it manifests by eating its way out of the demon-sworn's
former familiar. The quasit knows all spells known to the previous familiar. It loyally serves the
demon-sworn, despite any conflicts of alignment, obeying its mistress to the best of its abilities.

This familiar cannot be replaced, and if slain, the ritual to replace the lost familiar recreates
the same quasit, along with the same spells previously known. Replacing the familiar in this fashion
also imparts the demon-sworn with 1 permanent
[negative level](ref/rule/energy-drain-and-negative-levels), as if she had been hit by an
energy-draining creature.

This ability replaces the hex gained at 6th level.
