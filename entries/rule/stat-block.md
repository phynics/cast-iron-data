+++
id = "ref/rule/stat-block"
kind = "rule"
title = "Stat Block"
source_ids = ["bestiary"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stat_block", path = "json/rules_gm07.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder RPG Bestiary pg 5

This is where you'll find all of the information you need to run the monster in an encounter. A stat
block is organized as follows. Note that in cases where a line in a stat block has no value, that
line is omitted.

**Name and CR:** The monster's name is presented first, along with its challenge rating (CR).
Challenge rating is a numerical indication of how dangerous a monster is: the higher the number, the
deadlier the creature. Challenge rating is detailed in the
[Designing Encounters](ref/rule/designing-encounters) section.

**XP:** Listed here are the total experience points that PCs earn for defeating the monster.

**Race, Class, and Level:** Some monsters do not possess racial Hit Dice and are instead defined by
their class levels. For these monsters, their race, class, and level appear here. Unless otherwise
noted, the first class listed is the class chosen by the monster as its favored class.

**Alignment, Size, and Type:** While a monster's size and type remain constant (unless changed by
the application of [templates](ref/rule/templates) or other unusual modifiers), alignment is far
more fluid. The alignments listed for each monster represent the norm for those monsters - they can
vary as you require them to in order to serve the needs of your campaign. Only in the case of
relatively unintelligent monsters (creatures with an Intelligence of 2 or lower are almost never
anything other than neutral) and planar monsters (outsiders with alignments other than those listed
are unusual and typically outcasts from their kind) is the listed alignment relatively unchangeable.

**Init and Senses:** The creature's initiative modifier followed by any special senses and its
Perception check modifier.

**Aura:** If the creature has a particular magical or exceptional aura, it is listed here along with
its radius from the creature and, as applicable, a save DC to resist the aura's effects.

**AC:** The creature's Armor Class, touch Armor Class, and flat-footed Armor Class. The modifiers
that generate its AC are listed parenthetically at the end of this entry.

**hp:** The creature's hit points, followed by its Hit Dice (including modifiers from Constitution,
favored class levels, creature type modifiers, and the [Toughness](ref/feat/toughness) feat).
Creatures with PC class levels receive maximum hit points for their first HD, but all other HD rolls
are assumed to be average. [Fast healing](ref/umr/fast-healing) and
[regeneration](ref/umr/regeneration) values, if any, follow the creature's HD.

**Saving Throws:** The creature's Fortitude, Reflex, and Will saves, followed by situational
modifiers to those rolls.

**Defensive Abilities/DR/Immune/Resist/SR:** All of the creature's unusual defensive abilities.
[Damage reduction](ref/rule/damage-reduction), [immunities](ref/umr/immunity),
[resistances](ref/umr/resistance), and [spell resistance](ref/rule/spell-resistance) are called out
separately as necessary.

**Weaknesses:** All of the creature's unusual weaknesses are listed here.

**Speed:** The creature's land speed, and additional speeds as necessary for the creature.

**Melee:** The creature's melee attacks are listed here, with its attack roll modifier listed after
the attack's name followed by the damage in parentheses.

**Ranged:** As Melee above, but for ranged attacks.

**Space/Reach:** The creature's space and reach - if the creature's space and reach are standard
(one 5-foot square and a reach of 5 feet), this line is omitted.

**Special Attacks:** The creature's special attacks. Full details for these attacks are given at the
end of the stat block or in the universal monster rules section.

**Spell-Like Abilities:** After listing the caster level of the creature's
[spell-like abilities](ref/umr/spell-like-abilities), this section lists all of the creature's
spell-like abilities, organized by how many times per day it can use the abilities. Constant
spell-like abilities function at all times but can be [dispelled](ref/spell/dispel-magic). A
creature can reactivate a constant spell-like ability as a swift action.

**Spells Known/Prepared:** If the creature can actually cast spells, its caster level is indicated
here followed by the spells it knows or typically has prepared. Unless otherwise indicated, a
spellcasting creature does not receive any of a spellcasting class's other abilities, such as a
cleric's ability to spontaneously convert prepared spells to _cure_ or _inflict_ spells.

**Ability Scores:** The creature's ability scores are listed here. Unless otherwise indicated, a
creature's ability scores represent the baseline of its racial modifiers applied to scores of 10
or 11. Creatures with NPC class levels have stats in the standard array (13, 12, 11, 10, 9, 8),
while creatures with character class levels have the elite array (15, 14, 13, 12, 10, 8); in both
cases, the creature's ability score modifiers are listed at the end of its description.

**Base Atk/CMB/CMD:** These values give the creature's base attack, its Combat Maneuver Bonus, and
its Combat Maneuver Defense score.

**Feats:** The creature's feats are listed here. A bonus feat is indicated with a
footnote.^[1](ref/rule/stat-block#footnote-b)^

**Skills:** The creature's skills are listed here. Racial modifiers to skills are indicated at the
end of this entry.

**Languages:** The languages most commonly spoken by the creature are listed here. For unusual
creatures, you can swap out the languages known for other choices as needed. A creature with a
higher-than-normal Intelligence score receives the appropriate number of bonus languages.

**SQ:** Any special qualities possessed by the creature.

**Environment:** The regions and climates in which the creature is typically encountered are listed
here.

**Organization:** This lists how the creature is organized, including number ranges as appropriate.

**Treasure:** The exact value of the creature's treasure depends on if you're running a slow,
medium, or fast game, as summarized on [Table 12-5](ref/rule/placing-treasure). In cases where a
creature has specific magical gear assigned to it, the assumption is a medium game; if you play a
fast or slow game, you'll want to adjust the monster's gear as appropriate. "Standard" treasure
indicates the total value of the creature's treasure is that of a CR equal to the average party
level, as listed on Table 12-5. "Double" or "triple" treasure indicates the creature has double or
triple this standard value. "Incidental" indicates the creature has half this standard value, and
then only within the confines of its lair. "None" indicates that the creature normally has no
treasure (as is typical for an unintelligent creature that has no real lair, although such creatures
are often used to guard treasures of varying amounts). "NPC gear" indicates the monster has treasure
as normal for an NPC of a level equal to the monster's CR (see [Table 14-9](ref/rule/step-6-gear)).

**Special Abilities:** Finally, any of the creature's more unique special abilities are detailed in
full here.

**Description:** Under the stat block you'll find information on how the monster fits into the
world, notes on its ecology and society, and other bits of useful lore and flavor that will help you
breathe life into the creature when your PCs encounter it. Some monsters have additional sections
that cover variant creatures, notes on using the monsters as PCs, methods of constructing the
creature, and so on.

###### ^1^ {#footnote-b}

Example of a bonus feat's footnote.
