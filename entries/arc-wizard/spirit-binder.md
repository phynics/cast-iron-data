+++
id = "ref/arc-wizard/spirit-binder"
kind = "archetype"
title = "Spirit Binder"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Spirit%20Binder"
source_ids = ["familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spirit_binder", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "familiar-folio"
page = "9"

[fields]
kind = "archetype"
features = [
  { anchor = "soulbound-familiar", level = 1 },
  { anchor = "arcane-school", level = 1 },
  { anchor = "lost-talents", level = 1 },
]
trades = [
  { replaces = "Scribe Scroll", feature = "scribe-scroll", by = ["lost-talents"] },
  { replaces = "bonus feats", feature = "bonus-feats", by = ["lost-talents"] },
  { alters = "Arcane bond", feature = "arcane-bond", by = ["soulbound-familiar"] },
  { alters = "Arcane school", feature = "arcane-school", by = ["arcane-school"] },
]
+++

While most wizards learn their arts through gradual study, spirit binders have made a sudden arcane
breakthrough due to the traumatic experience of losing a loved one.

## Soulbound Familiar (Ex) {#soulbound-familiar}

A spirit binder must select a [familiar](ref/ability/familiars) for his arcane bond. Unlike in a
normal familiar-summoning ritual, a spirit binder created his special familiar through a dangerous
ritual catalyzed by the death of a loved one. Before the loved one's spirit passed on to the
Boneyard, the spirit binder was able to bind the spirit to an animal or vermin, which then became
his familiar.

A soulbound familiar's personality is that of the lost loved one, rather than a servant of the
spirit binder. It can have any alignment, even one that is diametrically opposed to the spirit
binder's. A soulbound familiar has the base attack bonus and base saving throws of the loved one's
favored class (using the spirit binder's level as its level). If the loved one died before the
beginning of the campaign, the spirit binder selects the familiar's favored class at 1st level and
it cannot be changed. This ability alters arcane bond.

## Arcane School {#arcane-school}

A spirit binder can't choose necromancy as an opposition school. This ability alters arcane school.

## Lost Talents (Ex) {#lost-talents}

A spirit binder's soulbound familiar possesses some of the ability of the lost loved one, and it is
capable of learning more. At 1st level, 5th level, and every 5 levels thereafter, the spirit
binder's familiar gains a new feat for which it meets the prerequisites. This ability replaces
Scribe Scroll and the wizard's bonus feats.
