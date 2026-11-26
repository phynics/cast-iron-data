+++
id = "ref/arc-monk/disciple-of-wholeness"
kind = "archetype"
title = "Disciple of Wholeness"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Disciple%20of%20Wholeness"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "disciple_of_wholeness", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "healers-handbook"
page = "4"

[fields]
kind = "archetype"
features = [
  { anchor = "healing-ki", level = 4 },
  { anchor = "hone-body", level = 5 },
  { anchor = "greater-hone-body", level = 11 },
  { anchor = "hone-soul", level = 13 },
]
trades = [
  { replaces = "The ability to spend ki to gain an extra attack during a flurry of blows", by = ["healing-ki"] },
  { replaces = "Purity of body", feature = "purity-of-body", by = ["hone-body"] },
  { replaces = "Diamond body", feature = "diamond-body", by = ["greater-hone-body"] },
  { replaces = "Diamond soul", feature = "diamond-soul", by = ["hone-soul"] },
  { alters = "Ki pool", feature = "ki-pool", by = ["healing-ki"] },
  { replaces = "The ki power gained at 4th level for an unchained monk", by = ["healing-ki"] },
  { replaces = "The ki power gained at 12th level for an unchained monk", by = ["greater-hone-body"] },
  { replaces = "The ki power gained at 14th level for an unchained monk", by = ["hone-soul"] },
]
+++

Disciples of wholeness train to bring themselves and others closer to physical and spiritual
perfection.

## Healing Ki (Su) {#healing-ki}

At 4th level, a disciple of wholeness can touch a creature as a swift action and spend 1 point from
her ki pool to restore a number of hit points equal to 1d4 + 1/2 her monk level to that creature. If
she has the wholeness of body class feature or ki power (as in the case of the unchained monk from
_Pathfinder RPG Pathfinder Unchained_), she can spend 2 points to restore a number of hit points
equal to 1d8 + her monk level to a touched creature. She does not gain the ability to spend ki to
gain an extra attack during a flurry of blows.

This ability alters ki pool, and it replaces the ki power gained at 4th level for an unchained monk.

## Hone Body (Su) {#hone-body}

At 5th level, a disciple of wholeness has immunity to supernatural and magical diseases as long as
she is undamaged (she loses this immunity when she has hit point or ability score damage). In
addition, she can always touch a creature as a swift action and spend 1 point from her ki pool to
render it immune to all diseases for 1 day. She cannot grant this immunity if the target is already
afflicted with a disease.

This ability replaces purity of body.

## Greater Hone Body (Su) {#greater-hone-body}

At 11th level, a disciple of wholeness is immune to poison while undamaged and can grant immunity to
poison (lasting for 1 day). This ability otherwise functions as per hone body.

This ability replaces the diamond body ability, and it replaces the ki power gained at 12th level
for an unchained monk (and an unchained monk cannot gain the diamond body ki power).

## Hone Soul (Su) {#hone-soul}

At 13th level, a disciple of wholeness can dispel a spell affecting a living creature by touching it
as a standard action and spending 1 point from her ki pool. This power functions like the targeted
dispel option of _[greater dispel magic](ref/spell/dispel-magic-greater),_ with the caster level
equal to the disciple of wholeness's monk level.

This ability replaces the diamond soul ability, and it replaces the ki power gained at 14th level
for an unchained monk (and an unchained monk cannot gain the diamond soul ki power).
