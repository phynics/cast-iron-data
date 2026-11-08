+++
id = "ref/arc-paladin/sword-of-valor"
kind = "archetype"
title = "Sword of Valor"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sword_of_valor", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]

[fields]
kind = "archetype"
replaces = ["Divine grace", "6th-level mercy", "Aura of justice"]
+++

**Sources:** Inner Sea Magic pg 39\
The goddess Iomedae was once a mortal paladin, and those holy champions who follow her path seek to
uphold her specific code of conduct in the hopes of honoring her name and destroying evil. Valor,
justice, and honor are their lifeblood, and they would sooner cut out their own hearts than betray
their comrades and faith. A sword of valor has the following class features.

**Prerequisites:** Must have [Iomedae](ref/faith/iomedae) as a patron deity

**First Into Battle (Su)**

**Ability:** A sword of valor can spend 1 use of _smite evil_ or _lay on hands_ to act in the
surprise round, even if she is surprised. When the paladin makes an Initiative check, she gains a
bonus to the check equal to her Charisma bonus.

**Gained:** At 2nd Level

**Replaces:** Divine grace

**Prayer of the Fourth Act (Su)**

**Ability:** By spending 1 minute leading a prayer to Iomedae, the sword of valor can spend one use
of _channel energy_ to give living creatures in the channel burst
[temporary hit points](ref/rule/temporary-hit-points) equal to the amount that ability normally
heals. These temporary hit points last for no more than 1 hour.

**Gained:** At 6th Level

**Replaces:** 6th-level mercy

**Worthy Enemy (Su)**

**Ability:** When a sword of valor critically hits an enemy with a _smite,_ the target must make a
Will saving throw (DC = 10 + 1/2 the paladin's level + the paladin's Charisma bonus) or be compelled
to surrender to the paladin, as if affected by a [suggestion](ref/spell/suggestion) spell (CL = the
paladin's level) to lay down arms and give up the fight. An enemy that succumbs to this ability
remains docile until it is injured by the paladin or one of his obvious allies, at which point the
compulsion to surrender immediately ends and the enemy is free to make his own choices again.

**Gained:** At 11th Level

**Replaces:** Aura of justice

**Special:** If the enemy makes the save, it is not subject to this ability for 24 hours. _Worthy
enemy_ is a mind-affecting effect.
