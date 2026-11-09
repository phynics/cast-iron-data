+++
id = "ref/rule/withdrawal-effects"
kind = "rule"
title = "Withdrawl Effects"
source_ids = ["blood-of-the-night"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "withdrawal_effects", path = "json/rules_subsystems04.json" },
]
[[sources]]
publication = "blood-of-the-night"
page = "22"

[fields]
kind = "none"
+++

An undead that hasn't fed recently suffers from withdrawal, depending on the number of hunger saves
it has failed. As shown on the Withdrawal Penalties table, an undead creature suffering from
withdrawal takes penalties to [channel resistance](ref/rule/channel-resistance), on Will saves, to
Strength and Charisma scores, to [damage reduction](ref/rule/damage-reduction), to
[fast healing](ref/umr/fast-healing), and on Disguise checks. The withdrawal penalties apply only if
the creature has the ability in question. For example, a hungry moroi's damage reduction decreases,
but a hungry ghoul ignores that column because it doesn't have damage reduction. All penalties are
removed when the creature completes a single feeding. This only ends the withdrawal penalties, and
does not grant the creature any feeding bonuses beyond those granted by the creature's ability
associated with feeding.

If the undead's Strength or Charisma penalties equal its Strength or Charisma, it becomes inert,
helpless, and wracked by nightmares of hunger; it only revives if fed by another. An undead
creature's [channel resistance](ref/rule/channel-resistance),
[damage reduction](ref/rule/damage-reduction), and [fast healing](ref/umr/fast-healing) cannot fall
below 0.

### Withdrawal Penalties

|Failed Hunger Saves|Channel Resistance|Will Saves|Str/Cha|DR|Fast Healing|Disguise|
| --- | --- | --- | --- | --- | --- | --- |
|1|-1|-2|-1|-2|-1|-2|
|2|-1|-2|-1|-2|-1|-2|
|3|-1|-2|-2|-4|-1|-4|
|4|-2|-3|-2|-4|-2|-4|
|5|-2|-3|-4|-4|-2|-4|
|6|-2|-3|-4|-6|-2|-6|
|7|-3|-4|-6|-6|-3|-6|
|8|-3|-4|-6|-6|-3|-6|
|9|-3|-4|-8|-8|-3|-8|
|10|-4|-5|-10|-8|-4|-8|
