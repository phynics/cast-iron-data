+++
id = "ref/arc-druid/aerie-protector"
kind = "archetype"
title = "Aerie Protector"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Aerie%20Protector"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aerie_protector", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "47"

[fields]
kind = "archetype"
features = [
  { anchor = "nature-bond", level = 1 },
  { anchor = "wild-empathy", level = 1 },
  { anchor = "sky-and-stone", level = 2 },
  { anchor = "wind-at-her-back", level = 4 },
  { anchor = "wild-shape", level = 6 },
  { anchor = "in-the-wind", level = 9 },
]
trades = [
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["sky-and-stone"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["wind-at-her-back"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["in-the-wind"] },
  { alters = "Weapon and armor proficiency", feature = "weapon-and-armor-proficiencies" },
  { alters = "Nature bond", feature = "nature-bond", by = ["nature-bond"] },
  { alters = "Wild empathy", feature = "wild-empathy", by = ["wild-empathy"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
]
+++

The aerie protector guards nature's nests and lairs in the highest mountains, and she is only ever
truly at ease when under vast expanses of open sky.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Aerie protectors are proficient with [javelins](ref/eq-weapon/javelin) and
[shortbows](ref/eq-weapon/shortbow) but not with scimitars or scythes. Aerie protectors are not
proficient with medium armor.

This alters the druid's weapon and armor proficiency.

## Nature Bond {#nature-bond}

If the aerie protector chooses an animal companion as her nature bond, she must choose an animal
with a fly speed. She can use spells or other effects to alter her companion's fly speed, but it
must be able to fly on its own before it becomes her companion.

If the aerie protector chooses a domain as her nature bond, she must choose the
[Air](ref/domain/air), [Eagle](ref/druiddomain/eagle), [Earth](ref/domain/earth),
[Mountain](ref/druiddomain/mountain), or [Weather](ref/domain/weather) domain.

This alters nature bond.

## Wild Empathy (Ex) {#wild-empathy}

An aerie protector gains a +4 bonus on wild empathy checks on flying animals, but she takes a -4
penalty on checks on other animals.

This alters wild empathy.

## Sky and Stone (Ex) {#sky-and-stone}

At 2nd level, an aerie protector gains a bonus equal to [half](ref/misc/fractions-and-rounding) her
level on Knowledge (geography) and Survival checks involving mountainous terrain or high altitudes,
and she cannot be tracked in such an environment.

This replaces woodland stride.

## Wind at Her Back (Su) {#wind-at-her-back}

At 4th level, an aerie protector gains a +4 bonus to CMD and on saving throws against the effects of
high altitude and effects that rely on air pressure or strong wind to move her or impede her flight.
This bonus also applies on Reflex saves against effects that deal electricity damage.

This replaces resist nature's lure.

## Wild Shape {#wild-shape}

An aerie protector gains this ability at 6th level, except her effective druid level is her druid
level - 2. If she takes on the form of a flying animal, she instead uses her druid level + 2.

## In the Wind (Ex) {#in-the-wind}

At 9th level, the climb and fly speeds of forms the aerie protector assumes with her wild shape
ability (if any) increase by 10 feet. The maneuverability of her flying forms improves by one
category.

This replaces venom immunity.
