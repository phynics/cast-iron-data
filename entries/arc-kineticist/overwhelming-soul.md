+++
id = "ref/arc-kineticist/overwhelming-soul"
kind = "archetype"
title = "Overwhelming Soul"
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
replaces = ["Internal buffer", "Elemental overflow"]
alters = ["Key ability score of wild talents", "Burn"]
replaces_features = ["internal-buffer", "elemental-overflow"]
alters_features = ["burn"]
+++

Some kineticists have such a powerful personality that they can seize control of their element with
their minds alone, without endangering their bodies.

**Mind Over Matter (Ex)**

**Ability:** An overwhelming soul uses her Charisma modifier instead of her Constitution modifier to
determine her damage with wild talents, the DCs of Constitution-based wild talents, the duration of
wild talents with a Constitution-based duration, her bonus on
[concentration](ref/rule/concentration) checks for wild talents, and the other Constitution-based
effects of all her wild talents.

**Alters:** Key ability score of wild talents

**Gained class skills:** bluff, diplo

**Mental Prowess (Su)**

**Ability:** An overwhelming soul's mind is strong enough to protect her body from the stress of
channeling the elements. However, in exchange, she is unable to push her limits quite as far as
other kineticists. She can't choose to accept burn, though she can use wild talents with a burn cost
if she can reduce that cost to 0 points with abilities such as _gather power_ and _infusion
specialization._ If she would be forced to accept burn against her will (for example, if she fails a
concentration check), instead of taking burn she takes 1 temporary
[negative level](ref/rule/energy-drain-and-negative-levels), which never kills her and can't be
removed with [restoration](ref/spell/restoration) or
[greater restoration](ref/spell/restoration-greater), but which disappears automatically after 24
hours.

**Alters:** Burn

**At 6th Level:** Once per day, she can reduce the total burn cost of any wild talent by 1.

**Replaces:** Internal buffer

**Overwhelming Power (Ex)**

**Gained:** At 3rd Level

**Passive:** An overwhelming soul gains a bonus on attack rolls and damage rolls with her kinetic
blasts. This bonus is equal to one-third of her kineticist level. The damage bonus doesn't apply to
[kinetic blade](ref/kinetic/kinetic-blade), [kinetic whip](ref/kinetic/kinetic-whip), or other
infusions that don't apply the damage bonus from _elemental overflow._

**Replaces:** Elemental overflow
