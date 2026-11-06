+++
id = "ref/template/recycled-construct"
kind = "rule"
title = "Recycled Construct"
source_ids = ["construct-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "recycled_construct", path = "json/monster_template3.json" },
]

[fields]
kind = "none"
+++

**Recycled Construct**

**Acquired:** present

**Challenge rating:** -1

**Source:** Construct Handbook/52

A skilled artificer can revitalize a ruined construct by jury-rigging the pieces left intact. The
patchwork nature of a recycled construct renders it fragile and leaves key circuitry exposed.
reducing its bonus hit points by 5.

"Recycled construct" is an acquired template that can be added to a [construct](ref/type/construct)
with 3 or more Hit Dice made predominantly of solid material. A recycled construct uses all the base
creature's statistics and special abilities except as noted here.

**CR:** Base creature's CR - 1.

**Defensive Abilities:** Reduce any [damage reduction](ref/rule/damage-reduction) or
[hardness](ref/umr/hardness) by 5. Replace any immunity to magic with
[spell resistance](ref/rule/spell-resistance) equal to the base creature's CR + 11. Any exceptions
to the base creature's immunity to magic automatically bypass the recycled construct's spell
resistance and function as described for the base creature.

**Weaknesses:** A recycled construct gains the following weakness.

> **Malfunction (Ex):** A recycled construct that takes precision damage or extra damage from a
> critical hit becomes [staggered](ref/misc/staggered) for 1 round and immediately triggers a
> malfunction. To determine the nature of this malfunction, roll 1d10 and consult the table below
> (CL = the base creature's HD; save DC = 10 + the base creature's HD). A creature can use a move
> action to attempt a special [Disable Device](ref/skill/disable-device) check before dealing
> precision damage to a recycled construct (DC = 20 + the base creature's HD). On a success, the
> attacking creature can roll twice and choose the malfunction result.
>
> |d10|Malfunction|
> | --- | --- |
> |1|No additional effect|
> |2|Sparks fly from the construct, [dazzling](ref/misc/dazzled) each adjacent creature that can see it (Fortitude negates).|
> |3|The construct flails wildly, making one melee attack against each adjacent creature. If the construct is wielding only a ranged weapon, it uses that weapon as an [improvised bludgeoning weapon](ref/misc/improvised-weapons).|
> |4|The construct leaks lubricant, affecting itself and all adjacent squares as if with a [grease](ref/spell/grease) spell for 1d4+1 rounds.|
> |5|The attack causes the construct to seize violently, functioning as a free [disarm](ref/rule/disarm) combat maneuver check against the weapon that triggered the malfunction. On a success, the weapon is thrown 1d4×10 feet in a random direction. A natural weapon instead provokes a free [grapple](ref/rule/grapple) combat maneuver attempt against the attacking creature for 1 round. This malfunction has no effect on ammunition.|
> |6|Acrid smoke, steam, or mist pours from the construct, as if from a [pyrotechnics](ref/spell/pyrotechnics) smoke cloud.|
> |7|Shrapnel explodes from the construct in all directions, dealing 1d6 points of slashing damage per Hit Die of the construct to each creature within 20 feet (Reflex half).|
> |8|The construct emits an earsplitting screech, [deafening](ref/misc/deafened) all creatures within 20 feet (Fortitude negates).|
> |9|Disruptive energy pulses from the construct, functioning as [dispel magic](ref/spell/dispel-magic) targeting every creature within 20 feet.|
> |10|The construct goes berserk, as a [clay golem](ref/monster/golem-clay-golem).|

**Attacks:** If the base creature has more than one natural attack, remove one natural attack. The
creator can replace the lost attack with a light, one-handed, or ranged weapon of at least
masterwork quality and a size appropriate for the base creature.

### Construction

A recycled construct is built from the remains of the base creature. When destroyed, the base
creature must not have taken damage exceeding its total hit points plus 20; otherwise the remnants
were too badly damaged to be useful. Additionally, recycling the construct requires replacement
parts worth half the value of the base creature's body. Construction requirements are identical to
the base creature, except the DC of any relevant skill checks is reduced by 5 and the cost is
reduced by half.

### Recycling Robots

In order to create a recycled robot or similar construct, a crafter must have the
[Craft Construct](ref/feat/craft-construct) feat and the [Technologist](ref/feat/technologist) feat.
Creating a recycled robot requires the remains of other complex constructs, such as robots or
clockworks, collectively worth 50,000 gp or more. Crafting a Medium or smaller recycled robot
requires the remains of two Medium complex constructs; a Large robot requires the remains of four
Medium constructs, and so on. Crafting a recycled robot requires 1 week per set of Medium complex
construct remains required for construction.

While creating a recycled robot, the crafter must attempt one
[Knowledge (engineering)](ref/skill/knowledge-engineering) check per Medium construct remains used
in construction (DC = 20 + the base creature's CR). For each failed check, the recycled robot gains
a glitch. To determine the nature of this glitch, roll 1d6 and consult the table below. Multiple
glitches of the same type stack. If the crafter fails more than half of the required Knowledge
(engineering) checks, he fails to recycle the construct and ruins the materials.

|d6|Glitch|
| --- | --- |
|1|Reduce any bonus hp the base construct received by 5 (minimum 0).|
|2|Reduce all movement speeds by 5 feet. If the recycled construct's burrow, fly, or swim speed is reduced to 0, it loses that movement option. Land speed can be reduced to a minimum of 5 feet.|
|3|Reduce base attack bonus by 1 (minimum +0).|
|4|Reduce any natural armor bonus by 1 (minimum +0).|
|5|The recycled robot takes a -1 penalty on all skill checks.|
|6|The recycled robot has a 5% chance each round of acting erratically, as if [confused](ref/misc/confused).|
