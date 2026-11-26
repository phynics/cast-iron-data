+++
id = "ref/arc-cleric/forgemaster"
kind = "archetype"
title = "Forgemaster"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Forgemaster"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "forgemaster", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "advanced-race-guide"
page = "15"

[fields]
kind = "archetype"
features = [
  { anchor = "artificer" },
  { anchor = "steel-spells" },
  { anchor = "divine-smith" },
  { anchor = "runeforger", level = 1 },
  { anchor = "craft-magic-arms-and-armor", level = 3 },
  { anchor = "master-smith", level = 5 },
]
trades = [
  { replaces = "Channel energy", feature = "channel-energy", by = ["runeforger"] },
]
+++

Forgemasters are priestly dwarves who are ritual casters and expert enchanters, able to produce
their rune-graven armaments with astonishing speed.

## Artificer {#artificer}

A forgemaster gains only one domain, which must be the Artifice domain (not including subdomains).
If she worships a deity, it must grant the Artifice domain.

## Steel Spells {#steel-spells}

A forgemaster adds the following spells to her spell list (spells marked with an asterisk \[\*\] are
found in the _Advanced Player's Guide_): 1st—_crafter's curse\*, crafter's fortune\*, lead
blades\*_; 2nd—_chill metal, heat metal, shatter_; 3rd—_keen edge, versatile weapon\*_; 8th—_iron
body, repel metal or stone_.

## Divine Smith (Su) {#divine-smith}

Whenever a forgemaster casts a spell that targets a weapon, shield, or armor, the spell takes effect
at +1 caster level. If the spell has one or more metamagic feats applied, she reduces the total
level adjustment to the spell by 1 (minimum 0).

## Runeforger (Su) {#runeforger}

A forgemaster may inscribe mystical runes upon a suit of armor, shield, or weapon as full-round
action, using this ability a number of times per day equal to 3 + her Intelligence modifier. These
runes last 1 round per cleric level, but inscribing the same rune twice on an item increases this
duration to 1 minute per level, three times to 10 minutes per level, and four times to 1 hour per
level. _[Erase](ref/spell/erase)_ affects runes as magical writing. A forgemaster learns
forgemaster's blessing at 1st level and may learn one additional rune at 2nd level and every 2
levels thereafter. Only one type of rune marked with an asterisk (\*) may be placed on an item at
any given time. This ability replaces channel energy.

### Ancient Splendor {#ancient-splendor}

The inscribed weapon, armor, or shield grants a +2 circumstance bonus on Diplomacy and Intimidate
checks (+4 when interacting with dwarves).

_Bloodthirst\*_: The inscribed piercing or slashing weapon functions as if it had the
_[wounding](ref/magic-enh/wounding)_ special ability, even if nonmagical. The forgemaster must be at
least 4th level before learning this rune.

### Deathstrike {#deathstrike}

The inscribed weapon stores a _[death knell](ref/spell/death-knell)_ spell that triggers immediately
if a blow from the weapon reduces a target to negative hit points. This expends all deathstrike
runes on the weapon. The forgemaster must be at least 4th level before learning this rune.

### Durability {#durability}

The inscribed item's [hardness](ref/umr/hardness) increases by an amount equal to the forgemaster's
Wisdom modifier, and its hit points increase by an amount equal to twice her level.

### Featherlight {#featherlight}

The inscribed item's weight is halved; a metal item's weight is reduced to 1/4 normal. If inscribed
on a suit of armor, its armor check penalty for Acrobatics, Climb, and Jump checks is halved.

### Forgemaster's Blessing {#forgemaster-s-blessing}

The inscribed nonmagical item functions as a masterwork item.

_Ghostglyph\*_: The inscribed [weapon](ref/magic-enh/ghost-touch-weapon), shield, or
[armor](ref/magic-enh/ghost-touch-armor) gains the _ghost touch_ special ability. The forgemaster
must be at least 4th level before learning this rune.

### Glowglyph {#glowglyph}

The inscribed item sheds light as a [torch](ref/eq-misc/torch). As a standard action, the bearer can
command the rune to erupt in a [burst](ref/misc/burst) of light as a shield with the
_[blinding](ref/magic-enh/blinding)_ special ability with a burst radius of 5 feet per glowglyph
rune inscribed on the item. This expends all glowglyph runes on the item.

_Invulnerability\*_: The inscribed armor grants its wearer DR/magic equal to 1/2 her cleric level.
The forgemaster must be at least 8th level before learning this rune.

_Powerstrike\*_: The inscribed weapon's critical threat range doubles. This does not stack with
_[keen edge](ref/spell/keen-edge),_ [Improved Critical](ref/feat/improved-critical), or similar
effects. The forgemaster must be at least 6th level before learning this rune.

_Return\*_: The inscribed weapon gains the _[returning](ref/magic-enh/returning)_ weapon special
ability. The forgemaster must be at least 4th level before learning this rune.

### Spellguard {#spellguard}

The inscribed item gains [spell resistance](ref/rule/spell-resistance) equal to 11 + her cleric
level. This applies only to effects targeting the item itself.

_Spellglyph\*_: The inscribed weapon gains the _[spell storing](ref/magic-enh/spell-storing)_
special ability. The forgemaster must be at least 4th level before learning this rune.

### Thief-Curse {#thief-curse}

The forgemaster designates one creature as the rightful owner of an item. Any other creature that
intentionally grasps the item is cursed (as _[bestow curse](ref/spell/bestow-curse)_) for the
duration of the rune. The forgemaster must be at least 6th level before learning this rune.

### Tracer {#tracer}

For as long as the rune lasts, the cleric may sense its location at will as a standard action, as if
using _[locate object](ref/spell/locate-object)._

## Craft Magic Arms and Armor {#craft-magic-arms-and-armor}

The forgemaster [gains this](ref/feat/craft-magic-arms-and-armor) as a bonus feat at 3rd level.

## Master Smith (Ex) {#master-smith}

At 5th level, a forgemaster can craft mundane metal items quickly, using
[half](ref/misc/fractions-and-rounding) their gp value to determine progress, and can craft magical
metal items in half the normal amount of time.
