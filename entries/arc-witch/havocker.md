+++
id = "ref/arc-witch/havocker"
kind = "archetype"
title = "Havocker"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Havocker"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "havocker", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "patron-element", level = 1 },
  { anchor = "infusion", level = 2 },
  { anchor = "spellburn", level = 2 },
]
trades = [
  { replaces = "1st-level hex", feature = "hex", levels = [1], by = ["patron-element"] },
  { replaces = "The witch's hexes from 2nd level on", by = ["infusion"] },
  { replaces = "major hex", feature = "major-hex", by = ["infusion"] },
  { replaces = "grand hex", feature = "grand-hex", by = ["infusion"] },
  { alters = "Familiar", feature = "witch-s-familiar", by = ["patron-element"] },
]
+++

Although most witches are guided to subtle curses and debilitating hexes by their mysterious
patrons, some are instead taught the secrets of harnessing raw, destructive elemental power.

## Patron Element {#patron-element}

A havocker's patron grants her the ability to devastate her foes with a specific
[element](ref/ability/elements). At 1st level, rather than selecting a standard patron and gaining
patron spells, the witch selects a specific [kineticist](ref/class/kineticist) element, which
represents the shadowy forces from which she gains her familiar and class powers. The havocker gains
the elemental focus and kinetic blast class features with the associated element, using her witch
level as her effective kineticist level. If the havocker takes levels in another class that grants
an elemental focus, the elemental focuses must be the same type, even if that means that the
elemental focus of one of the classes must change. Subject to GM discretion, the havocker can change
her former elemental focus to make them conform.

This ability alters the witch's familiar and replaces the witch's 1st-level hex.

## Infusion {#infusion}

At 2nd level and every 4 witch levels thereafter, the havocker gains an
[infusion wild talent](ref/ability/infusion-wild-talents) from the list of options available based
on her elemental focus, functioning as the kineticist ability of the same name. A havocker must meet
the prerequisites of the infusion wild talent and can't accept burn (but see the spellburn ability
below).

This ability replaces the witch's hexes from 2nd level on, major hex, and grand hex.

## Spellburn {#spellburn}

Beginning at 2nd level, a havocker can channel stored spell energy into her kinetic blast to
increase the blast's overall utility and power. To use her infusions, the havocker must lose a
prepared witch spell to apply the infusion to her kinetic blast. Any spell sacrificed is required to
have a spell level equal to or greater than the infusion's effective spell level. The havocker
cannot accept additional burn if the infusion would allow her to do so.
