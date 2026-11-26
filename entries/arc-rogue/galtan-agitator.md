+++
id = "ref/arc-rogue/galtan-agitator"
kind = "archetype"
title = "Galtan Agitator"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Galtan%20Agitator"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "galtan_agitator", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "39"

[fields]
kind = "archetype"
features = [
  { anchor = "reputation", level = 1 },
  { anchor = "ready-for-betrayal", level = 3 },
  { anchor = "enthralling-agitation", level = 4 },
  { anchor = "revolutionary-s-cause", level = 8 },
  { anchor = "leadership", level = 12 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["reputation"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["ready-for-betrayal"] },
  { replaces = "Rogue talent gained at 4th level", feature = "rogue-talents", levels = [4], by = ["enthralling-agitation"] },
  { replaces = "Rogue talent gained at 8th level", feature = "rogue-talents", levels = [8], by = ["revolutionary-s-cause"] },
  { replaces = "Rogue talent gained at 12th level", feature = "rogue-talents", levels = [12], by = ["leadership"] },
]
+++

Galtan agitators fight mightily to cast down the enemies of their ideals within the shambles of the
tumultuous nation of Galt. Any rogue (including the rogue from _Pathfinder RPG Pathfinder
Unchained_) can select the Galtan agitator archetype.

## Reputation (Ex) {#reputation}

This ability functions as the [renown](ref/soctalent/renown) [vigilante](ref/class/vigilante) social
talent (_Pathfinder RPG Ultimate Intrigue_ 12). In addition to improving attitudes, it also improves
the Galtan agitator's starting [influence](ref/rule/influence) and reputation with
[contacts](ref/rule/contacts) in the area by one level or step.

For the purpose of vigilante social talents, the Galtan agitator does not have a vigilante identity
and is always considered to be in her social identity, unless she has another identity (such as from
the vigilante class). If the Galtan agitator has another identity, she does not gain any benefits
from renown while in that identity unless she has the renown social talent or a similar ability.

This ability replaces trapfinding.

## Ready for Betrayal (Ex) {#ready-for-betrayal}

At 3rd level, a Galtan agitator gains a +1 bonus on Perception checks to recognize disguises and
notice hiding creatures and on Sense Motive checks to disbelieve lies. These bonuses increase by 1
every 3 rogue levels thereafter (to a maximum of +6 at 18th level).

This ability replaces trap sense.

## Enthralling Agitation (Su) {#enthralling-agitation}

At 4th level, a Galtan agitator can captivate a crowd once per day, as per the spell
_[enthrall](ref/spell/enthrall)_. (DC = 10 + 1/2 the Galtan agitator's rogue level + her Charisma
modifier). During the spell's effect, the Galtan agitator can attempt a DC 15 Charisma check to
increase her individual or organizational influence with the members of the crowd by 1 rank or step.
Or, if the crowd members' attitudes toward the Galtan agitator are indifferent or worse, this check
can improve their attitudes by 1 step. The Galtan agitator can never use this ability to increase
her individual or organization influence or improve the crowd's attitude by more than 2 ranks or
steps.

This replaces the rogue talent gained at 4th level.

## Revolutionary's Cause (Su) {#revolutionary-s-cause}

At 8th level, the Galtan agitator can lift an enthralled crowd's emotions and turn them toward a
common purpose. As a standard action after she has used her enthralling agitation —but before the
[enthrall](ref/spell/enthrall) effect wears off—she can target the affected creatures with a
plausible _[suggestion](ref/spell/suggestion)_ (DC = 10 + 1/2 her rogue level + her Charisma
modifier). that has a duration of up to 1 day.

This ability replaces the rogue talent gained at 8th level.

## Leadership (Ex) {#leadership}

At 12th level, a Galtan agitator gains [Leadership](ref/feat/leadership) as a bonus feat. If the
Galtan agitator already has the Leadership feat, she doubles her Charisma modifier when calculating
her base Leadership score.

This replaces the rogue talent gained at 12th level.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the Galtan agitator archetype: canny observer, coax
information, follow clues, hard to fool, and strong impression.

## Advanced Rogue Talents {#advanced-rogue-talents}

The following advanced rogue talents complement the Galtan agitator archetype: feat, thoughtful
reexamining, and skill mastery.
