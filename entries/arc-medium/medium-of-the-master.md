+++
id = "ref/arc-medium/medium-of-the-master"
kind = "archetype"
title = "Medium of the Master"
aon = "ArchetypeDisplay.aspx?FixedName=Medium%20Medium%20of%20the%20Master"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "medium_of_the_master", path = "json/archetypes_medium.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/medium" },
]
[[sources]]
publication = "martial-arts-handbook"
page = "5"

[fields]
kind = "archetype"
features = [
  { anchor = "unarmed-strike" },
  { anchor = "dedicated-spirit" },
  { anchor = "dedicated-surge" },
  { anchor = "spirit-call" },
  { anchor = "master-s-power" },
  { anchor = "shared-prowess", level = 2 },
  { anchor = "master-s-strike", level = 6 },
  { anchor = "ki-contact", level = 15 },
  { anchor = "master-s-style", level = 17 },
]
trades = [
  { replaces = "Shared seance", feature = "shared-seance", by = ["shared-prowess"] },
  { replaces = "Trance of three", feature = "trance-of-three", by = ["ki-contact"] },
  { alters = "Armor proficiency", feature = "weapon-and-armor-proficiencies", power = "armor" },
  { alters = "Spirit", feature = "spirit", by = ["dedicated-spirit"] },
  { alters = "Spirit surge", feature = "spirit-surge", by = ["dedicated-surge"] },
  { alters = "Spirit power (lesser)", by = ["master-s-power"] },
  { alters = "Spirit power (intermediate)", by = ["master-s-strike"] },
  { alters = "Spirit power (supreme)", by = ["master-s-style"] },
  { alters = "Class skills" },
]
+++

A medium of the master forgoes a connection with most spirits to form a bond with the spirits of
great martial artists.

## Class Skills {#class-skills}

A medium of the master gains Acrobatics as a class skill, but does not gain Use Magic Device as a
class skill.

This alters the medium's class skills.

## Armor Proficiency {#armor-proficiency}

A medium of the master is proficient with only light armor.

This alters the medium's armor proficiency.

## Unarmed Strike {#unarmed-strike}

A medium of the master gains [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a bonus
feat.

## Dedicated Spirit (Su) {#dedicated-spirit}

A medium of the master can channel only a [champion](ref/spirit/champion) spirit. A medium of the
master can channel that spirit in places of quiet introspection, such as a Darklands grotto,
peaceful glade, or windswept peak, in addition to a champion spirit's favored locations.

This alters spirit.

## Dedicated Surge (Su) {#dedicated-surge}

A medium of the master can use her spirit surge ability twice per day without incurring any
influence (this stacks with any additional uses she gains from accepting a taboo, starting at 2nd
level). In addition, when she uses spirit surge, the die she rolls is one step larger (1d8 at 1st
level, 1d10 at 10th level, and 2d6 at 20th level).

This alters spirit surge.

## Spirit Call (Su) {#spirit-call}

The medium of the master's unique bond allows her to briefly call on a champion spirit without
performing a seance. As a standard action, she can allow a spirit to gain 1 point of influence over
her to channel it for a number of minutes equal to her level. This influence remains for 24 hours,
stacking with any influence the medium gains by using this ability multiple times or by channeling a
spirit in a seance during that time.

## Master's Power (Su) {#master-s-power}

When a medium of the master channels a champion spirit, she treats her unarmed strike damage as that
of a [monk](ref/class/monk) of her level. For the purpose of determining damage, these levels stack
with levels from any other class that grants increased damage to unarmed strikes.

This alters spirit power (lesser).

## Shared Prowess (Su) {#shared-prowess}

At 2nd level, a medium of the master's spirit endows her with greater martial expertise. She gains a
dodge bonus to AC equal to her spirit bonus as long as she is wearing light or no armor.

This replaces shared seance.

## Master's Strike (Su) {#master-s-strike}

At 6th level, when a medium of the master gains the intermediate power granted by her champion
spirit, she also learns one type of style strike (_Pathfinder RPG Pathfinder Unchained_ 18).
Whenever she gains an additional attack from sudden attack, she can designate one of the blows as a
style strike as long as she makes it with an unarmed strike. She can select a different style strike
each time she channels a champion spirit.

This alters spirit power (intermediate).

## Ki Contact (Su) {#ki-contact}

At 15th level, as a swift action, a medium of the master can allow her spirit to gain 1 point of
influence over her in order to gain a ki power (_Pathfinder Unchained_ 16) and a number of ki points
equal to her Charisma modifier (minimum 1) until the spirit leaves her body. She uses her medium
levels as monk levels for the purposes of meeting the ki power's prerequisites and any
level-dependent benefits of the power. Multiple uses of this ability stack, allowing her to select
one power to serve as a prerequisite for another.

This replaces trance of three.

## Master's Style (Su) {#master-s-style}

At 17th level, when a medium of the master channels a champion spirit, she gains a bonus style feat
and the two feats in that style's feat path. She does not have to meet the prerequisites for these
feats.

This alters spirit power (supreme).
