+++
id = "ref/arc-skald/belkzen-war-drummer"
kind = "archetype"
title = "Belkzen War Drummer"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Belkzen%20War%20Drummer"
source_ids = ["advanced-class-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "belkzen_war_drummer", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "advanced-class-origins"
page = "19"

[fields]
kind = "archetype"
features = [
  { anchor = "fearsome-mien", level = 1 },
  { anchor = "deadly-rhythm", level = 1 },
  { anchor = "weapon-master", level = 7 },
  { anchor = "siege-drums", level = 7 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["fearsome-mien"] },
  { replaces = "Scribe Scroll", feature = "scribe-scroll", by = ["deadly-rhythm"] },
  { replaces = "Lore master", feature = "lore-master", by = ["weapon-master"] },
  { replaces = "Versatile performance gained benefit at 7th level", feature = "versatile-performance", levels = [7], by = ["siege-drums"] },
]
+++

These fierce drummers are equally adept at tapping out a driving rhythm and rapping enemies upside
the head with the same massive clubs they use to beat the crude hidecovered drums they carry into
battle.

## Weapon Proficiency {#weapon-proficiency}

A war drummer is proficient with all simple weapons and the [greatclub](ref/eq-weapon/greatclub).

## Fearsome Mien (Ex) {#fearsome-mien}

A war drummer adds 1/2 his class level (minimum 1) to all Intimidate and Bluff skill checks. This
ability replaces bardic knowledge.

## Deadly Rhythm (Ex) {#deadly-rhythm}

At 1st level, during his raging song, a Belkzen war drummer can draw [clubs](ref/eq-weapon/club) and
greatclubs as a free action as if he had the [Quick Draw](ref/feat/quick-draw) feat. At 3rd level,
the war drummer gains a +1 bonus on damage rolls for attacks made with clubs or greatclubs. At 7th
level and every 4 levels thereafter, this bonus increases by 1 (to a maximum of +5). At 6th level,
the war drummer gains [Improved Critical](ref/feat/improved-critical) with the club or the greatclub
as a bonus feat. This ability replaces Scribe Scroll.

## Weapon Master (Ex) {#weapon-master}

At 7th level, a war drummer gains [Craft Magic Arms and Armor](ref/feat/craft-magic-arms-and-armor)
as a bonus feat. This ability replaces lore master.

## Raging Song (Su) {#raging-song}

A war drummer gains access to the following raging song.

## Siege Drums (Su) {#siege-drums}

At 7th level, the Belkzen war drummer can [shatter](ref/spell/shatter) massive walls, doors, and
other inanimate obstacles using his war drums. This ability works as the _shatter_ spell, except the
drummer can increase the amount of damage and size of the object damaged by playing for longer
periods. The siege drummer can affect objects weighing up to 10 pounds per level, plus an additional
5 pounds per level for each additional round he plays. The damage dealt increases by 2d6 per round
(to a maximum of 20d6 after 10 rounds). The damage is dealt only after the drummer ceases playing.
This ability replaces the versatile performance gained benefit at 7th level.
