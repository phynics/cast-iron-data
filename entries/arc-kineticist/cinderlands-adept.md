+++
id = "ref/arc-kineticist/cinderlands-adept"
kind = "archetype"
title = "Cinderlands Adept"
aon = "ArchetypeDisplay.aspx?FixedName=Kineticist%20Cinderlands%20Adept"
source_ids = ["wilderness-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cinderlands_adept", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]
[[sources]]
publication = "wilderness-origins"
page = "28"

[fields]
kind = "archetype"
features = [
  { anchor = "fire-focus", level = 1 },
  { anchor = "galloping-siphon", level = 1 },
  { anchor = "mount", level = 4 },
]
trades = [
  { replaces = "Infusion gained at 1st level", feature = "infusion", levels = [1], by = ["galloping-siphon"] },
  { replaces = "Utility wild talents gained at 4th, 8th, and 12th levels", feature = "wild-talents", levels = [4, 8, 12], by = ["mount"] },
  { alters = "Elemental focus", feature = "elemental-focus", by = ["fire-focus"] },
  { alters = "expanded element", feature = "expanded-element", by = ["fire-focus"] },
  { alters = "Gather power", feature = "gather-power", by = ["galloping-siphon"] },
  { alters = "Class skills" },
]
+++

Among the Sun Clan's most noted champions are those who can tame the flames and bend them to their
will. These kineticists are skilled riders, able to wield both weapons and fire with deadly skill.

## Class Skills {#class-skills}

A Cinderlands adept gains Handle Animal and Ride as class skills, but does not gain Stealth and Use
Magic Device as class skills.

This alters the kineticist's class skills.

## Fire Focus (Su) {#fire-focus}

When a Cinderlands adept gains elemental focus, she must select fire (pyrokinesis) as her chosen
[element](ref/ability/elements). When she gains the expanded element class feature at 7th and 15th
levels, she must select her primary element of fire and does not learn to use a new element.

This alters elemental focus and expanded element.

## Galloping Siphon (Su) {#galloping-siphon}

When a Cinderlands adept gathers power while mounted, she and her mount gain fire
[resistance](ref/umr/resistance) 5 for a number of rounds equal to the total value of the burn cost
she reduces. This resistance increases to fire resistance 10 at 11th level. The Cinderlands adept
and her mount lose this resistance if she dismounts before the duration ends. In addition, a
Cinderlands adept gains [Mounted Combat](ref/feat/mounted-combat) as a bonus feat and a +1 bonus on
[concentration](ref/rule/concentration) checks due to riding. This bonus increases by +1 at 4th
level and every 4 levels thereafter (up to a maximum of +6 at 20th level).

This alters gather power and replaces the infusion gained at 1st level.

## Mount {#mount}

At 4th level, a Cinderlands adept gains a loyal mount. This ability functions like the
[druid's](ref/class/druid) [animal companion](ref/sidekick/animal-companion) ability (as described
in the nature bond class feature), except that the Cinderlands adept always gains a
[horse](ref/companion/horse) or [pony](ref/companion/pony) (though she can gain additional options
at the GM's discretion) and her effective druid level is equal to her burn rider level -3.

This replaces the utility wild talents gained at 4th, 8th, and 12th levels.
