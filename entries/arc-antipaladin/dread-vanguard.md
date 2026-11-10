+++
id = "ref/arc-antipaladin/dread-vanguard"
kind = "archetype"
title = "Dread Vanguard"
aon = "ArchetypeDisplay.aspx?FixedName=Antipaladin%20Dread%20Vanguard"
source_ids = ["champions-of-corruption"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dread_vanguard", path = "json/archetypes_antipaladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/antipaladin" },
]
[[sources]]
publication = "champions-of-corruption"
page = "22"

[fields]
kind = "archetype"
replaces = ["Spells", "Aura of sin"]
replaces_features = ["spells", "aura-of-sin"]
+++

Some antipaladins serve or ally themselves with villains who are bent on earthly conquest. They care
nothing for the intricacies of divine spellcasting, but malevolent energy still surrounds them.
Whether alone or at the head of a marauding host, these cruel warriors bring suffering and death -
but their presence also heralds the coming of a greater evil.

Dread vanguards have the following class features.

**Beacon of Evil (Su)**

**Flavor:** A dread vanguard unleashes the powers of his vile masters to strengthen both himself and
his allies.

**At 12th Level:** The dread vanguard now gains three additional uses of his _touch of corruption_
ability per day. When he activates _beacon of evil,_ a dread vanguard can choose to increase the
radius of one antipaladin aura he possesses to 30 feet. Also, the morale bonus granted to AC and on
attack rolls, damage rolls, and saving throws against fear increases to +2.

**At 16th Level:** The dread vanguard now gains four additional uses of his _touch of corruption_
ability per day. The [fast healing](ref/umr/fast-healing) granted by _beacon of evil_ increases
to 5. Additionally, the antipaladin's weapons and those of his allies within the aura's radius are
considered evil for the purpose of overcoming [damage reduction](ref/rule/damage-reduction).

**At 20th Level:** The dread vanguard now gains five additional uses of his _touch of corruption_
ability per day. The _beacon of evil's_ radius increases to 60 feet, and the morale bonus granted to
AC and on attack rolls, damage rolls, and saving throws against fear increases to +4. Lastly,
attacks made by the dread vanguard and his allies within the aura's radius are infused with pure
unholy power, and deal an additional 1d6 points of damage.

**At 8th Level:** The dread vanguard now gains two additional uses of his _touch of corruption_
ability per day. The _beacon of evil_ aura grants [fast healing](ref/umr/fast-healing) 3 to the
dread vanguard as well as to his allies while they remain within it. Additionally, while this aura
is active, the antipaladin can use his _touch of corruption_ ability against any targets within its
radius by making a ranged touch attack.

**Gained:** At 4th Level

**Passive:** A dread vanguard gains one additional use of his _touch of corruption_ ability per day.

**Replaces:** Spells

**Special:** A dread vanguard does not gain any spells or spellcasting abilities, cannot use spell
trigger or spell completion magic items, and does not have a caster level from this class.

**Standard:** He can spend a use of his _touch of corruption_ ability to manifest the darkness in
his soul as an area of flickering shadows with a 30-foot radius centered on him. These shadows don't
affect visibility. The antipaladin and all allies in the area gain a +1 morale bonus to AC and on
attack rolls, damage rolls, and saving throws against fear, and also ignore the first 5 points of
[hardness](ref/umr/hardness) when attacking unattended inanimate objects. This lasts for 1 minute,
as long as the dread vanguard is conscious.

**Dark Emissary (Sp)**

**Ability:** Once per day, the dread vanguard can expend two uses of his _touch of corruption_
ability to mark one location within 60 feet with the stain of evil. This location can be any point
in space, but the ability works best if placed on an altar, shrine, or other site important to a
community. The location is affected as if by a [desecrate](ref/spell/desecrate) spell. Creatures
approaching within 30 feet of the site must succeed at a Will save or suffer the effects of
[crushing despair](ref/spell/crushing-despair). Marking a new site ends all effects on the previous
site.

**Flavor:** A dread vanguard becomes a true messenger of the forces of darkness he serves.

**At 17th Level:** The dread vanguard can also mark the site with a
[symbol of pain](ref/spell/symbol-of-pain), and can mark two sites simultaneously. If he marks a
third, all effects on the oldest active site end.

**At 20th Level:** The dread vanguard can also mark the site wity a
[symbol of weakness](ref/spell/symbol-of-weakness), and can mark three sites simultaneously. If he
marks a fourth, all effects on the oldest active site end.

**Gained:** At 14th Level

**Passive:** Allies or evil creatures who serve the same power or organization as the dread vanguard
are immune to the _[crushing despair](ref/spell/crushing-despair)_ and symbol effects, and
automatically know that the location has been marked for their masters. They can treat this location
as very familiar for the purpose of [teleport](ref/spell/teleport) and similar spells and can use
[scrying](ref/spell/scrying) and related spells as though they were familiar with any subject within
20 feet of it.

**Replaces:** Aura of sin

**Special:** If available, all three of these effects overlap. Creatures must save against each
effect individually, and the effects stack. The caster level for all effects is equal to the dread
vanguard's class level. The save DC is equal to 10 + [half](ref/misc/fractions-and-rounding) the
antipaladin's level + his Charisma modifier. A location remains marked in this way for up to 1 day
per antipaladin level. During this time, the _[crushing despair](ref/spell/crushing-despair)_ and
_symbols_ are triggered when the first target enters each spell's area. They remain active for 10
minutes, then can be triggered again if targets are within range. If the effects are disabled, they
become inactive for 10 minutes, but then can be triggered again as normal.
[Dispel magic](ref/spell/dispel-magic) and similar spells suppress the effects, and all effects of
dark emissary can be removed by a [consecrate](ref/spell/consecrate) spell cast on the location by a
cleric of a level equal to or higher than the dread vanguard.
