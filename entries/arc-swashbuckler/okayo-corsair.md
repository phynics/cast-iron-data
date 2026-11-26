+++
id = "ref/arc-swashbuckler/okayo-corsair"
kind = "archetype"
title = "Okayo Corsair"
aon = "ArchetypeDisplay.aspx?FixedName=Swashbuckler%20Okayo%20Corsair"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "okayo_corsair", path = "json/archetypes_swashbuckler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/swashbuckler" },
]
[[sources]]
publication = "martial-arts-handbook"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "okayo-finesse", level = 1 },
  { anchor = "okayo-panache", level = 1 },
  { anchor = "deeds" },
  { anchor = "ki-panache", level = 3 },
  { anchor = "slow-fall", level = 7 },
  { anchor = "high-jump", level = 11 },
  { anchor = "abundant-step", level = 15 },
]
trades = [
  { replaces = "Weapon and armor proficiency", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Swashbuckler finesse", feature = "swashbuckler-finesse", by = ["okayo-finesse"] },
  { replaces = "Menacing swordplay", feature = "deeds", power = "menacing swordplay", by = ["ki-panache"] },
  { replaces = "Superior feint", feature = "deeds", power = "superior feint", by = ["slow-fall"] },
  { replaces = "Bleeding wound", feature = "deeds", power = "bleeding wound", by = ["high-jump"] },
  { replaces = "Dizzying defense", feature = "deeds", power = "dizzying defense", by = ["abundant-step"] },
  { alters = "Panache", feature = "panache", by = ["okayo-panache"] },
  { alters = "Bonus feats", feature = "bonus-feats" },
]
+++

An Okayo corsair practices a unique acrobatic martial art that draws inspiration from both the
mysticism of monastic combat traditions and the flair of a swashbuckler. This style originated among
pirates of the Dragon Empires and has since spread and become popular in the Shackles.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Okayo corsairs are proficient with simple weapons and all weapons from the monk
[weapon group](ref/ability/weapon-groups), as well as light armor and bucklers.

This replaces the swashbuckler's weapon and armor proficiency.

## Okayo Finesse (Ex) {#okayo-finesse}

An Okayo corsair gains the benefits of the [Weapon Finesse](ref/feat/weapon-finesse) feat with light
or one-handed melee weapons from the monk weapon group, and she can use her Charisma score in place
of Intelligence and Wisdom for the purpose of meeting prerequisites for combat feats. This ability
counts as the Weapon Finesse feat for the purpose of meeting feat prerequisites.

This replaces swashbuckler finesse.

## Okayo Panache (Ex) {#okayo-panache}

An Okayo corsair regains panache only when she confirms a critical hit or makes a killing blow with
a light or one-handed weapon from the monk weapon group. Additionally, the Okayo corsair gains the
ability to use a light or one-handed monk weapon for her swashbuckler class features, deeds, and
feats, even if the weapon is not a piercing weapon, but she can't use other light or one-handed
weapons with her class features or deeds.

This alters panache.

## Deeds {#deeds}

An Okayo corsair gains the following deeds.

## Ki Panache (Su) {#ki-panache}

At 3rd level, a power similar to a monk's ki awakens within the Okayo corsair. She can spend 1
panache point as a swift action to gain one of the following three benefits: she can make one
additional attack at her highest attack bonus when making a full attack, she can increase her speed
by 20 feet for 1 round, or she can give herself a +4 dodge bonus to AC for 1 round.

This deed replaces menacing swordplay.

## Slow Fall (Su) {#slow-fall}

At 7th level, the Okayo corsair can spend 1 panache point to slow her descent as per
_[feather fall](ref/spell/feather-fall)_, treating her swashbuckler level as her caster level,
provided that she is adjacent to a wall.

This deed replaces superior feint.

## High Jump (Su) {#high-jump}

At 11th level, so long as the Okayo corsair has at least 1 panache point, she adds her level as a
bonus on Acrobatics checks to jump and always counts as having a running start. She can spend 1
panache point as a swift action to gain a +20 bonus on Acrobatics checks to jump for 1 round.

This deed replaces bleeding wound.

## Abundant Step (Su) {#abundant-step}

At 15th level, an Okayo corsair can spend 2 panache points as a move action to move magically
between spaces, as _[dimension door](ref/spell/dimension-door)_. Her caster level for this effect is
equal to her swashbuckler level. She can't take other creatures with her when she uses this ability.

This deed replaces dizzying defense.

## Bonus Feats {#bonus-feats}

At 4th level, an Okayo corsair's swashbuckler levels are considered both fighter levels and monk
levels for the purpose of meeting combat feat prerequisites.

This alters the bonus feat class ability.
