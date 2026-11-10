+++
id = "ref/arc-slayer/spawn-slayer"
kind = "archetype"
title = "Spawn Slayer"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Spawn%20Slayer"
source_ids = ["blood-of-the-ancients"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spawn_slayer", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "blood-of-the-ancients"
page = "24"

[fields]
kind = "archetype"
replaces = ["The ability to study an opponent as a swift action at 7th level", "Stalker", "Master slayer"]
alters = ["Studied target"]
+++

Generations of Ninshaburian warriors fought the Spawn of Rovagug, holding the line against
impossible odds. Some of their ancient techniques persist to this day.

**Studied Spawn (Ex)**

**Alters:** Studied target

**Flavor:** A spawn slayer specializes in fighting against larger, single targets.

**At 10th Level:** If the target is Huge or larger, the bonuses increase by an additional 2.

**At 15th Level:** If the target is Gargantuan or larger, the bonuses increase by an additional 3.

**At 20th Level:** If the target is Colossal in size, the bonuses increase by an additional 4.

**At 5th Level:** The bonuses on weapon attack rolls, damage rolls, and skill checks against a
_studied target_ increase by [one-fifth](ref/misc/fractions-and-rounding) of his slayer level, as do
the DCs of slayer abilities against a _studied target._ If the target is Large or larger, these
bonuses increase by an additional 1.

**Replaces:** The ability to study an opponent as a swift action at 7th level

**Special:** A spawn slayer cannot maintain these bonuses against more than one target at a time.

**Gain Leverage (Ex)**

**Flavor:** A spawn slayer learns techniques to counteract a foe's size advantage.

**Gained:** At 7th Level

**Passive:** When performing a combat maneuver against a _studied target_ of Large or larger size,
the spawn slayer gains a bonus on the check equal to the creature's size modifier to CMB (Large +1,
Huge +2, Gargantuan +4, and Colossal +8). The spawn slayer adds this same bonus to his CMD when
defending against combat maneuvers from a Large or larger _studied target._

**Replaces:** Stalker

**Force Vulnerability (Ex)**

**Flavor:** A spawn slayer can create an opening in even an invulnerable foe's defenses.

**Gained:** At 20th Level

**Replaces:** Master slayer

**Special:** Whether or not the target fails this save, it cannot be targeted by _force
vulnerability_ again (by you or another slayer) for 24 hours.

**Standard:** He can make a single attack against a _studied target_ at his full attack bonus. If
the attack hits, the damage bypasses any [damage reduction](ref/rule/damage-reduction) and the
target must succeed at a Will saving throw (DC 10 + half the slayer's level + the slayer's
Intelligence modifier) or lose one of its defensive abilities for 2d6 rounds. The slayer can choose
which defensive ability is lost from the following options: a single immunity, all resistances,
regeneration, or [spell resistance](ref/rule/spell-resistance).
