+++
id = "ref/arc-monk/qinggong-monk"
kind = "archetype"
title = "Qinggong Monk"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Qinggong%20Monk"
source_ids = ["ultimate-magic", "martial-arts-handbook", "advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "qinggong_monk", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "ultimate-magic"
page = "51"
[[sources]]
publication = "martial-arts-handbook"
page = "21"
[[sources]]
publication = "advanced-race-guide"
page = "149"

[fields]
kind = "archetype"
features = [
  { anchor = "ki-power" },
]
trades = [
  { replaces = "The monk class ability the qinggong monk gives up for this ki power", by = ["ki-power"] },
]
+++

The qinggong monk is a master of her ki, using it to perform superhuman stunts or even blast
opponents with supernatural energy. Some achieve their power over ki through extreme discipline,
while others attain this power by intentionally or accidentally ingesting rare herbs or strange
mystical fruits, and a few are gifted these abilities by a dying qinggong master.

## Ki Power {#ki-power}

A qinggong monk can select a _ki_ power (see below) for which she qualifies in place of the
following monk class abilities: slow fall (4th), high jump (5th), wholeness of body (7th), diamond
body (11th), abundant step (12th), diamond soul (13th), quivering palm (15th), timeless body (17th),
tongue of the sun and moon (17th), empty body (19th), and perfect self (20th). This replaces the
monk class ability the qinggong monk gives up for this _ki_ power.

### Ki Powers {#ki-powers}

_Ki_ powers are abilities that draw on the power of a monk's _ki_. The standard monk presented in
the _Core Rulebook_ has several abilities that count as _ki_ powers, such as wholeness of body,
abundant step, and empty body. A qinggong monk can learn additional _ki_ powers, which often
replaces a non-_ki_ monk ability such as purity of body. _Ki_ powers are divided into three
categories: feats, monk abilities, and spells.

### Feats {#feats}

These _ki_ powers duplicate the effects of specific feats. A monk does not need to qualify for a
feat to select it as a _ki_ power. For example, a qinggong monk can select Spring Attack as a _ki_
power even if she doesn't meet the prerequisites for selecting Spring Attack as a feat. Activating
one of these _ki_ powers is a free action on the monk's turn; until the start of her next turn, the
monk is treated as if she had that feat. Some of these _ki_ powers that duplicate feats may also be
activated as an immediate action; these powers are noted in the _ki_ powers list.

### Monk Abilities {#monk-abilities}

Some _ki_ powers are standard monk abilities described in the _Core Rulebook_. Even if a qinggong
monk selects a different _ki_ power in place of a standard monk ability, she can select that monk
ability later as one of her _ki_ powers.

### Spells {#spells}

These _ki_ powers duplicate the effects of a spell, and are
[spell-like abilities](ref/umr/spell-like-abilities). A qinggong monk's class level is the caster
level for these spell-like abilities, and she uses Wisdom to determine her
[concentration](ref/rule/concentration) check bonus.

### Requirements {#requirements}

All _ki_ powers have a minimum monk level requirement to select them. A monk who does not meet this
requirement cannot select that _ki_ power.

### Activation {#activation}

Most _ki_ powers require the monk to spend _ki_ points; the exact amount is listed after the _ki_
power. _Ki_ powers that cost 0 _ki_ do not require the monk to have any _ki_ points in her _ki_ pool
to use the ability.

The saving throw against a monk's _ki_ power, if any, is equal to 10 + 1/2 the monk's level + the
monk's Wisdom bonus.

Feats or spells marked with a single asterisk (\*) are described in this book. Feats or spells
marked with two asterisks (\*\*) are in the _Advanced Player's Guide_. Feats marked with a dagger
(†) are _ki_ powers that can be activated as an immediate action.

### 4th-Level Ki Powers {#4th-level-ki-powers}

|Ki power|Details|
| --- | --- |
|Acrobatic Steps|1 _ki_ point|
|_augury_|1 _ki_ point|
|_barkskin_|self only, 1 _ki_ point|
|Deny Death\*, †|0 _ki_ points|
|_feather step_\*\*|self only, 1 _ki_ point|
|_hydraulic push_\*\*|1 _ki_ point|
|_ki arrow\*_|1 _ki_ point|
|_Ki_ Stand\*, †|0 _ki_ points|
|_message_|1 _ki_ point|
|Power Attack|1 _ki_ point|
|Quick Draw|1 _ki_ point|
|_scorching ray_|2 _ki_ points|
|slow fall|monk ability, 0 _ki_ points|
|Throw Anything|1 _ki_ point|
|_true strike_|self only, 1 _ki_ point|

### 6th-Level Ki Powers {#6th-level-ki-powers}

|Ki power|Details|
| --- | --- |
|_cloak of winds_\*\*|self only, 2 _ki_ points|
|_gaseous form_|self only, 1 _ki_ point|
|Heroic Recovery\*\*, †|1 _ki_ point|
|high jump|monk ability, 1 _ki_ point|
|_hydraulic torrent_ \*\*|2 _ki_ points|
|_remove disease_|2 _ki_ points|
|Sidestep \*\*, †|1 _ki_ point|
|Snatch Arrows†|1 _ki_ point|
|Spring Attack|1 _ki_ point|

### 8th-Level Ki Powers {#8th-level-ki-powers}

|Ki power|Details|
| --- | --- |
|_dragon's breath_\*\*|2 _ki_ points|
|Gliding Steps\*, †|1 _ki_ point|
|_neutralize poison_|3 _ki_ points|
|_poison_|2 _ki_ points|
|_restoration_|self only, 2 _ki_ points|
|_share memory_\*|0 _ki_ points|
|_silk to steel_\*|1 _ki_ point|
|Spider Step\*\*|1 _ki_ point|
|Whirlwind Attack|2 _ki_ points|
|wholeness of body|monk ability, level 7, 2 _ki_ points|

### 10th-Level Ki Powers {#10th-level-ki-powers}

|Ki power|Details|
| --- | --- |
|_discordant blast_\*\*|2 _ki_ points|
|Greater Bull Rush|2 _ki_ points|
|Greater Disarm|2 _ki_ points|
|Greater Feint|2 _ki_ points|
|Greater Sunder|2 _ki_ points|
|Improved Blind-Fight\*\*, †|1 _ki_ point|
|_ki leech_\*|0 _ki_ points|
|Lunge|1 _ki_ point|
|_shadow step_\*|1 _ki_ point|
|_spit venom_\*|2 _ki_ points|
|Step Up and Strike\*\*, †|2 _ki_ points|
|Wind Stance|2 _ki_ points|

### 12th-Level Ki Powers {#12th-level-ki-powers}

|Ki power|Details|
| --- | --- |
|abundant step|monk ability, 2 _ki_ points|
|_battlemind link\*_|4 _ki_ points|
|diamond body|monk ability|
|Elemental Fists\*\*|2 _ki_ points|
|Improvised Weapon Mastery|2 _ki_ points|
|_Ki_ Throw\*\*|2 _ki_ points|
|Punishing Kick\*\*|2 _ki_ points|
|_shadow walk_|3 _ki_ points|

### 14th-Level Ki Powers {#14th-level-ki-powers}

|Ki power|Details|
| --- | --- |
|_blood crow strike_\*|2 _ki_ points|
|Cloud Step\*\*|3 _ki_ points|
|_cold ice strike\*_|3 _ki_ points|
|diamond soul|monk ability|
|Disarming Strike\*\*|2 _ki_ points|
|Improved _Ki_ Throw\*\*|2 _ki_ points|
|_ki shout_\*|3 _ki_ points|
|_sonic thrust_\*|2 _ki_ points|

### 16th-Level Ki Powers {#16th-level-ki-powers}

|Ki power|Details|
| --- | --- |
|Bleeding Critical|3 _ki_ points|
|Greater Blind-Fight\*\*, †|2 _ki_ points|
|Improved Vital Strike|2 _ki_ points|
|Lightning Stance|3 _ki_ points|
|Penetrating Strike|2 _ki_ points|
|quivering palm|monk ability, 2 _ki_ points|
|_strangling hair\*_|3 _ki_ points|

### 18th-Level Ki Powers {#18th-level-ki-powers}

|Ki power|Details|
| --- | --- |
|timeless body|monk ability, 0 _ki_ points|
|tongue of the sun and moon|monk ability, 0 _ki_ points|

### 20th-Level Ki Powers {#20th-level-ki-powers}

|Ki power|Details|
| --- | --- |
|Blinding Critical|3 _ki_ points|
|Crippling Critical\*\*|3 _ki_ points|
|Deafening Critical|3 _ki_ points|
|empty body|monk ability, 3 _ki_ points|
|Greater Penetrating Strike|3 _ki_ points|
|perfect self|monk ability, level 20|
|Tiring Critical|3 _ki_ points|
