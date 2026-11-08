+++
id = "ref/arc-antipaladin/seal-breaker"
kind = "archetype"
title = "Seal-Breaker"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "seal_breaker", path = "json/archetypes_antipaladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/antipaladin" },
]

[fields]
kind = "archetype"
replaces = ["Aura of cowardice", "Fiendish boon", "Aura of despair", "Aura of vengeance"]
+++

**Sources:** Inner Sea Combat pg 43\
Seal-breakers are dedicated to [the Whispering Tyrant](ref/monster/the-whispering-tyrant) and have
tasked themselves with finding and destroying the seals that bind him within Gallowspire. Their ties
to the Whispering Tyrant give them power over undead creatures and other dark forces.

**Code of Conduct**

**Info:** The seal-breaker is dedicated to releasing
[the Whispering Tyrant](ref/monster/the-whispering-tyrant) from his prison. If a sealbreaker
willingly and altruistically commits a good act, he loses all class features except proficiencies.
This doesn't mean that a seal-breaker can't take actions someone else might qualify as good, only
that such actions must always lead toward the eventual release of the Whispering Tyrant. A
seal-breaker's code requires that he place the ultimate release of Tar-Baphon above all else, as
well as impose tyranny, take advantage whenever possible, and punish the good and just (provided
such actions don't interfere with his ultimate goal).

**Aura of the Grave (Su)**

**Flavor:** A seal-breaker is constantly surrounded by the chill of death.

**Gained:** At 3rd Level

**Passive:** Mindless undead within 10 feet of the seal-breaker will not attack him unless directly
ordered to, and even then only after succeeding at a Will save (DC = 10
[half](ref/misc/fractions-and-rounding) the seal-breaker's level his Charisma modifier).

**Replaces:** Aura of cowardice

**Corpse Rider (Su)**

**Ability:** A sealbreaker receives a boon from beyond the grave. This boon can take one of two
forms: the seal-breaker can choose to form a bond with his weapon, or he can choose to animate an
undead mount to ride.

**Gained:** At 5th Level

**Replaces:** Fiendish boon

**Bonded Weapon**

**Ability:** This ability works exactly like the antipaladin's _fiendish boon_ ability.

**Undead Mount**

**Ability:** The sealbreaker gains the ability to reanimate any Large corpse (or a Medium corpse for
Small seal-breakers) as his corpse mount. If no such corpse is present, the seal-breaker cannot
summon his mount. The corpse animates as a quadruped of the same size that the seal-breaker can
ride, regardless of the corpse's living form. This corpse mount functions as a druid's
[animal companion](ref/sidekick/animal-companion) using the seal-breaker's level as his effective
druid level. The mount has the same base statistics as a [heavy horse](ref/companion/horse),
[pony](ref/companion/pony), [boar](ref/companion/boar), [camel](ref/companion/camel), or
[dog](ref/companion/dog) (based on its size) with the following changes: its type changes to
[undead](ref/type/undead), it has a good Will save and bad Fortitude and Reflex saves, it uses the
base creature's Constitution score as its Charisma score (and likewise applies all level-based
advancements to Charisma instead of Constitution), and it has an Intelligence score of at least 6.

**Aura of Death (Su)**

**Gained:** At 8th Level

**Passive:** A seal-breaker radiates an aura that causes undead creatures within 10 feet to gain a
profane bonus on all saving throws.

**Replaces:** Aura of despair

**Aura of Rebirth (Su)**

**At 15th Level:** The seal-breaker can activate this ability as a **move action**.

**At 19th Level:** He can activate this ability as a **swift action**.

**Gained:** At 11th Level

**Replaces:** Aura of vengeance

**Standard:** If a living creature is slain within 10 feet of the seal-breaker, the seal-breaker can
spend two uses of his _smite good_ ability at the start of his next turn to summon the spirit of a
dead murderer to reanimate the corpse as a [mohrg](ref/monster/mohrg). The mohrg immediately rises
and attacks the seal breaker's foes, acting under the antipaladin's command. After 1 minute, the
murderer's soul leaves the body, which collapses, again lifeless.
