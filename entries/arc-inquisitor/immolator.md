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
features = [
  { anchor = "servant-of-the-flame" },
  { anchor = "judgment" },
  { anchor = "burnt-offering", level = 5 },
  { anchor = "judgment-by-fire", level = 20 },
]
trades = [
  { replaces = "Smiting judgment", feature = "judgment", power = "smiting", by = ["judgment"] },
  { replaces = "Bane", feature = "bane", by = ["burnt-offering"] },
  { replaces = "greater bane", feature = "greater-bane", by = ["burnt-offering"] },
  { alters = "True judgment", feature = "true-judgment", by = ["judgment-by-fire"] },
]
+++

The immolator puts her pyromaniacal urges to work in the service of a deity. She brings burning
retribution down upon the enemies of her faith, consigning their souls to the sacrificial flames. An
immolator has the following class features.

**Prerequisites:** Ifrit; Must worship a deity whose portfolio includes the [Fire](ref/domain/fire)
domain

## Servant of the Flame {#servant-of-the-flame}

An immolator must worship a deity whose portfolio includes the Fire domain. An immolator who selects
the Fire domain (or one of its associated subdomains, if available) uses her domain powers at +1
caster level (this stacks with the ifrit's fire affinity racial trait).

## Judgment (Su) {#judgment}

An immolator gains the following judgment instead of the smiting judgment.

### Immolation {#immolation}

The immolator channels purifying flame to consume her enemies. When dealing fire damage to an
opponent, she treats the target's fire resistance as 5 lower than normal (minimum 0). At 6th level,
she treats the target's resistance as 10 lower than normal, 15 lower than normal at 11th level, and
20 lower than normal at 16th level.

## Burnt Offering (Su) {#burnt-offering}

At 5th level, as a swift action, an immolator can imbue one of her weapons with the
_[flaming](ref/magic-enh/flaming)_ weapon special ability. Any creature slain by this weapon burns
with magical flame; its body turns to ash, though its equipment is not harmed. This special ability
only functions while the immolator wields the weapon. This ability lasts for a number of rounds per
day equal to the immolator's level. These rounds do not need to be consecutive. At 12th level, this
ability gives the immolator's weapon the _[flaming burst](ref/magic-enh/flaming-burst)_ weapon
special ability. This ability replaces bane and greater bane.

## Judgment by Fire (Su) {#judgment-by-fire}

At 20th level, an immolator can call fiery judgment down upon a foe during combat. Whenever an
immolator uses her judgment ability, she can invoke a judgment by fire on a foe as a swift action.
Once declared, the immolator can make a single melee (or ranged attack, if the foe is within 30
feet) against the target. If the attack hits, the attack deals fire damage instead of weapon damage,
and the target must make a successful Fortitude save or die (creatures immune to fire do not have to
save). The DC of this save is equal to 10 + 1/2 the immolator's level + the immolator's Wisdom
modifier. Regardless of whether the save is successful, the target creature is immune to the
immolator's judgment by fire ability for 24 hours. Creatures killed in this manner explode in a
burst of fire, dealing 10d6 points of fire damage to every creature within 5 feet (Reflex save for
half damage, DC 10 + 1/2 the immolator's level + the immolator's Wisdom modifier). Once this ability
has been used, it cannot be used again for 1d4 rounds. This ability modifies and functions as true
judgment.
