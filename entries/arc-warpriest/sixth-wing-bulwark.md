+++
id = "ref/arc-warpriest/sixth-wing-bulwark"
kind = "archetype"
title = "Sixth Wing Bulwark"
aon = "ArchetypeDisplay.aspx?FixedName=Warpriest%20Sixth%20Wing%20Bulwark"
source_ids = ["distant-realms"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sixth_wing_bulwark", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]
[[sources]]
publication = "distant-realms"
page = "32"

[fields]
kind = "archetype"
features = [
  { anchor = "sixth-wing-sworn" },
  { anchor = "focus-shield", level = 1 },
  { anchor = "sacred-shield", level = 1 },
  { anchor = "shield-of-grace", level = 6 },
  { anchor = "sacred-fortification", level = 7 },
  { anchor = "intercession", level = 12 },
  { anchor = "reflexive-fortification", level = 18 },
]
trades = [
  { replaces = "Focus weapon", feature = "focus-weapon", by = ["focus-shield"] },
  { replaces = "Sacred weapon", feature = "sacred-weapon", by = ["sacred-shield"] },
  { replaces = "Bonus feat gained at 6th level", feature = "bonus-feats", levels = [6], by = ["shield-of-grace"] },
  { replaces = "Bonus feat gained at 12th level", feature = "bonus-feats", levels = [12], by = ["intercession"] },
  { replaces = "Bonus feat gained at 18th level", feature = "bonus-feats", levels = [18], by = ["reflexive-fortification"] },
  { alters = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { alters = "Sacred armor", feature = "sacred-armor", by = ["sacred-fortification"] },
]
+++

Many are the followers of Ragathiel who lead in battle. Far fewer, but no less crucial to a
successful campaign, are those who hold the line and defend against the incursion of evil forces.
The Sixth Wing bulwark trains to do just that: fortifying herself and her allies to stand strong in
the face of any opposition, no matter how dire.

## Sixth Wing Sworn {#sixth-wing-sworn}

A Sixth Wing bulwark must be a worshiper of [Ragathiel](ref/faith/ragathiel). If she ever changes
her deity, she loses this archetype, cannot regain it, and becomes a normal warpriest.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A Sixth Wing bulwark gains proficiency in [tower shields](ref/eq-armor/tower-shield).

This alters the warpriest's weapon and armor proficiencies.

## Focus Shield {#focus-shield}

A Sixth Wing bulwark gains [Shield Focus](ref/feat/shield-focus) as a bonus feat.

This replaces focus weapon.

## Sacred Shield (Su) {#sacred-shield}

Dedicated training and divine grace allow a Sixth Wing bulwark to lessen the burden of a shield's
weight. As long as a Sixth Wing bulwark is wielding a shield, she reduces her total armor check
penalty by 1. This reduction improves by 1 for every 5 warpriest levels she has, to a maximum
reduction of 5 at 20th level.

At 4th level, a Sixth Wing bulwark can call upon Ragathiel's might to bless her shield as a swift
action. As long as she is wielding a shield, she gains DR 1/— and fire
[resistance](ref/umr/resistance) 5. For every 4 levels beyond 4th, this DR increases by 1 (to a
maximum of DR 5/— at 20th level) and her fire resistance increases by 5 (becoming
[immunity](ref/umr/immunity) to fire at 20th level). A Sixth Wing bulwark can use this ability a
number of rounds per day equal to her warpriest level; these rounds need not be consecutive.

As a swift action while her shield is benefitting from Ragathiel's blessing (or as part of the
action to activate the blessing), a Sixth Wing bulwark can direct her shield to protect an ally
within 60 feet. The shield sprouts burning wings and flies to defend the ally, providing its shield
bonus, [damage reduction](ref/rule/damage-reduction), and fire resistance to that ally instead of
the Sixth Wing bulwark. Rounds in which she uses her shield in this manner count normally against
the rounds per day in which she can use this ability. As long as she has rounds of sacred shield
remaining, she can recall her shield to her arm as a swift action and regain its benefits. A Sixth
Wing bulwark must maintain one hand free to direct the shield; if she no longer has a hand free or
if the duration of her sacred shield ability ends, the shield drops to the ground and ceases
providing any benefit.

This replaces sacred weapon.

## Shield of Grace (Su) {#shield-of-grace}

At 6th level, when a Sixth Wing bulwark uses her sacred shield to protect an ally, she can deliver
blessings, healing from her fervor ability, and touch spells through the shield to the ally
benefiting from the shield's protection.

This replaces the bonus feat gained at 6th level.

## Sacred Fortification (Su) {#sacred-fortification}

At 7th level, when a Sixth Wing bulwark activates her sacred armor ability, she can expend one use
of fervor to also activate her sacred shield ability.

This alters sacred armor.

## Intercession (Su) {#intercession}

At 12th level, by expending a use of fervor as a swift action, a Sixth Wing bulwark can teleport to
the location of a willing (or unconscious) ally and immediately teleport that ally to her own
previous position, in effect switching places with the ally. A Sixth Wing bulwark must have line of
effect to the target to use this ability.

This replaces the bonus feat gained at 12th level.

## Reflexive Fortification (Su) {#reflexive-fortification}

At 18th level, a Sixth Wing bulwark can use her sacred shield ability as an immediate action when
she is attacked. Alternatively, she can use this ability as an immediate action when an ally within
30 feet is attacked to send her shield to protect that ally. She can use this ability even if she is
surprised.

This replaces the bonus feat gained at 18th level.
