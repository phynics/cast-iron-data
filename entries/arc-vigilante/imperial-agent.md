+++
id = "ref/arc-vigilante/imperial-agent"
kind = "archetype"
title = "Imperial Agent"
aon = "ArchetypeDisplay.aspx?FixedName=Vigilante%20Imperial%20Agent"
source_ids = ["blood-of-the-ancients"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "imperial_agent", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "blood-of-the-ancients"
page = "21"

[fields]
kind = "archetype"
features = [
  { anchor = "slander", level = 1 },
  { anchor = "manipulative", level = 3 },
  { anchor = "false-flag", level = 5 },
]
trades = [
  { replaces = "Social talent gained at 1st level", feature = "social-talent", levels = [1], by = ["slander"] },
  { replaces = "Unshakable", feature = "unshakable", by = ["manipulative"] },
  { replaces = "Social talent gained at 5th level", feature = "social-talent", levels = [5], by = ["false-flag"] },
]
+++

Many residents of Lung Wa's successor states refuse to admit the empire has truly fallen, but the
self-proclaimed imperial agents have taken matters into their own hands. Imperial agents are often
the descendants of nobility and generals from Lung Wa, devoted to reuniting the empire by conquering
Lung Wa's successor states. Often forming secret networks with fanciful names, they focus on
destabilizing nations with blackmail, slander, and treachery.

## Slander (Ex) {#slander}

At 1st level, an imperial agent becomes an expert at spreading malicious rumors in order to foment
chaos and strife to further his aims. Slandering an individual or organization takes 1d4 days in a
[settlement](ref/rule/the-shape-of-civilization) smaller than a town, or 1 week in a town or larger
settlement. The imperial agent must succeed at either a Bluff or Diplomacy check. If the general
populace is indifferent towards the target of the slander, the DC of this check is 20 + the target's
Charisma modifier. For each step above indifferent the public's attitude towards the target is, the
DC increases by 5, and for each step below indifferent the public's attitude towards the target is,
the DC decreases by 5. If the imperial agent is successful, the public's attitude toward his target
is decreased by 1 step. If the imperial agent fails the check, however, he cannot affect the
settlement with this ability for 1 week, and the target of his slander becomes aware that someone is
spreading malicious rumors. The GM determines the exact effects of the public's shift in attitude.
Even if the public is hostile toward the target, they might not act openly against the target,
especially if doing so might be dangerous.

This replaces the social talent gained at 1st level.

## Manipulative (Ex) {#manipulative}

At 3rd level, an imperial agent is a master of blackmail, extortion, and subterfuge. He gains a
bonus equal to 1/2 his vigilante level on Bluff checks (except those to feint) and on Intimidate
checks (except those to demoralize an opponent).

This replaces unshakable.

## False Flag (Ex) {#false-flag}

At 5th level, whenever an imperial agent changes his identity, he has a third option (instead of
social or vigilante): he can wear a false flag. This functions identically to the
[many guises](ref/soctalent/many-guises) social talent, except that the false flag identity is
associated with a particular nation, organization, or other faction. The imperial agent gains a +20
circumstance bonus on Disguise checks to impersonate a member of that faction against creatures who
are unaffiliated with that faction, potentially allowing the imperial agent to pin the blame for his
actions on the faction he was impersonating. However, the imperial agent receives no bonus and a -10
penalty on Disguise checks against members of the faction he is impersonating. An imperial agent can
choose a different faction each time he uses this ability. Factions that lack a flag, uniform, or
other symbol of membership may be difficult or impossible to impersonate, at the GM's discretion.

This replaces the social talent gained at 5th level.
