+++
id = "ref/arc-kineticist/overwhelming-soul"
kind = "archetype"
title = "Overwhelming Soul"
aon = "ArchetypeDisplay.aspx?FixedName=Kineticist%20Overwhelming%20Soul"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "overwhelming_soul", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]
[[sources]]
publication = "occult-adventures"
page = "91"

[fields]
kind = "archetype"
features = [
  { anchor = "mind-over-matter" },
  { anchor = "mental-prowess" },
  { anchor = "overwhelming-power", level = 3 },
]
trades = [
  { replaces = "Internal buffer", feature = "internal-buffer", by = ["mental-prowess"] },
  { replaces = "Elemental overflow", feature = "elemental-overflow", by = ["overwhelming-power"] },
  { alters = "Class skills and the key ability score of wild talents", by = ["mind-over-matter"] },
  { alters = "Burn", feature = "burn", by = ["mental-prowess"] },
]
+++

Some kineticists have such a powerful personality that they can seize control of their element with
their minds alone, without endangering their bodies.

## Mind Over Matter (Ex) {#mind-over-matter}

An overwhelming soul uses her Charisma modifier instead of her Constitution modifier to determine
her damage with wild talents, the DCs of Constitution-based wild talents, the duration of wild
talents with a Constitution-based duration, her bonus on [concentration](ref/rule/concentration)
checks for wild talents, and the other Constitution-based effects of all her wild talents. She adds
Bluff and Diplomacy to her list of kineticist class skills. This ability alters the kineticist's
class skills and the key ability score of wild talents.

## Mental Prowess (Su) {#mental-prowess}

An overwhelming soul's mind is strong enough to protect her body from the stress of channeling the
elements. However, in exchange, she is unable to push her limits quite as far as other kineticists.
She can't choose to accept burn, though she can use wild talents with a burn cost if she can reduce
that cost to 0 points with abilities such as gather power and infusion specialization. If she would
be forced to accept burn against her will (for example, if she fails a concentration check), instead
of taking burn she takes 1 temporary [negative level](ref/rule/energy-drain-and-negative-levels),
which never kills her and can't be removed with _[restoration](ref/spell/restoration)_ or
_[greater restoration](ref/spell/restoration-greater)_, but which disappears automatically after 24
hours. At 6th level, once per day, she can reduce the total burn cost of any wild talent by 1. She
can use this ability an additional time per day at 10th level and every 4 levels thereafter. This
ability alters burn and replaces internal buffer.

## Overwhelming Power (Ex) {#overwhelming-power}

At 3rd level, an overwhelming soul gains a +1 bonus on attack rolls and damage rolls with her
kinetic blasts. The damage bonus doesn't apply to [kinetic blade](ref/kinetic/kinetic-blade),
[kinetic whip](ref/kinetic/kinetic-whip), or other infusions that don't apply the damage bonus from
elemental overflow. This bonus increases by 1 at 6th level and every 3 levels thereafter. This
ability replaces elemental overflow.
