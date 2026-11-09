+++
id = "ref/arc-monk/softstrike-monk"
kind = "archetype"
title = "Softstrike Monk"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "softstrike_monk", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "martial-arts-handbook"
page = "6"

[fields]
kind = "archetype"
replaces = ["Weapon proficiency", "Bonus feats gained at 6th and 10th levels", "Empty body"]
alters = ["Unarmed strike", "Wholeness of body", "Quivering palm"]
+++

The practices of softstrike monks date back to the peaceful eras of Imperial Lung Wa. Still common
among warriors today, softstrike monks employ a nonlethal but effective form of combat.

**Weapon Proficiency**

**Info:** A softstrike monk is proficient with the [aklys](ref/eq-weapon/aklys),
[bolas](ref/eq-weapon/bolas), [club](ref/eq-weapon/club), [light flail](ref/eq-weapon/light-flail),
[light mace](ref/eq-weapon/light-mace), [nunchaku](ref/eq-weapon/nunchaku),
[quarterstaff](ref/eq-weapon/quarterstaff), [sap](ref/eq-weapon/sap), [sling](ref/eq-weapon/sling),
and any weapon with the monk special quality that can deal bludgeoning damage. He is considered
proficient only with monk weapons that can deal multiple types of damage when dealing bludgeoning
damage.

**Replaces:** Weapon proficiency

**Feather Touch (Ex)**

**Passive:** A softstrike monk does not take the normal -4 penalty on attack rolls for using a
lethal weapon to deal nonlethal damage. In addition, he can use his _stunning fist_ ability while
making a nonlethal attack with a weapon.

**Nonlethal Strikes (Ex)**

**Ability:** When a softstrike monk deals nonlethal damage with his unarmed strikes, his monk level
is treated as 4 levels higher for the purposes of determining the damage he deals (to a maximum of
4d8 at 20th level for a Medium monk).

**Alters:** Unarmed strike

**Flavor:** A softstrike monk focuses on blows that do not inflict deadly harm.

**Special:** When dealing lethal damage with his unarmed strikes, his monk level is treated as if it
were 4 levels lower (minimum 1st level) for the purpose of determining damage.

**Tenet of Life (Su)**

**Passive:** Though a softstrike monk accepts that death may happen in combat, he cannot abide
killing in cold blood. If he slays an [unconscious](ref/misc/unconscious) or
[helpless](ref/misc/helpless) living foe, or merely stands by and allows such a killing to occur, he
becomes [shaken](ref/misc/shaken) for 1 hour. In addition, the act disrupts the softstrike monk's
ki; if he has a _ki pool,_ he loses a number of ki points equal to half his level, as if they had
been spent.

**Life-Giving Blows (Su)**

**Flavor:** A softstrike monk can force a piece of his life force into a nonliving creature to
disrupt its animating essence.

**Free:** If he hits an undead foe with an unarmed attack, he can spend 1 ki point to remove the
target's immunity to nonlethal damage for a number of minutes equal to his Wisdom modifier. If,
during this time, the target's nonlethal damage exceeds its current hit points, it is destroyed.

**At 10th Level:** A softstrike monk can also use this ability against constructs.

**Gained:** At 6th Level

**Replaces:** Bonus feats gained at 6th and 10th levels

**Wholeness of Body and Spirit (Su)**

**Ability:** A softstrike monk can use wholeness of body on both himself and other creatures, though
it heals only nonlethal damage. If he uses this ability on an unconscious foe, he can spend 1
additional ki point to force the creature to accept a pact of life. The creature must succeed at a
Will saving throw (DC = 10 + half the softstrike monk's level + his Wisdom modifier) or the pact
renders it unable to directly attack the monk and any allies within 60 feet, as per
[sanctuary](ref/spell/sanctuary), for a number of days equal to the softstrike monk's level.

**Alters:** Wholeness of body

**Gained:** At 7th Level

**Incapacitating Palm (Su)**

**Ability:** A softstrike monk renders the target of his _quivering palm_ unconscious instead of
killing the creature. Upon failing its Fortitude saving throw, the target is knocked unconscious for
a number of minutes equal to the softstrike monk's level.

**Alters:** Quivering palm

**Gained:** At 15th Level

**Resilient Body (Su)**

**Gained:** At 19th Level

**Passive:** A softstrike monk's mastery of nonlethal combat lets him apply his techniques to his
defense. A softstrike monk converts any precision damage he takes to nonlethal damage.

**Replaces:** Empty body
