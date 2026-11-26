+++
id = "ref/arc-wizard/hallowed-necromancer"
kind = "archetype"
title = "Hallowed Necromancer"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Hallowed%20Necromancer"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hallowed_necromancer", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "horror-adventures"
page = "74"

[fields]
kind = "archetype"
features = [
  { anchor = "arcane-school", level = 1 },
  { anchor = "turn-undead" },
  { anchor = "positive-touch", level = 1 },
  { anchor = "deathbane", level = 5 },
  { anchor = "ghostbane", level = 10 },
  { anchor = "guarded-life", level = 15 },
]
trades = [
  { replaces = "Grave touch", feature = "arcane-school", power = "grave touch", by = ["positive-touch"] },
  { replaces = "Scribe Scroll", feature = "scribe-scroll", by = ["positive-touch"] },
  { replaces = "Bonus feat gained at 5th level", feature = "bonus-feats", levels = [5], by = ["deathbane"] },
  { replaces = "Bonus feat gained at 10th level", feature = "bonus-feats", levels = [10], by = ["ghostbane"] },
  { replaces = "15th-level bonus feat", feature = "bonus-feats", levels = [15], by = ["guarded-life"] },
  { alters = "Arcane school", feature = "arcane-school", by = ["arcane-school"] },
  { alters = "spells", feature = "spells", by = ["arcane-school"] },
  { alters = "Power over undead", feature = "arcane-school", power = "power over undead", by = ["turn-undead"] },
]
+++

Many wizards study necromancy to create undead, but some study the same arts to purge the stain of
undeath.

## Arcane School {#arcane-school}

A hallowed necromancer must specialize in the school of [necromancy](ref/arcaneschool/necromancy)
and swear never to create undead.

This alters arcane school and spells.

## Turn Undead (Su) {#turn-undead}

A hallowed necromancer must select [Turn Undead](ref/feat/turn-undead) as a bonus feat with her
power over undead arcane school ability.

This alters power over undead.

## Positive Touch (Su) {#positive-touch}

As a standard action, a hallowed necromancer can sacrifice a prepared spell of the necromancy school
to spontaneously cast a cure spell of the same level or lower, counting the spell as a necromancy
spell rather than a conjuration spell. This cure spell harms only undead; it doesn't heal the
living. If the spell requires an attack roll, it as has a critical threat [range](ref/rule/range) of
19–20. A number of times per day equal to 3 + her Intelligence modifier, when she spontaneously
casts a cure spell, she can either turn the effect into a ray and increase the range to close or
remove the Will save but deal half the normal amount of damage.

This ability replaces grave touch and Scribe Scroll.

## Deathbane (Su) {#deathbane}

At 5th level, a hallowed necromancer's cure spells are [maximized](ref/feat/maximize-spell) when
used to damage undead and the save DCs of her spells cast on undead creatures are 1 higher. She can
expend 2 uses of positive touch as a swift action to imbue any weapon she wields with the
_undead_-_[bane](ref/magic-enh/bane)_ or _[ghost touch](ref/magic-enh/ghost-touch-weapon)_ weapon
special ability for 1 round per 5 wizard levels she has. These effects apply only against undead,
and only while the hallowed necromancer wields the weapon. If the weapon is her arcane bond item,
this ability costs only 1 use of positive touch.

This ability replaces the bonus feat gained at 5th level.

## Ghostbane (Su) {#ghostbane}

At 10th level, a hallowed necromancer can expend 3 uses of her positive touch as a swift action
while casting a spell to affect undead as if the spell were prepared with the
[Ectoplasmic Spell](ref/feat/ectoplasmic-spell), [Thanatopic Spell](ref/feat/thanatopic-spell), or
[Threnodic Spell](ref/feat/threnodic-spell) feat.

This ability replaces the bonus feat gained at 10th level.

## Guarded Life (Su) {#guarded-life}

At 15th level, when a hallowed necromancer fails a saving throw against a death effect, energy
drain, a necromantic effect, or a negative energy effect, she can expend 2 uses of positive touch as
an immediate action to reroll it. She must accept the result of the reroll even if it's worse. If
she would take hit point damage from such an effect, as an immediate action she can instead expend 1
use of positive touch and sacrifice a prepared necromancy spell of 4th level or higher to reduce the
damage she takes by an amount equal to her wizard level + 10 times the spell level.

This ability replaces the 15th level bonus feat.
