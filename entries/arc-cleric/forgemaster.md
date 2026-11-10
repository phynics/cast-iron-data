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
replaces = ["Channel energy"]
replaces_features = ["channel-energy"]
+++

Forgemasters are priestly dwarves who are ritual casters and expert enchanters, able to produce
their rune-graven armaments with astonishing speed.

**Prerequisites:** Dwarf; Worships a deity that grants the Artifice domain

**Artificer**

**Info:** A forgemaster gains only one domain, which must be the Artifice domain (not including
subdomains).

**Steel Spells**

**Info:** A forgemaster adds the following spells to her spell list at the listed spell level.

**Spells:** Crafter's curse, crafter's fortune, lead blades

**Spells:** Chill metal, heat metal, shatter

**Spells:** Keen edge, versatile weapon

**Spells:** Iron body, repel metal or stone

**Divine Smith (Su)**

**Passive:** Whenever a forgemaster casts a spell that targets a weapon, shield, or armor, the spell
takes effect at +1 caster level. If the spell has one or more metamagic feats applied, she reduces
the total level adjustment to the spell by 1 (minimum 0).

**Runeforger (Su)**

**Fullround:** A forgemaster may inscribe mystical runes upon a suit of armor, shield, or weapon.
These runes last 1 round per cleric level, but inscribing the same rune twice on an item increases
this duration to 1 minute per level, three times to 10 minutes per level, and four times to 1 hour
per level.

**Replaces:** Channel energy

**Special:** [Erase](ref/spell/erase) affects runes as magical writing. A forgemaster learns
_forgemaster's blessing_ at 1st level and may learn one additional rune at 2nd level and every 2
levels thereafter. Only one type of rune marked with an asterisk (\*) may be placed on an item at
any given time.

**Usage:** Int3 modifier times/day

**Ancient Splendor**

**Passive:** The inscribed weapon, armor, or shield grants a +2 circumstance bonus on Diplomacy and
Intimidate checks (+4 when interacting with dwarves).

**Bloodthirst\***

**Passive:** The inscribed piercing or slashing weapon functions as if it had the
[wounding](ref/magic-enh/wounding) special ability, even if nonmagical.

**Prereq:** 4th-level cleric

**Deathstrike**

**Passive:** The inscribed weapon stores a [death knell](ref/spell/death-knell) spell that triggers
immediately if a blow from the weapon reduces a target to negative hit points. This expends all
deathstrike runes on the weapon.

**Prereq:** 4th-level cleric

**Durability**

**Passive:** The inscribed item's [hardness](ref/umr/hardness) increases by an amount equal to the
forgemaster's Wisdom modifier, and its hit points increase by an amount equal to twice her level.

**Featherlight**

**Passive:** The inscribed item's weight is halved; a metal item's weight is reduced to 1/4 normal.
If inscribed on a suit of armor, its armor check penalty for Acrobatics and Climb checks is halved.

**Forgemaster's Blessing**

**Passive:** The inscribed nonmagical item functions as a masterwork item.

**Ghostglyph\***

**Passive:** The inscribed weapon, shield, or armor gains the ghost touch
([armor](ref/magic-enh/ghost-touch-armor) or [weapon](ref/magic-enh/ghost-touch-weapon)) special
ability.

**Prereq:** 4th-level cleric

**Glowglyph**

**Passive:** The inscribed item sheds light as a [torch](ref/eq-misc/torch).

**Standard:** The bearer can command the rune to erupt in a burst of light as a shield with the
[blinding](ref/magic-enh/blinding) special ability with a [burst](ref/misc/burst) radius of 5 feet
per glowglyph rune inscribed on the item. This expends all glowglyph runes on the item.

**Invulnerability\***

**Passive:** The inscribed armor grants its wearer DR/magic equal to
[half](ref/misc/fractions-and-rounding) her cleric level.

**Prereq:** 8th-level cleric

**Powerstrike\***

**Passive:** The inscribed weapon's critical threat range doubles. This does not stack with
_[keen edge](ref/spell/keen-edge),_ [Improved Critical](ref/feat/improved-critical), or similar
effects.

**Prereq:** 6th-level cleric

**Return\***

**Passive:** The inscribed weapon gains the [returning](ref/magic-enh/returning) weapon special
ability.

**Prereq:** 4th-level cleric

**Spellguard**

**Passive:** The inscribed item gains [spell resistance](ref/rule/spell-resistance) equal to 11 +
her cleric level. This applies only to effects targeting the item itself.

**Spellglyph\***

**Passive:** The inscribed weapon gains the [spell storing](ref/magic-enh/spell-storing) special
ability.

**Prereq:** 4th-level cleric

**Thief-Curse**

**Passive:** The forgemaster designates one creature as the rightful owner of an item. Any other
creature that intentionally grasps the item is cursed (as [bestow curse](ref/spell/bestow-curse))
for the duration of the rune.

**Prereq:** 6th-level cleric

**Tracer**

**Standard:** For as long as the rune lasts, the cleric may sense its location at will, as if using
[locate object](ref/spell/locate-object).

**Craft Magic Arms and Armor**

**Ability:** The forgemaster [gains this](ref/feat/craft-magic-arms-and-armor) as a bonus feat.

**Gained:** At 3rd Level

**Master Smith (Ex)**

**Gained:** At 5th Level

**Passive:** A forgemaster can craft mundane metal items quickly, using half their gp value to
determine progress, and can craft magical metal items in half the normal amount of time.
