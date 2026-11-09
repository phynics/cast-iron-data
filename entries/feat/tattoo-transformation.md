+++
id = "ref/feat/tattoo-transformation"
kind = "feat"
title = "Tattoo Transformation"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tattoo_transformation", path = "json/feat16.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/inscribe-magical-tattoo", label = "or" },
  { kind = "prerequisite", target = "ref/feat/varisian-tattoo", label = "or" },
]
[[sources]]
publication = "monster-summoners-handbook"
page = "15"

[fields]
kind = "feat"
prerequisites = "Inscribe Magical Tattoo or Varisian Tattoo; Tattoo Attunement; Spellcraft 9 ranks."
prerequisite_feats = ["ref/feat/inscribe-magical-tattoo", "ref/feat/tattoo-attunement", "ref/feat/varisian-tattoo"]
benefit = "When you use Tattoo Attunement on a creature you've summoned, you can gain that creature's elemental resistance as long as it is in tattoo form. If the creature has resistance to multiple elemental types, you gain only one of them. If the creature is immune to an elemental type, you gain resistance 20 to that type. For example, if the creature has resistance 10 to both fire and cold and immunity to electricity, you can gain resistance 10 to either fire or cold or resistance 20 to electricity as long as the creature is in tattoo form."
+++

You've learned to take on some of the resistance of a summoned creature when you absorb it as a
tattoo.\
**Prerequisites:** [Inscribe Magical Tattoo](ref/feat/inscribe-magical-tattoo) or
[Varisian Tattoo](ref/feat/varisian-tattoo); [Tattoo Attunement](ref/feat/tattoo-attunement);
Spellcraft 9 ranks.\
**Benefit:** When you use Tattoo Attunement on a creature you've summoned, you can gain that
creature's elemental resistance as long as it is in tattoo form. If the creature has resistance to
multiple elemental types, you gain only one of them. If the creature is immune to an elemental type,
you gain resistance 20 to that type. For example, if the creature has resistance 10 to both fire and
cold and immunity to electricity, you can gain resistance 10 to either fire or cold or resistance 20
to electricity as long as the creature is in tattoo form.
