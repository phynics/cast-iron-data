+++
id = "ref/arc-paladin/sword-of-valor"
kind = "archetype"
title = "Sword of Valor"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Sword%20of%20Valor"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sword_of_valor", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "inner-sea-magic"
page = "39"

[fields]
kind = "archetype"
features = [
  { anchor = "iomedae-worshiper" },
  { anchor = "first-into-battle", level = 2 },
  { anchor = "prayer-of-the-fourth-act", level = 6 },
  { anchor = "worthy-enemy", level = 11 },
]
trades = [
  { replaces = "Divine grace", feature = "divine-grace", by = ["first-into-battle"] },
  { replaces = "Mercy gained at 6th level", feature = "mercy", levels = [6], by = ["prayer-of-the-fourth-act"] },
  { replaces = "Aura of justice", feature = "aura-of-justice", by = ["worthy-enemy"] },
]
+++

The goddess [Iomedae](ref/faith/iomedae) was once a mortal paladin, and those holy champions who
follow her path seek to uphold her specific code of conduct in the hopes of honoring her name and
destroying evil. Valor, justice, and honor are their lifeblood, and they would sooner cut out their
own hearts than betray their comrades and faith. A sword of valor has the following class features.

## Iomedae Worshiper {#iomedae-worshiper}

A sword of valor must have Iomedae as a patron deity.

## First Into Battle (Su) {#first-into-battle}

At 2nd level, a sword of valor can spend 1 use of smite evil or lay on hands to act in the surprise
round, even if she is surprised. When the paladin makes an Initiative check, she gains a bonus to
the check equal to her Charisma bonus. This ability replaces divine grace.

## Prayer of the Fourth Act (Su) {#prayer-of-the-fourth-act}

At 6th level, by spending 1 minute leading a prayer to Iomedae, the sword of valor can spend one use
of channel energy to give living creatures in the channel burst
[temporary hit points](ref/rule/temporary-hit-points) equal to the amount that ability normally
heals. These temporary hit points last for no more than 1 hour. This replaces the paladin's mercy
gained at 6th level.

## Worthy Enemy (Su) {#worthy-enemy}

At 11th level, when a sword of valor critically hits an enemy with a smite, the target must make a
Will saving throw (DC = 10 + 1/2 the paladin's level + the paladin's Charisma bonus) or be compelled
to surrender to the paladin, as if affected by a _[suggestion](ref/spell/suggestion)_ spell (CL =
the paladin's level) to lay down arms and give up the fight. An enemy that succumbs to this ability
remains docile until it is injured by the paladin or one of his obvious allies, at which point the
compulsion to surrender immediately ends and the enemy is free to make his own choices again. If the
enemy makes the save, it is not subject to this ability for 24 hours. Worthy enemy is a
mind-affecting effect. This ability replaces aura of justice.
