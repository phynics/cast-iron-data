+++
id = "ref/carried/bestiary/monsters/dragon/metallic/silver/dragon/metallic/silver"
kind = "creature"
title = "Dragon, Metallic, Silver"
source_ids = ["bestiary"]
section = ["Monsters", "Dragon", "Metallic", "Silver", "Dragon", "Metallic"]
tags = ["small"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Bestiary/Monsters/Dragon/Metallic/Silver/Dragon/Metallic/Silver", path = "bestiary/creature/dragon_metallic_silver.json" },
]

[fields]
kind = "creature"
cr = "6"
size = "Small"
abilities = ["13", "14", "13", "14", "15", "14"]
+++

::: statblock
CR: 6
Size: Small
Race: lg dragon (cold)
Hit Dice: 7d12
Speed: 40 ft.
Ability Scores: Str 13, Dex 14, Con 13, Int 14, Wis 15, Cha 14
Environment: temperate mountains
Organization: solitary
Treasure: triple
Natural Armor: +6
Breath Weapon: cone, 2d8 cold
:::

## Special Abilities {#special-abilities}

### Change Shape {#change-shape}

::: statblock
Ability Type: Supernatural
:::

A silver dragon can assume any animal or humanoid form three times per day as if using polymorph.

### Cloudwalking {#cloudwalking}

::: statblock
Ability Type: Supernatural
:::

A very young or older silver dragon can tread on clouds or fog as though on solid ground.

### Cold Aura {#cold-aura}

::: statblock
Ability Type: Supernatural
:::

An old or older silver dragon is surrounded by an aura of cold. All creatures within 5 feet of the
dragon take 1d6 points of cold damage at the beginning of the dragon's turn. An ancient dragon's
aura extends to 10 feet. A great wyrm's aura damage increases to 2d6. A silver dragon can suppress
or activate this aura at will as a free action.

### Fog Vision {#fog-vision}

::: statblock
Ability Type: Extraordinary
:::

A juvenile or older silver dragon can see perfectly well in fog and clouds.

### Graceful Flight {#graceful-flight}

::: statblock
Ability Type: Extraordinary
:::

A young or older silver dragon's aerial maneuverability is one step better than normal.

### Paralyzing Breath {#paralyzing-breath}

::: statblock
Ability Type: Supernatural
:::

Instead of a cone of cold, a silver dragon can breathe a cone of paralyzing gas. Creatures within
the cone must succeed on a Fortitude save or be paralyzed for 1d6 rounds plus 1 round per age
category of the dragon.

### Reflective Scales {#reflective-scales}

::: statblock
Ability Type: Supernatural
:::

Any spell that targets an ancient or older silver dragon but fails to penetrate the silver dragon's
[spell resistance](ref/rule/spell-resistance) might be reflected. If the caster level check to
penetrate the dragon's spell resistance is failed by 5 or more, the spell is reflected. If the check
fails by 4 or less, the spell is merely wasted. This otherwise functions as spell turning.

### Spell-Like Abilities {#spell-like-abilities}

::: statblock
Ability Type: Spell-Like
:::

A silver dragon gains the following [spell-like abilities](ref/umr/spell-like-abilities), usable at
will upon reaching the listed age category. Very young—detect evil; Juvenile—feather fall; Adult—fog
cloud; Old—control winds; Ancient—control weather; Great wyrm—reverse gravity.

### True Courage {#true-courage}

::: statblock
Ability Type: Extraordinary
:::

A great wyrm silver dragon can fight on through pain and death. When reduced to below 0 hit points,
it remains conscious, automatically stabilizes, and can continue to act (although it is staggered).
If it takes damage or is the target of a spell that causes its death, it remains alive for 1 round
and can act normally (it is not staggered for this final round).

## Age Category {#age-category}

::: table
head = [
  [
    { text = "Age Category", header = true },
    { text = "Special Abilities", header = true },
    { text = "Caster Level\\*", header = true },
  ],
]
body = [
  [
    { text = "Wyrmling" },
    { text = "Change shape, cold subtype, immune to acid, paralyzing breath" },
    { text = "—" },
  ],
  [
    { text = "Very young" },
    { text = "Cloudwalking, _[detect evil](ref/spell/detect-evil)_" },
    { text = "—" },
  ],
  [
    { text = "Young" },
    { text = "Graceful flight" },
    { text = "1st" },
  ],
  [
    { text = "Juvenile" },
    { text = "Fog vision, _[feather fall](ref/spell/feather-fall)_" },
    { text = "3rd" },
  ],
  [
    { text = "Young adult" },
    { text = "DR 5/magic, [spell resistance](ref/rule/spell-resistance)" },
    { text = "5th" },
  ],
  [
    { text = "Adult" },
    { text = "Frightful presence, _[fog cloud](ref/spell/fog-cloud)_" },
    { text = "7th" },
  ],
  [
    { text = "Mature adult" },
    { text = "DR 10/magic" },
    { text = "9th" },
  ],
  [
    { text = "Old" },
    { text = "Cold aura, _[control winds](ref/spell/control-winds)_" },
    { text = "11th" },
  ],
  [
    { text = "Very old" },
    { text = "DR 15/magic" },
    { text = "13th" },
  ],
  [
    { text = "Ancient" },
    { text = "Reflective scales, _[control weather](ref/spell/control-weather)_" },
    { text = "15th" },
  ],
  [
    { text = "Wyrm" },
    { text = "DR 20/magic" },
    { text = "17th" },
  ],
  [
    { text = "Great wyrm" },
    { text = "True courage, _[reverse gravity](ref/spell/reverse-gravity)_" },
    { text = "19th" },
  ],
]
foot = [
  [
    { text = "\\* A silver dragon can cast cleric spells as arcane spells.", colspan = 3 },
  ],
]
:::
