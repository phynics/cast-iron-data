+++
id = "ref/arc-brawler/strangler"
kind = "archetype"
title = "Strangler"
aon = "ArchetypeDisplay.aspx?FixedName=Brawler%20Strangler"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "strangler", path = "json/archetypes_brawler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/brawler" },
]
[[sources]]
publication = "advanced-class-guide"
page = "88"

[fields]
kind = "archetype"
features = [
  { anchor = "strangle", level = 1 },
  { anchor = "practiced-strangler", level = 2 },
  { anchor = "sleeper-hold", level = 4 },
  { anchor = "neckbreaker", level = 16 },
]
trades = [
  { replaces = "Unarmed strike", feature = "unarmed-strike", by = ["strangle"] },
  { replaces = "brawler's flurry", feature = "brawler-s-flurry", by = ["strangle"] },
  { replaces = "AC bonus", feature = "ac-bonus", by = ["practiced-strangler"] },
  { replaces = "Awesome blow", feature = "awesome-blow", by = ["neckbreaker"] },
  { replaces = "improved awesome blow", feature = "improved-awesome-blow", by = ["neckbreaker"] },
  { alters = "Knockout", feature = "knockout", by = ["sleeper-hold"] },
]
+++

A strangler is trained to choke the life out of her victims with her vise-like grip. Some stranglers
are self-taught and are little more than brutish murderers, unhinged sociopaths, or opportunistic
alley-bashers. Others are members of murder cults or specialized schools of assassination, trained
since the cradle to kill with their bare hands.

## Class Skills {#class-skills}

A strangler gains Stealth as a class skill.

## Strangle (Ex) {#strangle}

At 1st level, a strangler deals +1d6 [sneak attack](ref/ability/sneak-attack) damage whenever she
succeeds at a [grapple](ref/rule/grapple) check to damage or pin an opponent. The strangler is
always considered flanking her target for the purpose of using this ability. This damage increases
by +1d6 at 2nd, 8th and 15th levels. This ability replaces unarmed strike and brawler's flurry.

## Practiced Strangler (Ex) {#practiced-strangler}

At 2nd level, when a strangler has the [grappled](ref/rule/grapple-conditions) condition, she does
not take a -4 penalty to Dexterity and does not lose her Dexterity bonus to AC. At 9th level, a
grappling or grappled strangler still threatens an area and is still able to make attacks of
opportunity while grappling or grappled; when pinned, she is not denied her Dexterity bonus and does
not take a -4 penalty to Armor Class. This ability replaces AC bonus.

## Sleeper Hold (Ex) {#sleeper-hold}

At 4th level, a strangler can instantly render a pinned opponent unconscious. This works like the
knockout ability, but requires a successful grapple combat maneuver check against the pinned
opponent and does not have to damage the opponent. Creatures that do not need to breathe, are immune
to critical hits, or are immune to nonlethal damage are immune to this ability. At 10th level, a
strangler can use this ability twice per day. At 16th level, she can use it three times per day.
This alters knockout.

## Neckbreaker (Ex) {#neckbreaker}

At 16th level, a strangler can attempt to instantly kill a pinned opponent as a standard action.
This works like the sleeper hold ability, but imposes a -5 penalty on her grapple combat maneuver
check. If the opponent succeeds at its Fortitude save, the strangler deals damage as if she had
attempted the grapple check to damage her opponent; if the opponent fails its Fortitude save, it
dies. Creatures that are immune to critical hits are immune to this ability. At 20th level, the
strangler can attempt this as a move action instead of a standard action. This ability replaces
awesome blow and improved awesome blow.
