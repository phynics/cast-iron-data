+++
id = "ref/arc-monk/invested-regent"
kind = "archetype"
title = "Invested Regent"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Invested%20Regent"
source_ids = ["heroes-of-the-high-court"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "invested_regent", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "heroes-of-the-high-court"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "investiture", level = 1 },
  { anchor = "vested-power", level = 2 },
]
trades = [
  { replaces = "Bonus feat gained at 1st level", feature = "bonus-feat", levels = [1], by = ["investiture"] },
  { replaces = "Bonus feat the invested regent gives up for the vested power", by = ["vested-power"] },
]
+++

The invested regent has been handpicked by inscrutable divine forces to command others—either at the
present or at some future time. The invested regent can harness a divine spark to perform superhuman
stunts, influence others, and escape injury. Invested regents come from all races and walks of life,
but they are more likely to be nobleborn in their cultures. Although some invested regents are
acutely aware of their powers' divine origins (such as powers gained from an investment ceremony to
[Asmodeus](ref/faith/asmodeus) in the nation of Cheliax), others do not know the source of their
abilities. Invested regents have strong personalities and a destiny to rule.

## Investiture (Su) {#investiture}

An invested regent gains a pool of investiture points, supernatural energy he can use to call upon
amazing abilities and divine protection. The number of points in the invested regent's investiture
pool is equal to 1/2 his monk level + his Charisma modifier. As long as he has at least 1 point in
his investiture pool, the invested regent can select one of his saving throws as a swift action and
gain a +1 sacred bonus on saving throws of that type for 1 round. If he spends 1 point from his
investiture pool during this swift action, he instead gains a sacred bonus equal to his Charisma
modifier on the saving throw selected.

A character with this feature and the ki pool class feature tracks investiture points and ki points
separately.

This ability replaces the bonus feat gained at 1st level.

## Vested Power (Ex or Sp) {#vested-power}

At 2nd level and every 4 monk levels thereafter, an invested regent can select a vested power (see
the Vested Powers section below) for which he qualifies in place of selecting a monk bonus feat. The
invested regent need not do so and can instead take the bonus feat, but once the decision to take a
bonus feat or a vested power is made, he can't change it.

This replaces the bonus feat the invested regent gives up for the vested power.

## Vested Powers {#vested-powers}

Vested powers are abilities that draw on an invested regent's investiture pool. Vested powers are
divided into two categories: feats and spells.

### Requirements {#requirements}

All vested powers have a minimum level requirement to select them. An invested regent who hasn't
reached the required monk level cannot select that vested power.

### Activation {#activation}

Most vested powers require the invested regent to spend investiture points; the exact amount is
listed after the vested power. Vested powers that cost 0 investiture points don't require the
invested regent to have any investiture points in his investiture pool to use the ability. The
saving throw against an invested regent's vested power, if any, is equal to 10 + 1/2 the invested
regent's monk level + his Charisma bonus.

### Feats {#feats}

These vested powers duplicate the effects of specific feats. An invested regent doesn't need to
qualify for a feat to select it as a vested power. For example, an invested regent can select
[Spring Attack](ref/feat/spring-attack) as a vested power even if he doesn't meet the prerequisites
for selecting Spring Attack as a feat. Activating one of these vested powers is a free action on the
invested regent's turn; until the start of his next turn, the invested regent is treated as if he
had that feat. Feats marked with an asterisk (\*) can also be activated as an immediate action when
it isn't the invested regent's turn.

### Spells {#spells}

These vested powers duplicate the effects of a spell and are
[spell-like abilities](ref/umr/spell-like-abilities). An invested regent's monk level is the caster
level for these spell-like abilities, and he uses Charisma to determine his
[concentration](ref/rule/concentration) check bonus. Activating one of these vested powers is a
standard action.

### 2nd-Level Vested Powers {#2nd-level-vested-powers}

- _[Comprehend languages](ref/spell/comprehend-languages)_ (2 investiture points)
- _[Divine favor](ref/spell/divine-favor)_ (1 investiture point)
- [Dodge](ref/feat/dodge)\* (0 investiture points)
- _[Entropic shield](ref/spell/entropic-shield)_ (1 investiture point)
- _[Expeditious retreat](ref/spell/expeditious-retreat)_ (2 investiture points)
- _[Feather step](ref/spell/feather-step)_ (self only, 1 investiture point)
- _[Hide from undead](ref/spell/hide-from-undead)_ (self only, 1 investiture point)
- _[Sanctuary](ref/spell/sanctuary)_ (self only, 1 investiture point)
- _[Shield of faith](ref/spell/shield-of-faith)_ (self only, 1 investiture point)

