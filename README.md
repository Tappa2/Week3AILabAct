Christian Tappa
iT-305
Profeclec

1.Explain:Explain in 5-9 sentences why rule-based systems need explicit "override" conditions like this, and what might go wrong if Aliah forgets to code the override check before the time/item check instead of after

Answer:rule-based systems need explicit override conditions because computers only follow code step-by-step and cannot guess human exceptions If we don't code special rules properly the system will just apply standard logic to everyone In our cafeteria kiosk the teacher's pass is supposed to skip the usual item and time limits If Aliah puts the time and item checks first, a student holding a valid pass will still get rejected if they have more than 3 items or less than 10 minutes left. The program would process the standard rules first and deny access before it even checks for the pass this causes a bug where the special privilege is ignored completely Placing override checks at the top of the function ensures priority rules run before standard restrictions

2: Question:What if two rules conflict — EXAMPLE a student has a teacher's pass but the cafeteria is currently closed for cleaning?

Answer:when two rules conflict, we need to follow which one has higher priority the rule cafeteria is closed is more important than the teacher's pass because even if a student or teacher has a pass, the cafeteria is still closed, so no one can buy anything anyway
