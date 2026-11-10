+++
id = "ref/arc-bard/first-world-minstrel"
kind = "archetype"
title = "First World Minstrel"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20First%20World%20Minstrel"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "first_world_minstrel", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "11"

[fields]
kind = "archetype"
replaces = ["Bardic knowledge", "Inspire courage", "Dirge of doom", "Well-versed"]
alters = ["Spell list"]
replaces_features = ["bardic-knowledge", "well-versed"]
+++

Most cultures tell stories of people stolen away by the fey, only to return years later, forever
changed. The First World minstrel was changed in such a way by the fey, and his performances channel
the mysterious powers of the First World.

**Fey Magic**

**Alters:** Spell list

**Info:** A First World minstrel adds [summon nature's ally](ref/spell/summon-natures-ally) spells
to his spell list instead of the equivalent [summon monster](ref/spell/summon-monster) spells.

**Wild Empathy (Ex)**

**Ability:** A First World minstrel gains the [wild empathy](ref/ability/wild-empathy) druid class
feature, using his bard level as his druid level for this ability.

**Replaces:** Bardic knowledge

**Bardic Performance**

**Info:** A First World minstrel gains the following types of bardic performance.

**Echoes of the First World (Su)**

**Ability:** A First World minstrel infuses himself or a single willing ally within 30 feet with the
strange magic of the First World, granting the target one of the special abilities from the
[fey creature template](ref/template/fey-creature) other than
_[change shape](ref/carried/bestiary/rules/universal-monster-rules/change-shape)_ for 1 round.

**Replaces:** Inspire courage

**Special:** For every 3 levels beyond 1st the First World minstrel has, he can target one
additional ally or add an additional special ability to one of his targets. This is a polymorph
effect that relies on audible components.

**Gremlin's Luck (Su)**

**Ability:** A First World minstrel can use his performance to inflict bad luck on a target within
30 feet for 1 round. Whenever the target rolls an ability check, attack roll, saving throw, or skill
check, it must roll twice and take the worse result. A target that succeeds at a Will save (DC 10 +
[half](ref/misc/fractions-and-rounding) the First World minstrel's level + his Charisma modifier)
negates the effect and is immune to this ability for 24 hours.

**Replaces:** Dirge of doom

**Special:** This is a mind-affecting effect that relies on audible components.

**Resist Nature's Lure (Ex)**

**Gained:** At 2nd Level

**Passive:** A First World minstrel gains the
[resist nature's lure](ref/ability/resist-natures-lure) druid class feature.

**Replaces:** Well-versed
