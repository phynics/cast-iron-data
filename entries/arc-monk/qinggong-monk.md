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
feat to select it as a _ki_ power. For example, a qinggong monk can select
[Spring Attack](ref/feat/spring-attack) as a _ki_ power even if she doesn't meet the prerequisites
for selecting Spring Attack as a feat. Activating one of these _ki_ powers is a free action on the
monk's turn; until the start of her next turn, the monk is treated as if she had that feat. Some of
these _ki_ powers that duplicate feats may also be activated as an immediate action; these powers
are noted in the _ki_ powers list.

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
|[Acrobatic Steps](ref/feat/acrobatic-steps)|1 _ki_ point|
|_[augury](ref/spell/augury)_|1 _ki_ point|
|_[barkskin](ref/spell/barkskin)_|self only, 1 _ki_ point|
|[Deny Death](ref/feat/deny-death)\*, †|0 _ki_ points|
|_[feather step](ref/spell/feather-step)_\*\*|self only, 1 _ki_ point|
|_[hydraulic push](ref/spell/hydraulic-push)_\*\*|1 _ki_ point|
|_[ki arrow](ref/spell/ki-arrow)\*_|1 _ki_ point|
|_Ki_ Stand\*, †|0 _ki_ points|
|_[message](ref/spell/message)_|1 _ki_ point|
|[Power Attack](ref/feat/power-attack)|1 _ki_ point|
|[Quick Draw](ref/feat/quick-draw)|1 _ki_ point|
|_[scorching ray](ref/spell/scorching-ray)_|2 _ki_ points|
|slow fall|monk ability, 0 _ki_ points|
|[Throw Anything](ref/feat/throw-anything)|1 _ki_ point|
|_[true strike](ref/spell/true-strike)_|self only, 1 _ki_ point|

### 6th-Level Ki Powers {#6th-level-ki-powers}

|Ki power|Details|
| --- | --- |
|_[cloak of winds](ref/spell/cloak-of-winds)_\*\*|self only, 2 _ki_ points|
|_[gaseous form](ref/spell/gaseous-form)_|self only, 1 _ki_ point|
|[Heroic Recovery](ref/feat/heroic-recovery)\*\*, †|1 _ki_ point|
|high jump|monk ability, 1 _ki_ point|
|_[hydraulic torrent](ref/spell/hydraulic-torrent)_ \*\*|2 _ki_ points|
|_[remove disease](ref/spell/remove-disease)_|2 _ki_ points|
|[Sidestep](ref/feat/sidestep) \*\*, †|1 _ki_ point|
|[Snatch Arrows](ref/feat/snatch-arrows)†|1 _ki_ point|
|Spring Attack|1 _ki_ point|

### 8th-Level Ki Powers {#8th-level-ki-powers}

