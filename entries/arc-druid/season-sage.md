+++
id = "ref/arc-druid/season-sage"
kind = "archetype"
title = "Season Sage"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Season%20Sage"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "season_sage", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "season-s-touch", level = 4 },
  { anchor = "season-s-veil", level = 6 },
  { anchor = "season-mastery", level = 12 },
]
trades = [
  { replaces = "Wild shape", feature = "wild-shape", by = ["season-s-touch"] },
]
+++

Season sages wander as the seasons change, turning the leaves and transforming nature as they pass
and taking pleasure in the transition between seasons.

## Season's Touch (Su) {#season-s-touch}

At 4th level, a season sage can infuse living things with the essence of a season with a touch,
causing them to manifest the changes associated with that season—for example, a touch of winter can
make some animals grow a thick winter coat, while a touch of summer can make them shed. A touch of
autumn would make a deciduous tree's leaves change colors, a touch of winter would make its leaves
fall, and a touch of spring would make it put forth new leaves. In addition, a season sage can use
the following abilities (in any combination) a total number of times per day equal to 1 + his Wisdom
modifier.

This replaces wild shape.

### Vernal Growth {#vernal-growth}

A touched living creature gains the effects of _[enlarge person](ref/spell/enlarge-person)_ (even if
it is not a humanoid) for 1 minute per druid level. A touched non-creature plant likewise doubles in
all dimensions for the same duration.

### Summer Might {#summer-might}

A touched creature gains a +4 enhancement bonus to Constitution for 1 minute per druid level.

### Autumn Rot {#autumn-rot}

A touched creature or object made of plant matter takes 1d6 points of acid damage per 2 druid
levels.

### Winter Frost {#winter-frost}

A touched creature or object takes 1d6 points of cold damage per 2 druid levels.

## Season's Veil (Su) {#season-s-veil}

At 6th level, a season sage can radiate an aura of seasonal power as a standard action once per day.
This affects a 20-foot-radius [burst](ref/misc/burst) centered on the season sage and lasts in that
area for 10 minutes, regardless of where the season sage moves afterward. At 8th level and every 2
levels thereafter, the season sage can use this ability an additional time per day. At 10th level,
the radius increases to 40 feet.

### Vernal Bloom {#vernal-bloom}

The area surges with life. Plants form vibrant, [heavy undergrowth](ref/rule/forest-terrain) (see
page 426 of the _Pathfinder RPG Core Rulebook_) while in the aura. If the area can support plants, a
circle of minor plants lingers afterward. At 8th level, the season sage can affect the area with
_[plant growth](ref/spell/plant-growth)_ as a swift action at will, which can linger after the aura
passes.

### Summer Heat {#summer-heat}

The area of effect is treated as if it were under the effects of
[extreme heat](ref/rule/heat-dangers). At 8th level, as a swift action the season sage can have the
area deal 1d6 points of fire damage each round to other creatures in the area.

### Autumn Squall {#autumn-squall}

The area is filled with fog, rain, and blown leaves. All creatures in the area gain
[concealment](ref/rule/concealment) (abilities to specifically see through fog or rain don't apply).
At 8th level, the season sage can affect the area with
_[diminish plants](ref/spell/diminish-plants)_ as a swift action at will, which also lingers after
the aura passes.

### Winter Chill {#winter-chill}

The area of effect is treated as if it were under the effects of
[extreme cold](ref/rule/cold-dangers). At 8th level, as a swift action the season sage can have the
area deal 1d6 points of cold damage each round to other creatures in the area.

## Season Mastery (Sp) {#season-mastery}

At 12th level, a season sage can cast _[control weather](ref/spell/control-weather)_ as a
[spell-like ability](ref/umr/spell-like-abilities) once per day; his choice of effects is not
limited by the season.
