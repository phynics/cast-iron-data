+++
id = "ref/arc-fighter/skirmisher"
kind = "archetype"
title = "Skirmisher"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Skirmisher"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "skirmisher", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]

[fields]
kind = "archetype"
features = [
  { anchor = "wilderness-training" },
  { anchor = "conditioning", level = 2 },
  { anchor = "light-infantry-training" },
  { anchor = "reconnaissance-training" },
  { anchor = "mobility-training", level = 3 },
  { anchor = "mobile-mastery", level = 19 },
]
trades = [
  { replaces = "The fighter's weapon and armor proficiency", feature = "weapon-and-armor-proficiencies" },
  { replaces = "2nd level fighter bonus feat", feature = "bonus-feats", levels = [2], by = ["conditioning"] },
  { replaces = "Bravery", feature = "bravery", by = ["reconnaissance-training"] },
  { replaces = "Armor training", feature = "armor-training", by = ["mobility-training"] },
  { replaces = "Armor mastery", feature = "armor-mastery", by = ["mobile-mastery"] },
  { alters = "Class skills", by = ["wilderness-training"] },
  { alters = "skill ranks per level", by = ["wilderness-training"] },
]
+++

Not all battles are fought between armies; sometimes, a settlement or nation faces a threat too dire
to fight in the open. In order to repel a much larger enemy force, some soldiers must abandon
equipment and tactics designed for open-field warfare and instead rely on ambushes, hit-and-run
tactics, and sabotage to whittle down their enemies' strength and morale. Skirmishers use harsh
weather and unforgiving terrain to their advantage, attacking isolated groups of enemies that cannot
flee or fight back effectively. Many tribal warriors also employ small-unit tactics because it is
part of their warrior culture, because they cannot field a large army, or simply because they refuse
to fight on the enemy's terms.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A skirmisher is proficient with light armor and shields but not with medium armor, heavy armor, or
tower shields.

This replaces the fighter's weapon and armor proficiency.

## Wilderness Training (Ex) {#wilderness-training}

A skirmisher relies on his skills and the element of surprise rather than the heaviest shields and
armor. He gains [Acrobatics](ref/skill/acrobatics) and [Stealth](ref/skill/stealth) as class skills.
In addition, the skirmisher gains a number of skill ranks at each level equal to 4 + his
Intelligence modifier, instead of 2 + his Intelligence modifier.

This alters the fighter's class skills and skill ranks per level.

## Conditioning (Ex) {#conditioning}

At 2nd level, a skirmisher becomes more resistant to mental and physical threats that are commonly
employed by his enemies or often encountered in the terrain in which he operates. The skirmisher
must choose one of the specializations below, gaining a +1 bonus on saving throws of the appropriate
type. This bonus increases by 1 for every 4 levels beyond 2nd.

### Alpine Training (Ex) {#alpine-training}

A skirmisher operating in mountainous terrain becomes resistant to cold climates and the rigors of
long treks at high altitudes. He gains a bonus on Fortitude saving throws against
[altitude sickness](ref/rule/mountain-travel), exposure to [cold weather](ref/rule/cold-dangers),
and other effects that cause [fatigue](ref/misc/fatigued) or [exhaustion](ref/misc/exhausted).

### Counter-Interrogation Training (Ex) {#counter-interrogation-training}

A skirmisher undertaking infiltration missions learns to resist interrogation and persuasion. The
skirmisher gains a bonus on Will saving throws against charms and divinations.

### Jungle Training (Ex) {#jungle-training}

Through repeated exposure, a skirmisher operating in jungles and wetlands builds up a tolerance
against pathogens and toxins. He gains a bonus on Fortitude saving throws against disease and
poison.

## Light Infantry Training (Ex) {#light-infantry-training}

A skirmisher fighting in a light infantry unit learns to avoid fire from enemy artillery, siege
weapons, and spellcasters. He gains a bonus on Reflex saving throws against attacks that deal half
damage on a successful save (such as the _[fireball](ref/spell/fireball)_ spell) but not against
traps, natural hazards, or environmental effects.

This replaces the bonus feat the fighter normally receives at 2nd level.

## Reconnaissance Training (Ex) {#reconnaissance-training}

A skirmisher operating in heavily trapped or naturally hazardous areas learns to expertly avoid
them. At 2nd level, he gains a +1 bonus on Reflex saving throws to avoid traps, natural hazards, and
environmental effects. This bonus increases by 1 for every 4 levels beyond 2nd.

This replaces bravery.

## Mobility Training (Ex) {#mobility-training}

At 3rd level, a skirmisher learns to be more maneuverable while wearing light or no armor. He gains
a +1 dodge bonus to AC while wearing light or no armor and while carrying no more than a light load.
Anything that causes the skirmisher to lose his Dexterity bonus to AC also causes the skirmisher to
lose this dodge bonus. This bonus increases by 1 for every 4 levels beyond 3rd (to a maximum of +4
at 15th level).

In addition, a skirmisher gains an enhancement bonus of +5 feet to his base speed. At 7th level, the
bonus increases to +10 feet. This benefit applies only when he is wearing no armor or light armor,
and when he is carrying no more than a light load.

This replaces armor training.

## Mobile Mastery (Ex) {#mobile-mastery}

At 19th level, a skirmisher learns to position his body and conceal his body proportions with
clothes so well that it is difficult to hit him. He gains a 20% miss chance on attacks against him.
Mobile mastery functions even when the skirmisher is [flat-footed](ref/rule/flat-footed), but not
when he is immobilized or [helpless](ref/misc/helpless), when he wears medium or heavy armor, or
when he carries a medium or heavy load.

This replaces armor mastery.
