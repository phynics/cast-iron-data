+++
id = "ref/arcaneschool/evocation"
kind = "class_option"
title = "Evocation"
source_ids = ["core-rulebook", "advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "evocation", path = "json/class_ability_arcane_schools.json" },
]
[[sources]]
publication = "core-rulebook"
page = "81"
[[sources]]
publication = "advanced-players-guide"
page = "143, 146"

[fields]
kind = "class_option"
group = "arcane-school"
features = [
  { anchor = "intense-spells" },
  { anchor = "force-missile" },
  { anchor = "elemental-wall", level = 8 },
]
+++

Evokers revel in the raw power of magic, and can use it to create and destroy with shocking ease.

## Intense Spells (Su) {#intense-spells}

Whenever you cast an evocation spell that deals hit point damage, add 1/2 your wizard level to the
damage (minimum +1). This bonus damage is not increased by [Empower Spell](ref/feat/empower-spell)
or similar effects. This bonus only applies once to a spell, not once per missile or ray, and cannot
be split between multiple missiles or rays. This damage is of the same type as the spell. At 20th
level, whenever you cast an evocation spell you can roll twice to penetrate a creature's
[spell resistance](ref/rule/spell-resistance) and take the better result.

## Force Missile (Sp) {#force-missile}

As a standard action you can unleash a force missile that automatically strikes a foe, as
_[magic missile](ref/spell/magic-missile)_. The force missile deals 1d4 points of damage plus the
damage from your intense spells evocation power. This is a force effect. You can use this ability a
number of times per day equal to 3 + your Intelligence modifier.

## Elemental Wall (Sp) {#elemental-wall}

At 8th level, you can create a wall of energy that lasts for a number of rounds per day equal to
your wizard level. These rounds do not need to be consecutive. This wall deals acid, cold,
electricity, or fire damage, determined when you create it. The elemental wall otherwise functions
like _[wall of fire](ref/spell/wall-of-fire)_.

## Admixture School {#sec-admixture-school}

**Associated School:** Evocation.

**Replacement Powers:** The following school powers replace the force missile and elemental wall
powers of the evocation school.

**Versatile Evocation (Su):** When you cast an evocation spell that does acid, cold, electricity, or
fire damage, you may change the damage dealt to one of the other four energy types. This changes the
descriptor of the spell to match the new energy type. Any non-damaging effects remain unchanged
unless the new energy type invalidates them (an _[ice storm](ref/spell/ice-storm)_ that deals fire
damage might still provide a penalty on Perception checks due to smoke, but it would not create
difficult terrain). Such effects are subject to GM discretion. You can use this ability a number of
times per day equal to 3 + your Intelligence modifier.

**Elemental Manipulation (Su):** At 8th level, you can emit a 30-foot aura that transforms magical
energy. Choose an energy type from acid, cold, electricity, and fire, and a second type to transform
it into. Any magical source of energy of this type with a caster level equal to or less than your
wizard level is altered to the chosen energy type. This includes supernatural effects from creatures
with Hit Dice no greater than your caster level. For example, you could transform a
[white dragon's](ref/family/dragon-white) frigid breath weapon (a supernatural ability), but not a
[fire elemental's](ref/monster/fire-elemental) fiery touch (an extraordinary ability). If an effect
lies only partially within your aura, only the portions within the aura are transformed. You can use
this ability for a number of rounds per day equal to your wizard level. The rounds do not need to be
consecutive.

## Generation School {#sec-generation-school}

**Associated School:** Evocation.

**Replacement Powers:** The following school powers replace the intense spells and force missile
powers of the evocation school.

**Lingering Evocations (Su):** Any evocation spell you cast with a duration greater than
instantaneous lasts an additional number of rounds equal to 1/2 your wizard level (minimum +1). At
20th level, any dispel checks made against your evocation spells must be rolled twice, and your
opponent must use the less favorable result.

**Wind Servant (Sp):** As a standard action, you can generate a blast of air that hurls an
unattended object (or objects) or an object in your possession up to 30 feet in a straight line. If
you have a free hand, you can catch an object hurled toward yourself. You can move objects weighing
up to 1 pound per wizard level. Objects are not thrown with enough force to cause damage, although
fragile objects like alchemical weapons shatter on contact with a creature or hard surface. To hit a
creature with an object, you must succeed at a ranged touch attack. You can use this ability a
number of times per day equal to 3 + your Intelligence modifier.
