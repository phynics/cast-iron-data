+++
id = "ref/rule/step-4-template-graft"
kind = "rule"
title = "Step 4: Template Graft"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "step_4_template_graft", path = "json/rules_adv_gm02.json" },
]
[[sources]]
publication = "pathfinder-unchained"
page = "216"

[fields]
kind = "none"
+++

These optional grafts replicate popular monster templates, and are applied on top of the creature
type or class graft chosen for the monster. Template graft entries follow a format similar to
creature type grafts.

**Minimum or Maximum CR:** This entry indicates what the lowest or highest possible CR for the
monster can be. A header that says "CR 2+" indicates the monster's CR must be 2 or higher, and "CR
9-" means its CR can't be higher than 9.

**Required Creature Type or Subtype:** For templates that change a creature's type or subtype in the
normal monster creation system, this entry shows which creature type or subtype the monster must be
in order to apply the template graft.

**Suggested Array:** This indicates the monster array the template is most closely associated with,
if any. Liches, for example, are almost always spellcasters.

**Automatic Traits:** All creatures with this graft gain these abilities. The automatic traits might
tell you to add particular monster options or skills. These count against the monster's normal
number of options, skills, and so forth, replacing them (unlike subtype grafts, which grant options
and skills for free). However, even if the automatic traits would cause a monster to exceed its
maximum number of options or skills, the monster still gains all of them. If the monster has a class
graft, use your best judgment when replacing options to maintain the feeling of both the class and
template.

**Suggested Ability Modifiers:** This section lists the recommended assignments for the monster's
high ability scores, in order from highest to lowest. For instance, the graveknight lists "Strength,
Charisma, Wisdom," meaning that when making a CR 10 graveknight, you would give it a +7 Strength
modifier, a +5 Charisma modifier, and a +3 Wisdom modifier. Not all entries list modifiers for all
abilities. A ghost, for example, lists only Charisma since the remaining statistics can vary, and a
half-dragon doesn't have an entry at all as half-dragons are so varied.

### Ghost (CR 2+)

A soul unable to rest becomes a spectral undead creature.

**Required Creature Type:** Undead.

**Required Subtype:** Incorporeal.

**Automatic Traits:** Fly 30 ft. (perfect); Ability modifiers-set Strength modifier to -, increase
Charisma modifier by 2; options-channel resistance, corrupting touch, rejuvenation (2d4 days); one
of the following at CR 6 plus one for every 3 CR above 6: at-will magic
([telekinesis](ref/spell/telekinesis)), corrupting gaze, draining touch, frightful presence,
malevolence; skills-gain Perception and Stealth as master skills.

**Suggested Ability Modifiers:** Charisma.

### Graveknight (CR 5+)

This undead creature is heavily armed and armored, and can be rejuvenated if destroyed.

**Required Creature Type:** Undead.

**Suggested Array:** Combatant.

**Automatic Traits:** Increase AC by 2 and touch AC by 4, decrease flat-footed AC by 6;
options-channel destruction, [channel resistance](ref/rule/channel-resistance), devastating blast
(as the breath weapon option in a 30-foot cone dealing acid, cold, electricity, or fire damage), DR
10/magic, immunity (cold and electricity), phantom mount, rejuvenation (1d10 days), sacrilegious
aura, [spell resistance](ref/rule/spell-resistance), undead mastery, one additional combat option;
skills-gain Intimidate, Perception, and Ride as master skills. Suggested Ability Modifiers:
Strength, Charisma.

### Half-Celestial (CR 1+)

This creature was born of a good outsider and a mortal, or created by a major infusion of holy
energy.

**Required Creature Type:** Outsider.

**Automatic Traits:** +4 bonus on saving throws against poison; gain a fly speed equal to twice base
speed (good maneuverability); options-DR 5/magic (increases to DR 10/magic at CR 12), energy
resistance 10 (acid, cold, and electricity), immunity (disease), secondary magic (good), smite
(evil); skill-gain one additional master skill.

### Half-Dragon (CR 3+)

This creature is born of a dragon and some other form of creature. It exhibits traits of both its
parents.

**Required Creature Type:** Dragon.

**Automatic Traits:** Options-breath weapon (usable 1/day), immunity (sleep, paralysis, and one of
acid, cold, electricity, or fire); skill-gain one additional master skill.

### Half-Fiend (CR 1+)

This creature is heavily tainted with evil power, most likely demonic or infernal.

**Required Creature Type:** Outsider.

**Automatic Traits:** Gain a fly speed equal to twice the base speed (good maneuverability);
options-DR 5/magic (increases to DR 10/magic at CR 12), energy resistance 10 (acid, cold,
electricity, and fire), immunity (poison), secondary magic (evil), smite (good); skill-gain one
additional master skill.

### Lich (CR 2+)

This spellcaster retained its magical powers after it died and rose again in undeath.

**Required Creature Type:** Undead.

**Suggested Array:** Spellcaster.

**Automatic Traits:** Increase AC by 2; options-channel resistance, DR 15/bludgeoning and magic,
fear aura, immunity (cold and electricity), paralyzing touch, rejuvenation (1d10); skills-gain
Perception, Sense Motive, and Stealth as master skills.

**Suggested Ability Modifiers:** Intelligence, Wisdom, or Charisma should be highest ability
modifier, depending on which of these the lich uses to cast its spells.

### Lycanthrope (CR 1+)

This humanoid can turn into an animal or assume a hybrid form between its humanoid and animal
natures.

**Required Creature Type:** Humanoid.

**Required Subtype:** Shapechanger.

**Automatic Traits:** Options-curse of lycanthropy.

**Suggested Ability Modifiers:** Constitution.

### Skeleton (CR 8-)

The animated bones of the dead attack as a skeleton - a mindless soldier in an army of the dead.

**Required Creature Type:** Undead.

**Suggested Array:** Combatant.

**Automatic Traits:** Ability modifiers-set Intelligence modifier to -; options-DR 5/bludgeoning,
immunity (cold), improved initiative.

**Suggested Ability Modifiers:** Strength, Dexterity.

### Vampire (CR 5+)

This charismatic undead monster feasts on blood and has impressive supernatural powers.

**Required Creature Type:** Undead.

**Suggested Array:** Any: a vampire could fill any role and be built using any array. It is capable
in combat even if it's an expert or spellcaster.

**Automatic Traits:** Increase AC by 2 and flat-footed AC by 2,
[spider climb](ref/spell/spider-climb) (constant), vampire weaknesses; options-at-will magic
([dominate person](ref/spell/dominate-person)), blood drain, change shape (dire bat or wolf, as
[beast shape II](ref/spell/beast-shape-2)), [channel resistance](ref/rule/channel-resistance),
children of the night, create spawn, DR 10/magic and silver, energy drain, energy resistance 10
(cold and electricity), [fast healing](ref/umr/fast-healing) 5, gaseous form; skills-gain Bluff,
Perception, Sense Motive, and Stealth as master skills.

**Suggested Ability Modifiers:** Strength, Dexterity, Charisma.

### Zombie(CR 9-)

A reanimated corpse can become a sluggish and unthinking zombie.

**Required Creature Type:** Undead.

**Suggested Array:** Combatant.

**Automatic Traits:** Staggered (can perform only a single move action or standard action each
round); ability modifiers-set Intelligence modifier to -; options-DR 5/slashing, extra hit points;
skills-no master or good skills.

**Suggested Ability Modifiers:** Strength.
