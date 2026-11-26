+++
id = "ref/arc-antipaladin/seal-breaker"
kind = "archetype"
title = "Seal-Breaker"
aon = "ArchetypeDisplay.aspx?FixedName=Antipaladin%20Seal-Breaker"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "seal_breaker", path = "json/archetypes_antipaladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/antipaladin" },
]
[[sources]]
publication = "inner-sea-combat"
page = "43"

[fields]
kind = "archetype"
features = [
  { anchor = "aura-of-the-grave", level = 3 },
  { anchor = "corpse-rider", level = 5 },
  { anchor = "aura-of-death", level = 8 },
  { anchor = "aura-of-rebirth", level = 11 },
  { anchor = "code-of-conduct" },
]
trades = [
  { replaces = "Aura of cowardice", feature = "aura-of-cowardice", by = ["aura-of-the-grave"] },
  { replaces = "Fiendish boon", feature = "fiendish-boon", by = ["corpse-rider"] },
  { replaces = "Aura of despair", feature = "aura-of-despair", by = ["aura-of-death"] },
  { replaces = "Aura of vengeance", feature = "aura-of-vengeance", by = ["aura-of-rebirth"] },
]
+++

Seal-breakers are dedicated to [the Whispering Tyrant](ref/monster/the-whispering-tyrant) and have
tasked themselves with finding and destroying the seals that bind him within Gallowspire. Their ties
to the Whispering Tyrant give them power over undead creatures and other dark forces.

## Aura of the Grave (Su) {#aura-of-the-grave}

At 3rd level, a seal-breaker is constantly surrounded by the chill of death. Mindless
[undead](ref/type/undead) within 10 feet of the seal-breaker will not attack him unless directly
ordered to, and even then only after succeeding at a Will save (DC = 10 + 1/2 the seal-breaker's
level + his Charisma modifier). This ability replaces aura of cowardice.

## Corpse Rider (Su) {#corpse-rider}

Upon reaching 5th level, a seal-breaker receives a boon from beyond the grave. This boon can take
one of two forms: the seal-breaker can choose to form a bond with his weapon, or he can choose to
animate an undead mount to ride.

If a bonded weapon is selected, this ability works exactly like the antipaladin's fiendish boon
ability.

If the undead mount ability is selected, the seal-breaker gains the ability to reanimate any Large
corpse (or a Medium corpse for Small seal-breakers) as his corpse mount. If no such corpse is
present, the seal-breaker cannot summon his mount. The corpse animates as a quadruped of the same
size that the seal-breaker can ride, regardless of the corpse's living form. This corpse mount
functions as a druid's [animal companion](ref/sidekick/animal-companion) using the seal-breaker's
level as his effective druid level. The mount has the same base statistics as a
[heavy horse](ref/companion/horse), [pony](ref/companion/pony), [boar](ref/companion/boar),
[camel](ref/companion/camel), or [dog](ref/companion/dog) (based on its size) with the following
changes: its type changes to undead, it has a good Will save and bad Fortitude and Reflex saves, it
uses the base creature's Constitution score as its Charisma score (and likewise applies all
level-based advancements to Charisma instead of Constitution), and it has an Intelligence score of
at least 6. This ability otherwise functions as and replaces fiendish boon.

## Aura of Death (Su) {#aura-of-death}

At 8th level, a seal-breaker radiates an aura that causes undead creatures within 10 feet to gain a
+2 profane bonus on all saving throws. This ability replaces aura of despair.

## Aura of Rebirth (Su) {#aura-of-rebirth}

At 11th level, if a living creature is slain within 10 feet of the seal-breaker, the seal-breaker
can spend two uses of his smite good ability at the start of his next turn as a standard action to
summon the spirit of a dead murderer to reanimate the corpse as a [mohrg](ref/monster/mohrg). The
mohrg immediately rises and attacks the seal-breaker's foes, acting under the antipaladin's command.
After 1 minute, the murderer's soul leaves the body, which collapses, again lifeless. At 15th level,
the seal-breaker can activate this ability as a move action. At 19th level, he can activate this
ability as a swift action. This ability replaces aura of vengeance.

## Code of Conduct {#code-of-conduct}

The seal-breaker is dedicated to releasing
[the Whispering Tyrant](ref/monster/the-whispering-tyrant) from his prison. If a seal-breaker
willingly and altruistically commits a good act, he loses all class features except proficiencies.
This doesn't mean that a seal-breaker can't take actions someone else might qualify as good, only
that such actions must always lead toward the eventual release of the Whispering Tyrant. A
seal-breaker's code requires that he place the ultimate release of Tar-Baphon above all else, as
well as impose tyranny, take advantage whenever possible, and punish the good and just (provided
such actions don't interfere with his ultimate goal).
