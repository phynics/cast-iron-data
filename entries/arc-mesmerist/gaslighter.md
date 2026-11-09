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
replaces = ["Consummate liar", "Touch treatment (minor)", "Touch treatment (moderate)", "Touch treatment (greater)", "Touch treatment (break enchantment)"]
alters = ["Painful stare"]
+++

A gaslighter takes joy in others' suffering, delighting in driving them to madness.

**Alignment**

**Info:** A gaslighter must be of an evil alignment. A gaslighter who becomes nonevil cannot gain
new levels as a mesmerist but retains all his class abilities.

**Consummate Cruelty**

**Ability:** A gaslighter can take [Improved Dirty Trick](ref/feat/improved-dirty-trick) and
[Greater Dirty Trick](ref/feat/greater-dirty-trick) without having
[Combat Expertise](ref/feat/combat-expertise) or an Intelligence score of 13. He can also ignore
those two prerequisites for other feats that have Improved Dirty Trick or Greater Dirty Trick as a
prerequisite.

**Passive:** A gaslighter gains a bonus equal to 1/2 his mesmerist level (minimum 1) on Intimidate
checks.

**Replaces:** Consummate liar

**Horrid Mask (Su)**

**Alters:** Painful stare

**Gained:** At 3rd Level

**Replaces:** Touch treatment (minor)

**Special:** Any creature holding a visible mirror that attempts to demoralize the target can choose
to add the gaslighter's Charisma modifier to its Intimidate check instead of its own. _Horrid mask_
lasts until that particular _hypnotic stare_ ends (often when the target moves away from a mirror).

**Standard:** A gaslighter can implant a maddening phantasm in the mind of the target of his
_hypnotic stare,_ causing the target to perceive its own reflection as corrupted in some disturbing
way. This is a mind-affecting fear effect, and there is no saving throw. The target is
simultaneously captivated and horrified by the sight of its own reflection, and in any round in
which the target can see itself in a mirror within 30 feet, the gaslighter can trigger his _painful
stare_ against the target without dealing damage. This is a [gaze](ref/umr/gaze) attack, and the
creature can avert its eyes to attempt to avoid it.

**Usage:** Charisma3 modifier times/day

**Phantasmal Force (Su)**

**Ability:** A gaslighter can force the target of his _horrid mask_ ability to recoil from its
reflection. Whenever the gaslighter uses _horrid mask,_ if an affected target begins its turn
adjacent to a mirror, it must succeed at a Will save (DC = 10 + 1/2 the gaslighter's mesmerist
level + his Charisma modifier) or be compelled to either flee from the mirror (or the creature
holding it) to beyond 30 feet or attempt to destroy the mirror (or the creature holding it). This is
a gaze attack, and the target can attempt to avert its eyes.

**Gained:** At 6th Level

**Replaces:** Touch treatment (moderate)

**Phantasmal Foes (Su)**

**Gained:** At 10th Level

**Replaces:** Touch treatment (greater)

**Special:** The gaslighter can use either this ability or _horrid mask_ during a particular
_hypnotic stare,_ but not both at once. This is a mind-affecting fear effect.

**Standard:** A gaslighter can spend one use of his _horrid mask_ ability to convince the target of
his _hypnotic stare_ that it is surrounded by foes only it can see. The target is treated as
[flanked](ref/rule/flanking) for any melee attacks against it until the _hypnotic stare_ ends.

**Corosion of Sanity (Su)**

**Gained:** At 14th Level

**Passive:** Whenever a creature fails its initial saving throw against a gaslighter's single-target
mind-affecting effect, the target also takes 1 point of
[Wisdom damage](ref/rule/ability-damage-drain). This has no effect on abilities that don't allow a
saving throw or affect multiple targets or an area.

**Replaces:** Touch treatment (break enchantment)

**Special:** If using [the sanity system](ref/rule/sanity), the target takes 2 points of sanity
damage instead.
