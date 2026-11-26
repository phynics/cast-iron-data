+++
id = "ref/arc-mesmerist/gaslighter"
kind = "archetype"
title = "Gaslighter"
aon = "ArchetypeDisplay.aspx?FixedName=Mesmerist%20Gaslighter"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gaslighter", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]
[[sources]]
publication = "horror-adventures"
page = "60"

[fields]
kind = "archetype"
features = [
  { anchor = "consummate-cruelty", level = 1 },
  { anchor = "horrid-mask", level = 3 },
  { anchor = "phantasmal-force", level = 6 },
  { anchor = "phantasmal-foes", level = 10 },
  { anchor = "corrosion-of-sanity", level = 14 },
]
trades = [
  { replaces = "Consummate liar", feature = "consummate-liar", by = ["consummate-cruelty"] },
  { replaces = "Touch treatment (minor)", feature = "touch-treatment", levels = [3], by = ["horrid-mask"] },
  { replaces = "Touch treatment (moderate)", feature = "touch-treatment", levels = [6], by = ["phantasmal-force"] },
  { replaces = "Touch treatment (greater)", feature = "touch-treatment", levels = [10], by = ["phantasmal-foes"] },
  { replaces = "Touch treatment (break enchantment)", feature = "touch-treatment", levels = [14], by = ["corrosion-of-sanity"] },
  { alters = "Painful stare", feature = "painful-stare", by = ["horrid-mask"] },
]
+++

A gaslighter takes joy in others' suffering, delighting in driving them to madness.

## Alignment {#alignment}

A gaslighter must be of an evil alignment. A gaslighter who becomes nonevil cannot gain new levels
as a mesmerist but retains all his class abilities.

## Consummate Cruelty {#consummate-cruelty}

A gaslighter gains a bonus equal to 1/2 his mesmerist level (minimum 1) on Intimidate checks. A
gaslighter can take [Improved Dirty Trick](ref/feat/improved-dirty-trick) and
[Greater Dirty Trick](ref/feat/greater-dirty-trick) without having
[Combat Expertise](ref/feat/combat-expertise) or an Intelligence score of 13. He can also ignore
those two prerequisites for other feats that have Improved Dirty Trick or Greater Dirty Trick as a
prerequisite.

This ability replaces consummate liar.

## Horrid Mask (Su) {#horrid-mask}

At 3rd level, as a standard action, a gaslighter can implant a maddening phantasm in the mind of the
target of his hypnotic stare, causing the target to perceive its own reflection as corrupted in some
disturbing way. This is a mind-affecting fear effect, and there is no saving throw. The target is
simultaneously captivated and horrified by the sight of its own reflection, and in any round in
which the target can see itself in a mirror within 30 feet, the gaslighter can trigger his painful
stare against the target without dealing damage. This is a [gaze](ref/umr/gaze) attack, and the
creature can avert its eyes to attempt to avoid it. Any creature holding a visible mirror that
attempts to demoralize the target can choose to add the gaslighter's Charisma modifier to its
Intimidate check instead of its own. Horrid mask lasts until that particular hypnotic stare ends
(often when the target moves away from a mirror). The gaslighter can use this ability a number of
times per day equal to 3 + his Charisma modifier.

This ability replaces touch treatment (minor) and alters painful stare.

## Phantasmal Force (Su) {#phantasmal-force}

At 6th level, a gaslighter can force the target of his horrid mask ability to recoil from its
reflection. Whenever the gaslighter uses horrid mask, if an affected target begins its turn adjacent
to a mirror, it must succeed at a Will save (DC = 10 + 1/2 the gaslighter's mesmerist level + his
Charisma modifier) or be compelled to either flee from the mirror (or the creature holding it) to
beyond 30 feet or attempt to destroy the mirror (or the creature holding it). This is a gaze attack,
and the target can attempt to avert its eyes.

This ability replaces touch treatment (moderate).

## Phantasmal Foes (Su) {#phantasmal-foes}

At 10th level, a gaslighter can spend one use of his horrid mask ability as a standard action to
convince the target of his hypnotic stare that it is surrounded by foes only it can see. The target
is treated as [flanked](ref/rule/flanking) for any melee attacks against it until the hypnotic stare
ends. The gaslighter can use either this ability or horrid mask during a particular hypnotic stare,
but not both at once. This is a mind-affecting fear effect.

This ability replaces touch treatment (greater).

## Corrosion of Sanity (Su) {#corrosion-of-sanity}

At 14th level, whenever a creature fails its initial saving throw against a gaslighter's
single-target mind-affecting effect, the target also takes 1 point of
[Wisdom damage](ref/rule/ability-damage-drain). This has no effect on abilities that don't allow a
saving throw or affect multiple targets or an area. If using [the sanity system](ref/rule/sanity)
(see page 12), the target takes 2 points of sanity damage instead.

This ability replaces touch treatment (_break enchantment_).
