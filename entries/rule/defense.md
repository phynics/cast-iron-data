+++
id = "ref/rule/defense"
kind = "rule"
title = "Defense"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "defense", path = "json/rules_opt_combat01.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "191"

[fields]
kind = "none"
+++

In this alternative system, a creature does not have an Armor Class (AC); it instead has a Defense
score. Defense is similar to touch AC in the standard Pathfinder Roleplaying Game rules, but it also
adds the shield bonus (including any enhancement bonus to the shield), and any enhancement bonus to
armor.

> Defense = 10 + shield bonus + Dexterity modifier + other modifiers (including armor's enhancement
> bonus, but not armor bonus or natural armor bonus)

Defense represents how easy or difficult it is to hit a creature. The shield bonus is added because
a creature is considered to be actively blocking attacks with its shield whenever it can, which is
whenever it would gain its Dexterity bonus to AC and not be flat-footed.

**Losing Dexterity Bonus to Defense:** Situations or effects that would cause you to lose your
Dexterity bonus to AC instead cause you to lose your Dexterity bonus to Defense. Also, whenever you
lose your Dexterity bonus to Defense, you also lose any shield bonus to Defense, since when you lose
your Dexterity bonus to AC, you also lose the ability to properly respond to attacks with your
shield.

**Flat-Footed Defense:** You do not gain your Dexterity or shield bonus to your Defense if you are
flat-footed or lose your Dexterity bonus to Defense; thus, your Flat-Footed Defense is equal to your
Defense minus your Dexterity bonus and shield bonus.

**Defense and Using a Shield without Proficiency:** When a creature uses a shield it is not
proficient with, it takes that shield's armor check penalty as a penalty to the shield bonus, along
with the other penalties for using a shield without proficiency. Furthermore, it also takes this
penalty to its Flat-Footed Defense, as the shield actually gets in the way instead of defending
against incoming attacks.
