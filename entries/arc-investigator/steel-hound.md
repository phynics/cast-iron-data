+++
id = "ref/arc-investigator/steel-hound"
kind = "archetype"
title = "Steel Hound"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Steel%20Hound"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "steel_hound", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "advanced-class-guide"
page = "103"

[fields]
kind = "archetype"
features = [
  { anchor = "packing-heat", level = 2 },
  { anchor = "investigator-talents", level = 3 },
  { anchor = "shot-in-the-dark", level = 4 },
  { anchor = "talented-shot", level = 11 },
]
trades = [
  { replaces = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Poison lore", feature = "poison-lore", by = ["packing-heat"] },
  { replaces = "Swift alchemy", feature = "swift-alchemy", by = ["shot-in-the-dark"] },
  { alters = "Investigator talents", feature = "investigator-talent", by = ["investigator-talents"] },
]
+++

Black powder and firearms are a natural extension of the alchemical experimentation that
investigators use on a regular basis. Steel hounds are investigators who have taken to using
firearms in place of the more mundane weapons their counterparts favor.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Steel hounds are proficient with simple weapons, plus the [rapier](ref/eq-weapon/rapier), the
[sap](ref/eq-weapon/sap), and one type of firearm selected at 1st level. They are proficient in
light armor, but not shields. This replaces the investigator's weapon and armor proficiencies.

## Packing Heat (Ex) {#packing-heat}

At 2nd level, the steel hound gains both the [Amateur Gunslinger](ref/feat/amateur-gunslinger) and
[Gunsmithing](ref/feat/gunsmithing) feats as bonus feats. He also gains a battered gun identical to
the one gained by the [gunslinger](ref/class/gunslinger). This ability replaces poison lore.

## Investigator Talents {#investigator-talents}

The steel hound can select the [Extra Grit](ref/feat/extra-grit) or
[Rapid Reload](ref/feat/rapid-reload) feats in place of an investigator talent.

## Shot in the Dark (Ex) {#shot-in-the-dark}

At 4th level, a steel hound gains the following deed. This deed works and interacts with grit the
same way as gunslinger deeds, but only the steel hound can use it. If the steel hound also has
levels in gunslinger, he can spend grit points from that class to use this deed.

### Blind Shot (Su) {#blind-shot}

A steel hound can spend 1 grit point to ignore all miss chances due to
[concealment](ref/rule/concealment) when making firearm attacks. This effect lasts until the end of
his turn. This ability allows the steel hound to ignore concealment, but does not reveal or allow
him to see the enemy. This ability replaces swift alchemy.

## Talented Shot (Ex) {#talented-shot}

At 11th level, a steel hound can select a gunslinger deed in place of an investigator talent. He can
select from any deed available to a gunslinger of his investigator level - 4.