### 6th-Level Vested Powers {#6th-level-vested-powers}

- _[Calm emotions](ref/spell/calm-emotions)_ (1 investiture point)
- _[Cloak of winds](ref/spell/cloak-of-winds)_ (self only, 2 investiture points)
- _[Enthrall](ref/spell/enthrall)_ (2 investiture points)
- _[Gaseous form](ref/spell/gaseous-form)_ (self only, 1 investiture point)
- _[Helping hand](ref/spell/helping-hand)_ (1 investiture point)
- [Heroic Defiance](ref/feat/heroic-defiance)\* (1 investiture point)
- [Heroic Recovery](ref/feat/heroic-recovery)\* (1 investiture point)
- _[Protective spirit](ref/spell/protective-spirit)_ (2 investiture points)
- _[Remove disease](ref/spell/remove-disease)_ (self only, 2 investiture points)
- [Sidestep](ref/feat/sidestep)\* (1 investiture point)
- [Snatch Arrows](ref/feat/snatch-arrows)\* (1 investiture point)
- [Spring Attack](ref/feat/spring-attack) (1 investiture point)
- _[Tongues](ref/spell/tongues)_ (self only, 2 investiture points)

### 10th-Level Vested Powers {#10th-level-vested-powers}

- _[Air walk](ref/spell/air-walk)_ (self only, 2 investiture points)
- _[Death ward](ref/spell/death-ward)_ (self only, 2 investiture points)
- _[Dimension door](ref/spell/dimension-door)_ (self only, 2 investiture points)
- _[Discern lies](ref/spell/discern-lies)_ (3 investiture points)
- _[Divine power](ref/spell/divine-power)_ (3 investiture points)
- _[Freedom of movement](ref/spell/freedom-of-movement)_ (self only, 3 investiture points)
- [Improved Blind-Fight](ref/feat/improved-blind-fight)\* (1 investiture point)
- [Improved Great Fortitude](ref/feat/improved-great-fortitude)\* (1 investiture point)
- [Improved Iron Will](ref/feat/improved-iron-will)\* (1 investiture point)
- [Improved Lightning Reflexes](ref/feat/improved-lightning-reflexes)\* (1 investiture point)
- _[Mark of justice](ref/spell/mark-of-justice)_ (3 investiture points)
- _[Neutralize poison](ref/spell/neutralize-poison)_ (self only, 3 investiture points)
- _[Restoration](ref/spell/restoration)_ (self only, 2 investiture points)
- _[Spell resistance](ref/spell/spell-resistance)_ (self only, 2 investiture points)
- [Wind Stance](ref/feat/wind-stance) (2 investiture points)

### 14th-Level Vested Powers {#14th-level-vested-powers}

- _[Antilife shell](ref/spell/antilife-shell)_ (3 investiture points)
- [Disarming Strike](ref/feat/disarming-strike) (2 investiture points)
- [Greater Blind-Fight](ref/feat/greater-blind-fight)\* (2 investiture points)
- _[Greater command](ref/spell/command-greater)_ (3 investiture points)
- _[Greater forbid action](ref/spell/forbid-action-greater)_ (3 investiture points)
- [Lightning Stance](ref/feat/lightning-stance) (3 investiture points)
- _[Shadow walk](ref/spell/shadow-walk)_ (self only, 3 investiture points)
- _[Unwilling shield](ref/spell/unwilling-shield)_ (3 investiture points)

### 18th-Level Vested Powers {#18th-level-vested-powers}

- _[Divine vessel](ref/spell/divine-vessel)_ (3 investiture points)
- _[Foresight](ref/spell/foresight)_ (self only, 3 investiture points)
- _[Greater restoration](ref/spell/restoration-greater)_ (self only, 3 investiture points)
- _[Regenerate](ref/spell/regenerate)_ (self only, 3 investiture points)
- _[Repulsion](ref/spell/repulsion)_ (3 investiture points)
