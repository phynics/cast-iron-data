+++
id = "ref/arc-rogue/sly-saboteur"
kind = "archetype"
title = "Sly Saboteur"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Sly%20Saboteur"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sly_saboteur", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "77"

[fields]
kind = "archetype"
replaces = ["Trap sense", "Uncanny dodge", "Improved uncanny dodge"]
+++

Sly saboteurs are irregular soldiers who specialize in sabotage and surprise attacks. Though they
often face enemies with greater numbers or resources (or both), sly saboteurs have the advantage of
knowing the local people and terrain. They might be rebels fighting against a corrupt government, or
they might be members of a militia opposing an invading force. Some are environmentalists who
sabotage the tools of industry in order to protect unspoiled nature.

**Gained class skills:** sur

**Lost class skills:** kd

**Scamper (Ex)**

**Ability:** A sly saboteur can move through 5 feet of
[difficult terrain](ref/rule/terrain-and-obstacles) each round as if it were normal terrain.

**Gained:** At 3rd Level

**Replaces:** Trap sense

**Special:** This ability allows the sly saboteur to take a 5-foot step into difficult terrain. This
ability applies only when she is wearing light armor or no armor and carrying no more than a light
load, and it stacks with the [Acrobatic Steps](ref/feat/acrobatic-steps) and
[Nimble Moves](ref/feat/nimble-moves) feats.

At 6th level: This distance 10 feet.

At 9th level: This distance 15 feet.

At 12th level: This distance 20 feet.

At 15th level: This distance 25 feet.

At 18th level: This distance 30 feet.

**Catastrophic Failure (Ex)**

**Ability:** When a sly saboteur uses Disable Device to rig a device to fail, she can increase the
DC of the check by 5. If she does so and succeeds at the check, when the device fails, users take
damage equal to the sly saboteur's sneak attack, or they take half that amount with a successful
Reflex save (DC = 10 + half the sly saboteur's level + her Dexterity modifier).

**Gained:** At 4th Level

**Replaces:** Uncanny dodge

**Special:** The type of damage depends on the nature of the device but is typically bludgeoning,
fire, piercing, or slashing.

**Disable Magic Device (Su)**

**Ability:** A sly saboteur can use Disable Device to rig a magic item to fail as if it were an
extremely complex device. If the item's effect is instantaneous, the effect is countered the next
time the item is activated, but the activation still consumes a charge or use. If the item's effect
is continuous or has a duration, the effect fails after 1d4 rounds or minutes of use (sly saboteur's
choice). This ends the duration or suppresses a continuous effect for 1d4 rounds (as the spell
[dispel magic](ref/spell/dispel-magic)). This ability cannot be used on artifacts.

**Gained:** At 8th Level

**Replaces:** Improved uncanny dodge

**Special:** If this ability is combined with the _catastrophic failure_ ability, the resulting
damage is untyped magic and is not reduced by [damage reduction](ref/rule/damage-reduction) or
energy resistance.

**These rogue talents complement this archetype:** Cunning trigger, fast stealth, getaway artist,
quick disable, quick trapsmith, rogue crawl, trap spotter, wall scramble

**These advanced rogue talents complement this archetype:** Frugal trapsmith, hide in plain sight,
knock-out blow, rumormonger, skill mastery, stealthy sniper
