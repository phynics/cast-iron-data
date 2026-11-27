+++
id = "ref/arc-vigilante/teisatsu"
kind = "archetype"
title = "Teisatsu"
aon = "ArchetypeDisplay.aspx?FixedName=Vigilante%20Teisatsu"
source_ids = ["spymasters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "teisatsu", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "spymasters-handbook"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "infiltrator", level = 1 },
  { anchor = "ki-pool", level = 2 },
  { anchor = "teisatsu-talents" },
]
trades = [
  { replaces = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Vigilante talent gained at 2nd level", feature = "vigilante-talent", levels = [2], by = ["ki-pool"] },
  { alters = "Vigilante specialization", feature = "vigilante-specialization", by = ["infiltrator"] },
  { alters = "Vigilante talents", feature = "vigilante-talent", by = ["teisatsu-talents"] },
]
+++

Teisatsu are specialized vigilantes who focus on infiltrating social scenes and high-society
gatherings on behalf of the feuding lords of Minkai. Trained as assassins and spies, they cultivate
a suite of personalities and study secret arts that hone their bodies into deadly weapons.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Teisatsu are proficient with all simple weapons, plus the [kama](ref/eq-weapon/kama),
[katana](ref/eq-weapon/katana), [kusarigama](ref/eq-weapon/kusarigama),
[nunchaku](ref/eq-weapon/nunchaku), [sai](ref/eq-weapon/sai),
[short sword](ref/eq-weapon/short-sword), [shortbow](ref/eq-weapon/shortbow),
[shuriken](ref/eq-weapon/shuriken), [siangham](ref/eq-weapon/siangham), and
[wakizashi](ref/eq-weapon/wakizashi). They are proficient with light and medium armor, but not with
shields.

This replaces the vigilante's normal weapon and armor proficiencies.

## Infiltrator (Ex) {#infiltrator}

A teisatsu is required to choose stalker as his specialization.

This alters vigilante specialization.

## Ki Pool (Su) {#ki-pool}

At 2nd level, a teisatsu gains a _ki_ pool, identical to the [ninja](ref/class/ninja) class feature
(_Pathfinder RPG Ultimate Combat_ 14), using his vigilante level as his effective ninja level.

This ability replaces the vigilante talent gained at 2nd level.

## Teisatsu Talents {#teisatsu-talents}

A teisatsu selects vigilante talents as normal. He can't select the
[rogue talent](ref/vigtalent/rogue-talent) vigilante talent. He can, however, select either of the
talents below, which are unique to the teisatsu.

This ability alters vigilante talents.

### Ki Power (Su) {#ki-power}

The teisatsu gains a single ki power of his choice from the list available to the
[unchained monk](ref/class/unchained-monk) class (_Pathfinder RPG Pathfinder Unchained_ 14).

### Shadow Tricks (Ex) {#shadow-tricks}

The teisatsu gains a single ninja trick (but not a master trick) of his choice. He cannot select a
rogue talent in place of a ninja trick in this manner. If he selects a ninja trick marked with an
asterisk (\*), that talent applies to his hidden strikes instead of to sneak attacks, and the talent
counts as a stalker vigilante talent with an asterisk (\*) for the limitation of applying only one
effect to a single hidden strike.
