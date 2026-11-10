+++
id = "ref/arc-occultist/necroccultist"
kind = "archetype"
title = "Necroccultist"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "necroccultist", path = "json/archetypes_occultist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/occultist" },
]
[[sources]]
publication = "occult-adventures"
page = "100"

[fields]
kind = "archetype"
replaces = ["Object reading", "Aura sight", "Outside contact"]
alters = ["Implements", "implement mastery"]
replaces_features = ["object-reading", "aura-sight", "outside-contact"]
alters_features = ["implements", "implement-mastery"]
+++

Necroccultists' fascination with death and the undead drives them to explore the forbidden
necromantic arts as they search for secrets they can use to manipulate the natural cycle of life and
death. They contact and learn from the dead, rather than from items or outsiders, allowing them to
drain the life of their foes to feed their own power, and even call forth phantasmal hordes of
spirits to destroy their enemies.

**Necromantic Bond (Su)**

**Ability:** Each time he gains an occultist level, a necroccultist can add one necromancy spell
from the wizard spell list to his occultist spell list and his list of spells known. The
necroccultist can't choose a spell of a higher level than he is able to cast, and he adds the spell
at the same spell level it appears on the wizard spell list.

**Alters:** Implements, implement mastery

**At 14th Level:** He doesn't gain an additional school of implements. Instead, the DCs of saving
throws to resist a necroccultist's necromancy spells and necromancy focus powers increase by 2.

**Info:** A necroccultist gains access to only the [necromancy](ref/implement/necromancy) school of
implements. He must select necromancy for his _implement mastery._

**Gained:** At 1st Level

**Deadspeaker (Su)**

**Fullround:** A necroccultist can learn the answers to a specific set of questions concerning a
dead or undead creature. The necroccultist must consume at least one drop of the creature's blood, a
small portion of its flesh, or a fragment of one of its bones as a part of this action. This ability
otherwise functions as [blood biography](ref/spell/blood-biography), using the necroccultist's
occultist level as his caster level.

**Gained:** At 2nd Level

**Provokes attack of opportunity:** Yes

**Replaces:** Object reading

**Usage:** 1 time/day per 2 occultist levels

**Ghostly Horde (Su)**

**Gained:** At 5th Level

**Provokes attack of opportunity:** No

**Replaces:** Aura sight

**Special:** The ghostly horde remains for 1 round, though at the beginning of his turn, the
necroccultist can expend 1 point of mental focus as a **swift action** to extend the duration for 1
additional round.

**Standard:** A necroccultist can spend 1 point of mental focus from a necromancy implement to
summon a mob of ghostly spirits to harass his enemies. The ghostly horde appears within 60 feet of
the necroccultist, fills an area 20 feet in diameter, and always hovers a few inches off the ground
(thus ignoring any [difficult terrain](ref/rule/terrain-and-obstacles)). The necroccultist can
command the ghostly horde to move up to 30 feet each round as a **move action**, though the farthest
edge of the ghostly horde can never be more than 60 feet from the necroccultist. Any creature caught
inside the ghostly horde takes 1d6 points of damage per 2 occultist levels at the start of its turn
(up to a maximum of 10d6 points of damage at 20th level). A successful Fortitude save (DC = 10 + 1/2
the necroccultist's occultist level + the necroccultist's Intelligence modifier) halves this damage.
This damage is not negative energy - it manifests in the form of physical wounds and aches as if
from supernatural aging. Nonliving creatures and creatures immune to magical aging are immune to
this damage, but otherwise the damage bypasses all forms of
[damage reduction](ref/rule/damage-reduction).

**Usage:** 1 time/day per 5 occultist levels

**Life Drain (Sp)**

**Ability:** A necroccultist can expend 1 point of mental focus from a necromancy implement to
unleash a life-draining ray as a ranged touch attack that causes the target to accrue 1d4
[negative levels](ref/rule/energy-drain-and-negative-levels). The ray has a range of 60 feet. The
negative levels last a number of minutes equal to the necroccultist's occultist level.

**Gained:** At 8th Level

**Replaces:** Outside contact

**Special:** For each negative level this attack gives a target, the necroccultist regains a number
of hit points equal to his occultist level.

**Usage:** 1 time/day + 1 per 3 occultist levels beyond 8th
