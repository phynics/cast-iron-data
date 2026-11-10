+++
id = "ref/arc-inquisitor/immolator"
kind = "archetype"
title = "Immolator"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Immolator"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "immolator", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "advanced-race-guide"
page = "128"

[fields]
kind = "archetype"
replaces = ["Smiting judgment", "Bane", "greater bane"]
alters = ["True judgment"]
replaces_features = ["bane", "greater-bane"]
alters_features = ["true-judgment"]
+++

The immolator puts her pyromaniacal urges to work in the service of a deity. She brings burning
retribution down upon the enemies of her faith, consigning their souls to the sacrificial flames. An
immolator has the following class features.

**Prerequisites:** Ifrit; Must worship a deity whose portfolio includes the [Fire](ref/domain/fire)
domain

**Servant of the Flame**

**Passive:** An immolator who selects the Fire domain (or one of its associated subdomains, if
available) uses her domain powers at +1 caster level (this stacks with the ifrit's fire affinity
racial trait).

**Judgment (Su)**

**Info:** An immolator gains the following judgment.

**Replaces:** Smiting judgment

**Immolation**

**Flavor:** The immolator channels purifying flame to consume her enemies.

**Passive:** When dealing fire damage to an opponent, she treats the target's fire resistance as 5
lower than normal (minimum 0).

At 6th level: She treats the target's resistance as 10 lower than normal.

At 11th level: She treats the target's resistance as 15 lower than normal.

At 16th level: She treats the target's resistance as 20 lower than normal.

**Burnt Offering (Su)**

**At 12th Level:** This ability gives the immolator's weapon the
[flaming burst](ref/magic-enh/flaming-burst) weapon special ability.

**Gained:** At 5th Level

**Replaces:** Bane, greater bane

**Swift:** An immolator can imbue one of her weapons with the [flaming](ref/magic-enh/flaming)
weapon special ability. Any creature slain by this weapon burns with magical flame; its body turns
to ash, though its equipment is not harmed. This special ability only functions while the immolator
wields the weapon.

**Usage:** 1 time/day per inquisitor level

**Judgment by Fire (Su)**

**Alters:** True judgment

**Flavor:** An immolator can call fiery judgment down upon a foe during combat.

**Gained:** At 20th Level

**Special:** Creatures killed in this manner explode in a burst of fire, dealing 10d6 points of fire
damage to every creature within 5 feet (Reflex save for half damage, DC 10 + 1/2 the immolator's
level + the immolator's Wisdom modifier). Once this ability has been used, it cannot be used again
for 1d4 rounds. This ability otherwise functions as _true judgment._

**Swift:** Whenever an immolator uses her judgment ability, she can invoke a judgment by fire on a
foe. Once declared, the immolator can make a single melee (or ranged attack, if the foe is within 30
feet) against the target. If the attack hits, the attack deals fire damage instead of weapon damage,
and the target must make a successful Fortitude save or die (creatures immune to fire do not have to
save). The DC of this save is equal to 10 + 1/2 the immolator's level + the immolator's Wisdom
modifier. Regardless of whether the save is successful, the target creature is immune to the
immolator's judgment by fire ability for 24 hours.
