+++
id = "ref/arc-mesmerist/eyebiter"
kind = "archetype"
title = "Eyebiter"
aon = "ArchetypeDisplay.aspx?FixedName=Mesmerist%20Eyebiter"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "eyebiter", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "36"

[fields]
kind = "archetype"
features = [
  { anchor = "eyeball-familiar", level = 1 },
  { anchor = "ocular-occlusion", level = 3 },
  { anchor = "staring-eye", level = 5 },
  { anchor = "omnivisual", level = 11 },
]
trades = [
  { replaces = "Consummate liar", feature = "consummate-liar", by = ["eyeball-familiar"] },
  { replaces = "mesmerist trick gained at 1st level", feature = "mesmerist-tricks", levels = [1], by = ["eyeball-familiar"] },
  { replaces = "All instances of touch treatment", feature = "touch-treatment", by = ["ocular-occlusion"] },
  { replaces = "Mental potency", feature = "mental-potency", by = ["staring-eye"] },
  { replaces = "Glib lie", feature = "glib-lie", by = ["omnivisual"] },
]
+++

Mesmerists focus their abilities through the eyes, drawing forth their power as the windows to the
mind and soul. Eyebiters take this a step further. An eyebiter's eyes become so infused with psychic
might that they can leave the eyebiter's body and move about on their own.

## Eyeball Familiar (Ex) {#eyeball-familiar}

An eyebiter imbues one of his eyes with limited sentience, so that he can pluck it out and allow it
to move on its own. The eyeball familiar functions similarly to the
[tumor familiar](ref/discovery/tumor-familiar) alchemist discovery (_Pathfinder RPG Ultimate Magic_
17) except as follows. The eyeball familiar does not have [fast healing](ref/umr/fast-healing). The
eyeball familiar doesn't resemble an animal, and its size is Fine for a Medium or smaller eyebiter
(or one size category larger for every size category the eyebiter is larger than Medium). It has a
fly speed of 20 feet (perfect maneuverability) and no physical attacks (though it can still deliver
touch spells once the eyebiter has reached 3rd level). The eyeball has a Strength score of 1, a
Dexterity score of 12, and a Constitution score of 10. It has no set Hit Die, base saves, or skill
ranks of its own, though it uses its master's when a familiar normally would. It doesn't grant its
master any familiar bonus, nor can it ever be an improved familiar.

Whenever the eyebiter's eyeball familiar leaves his body, he is [dazzled](ref/misc/dazzled) until it
returns (if it is destroyed, the eyebiter loses that eye until he gains the effects of a
_[regeneration](ref/spell/regenerate)_). An eyebiter must have at least one eye to use this ability,
and an eyebiter with only one eye is [blinded](ref/misc/blinded) instead of dazzled until his
familiar returns.

This ability replaces consummate liar and the mesmerist trick gained at 1st level.

## Ocular Occlusion (Su) {#ocular-occlusion}

At 3rd level, an eyebiter gains the ability to cloud the sight of others with a melee touch attack.
He can use this ability as a standard action a number of times per day equal to 3 + his Charisma
modifier. A successful Will save negates the effect (DC = 10 + 1/2 the eyebiter's mesmerist level +
his Charisma modifier); this is a mind-affecting ability. If the eyebiter chooses to use an ocular
occlusion of a lower level than the highest-level effect he has gained, he can instead use a
standard action to target a creature within 30 feet with that effect as a ranged touch attack.

### Clouded Vision {#clouded-vision}

At 3rd level, the eyebiter can cause the target to become dazzled for 1 minute and suffer a 20% miss
chance on all attacks the target makes against opponents within 60 feet. Opponents more than 60 feet
away have [total concealment](ref/rule/concealment) from the target.

### Cause or Cure Blindness {#cause-or-cure-blindness}

At 6th level, the eyebiter can blind the target for 1 minute or affect it as per the spells
_[remove blindness](ref/spell/remove-blindness-deafness)_.

### Eyeless Horror {#eyeless-horror}

At 10th level, the eyebiter creates a powerful illusion that causes the target's eyes to appear as
if they have been ripped out, with blood pouring from the sockets. The target is blinded and
[shaken](ref/misc/shaken) for 1 round per the eyebiter's mesmerist level, taking 1d4 points of
nonlethal damage each round. The target can attempt a second Will save when attacked to negate the
shaken effect and the nonlethal damage.

### Spellblight {#spellblight}

At 14th level, the eyebiter can afflict the target with the ebon eyes, the eldritch cataracts, or
the hemoculysis spellblight (_Ultimate Magic_ 95).

This ability replaces all instances of touch treatment.

## Staring Eye (Su) {#staring-eye}

At 5th level, an eyebiter can expend one use of his daily mesmerist tricks to either see through his
eyeball familiar as if it were an _[arcane eye](ref/spell/arcane-eye)_, or to use his hypnotic stare
(including related abilities like painful stare and bold stare), as well as any [gaze](ref/umr/gaze)
attack he possesses (like _[burning gaze](ref/spell/burning-gaze)_ and
_[eyebite](ref/spell/eyebite)_) through his eyeball familiar, as if he were at its location.

This ability replaces mental potency.

## Omnivisual (Ex) {#omnivisual}

At 11th level, an eyebiter's roving eyeball familiar is constantly watching in all directions. As
long as his eyeball familiar is outside his body and near enough to see the same things (such as
being in the same room), the eyebiter gains [all-around vision](ref/umr/all-around-vision) and
cannot be [flanked](ref/rule/flanking).

This ability replaces glib lie.
