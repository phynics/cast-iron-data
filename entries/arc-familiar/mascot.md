+++
id = "ref/arc-familiar/mascot"
kind = "archetype"
title = "Mascot"
source_ids = ["ultimate-wilderness", "familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mascot", path = "json/archetypes_FAMILIAR.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "211"
[[sources]]
publication = "familiar-folio"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "affinity-for-my-team" },
  { anchor = "lucky-mascot" },
  { anchor = "share-spells", level = 3 },
  { anchor = "deliver-touch-spells", level = 5 },
  { anchor = "speak-with-team", level = 7 },
  { anchor = "heart-of-the-team" },
]
trades = [
  { replaces = "Alertness", by = ["affinity-for-my-team"] },
  { replaces = "Improved evasion", by = ["lucky-mascot"] },
  { replaces = "Speak with master", by = ["speak-with-team"] },
  { replaces = "speak with animals of its kind", by = ["speak-with-team"] },
  { replaces = "Spell resistance", by = ["heart-of-the-team"] },
  { replaces = "scry on familiar", by = ["heart-of-the-team"] },
  { alters = "Empathic link", by = ["affinity-for-my-team"] },
  { alters = "Share spells", by = ["share-spells"] },
  { alters = "Deliver touch spells", by = ["deliver-touch-spells"] },
]
+++

A familiar sometimes serves as the centerpiece of an adventuring party. Known as a mascot, this type
of familiar eventually treats the entire party as its master.

## Mascot Skills {#mascot-skills}

A mascot treats all Perform skills as class skills.

## Affinity for My Team (Su) {#affinity-for-my-team}

A mascot is the heart and soul of its team. At first, the team consists of only the familiar and its
master, but at 3rd level and every 3 levels thereafter, a mascot can add an additional member to its
team. A mascot's empathic link extends to all members of its team. A mascot can add or remove one
team member over the course of a day.

This replaces alertness and alters empathic link.

## Lucky Mascot (Su) {#lucky-mascot}

Whenever a mascot uses the aid another action to improve a team member's attack roll or AC, that
team member also gains a +1 luck bonus to AC for 1 round.

This replaces improved evasion.

## Share Spells (Ex) {#share-spells}

At 3rd level, spells that target a mascot via its share spells ability function at its master's
caster level - 2. The mascot also benefit from the spells of any team member when it is using share
spells.

This alters share spells.

## Deliver Touch Spells (Su) {#deliver-touch-spells}

At 5th level, spells delivered by a mascot's deliver touch spells ability function at its master's
caster level - 2. The mascot can deliver the touch spells of any of its team members.

This alters deliver touch spells.

## Speak with Team (Ex) {#speak-with-team}

At 7th level, a mascot gains the ability to speak with all members of its team verbally as if using
speak with master.

This replaces speak with master and speak with animals of its kind.

## Heart of the Team (Ex) {#heart-of-the-team}

Once per day at 13th level, as a full-round action, a mascot can designate any member of its team as
its master for the purpose of calculating its base attack bonus, Hit Dice, hit points, saving
throws, and skill ranks.

This replaces [spell resistance](ref/rule/spell-resistance) and scry on familiar.
