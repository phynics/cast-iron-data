+++
id = "ref/arc-samurai/brawling-blademaster"
kind = "archetype"
title = "Brawling Blademaster"
aon = "ArchetypeDisplay.aspx?FixedName=Samurai%20Brawling%20Blademaster"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "brawling_blademaster", path = "json/archetypes_samurai.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/samurai" },
]
[[sources]]
publication = "martial-arts-handbook"
page = "10"

[fields]
kind = "archetype"
features = [
  { anchor = "empty-hand", level = 1 },
  { anchor = "nimble", level = 2 },
  { anchor = "dual-expertise", level = 3 },
  { anchor = "harmonious-flow", level = 4 },
  { anchor = "perfect-clarity", level = 5 },
  { anchor = "superior-focus", level = 14 },
]
trades = [
  { replaces = "Mount", feature = "mount", by = ["empty-hand"] },
  { replaces = "Weapon expertise", feature = "weapon-expertise", by = ["dual-expertise"] },
  { replaces = "Mounted archer", feature = "mounted-archer", by = ["harmonious-flow"] },
  { replaces = "Banner", feature = "banner", by = ["perfect-clarity"] },
  { replaces = "Greater banner", feature = "greater-banner", by = ["superior-focus"] },
  { alters = "Weapon and armor proficiency", feature = "weapon-and-armor-proficiencies" },
]
+++

While some martial arts traditions focus on the strength of the body, most schools of combat and
self-defense know the importance of using weapons as well. Brawling blademaster samurai use weapon
strikes and unarmed attacks in equal measure—foes expecting to defend themselves against a dagger or
a sword are often caught off guard by a brawling blademaster's brutal kicks or punches.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Brawling blademasters are proficient with all simple and martial weapons, plus the
[katana](ref/eq-weapon/katana) and [wakizashi](ref/eq-weapon/wakizashi). Brawling blademasters are
proficient with light armor, but not with shields.

This alters the samurai's weapon and armor proficiency.

## Empty Hand (Ex) {#empty-hand}

A brawling blademaster gains [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a bonus
feat. She uses her samurai level as her [monk](ref/class/monk) level for determining the amount of
damage she deals with an unarmed strike. These levels stack with monk levels to determine the
brawling blademaster's unarmed strike damage.

This replaces mount.

## Nimble (Ex) {#nimble}

At 2nd level, a brawling blademaster gains the [gunslinger's](ref/class/gunslinger) nimble class
feature (_Pathfinder RPG Ultimate Combat_ 12), using her samurai level as his gunslinger level.

## Dual Expertise (Ex) {#dual-expertise}

At 3rd level, a brawling blademaster gains [Two-Weapon Fighting](ref/feat/two-weapon-fighting) as a
bonus feat, even if she doesn't meet the prerequisites. Furthermore, when the brawling blademaster
selects a feat with the bonus feat class feature, she can ignore any Dexterity requirements for the
feat if its prerequisites include the Two-Weapon Fighting feat.

This replaces weapon expertise.

## Harmonious Flow (Ex) {#harmonious-flow}

At 4th level, the brawling blademaster becomes skilled at combining weapon attacks and unarmed
strikes into a harmonious combat style. When attacking the target of her challenge, the brawling
blademaster doesn't take the usual -2 penalty on attack rolls associated with attacking with two
weapons if her main-hand weapon is a light or one-handed manufactured weapon and her off-hand weapon
is an unarmed strike (or vice versa). While she's using this ability, one of her hands must be empty
even if she uses another body part to make an unarmed strike.

This replaces mounted archer.

## Perfect Clarity (Ex) {#perfect-clarity}

At 5th level, the brawling blademaster sees all her foes with perfect clarity even when focused on
one opponent. She no longer takes a penalty to her AC during a challenge.

This ability replaces banner.

## Superior Focus (Ex) {#superior-focus}

At 14th level, the brawling blademaster gains a +2 bonus on saving throws during a challenge.

This replaces greater banner.
