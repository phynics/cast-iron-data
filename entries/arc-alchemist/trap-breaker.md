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
replaces = ["Poison use", "poison resistance +2", "Poison resistance +4", "poison resistance +6", "Swift poisoning", "Poison immunity"]
replaces_features = ["poison-use", "swift-poisoning"]
+++

Trap breakers forgo the study of poison to instead master the construction and deployment of traps,
using their nimble fingers to disable dangerous devices and their alchemical knowledge to create
devastating land mines.

**Trapfinding (Ex)**

**Gained:** At 2nd Level

**Passive:** A trap breaker adds [half](ref/misc/fractions-and-rounding) his alchemist level on
Perception checks made to locate traps and on Disable Device checks. A trap breaker can use Disable
Device to disarm magic traps.

**Replaces:** Poison use, poison resistance +2

**Explosive Disarm (Ex)**

**Flavor:** A trap breaker can attempt to disarm a mechanical trap by detonating it rather than
disarming it with a Disable Device check.

**Fullround:** A trap breaker may expend one of his bombs to make a ranged touch attack against a
trap, using the trap's Disable Device DC as its AC. If the attack misses, the bomb's splash damage
activates the trap. If the attack hits, the bomb deactivates the trap without setting it off. The
trap breaker must both know the location of the trap and be able to reach the trap's trigger with a
ranged touch attack in order to use this ability.

**At 8th Level:** A trap breaker can disarm magic traps with this ability.

**Gained:** At 5th Level

**Replaces:** Poison resistance +4, poison resistance +6

**Land Mine (Ex)**

**Flavor:** A trap breaker can turn his bombs into land mines.

**Fullround:** A trap breaker can set a land mine, which fills a single 5-foot square, and can't be
placed in the same space as another trap, land mine, or magic trap. The trap breaker can arm the
land mine with any bomb he is eligible to use, and the effects of this bomb are immediately
transferred to the land mine.

**Gained:** At 6th Level

**Provokes attack of opportunity:** Yes

**Replaces:** Swift poisoning

**Special:** Creating a land mine uses up two of the alchemist's bombs per day. The DCs for
Perception checks to notice the land mine, Disable Device checks to disable it, and saving throws to
avoid its effects are equal to 10 + 1/2 the alchemist's level + his Intelligence modifier. Land
mines last for 1 day per alchemist level or until they are triggered, whichever comes first. All
alchemist land mines share the qualities listed in the trap block below.

**Alchemist Land Minds**

**Type:** Mechanical

**Challenge rating:** variable

**Perception DC:** See above

**Disable Device DC:** See above

**Trigger:** location

**Effect:** See above

**Mine Engineering (Ex)**

**Flavor:** A trap breaker's expertise in improving explosives allows him to create land mines with
minimal expense.

**Gained:** At 10th Level

**Passive:** Creating a land mine uses up only one of the alchemist's bombs per day.

**Replaces:** Poison immunity
