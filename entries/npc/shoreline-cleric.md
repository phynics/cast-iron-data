+++
id = "ref/npc/shoreline-cleric"
kind = "creature"
title = "Shoreline Cleric"
source_ids = ["npc-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shoreline_cleric", path = "json/npcs5.json" },
]
[[sources]]
publication = "npc-codex"
page = "45"

[fields]
kind = "creature"
cr = "3"
+++

Half-elf [cleric](ref/class/cleric) of [Gozreh](ref/faith/gozreh) 4\
N Medium humanoid (elf, human)

::: statblock
Challenge rating: 3
XP: 800
Init: +2
Senses: [low-light vision](ref/rule/low-light-vision); Perception +9
:::

### Defense

::: statblock
AC: 19, touch 12, flat-footed 17 (+5 armor, +2 Dex, +2 natural)
hp: 25 (4d8+4)
Fort: +5
Ref: +3
Will: +8; +2 vs. enchantments
Immune: sleep
:::

### Offense

::: statblock
Speed: 30 ft.
Melee: trident +2 (1d8-1)
Ranged: shortbow +5 (1d6/×3)
Special Attacks: channel positive energy 4/day (DC 13, 2d6), wooden fist (+2, 7 rounds/day)
:::

::: statblock
title = "Spell-Like Abilities"
Caster level: 4th
Concentration: +8
7/day: storm burst (1d6+2 nonlethal damage)
:::

::: statblock
title = "Cleric Spells Prepared"
Caster level: 4th
Concentration: +8
2nd: [barkskin](ref/spell/barkskin)^[1](ref/npc/shoreline-cleric#footnote-d)^, [hold person](ref/spell/hold-person) (2, DC 16), [summon monster II](ref/spell/summon-monster-2)
1st: [cause fear](ref/spell/cause-fear) (DC 15), [cure light wounds](ref/spell/cure-light-wounds), [endure elements](ref/spell/endure-elements)^[1](ref/npc/shoreline-cleric#footnote-d)^, [entangle](ref/spell/entangle) (DC 15), [entropic shield](ref/spell/entropic-shield)
0 (at will): [bleed](ref/spell/bleed) (2, DC 14), [guidance](ref/spell/guidance), [light](ref/spell/light)
Domains: [Plant](ref/domain/plant), [Weather](ref/domain/weather)
:::

### Tactics

**Before Combat** The cleric casts barkskin.\
**During Combat** The cleric casts entropic shield, then uses hold person, entangle, and bane
arrows.\
**Base Statistics** Without barkskin, her statistics are **AC** 17, touch 12, flat-footed 15.

### Statistics

::: statblock
Str: 8
Dex: 14
Con: 13
Int: 10
Wis: 18
Cha: 12
Base Atk: +3
CMB: +2
CMD: 14
Feats: [Deadly Aim](ref/feat/deadly-aim), [Martial Weapon Proficiency](ref/feat/martial-weapon-proficiency) (shortbow), [Skill Focus](ref/feat/skill-focus) (Stealth)
Skills: Heal +8, Knowledge (nature) +2, Knowledge (religion) +5, Perception +9, Sense Motive +8, Stealth +7
Languages: Common, Elven
SQ: aura, elf blood
Combat Gear: +1 human-[bane](ref/magic-enh/bane) arrows (2), +1 orc-bane arrow, potion of [cure moderate wounds](ref/spell/cure-moderate-wounds)
Other Gear: +1 [chain shirt](ref/eq-armor/chain-shirt), [shortbow](ref/eq-weapon/shortbow) with 20 arrows, [trident](ref/eq-weapon/trident), [feather token (anchor)](ref/magic-wondrous/feather-token-anchor), [wooden holy symbol](ref/eq-misc/wooden-holy-symbol), 256 gp
:::

###### ^1^ {#footnote-d}

Domain spell
