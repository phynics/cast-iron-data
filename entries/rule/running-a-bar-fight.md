+++
id = "ref/rule/running-a-bar-fight"
kind = "rule"
title = "Running a Bar Fight"
source_ids = ["inner-sea-taverns"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "running_a_bar_fight", path = "json/rules_rulesets01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Inner Sea Taverns pg 55

A bar fight begins much like a normal combat, with all the major participants rolling for initiative
and characters acting in initiative order. On a participant's turn, she can perform one of the
actions listed below. Relative positions don't matter between major participants, as it is assumed
any participant can reach any other in a given round. At initiative count 0, the crowd reduces the
tenacity of all major participants by the amount listed in its stat block.

### Bow Out

You flee the fight entirely.\
**Action:** Attempt either an Acrobatics or Stealth check (DC = 15 + the crowd's CR). If you are
successful, you are no longer part of the bar fight and cannot reenter it.

### Cast a Spell

You perform some magic amid the melee.\
**Action:** Being in a bar fight makes it difficult to focus, so you must succeed at a concentration
check (DC = 15 + the spell level) to cast a spell with a casting time of 1 standard action or less;
casting spells with longer casting times is impossible. You are assumed to be in range of any target
you wish to affect.\
**Special:** Casting damaging spells immediately turns the bar fight into a normal combat. Healing
magic doesn't help a participant regain tenacity. The crowd is treated as a swarm for the purpose of
what spells can affect it.

### Hunker Down

You duck behind a turned-over table or the bar to get a respite from the tumult.\
**Action:** Attempt either an Acrobatics or Stealth check (DC = 10 + the crowd's CR). If you are
successful, the crowd doesn't reduce your tenacity this round and you gain a +2 bonus to your touch
AC until the beginning of your next turn.

### Improvise a Weapon

You grab a chair to smash over someone's head or a bottle to throw into someone's face.\
**Action:** Attempt a Perception check (DC = 15 + the crowd's CR). If you are successful, the next
brawling check you attempt for a mix it up or take a swing action can be a basic ranged attack (use
your Dexterity modifier for the brawling check). Alternatively, the next time you succeed at a
brawling check, you reduce the tenacity of the target by 1d8 + your Strength modifier.\
**Special:** If you have the [Catch Off-Guard](ref/feat/catch-off-guard) or
[Throw Anything](ref/feat/throw-anything) feat, you automatically succeed at the Perception check.

### Mix It Up

You wade into the crowd to knock some skulls.\
**Action:** Attempt a brawling check against the crowd's defense. If you are successful, you reduce
the crowd's tenacity by an amount determined by your statistics (see
[Brawling Damage](ref/rule/setting-up-a-bar-fight)).

### Redirect

You divert part of the crowd's attention to another person.\
**Action:** Attempt either a Bluff or Intimidate check (DC = 15 + the crowd's CR). If you are
successful, the amount the crowd reduces your tenacity by is halved and the amount the crowd reduces
the tenacity of a major participant of your choice by is multiplied by 1-1/2.\
**Special:** For each character who successfully redirects the crowd's attention against the same
major participant in 1 round, the multiplier increases by half (from 1-1/2 to 2, to 2-1/2, to 3, and
so forth).

### Set Up a Strike

You perform a fancy maneuver to take advantage of the bar's furnishings, such as leaping onto the
bar to get higher ground or swinging from a light fixture.\
**Action:** Attempt either an Acrobatics or Climb check (DC = 12 + the crowd's CR). If you are
successful, you gain a +2 bonus on brawling checks and threaten a critical hit on a natural 19 or 20
until the end of your next turn. If you roll a natural 1 on this check, you take a -2 penalty to
your touch AC until the beginning of your next turn.

### Spread Rumors

With choice words, you get the crowd to turn on itself.\
**Action:** Attempt a Bluff or Knowledge (local) check (DC = 15 + the crowd's CR). If you are
successful, the crowd's tenacity is reduced by the same amount it reduces your tenacity.

### Take a Swing

You strike out against a particular person.\
**Action:** Attempt a brawling check against a major participant's touch AC. If you are successful,
you reduce the target's tenacity by an amount determined by your statistics (see
[Brawling Damage](ref/rule/setting-up-a-bar-fight)).

## Experience for Bar Fights

The PCs should receive XP for each major participant they reduce to 0 tenacity, as well as for the
crowd if they reduce its tenacity to 0. They shouldn't receive any XP for the bar fight if they all
bow out or are all knocked out by having their tenacity pools reduced to 0.
