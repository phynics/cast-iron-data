+++
id = "ref/arc-spiritualist/hag-haunted"
kind = "archetype"
title = "Hag-Haunted"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Hag-Haunted"
source_ids = ["blood-of-the-coven"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hag_haunted", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "blood-of-the-coven"
page = "23"

[fields]
kind = "archetype"
features = [
  { anchor = "hag-phantom", level = 1 },
  { anchor = "hag-spellcasting" },
  { anchor = "death-curse", level = 4 },
]
trades = [
  { replaces = "Shared consciousness", feature = "shared-consciousness", by = ["hag-phantom"] },
  { replaces = "fused consciousness", feature = "fused-consciousness", by = ["hag-phantom"] },
  { replaces = "Spiritual interference", feature = "spiritual-interference", by = ["death-curse"] },
  { replaces = "greater spiritual interference", feature = "greater-spiritual-interference", by = ["death-curse"] },
  { alters = "Phantom", feature = "phantom", by = ["hag-phantom"] },
]
+++

[Hags](ref/family/hag)—those of flesh and blood, at any rate—die like any other mortals, and their
souls normally depart to the Outer Planes for judgment. A hag who dies with a curse on her breath is
often anchored to the Ethereal Plane by the power of her hatred —similar to vile and angry mortal
souls—and some even claw their way back to the living world through the souls of those they despised
or ruined... or those unfortunate souls they birthed. Hag-haunted spiritualists are tethered to
these spiteful spirits, anchoring them once again in the world of the living. While this partnership
imparts powerful magic, they run the constant risk of serving as little more than mounts for their
overwhelming phantoms.

Hag-haunted spiritualists are rarely the masters in their relationship with their phantoms, and the
only tool at their disposal to control their wicked minion is to dismiss them back to the Ethereal
Plane. In the best scenarios, the relationship is one of mutual competition and constant bargaining,
but just as often the hag phantom dominates and abuses her spiritualist.

## Hag Phantom {#hag-phantom}

A hag phantom forms from the soul of a deceased hag. She always has an evil alignment, rather than
matching the spiritualist's alignment, and must select one of the following emotional focuses:
[anger](ref/emotionalfocus/anger), [hatred](ref/emotionalfocus/hatred),
[jealousy](ref/emotionalfocus/jealousy), or [zeal](ref/emotionalfocus/zeal). The hag phantom starts
with a +2 bonus to Strength and Intelligence and has her own agenda—usually contrary to the
spiritualist's—though she recognizes that the spiritualist can unmanifest her, and therefore she
typically hides suspicious actions from her spiritualist. When in the spiritualist's consciousness,
the hag phantom can grant the hag-haunted [Spell Focus](ref/feat/spell-focus) (necromancy) and
[Skill Focus](ref/feat/skill-focus) (Bluff), but she often revokes them if the spiritualist banishes
her there as a punishment, and she might use them as leverage to get what she wants. When the
spiritualist reaches 10th level, the hag can also grant these feats while manifested, and when the
spiritualist reaches 12th level, she can also grant
[Greater Spell Focus](ref/feat/greater-spell-focus) (necromancy).

This alters phantom and replaces shared consciousness and fused consciousness.

## Hag Spellcasting {#hag-spellcasting}

A hag-haunted spiritualist's spells come from her connection to her hag phantom. Her spells are
considered arcane rather than psychic, and they use verbal and somatic components instead of thought
and emotion components. She still selects her spells known from the spiritualist class list.

## Death Curse (Sp) {#death-curse}

A hag phantom is partially animated by the power of a hag's dying curse, and at 4th level this
grants her a death curse of her own. As an immediate action, whenever the hag phantom is slain and
returned to the Ethereal Plane, the phantom can utter a curse on the creature that killed her,
targeting it with _[bestow curse](ref/spell/bestow-curse)_. At 6th level, the spiritualist gains
_[bestow curse](ref/spell/bestow-curse)_ as an extra 3rd-level spell known. At 16th level, the
spiritualist gains _[major curse](ref/spell/curse-major)_ as an additional 6th-level spell known.

This replaces spiritual interference and greater spiritual interference.