|Ki power|Details|
| --- | --- |
|_[dragon's breath](ref/spell/dragons-breath)_\*\*|2 _ki_ points|
|[Gliding Steps](ref/feat/gliding-steps)\*, †|1 _ki_ point|
|_[neutralize poison](ref/spell/neutralize-poison)_|3 _ki_ points|
|_[poison](ref/spell/poison)_|2 _ki_ points|
|_[restoration](ref/spell/restoration)_|self only, 2 _ki_ points|
|_[share memory](ref/spell/share-memory)_\*|0 _ki_ points|
|_[silk to steel](ref/spell/silk-to-steel)_\*|1 _ki_ point|
|[Spider Step](ref/feat/spider-step)\*\*|1 _ki_ point|
|[Whirlwind Attack](ref/feat/whirlwind-attack)|2 _ki_ points|
|wholeness of body|monk ability, level 7, 2 _ki_ points|

### 10th-Level Ki Powers {#10th-level-ki-powers}

|Ki power|Details|
| --- | --- |
|_[discordant blast](ref/spell/discordant-blast)_\*\*|2 _ki_ points|
|[Greater Bull Rush](ref/feat/greater-bull-rush)|2 _ki_ points|
|[Greater Disarm](ref/feat/greater-disarm)|2 _ki_ points|
|[Greater Feint](ref/feat/greater-feint)|2 _ki_ points|
|[Greater Sunder](ref/feat/greater-sunder)|2 _ki_ points|
|[Improved Blind-Fight](ref/feat/improved-blind-fight)\*\*, †|1 _ki_ point|
|_[ki leech](ref/spell/ki-leech)_\*|0 _ki_ points|
|[Lunge](ref/feat/lunge)|1 _ki_ point|
|_[shadow step](ref/spell/shadow-step)_\*|1 _ki_ point|
|_[spit venom](ref/spell/spit-venom)_\*|2 _ki_ points|
|[Step Up and Strike](ref/feat/step-up-and-strike)\*\*, †|2 _ki_ points|
|[Wind Stance](ref/feat/wind-stance)|2 _ki_ points|

### 12th-Level Ki Powers {#12th-level-ki-powers}

|Ki power|Details|
| --- | --- |
|abundant step|monk ability, 2 _ki_ points|
|_[battlemind link](ref/spell/battlemind-link)\*_|4 _ki_ points|
|diamond body|monk ability|
|[Elemental Fists](ref/feat/elemental-fist)\*\*|2 _ki_ points|
|[Improvised Weapon Mastery](ref/feat/improvised-weapon-mastery)|2 _ki_ points|
|_Ki_ Throw\*\*|2 _ki_ points|
|[Punishing Kick](ref/feat/punishing-kick)\*\*|2 _ki_ points|
|_[shadow walk](ref/spell/shadow-walk)_|3 _ki_ points|

### 14th-Level Ki Powers {#14th-level-ki-powers}

|Ki power|Details|
| --- | --- |
|_[blood crow strike](ref/spell/blood-crow-strike)_\*|2 _ki_ points|
|[Cloud Step](ref/feat/cloud-step)\*\*|3 _ki_ points|
|_[cold ice strike](ref/spell/cold-ice-strike)\*_|3 _ki_ points|
|diamond soul|monk ability|
|[Disarming Strike](ref/feat/disarming-strike)\*\*|2 _ki_ points|
|Improved _Ki_ Throw\*\*|2 _ki_ points|
|_[ki shout](ref/spell/ki-shout)_\*|3 _ki_ points|
|_[sonic thrust](ref/spell/sonic-thrust)_\*|2 _ki_ points|

### 16th-Level Ki Powers {#16th-level-ki-powers}

|Ki power|Details|
| --- | --- |
|[Bleeding Critical](ref/feat/bleeding-critical)|3 _ki_ points|
|[Greater Blind-Fight](ref/feat/greater-blind-fight)\*\*, †|2 _ki_ points|
|[Improved Vital Strike](ref/feat/improved-vital-strike)|2 _ki_ points|
|[Lightning Stance](ref/feat/lightning-stance)|3 _ki_ points|
|[Penetrating Strike](ref/feat/penetrating-strike)|2 _ki_ points|
|quivering palm|monk ability, 2 _ki_ points|
|_[strangling hair](ref/spell/strangling-hair)\*_|3 _ki_ points|

### 18th-Level Ki Powers {#18th-level-ki-powers}

|Ki power|Details|
| --- | --- |
|timeless body|monk ability, 0 _ki_ points|
|tongue of the sun and moon|monk ability, 0 _ki_ points|

### 20th-Level Ki Powers {#20th-level-ki-powers}

|Ki power|Details|
| --- | --- |
|[Blinding Critical](ref/feat/blinding-critical)|3 _ki_ points|
|[Crippling Critical](ref/feat/crippling-critical)\*\*|3 _ki_ points|
|[Deafening Critical](ref/feat/deafening-critical)|3 _ki_ points|
|empty body|monk ability, 3 _ki_ points|
|[Greater Penetrating Strike](ref/feat/greater-penetrating-strike)|3 _ki_ points|
|perfect self|monk ability, level 20|
|[Tiring Critical](ref/feat/tiring-critical)|3 _ki_ points|
