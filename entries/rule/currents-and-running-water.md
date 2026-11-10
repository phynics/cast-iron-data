+++
id = "ref/rule/currents-and-running-water"
kind = "rule"
title = "Currents and Running Water"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "currents_and_running_water", path = "json/rules_campaign_types01.json" },
]
[[sources]]
publication = "aquatic-adventures"

[fields]
kind = "none"
+++

Currents in the ocean (or a similarly large body of water) work similarly to
[rivers](ref/rule/aquatic-terrain). Each current has a particular speed (measured in feet per
round), width, and direction, and at the beginning of a creature's turn, the current pushes it that
distance. This movement provokes attacks of opportunity to creatures not in the same current. A
creature can try to swim against the current's flow on its turn to stay in place, but it's usually a
better idea to swim perpendicular to the current to reach the edge and exit the current.
Fortunately, while rivers can reach speeds up to 90 feet per round, the fastest natural ocean
currents are usually not much faster than 50 feet per round in the sunlight zone, and are slower the
deeper one travels. This is because currents are mainly influenced by the weather near the surface
and tiny discrepancies in temperature far below the surface, and the effects of the latter are not
as strong. Currents always count as at least rough water ([Swim](ref/skill/swim) DC 15), and faster
currents count as at least stormy water (Swim DC 20).

The majority of the ocean does not count as running water, but currents do. Thus while the spell
[locate creature](ref/spell/locate-creature) functions underwater, it rarely extends to its full
range, since even an extremely slow current blocks the spell. Likewise,
[vampires](ref/template/vampire) tempt fate in the ocean by exposing themselves to the risk of an
unexpected current.
