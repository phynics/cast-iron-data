+++
id = "ref/arc-druid/aerie-protector"
kind = "archetype"
title = "Aerie Protector"
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
replaces = ["Woodland stride", "Resist nature's lure", "Venom immunity"]
alters = ["Weapon and armor proficiency", "Nature bond", "Wild empathy", "Wild shape"]
replaces_features = ["woodland-stride", "resist-nature-s-lure", "venom-immunity"]
alters_features = ["nature-bond", "wild-empathy", "wild-shape"]
+++

The aerie protector guards nature's nests and lairs in the highest mountains, and she is only ever
truly at ease when under vast expanses of open sky.

**Weapon and Armor Proficiency**

**Alters:** Weapon and armor proficiency

**Info:** Aerie protectors are proficient with [javelins](ref/eq-weapon/javelin) and
[shortbows](ref/eq-weapon/shortbow) but not with scimitars or scythes. Aerie protectors are not
proficient with medium armor.

**Nature Bond**

**Action:** Choice

**Alters:** Nature bond

If the aerie protector chooses an animal companion as her nature bond, she must choose an animal
with a fly speed. She can use spells or other effects to alter her companion's fly speed, but it
must be able to fly on its own before it becomes her companion.

If the aerie protector chooses a domain as her nature bond, she must choose the
[Air](ref/domain/air), [Eagle](ref/druiddomain/eagle), [Earth](ref/domain/earth),
[Mountain](ref/druiddomain/mountain), or [Weather](ref/domain/weather) domain.

**Wild Empathy (Ex)**

**Alters:** Wild empathy

**Passive:** An aerie protector gains a +4 bonus on _wild empathy_ checks on flying animals, but she
takes a -4 penalty on checks on other animals.

**Sky and Stone (Ex)**

**Gained:** At 2nd Level

**Passive:** An aerie protector gains a bonus equal to [half](ref/misc/fractions-and-rounding) her
level on Knowledge (geography) and Survival checks involving mountainous terrain or high altitudes,
and she cannot be tracked in such an environment.

**Replaces:** Woodland stride

**Wind at Her Back (Su)**

**Gained:** At 4th Level

**Passive:** An aerie protector gains a +4 bonus to CMD and on saving throws against the effects of
high altitude and effects that rely on air pressure or strong wind to move her or impede her flight.
This bonus also applies on Reflex saves against effects that deal electricity damage.

**Replaces:** Resist nature's lure

**Wild Shape**

**Ability:** An aerie protector gains _wild shape,_ except her effective druid level is her druid
level - 2. If she takes on the form of a flying animal, she instead uses her druid level + 2.

**Alters:** Wild shape

**Gained:** At 6th Level

**In the Wind (Ex)**

**Gained:** At 9th Level

**Passive:** The climb and fly speeds of forms the aerie protector assumes with her _wild shape_
ability (if any) increase by 10 feet. The maneuverability of her flying forms improves by one
category.

**Replaces:** Venom immunity
