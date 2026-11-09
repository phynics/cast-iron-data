+++
id = "ref/arc-wizard/hallowed-necromancer"
kind = "archetype"
title = "Hallowed Necromancer"
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
replaces = ["Grave touch necromancy school ability", "Scribe Scroll", "5th-level bonus feat", "10th-level bonus feat", "15th-level bonus feat"]
alters = ["Arcane school", "spells", "Power over undead necromancy school ability"]
+++

Many wizards study necromancy to create undead, but some study the same arts to purge the stain of
undeath.

**Arcane School**

**Alters:** Arcane school, spells

**Info:** A hallowed necromancer must specialize in the school of
[necromancy](ref/arcaneschool/necromancy) and swear never to create undead.

**Turn Undead (Su)**

**Ability:** A hallowed necromancer must select [Turn Undead](ref/feat/turn-undead) as a bonus feat
with her _power over undead_ arcane school ability.

**Alters:** _Power over undead_ necromancy school ability

**Positive Touch (Su)**

**Ability:** A number of times per day equal to 3 + her Intelligence modifier, when she
spontaneously casts a _cure_ spell, she can either turn the effect into a ray and increase the
[range](ref/rule/range) to Close or remove the Will save but deal half the normal amount of damage.

**Replaces:** _Grave touch_ necromancy school ability, Scribe Scroll

**Standard:** A hallowed necromancer can sacrifice a prepared spell of the necromancy school to
spontaneously cast a cure spell of the same level or lower, counting the spell as a necromancy spell
rather than a conjuration spell. This _cure_ spell harms only undead; it doesn't heal the living. If
the spell requires an attack roll, it has a critical threat range of 19-20.

**Death Bane (Su)**

**Gained:** At 5th Level

**Passive:** A hallowed necromancer's _cure_ spells are [maximized](ref/feat/maximize-spell) when
used to damage undead and the save DCs of her spells cast on undead creatures are 1 higher.

**Replaces:** 5th-level bonus feat

**Swift:** She can expend 2 uses of _positive touch_ to imbue any weapon she wields with the
undead-[bane](ref/magic-enh/bane) or [ghost touch](ref/magic-enh/ghost-touch-weapon) weapon special
ability for a number of rounds equal to [one-fifth](ref/misc/fractions-and-rounding) her wizard
level. These effects apply only against undead, and only while the hallowed necromancer wields the
weapon.

If the weapon is her _arcane bond_ item, this ability costs only 1 use of _positive touch._

**Ghostbane (Su)**

**Gained:** At 10th Level

**Replaces:** 10th-level bonus feat

**Swift:** A hallowed necromancer can expend 3 uses of her _positive touch_ while casting a spell to
affect undead as if the spell were prepared with the
[Ectoplasmic Spell](ref/feat/ectoplasmic-spell), [Thanatopic Spell](ref/feat/thanatopic-spell), or
[Threnodic Spell](ref/feat/threnodic-spell) feat.

**Guarded Life (Su)**

**Immediate:** When a hallowed necromancer fails a saving throw against a death effect, energy
drain, a necromantic effect, or a negative energy effect, she can expend 2 uses of _positive touch_
to reroll it. She must accept the result of the reroll even if it's worse.

If she would take hit point damage from such an effect, she can instead expend 1 use of _positive
touch_ and sacrifice a prepared necromancy spell of 4th level or higher to reduce the damage she
takes by an amount equal to her wizard level + 10 times the spell level.

**Gained:** At 15th Level

**Replaces:** 15th-level bonus feat
