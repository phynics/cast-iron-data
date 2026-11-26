+++
id = "ref/arc-familiar/egotist"
kind = "archetype"
title = "Egotist"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "egotist", path = "json/archetypes_FAMILIAR.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "210"

[fields]
kind = "archetype"
features = [
  { anchor = "song-of-myself" },
  { anchor = "order-master", level = 3 },
  { anchor = "receive-touch-spells", level = 5 },
  { anchor = "scry-on-master", level = 11 },
]
trades = [
  { replaces = "Deliver touch spells", by = ["receive-touch-spells"] },
  { replaces = "Scry on familiar", by = ["scry-on-master"] },
  { alters = "Alertness", by = ["song-of-myself"] },
  { alters = "the variable familiar bonus", by = ["song-of-myself"] },
  { alters = "Speak with master", by = ["order-master"] },
]
+++

An egotist believes itself to be the real master in the relationship—the power behind the throne. It
often attempts to communicate "orders" for its master as best it can, interfering in matters ranging
from spell choices and tactical combat decisions to its master's love life.

## Egotist Skills {#egotist-skills}

An egotist treats Intimidate as a class skill.

## Song of Myself (Ex) {#song-of-myself}

An egotist gains [Alertness](ref/feat/alertness) as a bonus feat rather than providing that feat to
its master. It gains the variable familiar bonus (such as the [bat's](ref/monster/familiar-bat) +3
bonus on Fly checks) instead of granting the bonus to its master.

This alters alertness and the variable familiar bonus.

## Order Master (Ex) {#order-master}

An egotist gains speak with master at 3rd level instead of 5th level.

This alters speak with master.

## Receive Touch Spells (Ex) {#receive-touch-spells}

At 5th level, an egotist can demand a particular touch spell as a standard action. If it does so,
until the egotist's next turn, its master can cast that spell on the egotist once as a ranged touch
within close range, as if using [Reach Spell](ref/feat/reach-spell).

This replaces deliver touch spells.

## Scry on Master (Sp) {#scry-on-master}

At 11th level, an egotist can scry on its master (as if casting the _[scrying](ref/spell/scrying)_
spell) once per day.

This replaces scry on familiar.
