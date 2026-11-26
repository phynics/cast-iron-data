+++
id = "ref/arc-monk/windstep-master"
kind = "archetype"
title = "Windstep Master"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Windstep%20Master"
source_ids = ["elemental-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "windstep_master", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "elemental-masters-handbook"
page = "17"

[fields]
kind = "archetype"
features = [
  { anchor = "hurricane-punch", level = 1 },
  { anchor = "wind-step", level = 4 },
  { anchor = "swift-ki", level = 4 },
]
trades = [
  { replaces = "Stunning fist", feature = "stunning-fist", by = ["hurricane-punch"] },
  { replaces = "Slow fall or the ki power gained at 4th level for an unchained monk", feature = "slow-fall", by = ["wind-step"] },
  { replaces = "The ability to spend ki to increase his base speed", by = ["swift-ki"] },
  { alters = "Ki pool", feature = "ki-pool", by = ["swift-ki"] },
]
+++

Most monks are agile and fleet of foot, but few can rival a windstep master's lightness of step.
Windstep masters train in mountaintop monasteries and other holy houses dedicated to the wind, such
as the Monastery of Unfolding Wind in Niswan. Monks built using _Pathfinder RPG Pathfinder
Unchained_ can also take this archetype.

## Hurricane Punch (Ex) {#hurricane-punch}

At 1st level, a windstep master gains [Hurricane Punch](ref/feat/hurricane-punch) (see page 19) as a
bonus feat, even if he does not meet the prerequisites. While using this feat, he doesn't provoke an
attack of opportunity, even if he doesn't have the [Improved Bull Rush](ref/feat/improved-bull-rush)
feat.

At 4th level, while using the Hurricane Punch feat, the windstep master can
[bull rush](ref/rule/bull-rush) a target up to two size categories larger. At 12th level, the
windstep master's target can be up to three size categories larger. At 20th level, the target can be
of any size category.

At 8th level, when the windstep master uses the Hurricane Punch feat to successfully bull rush a
creature, he can push the creature back an additional 5 feet. At 16th level, he can push the
creature back an additional 10 feet.

This ability replaces stunning fist.

## Wind Step (Su) {#wind-step}

At 4th level, the windstep master's steps become supernaturally light. As a move action, he can use
_[air walk](ref/spell/air-walk)_ (as per the spell) up to a distance equal to his fast movement
bonus. He must reach a solid, level surface able to support his weight by the end of his turn or he
falls.

This ability replaces slow fall or the ki power gained at 4th level for an unchained monk.

## Swift Ki (Su) {#swift-ki}

At 4th level, the windstep master can spend 1 point from his ki pool as a swift action to sustain
his wind step for 1 minute. During this time, the windstep master can remain airborne even if he
doesn't reach a solid surface. He can also spend 1 point from his ki pool as a swift action to
increase his wind step distance by 20 feet for 1 round. The windstep master does not gain the
ability to spend ki to increase his base speed by 20 feet for 1 round.

This ability alters ki pool.
