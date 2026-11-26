+++
id = "ref/arc-mesmerist/cult-master"
kind = "archetype"
title = "Cult Master"
aon = "ArchetypeDisplay.aspx?FixedName=Mesmerist%20Cult%20Master"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cult_master", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]
[[sources]]
publication = "occult-adventures"
page = "96"

[fields]
kind = "archetype"
features = [
  { anchor = "insidious-personality", level = 1 },
  { anchor = "fanatical-stare", level = 1 },
  { anchor = "cult-tricks", level = 1 },
  { anchor = "false-healing", level = 3 },
  { anchor = "faithful-followers", level = 7 },
  { anchor = "fanatical-devotion", level = 10 },
  { anchor = "masterful-cult-tricks", level = 12 },
  { anchor = "reborn", level = 20 },
]
trades = [
  { replaces = "Consummate liar", feature = "consummate-liar", by = ["insidious-personality"] },
  { replaces = "Painful stare", feature = "painful-stare", by = ["fanatical-stare"] },
  { replaces = "3rd- and 6th-level touch treatments", feature = "touch-treatment", levels = [3, 6], by = ["false-healing"] },
  { replaces = "7th-level bold stare", feature = "bold-stare", levels = [7], by = ["faithful-followers"] },
  { replaces = "10th- and 14th-level touch treatments", feature = "touch-treatment", levels = [10, 14], by = ["fanatical-devotion"] },
  { replaces = "Rule minds", feature = "rule-minds", by = ["reborn"] },
  { alters = "Mesmerist tricks", feature = "mesmerist-tricks", by = ["cult-tricks"] },
  { alters = "Masterful tricks", feature = "masterful-tricks", by = ["masterful-cult-tricks"] },
]
+++

The leaders of some cults are simply charlatans, bathing in the adulation of their followers. Others
believe themselves to be truly in touch with an unknown power, bringing their unique messages to
those willing to follow and obey them.

## Insidious Personality (Ex) {#insidious-personality}

A cult master adds 1/2 his class level (minimum 1) as a bonus on all Diplomacy checks. This ability
replaces consummate liar.

## Fanatical Stare (Su) {#fanatical-stare}

At 1st level, a cult master can turn his gaze on a creature to fill it with fervent belief in the
cult master. The target of the gaze gains a +1 competence bonus on attack rolls and weapon damage
rolls. This bonus increases by 1 for every 6 mesmerist levels the cult master possesses, to a
maximum of +4 at 18th level. Instead of taking the hypnotic stare's penalty on Will saves, the
target gains a bonus of an equal amount on Will saves. The bonuses don't apply to attacks against
the cult master or on saves against the cult master's spells or abilities. The cult master can also
suppress any penalties inflicted by his stare for the target. This ability replaces painful stare.

## Cult Tricks (Su) {#cult-tricks}

The following new tricks can be selected by a cult master. These tricks can be implanted only in a
cohort or follower of the cult master.

### Double {#double}

An illusion makes either the cult master's cohort or one of his followers appear to be him. The cult
master can trigger this trick when he is targeted by an attack, provided he is adjacent to the
subject, to give the attack a 50% miss chance. If the attack misses the cult master, it targets the
subject instead. This is an illusion (glamer) effect.

### Extol {#extol}

A mental compulsion causes a cohort or follower to extol the virtues of the cult master. The cult
master can trigger this trick whenever he attempts a Diplomacy check, as long as he is within 60
feet of the subject. The subject takes the [aid another](ref/rule/aid-another) action on the cult
master's Diplomacy check. If the subject is successful, the cult master gains a +4 bonus on his
check. This is an enchantment (compulsion) effect.

This ability alters mesmerist tricks.

## False Healing (Su) {#false-healing}

At 3rd level, a cult master can provide temporary healing by using his psychic powers to trick the
mind a number of times per day equal to 3 + his Charisma modifier. Using the ability is a standard
action (or a swift action if the cult master uses it on himself), and the cult master must be able
to touch his target. The cult master grants a number of
[temporary hit points](ref/rule/temporary-hit-points) equal to 1d8 + his Charisma modifier to the
target. At 6th level, the cult master can either grant a number of temporary hit points equal to
2d8 + his Charisma modifier to the target or temporarily remove 1d4 points of
[ability damage](ref/rule/ability-damage-drain). A creature can receive the effect of the false
healing only once per day. The temporary hit points or reduction in ability damage lasts a number of
hours equal to the cult master's class level. This ability replaces the 3rd- and 6th-level touch
treatments.

## Faithful Followers (Ex) {#faithful-followers}

At 7th level, a cult master begins to attract followers to his espoused beliefs, thanks to his
magnetic personality. The cult master gains [Leadership](ref/feat/leadership) as a bonus feat. This
ability replaces the 7th-level bold stare.

## Fanatical Devotion (Ex) {#fanatical-devotion}

At 10th level, a cult master has manipulated his cohort and followers into becoming utterly devoted
to him. The cult master no longer takes a penalty to his Leadership score for being aloof or cruel.
Additionally, the DCs of all enchantment spells the cult master casts on his cohort and followers
increase by 4. At 14th level, the cult master no longer takes a penalty to his Leadership score for
any cohorts or followers he has killed or caused to be killed. This ability replaces the 10th- and
14th-level touch treatments.

## Masterful Cult Tricks (Su) {#masterful-cult-tricks}

The following new master tricks can be selected by any cult master of 12th level or higher. These
tricks can be implanted only in a cohort or follower of the cult master.

### Avenge Me {#avenge-me}

The cult master creates a compulsion for one of his followers to avenge him. Whenever the cult
master takes hit point damage from an attack, he can trigger this trick as long as he is within 60
feet of the subject. The subject is immediately affected as if by the _[rage](ref/spell/rage)_ spell
for 1 round per mesmerist level.

### Die for Me {#die-for-me}

The cult master instills within either his cohort or one of his followers the desire to give her
life for him. The cult master can trigger this trick whenever he would take hit point damage from an
attack, spell, or effect and the subject is with 60 feet of him. Half the damage is psychically
transferred to the subject. This is an enchantment (compulsion) effect.

This ability alters masterful tricks.

## Reborn (Su) {#reborn}

At 20th level, a cult master can ensure his own survival upon his death. The cult master can perform
a 1-hour ceremony costing 5,000 gp in rare materials in which he uses his psychic powers to implant
a small portion of his essence into his cohort, who must be a minimum of 17th level. When the cult
master dies, in 7 days the cohort physically and mentally transforms into the cult master as if
_[clone](ref/spell/clone)_ had been cast, except that the cohort's body takes the place of the inert
body. The cult master can't use this ability again until he gains a new cohort of at least 17th
level and performs the necessary ceremony. The cohort can't be brought back to life except through
_[miracle](ref/spell/miracle)_ or _[wish](ref/spell/wish)_. This ability replaces rule minds.
