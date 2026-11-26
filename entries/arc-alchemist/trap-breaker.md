+++
id = "ref/arc-alchemist/trap-breaker"
kind = "archetype"
title = "Trap Breaker"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Trap%20Breaker"
source_ids = ["dungeoneers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "trap_breaker", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "dungeoneers-handbook"
page = "23"

[fields]
kind = "archetype"
features = [
  { anchor = "trapfinding", level = 2 },
  { anchor = "explosive-disarm", level = 5 },
  { anchor = "land-mine", level = 6 },
  { anchor = "mine-engineering", level = 10 },
]
trades = [
  { replaces = "Poison use", feature = "poison-use", by = ["trapfinding"] },
  { replaces = "poison resistance +2", feature = "poison-resistance", levels = [2], by = ["trapfinding"] },
  { replaces = "Poison resistance +4", feature = "poison-resistance", levels = [5], by = ["explosive-disarm"] },
  { replaces = "poison resistance +6", feature = "poison-resistance", levels = [8], by = ["explosive-disarm"] },
  { replaces = "Swift poisoning", feature = "swift-poisoning", by = ["land-mine"] },
  { replaces = "Poison immunity", feature = "poison-resistance", levels = [10], by = ["mine-engineering"] },
]
+++

Trap breakers forgo the study of poison to instead master the construction and deployment of traps,
using their nimble fingers to disable dangerous devices and their alchemical knowledge to create
devastating land mines.

## Trapfinding (Ex) {#trapfinding}

Starting at 2nd level, a trap breaker adds 1/2 his alchemist level on Perception checks made to
locate traps and on Disable Device checks. A trap breaker can use Disable Device to disarm magic
traps. This ability replaces poison use and poison resistance +2.

## Explosive Disarm (Ex) {#explosive-disarm}

At 5th level, a trap breaker can attempt to disarm a mechanical trap by detonating it rather than
disarming it with a Disable Device check. As a full-round action, a trap breaker may expend one of
his bombs to make a ranged touch attack against a trap, using the trap's Disable Device DC as its
AC. If the attack misses, the bomb's splash damage activates the trap. If the attack hits, the bomb
deactivates the trap without setting it off. The trap breaker must both know the location of the
trap and be able to reach the trap's trigger with a ranged touch attack in order to use this
ability. At 8th level, a trap breaker can disarm magic traps with this ability. This ability
replaces poison resistance +4 and poison resistance +6.

## Land Mine (Ex) {#land-mine}

At 6th level, a trap breaker can turn his bombs into land mines. Setting a land mine is a full-round
action that provokes attacks of opportunity. The land mine fills a single 5-foot square, and can't
be placed in the same space as another trap, land mine, or magic trap. The trap breaker can arm the
land mine with any bomb he is eligible to use, and the effects of this bomb are immediately
transferred to the land mine. Creating a land mine uses up two of the alchemist's bombs per day. The
DCs for Perception checks to notice the land mine, Disable Device checks to disable it, and saving
throws to avoid its effects are equal to 10 + 1/2 the alchemist's level + his Intelligence modifier.
All alchemist land mines are mechanical traps with the qualities _Trigger_: location and _Reset_:
none. Land mines last for 1 day per alchemist level or until they are triggered, whichever comes
first. This ability replaces swift poisoning.

## Mine Engineering (Ex) {#mine-engineering}

At 10th level, a trap breaker's expertise in improving explosives allows him to create land mines
with minimal expense. Creating a land mine uses up only one of the alchemist's bombs per day. This
ability replaces poison immunity.
