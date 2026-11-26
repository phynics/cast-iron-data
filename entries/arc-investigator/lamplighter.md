+++
id = "ref/arc-investigator/lamplighter"
kind = "archetype"
title = "Lamplighter"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Lamplighter"
source_ids = ["heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lamplighter", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "heroes-of-the-streets"
page = "17"

[fields]
kind = "archetype"
features = [
  { anchor = "lamplighter", level = 1 },
  { anchor = "alchemical-illumination", level = 2 },
  { anchor = "ready-for-the-revelation", level = 3 },
]
trades = [
  { replaces = "Poison lore", feature = "poison-lore", by = ["alchemical-illumination"] },
  { replaces = "poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["alchemical-illumination"] },
  { replaces = "poison immunity", feature = "poison-resistance", levels = [11], by = ["alchemical-illumination"] },
  { replaces = "Keen recollection", feature = "keen-recollection", by = ["ready-for-the-revelation"] },
  { replaces = "trap sense", feature = "trap-sense", by = ["ready-for-the-revelation"] },
  { alters = "Class skills" },
]
+++

Lamplighters are investigators tasked with keeping the night streets safe and lit, and securing
darkened areas against whatever dangers lurk in the shadows. They also investigate those who seek to
hide their crimes from the light of day.

## Skills {#skills}

Perform and Profession are not class skills for a lamplighter. This ability alters the
investigator's class skills.

## Lamplighter (Su) {#lamplighter}

At 1st level, a lamplighter can take a move action to create a small flame that immediately ignites
a lamp, torch, or similar flammable item he's holding.

## Alchemical Illumination (Sp) {#alchemical-illumination}

At 2nd level, as a standard action, a lamplighter can cast certain [light](ref/spelldef/light)
spells by burning a magic extract, infusion, or potion of a spell of the same or greater level than
the [light](ref/spell/light) spell in a lit lantern or torch. If the spell has a range of touch, the
lantern or torch counts as the object touched. The spell's DC, if any, equals 10 + spell level + the
lamplighter's Intelligence modifier. At 2nd level, the lamplighter can cast _light_ and
_[continual flame](ref/spell/continual-flame)_ (24 hour duration). At 5th level, the lamplighter can
cast _[daylight](ref/spell/daylight)_ and _[discovery torch](ref/spell/discovery-torch)_. At 8th
level, the lamplighter can cast _[searing light](ref/spell/searing-light)_. At 11th level, the
lamplighter can cast _[judgment light](ref/spell/judgment-light)_. The lamplighter need not have an
active judgment to cast this spell, can choose what color of _judgment light_ is created, can use
his alignment for golden light, and can select any element for copper light. This ability replaces
poison lore, poison resistance, and poison immunity.

## Ready for the Revelation (Ex) {#ready-for-the-revelation}

At 3rd level, a lamplighter can use inspiration on initiative checks without spending a use of
inspiration. He can use his Intelligence modifier in place of his Dexterity modifier on initiative
checks. At 6th level, if the lamplighter has [Quick Draw](ref/feat/quick-draw), he can draw a weapon
as part of his initiative check. At 9th level, the lamplighter isn't
[flat-footed](ref/rule/flat-footed) before he acts in the first round of combat. At 12th level, the
lamplighter adds his Intelligence bonus as well as his Dexterity bonus to initiative checks. At 15th
level, the lamplighter can act last during the surprise round even if he is otherwise unaware combat
has started. At 18th level, the lamplighter is not limited to just a move or standard action during
the surprise round—he can act normally. This ability replaces keen recollection and trap sense.
