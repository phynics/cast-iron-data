+++
id = "ref/arc-spiritualist/onmyoji"
kind = "archetype"
title = "Onmyoji"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Onmyoji"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "onmyoji", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "occult-adventures"
page = "111"

[fields]
kind = "archetype"
features = [
  { anchor = "divine-spellcasting" },
  { anchor = "spiritual-resistance" },
  { anchor = "divine-teachings" },
]
trades = [
  { replaces = "Shared consciousness", feature = "shared-consciousness", by = ["spiritual-resistance"] },
  { replaces = "fused consciousness", feature = "fused-consciousness", by = ["spiritual-resistance"] },
  { replaces = "Spiritual interference", feature = "spiritual-interference", by = ["divine-teachings"] },
  { replaces = "greater spiritual interference", feature = "greater-spiritual-interference", by = ["divine-teachings"] },
  { alters = "Spellcasting", feature = "spells", by = ["divine-spellcasting"] },
]
+++

Though most spiritualists are chosen by their phantoms, others deliberately call phantoms to them
through years of careful preparation and study in obscure divine traditions. These spiritualists,
known as onmyoji, form close bonds with their phantoms, as any other spiritualist does, but see the
phantoms as partners and tools in their work. Onmyoji serve as emissaries between the mundane world
and the spiritual one, either working to ensure that troubles in the spiritual world do not spill
over into the world of mortals, or stirring up spiritual trouble in order to achieve their ends
among the living.

## Divine Spellcasting {#divine-spellcasting}

An onmyoji's spellcasting ability comes from divine rather than psychic power. As a divine caster,
the onmyoji's spells use verbal components instead of thought components, and somatic components
instead of emotional components, and she uses an ofuda as a divine focus. Ofudas are scrolls with
holy writings written on parchment, cloth, or wood (having the same cost as a
[wooden holy symbol](ref/eq-misc/wooden-holy-symbol)) or metal (having the same cost as a
[silver holy symbol](ref/eq-misc/holy-symbol-silver)). This ability alters spellcasting.

## Spiritual Resistance (Su) {#spiritual-resistance}

An onmyoji's phantom provides her with protection from supernatural forces. While the phantom is
confined within the onmyoji's consciousness (not stranded on the Ethereal Plane or fully
manifested), it grants her a +2 bonus on saving throws against the spell-like and supernatural
abilities of fey, outsiders, and incorporeal undead. At 6th level and every 6 levels thereafter,
this bonus increases by 1 (to a maximum of +5 at 18th level). This ability replaces shared
consciousness and fused consciousness.

## Divine Teachings (Su) {#divine-teachings}

An onmyoji gains the ability to call upon her phantom to help her cast spells she normally couldn't.
At 4th level and every 3 levels thereafter, an onmyoji can choose a single spell from the cleric
spell list with a spell level she is currently able to cast, and add that spell to her list of
spells known, at the same spell level as it appears on the cleric spell list. Because the onmyoji
relies on her phantom's influence in order to cast these spells, she can cast spells added in this
way only while the phantom is confined within her consciousness (not stranded on the Ethereal Plane
or fully manifested). This ability replaces spiritual interference and greater spiritual
interference.
